# Simulación: qué pasa al mandar un mensaje en una sesión nueva

Antes de entrar en la anatomía de un preset, aquí va la traza de lo que ocurre **de verdad** cuando
abres una sesión nueva, mandas un mensaje y tienes un preset elegido — comparado con un request
normal, sin elegir nada, solo con el contexto y una pregunta.

El frame **“Presets de DSH”** del dashboard (`index.html`) trae la misma simulación en formato visual;
esto es el texto largo con las citas.

## Fuentes y método

- Los ficheros de los presets: `~/.dsh/.agent-presets/<preset>/preset.yml` y `agent.cordis.yml`
  (más sus bases heredadas vía `inherit-composition.js`).
- Los paquetes del harness que ensamblan el prompt: `dsh-system-prompt` (`renderPrompt`,
  `SECTION_ORDERS`), `dsh-agent-loop` (dónde entra el system prompt en la sesión),
  `dsh-agent-instructions` (el baseline de AGENTS.md), `dsh-agent-presets` (el roster y su default)
  y `dsh-web-app/cordis.patch.yml` (`agent-presets.default: standard`).
- **Los bytes del system prompt se midieron**, no se estimaron: se leyó el primer `system/message`
  de dos sesiones reales del disco. Para repetirlo:

```bash
zstd -dc -- ~/.dsh/sessions/<workspace>/<sesion>/session.v3.jsonl.zstd | python3 -c "
import sys, json
for l in sys.stdin:
    e = json.loads(l)
    if e.get('type') == 'system/message':
        t = ''.join(c.get('text','') for c in e['data']['message']['content'])
        if t.strip():
            print(len(t.encode()), 'bytes'); print(t); break"
```

- Los bytes del `prefix` de la persona salen del bloque escalar del YAML, con el sangrado del bloque
  descontado. `python3 presets.py --verifica` contrasta esa cuenta contra PyYAML sobre cada preset
  instalado (los tres dan `0` de diferencia). Lo que no se midió se declara **“no medido”**.

---

## 0) Qué es un preset y en qué escenarios funciona

Un preset es un **grafo de módulos** que se monta al crear la sesión. Decide cuatro cosas:

1. **La persona** — el texto que abre el system prompt (`deployment:persona-prefix`).
2. **Qué herramientas existen** — cada módulo `@deepseek-ai/dsh-tool-*` montado aporta su herramienta
   y su sección de guía en el prompt.
3. **Qué políticas se imponen** — por ejemplo un plugin que fija la sesión en `read-only` al arrancar.
4. **Si el trabajo pesado se delega** — o lo hace el modelo principal con sus propias manos.

En qué escenarios funciona, en una frase: **por la forma del trabajo, no por el tema**.

| Forma del trabajo | Qué conviene | Por qué |
|---|---|---|
| Preguntas, lecturas, cambios de una línea | **No elegir nada** (se usa el default del roster) | Una sola llamada, sin ida y vuelta ni prompt largo |
| Pieza corta o mediana que querés cerrar de una tirada | Preset **directo** (p. ej. HyperFrames Educativo) | El modelo de la sesión produce y verifica; no depende del router |
| Trabajo pesado, multi-archivo, muchas iteraciones | Preset que **delega** (Orquestador) | El hijo produce y la raíz queda read-only: la cuota del principal no se quema produciendo |
| Cuota del modelo principal escasa | Preset que **delega** | El peso se reparte con el router y su failover |

Tres cosas que un preset **no** hace: no cambia el modelo ni la cuota, no mete tus archivos dentro del
prompt (eso lo decide el modelo llamando a herramientas) y no se puede cambiar a mitad de sesión.

---

## 1) El punto que casi nadie tiene claro: **no existe “sin composición”**

Una sesión **siempre** se compone desde un preset. Si no elegís ninguno, el roster aplica su default
(`agent-presets.default: standard` en el perfil web) y se monta el preset `standard` que trae el propio
paquete `dsh-agent-presets`. Consecuencias:

- Elegir **«Standard» a mano** da exactamente la misma composición que no elegir nada.
- La comparación útil no es «con preset / sin preset», sino **«con ESTE preset / con el default»**.
- Un preset **no se suma** al default: su composición **lo reemplaza**.

Reparto observado en las 80 sesiones más recientes del disco (cabecera `agentPreset` + evento
`agent-preset/selected`):

| Preset | Sesiones |
|---|---|
| `standard` (default del roster; incluye las que no eligieron nada) | 34 |
| `hyperframes-orquestador-educativo` | 32 |
| `orchestrator` | 14 |

---

## 2) Las dos trazas, medidas

### A) Con un preset elegido — `hyperframes-educativo`

Sesión medida: `~/.dsh/sessions/--home-devni-imagen-reddit-opencode--/session-6408e2f7-…`
(cwd `/home/devni/imagen/reddit-opencode`). **System prompt: 28.704 bytes.**

| orden | sección | bytes | qué es |
|---:|---|---:|---|
| -1000 | `harness:identity` | 48 | `You are an AI agent powered by DeepSeek Harness.` |
| 0 | `deployment:persona-prefix` | 6.565 | el `prefix` del preset, con `{{model}}` y `{{cwd}}` resueltos |
| 100 | `preset:hyperframes-educativo` | 22.026 | sección que aporta `hyperframes-prompt-extension.js` |
| 10200 | `deployment:persona-suffix` | 61 | `Your working directory is /home/devni/imagen/reddit-opencode.` |

La suma da 28.700 B y el prompt mide 28.704 B: los 4 B de diferencia son los separadores entre
secciones. **La persona del preset no aparece como sección nueva: ocupa el slot
`deployment:persona-prefix` y reemplaza a la del default.**

### B) Sin elegir preset — se monta `standard`

Sesión medida: `~/.dsh/sessions/--home-devni-imagen-reddit-opencode--/session-d26f77b4-…`
(mismo cwd). **System prompt: 6.902 bytes.**

| orden | sección | bytes | qué es |
|---:|---|---:|---|
| -1000 | `harness:identity` | 48 | la misma línea de siempre |
| 0 | `deployment:persona-prefix` | 64 | `You are a coding agent powered by the deepseek-v4.1-flash model.` |
| 1000 | guía de herramientas (`tool:*`, `harness:source`, `web-surface`) | 6.723 | 18 secciones: `read`, `write`, `edit`, `glob`, `grep`, `bash`, `jobs`, `web_search`, `web_fetch`, `goal`, `workflow`, `ralph`, `subagent`, `subagent_fork`, `present`, checkout, GUI… |
| 10200 | `deployment:persona-suffix` | 61 | el mismo `cwd` |

La suma da 6.896 B y el prompt mide 6.902 B. **En este prompt la pieza más grande no es la persona
(64 B) sino la guía de herramientas (6.723 B).**

### C) Lo que va aparte, en los dos casos

| Pieza | Cómo entra | Tamaño |
|---|---|---|
| Instrucciones del proyecto (AGENTS.md / CLAUDE.md) | mensaje de rol usuario, baseline durable del primer request | hasta 64 kB (`maxBytes: 65536`) |
| Contexto de entorno | snapshot «Current runtime context» (workspace, fecha, política de sandbox y de aprobación) | no medido |
| Catálogo de skills | secciones del system prompt | según las skills disponibles |
| Historial de la sesión + tu mensaje | mensajes de rol usuario | según la conversación |

**Tus ficheros no viajan dentro del prompt.** Solo entran si el modelo llama a una herramienta
(`read`, `glob`, `grep`, `bash`). El prompt es instrucciones + conversación.

---

## 3) La traza paso a paso

| # | Paso | Con un preset elegido | Sin elegir preset |
|---:|---|---|---|
| 0 | Elegís el preset (o no) | El selector lee `preset.yml` de cada carpeta: solo metadatos (nombre, descripción, orden). No se carga código todavía | No elegís nada: se aplica el default del roster (`standard`) |
| 1 | Se compone el grafo | Se montan los módulos de `agent.cordis.yml`: persona, plugins, módulos de herramienta y grupos | Se montan los módulos de `standard`: persona, 13 módulos de herramienta, 3 grupos, delegación con `subagent`/`subagent_fork`/`workflow`/`ralph`. Sin plugins de política. (`hyperframes-educativo` monta 11: vacía el grupo de delegación) |
| 2 | Se ensambla el system prompt | 28.704 B medidos (persona + extensión del preset) | 6.902 B medidos (persona de 64 B + guía de herramientas de 6.723 B) |
| 3 | Mandás el mensaje | system prompt + instrucciones del proyecto + contexto de entorno + historial + TU MENSAJE | la misma forma, con el otro system prompt |
| 4 | Primer request | Se añaden los dos mensajes aparte (AGENTS.md y contexto de entorno) | los mismos dos mensajes: no dependen del preset |
| 5 | Quién escribe | Según el preset: `Orquestador` deja la raíz en **read-only** y produce un hijo in-process (`omniroute_code`); `HyperFrames Educativo` vacía la delegación y produce el modelo principal | El modelo principal escribe directamente: `write`, `edit` y `bash` van al sandbox del workspace |
| 6 | Cuota y verificación | Según el preset: watchdog y observador de límites si los monta; la raíz verifica leyendo evidencia | Una sola llamada, sin router ni failover ni cuarentenas; la verificación la hacés vos |

### El caso `Orquestador`, con sus números

| Módulo | Qué aporta | Dato real |
|---|---|---|
| `persona` | El system prompt propio | `prefix` de **12.764 caracteres / 12.964 bytes** + `suffix` «Your working directory is `{{cwd}}`» |
| `agent-instructions` | Instrucciones del proyecto | `maxBytes: 65536` (64 kB) |
| `orchestrator-readonly-policy-v2.js` | Fija la sesión en read-only al arrancar y lo reafirma en cada pre-step | plugin del preset |
| `orchestrator-job-watchdog.js` | Vigila los jobs hijos por señales de vida reales | plugin del preset |
| `omniroute-limit-observer.js` | Registra límites y pone el modelo que falla en cuarentena | plugin del preset |
| `orchestrator-spawn-provider.js` | Aporta el spawn del hijo in-process | plugin del preset |
| herramientas | 12 módulos (incluye `subagent` para el spawn) | contados del `agent.cordis.yml` |
| grupos | 3 grupos `cordis:group` (planning, compaction, **delegation**) | la delegación vive en un grupo aislado |

La única vía de producción es `omniroute_code`: el hijo arranca con **sesión nueva y prompt propio**,
**no ve tu conversación**, y el failover entre carriles lo hace el router
(`big-pickle` → `longcat-2.5` → OpenRouter Cohere → `nex-n2.5-pro:free` → Gemini Flash Lite ×2).
El razonamiento `max` solo se inyecta si el combo ya resolvió a Gemini.

---

## 4) Lo que un preset **no** hace

- No cambia el modelo de la sesión ni la cuota: el modelo lo elige la sesión, el preset decide *cómo* trabaja.
- No mete tus archivos en el prompt: eso lo decide el modelo llamando a herramientas.
- No se suma al prompt del default: lo **reemplaza**.
- No comparte tu conversación con los hijos: cada hijo recibe un prompt nuevo y autocontenido.
- No sobrevive a la sesión: se aplica al crearla, no se puede “cambiar a mitad”.

---

## 5) Cómo se comprueba

```bash
python3 presets.py --verifica   # bytes del prefix: regex propia vs PyYAML (0 fallos = coincide)
python3 presets.py              # regenera presets.json con la simulación
python3 index_datos.py          # la mete en datos.json / datos.js del dashboard
```

---

_Siguiente paso (pendiente): **anatomía de un preset** — estructura de `preset.yml` y
`agent.cordis.yml`, herencia con `inherit-composition.js` + `patches`, y cómo escribir uno desde cero._
