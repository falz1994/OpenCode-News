#!/usr/bin/env python3
"""Comprueba que cada enlace a un hilo de Reddit en los titulares apunta a un hilo real.

Los titulares de `fuente.json` se escriben a mano y llevan enlaces a hilos. Es facil
construir uno «a ojo» a partir del titulo y que no exista: este script compara el id
de cada enlace con los ids de los volcados y falla si alguno no aparece.

Uso:
  python3 valida_enlaces.py
"""
import glob
import json
import re
import sys

RUTA = "fuente.json"


def ids_conocidos():
    """Ids de todos los hilos de los volcados (sin los de comentarios huérfanos)."""
    ids = set()
    for fn in sorted(glob.glob("hilos-*.json")):
        if "huerfanos" in fn:
            continue
        try:
            d = json.load(open(fn, encoding="utf-8"))
        except Exception:
            continue
        for t in d.get("threads", []):
            ids.add(t["id"])
    return ids


def enlaces(fuente):
    """(titular, url) de cada enlace a un hilo de Reddit en los titulares."""
    for fila in fuente.get("titulares", {}).get("filas", []):
        for celda in fila:
            if not isinstance(celda, str):
                continue
            for m in re.finditer(r"reddit\.com/r/(\w+)/comments/([a-z0-9]+)", celda):
                yield fila[1], m.group(0), m.group(1), m.group(2)


def main():
    ids = ids_conocidos()
    if not ids:
        sys.exit("no hay volcados: ejecuta fetch.py primero")

    fuente = json.load(open(RUTA, encoding="utf-8"))
    subreddits = {(d.get("meta") or {}).get("subreddit") for d in
                  (json.load(open(fn, encoding="utf-8")) for fn in glob.glob("hilos-*.json")
                   if "huerfanos" not in fn)}

    malos, total = [], 0
    for titular, url, sub, id_hilo in enlaces(fuente):
        total += 1
        if id_hilo not in ids:
            malos.append((titular, url, "el hilo no está en ningún volcado"))
        elif sub not in subreddits:
            malos.append((titular, url, f"r/{sub} no tiene volcados"))

    print(f"hilos conocidos: {len(ids)} · enlaces revisados: {total}")
    if malos:
        print("\nENLACES QUE NO CUADRA:")
        for titular, url, motivo in malos:
            print(f"  · {titular[:60]}\n      {url}\n      {motivo}")
        return 1
    print("OK: todos los enlaces apuntan a hilos reales")
    return 0


if __name__ == "__main__":
    sys.exit(main())
