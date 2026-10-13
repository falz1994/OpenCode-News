#!/usr/bin/env python3
"""Cruza cada modelo con el DOMINIO de tarea en el que la gente dice que destaca.

Responde: "¿en que es bueno cada modelo segun los comentarios?" (frontend, backend,
planificacion, motion graphics, implementacion, debugging, tests/review, orquestacion...)

Uso:
  python3 especialidades.py                        # ambos subs
  python3 especialidades.py --subreddit opencodeCLI
  python3 especialidades.py --citas 2 --minimo 3   # citas por modelo y minimo de menciones
"""
import argparse, collections, datetime, glob, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ap = argparse.ArgumentParser()
ap.add_argument("--subreddit", help="limitar a un sub (por defecto: todos los volcados)")
ap.add_argument("--citas", type=int, default=2, help="citas por modelo y dominio")
ap.add_argument("--minimo", type=int, default=2, help="menciones minimas para mostrar el dominio")
ap.add_argument("--largo", type=int, default=170, help="caracteres por cita")
a = ap.parse_args()

MODELOS = {
    "DeepSeek 4.1 Flash": r"deepseek|ds ?4\.1|v4\.1 ?flash|dsv4|ds flash",
    "GLM 5.3 (Flash)": r"\bglm\b",
    "Muse Spark 1.3": r"muse ?spark|muse ?1\.3|\bspark\b",
    "MiMo v2.6": r"\bmimo\b",
    "Space Bunny/MiniMax": r"space ?bunny|minimax",
    "Kimi K2.7/K3": r"\bkimi\b|\bk3\b",
    "Qwen 3.8": r"\bqwen\b",
    "Opus 5.5": r"\bopus\b",
    "Sonnet 5.5": r"\bsonnet\b",
    "Haiku 5.5": r"\bhaiku\b",
    "GPT-6 Luna": r"\bluna\b",
    "Sol 6.1 / GPT-6": r"\bsol ?6|\bsol\b|gpt-?6",
    "Gemini 4 Argon": r"gemini|argon",
    "big-pickle (MAI)": r"big-?pickle",
    "LongCat 2.5": r"longcat",
    "Ling 3.1": r"\bling\b",
    "Step 5 Preview": r"step ?5|stepfun",
    "Cat Jam": r"cat ?jam",
    "Nemotron": r"nemotron",
    "Grok 4.6": r"\bgrok\b",
}
DOMINIOS = {
    "frontend":      r"front-?end|frontend|\bUI\b|\bUX\b|\bcss\b|tailwind|\breact\b|\bvue\b|svelte|next\.?js|web ?ui|landing|component|layout",
    "backend":       r"back-?end|backend|database|\bsql\b|postgres|server[- ]side|microservice|\bendpoint\w*|\bapi[s]?\b(?!\s*(key|keys|pricing|price|cost|costs|usage|credits|access|rate|limit|call|spend|budget|plan))",
    "planificacion": r"\bplanning\b|\bplanner\b|plan mode|architect\w*|design doc|\bspec[s]?\b|requirement\w*|scoping|roadmap|task breakdown|\bspecs?\b",
    "motion/visual": r"motion graphic\w*|animat\w*|\bvideo\w*|hyperframe|keyframe|render\w*|after effects|montage|visual effect|\bmotion\b",
    "diseno":        r"\bdesign\w*|\bvisual\w*|figma|aesthetic|\blook\b|typography|palette",
    "implementar":   r"implement\w*|\bcod(e|ing)\b|refactor\w*|\bfeature\w*|boilerplate|scaffold|build (the|a|my)",
    "debugging":     r"debug\w*|\bbugs?\b|\bbuggy\b|\bfix\w*|root cause|stack ?trace|\berror\w*|troubleshoot",
    "tests/QA":      r"\btests?\b|\btesting\b|pytest|unit test|benchmark\w*|\bQA\b|verif\w*|\breview\w*|adversarial",
    "orquestacion":  r"orchestrat\w*|\brouter\w*|routing|sub-?agents?\b|agent loop|multi-?agent|long context|context window|scheduler",
    "escritura/docs":r"\bwrit\w*|\bdocs?\b|documentation|commit message|prose|\bcopy\b|readme|summar\w*",
    "investigacion": r"research\w*|scrap\w*|data ?(extraction|analysis|aggregation)|\betl\b|transl\w*|web ?search",
    "vision":        r"\bvision\b|screenshot|\bimages?\b|\bocr\b|diagram|multimodal",
    "local/privado": r"\blocal\w*|offline|self-?host\w*|privacy|\bZDR\b|on-?device|ollama|llama\.cpp",
    "tareas simples":r"simple (task|thing|stuff)|tiny task|small task|trivial|grunt|quick (task|job)|bulk work|cheap work",
}

# ---------------------------------------------------------------- carga
hilos = {}
for fn in glob.glob(os.path.join(HERE, "hilos-*.json")):
    if "huerfanos" in fn:
        continue
    try:
        d = json.load(open(fn, encoding="utf-8"))
    except Exception:
        continue
    sub = (d.get("meta") or {}).get("subreddit")
    if a.subreddit and sub != a.subreddit:
        continue
    for t in d.get("threads", []):
        prev = hilos.get(t["id"])
        if not prev or len(t.get("comments") or []) > len(prev.get("comments") or []):
            hilos[t["id"]] = t
if not hilos:
    sys.exit("sin volcados; ejecuta fetch.py primero")

unidades = []
for t in hilos.values():
    sub = t.get("subreddit") or "?"
    unidades.append((t.get("score") or 0, t["title"] + ". " + (t.get("selftext") or ""), sub))
    for c in t.get("comments") or []:
        unidades.append((c.get("score") or 0, c.get("body") or "", sub))
print(f"# Especialidades por modelo — {len(unidades)} unidades de texto "
      f"({len(hilos)} hilos{'' if not a.subreddit else ', r/' + a.subreddit})\n")

rx_dom = {k: re.compile(v, re.I) for k, v in DOMINIOS.items()}
matriz = collections.defaultdict(collections.Counter)   # modelo -> dominio -> n
citas = collections.defaultdict(list)                   # (modelo, dominio) -> [(score, sub, frase)]

for nombre, pat in MODELOS.items():
    rx_m = re.compile(pat, re.I)
    for score, txt, sub in unidades:
        if not rx_m.search(txt):
            continue
        for frase in re.split(r"(?<=[.!?])\s+|\n", txt):
            if not rx_m.search(frase):
                continue
            frase = " ".join(frase.split())
            if not (10 < len(frase) < 320):
                continue
            for dom, rx in rx_dom.items():
                if rx.search(frase):
                    matriz[nombre][dom] += 1
                    citas[(nombre, dom)].append((score, sub, frase))

# ---------------------------------------------------------------- matriz
dominios = list(DOMINIOS)
corto = {d: d[:9] for d in dominios}
print("## MATRIZ modelo x dominio (nº de frases que los vinculan)\n")
print(f"{'modelo':<22}" + "".join(f"{corto[d]:>10}" for d in dominios))
for nombre in MODELOS:
    fila = matriz.get(nombre)
    if not fila:
        continue
    print(f"{nombre:<22}" + "".join(f"{(fila[d] or ''):>10}" for d in dominios))

# ---------------------------------------------------------------- detalle
print("\n## DETALLE: dominios top por modelo\n")
for nombre in MODELOS:
    fila = matriz.get(nombre)
    if not fila:
        continue
    tops = [(d, n) for d, n in fila.most_common() if n >= a.minimo][:4]
    if not tops:
        continue
    print(f"\n### {nombre}")
    for dom, n in tops:
        print(f"  · {dom} ({n} menciones)")
        vistos = set()
        mostradas = 0
        for score, sub, frase in sorted(citas[(nombre, dom)], key=lambda x: -x[0]):
            k = frase[:40].lower()
            if k in vistos:
                continue
            vistos.add(k)
            print(f"      [{score:>4}↑ r/{sub}] {frase[:a.largo]}")
            mostradas += 1
            if mostradas >= a.citas:
                break
