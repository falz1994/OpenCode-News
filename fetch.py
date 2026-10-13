#!/usr/bin/env python3
"""Volcar hilos + comentarios de un subreddit en un rango de fechas via Arctic Shift API.

Ejemplos:
  python3 fetch.py                                     # r/opencode, 2026-09-08 .. 2026-10-09
  python3 fetch.py --after 2026-10-08 --before 2026-10-13 --prefix hilos-ultimos-dias --orphans
"""
import argparse, json, time, urllib.request, urllib.parse, datetime, sys, os

BASE = "https://arctic-shift.photon-reddit.com/api"
LIMIT = 100
OUT = os.path.dirname(os.path.abspath(__file__))

ap = argparse.ArgumentParser()
ap.add_argument("--subreddit", default="opencode")
ap.add_argument("--after", default="2026-09-08", help="desde (YYYY-MM-DD)")
ap.add_argument("--before", default="2026-10-09", help="hasta, exclusivo (YYYY-MM-DD)")
ap.add_argument("--prefix", default="hilos-ultimo-mes", help="nombre base de salida")
ap.add_argument("--orphans", action="store_true",
                help="volcar tambien los comentarios cuyo hilo quedo fuera del rango")
args = ap.parse_args()

SUBREDDIT = args.subreddit
AFTER = args.after
BEFORE = args.before
PREFIX = args.prefix
END_TS = int(datetime.datetime.fromisoformat(BEFORE).replace(tzinfo=datetime.UTC).timestamp())

def get(path, params):
    url = f"{BASE}/{path}?" + urllib.parse.urlencode(params)
    for attempt in range(5):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "research-script/1.0"})
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r)
        except Exception as e:
            wait = 2 ** attempt
            print(f"  retry {attempt+1} ({e}) wait {wait}s", flush=True)
            time.sleep(wait)
    raise RuntimeError(f"failed: {url}")

def paginate(kind, extra):
    """kind: posts|comments. Sort asc, paginate by created_utc, dedupe by id."""
    items, seen, after = [], set(), AFTER
    while True:
        data = get(f"{kind}/search", {"subreddit": SUBREDDIT, "after": after,
                                      "before": BEFORE, "limit": LIMIT,
                                      "sort": "asc", **extra})["data"]
        if not data:
            break
        new = [d for d in data if d["id"] not in seen]
        for d in new:
            seen.add(d["id"])
        items.extend(new)
        last_ts = max(d["created_utc"] for d in data)
        print(f"  {kind}: +{len(new)} (total {len(items)}) @ {datetime.datetime.fromtimestamp(last_ts, datetime.UTC):%Y-%m-%d %H:%M}", flush=True)
        if not new:  # boundary same-second: avanza 1s
            last_ts += 1
        if len(data) < LIMIT and last_ts >= END_TS - 1:
            break
        after = last_ts
        time.sleep(0.4)
    return items

print("== Posts ==", flush=True)
posts = paginate("posts", {})
print("== Comments ==", flush=True)
comments = paginate("comments", {})
print(f"posts={len(posts)} comments={len(comments)}", flush=True)

# agrupa comentarios por hilo
by_thread = {}
for c in comments:
    by_thread.setdefault(c.get("link_id", ""), []).append(c)

def ts(u):
    return datetime.datetime.fromtimestamp(u, datetime.UTC).isoformat()

def clean_post(p):
    return {k: p.get(k) for k in (
        "id", "title", "author", "created_utc", "created", "selftext", "score",
        "ups", "downs", "num_comments", "permalink", "url", "is_self",
        "subreddit", "link_flair_text", "edited", "over_18", "domain")} | {
        "created_iso": ts(p["created_utc"]),
        "permalink_url": "https://www.reddit.com" + (p.get("permalink") or f"/r/{SUBREDDIT}/comments/{p['id']}/"),
    }

def clean_comment(c):
    return {k: c.get(k) for k in (
        "id", "author", "body", "score", "ups", "downs", "parent_id",
        "link_id", "created_utc", "permalink", "edited", "depth")} | {
        "created_iso": ts(c["created_utc"]),
    }

# ordena comentarios por hilo y anida replies
def thread_comments(pid):
    cs = by_thread.get(f"t3_{pid}", [])
    by_id = {c["id"]: c for c in cs}
    kids = {}
    for c in cs:
        par = c.get("parent_id", "")
        key = par[3:] if par.startswith("t1_") else None
        kids.setdefault(key, []).append(c)
    for v in kids.values():
        v.sort(key=lambda x: x["created_utc"])
    out, seen = [], set()

    def dfs(node, d):
        if node["id"] in seen:
            return
        seen.add(node["id"])
        out.append(clean_comment(node) | {"depth": d})
        for k in kids.get(node["id"], []):
            dfs(k, d + 1)

    for root in kids.get(None, []):
        dfs(root, 0)
    # huérfanos (padre fuera del conjunto)
    for c in sorted(cs, key=lambda x: x["created_utc"]):
        if c["id"] not in seen:
            dfs(c, 0)
    return out

hilos = []
for p in sorted(posts, key=lambda x: -x["created_utc"]):
    rec = clean_post(p)
    rec["comments"] = thread_comments(p["id"])
    hilos.append(rec)

meta = {
    "subreddit": SUBREDDIT,
    "range": f"{AFTER} .. {BEFORE}",
    "fetched_at": datetime.datetime.now(datetime.UTC).isoformat(),
    "posts": len(hilos),
    "comments": sum(len(h["comments"]) for h in hilos),
    "source": "arctic-shift.photon-reddit.com",
}
doc = {"meta": meta, "threads": hilos}
with open(os.path.join(OUT, f"{PREFIX}.json"), "w", encoding="utf-8") as f:
    json.dump(doc, f, ensure_ascii=False, indent=1)

# comentarios cuyo hilo no esta en este volcado (hilos anteriores al rango)
used = {c["id"] for h in hilos for c in h["comments"]}
orphans = [clean_comment(c) | {"link_id": c.get("link_id", "")}
           for c in sorted(comments, key=lambda x: -x["created_utc"]) if c["id"] not in used]
if args.orphans:
    with open(os.path.join(OUT, f"{PREFIX}-comentarios-huerfanos.json"), "w", encoding="utf-8") as f:
        json.dump({"meta": meta | {"comments": len(orphans), "nota": "hilos fuera del rango"},
                   "comments": orphans}, f, ensure_ascii=False, indent=1)
print(f"huerfanos={len(orphans)}", flush=True)

# Markdown
def md(s):
    return (s or "").replace("\r", "").rstrip()

lines = [f"# r/{SUBREDDIT} — hilos {AFTER} → {BEFORE}",
         f"_Generado: {meta['fetched_at']} · {meta['posts']} hilos · {meta['comments']} comentarios · fuente: Arctic Shift_", ""]
for h in hilos:
    lines.append(f"## {h['title']}")
    lines.append(f"**u/{h['author']}** · {h['created_iso'][:16].replace('T',' ')} UTC · ↑{h['score']} · {h['num_comments']} comentarios · [enlace]({h['permalink_url']})")
    lines.append("")
    if h["selftext"]:
        lines.append(md(h["selftext"]))
        lines.append("")
    if h["comments"]:
        lines.append("**Comentarios:**")
        lines.append("")
        for c in h["comments"]:
            indent = "  " * c.get("depth", 0)
            body = md(c["body"]).replace("\n", "\n" + indent + "    ")
            lines.append(f"{indent}- **u/{c['author']}** (↑{c['score']}, {c['created_iso'][:16].replace('T',' ')}): {body}")
        lines.append("")
    lines.append("---")
    lines.append("")
with open(os.path.join(OUT, f"{PREFIX}.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print("OK:", json.dumps(meta, ensure_ascii=False))
