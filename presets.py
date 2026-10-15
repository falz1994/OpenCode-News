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
ap.add_argument("--dir-estandar",
                default=os.path.expanduser("~/.npm-global/lib/node_modules/@deepseek-ai/dsh/"
                                           "node_modules/@deepseek-ai/dsh-agent-presets/presets"),
                help="presets que trae el paquete dsh-agent-presets (incluye `standard`)")
ap.add_argument("--verifica", action="store_true",
                help="contrasta la cuenta del prefix contra PyYAML y el desglose del prompt "
                     "contra las dos sesiones medidas; termina")
a = ap.parse_args()

PRESET_STANDARD = "standard"          # preset base del que hereda el educativo directo
PRESET_ORQUESTADOR = "orchestrator"   # preset que delega (se documenta en las tarjetas)
# El preset que ilustra la columna "con preset" de la simulacion. Tiene que ser
# el mismo que se midio en MEDICION["con_preset"]: si no coinciden, el texto del
# paso 1 describiria un preset y la columna diria otro. `--verifica` lo contrasta.
PRESET_SIMULADO = "hyperframes-educativo"

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

# Lista que se usaba a mano para describir el preset por defecto. Ya NO se usa:
# la tabla de modulos lee el `agent.cordis.yml` real de `standard`. Se conserva
# solo como referencia historica — declaraba `subagent`, `workflow` y `ralph`
# como modulos de herramienta, cuando en ese preset viven dentro del grupo de
# delegacion y la guia de herramientas no los cuenta.
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
#
# Los bytes se midieron SOBRE LOS BYTES del prompt, no sobre sus caracteres: el
# prompt lleva acentos y guiones largos, y mezclar indices de caracter con
# rebanadas de texto infla las cuentas. Para repetir la medida en cualquier
# sesion (imprime el desglose por seccion tal como se lee abajo):
#
#   zstd -dc -- <sesion>/session.v3.jsonl.zstd | python3 scripts/mide_prompt.py
#
# Cada fila lleva su `bytes` por escenario y una `verifica` con el texto que
# debe medir exactamente esa cantidad. `--verifica` recalcula las dos cosas.
MEDICION = {
    "con_preset": {
        "preset": "hyperframes-educativo",
        "sesion": "~/.dsh/sessions/--home-devni-imagen-reddit-opencode--/"
                  "session-6408e2f7-ef2b-4f09-9c38-d647de84990b",
        "cwd": "/home/devni/imagen/reddit-opencode",
        "total": 28704,
        "secciones": [
            {"nombre": "harness:identity", "orden": -1000, "bytes": 48,
             "texto": "You are an AI agent powered by DeepSeek Harness.",
             "verifica": "You are an AI agent powered by DeepSeek Harness."},
            {"nombre": "deployment:persona-prefix", "orden": 0, "bytes": 6565,
             "texto": "el `prefix` del preset, con {{model}} y {{cwd}} resueltos",
             "verifica": "Eres un agente de producción educativa en video"},
            {"nombre": "preset: (compuesta)", "orden": 100, "bytes": 22024,
             "texto": "sección del preset: la extensión aporta 16.789 B y su guía de herramientas 5.235 B "
                      "(referencia de archivos 345 B incluida). No es una sección suelta: la extensión "
                      "registra orden 100 y las secciones de sus módulos caen en el mismo tramo.",
             "compuesta": [
                 {"nombre": "extensión del preset (hyperframes-prompt-extension.js)", "bytes": 16789,
                  "verifica": "HYPERFRAMES EDUCATIVO — CAPA COMPARTIDA OBLIGATORIA"},
                 {"nombre": "guía de sus herramientas", "bytes": 5235,
                  "verifica": "Tokens prefixed with @ are workspace paths the user explicitly referenced",
                  "desglose": [
                      {"nombre": "referencia de archivos", "bytes": 345,
                       "verifica": "Tokens prefixed with @ are workspace paths the user explicitly referenced"},
                      {"nombre": "una sección por herramienta montada (11 herramientas)", "bytes": 4890,
                       "verifica": "Check the [exit code: N] marker on every bash result"},
                  ]},
             ]},
            {"nombre": "deployment:persona-suffix", "orden": 10200, "bytes": 61,
             "texto": "Your working directory is /home/devni/imagen/reddit-opencode.",
             "verifica": "Your working directory is /home/devni/imagen/reddit-opencode."},
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
             "texto": "You are an AI agent powered by DeepSeek Harness.",
             "verifica": "You are an AI agent powered by DeepSeek Harness."},
            {"nombre": "deployment:persona-prefix", "orden": 0, "bytes": 64,
             "texto": "You are a coding agent powered by the deepseek-v4.1-flash model.",
             "verifica": "You are a coding agent powered by the deepseek-v4.1-flash model."},
            {"nombre": "guía de herramientas (compuesta)", "orden": 1000, "bytes": 6723,
             "texto": "referencia de archivos (345 B), una sección por herramienta montada (5.025 B), "
                      "harness:source (358 B) y GUI web (995 B); cada tramo incluye el separador que lo "
                      "une al siguiente",
             "verifica": "Tokens prefixed with @ are workspace paths the user explicitly referenced",
             "compuesta": [
                 {"nombre": "referencia de archivos", "bytes": 345,
                  "verifica": "Tokens prefixed with @ are workspace paths the user explicitly referenced"},
                 {"nombre": "una sección por herramienta montada (15 herramientas)", "bytes": 5025,
                  "verifica": "Check the [exit code: N] marker on every bash result"},
                 {"nombre": "harness:source", "bytes": 358,
                  "verifica": "The DeepSeek Harness implementation checkout is at"},
                 {"nombre": "web-surface", "bytes": 995,
                  "verifica": "You are interacting with the user through the DeepSeek Harness Web GUI"},
             ]},
            {"nombre": "deployment:persona-suffix", "orden": 10200, "bytes": 61,
             "texto": "Your working directory is /home/devni/imagen/reddit-opencode.",
             "verifica": "Your working directory is /home/devni/imagen/reddit-opencode."},
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
#
# `con_preset` / `sin_preset`: los bytes de esa seccion en cada escenario, tal
# como se midieron en las dos sesiones de MEDICION. `None` = la seccion no
# existe en ese escenario. Son la fuente de la columna "bytes" de la tabla: si
# aqui falta el numero, la tabla muestra un hueco, no un cero.
ASSEMBLY = [
    {"orden": -1000, "seccion": "harness:identity",
     "con_preset": 48, "sin_preset": 48,
     "nota": "Siempre presente; no lo cambia ningún preset."},
    {"orden": 0, "seccion": "deployment:persona-prefix",
     "con_preset": 6565, "sin_preset": 64,
     "nota": "Con preset: el `prefix` del módulo `persona`, con {{model}} y {{cwd}} resueltos. Sin preset: "
             "el del preset por defecto («You are a coding agent…»). Nunca se suman: la sección se reemplaza."},
    {"orden": 100, "seccion": "preset:… (extensiones del preset)",
     "con_preset": 22024, "sin_preset": None,
     "nota": "Solo si el preset monta un plugin que registra secciones propias. En la sesión medida la "
             "extensión educativa aporta 16.789 B y su guía de herramientas 5.235 B: la sección es la suma "
             "de las dos, porque las secciones de los módulos del preset comparten el orden 100."},
    {"orden": 500, "seccion": "políticas (plan, equipo, PTC)",
     "con_preset": None, "sin_preset": None,
     "nota": "Sólo si el preset monta esos módulos. Ninguno de los dos presets medidos los monta."},
    {"orden": 900, "seccion": "file-reference",
     "con_preset": 345, "sin_preset": 345,
     "nota": "Cómo se referencian archivos en el mensaje. Igual en los dos casos: lo aporta el perfil base."},
    {"orden": 1000, "seccion": "guía de herramientas (tool:bash, tool:read, tool:write, tool:glob, "
                               "tool:grep, tool:jobs, tool:web_search, tool:web_fetch, tool:goal, "
                               "tool:subagent, …)",
     "con_preset": 4890, "sin_preset": 5025,
     "nota": "Una sección por herramienta montada. Con el preset directo pesa MENOS que con el default: "
             "los dos montan 11 módulos de herramienta, pero el default además guía subagent, "
             "subagent_fork, workflow y ralph, que viven en su grupo de delegación."},
    {"orden": 10000, "seccion": "harness:source",
     "con_preset": 358, "sin_preset": 358,
     "nota": "Cómo leer el propio harness. Con preset sus bytes quedan DENTRO del tramo 100 (junto a la "
             "extensión), no como sección suelta: el valor se repite aquí para comparar, no se suma dos veces."},
    {"orden": 10100, "seccion": "web-surface",
     "con_preset": 995, "sin_preset": 995,
     "nota": "Cómo interactuar con la GUI web. Igual que harness:source: con preset queda dentro del "
             "tramo 100 y aquí se repite para comparar, no se suma dos veces."},
    {"orden": 10200, "seccion": "deployment:persona-suffix",
     "con_preset": 61, "sin_preset": 61,
     "nota": "`suffix` del módulo `persona` («Your working directory is {{cwd}}»), resuelto al cwd medido."},
]


# Miles con punto, sin tocar la puntuacion de la frase. Un `.replace(",", ".")`
# global sobre el texto entero tambien cambiaba las comas de la redaccion.
def n(x):
    return f"{x:,}".replace(",", ".")

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


def verifica_prompt():
    """Relee las dos sesiones de MEDICION y contrasta el desglose declarado.

    Detecta lo que se rompe solo: numeros que se copiaron a mano y dejaron de
    coincidir con la sesion, o un desglose que ya no suma el total. Se salta sin
    fallar si la sesion no esta en el disco (otra maquina, sesion purgada).
    """
    import subprocess, sys as _sys
    ruta_script = os.path.join(HERE, "scripts", "mide_prompt.py")
    if not os.path.exists(ruta_script):
        print("  · scripts/mide_prompt.py no existe: no se puede contrastar el desglose")
        return 0
    _sys.path.insert(0, os.path.join(HERE, "scripts"))
    import mide_prompt

    fallos = 0
    for clave in ("con_preset", "sin_preset"):
        m = MEDICION[clave]
        zstd = os.path.expanduser(m["sesion"]) + "/session.v3.jsonl.zstd"
        if not os.path.exists(zstd):
            print(f"  · {clave}: sesion no encontrada ({m['sesion']}) — sin contrastar")
            continue
        try:
            salida = subprocess.run(["zstd", "-dc", "--", zstd], capture_output=True, check=True)
        except Exception as e:
            print(f"  · {clave}: no se pudo descomprimir la sesion ({e})")
            continue
        prompt = mide_prompt.lee_prompt(salida.stdout.decode("utf-8", "replace").splitlines())
        if prompt is None:
            print(f"  MAL {clave}: la sesion no tiene un system/message legible")
            fallos += 1
            continue
        real = mide_prompt.mide(prompt)
        etiqueta = f"{clave} ({m['preset'].split(' (')[0]})"
        ok_total = real["total"] == m["total"]
        fallos += 0 if ok_total else 1
        print(f"  {'OK ' if ok_total else 'MAL'} {etiqueta}: total declarado {m['total']} B / "
              f"medido {real['total']} B")
        # el desglose declarado debe sumar el total menos los separadores
        suma = sum(s["bytes"] for s in m["secciones"])
        sep = m["total"] - suma
        ok_suma = 0 <= sep <= 2 * len(m["secciones"])
        fallos += 0 if ok_suma else 1
        print(f"  {'OK ' if ok_suma else 'MAL'} {etiqueta}: secciones suman {suma} B "
              f"+ {sep} B de separadores = {m['total']} B")
        # las partes de una seccion compuesta deben sumar la seccion
        for s in m["secciones"]:
            partes = s.get("compuesta")
            if not partes:
                continue
            sp = sum(p["bytes"] for p in partes)
            ok_c = sp == s["bytes"]
            fallos += 0 if ok_c else 1
            print(f"  {'OK ' if ok_c else 'MAL'} {etiqueta}: «{s['nombre']}» {s['bytes']} B = "
                  + " + ".join(f"{p['bytes']}" for p in partes) + f" = {sp} B")
            for p in partes:
                for q in p.get("desglose", []):
                    pass
                d = p.get("desglose")
                if d:
                    sd = sum(x["bytes"] for x in d)
                    ok_d = sd == p["bytes"]
                    fallos += 0 if ok_d else 1
                    print(f"  {'OK ' if ok_d else 'MAL'} {etiqueta}: «{p['nombre']}» {p['bytes']} B = "
                          + " + ".join(str(x["bytes"]) for x in d) + f" = {sd} B")
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
    texto_persona = bloque_escalar(todo, "prefix") if persona else ""
    return {
        "persona_propia": persona,
        "largo_prompt_persona": largo,
        "bytes_prompt_persona": len(texto_persona.encode("utf-8")),
        # el texto sin resolver (`{{model}}`, `{{cwd}}`): quien lo use lo interpola
        "prefix_persona": texto_persona,
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
    """Rellena el ensamblado con los bytes medidos en los ficheros reales.

    Los bytes salen de ASSEMBLY (medidos en las dos sesiones de MEDICION), no de
    una estimacion. Se anaden los campos que consume la tabla del frame:
    `bytes_con_preset` y `bytes_sin_preset` (None = la seccion no existe ahi).
    """
    out = []
    for s in ASSEMBLY:
        s = dict(s)
        s["bytes_con_preset"] = s.pop("con_preset", None)
        s["bytes_sin_preset"] = s.pop("sin_preset", None)
        if s["seccion"] == "deployment:persona-prefix":
            # El fichero vivo del preset puede haber cambiado despues de la
            # sesion medida: se declaran las dos cifras y a que pertenece cada una.
            vivo = pre["rasgos"]["bytes_prompt_persona"]
            s["texto"] = (f"{pre['rasgos']['largo_prompt_persona']} caracteres del `prefix` del preset "
                          f"({vivo} B en el fichero de ahora; {s['bytes_con_preset']} B en la sesión medida)")
            s["bytes"] = vivo
            s["texto_sin_preset"] = "la del preset por defecto, no se suma: la sección se reemplaza"
        elif s["seccion"] == "deployment:persona-suffix":
            suf = pre["rasgos"]["suffix_persona"]
            s["texto"] = f"`{suf}`" if suf else "vacío (0 bytes)"
            s["bytes"] = len(suf.encode("utf-8"))
            s["texto_sin_preset"] = "la misma sección, con el cwd del deployment"
        elif s["seccion"] == "harness:identity":
            s["bytes"] = s["bytes_con_preset"]
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
            # El preset `standard` SI declara su propia persona: se lee de su
            # fichero y se resuelven las variables. Antes esto se escribia a mano
            # con PERSONA_DEFAULT/SUFFIX_DEFAULT, y bastaba tocar el preset para
            # que la tabla quedara mintiendo.
            resuelta = (r.get("prefix_persona") or PERSONA_DEFAULT)
            resuelta = resuelta.replace("{{model}}", MODELO_MEDIDO).replace("{{cwd}}", CWD_MEDIDO)
            f["persona"] = {
                "aporta": f"System prompt del preset `{std.get('id', PRESET_STANDARD)}`",
                "dato": f"«{resuelta}» — {len(resuelta.encode())} B",
            }
            suf = (r.get("suffix_persona") or SUFFIX_DEFAULT).replace("{{cwd}}", CWD_MEDIDO)
            f["persona (suffix)"] = {
                "aporta": "`deployment:persona-suffix`",
                "dato": f"«{suf}» — {len(suf.encode())} B",
            }
        else:
            f["persona"] = {
                "aporta": "System prompt propio del preset",
                "dato": (f"prefix de {n(r['largo_prompt_persona'])} caracteres"
                         + (f" + suffix «{r['suffix_persona']}»" if r["suffix_persona"] else "")),
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

    # El escenario "sin preset" es el preset `standard` que monta el roster: sus
    # modulos, plugins, grupos y delegacion son LOS SUYOS, leidos de su fichero.
    # Lo unico que cambia es la persona: el deployment aporta la suya (64 B) y el
    # suffix resuelto. Antes esto se sobreescribia con una lista de herramientas
    # escrita a mano y la tabla llegaba a declarar 13 modulos donde el preset
    # monta 11 (metia `subagent`/`workflow`/`ralph` como si fueran herramientas).
    default = {"id": std.get("id", PRESET_STANDARD),
               "nombre": "perfil por defecto (preset `standard`)",
               "rasgos": dict(std["rasgos"], largo_prompt_persona=0,
                              bytes_prompt_persona=0, suffix_persona="")}
    return {"con_preset": filas(pre), "sin_preset": filas(default, es_default=True)}


def paso_cuota(r, quien_verifica):
    """Texto del paso «Cuota y verificación», derivado de los rasgos medidos.

    Antes estaba escrito a mano y la columna del default afirmaba que se
    distingue por ir «sin router, sin failover y sin cuarentenas». Con el preset
    que se mide (`hyperframes-educativo`) eso no distingue nada: ese preset
    tampoco monta router, y el paso 5 lo dice con sus propias palabras. Un texto
    fijo sobre un preset que cambia acaba describiendo otro preset, que es
    justamente el defecto que ya se corrigio en el paso 1. Aqui se deriva de los
    rasgos para que siga siendo cierto si cambia el preset medido.
    """
    vig = [n for n, on in (("watchdog de jobs", r["watchdog"]),
                           ("observador de límites", r["observador_limites"])) if on]
    cuota = ("Monta " + " y ".join(vig) + ": hay un plugin que vigila la cuota."
             if vig else
             "No monta watchdog ni observador de límites: ningún plugin vigila la cuota.")
    via = (r["delegacion"] or {}).get("via", "ninguna")
    if via == "ninguna":
        reparto = ("La vía de delegación está vaciada: no hay ninguna herramienta para repartir "
                   "el trabajo, así que la cuota que se gasta es la del modelo de la sesión.")
    elif r["plugins"]:
        reparto = (f"El preset monta la vía de delegación (`{via}`) y sus plugins de política: "
                   "el trabajo pesado lo hace un hijo, así que la cuota que se quema produciendo "
                   "no es la del modelo de la sesión.")
    else:
        reparto = (f"El grupo de delegación está montado (`{via}`), pero sin plugins de política: "
                   "solo se usa si el modelo decide llamarlo. Si no lo llama, la cuota que se "
                   "gasta es la del modelo de la sesión.")
    return " ".join([cuota, reparto, quien_verifica])


def build_simulacion(pre, std):
    """Traza de una sesion nueva: preset elegido frente a un request sin preset.

    Los numeros de bytes salen de `MEDICION` (dos sesiones reales leidas del
    disco); los del preset que se muestra salen de sus ficheros. Nada se estima.
    """
    r_pre = pre["rasgos"]
    r_std = std["rasgos"]
    mp = MEDICION["con_preset"]
    ms = MEDICION["sin_preset"]
    # las partes de la seccion compuesta del preset (extension + guia)
    sec_mp = mp["secciones"][2]["compuesta"]
    return {
        "titulo": "Simulación: mandar un mensaje en una sesión nueva",
        "intro": (
            "Qué se carga y qué se manda al prompt cuando abrís una sesión nueva y mandás un mensaje. "
            "La columna izquierda es una sesión con un preset elegido; la derecha, un request normal sin "
            "elegir nada. Los bytes del system prompt están medidos de dos sesiones reales del disco "
            "(las rutas están en cada columna): no son estimaciones."),
        "columnas": [
            {"id": "con_preset", "titulo": "Con un preset elegido",
             "sub": f"ejemplo medido: `{mp['preset']}` · system prompt de {n(mp['total'])} B",
             "sesion": mp["sesion"], "total": mp["total"]},
            {"id": "sin_preset", "titulo": "Request normal, sin elegir preset",
             "sub": f"se compone con el default del roster: {ms['preset'].split(' (')[0]} · "
                    f"system prompt de {n(ms['total'])} B",
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
             "con_preset": (f"Se montan los módulos de `agent.cordis.yml` y de su base heredada: persona, "
                            f"{len(r_pre['plugins'])} plugins de política, {len(r_pre['herramientas'])} módulos "
                            f"de herramienta y {r_pre['grupos']} grupos. Su grupo de delegación se vacía a "
                            "propósito: no monta `subagent`, `subagent_fork`, `workflow` ni `ralph`, que sí "
                            "están en el preset por defecto."),
             "sin_preset": (f"Se montan los módulos del preset `standard` (el que trae el paquete): persona, "
                            f"{len(r_std['herramientas'])} módulos de herramienta, {r_std['grupos']} grupos y el "
                            "grupo de delegación completo con `subagent`, `subagent_fork`, `workflow` y "
                            "`ralph`. Sin plugins de política."),
             "fuente": "agent.cordis.yml"},
            {"n": 2, "titulo": "Se ensambla el system prompt",
             "con_preset": (f"`deployment:persona-prefix` = {n(mp['secciones'][1]['bytes'])} B: el `prefix` del "
                            f"preset. Después, la sección del preset suma {n(mp['secciones'][2]['bytes'])} B y "
                            "no es una sección suelta: la extensión registra orden 100 y las secciones de sus "
                            f"módulos caen en el mismo tramo ({n(sec_mp[0]['bytes'])} B de extensión + "
                            f"{n(sec_mp[1]['bytes'])} B de guía de herramientas). Total medido: "
                            f"{n(mp['total'])} B."),
             "sin_preset": (f"`deployment:persona-prefix` = {ms['secciones'][1]['bytes']} B: la persona del "
                            f"preset `standard` («You are a coding agent…»). La guía de herramientas pesa "
                            f"{n(ms['secciones'][2]['bytes'])} B y ahí sí es la pieza más grande del prompt. "
                            f"Total medido: {n(ms['total'])} B."),
             "fuente": "dsh-system-prompt · renderPrompt"},
            {"n": 3, "titulo": "Mandás el mensaje",
             "con_preset": ("Lo que ve el modelo es: system prompt + instrucciones del proyecto + contexto "
                            "de entorno + historial + TU MENSAJE."),
             "sin_preset": (f"La misma forma, con el system prompt de {n(ms['total'])} B. Tus ficheros NO viajan "
                            "dentro: entran solo si el modelo llama a una herramienta."),
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
             "con_preset": paso_cuota(r_pre, "La verificación se hace leyendo evidencia del disco."),
             "sin_preset": paso_cuota(r_std, "La verificación la hacés vos."),
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
            # `secciones_prompt` es la que aporta `bytes_con_preset` /
            # `bytes_sin_preset`: sin pasar por ella la tabla sale con la
            # columna de bytes vacia.
            "orden_posible": secciones_prompt(pre, std),
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
    print("== bytes del `prefix` de la persona: regex propia vs PyYAML ==")
    f1 = verifica()
    print()
    print("== desglose del system prompt declarado vs las sesiones reales ==")
    f2 = verifica_prompt()
    raise SystemExit(1 if (f1 or f2) else 0)

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
if PRESET_SIMULADO in por_id:
    # El preset `standard` viaja DENTRO del paquete dsh-agent-presets, no en
    # ~/.dsh/.agent-presets. Se lee de ahi para que la columna "sin preset"
    # describa el preset de verdad (11 modulos, 2 grupos) y no una copia a mano.
    std = por_id.get(PRESET_STANDARD)
    if std is None:
        ruta_std = os.path.join(a.dir_estandar, PRESET_STANDARD, "agent.cordis.yml")
        if os.path.exists(ruta_std):
            r = rasgos([ruta_std])
            std = {"id": PRESET_STANDARD, "nombre": "standard (del paquete)", "rasgos": r,
                   "es_del_paquete": True}
        else:
            print(f"  ! no se encontro el preset `{PRESET_STANDARD}` en {a.dir_estandar}: "
                  "la simulacion queda sin la columna de comparacion")
    if std:
        simulacion = build_simulacion(por_id[PRESET_SIMULADO], std)
else:
    print(f"  ! el preset `{PRESET_SIMULADO}` (el que se mide en la simulacion) no esta instalado: "
          "no se genera la simulacion")

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
