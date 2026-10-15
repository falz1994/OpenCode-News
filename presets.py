#!/usr/bin/env python3
"""Lee los presets de DSH instalados y genera la fuente del frame "Presets".

Fuente:  ~/.dsh/.agent-presets/<preset>/preset.yml        (nombre, descripcion, orden)
         ~/.dsh/.agent-presets/<preset>/agent.cordis.yml  (grafo de modulos)
Salida:  presets.json  (lo consume index_datos.py -> datos.json -> index.html)

No inventa nada: la descripcion sale del preset.yml; los rasgos se cuentan del
agent.cordis.yml resolviendo la herencia (inherit-composition.js -> path) e
ignorando los modulos con `disabled: true`. Los "escenarios" son curados aqui
abajo, porque no estan en los ficheros.

Los bytes del prompt de persona se miden del propio YAML: se toma el bloque
`prefix: |` / `prefix: |-` y se descartan el indicador de chomping y el
sangrado comun. Un `|-` mal recortado cuenta dos bytes de mas (el guion y el
salto), asi que la medida se hace con `bloque_escalar()`.

Uso:
  python3 presets.py
  python3 presets.py --dir ~/.dsh/.agent-presets
"""
import argparse, json, os, re, glob, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ap = argparse.ArgumentParser()
ap.add_argument("--dir", default=os.path.expanduser("~/.dsh/.agent-presets"))
ap.add_argument("--verifica", action="store_true",
                help="contrasta la cuenta del prefix contra PyYAML y termina")
a = ap.parse_args()

PRESET_STANDARD = "standard"          # preset base del que hereda el educativo directo
PRESET_ORQUESTADOR = "orchestrator"   # preset que se usa como ejemplo en la simulacion

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

# Que hace cada preset cuando el trabajo pesa. Se lee del grafo, no se supone.
DELEGACION = {
    "omniroute_code": {
        "mecanismo": "un hijo in-process (omniroute_code)",
        "escribe": "el hijo escribe; la raíz queda read-only",
        "carriles": "router local OmniRoute, combo `code` con failover propio",
    },
    "subagent": {
        "mecanismo": "subagentes in-process (subagent, subagent_fork, workflow, ralph)",
        "escribe": "el modelo principal escribe directamente en el workspace",
        "carriles": "el modelo de la sesión, sin router",
    },
    "ninguna": {
        "mecanismo": "ninguna: el modelo principal produce todo",
        "escribe": "el modelo principal escribe directamente en el workspace",
        "carriles": "el modelo de la sesión, sin router",
    },
}

# Que hace cada plugin, para no decir solo "plugin del preset".
PLUGINS = {
    "orchestrator-readonly-policy-v2.js": "Fija la sesión en read-only al arrancar y lo reafirma en cada pre-step",
    "orchestrator-job-watchdog.js": "Vigila los jobs hijos por señales de vida reales",
    "omniroute-limit-observer.js": "Registra límites y pone el modelo que falla en cuarentena",
    "orchestrator-spawn-provider.js": "Aporta el spawn del hijo in-process (omniroute_code)",
}

# Modulos de herramienta que monta el PERFIL BASE del harness (sin preset).
# Fuente: node_modules/@deepseek-ai/dsh-base/cordis.patch.yml del checkout de DSH.
# Se listan en vez de contarse con una regex sobre ese fichero porque el patch
# usa `patch:`/`replace:` y contar coincidencias daria un numero distinto al que
# el host monta de verdad; esta lista es la de los modulos nombrados alli.
# Persona del preset que el roster usa por defecto (`standard`, el que trae el
# paquete dsh-agent-presets). Fuente:
# node_modules/@deepseek-ai/dsh-agent-presets/presets/standard/agent.cordis.yml
PERSONA_DEFAULT = "You are a coding agent powered by the {{model}} model."
SUFFIX_DEFAULT = "Your working directory is {{cwd}}."
MODELO_MEDIDO = "deepseek-v4.1-flash"
CWD_MEDIDO = "/home/devni/imagen/reddit-opencode"

HERRAMIENTAS_BASE = ["bash", "pwsh", "jobs", "fs", "fs-search", "skill", "todo",
                     "goal", "web", "subagent-control", "subagent", "workflow", "ralph"]

# ---------------------------------------------------------------- medicion real
# Estos numeros NO se calculan: se midieron leyendo el `system/message` de dos
# sesiones reales del disco. Son la evidencia de la simulacion. Para repetir la
# medicion sobre cualquier sesion:
#
#   zstd -dc -- <sesion>/session.v3.jsonl.zstd | python3 -c "
#   import sys,json
#   for l in sys.stdin:
#       e=json.loads(l)
#       if e.get('type')=='system/message':
#           t=''.join(c.get('text','') for c in e['data']['message']['content'])
#           if t.strip(): print(len(t.encode()),'bytes'); print(t); break"
#
MEDICION = {
    "con_preset": {
        "preset": "hyperframes-educativo",
        "sesion": "~/.dsh/sessions/--home-devni-imagen-reddit-opencode--/"
                  "session-6408e2f7-ef2b-4f09-9c38-d647de84990b",
        "cwd": "/home/devni/imagen/reddit-opencode",
        "total": 28704,
        "secciones": [
            {"nombre": "harness:identity", "orden": -1000, "bytes": 48,
             "texto": "You are an AI agent powered by DeepSeek Harness."},
            {"nombre": "deployment:persona-prefix", "orden": 0, "bytes": 6565,
             "texto": "el `prefix` del preset, con {{model}} y {{cwd}} resueltos"},
            {"nombre": "preset:hyperframes-educativo", "orden": 100, "bytes": 22026,
             "texto": "sección que aporta hyperframes-prompt-extension.js (motion editorial + protocolo de calidad)"},
            {"nombre": "deployment:persona-suffix", "orden": 10200, "bytes": 61,
             "texto": "Your working directory is /home/devni/imagen/reddit-opencode."},
        ],
    },
    "sin_preset": {
        "preset": "standard (el default del roster: `agent-presets.default: standard`)",
        "sesion": "~/.dsh/sessions/--home-devni-imagen-reddit-opencode--/"
                  "session-d26f77b4-5e65-494a-a5e3-6c09858f9d4f",
        "cwd": "/home/devni/imagen/reddit-opencode",
        "total": 6902,
        "secciones": [
            {"nombre": "harness:identity", "orden": -1000, "bytes": 48,
             "texto": "You are an AI agent powered by DeepSeek Harness."},
            {"nombre": "deployment:persona-prefix", "orden": 0, "bytes": 64,
             "texto": "You are a coding agent powered by the deepseek-v4.1-flash model."},
            {"nombre": "guía de herramientas (tool:*, harness:source, web-surface)",
             "orden": 1000, "bytes": 6723,
             "texto": "18 secciones: read, write, edit, glob, grep, bash, jobs, web_search, web_fetch, goal, "
                      "workflow, ralph, subagent, subagent_fork, present, checkout, GUI…"},
            {"nombre": "deployment:persona-suffix", "orden": 10200, "bytes": 61,
             "texto": "Your working directory is /home/devni/imagen/reddit-opencode."},
        ],
    },
    # Reparto observado en las 80 sesiones mas recientes del disco (cabecera
    # `agentPreset` + evento `agent-preset/selected`).
    "reparto": [
        {"preset": "standard", "sesiones": 34,
         "nota": "default del roster; incluye las que no eligieron nada"},
        {"preset": "hyperframes-orquestador-educativo", "sesiones": 32},
        {"preset": "orchestrator", "sesiones": 14},
    ],
}

# Como se ensambla el system prompt. Los nombres de seccion y su orden salen de
# @deepseek-ai/dsh-system-prompt (SECTION_ORDERS) y de los modulos del preset.
ASSEMBLY = [
    {"orden": -1000, "seccion": "harness:identity",
     "nota": "Siempre presente; no lo cambia ningún preset (48 B medidos)."},
    {"orden": 0, "seccion": "deployment:persona-prefix",
     "nota": "Con preset: el `prefix` del módulo `persona`. Sin preset: el del preset por defecto "
             "(«You are a coding agent…», 64 B). Nunca se suman: la sección se reemplaza."},
    {"orden": 100, "seccion": "preset:… (extensiones del preset)",
     "nota": "Solo si el preset monta un plugin que registra secciones propias. La extensión educativa "
             "aporta 22.026 B en la sesión medida."},
    {"orden": 500, "seccion": "políticas (plan, equipo, PTC)",
     "nota": "Sólo si el preset monta esos módulos."},
    {"orden": 900, "seccion": "file-reference",
     "nota": "Cómo se referencian archivos en el mensaje (343 B medidos en el preset por defecto)."},
    {"orden": 1000, "seccion": "guía de herramientas (tool:bash, tool:read, tool:write, tool:glob, "
                               "tool:grep, tool:jobs, tool:web_search, tool:web_fetch, tool:goal, "
                               "tool:subagent, …)",
     "nota": "Una sección por herramienta montada. En el preset por defecto suman 6.723 B: es la pieza "
             "más grande de ese prompt."},
    {"orden": 10000, "seccion": "harness:source",
     "nota": "Cómo leer el propio harness (356 B medidos)."},
    {"orden": 10100, "seccion": "web-surface",
     "nota": "Cómo interactuar con la GUI web (995 B medidos)."},
    {"orden": 10200, "seccion": "deployment:persona-suffix",
     "nota": "`suffix` del módulo `persona` («Your working directory is {{cwd}}», 61 B resueltos)."},
]


def bloques(txt):
    """Cada modulo del cordis.yml empieza en '- ' a nivel raiz."""
    return [b for b in re.split(r"\n(?=- )", txt) if b.strip()]


def activo(b):
    """`disabled: true` lo excluye; `disabled: !!js ...` es condicional (cuenta)."""
    return not re.search(r"^\s*disabled:\s*true\s*$", b, re.M)


def bloque_escalar(b, clave):
    """Devuelve el texto de un bloque escalar YAML (`clave: |`, `|-`, `>-`).

    Quita el indicador de chomping y el sangrado comun. Sin esto, un `|-`
    deja un guion suelto como primera linea y la cuenta sube dos bytes.
    """
    m = re.search(rf"^\s*{clave}:\s*\|[-+]?\s*$", b, re.M)
    if not m:
        return ""
    lineas = []
    for linea in b[m.end():].splitlines():
        if linea.strip() and not linea.startswith(" "):
            break
        if linea.startswith("- ") or linea.strip().startswith("config:"):
            break
        lineas.append(linea)
    # La sangria del bloque la fija la PRIMERA linea con contenido: se quita
    # esa cantidad de cada linea y se conserva la indentacion relativa de las
    # listas anidadas. Contraste: PyYAML sobre el mismo fichero da el mismo
    # numero (ver `--verifica`).
    sangria = next((len(l) - len(l.lstrip(" ")) for l in lineas if l.strip()), 0)
    if sangria:
        lineas = [l[sangria:] if l[:sangria].strip() == "" else l for l in lineas]
    return "\n".join(lineas).strip()


def largo_prefix(b):
    return len(bloque_escalar(b, "prefix"))


def verifica():
    """Contrasta `bloque_escalar` con PyYAML sobre cada preset instalado.

    PyYAML no entiende el tag `!!js` del que dependen los condicionales, asi
    que se registra un constructor que lo lee como texto.
    """
    import yaml

    class Loader(yaml.SafeLoader):
        pass

    Loader.add_constructor("tag:yaml.org,2002:js", lambda l, n: l.construct_scalar(n))
    fallos = 0
    for d in sorted(glob.glob(os.path.join(a.dir, "*"))):
        if not os.path.isdir(d) or os.path.basename(d).startswith("_"):
            continue
        agente = os.path.join(d, "agent.cordis.yml")
        if not os.path.exists(agente):
            continue
        # Un wrapper no declara persona: la hereda de la base que apunta su
        # `inherit-composition`. Se verifica la base, que es la que aporta el texto.
        rutas = [agente] + heredadas(agente)
        leido = False
        for ruta in rutas:
            try:
                doc = yaml.load(open(ruta, encoding="utf-8"), Loader=Loader)
            except Exception as e:
                print(f"  · {os.path.basename(d)}: PyYAML no pudo leer {os.path.basename(ruta)} ({e})")
                continue
            filas = [b for b in doc if isinstance(b, dict) and b.get("id") == "persona"]
            if not filas:
                continue
            leido = True
            pre = filas[0]["config"]["prefix"]
            mio = bloque_escalar(open(ruta, encoding="utf-8").read(), "prefix")
            # PyYAML conserva el salto final que el bloque `|` agrega al valor;
            # el texto que se renderiza va sin el, asi que se comparan sin
            # espacios en los bordes.
            ok = mio.strip() == pre.strip()
            fallos += 0 if ok else 1
            etiqueta = os.path.basename(d) if ruta == agente else f"{os.path.basename(d)} (base {os.path.relpath(ruta, a.dir)})"
            print(f"  {'OK ' if ok else 'MAL'} {etiqueta}: "
                  f"yaml={len(pre.strip())}c/{len(pre.strip().encode())}B  "
                  f"regex={len(mio)}c/{len(mio.encode())}B")
        if not leido:
            print(f"  · {os.path.basename(d)}: sin modulo persona ni en el wrapper ni en su base")
    return fallos


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
    persona, largo, maxbytes, suffix = False, 0, None, ""
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
                suffix = bloque_escalar(b, "suffix") or suffix
            m = re.search(r"maxBytes:\s*(\d+)", b)
            if m and "agent-instructions" in b:
                maxbytes = int(m.group(1))
    deleg = delegacion(todo)
    return {
        "persona_propia": persona,
        "largo_prompt_persona": largo,
        "bytes_prompt_persona": len(bloque_escalar(todo, "prefix").encode("utf-8")) if persona else 0,
        "suffix_persona": suffix,
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
        "delegacion": deleg,
    }


def delegacion(todo):
    """Deduce del grafo qué vía de delegación queda montada, si alguna."""
    m = re.search(r"id:\s*delegation\s*\n\s*(?:name:[^\n]*\n\s*)?(?:group:[^\n]*\n\s*)?"
                  r"(?:isolate:\n(?:[ \t]+[^\n]*\n)*)?config:\s*\[\s*\]", todo)
    if m:
        return dict(DELEGACION["ninguna"], via="ninguna", herramientas=0)
    montadas = re.findall(r"toolName:\s*([A-Za-z0-9_]+)", todo)
    if "omniroute_code" in montadas:
        return dict(DELEGACION["omniroute_code"], via="omniroute_code",
                    herramientas=len(montadas))
    if "subagent" in montadas:
        return dict(DELEGACION["subagent"], via="subagent", herramientas=len(montadas))
    return dict(DELEGACION["ninguna"], via="ninguna", herramientas=len(montadas))


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


def leer_preset(d):
    """Carga un preset suelto del directorio de presets."""
    py = os.path.join(d, "preset.yml")
    if not os.path.exists(py):
        return None
    txt = open(py, encoding="utf-8").read()
    nombre = (re.search(r"^name:\s*(.+)$", txt, re.M) or [None, os.path.basename(d)])[1].strip()
    orden = re.search(r"^order:\s*(\d+)", txt, re.M)
    desc = re.search(r"^description:\s*>-\s*\n((?:\s{2,}.*\n?)+)", txt, re.M)
    descripcion = " ".join(desc.group(1).split()) if desc else ""
    agente = os.path.join(d, "agent.cordis.yml")
    bases = heredadas(agente)
    esc = ESCENARIOS.get(nombre.lower(), {})
    return {
        "id": os.path.basename(d),
        "nombre": nombre,
        "orden": int(orden.group(1)) if orden else None,
        "descripcion": descripcion,
        "cuando": esc.get("cuando", []),
        "evitar": esc.get("evitar", ""),
        "ruta": d,
        "hereda_de": [os.path.relpath(b, a.dir) for b in bases],
        "rasgos": rasgos([agente] + bases),
    }


# ---------------------------------------------------------------- simulacion
def secciones_prompt(pre, std):
    """Rellena el ensamblado con los bytes medidos en los ficheros reales."""
    out = []
    for s in ASSEMBLY:
        s = dict(s)
        if s["seccion"] == "deployment:persona-prefix":
            s["texto"] = f"{pre['rasgos']['largo_prompt_persona']} caracteres del `prefix` del preset"
            s["bytes"] = pre["rasgos"]["bytes_prompt_persona"]
            s["texto_sin_preset"] = "vacío (0 bytes): la sección se descarta al renderizar"
        elif s["seccion"] == "deployment:persona-suffix":
            suf = pre["rasgos"]["suffix_persona"]
            s["texto"] = f"`{suf}`" if suf else "vacío (0 bytes)"
            s["bytes"] = len(suf.encode("utf-8"))
            s["texto_sin_preset"] = "vacío (0 bytes)"
        elif s["seccion"] == "harness:identity":
            s["bytes"] = len(s["texto"].encode("utf-8"))
            s["texto_sin_preset"] = s["texto"]
        else:
            s["bytes"] = None
            s["texto_sin_preset"] = "igual en los dos casos (perfil base)"
        out.append(s)
    return out


def modulos(pre, std):
    """Modulos que monta cada escenario, indexados por modulo.

    Se devuelve un diccionario por escenario (no dos listas paralelas): las dos
    listas tienen distinta longitud y emparejarlas por posicion haria comparar
    un plugin del preset contra una fila que no le corresponde.
    """
    def filas(p, es_default=False):
        r = p["rasgos"]
        f = {}
        if es_default:
            resuelta = (PERSONA_DEFAULT.replace("{{model}}", MODELO_MEDIDO)
                        .replace("{{cwd}}", CWD_MEDIDO))
            f["persona"] = {
                "aporta": "System prompt del preset por defecto (`standard`)",
                "dato": f"«{resuelta}» — {len(resuelta.encode())} B",
            }
        else:
            f["persona"] = {
                "aporta": "System prompt propio del preset",
                "dato": (f"prefix de {r['largo_prompt_persona']:,} caracteres".replace(",", ".")
                         + (f" + suffix «{r['suffix_persona']}»" if r["suffix_persona"] else "")),
            }
        if es_default:
            f["persona (suffix)"] = {
                "aporta": "`deployment:persona-suffix`",
                "dato": f"«{SUFFIX_DEFAULT.replace('{{cwd}}', CWD_MEDIDO)}» — "
                        f"{len(SUFFIX_DEFAULT.replace('{{cwd}}', CWD_MEDIDO).encode())} B",
            }
        f["agent-instructions"] = {
            "aporta": "Instrucciones del proyecto (AGENTS.md y similares)",
            "dato": f"tope de {r['instrucciones_max_bytes'] // 1024} kB" if r["instrucciones_max_bytes"] else "—",
        }
        for p_ in r["plugins"]:
            f[p_] = {"aporta": PLUGINS.get(p_, "Plugin del preset"), "dato": "montado"}
        f["herramientas"] = {
            "aporta": "Módulos de herramienta del grafo",
            "dato": f"{len(r['herramientas'])} módulos: " + ", ".join(r["herramientas"]),
        }
        f["grupos cordis:group"] = {
            "aporta": "Plan mode, compactación y delegación",
            "dato": f"{r['grupos']} grupos",
        }
        d = r["delegacion"]
        f["grupo delegation"] = {
            "aporta": "Vía de producción del trabajo pesado",
            "dato": ("vaciado con `config: []`: no existe ninguna vía"
                     if r["delegacion_vaciada"] else d["mecanismo"]),
        }
        return f

    # El escenario "sin preset" es el perfil por defecto del harness: no tiene
    # los plugins ni el grupo de delegación del preset, y su persona es la del
    # deployment (vacia en esta instalación: dsh-base monta personaPrefix: '').
    default = {"id": "default", "nombre": "perfil por defecto",
               "rasgos": dict(std["rasgos"], plugins=[], largo_prompt_persona=0,
                              bytes_prompt_persona=0, suffix_persona="",
                              herramientas=HERRAMIENTAS_BASE,
                              grupos=2, delegacion_vaciada=False,
                              delegacion=dict(DELEGACION["subagent"]))}
    return {"con_preset": filas(pre), "sin_preset": filas(default, es_default=True)}


def build_simulacion(pre, std):
    """Traza de una sesion nueva: preset elegido frente a un request sin preset.

    Los numeros de bytes salen de `MEDICION` (dos sesiones reales leidas del
    disco); los del preset que se muestra salen de sus ficheros. Nada se estima.
    """
    r_pre = pre["rasgos"]
    mp = MEDICION["con_preset"]
    ms = MEDICION["sin_preset"]
    return {
        "titulo": "Simulación: mandar un mensaje en una sesión nueva",
        "intro": (
            "Qué se carga y qué se manda al prompt cuando abrís una sesión nueva y mandás un mensaje. "
            "La columna izquierda es una sesión con un preset elegido; la derecha, un request normal sin "
            "elegir nada. Los bytes del system prompt están medidos de dos sesiones reales del disco "
            "(las rutas están en cada columna): no son estimaciones."),
        "columnas": [
            {"id": "con_preset", "titulo": "Con un preset elegido",
             "sub": f"ejemplo medido: `{mp['preset']}` · system prompt de {mp['total']:,} B".replace(",", "."),
             "sesion": mp["sesion"], "total": mp["total"]},
            {"id": "sin_preset", "titulo": "Request normal, sin elegir preset",
             "sub": f"se compone con el default del roster: {ms['preset'].split(' (')[0]} · "
                    f"system prompt de {ms['total']:,} B".replace(",", "."),
             "sesion": ms["sesion"], "total": ms["total"]},
        ],
        "pasos": [
            {"n": 0, "titulo": "Elegís el preset (o no)",
             "con_preset": (f"El selector lee `preset.yml` de cada carpeta de `{a.dir}` y de los presets "
                            "que trae el propio paquete. Ese fichero solo aporta metadatos: nombre, "
                            "descripción y orden. Todavía no se carga código."),
             "sin_preset": ("No elegís nada. La sesión NO queda sin composición: el roster tiene un default "
                            "(`agent-presets.default: standard` en el perfil web) y se monta ese."),
             "fuente": "preset.yml · dsh-web-app/cordis.patch.yml"},
            {"n": 1, "titulo": "Se compone el grafo de módulos",
             "con_preset": (f"Se montan los módulos de `agent.cordis.yml`: persona, {len(r_pre['plugins'])} "
                            f"plugins, {len(r_pre['herramientas'])} módulos de herramienta y "
                            f"{r_pre['grupos']} grupos."),
             "sin_preset": ("Se montan los módulos del preset `standard` (el que trae el paquete): persona, "
                            "11 módulos de herramienta, 3 grupos y el grupo de delegación con `subagent`, "
                            "`subagent_fork`, `workflow` y `ralph`. Sin plugins de política."),
             "fuente": "agent.cordis.yml"},
            {"n": 2, "titulo": "Se ensambla el system prompt",
             "con_preset": (f"`deployment:persona-prefix` = {mp['secciones'][1]['bytes']:,} B del preset; "
                            "además su extensión aporta "
                            f"{mp['secciones'][2]['bytes']:,} B. Total medido: {mp['total']:,} B."
                            ).replace(",", "."),
             "sin_preset": (f"`deployment:persona-prefix` = {ms['secciones'][1]['bytes']} B: la persona del "
                            f"preset `standard` («You are a coding agent…»). La guía de herramientas pesa "
                            f"{ms['secciones'][2]['bytes']:,} B. Total medido: {ms['total']:,} B."
                            ).replace(",", "."),
             "fuente": "dsh-system-prompt · renderPrompt"},
            {"n": 3, "titulo": "Mandas el mensaje",
             "con_preset": ("Lo que ve el modelo es: system prompt + instrucciones del proyecto + contexto "
                            "de entorno + historial + TU MENSAJE."),
             "sin_preset": ("La misma forma, con el system prompt de 6.902 B. Tus ficheros NO viajan dentro: "
                            "entran solo si el modelo llama a una herramienta."),
             "fuente": "dsh-agent-loop"},
            {"n": 4, "titulo": "Primer request: dos mensajes aparte",
             "con_preset": ("Las instrucciones del proyecto (AGENTS.md, hasta 64 kB) y el contexto de entorno "
                            "(workspace, fecha, política de sandbox y de aprobación) van como mensajes "
                            "aparte, no dentro del system prompt."),
             "sin_preset": "Los mismos dos mensajes: no dependen del preset.",
             "fuente": "dsh-agent-instructions · runtime-context"},
            {"n": 5, "titulo": "Quién escribe",
             "con_preset": (f"{r_pre['delegacion']['escribe'].capitalize()}."
                            + (f" Carriles: {r_pre['delegacion']['carriles']}." if r_pre['delegacion'].get('carriles') else "")),
             "sin_preset": ("El modelo principal escribe directamente: `write`, `edit` y `bash` van al "
                            "sandbox del workspace. No hay pin read-only."),
             "fuente": "plugins del preset / sandbox"},
            {"n": 6, "titulo": "Cuota y verificación",
             "con_preset": (("Watchdog y observador de límites activos. " if r_pre["watchdog"] else "")
                            + "La verificación la hace la raíz leyendo evidencia."),
             "sin_preset": ("Una sola llamada al modelo de la sesión: sin router, sin failover y sin "
                            "cuarentenas. La verificación la hacés vos."),
             "fuente": "plugins del preset"},
            {"n": 7, "titulo": "¿Y si el preset elegido es «Standard»?",
             "con_preset": ("Elegir «Standard» a mano da exactamente la misma composición que no elegir nada: "
                            "es el default del roster. La diferencia aparece cuando elegís OTRO preset, porque "
                            "su composición reemplaza a la del default."),
             "sin_preset": ("Por eso la comparación honesta no es «con preset / sin preset», sino «con ESTE "
                            "preset / con el default». Un preset no se suma al default: lo reemplaza."),
             "fuente": "dsh-agent-presets"},
        ],
        "ensamblado": {
            "nota": ("Las secciones se interpolan y las vacías se descartan (`renderPrompt`). Con un preset, su "
                     "persona ocupa el mismo slot que la del deployment: la reemplaza, no se suma."),
            "medido": [dict(mp, etiqueta="con preset elegido"), dict(ms, etiqueta="sin elegir preset")],
            "orden_posible": [dict(x) for x in ASSEMBLY],
            "aparte": [
                {"que": "Instrucciones del proyecto (AGENTS.md / CLAUDE.md)",
                 "como": "mensaje de rol usuario con el baseline durable", "bytes": "hasta 64 kB"},
                {"que": "Contexto de entorno", "como": "snapshot «Current runtime context»",
                 "bytes": "no medido: workspace, fecha y textos de política"},
                {"que": "Catálogo de skills", "como": "secciones del system prompt",
                 "bytes": "según las skills disponibles"},
                {"que": "Historial de la sesión + tu mensaje", "como": "mensajes de rol usuario",
                 "bytes": "según la conversación"},
            ],
        },
        "modulos": modulos(pre, std),
        "reparto": MEDICION["reparto"],
        "no_hace": [
            "No cambia el modelo de la sesión ni la cuota: el modelo lo elige la sesión, el preset decide cómo trabaja.",
            "No mete tus archivos dentro del prompt: eso lo decide el modelo llamando a herramientas.",
            "No comparte tu conversación con los hijos: cada hijo recibe un prompt nuevo y autocontenido.",
            "No sobrevive a la sesión: se aplica al crearla, no se puede cambiar a mitad.",
        ],
    }


# ---------------------------------------------------------------- recoleccion
if a.verifica:
    raise SystemExit(1 if verifica() else 0)

presets, por_id = [], {}
for d in sorted(glob.glob(os.path.join(a.dir, "*"))):
    if not os.path.isdir(d) or os.path.basename(d).startswith("_"):
        continue
    p = leer_preset(d)
    if p:
        presets.append(p)
        por_id[p["id"]] = p

presets.sort(key=lambda p: (p["orden"] is None, p["orden"] or 0, p["nombre"]))

simulacion = None
if PRESET_ORQUESTADOR in por_id:
    std = por_id.get(PRESET_STANDARD)
    if std is None:
        # El preset base del que hereda el educativo directo se llama «standard»
        # dentro del propio fichero; si no está instalado suelto, se usa el
        # preset educativo directo (que ES el base con la extensión encima).
        std = next((p for p in presets if p["id"] == "hyperframes-educativo"), None)
    if std:
        simulacion = build_simulacion(por_id[PRESET_ORQUESTADOR], std)

doc = {
    "titulo": "Presets de DSH: cómo trabaja el agente",
    "fuente": a.dir,
    "actualizado": datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%d %H:%M UTC"),
    "nota": "Un preset no es un modelo: es la configuración con la que arranca la sesión "
            "(persona, instrucciones, herramientas, políticas y delegación). Se elige antes de crear la sesión.",
    "que_es": {
        "titulo": "Qué es un preset y en qué escenarios funciona",
        "parrafos": [
            "Un preset es un grafo de módulos que se monta al crear la sesión. Decide cuatro cosas: la persona "
            "(el texto que abre el system prompt), qué herramientas existen, qué políticas se imponen (por "
            "ejemplo fijar la sesión en read-only) y si el trabajo pesado se delega o lo hace el modelo principal.",
            "No es un modelo ni una cuota: el modelo lo elige la sesión. Tampoco es un prompt que se suma al "
            "del deployment: cuando un preset declara `persona`, ocupa el mismo slot y lo reemplaza.",
            "Elegilo por la forma del trabajo, no por el tema: si el trabajo es pesado, multi-archivo o la cuota "
            "del modelo principal es escasa, conviene un preset que delegue; si es una pregunta o un cambio de "
            "una línea, el perfil por defecto gana porque no paga la ida y vuelta.",
        ],
        "regla": "Un preset se elige antes de crear la sesión y no se cambia a mitad.",
    },
    "presets": presets,
}
if simulacion:
    doc["simulacion"] = simulacion

with open(os.path.join(HERE, "presets.json"), "w", encoding="utf-8") as f:
    json.dump(doc, f, ensure_ascii=False, indent=1)

print(f"{len(presets)} presets desde {a.dir}")
for p in presets:
    r = p["rasgos"]
    d = r["delegacion"]
    print(f"  · {p['nombre']} (orden {p['orden']})"
          f"{' ← hereda de ' + ', '.join(p['hereda_de']) if p['hereda_de'] else ''}")
    print(f"      plugins={len(r['plugins'])} herramientas={len(r['herramientas'])} grupos={r['grupos']} "
          f"read_only={r['read_only']} watchdog={r['watchdog']} "
          f"persona={r['largo_prompt_persona']}c/{r['bytes_prompt_persona']}B delegacion={d['via']}")
if simulacion:
    print(f"  simulacion: {len(simulacion['pasos'])} pasos · "
          f"{len(simulacion['ensamblado']['medido'])} prompts medidos · "
          f"{len(simulacion['ensamblado']['orden_posible'])} secciones de orden documentadas")
