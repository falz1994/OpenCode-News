#!/usr/bin/env python3
"""Lee los presets de DSH instalados y genera la fuente del frame "Presets".

Fuente:  ~/.dsh/.agent-presets/<preset>/preset.yml        (nombre, descripcion, orden)
         ~/.dsh/.agent-presets/<preset>/agent.cordis.yml  (grafo de modulos)
Salida:  presets.json  (lo consume index_datos.py -> datos.json -> index.html)

No inventa nada: la descripcion sale del preset.yml; los rasgos se cuentan del
agent.cordis.yml resolviendo la herencia (inherit-composition.js -> path) e
ignorando los modulos con `disabled: true`. Los "escenarios" son curados aqui
abajo, porque no estan en los ficheros.

Uso:
  python3 presets.py
  python3 presets.py --dir ~/.dsh/.agent-presets
"""
import argparse, json, os, re, glob, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ap = argparse.ArgumentParser()
ap.add_argument("--dir", default=os.path.expanduser("~/.dsh/.agent-presets"))
a = ap.parse_args()

ESCENARIOS = {
    "hyperframes educativo": {
        "cuando": [
            "Piezas educativas cortas o medianas que querés cerrar de una tirada.",
            "Cuando el modelo que ya elegiste en la sesión basta para producir y verificar.",
            "Cuando NO querés depender del router local ni de cuota compartida.",
        ],
        "evitar": "Producciones largas con muchas iteraciones de render: el modelo principal hace todo y su cuota se agota.",
    },
    "hyperframes orquestador educativo": {
        "cuando": [
            "Series o piezas educativas largas, con varias escenas y verificaciones visuales.",
            "Cuando querés que el modelo principal dirija y verifique y que el render lo haga otro.",
            "Cuando la cuota del modelo principal es escasa y hay que repartir el trabajo.",
        ],
        "evitar": "Tareas de un solo paso: montar la orquestación cuesta más que hacerlas directamente.",
    },
    "orquestador": {
        "cuando": [
            "Trabajo pesado multi-archivo que conviene sacar del modelo principal (cuota, coste o paralelismo).",
            "Investigación + implementación donde el root debe leer, comparar y decidir, no escribir.",
            "Cuando querés la garantía de que la raíz no toca archivos: todo lo producido pasa por un hijo.",
        ],
        "evitar": "Preguntas o cambios de una línea: la delegación añade latencia y el hijo no ve la conversación.",
    },
}


def bloques(txt):
    """Cada modulo del cordis.yml empieza en '- ' a nivel raiz."""
    return [b for b in re.split(r"\n(?=- )", txt) if b.strip()]


def activo(b):
    """`disabled: true` lo excluye; `disabled: !!js ...` es condicional (cuenta)."""
    return not re.search(r"^\s*disabled:\s*true\s*$", b, re.M)


def largo_prefix(b):
    m = re.search(r"prefix:\s*\|", b)
    if not m:
        return 0
    lineas = []
    for linea in b[m.end():].splitlines():
        if linea.startswith("- ") or linea.strip().startswith("config:"):
            break
        lineas.append(linea)
    return len("\n".join(lineas).strip())


def rasgos(rutas):
    """Cuenta modulos activos sobre el preset y sus bases heredadas."""
    textos = []
    for r in rutas:
        try:
            textos.append(open(r, encoding="utf-8").read())
        except Exception:
            pass
    todo = "\n".join(textos)
    herramientas, skills, plugins, grupos, condicionales = set(), set(), set(), 0, []
    persona, largo, maxbytes = False, 0, None
    for txt in textos:
        for b in bloques(txt):
            if not activo(b):
                continue
            if re.search(r"disabled:\s*!!js", b):
                nom = (re.search(r"name:\s*'?([^'\n]+)'?", b) or [None, "?"])[1]
                condicionales.append(nom.strip())
            for t in re.findall(r"@deepseek-ai/dsh-tool-([a-z0-9-]+)", b):
                herramientas.add(t)
            for s in re.findall(r"@deepseek-ai/dsh-(skill-filesystem|tool-skill)", b):
                skills.add(s)
            plugins.update(re.findall(r"name:\s*\./([A-Za-z0-9._-]+\.(?:js|mjs))", b))
            if "cordis:group" in b:
                grupos += 1
            if "dsh-persona" in b:
                persona = True
                largo = max(largo, largo_prefix(b))
            m = re.search(r"maxBytes:\s*(\d+)", b)
            if m and "agent-instructions" in b:
                maxbytes = int(m.group(1))
    return {
        "persona_propia": persona,
        "largo_prompt_persona": largo,
        "instrucciones_max_bytes": maxbytes,
        "plugins": sorted(plugins),
        "herramientas": sorted(herramientas),
        "skills": sorted(skills),
        "grupos": grupos,
        "read_only": bool(re.search(r"read-?only", todo, re.I)),
        "watchdog": any("watchdog" in p for p in plugins),
        "observador_limites": any("limit" in p for p in plugins),
        "menciona_omniroute": "omniroute" in todo.lower(),
        "condicionales": sorted(set(condicionales)),
        "delegacion_vaciada": bool(re.search(r"id:\s*delegation\s*\n\s*config:\s*\[\s*\]", todo)),
    }


def heredadas(ruta_agent):
    """Sigue `path:` de los modulos inherit-composition."""
    try:
        txt = open(ruta_agent, encoding="utf-8").read()
    except Exception:
        return []
    base = os.path.dirname(ruta_agent)
    fuera = []
    for m in re.finditer(r"path:\s*([^\s]+\.cordis\.yml)", txt):
        p = os.path.normpath(os.path.join(base, m.group(1)))
        if os.path.exists(p):
            fuera.append(p)
    return fuera


presets = []
for d in sorted(glob.glob(os.path.join(a.dir, "*"))):
    if not os.path.isdir(d) or os.path.basename(d).startswith("_"):
        continue
    py = os.path.join(d, "preset.yml")
    if not os.path.exists(py):
        continue
    txt = open(py, encoding="utf-8").read()
    nombre = (re.search(r"^name:\s*(.+)$", txt, re.M) or [None, os.path.basename(d)])[1].strip()
    orden = re.search(r"^order:\s*(\d+)", txt, re.M)
    desc = re.search(r"^description:\s*>-\s*\n((?:\s{2,}.*\n?)+)", txt, re.M)
    descripcion = " ".join(desc.group(1).split()) if desc else ""
    agente = os.path.join(d, "agent.cordis.yml")
    bases = heredadas(agente)
    esc = ESCENARIOS.get(nombre.lower(), {})
    presets.append({
        "id": os.path.basename(d),
        "nombre": nombre,
        "orden": int(orden.group(1)) if orden else None,
        "descripcion": descripcion,
        "cuando": esc.get("cuando", []),
        "evitar": esc.get("evitar", ""),
        "ruta": d,
        "hereda_de": [os.path.relpath(b, a.dir) for b in bases],
        "rasgos": rasgos([agente] + bases),
    })

presets.sort(key=lambda p: (p["orden"] is None, p["orden"] or 0, p["nombre"]))

doc = {
    "titulo": "Presets de DSH: cómo trabaja el agente",
    "fuente": a.dir,
    "actualizado": datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%d %H:%M UTC"),
    "nota": "Un preset no es un modelo: es la configuración con la que arranca la sesión "
            "(persona, instrucciones, herramientas, políticas y delegación). Se elige antes de crear la sesión.",
    "presets": presets,
}
with open(os.path.join(HERE, "presets.json"), "w", encoding="utf-8") as f:
    json.dump(doc, f, ensure_ascii=False, indent=1)

print(f"{len(presets)} presets desde {a.dir}")
for p in presets:
    r = p["rasgos"]
    print(f"  · {p['nombre']} (orden {p['orden']})"
          f"{' ← hereda de ' + ', '.join(p['hereda_de']) if p['hereda_de'] else ''}")
    print(f"      plugins={len(r['plugins'])} herramientas={len(r['herramientas'])} grupos={r['grupos']} "
          f"read_only={r['read_only']} watchdog={r['watchdog']} prompt_persona={r['largo_prompt_persona']}B")
