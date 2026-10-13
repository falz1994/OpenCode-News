#!/usr/bin/env python3
"""Responde las 3 preguntas recurrentes de los subs de OpenCode a partir de los volcados locales.

  1) NOTICIAS      - que se ha anunciado, lanzado, roto o cambiado
  2) CALIDAD-PRECIO - modelos mas baratos y mejor valor en OpenCode Go / Zen
  3) MODELOS       - habilidades y debilidades de cada modelo segun las experiencias

Uso:
  python3 informe.py --subreddit opencodeCLI --dias 30
  python3 informe.py --subreddit opencode --dias 7 --top 12 --citas 3
"""
import argparse, collections, datetime, glob, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))

ap = argparse.ArgumentParser()
ap.add_argument("--subreddit", default="opencode")
ap.add_argument("--dias", type=int, default=30, help="ventana temporal en dias")
ap.add_argument("--top", type=int, default=15, help="elementos por seccion")
ap.add_argument("--citas", type=int, default=3, help="citas por modelo (positivas y negativas)")
a = ap.parse_args()

# ---------------------------------------------------------------- carga
def cargar(sub):
    """Une todos los volcados del subreddit, deduplicando hilos por id."""
    hilos = {}
    for fn in glob.glob(os.path.join(HERE, "hilos-*.json")):
        if "huerfanos" in fn:
            continue
        try:
            d = json.load(open(fn, encoding="utf-8"))
        except Exception:
            continue
        if (d.get("meta") or {}).get("subreddit") != sub:
            continue
        for t in d.get("threads", []):
            prev = hilos.get(t["id"])
            if not prev or len(t.get("comments") or []) > len(prev.get("comments") or []):
                hilos[t["id"]] = t
    return list(hilos.values())

hilos = cargar(a.subreddit)
if not hilos:
    sys.exit(f"sin volcados de r/{a.subreddit}; usa fetch.py --subreddit {a.subreddit}")

ahora = datetime.datetime.now(datetime.UTC).timestamp()
desde = ahora - a.dias * 86400
ventana = [t for t in hilos if t["created_utc"] >= desde]
f = lambda u: datetime.datetime.fromtimestamp(u, datetime.UTC).strftime("%m-%d %H:%M")

unidades = []           # (score, texto, titulo, tipo)
for t in ventana:
    unidades.append((t.get("score") or 0, t["title"] + "\n" + (t.get("selftext") or ""), t["title"], "POST"))
    for c in t.get("comments") or []:
        unidades.append((c.get("score") or 0, c.get("body") or "", t["title"], "COM"))

print(f"# r/{a.subreddit} — informe de los ultimos {a.dias} dias")
print(f"_{len(ventana)} hilos y {sum(len(t.get('comments') or []) for t in ventana)} comentarios "
      f"· generado {datetime.datetime.now(datetime.UTC):%Y-%m-%d %H:%M} UTC_\n")

# ---------------------------------------------------------------- 1) NOTICIAS
NEWS = re.compile(r"(?i)\b(releas\w*|launch\w*|announc\w*|introduc\w*|now (available|free|on)|"
                  r"deprecat\w*|discontinu\w*|price|pricing|limits?|quota|update[sd]?|new model|"
                  r"stealth|free for|shut ?down|broken|outage|down)\b")
print("=" * 100)
print(f"## 1) NOTICIAS MAS IMPORTANTES\n")
top_score = sorted(ventana, key=lambda t: -(t.get("score") or 0))[:a.top]
for t in top_score:
    print(f"[{t['score']:>4}↑ {t['num_comments']:>3}c {f(t['created_utc'])}] {t['title'][:100]}")
novedades = [t for t in ventana if NEWS.search(t["title"])]
novedades.sort(key=lambda t: -(t.get("score") or 0))
print(f"\n--- anuncios/novedades detectados en el titulo ({len(novedades)}) ---")
for t in novedades[:a.top]:
    primer = ""
    cs = sorted(t.get("comments") or [], key=lambda c: -(c.get("score") or 0))
    if cs:
        primer = " | top: " + " ".join((cs[0].get("body") or "").split())[:130]
    print(f"[{t['score']:>4}↑ {f(t['created_utc'])}] {t['title'][:95]}{primer}")

# ---------------------------------------------------------------- 2) CALIDAD-PRECIO
VALUE = re.compile(r"(?i)(\$ ?\d|\bcheap\w*|\bpric\w*|\bcost\w*|\bvalue\b|\bworth\b|\bbudget\b|"
                   r"usage limit|quota|\blimits?\b|per 1m|token[s]? per|subscription|plan)")
GO = re.compile(r"(?i)(opencode ?go|\bgo plan\b|\bzen\b|\$ ?10\b|\bplan\b)")
MODELOS = {
    "DeepSeek 4.1 Flash": r"deepseek|ds ?4\.1|v4\.1 ?flash|dsv4",
    "GLM 5.3 (Flash)": r"\bglm\b",
    "Muse Spark 1.3": r"muse ?spark|muse ?1\.3",
    "MiMo v2.6 (Flash/Pro)": r"\bmimo\b",
    "Space Bunny / MiniMax": r"space ?bunny|minimax",
    "Kimi (K2.7/K3)": r"\bkimi\b|\bk3\b",
    "Qwen": r"\bqwen\b",
    "Opus 5.5": r"\bopus\b",
    "Sonnet 5.5": r"\bsonnet\b",
    "Haiku 5.5": r"\bhaiku\b",
    "GPT-6 Luna / Sol": r"\bluna\b|\bsol\b|gpt-?6",
    "big-pickle (MAI)": r"big-?pickle",
    "LongCat 2.5": r"longcat",
    "Ling 3.1": r"\bling\b",
    "Step 5 Preview": r"step ?5|stepfun",
    "Cat Jam": r"cat ?jam",
    "Nemotron": r"nemotron",
    "Grok": r"\bgrok\b",
}
VALOR = []
for s, txt, tit, tipo in unidades:
    if VALUE.search(txt) and GO.search(txt):
        VALOR.append((s, txt, tit, tipo))
VALOR.sort(key=lambda x: -x[0])
print("\n" + "=" * 100)
print("## 2) CALIDAD-PRECIO EN OPENCODE GO / ZEN\n")
print(f"({len(VALOR)} menciones de precio/limites/valor en el sub)")
for s, txt, tit, tipo in VALOR[:a.top]:
    print(f"[{s}↑ {tipo}] {' '.join(txt.split())[:230]}")

# ---------------------------------------------------------------- 3) MODELOS
POS = re.compile(r"(?i)\b(good|great|best|excelent\w*|excellent|fast|quick|smart|cheap\w*|beast|solid|"
                 r"reliable|impressive|love\w*|amazing|underrated|workhorse|accurate|clean|recommend\w*|"
                 r"worth it|generous)\b")
NEG = re.compile(r"(?i)\b(bad|worst|slow\w*|dumb\w*|stupid|expensive|costly|bug[sgy]?\b|buggy|loop\w*|"
                 r"fail\w*|worse|rubbish|garbage|trash|hallucinat\w*|timeout\w*|rate.?limit\w*|quantiz\w*|"
                 r"lobotom\w*|overthink\w*|benchmaxx\w*|unusable|broken|meh|scam|avoid|useless|burn\w*|"
                 r"eat\w* (up )?(my |the )?tokens|token hog|waste\w*)\b")
NEGADO = re.compile(r"(?i)\b(not|isn'?t|aren'?t|no|never|hardly|nunca)\s+"
                    r"(bad|terrible|awful|expensive|slow|dumb|useless)\b")
print("\n" + "=" * 100)
print("## 3) HABILIDADES Y DEBILIDADES POR MODELO\n")
RESUMEN = []
for nombre, pat in MODELOS.items():
    rx = re.compile(pat, re.I)
    citas = []
    npos = nneg = 0
    for s, txt, tit, tipo in unidades:
        if not rx.search(txt):
            continue
        for frase in re.split(r"(?<=[.!?])\s+|\n", txt):
            if not rx.search(frase):
                continue
            frase = " ".join(frase.split())
            if not (8 < len(frase) < 300):
                continue
            p, n = bool(POS.search(frase)), bool(NEG.search(frase))
            if NEGADO.search(frase):      # "not bad", "no es caro" -> positivo
                p, n = True, False
            if p:
                npos += 1
            if n:
                nneg += 1
            if p or n:
                citas.append((s, "+" if p and not n else "-" if n and not p else "±", frase))
    if not citas:
        continue
    RESUMEN.append((npos + nneg, nombre, npos, nneg))
    print(f"\n### {nombre}  (menciones valorativas: {npos + nneg} · +{npos} / -{nneg})")
    for signo, etiqueta in (("+", "FUERTE"), ("-", "DEBIL")):
        vistos, out = set(), []
        for s, sg, frase in sorted(citas, key=lambda x: -x[0]):
            if sg != signo:
                continue
            k = frase[:45].lower()
            if k in vistos:
                continue
            vistos.add(k)
            out.append((s, frase))
            if len(out) >= a.citas:
                break
        for s, frase in out:
            print(f"  {etiqueta:6} [{s:>4}↑] {frase[:225]}")

print("\n" + "=" * 100)
print("## RESUMEN (modelos ordenados por volumen de opinion)")
for total, nombre, npos, nneg in sorted(RESUMEN, reverse=True):
    ratio = npos / (npos + nneg) if (npos + nneg) else 0
    barra = "#" * int(round(ratio * 20))
    print(f"  {nombre:<24} {total:>4} opiniones  +{npos:<4} -{nneg:<4} {ratio*100:>3.0f}% positivo  {barra}")
