# INDEX — Modelos de OpenCode por habilidad

Índice de referencia del proyecto. Todo sale del scraping de **r/opencode + r/opencodeCLI**
(2.185 hilos, 20.592 unidades de texto, 8-sep → 13-oct-2026).

## Índice

1. [Matriz principal: modelo × habilidad](#1-matriz-principal-modelo--habilidad)
2. [Leyenda y criterio](#2-leyenda-y-criterio)
3. [Tabla A — Rol ideal, pega principal y sentimiento](#3-tabla-a--rol-ideal-pega-principal-y-sentimiento)
4. [Tabla B — Stack recomendado según presupuesto](#4-tabla-b--stack-recomendado-según-presupuesto)
5. [Tabla C — Precio real y valor en Go/Zen](#5-tabla-c--precio-real-y-valor-en-gozen)
6. [Tabla D — Evidencia dura: benchmarks de la comunidad](#6-tabla-d--evidencia-dura-benchmarks-de-la-comunidad)
7. [Tabla E — Modelos stealth y routers: qué son en realidad](#7-tabla-e--modelos-stealth-y-routers-qué-son-en-realidad)
8. [Tabla F — Banderas rojas recurrentes](#8-tabla-f--banderas-rojas-recurrentes)
9. [Cómo se regenera](#9-cómo-se-regenera)

---

## 1) Matriz principal: modelo × habilidad

`+++` primera opción · `++` buen encaje · `+` aceptable · `±` flojo pero usable · `✗` evitar · `–` sin evidencia

| Modelo | Frontend | Backend | Planif. | Motion/Visual | Código | Debug | Tests/Review | Orquest. | Docs | Research | Visión | Local | Simples | Valor |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| **Opus 5.5** | ++ | ++ | +++ | +++ | +++ | ++ | +++ | +++ | +++ | ++ | ++ | ✗ | ± | ± |
| **Sonnet 5.5** | ++ | ++ | ++ | ++ | +++ | +++ | +++ | ++ | ++ | ++ | + | ✗ | + | + |
| **Haiku 5.5** | + | + | + | – | ++ | + | ++ | + | + | + | – | ✗ | ++ | ++ |
| **GPT-6 Luna** | + | ++ | ++ | – | ++ | + | ++ | ++ | ++ | ++ | + | ✗ | +++ | +++ |
| **Sol 6.1 / GPT-6** | + | ++ | +++ | + | ++ | + | +++ | +++ | ++ | ++ | – | ✗ | + | ++ |
| **Gemini 4 Argon** | +++ | ++ | ++ | +++ | ++ | ++ | ++ | + | ++ | ++ | +++ | ✗ | + | ± |
| **DeepSeek 4.1 Flash** | ++ | +++ | ++ | ++ | +++ | +++ | ++ | ++ | + | + | ++ | ✗ | +++ | +++ |
| **GLM 5.3 Flash** | +++ | +++ | +++ | + | +++ | +++ | +++ | +++ | +++ | +++ | + | ✗ | ++ | ++ |
| **Muse Spark 1.3** | ++ | ++ | + | + | ++ | ++ | + | ++ | ✗ | ++ | + | ✗ | ++ | +++ |
| **MiMo 2.6 Flash/Pro** | ++ | ++ | ++ | +++ | +++ | ++ | ++ | ++ | + | + | ++ | ✗ | ++ | +++ |
| **Kimi K2.7 / K2.6 / K3** | +++ | ++ | +++ | + | +++ | ++ | ++ | ++ | ++ | ++ | ++ | ✗ | + | ± |
| **Qwen 3.8** | + | ++ | ++ | – | ++ | + | + | +++ | + | ++ | + | +++ | ++ | ++ |
| **Space Bunny (MiniMax)** | ++ | + | + | +++ | +++ | + | ++ | + | + | + | ++ | ✗ | + | ++ |
| **Step 5 Preview** | – | + | + | – | ++ | + | ++ | – | + | – | – | ✗ | ++ | +++ |
| **LongCat 2.5** | ++ | + | – | – | + | ± | – | – | – | – | ++ | ✗ | ++ | +++ |
| **Ling 3.1** | – | – | – | – | + | – | – | – | – | – | – | ✗ | ++ | +++ |
| **Nemotron 3 Ultra** | – | + | + | – | ± | ± | ± | ++ | – | – | – | ✗ | ± | ++ |
| **Cat Jam** | – | – | – | – | ± | – | – | – | – | – | – | ✗ | ++ | +++ |
| **big-pickle (MAI)** | – | + | – | – | ± | ± | – | – | ✗ | – | – | ✗ | ± | ++ |
| **Grok 4.6** | – | + | + | – | + | – | – | – | – | – | – | ✗ | – | ✗ |

**Lectura rápida por columna**

- **Frontend**: Gemini 4 Argon, GLM 5.3 Flash y Kimi K2.7 Code.
- **Backend**: DeepSeek 4.1 Flash y GLM 5.3 Flash, con Muse Spark para bugs que cruzan capas.
- **Planificación**: Opus 5.5 y Sol 6.1; GLM 5.3 Flash como opción barata; Kimi K2.7 como planner.
- **Motion/Visual**: Opus 5.5, Gemini 4 (diseño), MiMo 2.6 Pro (3D/skeletons) y Space Bunny (one-shot creativo).
- **Código**: DeepSeek y GLM primero; Muse y MiMo como segundos.
- **Debug**: GLM 5.3 Flash, Muse Spark y Sonnet 5.5.
- **Tests/Review**: GLM 5.3 Flash (adversarial), Sol/Opus, Sonnet.
- **Orquestación**: GLM 5.3 Flash; Qwen si el contexto es largo.
- **Docs**: GLM 5.3 Flash por delante del resto.
- **Research**: GLM 5.3 Flash, Luna y Muse Spark.
- **Visión**: Gemini 4, DeepSeek, Kimi y LongCat (barato).
- **Local/privacidad**: solo Qwen (ollama / llama.cpp). Todo lo demás es nube y varios entrenan con tus datos.
- **Simples/grunt work**: DeepSeek Flash, Luna low/medium y los gratis.
- **Valor**: DeepSeek y los free/flash por delante; Opus, Grok y Kimi K3 al final.

---

## 2) Leyenda y criterio

- Las valoraciones salen de **frases donde alguien vincula explícitamente un modelo con una tarea**
  ("uso X para Y", "X es mejor en Z"), ponderadas por votos. **No son benchmarks controlados.**
- `–` significa *sin evidencia suficiente*, no "malo". Las columnas con menos datos son
  **Motion/Visual** (menos de 10 frases útiles) y **Visión**.
- `Valor` = calidad/precio dentro de OpenCode Go/Zen, no precio absoluto (ver [Tabla C](#5-tabla-c--precio-real-y-valor-en-gozen)).
- Los modelos stealth cambian de identidad: ver [Tabla E](#7-tabla-e--modelos-stealth-y-routers-qué-son-en-realidad).

---

## 3) Tabla A — Rol ideal, pega principal y sentimiento

| Modelo | Rol ideal | Pega principal | Opiniones | % positivo |
|---|---|---|---|:--:|:--:|
| Opus 5.5 | Arquitecto / design docs | Consumo de tokens brutal | 22 | 64% |
| Sonnet 5.5 | Implementar tras el plan de Opus; paneles de review | Caro en tokens | 20 | 60% |
| Haiku 5.5 | Worker barato para coding directo | Precio ×5 al pasar de 100k de contexto | 15 | 80% |
| GPT-6 Luna | Volumen a bajo coste; worker | Lento en razonamiento alto | 67 | 70% |
| Sol 6.1 | Cabeza pensante eficiente en tokens | Lento | – | – |
| Gemini 4 Argon | Frontend y diseño visual | Coste por tarea | – | – |
| DeepSeek 4.1 Flash | **Workhorse por defecto** | Bucles repetidos, caídas, contexto largo | 99 | 63% |
| GLM 5.3 Flash | **Orquestador y revisor** | Precio en Go; hay que babysitearlo | 49 | 61% |
| Muse Spark 1.3 | Subagente rápido | Benchmaxxed, no entiende ambigüedad, **entrena con tus datos** | 33 | 70% |
| MiMo 2.6 Flash/Pro | Implementador; mejor modelo medio | Repite tool-calls y quema contexto | 55 | 58% |
| Kimi K2.7/K2.6/K3 | Frontend y planner | K3 es el más caro de Go | 19 | 63% |
| Qwen 3.8 | Local/self-host y agentes largos | Overthinking | 18 | 61% |
| Space Bunny | One-shot creativo y refactors grandes | Lento, token-ineficiente, retirado | 30 | 53% |
| Step 5 Preview | Alternativa gratis decente | Lento, se distrae, endpoints caídos | 7 | 57% |
| LongCat 2.5 | Visión barata, commits, microtareas | Rompió el CLI a varios usuarios | 3 | 0% |
| Ling 3.1 | Relleno gratis | Sin defensores | 1 | 0% |
| Nemotron 3 Ultra | Orquestador por su ventana de 1M | Falla tareas básicas | 4 | 50% |
| big-pickle (MAI) | — | Documentos y rutas alucinadas | 3 | 33% |
| Grok 4.6 | — | Quema la cuota en 3 prompts | 15 | 53% |
| Cat Jam | Tareas triviales a 300-350 tps | Inteligencia muy baja | – | – |

---

## 4) Tabla B — Stack recomendado según presupuesto

| Presupuesto | Planificador | Orquestador | Implementador | Revisor | Worker barato |
|---|---|---|---|---|---|
| **$0 (free tier)** | Luna / Muse Spark | GLM 5.3 Flash (si entra) | MiMo 2.6 Flash Free · Ling 3.1 | Muse Spark · Space Bunny | LongCat 2.5 · Step 5 · Cat Jam |
| **$10 (Go)** | Luna max o GLM 5.3 | GLM 5.3 Flash | DeepSeek 4.1 Flash | GLM 5.3 Flash (adversarial) | DeepSeek Flash · MiMo Flash |
| **$20** | Opus 5.5 (plan + design docs) | Sonnet 5.5 | Sonnet 5.5 | Sonnet 5.5 | Luna low/medium |
| **$30-40** | Opus 5.5 / Sol 6.1 | Opus 5.5 + GLM 5.3 | DeepSeek 4.1 Flash + MiMo Pro | GLM 5.3 Flash + Sonnet | Haiku 5.5 |
| **Local (0 €/token)** | Qwen 3.8 (si te da) | Qwen 3.8 largo contexto | Qwen 3.6 35B A3B | — | Qwen local pequeño |

Consenso repetido en los dos subs: **el plan de $10 sigue siendo el mejor valor**
($60-80 de uso de DeepSeek por $10); **Go Plus de $40 no compensa** ("2x los límites por 4x el precio");
y el mejor setup "es el que te deja trabajar sin pensar en los límites".

---

## 5) Tabla C — Precio real y valor en Go/Zen

| Modelo / plan | Entrada /1M | Salida /1M | Cache read /1M | Notas |
|---|---|---|---|---|
| DeepSeek 4.1 Flash | $0.15 | $0.60 | **$0.003** | 96% de cache hit; 2,5x el trabajo de GLM por 20% más de coste |
| GLM 5.3 Flash | $0.15 | $0.50 | $0.03 | 92% de cache hit; "se siente más listo" pero cuesta más por tarea |
| GPT-6 Luna (Zen) | $0.10 | $0.50 | $0.01 | Más barato que DeepSeek en lista; **la caché decide** |
| Haiku 5.5 | $0.10 | $0.50 | — | ≤100k tokens; **×5 de precio** al pasarlos |
| Kimi K3 | $2.00 | $10.00 | — | El más caro de Go; quema la cuota en 3 prompts |
| Mistral Large 4 | — | — | — | "Toda la potencia de Luna por 15x el coste" |
| **Go $10** | — | — | — | $60 → **$80** de uso DeepSeek (subida sin anunciar, oct-12) |
| **Go Plus $40** | — | — | — | 2x límites por 4x precio → "DOA"; la gente apila subs de $10 |
| OpenDesign Go ($8-10) | — | — | — | **$120** de crédito con DS 4.1 Flash; sin verificar, olor a CrofAI |

Casos de referencia: **CrofAI** se anunciaba como "el proveedor más barato del mundo" y resultó ser un
wrapper de OpenRouter revendiendo modelos baratos con hasta **20x de margen** (cerró al descubrirse).
Regla que repiten: *si suena demasiado bueno, hay trampa*.

---

## 6) Tabla D — Evidencia dura: benchmarks de la comunidad

**Terminal-Bench 2.1** (89 tareas × 3 intentos, tests de la comunidad)

| Modelo | Pass@1 | Pass@3 | Tokens por intento | Velocidad |
|---|:--:|:--:|:--:|---|
| Space Bunny (retirado) | **52,1%** | 66,3% | ~1,69M | mediana 979 s |
| Step 5 Preview | 50,2% | 64,0% | ~0,90M | el más lento |
| LongCat 2.5 Preview | 48,7% | 64,0% | **~0,54M** | mediana 784 s |
| MiMo v2.5 | 44,2% | 66,3% | ~0,57M | mediana 830 s |

**Workers gratis, 8-oct** (Q&A + arreglar 2 tests que fallan, con pytest y timeout de 420 s)

| Puesto | Modelo | Puntuación | Segundos |
|:--:|---|:--:|:--:|
| 1 | mimo-v2.6-flash-free | **100** | 129 |
| 2 | muse-spark-1.3-contributor-free | 99 | 132 |
| 3 | space-bunny-free | 95 | 167 |
| 4 | longcat-2.5-preview-free | 92 | 214 |
| 5 | ling-3.1-flash-free | 91 | 220 |
| 6 | nemotron-3-ultra-free | 70 | 257 |
| 7 | nemotron-3.5-lightning-free | 20 | 422 |
| 8 | exo-free · fledge-alpha-free · ling-3.0-fin-free | **0** (timeout) | — |

**Otras pruebas**

- **Animación (test del caballo)**: Space Bunny ganó con claridad; Exo Free lo hizo con **<2M tokens**
  frente a los **35M** de Space Bunny.
- **Bug real en C#**: DeepSeek V4.1 Flash High lo resolvió por **$0.042** (Luna High $0.043;
  Terra High $0.396). "DS Flash 4.1 realmente superó a Luna".
- **MiMo-V2.6-Pro**: top open-weights del índice AA (**46**) y en la frontera Pareto
  inteligencia/coste ($0.13 por tarea del índice).
- **Opencode Go Bench**: 43 modelos de opencode.ai/go cruzados con Artificial Analysis
  (crítica habitual: Go sirve versiones cuantizadas, así que el benchmark del modelo oficial no aplica).

---

## 7) Tabla E — Modelos stealth y routers: qué son en realidad

| Nombre público | Qué era en realidad | Cómo se supo |
|---|---|---|
| **Space Bunny** | MiniMax **M3.1** | Filtraba etiquetas `<minimax>` y el tokenizer coincide con M2/M3 |
| **Exo Free** | Router a GPT/Claude (probablemente **Haiku 5.5**); murió en horas | Se cayó al llegar tráfico; "murió como router" |
| **Fledge Alpha** | **Router**: DeepSeek 4.1 + Kimi (¿K3?) + un tercero; con visión | Fingerprint de tokenizer |
| **big-pickle** | **MAI de Microsoft AI** (varía con el tiempo) | Se autodelata al preguntarle |
| **Cat Jam** | "CatJam by LitterBox AI"; se sospecha **Groq** por los 300-350 tps | Respuesta del propio modelo |
| **Hy4 Preview** | Probablemente MiniMax/Space Bunny | Comparativas de la comunidad |
| **Union Alpha** | Se especuló **Mistral** | Contexto: conferencia y cuenta en España |
| **CrofAI** | Wrapper de OpenRouter con hasta 20x de margen | Auditoría de la comunidad → cerró |
| **"greg-2-super"** (en OpenRouter) | Ruta a Kimi K2.7 Code | Nombres de ruta filtrados |

---

## 8) Tabla F — Banderas rojas recurrentes

| Señal | Detalle |
|---|---|
| **Bucles y repeticiones** | DeepSeek 4.1 repite bucles; MiMo 2.6 repite tool-calls idénticas quemando contexto; Muse 1.3 da 8 rondas de review sin terminar |
| **Datos de entrenamiento** | Los modelos "Contributor" (Muse Spark) y Space Bunny **entrenan con tus prompts** según la propia doc de Go |
| **Cuotas que se agotan** | Kimi K3 y Grok 4.6 queman la cuota en 3 prompts; el free tier se agota "en minutos" en horas punta |
| **Límites opacos** | El límite gratis de Zen no es público y "varía según la demanda"; cambios de precio/limit sin anuncio (DeepSeek $60→$80) |
| **Cuantización** | Lo que sirve Go no siempre es el modelo oficial: GLM 5.3 Flash es FP8 completo, pero el debate cuantización es constante |
| **Estabilidad** | Endpoints caídos (Step 5: "Endpoint is unavailable"), lentitud general (70-87 tok/s en Go vs 270 t/s de la API directa de DeepSeek) |
| **Seguridad** | OpenCode Desktop 2.0.26 (Windows): el permiso `external_directory` no salta; OpenChamber subió **1,86 GB** a su relay por una ruta de dictado sin límites |
| **Rompe-instalaciones** | LongCat 2.5 Preview obligó a reinstalar el CLI a varios usuarios |

---

## 9) Cómo se regenera

```bash
python3 noticias.py --subreddit opencode        # delta desde el último volcado
python3 noticias.py --subreddit opencodeCLI
python3 informe.py --subreddit opencode --dias 30      # noticias / calidad-precio / modelos
python3 especialidades.py --citas 2 --minimo 3         # matriz modelo × dominio
```

Datos de origen: `hilos-*.json` (hilos + comentarios), `hilos-*-comentarios-huerfanos.json`
(comentarios en hilos antiguos, ~900 por mes que antes se perdían), `especialidades.txt`,
`dominios.txt`, `informe-opencodeCLI.md`.
