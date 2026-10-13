#!/usr/bin/env python3
"""Genera la fuente de datos que consume index.html.

Entrada:  fuente.json (tablas curadas a mano) + los volcados hilos-*.json (scraping)
Salida:   datos.json  y  datos.js  (window.DATOS = {...}, para abrir el HTML con file://)

Uso:
  python3 index_datos.py
  python3 index_datos.py --noticias-dias 7
"""
import argparse, collections, datetime, glob, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ap = argparse.ArgumentParser()
ap.add_argument("--fuente", default=os.path.join(HERE, "fuente.json"))
ap.add_argument("--noticias-dias", type=int, help="sobrescribe fuente.json")
ap.add_argument("--salida", default="datos")
a = ap.parse_args()

f = json.load(open(a.fuente, encoding="utf-8"))
if a.noticias_dias:
    f["noticias_dias"] = a.noticias_dias

# ---------------------------------------------------------------- volcados
hilos, subs = {}, collections.Counter()
for fn in sorted(glob.glob(os.path.join(HERE, "hilos-*.json"))):
    if "huerfanos" in fn:
        continue
    try:
        d = json.load(open(fn, encoding="utf-8"))
    except Exception:
        continue
    sub = (d.get("meta") or {}).get("subreddit")
    if not sub:
        continue
    for t in d.get("threads", []):
        subs[sub] += 1
        p = hilos.get(t["id"])
        if not p or len(t.get("comments") or []) > len(p.get("comments") or []):
            hilos[t["id"]] = t
if not hilos:
    sys.exit("no hay volcados: ejecuta fetch.py primero")

ahora = datetime.datetime.now(datetime.UTC)
corte = ahora.timestamp() - f.get("ventana_dias", 45) * 86400

unidades = []      # (score, texto, sub) — solo hilos dentro de la ventana
for t in hilos.values():
    if t["created_utc"] < corte:
        continue
    sub = t.get("subreddit") or "?"
    unidades.append((t.get("score") or 0, t["title"] + ". " + (t.get("selftext") or ""), sub))
    for c in t.get("comments") or []:
        unidades.append((c.get("score") or 0, c.get("body") or "", sub))

# ---------------------------------------------------------------- sentimiento
POS = re.compile(r"(?i)\b(good|great|best|excelent\w*|excellent|fast|quick|smart|cheap\w*|beast|solid|"
                 r"reliable|impressive|love\w*|amazing|underrated|workhorse|accurate|clean|recommend\w*|"
                 r"worth it|generous)\b")
NEG = re.compile(r"(?i)\b(bad|worst|slow\w*|dumb\w*|stupid|expensive|costly|bug[sgy]?\b|buggy|loop\w*|"
                 r"fail\w*|worse|rubbish|garbage|trash|hallucinat\w*|timeout\w*|rate.?limit\w*|quantiz\w*|"
                 r"lobotom\w*|overthink\w*|benchmaxx\w*|unusable|broken|meh|scam|avoid|useless|burn\w*|"
                 r"eat\w* (up )?(my |the )?tokens|token hog|waste\w*)\b")
NEGADO = re.compile(r"(?i)\b(not|isn'?t|aren'?t|no|never|hardly)\s+(bad|terrible|awful|expensive|slow|dumb|useless)\b")

# ---------------------------------------------------------------- dominios
DOMINIOS = {
    "frontend":      r"front-?end|frontend|\bUI\b|\bUX\b|\bcss\b|tailwind|\breact\b|\bvue\b|svelte|next\.?js|web ?ui|landing|component",
    "backend":       r"back-?end|backend|database|\bsql\b|postgres|server[- ]side|microservice|\bendpoints?\b|\bapis?\b(?!\s*(key|keys|pricing|price|cost|costs|usage|credits|access|rate|limit|call|spend|budget|plan))",
    "planificacion": r"\bplanning\b|\bplanner\b|plan mode|architect\w*|design doc|\bspec[s]?\b|requirement\w*|scoping|roadmap|task breakdown",
    "motion":        r"motion graphic\w*|animat\w*|\bvideo\w*|hyperframe|keyframe|render\w*|montage|\bvisual\w*|\bdesign\w*|figma|aesthetic|\b3d\b|skeleton",
    "codigo":        r"implement\w*|\bcod(e|ing)\b|refactor\w*|\bfeature\w*|boilerplate|scaffold",
    "debug":         r"debug\w*|\bbugs?\b|\bbuggy\b|root cause|stack ?trace|troubleshoot",
    "tests":         r"\btests?\b|\btesting\b|pytest|unit test|\bQA\b|verif\w*|\breview\w*|adversarial|\bbenchmark\w*",
    "orquestacion":  r"orchestrat\w*|\brouter\w*|routing|sub-?agents?\b|multi-?agent|long context|context window|scheduler",
    "docs":          r"\bwrit\w*|\bdocs?\b|documentation|readme|prose|commit message",
    "research":      r"research\w*|scrap\w*|data ?(extraction|analysis|aggregation)|\betl\b|transl\w*|web ?search",
    "vision":        r"\bvision\b|screenshot|\bocr\b|diagram|multimodal",
    "local":         r"\blocal\w*|offline|self-?host\w*|privacy|ollama|llama\.cpp",
    "simples":       r"simple (task|thing|stuff)|tiny task|small task|trivial|grunt|quick (task|job)|bulk work|boilerplate",
    "valor":         r"(?i)(\$ ?\d|\bcheap\w*|\bpric\w*|\bcost\w*|\bvalue\b|\bworth\b|usage limit|quota|per 1m)",
}
rx_dom = {k: re.compile(v, re.I) for k, v in DOMINIOS.items()}

# ---------------------------------------------------------------- por modelo
for m in f["modelos"]:
    rx = re.compile(m["alias"], re.I)
    menciones = collections.Counter()
    pos = neg = 0
    for score, txt, sub in unidades:
        if not rx.search(txt):
            continue
        for frase in re.split(r"(?<=[.!?])\s+|\n", txt):
            if not rx.search(frase) or not (8 < len(frase) < 320):
                continue
            p, n = bool(POS.search(frase)), bool(NEG.search(frase))
            if NEGADO.search(frase):
                p, n = True, False
            if p:
                pos += 1
            if n:
                neg += 1
            if p or n or True:
                for dom, rxd in rx_dom.items():
                    if rxd.search(frase):
                        menciones[dom] += 1
    total = pos + neg
    m["menciones"] = dict(menciones)
    m["sentimiento"] = {"pos": pos, "neg": neg, "total": total,
                        "pct": round(100 * pos / total) if total else None}
    print(f"  {m['nombre']:<26} opiniones={total:<4} menciones={sum(menciones.values())}")

# ---------------------------------------------------------------- noticias
dias = f.get("noticias_dias", 12)
top = f.get("noticias_top", 14)
desde = (ahora - datetime.timedelta(days=dias)).timestamp()
noticias = []
for t in hilos.values():
    if t["created_utc"] >= desde:
        noticias.append({
            "titulo": t["title"], "score": t.get("score") or 0,
            "comentarios": t.get("num_comments") or 0,
            "fecha": datetime.datetime.fromtimestamp(t["created_utc"], datetime.UTC).strftime("%Y-%m-%d %H:%M"),
            "sub": t.get("subreddit") or "?", "url": t.get("permalink_url") or "",
        })
noticias.sort(key=lambda x: -x["score"])
f["noticias"] = noticias[:top]

# ---------------------------------------------------------------- meta + salida
n_coment = sum(len(t.get("comments") or []) for t in hilos.values())
f["meta"] = {
    "generado": ahora.strftime("%Y-%m-%d %H:%M UTC"),
    "subs": dict(subs),
    "hilos": len(hilos),
    "comentarios": n_coment,
    "unidades": len(unidades),
    "ventana_dias": f.get("ventana_dias", 45),
    "fuente_datos": "Arctic Shift API (arctic-shift.photon-reddit.com)",
}
for nombre in ("datos.json", "datos.js"):
    ruta = os.path.join(HERE, nombre)
    with open(ruta, "w", encoding="utf-8") as out:
        if nombre.endswith(".js"):
            out.write("// generado por index_datos.py — no editar a mano\n")
            out.write("window.DATOS = ")
            json.dump(f, out, ensure_ascii=False, indent=1)
            out.write(";\n")
        else:
            json.dump(f, out, ensure_ascii=False, indent=1)
    print("escrito:", ruta)
print(f"\nOK · {len(f['modelos'])} modelos · {len(noticias[:top])} noticias · "
      f"{f['meta']['hilos']} hilos · {n_coment} comentarios")
