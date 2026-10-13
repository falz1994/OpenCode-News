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

## Dashboard

- **`index.html`** — matriz modelo × habilidad, roles por presupuesto, precios, benchmarks, stealth y
  banderas rojas. Se abre con doble clic (usa `datos.js`) o servido por HTTP (recarga `datos.json`).
- **`fuente.json`** — la fuente editable: valoraciones, roles, pegas y las tablas curadas.
  Es lo único que hay que tocar a mano cuando cambie tu criterio.
- **`datos.json` / `datos.js`** — salida generada. No editar a mano.

```bash
python3 index_datos.py          # regenera datos.json/datos.js
python3 -m http.server 8765     # opcional: http://127.0.0.1:8765/index.html
```

Los recuentos de menciones por habilidad y el sentimiento (positivas/negativas) **se calculan
solos** desde los volcados; las valoraciones `+++/++/+/–/✗` son criterio curado en `fuente.json`.

## Uso

```bash
# volcado histórico de un sub (un mes)
python3 fetch.py --subreddit opencodeCLI --after 2026-09-13 --before 2026-10-14 \
                 --prefix hilos-opencodeCLI-ultimo-mes --orphans

# "¿qué hay nuevo?" -> scraping del delta desde el último volcado
python3 noticias.py --subreddit opencodeCLI

# informe de los 3 ejes sobre los volcados que ya tienes
python3 informe.py --subreddit opencodeCLI --dias 30 --top 12 --citas 2
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
