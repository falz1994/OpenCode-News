# FACTCHECK — frame «Presets de DSH» del dashboard

Registro de verificación de las afirmaciones numéricas y estructurales que muestra el bloque
**Presets de DSH: cómo trabaja el agente** de `index.html`, incluida la simulación «mandar un
mensaje en una sesión nueva».

Fuentes de verdad, en este orden:

1. Los ficheros de preset instalados: `~/.dsh/.agent-presets/<preset>/{preset.yml,agent.cordis.yml}`
   y las bases que resuelve `inherit-composition.js` (`path:` + `patches`).
2. Los presets que trae el paquete:
   `~/.npm-global/lib/node_modules/@deepseek-ai/dsh/node_modules/@deepseek-ai/dsh-agent-presets/presets/`
   (`standard`, `minimal`, `ptc`, `cordis`).
3. El **system prompt real** de dos sesiones del disco, leído del primer `system/message` no vacío.
4. El código que lo ensambla: `dsh-system-prompt` (`renderPrompt`), `dsh-agent-presets`
   (roster y default) y `dsh-web-app/cordis.patch.yml` (`agent-presets.default: standard`).

Reproducir la medición del prompt:

```bash
zstd -dc -- ~/.dsh/sessions/--home-devni-imagen-reddit-opencode--/<sesion>/session.v3.jsonl.zstd \
  | python3 scripts/mide_prompt.py
python3 presets.py --verifica     # contrasta el desglose declarado contra las dos sesiones
```

---

## A. Defectos encontrados y corregidos

| # | Afirmación / elemento | Veredicto | Evidencia | Fecha | Cambio aplicado |
|---|---|---|---|---|---|
| A1 | La columna «Con un preset elegido» se titulaba `hyperframes-educativo`, pero el texto del paso 1 describía otro preset (4 plugins, 12 herramientas, 3 grupos) | **Falso** — el generador construía la simulación con `por_id[PRESET_ORQUESTADOR]` | `presets.py` llamaba `build_simulacion(por_id["orchestrator"], …)` mientras `MEDICION["con_preset"]["preset"]` dice `hyperframes-educativo`. `rasgos` del educativo directo: `plugins=0 herramientas=11 grupos=2` | 2026-10-15 | La simulación se construye con `PRESET_SIMULADO = "hyperframes-educativo"`, el mismo que se midió. Si no está instalado, no se genera la simulación y se avisa |
| A2 | La sección `preset:` del prompt medía «22.026 B» | **Impreciso** — eran 22.024 B de texto; los 2 B de más eran el separador `\n\n` contado dentro de la sección | Medición por bytes sobre la sesión `session-6408e2f7-…`: 48 + 6.565 + 22.024 + 61 = 28.698 B, + 3 separadores de 2 B = 28.704 B = total real | 2026-10-15 | `MEDICION` declara 22.024 B. `presets.py --verifica` comprueba que las secciones sumen el total menos los separadores |
| A3 | La sección `preset:` se presentaba como una sección suelta | **Incompleto** — es **compuesta**: la extensión registra orden 100 y las secciones de los módulos del preset caen en el mismo tramo | En la sesión medida, el tramo 100 contiene la extensión (16.789 B), `file-reference` (345 B) y la guía de sus 11 herramientas (4.890 B) | 2026-10-15 | El paso 2 explica la composición y muestra el desglose 16.789 + 5.235 = 22.024 |
| A4 | `harness:source` (356 B) y `web-surface` (995 B) declarados con esos bytes | **Impreciso** — 358 B y 995 B; los 356 B eran el texto sin su separador | Medición por bytes: `i_web - i_src` = 358 (356 + 2 de separador), `i_suf - 2 - i_web` = 995 | 2026-10-15 | `MEDICION` y `ASSEMBLY` declaran 358 y 995 |
| A5 | `file-reference` declarado con 343 B | **Impreciso** — 343 B es el texto del primer párrafo; el tramo mide 345 B contando su separador | `i_tools - i_fr` = 345 en las dos sesiones | 2026-10-15 | `MEDICION` y `ASSEMBLY` declaran 345. Convención: **cada tramo incluye el separador que lo une al siguiente**, así los tramos suman exactamente el total |
| A6 | Guía de herramientas del default: «18 secciones … 6.723 B» | **Impreciso en el conteo** — 6.723 B es correcto, pero son **15 secciones de herramienta**, no 18 | `b[i_fr:i_src].split(b"\n\n")` da 15 bloques de herramienta no vacíos (+1 vacío por el separador final); la guía completa tiene 18 bloques con los tres fijos | 2026-10-15 | El texto describe los tramos (345 + 5.025 + 358 + 995) y dice «15 secciones de herramienta» |
| A7 | Tabla «Módulos que se montan»: el default con **13 módulos de herramienta** (incluía `subagent-control`, `subagent`, `workflow`, `ralph`) | **Falso** — el preset `standard` monta **11** módulos; esas cuatro filas viven en el grupo de delegación, no son módulos de herramienta | `rasgos([presets/standard/agent.cordis.yml])` → 11 herramientas, 2 grupos, delegación `subagent` | 2026-10-15 | La tabla lee el `agent.cordis.yml` real de `standard`; se eliminó la lista escrita a mano (`HERRAMIENTAS_BASE`, conservada solo como referencia) |
| A8 | Fila «persona» del default: texto y bytes escritos a mano | **Incompleto** — el preset `standard` **sí** declara su persona; se leía de una constante | `presets/standard/agent.cordis.yml` → `prefix: >- You are a coding agent powered by the {{model}} model.` (64 B resueltos) | 2026-10-15 | Se lee del fichero y se resuelven `{{model}}` y `{{cwd}}` |
| A9 | Columna «bytes» de «Orden posible de las secciones» **vacía en las 9 filas** | **Falso** — un hueco no se distingue de un cero | El renderizador hacía `el("div",{class:"bytes"}, "")` y `secciones_prompt()` nunca llegaba a `orden_posible` (se pasaba `ASSEMBLY` crudo) | 2026-10-15 | `orden_posible` usa `secciones_prompt()`; cada fila muestra «con preset N B» / «sin preset N B» y `—` cuando la sección no existe |
| A10 | Divisores de la grilla de simulación desalineados entre columnas | **Falso** — defecto visual | Con `align-items:start`, las celdas de una misma fila medían 55 px y 75 px: el borde superior de la celda corta terminaba 20 px antes (pasos 1, 2, 3 y 4) | 2026-10-15 | `.sim .celda{align-self:stretch}`: las dos celdas de la fila miden lo mismo y el divisor cae a la misma altura |
| A11 | Formato de miles inconsistente: `6.565 B` junto a `6,902 B` y `6902 bytes` | **Falso** — la misma cifra con tres formatos | `toLocaleString("es-ES")` del navegador no agrupa a 4 dígitos; además un `.replace(",", ".")` global sobre la frase convertía «Después, la sección» en «Después. la sección» | 2026-10-15 | Un solo formateador (`conMiles`/`bBytes`) en el bloque de presets; en Python, el helper `n()`. Medición en navegador: 0 formatos inconsistentes |
| A12 | `presets.json` no se regeneraba tras editar el preset, y el frame mostraba a la vez el valor vivo (6,5 kB) y el de la sesión (6.565 B) | **Riesgo de contradicción** | `agent.cordis.yml` del preset educativo se editó el 2026-10-15 00:16; el fichero vivo mide 6.528 B mientras la sesión medida (11 oct) tenía 6.565 B | 2026-10-15 | La fila declara las dos cifras y a qué pertenece cada una: «6.474 caracteres … (6.528 B en el fichero de ahora; 6.565 B en la sesión medida)» |

## B. Afirmaciones verificadas como correctas

| Afirmación | Veredicto | Evidencia | Fecha |
|---|---|---|---|
| El roster tiene un default y es `standard` | **Correcto** | `dsh-web-app/cordis.patch.yml`: `- id: agent-presets / config: default: standard` | 2026-10-15 |
| Una sesión siempre se compone desde un preset; elegir «Standard» a mano equivale a no elegir nada | **Correcto** | `dsh-agent-presets/README.md`: «Every session names a preset — explicitly or through the configured default — and is composed from it»; el valor se lee al crear la sesión | 2026-10-15 |
| System prompt medido con el preset: **28.704 B** | **Correcto** | `session-6408e2f7-…`: 28.704 B | 2026-10-15 |
| System prompt medido con el default: **6.902 B** | **Correcto** | `session-d26f77b4-…`: 6.902 B | 2026-10-15 |
| `harness:identity` = 48 B y es igual en los dos casos | **Correcto** | `"You are an AI agent powered by DeepSeek Harness."` = 48 B en las dos sesiones | 2026-10-15 |
| Persona del default = 64 B | **Correcto** | `"You are a coding agent powered by the deepseek-v4.1-flash model."` = 64 B | 2026-10-15 |
| `deployment:persona-suffix` = 61 B | **Correcto** | `"Your working directory is /home/devni/imagen/reddit-opencode."` = 61 B | 2026-10-15 |
| Guía de herramientas del default = 6.723 B | **Correcto** | 345 + 5.025 + 358 + 995 = 6.723 B | 2026-10-15 |
| Las secciones se unen con `\n\n` y las vacías se descartan | **Correcto** | `dsh-system-prompt/lib/index.js`: `renderPrompt` = `map(interpolate).filter(t => t.length > 0).join("\n\n")` | 2026-10-15 |
| La persona del preset ocupa el mismo slot que la del deployment (no se suma) | **Correcto** | `dsh-persona` publica `deployment:persona-prefix`; la composición del preset la sombrea | 2026-10-15 |
| `hyperframes-educativo` vacía su grupo de delegación | **Correcto** | `agent.cordis.yml` del preset: `patches: - id: delegation / config: []` | 2026-10-15 |
| Reparto: 34 + 32 + 14 = 80 sesiones | **Correcto** | Cabecera `agentPreset` y evento `agent-preset/selected` de las 80 sesiones más recientes del disco | 2026-10-15 |
| Las instrucciones del proyecto entran como mensaje aparte, con tope de 64 kB | **Correcto** | `dsh-agent-instructions`: `maxBytes: 65536` en los dos presets | 2026-10-15 |
| Los ficheros del usuario no viajan dentro del prompt | **Correcto** | Solo entran por llamada a herramienta (`read`, `glob`, `grep`, `bash`); el prompt es instrucciones + conversación | 2026-10-15 |

## C. No verificado / fuera de alcance

| Punto | Estado |
|---|---|
| Bytes exactos del bloque «Current runtime context» | **No medido.** El frame lo declara como «no medido: workspace, fecha y textos de política» |
| Bytes del catálogo de skills | **No medido.** Depende de las skills disponibles en cada sesión |
| Tamaño del historial de la conversación | **No medido.** Depende de la conversación |
| El default del roster en otros perfiles (`headless`) | **No verificado.** Solo se comprobó el perfil `web`, que es el que sirve este dashboard |
| «Standard Pro» | **No existe** en esta instalación. Los presets de fábrica del paquete son `standard`, `minimal`, `ptc` y `cordis`; los de usuario, `hyperframes-educativo`, `hyperframes-orquestador-educativo` y `orchestrator` |

## D. Cómo se comprueba

```bash
python3 scripts/mide_prompt.py < <(zstd -dc -- <sesion>/session.v3.jsonl.zstd)  # desglose por bytes
python3 presets.py --verifica    # prefix vs PyYAML + desglose vs las dos sesiones reales
python3 presets.py               # regenera presets.json
python3 index_datos.py           # lo mete en datos.json / datos.js
python3 audita.py                # desbordes, contraste y solapes
python3 captura.py --texto "Simulación" -o .rev/sim-final.png --alto 1150 --offset 130
```
