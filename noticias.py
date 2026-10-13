#!/usr/bin/env python3
"""Trae SOLO lo nuevo de un subreddit desde su ultimo volcado y resume lo mas relevante.

Uso:
  python3 noticias.py                                  # r/opencode
  python3 noticias.py --subreddit opencodeCLI          # el otro sub
  python3 noticias.py --top 30                         # mas hilos en el resumen
  python3 noticias.py --desde 2026-10-10                # forzar inicio del rango

Los volcados se identifican por su meta.subreddit, asi que cada sub lleva su propio
"ultimo dato conocido" y no se pisan entre ellos.
"""
import argparse, glob, json, os, subprocess, sys, datetime, collections

HERE = os.path.dirname(os.path.abspath(__file__))
ap = argparse.ArgumentParser()
ap.add_argument("--subreddit", default="opencode")
ap.add_argument("--top", type=int, default=20)
ap.add_argument("--desde", help="forzar fecha inicial YYYY-MM-DD (por defecto: ultimo dato conocido)")
a = ap.parse_args()

def ts(u):
    return datetime.datetime.fromtimestamp(u, datetime.UTC)

# 1) ultimo dato conocido en los volcados de ESTE subreddit
ultimo = 0
for fn in glob.glob(os.path.join(HERE, "hilos-*.json")):
    if "huerfanos" in fn:
        continue
    try:
        d = json.load(open(fn, encoding="utf-8"))
    except Exception:
        continue
    if (d.get("meta") or {}).get("subreddit") != a.subreddit:
        continue
    for t in d.get("threads", []):
        ultimo = max(ultimo, t["created_utc"])
if not ultimo:
    sys.exit(f"no hay volcados de r/{a.subreddit}: ejecuta fetch.py --subreddit {a.subreddit}")

inicio = a.desde or ts(ultimo).strftime("%Y-%m-%d")
fin = (datetime.datetime.now(datetime.UTC) + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
prefix = f"hilos-{a.subreddit}-desde-{inicio}"
print(f"subreddit: r/{a.subreddit}")
print(f"ultimo dato conocido: {ts(ultimo):%Y-%m-%d %H:%M} UTC")
print(f"scraping {inicio} -> {fin} (ahora {datetime.datetime.now(datetime.UTC):%Y-%m-%d %H:%M} UTC)\n", flush=True)

# 2) scraping incremental (reutiliza fetch.py)
cmd = [sys.executable, os.path.join(HERE, "fetch.py"), "--subreddit", a.subreddit,
       "--after", inicio, "--before", fin, "--prefix", prefix, "--orphans"]
subprocess.run(cmd, check=True)

# 3) resumen
d = json.load(open(os.path.join(HERE, f"{prefix}.json"), encoding="utf-8"))
threads = d["threads"]
nuevos = [t for t in threads if t["created_utc"] > ultimo]
print("\n" + "=" * 90)
print(f"POSTS NUEVOS desde {ts(ultimo):%Y-%m-%d %H:%M} UTC: {len(nuevos)}")
por_dia = collections.Counter(ts(t["created_utc"]).strftime("%m-%d") for t in nuevos)
print("por dia:", dict(sorted(por_dia.items())))

def linea(t):
    return (f"[{t['score']:>4}↑ {t['num_comments']:>3}c {ts(t['created_utc']):%m-%d %H:%M}] "
            f"{t['title'][:105]}\n      {t['permalink_url']}")

print(f"\n--- TOP {a.top} POR SCORE ---")
for t in sorted(nuevos, key=lambda x: -(x.get("score") or 0))[:a.top]:
    print(linea(t))
    cuerpo = " ".join((t.get("selftext") or "").split())[:200]
    if cuerpo:
        print(f"      {cuerpo}")

print("\n--- MAS RECIENTES ---")
for t in sorted(nuevos, key=lambda x: -x["created_utc"])[:a.top]:
    print(linea(t))

print("\n--- COMENTARIOS NUEVOS CON MAS SCORE ---")
coms = [(c, t["title"]) for t in threads for c in t["comments"]]
for c, titulo in sorted(coms, key=lambda x: -(x[0].get("score") or 0))[:15]:
    print(f"[{c['score']}↑ {ts(c['created_utc']):%m-%d %H:%M}] ({titulo[:45]}) "
          f"u/{c['author']}: {' '.join((c['body'] or '').split())[:210]}")
