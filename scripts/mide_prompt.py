#!/usr/bin/env python3
"""Mide el system prompt real de una sesion y lo desglosa por seccion, EN BYTES.

Por que existe: el prompt lleva acentos y guiones largos, asi que un caracter no
es un byte. Si se mezclan indices de caracter con rebanadas de texto las cuentas
salen infladas. Todo aqui se hace sobre `text.encode()`.

Como atribuye los bytes: `renderPrompt` une las secciones no vacias con "\\n\\n".
Las secciones de tamano fijo se localizan por su texto de arranque; la guia de
herramientas (una seccion por herramienta montada, tamano variable) se obtiene
por resta, que es exacta porque los otros tramos son fijos.

Uso:
  zstd -dc -- <sesion>/session.v3.jsonl.zstd | python3 scripts/mide_prompt.py
  zstd -dc -- <sesion>/session.v3.jsonl.zstd | python3 scripts/mide_prompt.py --json
"""
import argparse, json, sys

IDENT = "You are an AI agent powered by DeepSeek Harness."
EXT = "HYPERFRAMES EDUCATIVO — CAPA COMPARTIDA OBLIGATORIA"
FILEREF = "Tokens prefixed with @ are workspace paths the user explicitly referenced"
TOOLS = "Check the [exit code: N] marker on every bash result"
SRC = "The DeepSeek Harness implementation checkout is at"
WEB = "You are interacting with the user through the DeepSeek Harness Web GUI"
SUF = "Your working directory is "


def B(s):
    return s.encode("utf-8")


def lee_prompt(stream):
    for linea in stream:
        try:
            e = json.loads(linea)
        except Exception:
            continue
        if e.get("type") == "system/message":
            t = "".join(c.get("text", "") for c in e["data"]["message"]["content"])
            if t.strip():
                return t
    return None


def mide(prompt):
    b = B(prompt)
    secciones = []

    def agrega(nombre, ini, fin, orden=None, nota=None):
        trozo = b[ini:fin]
        s = {"nombre": nombre, "bytes": len(trozo), "orden": orden}
        if nota:
            s["nota"] = nota
        secciones.append(s)
        return len(trozo)

    # --- tramos de tamano fijo, localizados por su arranque ---
    i_ident = len(B(IDENT))                       # identity ocupa el inicio exacto
    i_fr = b.index(B(FILEREF))
    i_tools = b.index(B(TOOLS))
    i_src = b.index(B(SRC))
    i_web = b.index(B(WEB))
    i_suf = b.rindex(B("\n\n" + SUF)) + 2         # el suffix cierra el prompt

    # bloques contiguos antes de la guia: cada uno se corta en el siguiente marcador
    n_fr = i_tools - i_fr                         # file-reference + separador
    n_src = i_web - i_src                         # harness:source + separador
    n_web = i_suf - 2 - i_web                     # web-surface

    agrega("harness:identity", 0, i_ident, -1000)
    i_pers_ini = i_ident + 2

    if B(EXT) in b:
        # CON preset: el slot persona-prefix lo ocupa el preset y la seccion
        # `preset:` es COMPUESTA por la extension + la guia de sus modulos.
        i_ext = b.index(B(EXT))
        n_pers = i_ext - 2 - i_pers_ini
        compuesto = (i_suf - 2) - i_ext
        agrega("deployment:persona-prefix", i_pers_ini, i_ext - 2, 0)
        agrega("preset: (compuesta)", i_ext, i_suf - 2, 100,
               "la extension registra orden 100 y las secciones de sus modulos caen en el mismo tramo")
        agrega("  · extension del preset", i_ext, i_fr, 100)
        agrega("  · guia de sus herramientas", i_fr, i_suf - 2, 100,
               "referencia de archivos + una seccion por herramienta montada")
        agrega("     - file-reference", i_fr, i_tools, 900,
               "incluye los 2 B del separador que lo une a las herramientas")
        # En este tramo solo la referencia de archivos es fija: el preset NO
        # monta harness:source ni web-surface como secciones aparte.
        base = n_fr
    else:
        # SIN preset: persona de 64 B y despues la guia de herramientas completa.
        n_pers = i_fr - 2 - i_pers_ini
        agrega("deployment:persona-prefix", i_pers_ini, i_fr - 2, 0)
        agrega("guia de herramientas", i_fr, i_suf - 2, 1000)
        # Cada tramo fijo incluye el separador que lo une al siguiente, para que
        # la suma de los tramos sea exactamente el total de la guia.
        agrega("     - file-reference", i_fr, i_tools, 900,
               "incluye los 2 B del separador que lo une a las herramientas")
        agrega("     - harness:source", i_src, i_web, 10000,
               "incluye los 2 B del separador que lo une a web-surface")
        agrega("     - web-surface", i_web, i_suf - 2, 10100)
        base = n_fr + n_src + n_web

    # la guia de herramientas por resta: el resto del tramo son las herramientas
    clave = "  · guia de sus" if B(EXT) in b else "guia de herramientas"
    idx = next(i for i, s in enumerate(secciones) if clave in s["nombre"])
    secciones[idx]["bytes_herramientas"] = secciones[idx]["bytes"] - base

    agrega("deployment:persona-suffix", i_suf, len(b), 10200)

    suma = sum(s["bytes"] for s in secciones if not s["nombre"].startswith(("  · ", "     - ")))
    return {"total": len(b), "secciones": secciones,
            "suma_secciones": suma, "separadores": len(b) - suma}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    prompt = lee_prompt(sys.stdin)
    if prompt is None:
        raise SystemExit("no se encontro un system/message no vacio en la entrada")
    d = mide(prompt)
    if a.json:
        print(json.dumps(d, ensure_ascii=False, indent=1))
        return
    print(f"system prompt = {d['total']} bytes")
    for s in d["secciones"]:
        orden = f"orden {s['orden']}" if s["orden"] is not None else ""
        extra = ""
        if "bytes_herramientas" in s:
            extra = f"  (de eso, herramientas: {s['bytes_herramientas']} B)"
        print(f"  {s['bytes']:7d} B  {orden:>12s}  {s['nombre']}{extra}")
    print(f"  {d['suma_secciones']:7d} B  {'':>12s}  suma de secciones")
    print(f"  {d['separadores']:7d} B  {'':>12s}  separadores (\\n\\n entre secciones)")


if __name__ == "__main__":
    main()
