# Simulación: qué pasa al mandar un mensaje con un preset seleccionado

Antes de entrar en la anatomía de un preset, aquí va la traza de lo que ocurre **de verdad** cuando
abres una sesión nueva, mandas un mensaje y tienes un preset elegido — comparado con un request
normal, sin preset, solo con el contexto y una pregunta.

Fuentes de esta traza: los propios ficheros de `~/.dsh/.agent-presets/`
(`preset.yml` + `agent.cordis.yml` + plugins) y la documentación del harness.
El frame **“Presets de DSH”** del dashboard (`index.html`) resume cada preset; esto es el paso a paso.

---

## A) Sesión nueva **con preset** (ejemplo: `Orquestador`)

### 0. Antes de crear la sesión
Eliges el preset en Ajustes. El selector lee `preset.yml` de cada carpeta de
`~/.dsh/.agent-presets/`, que solo aporta metadatos: `name`, `description` y `order`
(el Orquestador no declara `order`; HyperFrames Educativo es 1 y el Orquestador Educativo es 2).

> Aquí no se carga nada de código todavía: es solo la etiqueta que decides.

### 1. Se compone el grafo de módulos (`agent.cordis.yml`)
Al arrancar la sesión, el harness instancia los módulos del preset, en este orden de bloques:

| Módulo | Qué aporta | Dato real del preset Orquestador |
|---|---|---|
| `persona` (`@deepseek-ai/dsh-persona`) | El system prompt propio del preset | `prefix` de **13.094 caracteres** + `suffix` “Your working directory is `{{cwd}}`” |
| `agent-instructions` | Instrucciones del proyecto (AGENTS.md y similares) | `maxBytes: 65536` (64 kB) |
| `orchestrator-readonly-policy-v2.js` | Fija la sesión en **read-only** al arrancar | Plugin del preset |
| `orchestrator-job-watchdog.js` | Vigila los jobs hijos por señales de vida reales | Plugin del preset |
| `omniroute-limit-observer.js` | Registra límites y pone modelos en cuarentena | Plugin del preset |
| `orchestrator-spawn-provider.js` | Aporta el spawn del hijo in-process | Plugin del preset |
| herramientas | 12 módulos (`bash`/`pwsh`, `fs`, `fs-search`, `jobs`, `skill`, `goal`, `ask-user`, `todo`, `web`, `present`, …) | Contadas del `agent.cordis.yml` |
| grupos | 3 grupos `cordis:group` (planning, compaction, **delegation**) | La delegación vive en un grupo aislado |

Variables: `{{model}}` y `{{cwd}}` se resuelven del route y del workspace de la sesión.
**Ninguna otra variable puede aparecer en la persona o el ensamblado del prompt falla.**

### 2. Mandas el mensaje
El prompt que ve el modelo se ensambla así:

```
persona del preset (prefix + suffix con {{model}} y {{cwd}})
+ instrucciones del proyecto (hasta 64 kB)
+ catálogo de skills disponibles
+ contexto de entorno (workspace, fecha)
+ historial de la sesión
+ TU MENSAJE
```

Dos cosas que la gente asume mal y no ocurren:

- **Tus ficheros no viajan dentro del prompt.** Solo entran si el modelo llama a una herramienta
  (`read`, `glob`, `grep`, `bash`). El prompt es instrucciones + conversación.
- **El preset no elige el modelo.** El modelo lo elige la sesión; el preset decide *cómo* trabaja.

### 3. La raíz queda en read-only
El plugin de política fija la sesión en `read-only` al arrancar: cualquier `write`, `edit` o `bash`
que produzca archivos **se rechaza en el sandbox**. No es un bug ni algo que esquivar: es la garantía
de que todo lo pesado sale de la raíz. (Los hijos in-process están exentos: comparten sesión y
workspace, y son los únicos que escriben.)

### 4. Delegación (si el trabajo es pesado)
El root llama a `omniroute_code` — **una sola vía**, eliges la herramienta, no el modelo:

1. El hijo arranca con **sesión nueva y prompt propio**: **no ve tu conversación**. Si no le pasas
   rutas absolutas, el contrato esperado y el comando de verificación, trabaja a ciegas.
2. El router local decide el carril con failover propio:
   `big-pickle` → `longcat-2.5` (OpenCode/Zen vía `ocwrap`) → OpenRouter Cohere →
   `nex-n2.5-pro:free` → Gemini Flash Lite (×2 cuentas).
3. El razonamiento `max` **solo** se inyecta si el combo ya resolvió a Gemini; nunca se manda a
   OpenCode/OpenRouter.
4. Límites prácticos del router: 60 req/min, 6 concurrentes, 350 ms entre requests → se lanza en
   lotes de 2-3.

### 5. Vigilancia mientras corre
- **Watchdog**: aviso a los **20 min** de silencio total (no mata), **kill a los 45 min** de silencio
  total o si el job pasa de **75 min** de runtime. La evidencia queda en
  `<cwd>/.dsh-tmp/watchdog-stalls.jsonl`. Un `job_output` que responde “(no new output)” **no**
  significa que el hijo esté colgado.
- **Observador de límites**: el modelo que da su primer error entra en **cuarentena 5 horas**;
  no se reintenta, se usa el siguiente escalón sano.

### 6. Verificación (la hace la raíz, no el hijo)
El hijo **produce y renderiza** el snapshot; el root lee el `contact-sheet.jpg` con `read_image` y
juzga con criterios concretos (texto solapado, contraste, encuadre). Renderizar no es ver: el hijo
genera el PNG pero no lo mira.

### 7. Cierre
Síntesis para el usuario: qué se delegó, con qué evidencia, si hubo failover y el **ratio** de
trabajo propio (`bash`/`read`) contra delegado.

---

## B) Request normal: solo contexto y una pregunta (sin preset)

| Paso | Qué pasa |
|---|---|
| 0 | No eliges preset: se usa el **perfil por defecto** del harness. El preset no “añade” nada; cuando existe, *shadowea* la persona por defecto |
| 1 | Se cargan los módulos base: persona por defecto, instrucciones del proyecto, herramientas base y skills. **Sin** plugins de política, sin watchdog, sin observador de límites y sin el grupo de delegación con router |
| 2 | Prompt = persona base + instrucciones + historial + tu pregunta. Igual que antes: **tus ficheros no van dentro**, se leen si el modelo llama a una herramienta |
| 3 | El modelo principal **escribe directamente**: `write`, `edit` y `bash` van al sandbox del workspace. No hay pin read-only ni delegación forzada |
| 4 | **Una sola llamada** al modelo de la sesión: sin router, sin failover y sin cuarentenas. La cuota que se consume es la de ese modelo |
| 5 | La verificación la haces tú (o el propio modelo en la misma sesión), sin watchdog ni contacto con hijos |

---

## C) Comparación directa

| Dimensión | Con preset `Orquestador` | Sin preset (perfil por defecto) |
|---|---|---|
| System prompt | Persona propia (13 kB) que shadowea la del deployment | Persona por defecto |
| Instrucciones de proyecto | Sí, con tope de 64 kB | Sí (las del perfil base) |
| Herramientas | 12, con shell solo para leer/verificar | Las base |
| Escritura de la raíz | **Bloqueada** (read-only forzado) | Permitida en el workspace |
| Delegación | Obligatoria para el trabajo pesado, a un hijo in-process | No existe: el modelo hace y escribe |
| Router / failover | Combo `code` con failover y cuarentena 5 h | No hay |
| Vigilancia de jobs | Watchdog (aviso 20 min, kill 45/75 min) | No hay |
| Verificación | La raíz lee evidencia visual y decide | La misma sesión |
| Coste por paso | Prompt largo + ida y vuelta al hijo | Una llamada directa |
| Cuándo conviene | Trabajo pesado, multi-archivo, cuota escasa, quieres que la raíz no toque nada | Preguntas, lecturas y cambios pequeños |

---

## D) Lo que un preset **no** hace

- No cambia el modelo de la sesión ni la cuota.
- No mete tus archivos en el prompt: eso lo decide el modelo llamando a herramientas.
- No comparte tu conversación con los hijos: cada hijo recibe un prompt nuevo y autocontenido.
- No sobrevive a la sesión: se aplica al crearla, no se puede “cambiar a mitad”.

---

_Siguiente paso (pendiente): **anatomía de un preset** — estructura de `preset.yml` y
`agent.cordis.yml`, herencia con `inherit-composition.js` + `patches`, y cómo escribir uno desde cero._
