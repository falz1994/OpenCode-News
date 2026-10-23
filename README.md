# reddit-opencode

Scraping y análisis de los subreddits de OpenCode (r/opencode y r/opencodeCLI) vía la API
pública **Arctic Shift** (no requiere ninguna API key).

👉 **Índice de referencia: [`INDEX.md`](INDEX.md)** — matriz modelo × habilidad (quién es bueno en
frontend, backend, planificación, motion graphics, debugging, tests, orquestación…), roles por
presupuesto, precios reales, benchmarks de la comunidad y banderas rojas.

## Por qué existe

En estos subs las preguntas se repiten siempre. El proyecto está montado para responderlas
con datos en vez de con impresiones:

1. **¿Cuáles son las noticias más importantes?** → `informe.py` sección 1
2. **¿Qué modelos salen mejor de precio/calidad en OpenCode Go / Zen?** → `informe.py` sección 2
3. **¿Cuáles son las habilidades y debilidades de cada modelo (sobre todo los flash)
   según las experiencias de la gente?** → `informe.py` sección 3

## Scripts

| Script | Para qué |
|---|---|
| `fetch.py` | Descarga hilos + comentarios de un rango. `--subreddit --after --before --prefix --orphans` |
| `noticias.py` | Scraping **incremental**: detecta el último dato de ese sub y trae solo lo nuevo + resumen |
| `informe.py` | Informe de los 3 ejes (noticias / calidad-precio / modelos) desde los volcados locales |
| `especialidades.py` | Matriz modelo × dominio de tarea (frontend, backend, planning, motion, debug…) |
| `index_datos.py` | Genera la fuente del dashboard: `datos.json` + `datos.js` a partir de `fuente.json` + volcados |
| `go_limites.py` | Scrapea los **límites de uso oficiales de OpenCode Go** → `go_limites.json` (incluye el multiplicador ×plan) |
| `presets.py` | Lee los presets de DSH (`~/.dsh/.agent-presets`) y genera `presets.json` para el frame de presets |
| `audita.py` | Auditoría del dashboard con Chrome headless (CDP): contraste WCAG, desbordes, solapes con el header y geometría |
| `valida_enlaces.py` | Comprueba que cada enlace a un hilo de los titulares apunta a un hilo real |
| `sonda.py` | Medidas puntuales de layout (una celda, un chip, un título) para decidir si algo está mal alineado |
| `captura.py` | Capturas dirigidas: desplaza a un título y guarda el viewport en claro/oscuro y a cualquier ancho |

## Límites de OpenCode Go

`go_limites.py` baja la tabla oficial de <https://opencode.ai/v2/docs/console/go/> y calcula lo que
la gente compara de verdad: **cuánto valor de uso da cada modelo por los $10 del plan**.

| Modelo | Límite/mes (Go) | ×plan | Go Plus | Peticiones/mes |
|---|---|---|:--:|---|---|
| DeepSeek V4.1 Flash | $80 | **x8** | $160 | 173.330 |
| GLM-5.3-Flash · GLM-5.2 · Kimi K2.7 Code · LongCat-2.0 · MiMo-V2.6/V2.5 · MiniMax M3 · Muse Spark 1.2/1.3 | $60 | **x6** | $120-240 | 4.300-226.600 |
| Qwen3.8 Flash · Space Bunny · Hy4 · Gemini 4 Argon Contributor | $30 | x3 | $90-120 | 6.770-27.000 |
| GPT 6 Luna · GPT 5.6 Luna · Claude Haiku 5.5 · Grok 4.7 · Kimi K3 · MiMo-Pro · Step 5 Preview · GLM-5.3 · Qwen3.8 Max | $15 | x1.5 | $60 | 490-21.130 |
| LongCat 2.5 Preview · **Beam** (Free) | ∞ | ∞ | ∞ | ilimitado |

Reglas: 5 h = 20% del límite mensual, semana = 50%, mes = 100%. DeepSeek tiene horas punta
(01:00-04:00 y 06:00-10:00 UTC, L-V). Muse Spark Contributor y Gemini 4 Argon Contributor
**entrenan con tus datos**; Beam Free no entrena pero retiene 30 días.

La tabla es viva: el 16-oct salieron Cat Jam Free, Grok 4.6, Kimi K2.6, MiniMax M2.7 y
Step 5 Preview Free (que reapareció como modelo de pago), y entraron Beam Free y el Step 5 de pago.

Cada ejecución **compara con el scrape anterior** y guarda el diff en `go_limites.json`
(`cambios.nuevos` / `fuera` / `modificados`), que el dashboard muestra como aviso: así se ve de un
vistazo cuándo entra o sale un modelo o cambia un precio.

## Dashboard

- **`index.html`** — matriz modelo × habilidad, **límites oficiales de Go con el multiplicador ×plan**,
  roles por presupuesto, precios, benchmarks, stealth y banderas rojas. Se abre con doble clic
  (usa `datos.js`) o servido por HTTP (recarga `datos.json`).
- **`fuente.json`** — la fuente editable: valoraciones, roles, pegas, los **titulares curados** y las
  tablas curadas. Es lo único que hay que tocar a mano cuando cambie tu criterio.
- **`go_limites.json`** — la otra fuente, scrapeada de la web oficial con `go_limites.py`.
- **`datos.json` / `datos.js`** — salida generada. No editar a mano.

```bash
python3 go_limites.py           # refresca los límites de Go desde la web oficial
python3 index_datos.py          # regenera datos.json/datos.js
python3 -m http.server 8765     # opcional: http://127.0.0.1:8765/index.html
```

Los recuentos de menciones por habilidad y el sentimiento (positivas/negativas) **se calculan
solos** desde los volcados; las valoraciones `+++/++/+/–/✗` son criterio curado en `fuente.json`.

### Noticias, titulares y comentarios

Tres bloques, con tres niveles de curación distintos:

| Bloque | De dónde sale | Cómo se ordena |
|---|---|---|
| **Titulares** | `titulares` en `fuente.json`, escrito a mano | orden curado; cada fila lleva fecha, detalle y enlace a la fuente oficial o al hilo |
| **Noticias recientes** | volcados `hilos-*.json` | *temperatura*: `log10(1 + score + 2·comentarios) / (horas + 6)^0.7` |
| **Comentarios más votados** | comentarios de los volcados | score del comentario, ventana corta (`comentarios_dias`) |

La temperatura existe porque el `score` de Arctic Shift llega con retraso: los hilos de hoy siguen
a 1-2↑ mientras ya tienen 100 comentarios, así que ordenar por score dejaba la sección anclada en
los hilos más viejos de la ventana. Se usan los comentarios del propio volcado (no `num_comments`,
que viene a 0) y, si el score no se ha refrescado, el del mejor comentario como aproximación.

Ajustes en `fuente.json`: `noticias_dias` (ventana, 12), `noticias_top` (14), `comentarios_dias`
(5) y `comentarios_top` (12).

### Criterios de UI

- **Rampa secuencial de un solo tono** (azul) para las valoraciones: más azul = mejor. Se evitó el
  verde doble porque dos verdes parecidos no dejaban distinguir cuál era el mejor.
- **★ en el mejor de cada columna** con recuadro de acento: codificación redundante, no depende del color.
- El **rojo se reserva para `✗` (evitar)**; "sin evidencia" (`–`) es gris neutro. Así "no aplica"
  (p. ej. modelos cloud en la columna local) nunca se lee como "malo".
- Tema claro/oscuro con `prefers-color-scheme` y memoria en `localStorage`.
- Accesibilidad: `caption`, `scope` en cabeceras y celdas, `aria-sort`, ordenación por teclado
  (las cabeceras son `<button>`) y `aria-label` con la valoración y las menciones.

## Presets de DSH

El dashboard incluye el frame **“Presets de DSH: cómo trabaja el agente”** con tres bloques:

1. **Qué es un preset y en qué escenarios funciona** — no es un modelo ni una cuota: es el grafo de
   módulos que se monta al crear la sesión (persona, herramientas, políticas y delegación), y se elige
   antes de crearla.
2. **Una tarjeta por preset** — descripción, *cuándo funciona*, *cuándo evitarlo* y los **rasgos medidos
   del grafo** (bytes del prompt de persona, módulos de herramienta, read-only, watchdog, observador de
   límites, vía de delegación y de qué preset hereda).
3. **Simulación: mandar un mensaje en una sesión nueva** — el mismo mensaje con un preset elegido frente
   a un request normal sin preset, paso a paso: qué se carga, qué se manda al prompt, quién escribe y
   quién verifica. Incluye el orden real de las secciones del system prompt con los bytes medidos.

Todo se genera con `presets.py`, que lee `preset.yml` y resuelve la herencia de `agent.cordis.yml`
(`inherit-composition.js` → `path`), ignorando los módulos `disabled`. Los bytes del `prefix` de la
persona se miden del propio YAML y se contrastan con PyYAML:

```bash
python3 presets.py              # refresca presets.json desde ~/.dsh/.agent-presets
python3 presets.py --verifica   # contrasta la cuenta del prefix contra PyYAML (debe dar 0 fallos)
python3 index_datos.py          # lo mete en datos.json / datos.js
```

- **`PRESETS.md`** — la traza larga, con las citas de los ficheros del harness.

### Revisión visual

```bash
python3 -m http.server 8765 &                                  # el dashboard por HTTP
python3 audita.py --tema oscuro                                # defectos: contraste, desbordes, solapes
python3 captura.py --h2 "Presets de DSH" -o .rev/presets.png    # captura dirigida
```

`audita.py` necesita Chrome y lo arranca con `--no-sandbox` (el helper SUID no está configurado en esta
máquina); solo audita `127.0.0.1`. Las celdas de tabla quedan excluidas del chequeo de desborde porque
llevan `white-space: nowrap` a propósito.

## Uso

```bash
# volcado histórico de un sub (un mes)
python3 fetch.py --subreddit opencodeCLI --after 2026-09-13 --before 2026-10-14 \
                 --prefix hilos-opencodeCLI-ultimo-mes --orphans

# "¿qué hay nuevo?" -> scraping del delta desde el último volcado
python3 noticias.py --subreddit opencodeCLI

# informe de los 3 ejes sobre los volcados que ya tienes
python3 informe.py --subreddit opencodeCLI --dias 30 --top 12 --citas 2

# ciclo completo de actualización del dashboard
python3 noticias.py --subreddit opencode && python3 noticias.py --subreddit opencodeCLI
python3 go_limites.py && python3 index_datos.py
```

## Ficheros de datos

- `hilos-<sub>-*.json` → hilos con comentarios anidados (fuente de verdad para los análisis)
- `hilos-<sub>-*.md` → el mismo volcado en Markdown legible
- `hilos-<sub>-*-comentarios-huerfanos.json` → comentarios nuevos publicados en hilos
  anteriores al rango (sin esto se perderían: en el volcado de un mes eran ~900)
- `*.log` → trazas de cada descarga

## Notas

- Reddit bloquea su `.json` directo (HTTP 403), por eso se usa Arctic Shift.
- Los volcados se identifican por `meta.subreddit`: cada sub lleva su propio
  "último dato conocido", así que `noticias.py` no mezcla subreddits.
- Los `.json`/`.md` contienen **texto público de Reddit con nombres de usuario de terceros**:
  no son secretos, pero conviene no redistribuirlos sin filtrar.
- El código no usa credenciales de ningún tipo y no lee variables de entorno.
