// generado por index_datos.py — no editar a mano
window.DATOS = {
 "titulo": "Modelos de OpenCode por habilidad",
 "subtitulo": "Matriz modelo x habilidad construida desde r/opencode + r/opencodeCLI",
 "nota": "Valoraciones curadas a mano a partir de frases donde la comunidad asigna un modelo a una tarea. Los recuentos de menciones y el sentimiento los calcula index_datos.py sobre los volcados.",
 "ventana_dias": 45,
 "noticias_dias": 12,
 "noticias_top": 14,
 "habilidades": [
  {
   "id": "frontend",
   "nombre": "Frontend / UI",
   "ayuda": "Interfaces, React/Vue, CSS, diseño web"
  },
  {
   "id": "backend",
   "nombre": "Backend / APIs",
   "ayuda": "Servicios, bases de datos, endpoints"
  },
  {
   "id": "planificacion",
   "nombre": "Planificación",
   "ayuda": "Arquitectura, specs y design docs"
  },
  {
   "id": "motion",
   "nombre": "Motion / Visual",
   "ayuda": "Animación, vídeo, gráficos, 3D"
  },
  {
   "id": "codigo",
   "nombre": "Programación",
   "ayuda": "Implementación y refactor"
  },
  {
   "id": "debug",
   "nombre": "Debugging",
   "ayuda": "Cazar y arreglar bugs"
  },
  {
   "id": "tests",
   "nombre": "Tests / Review",
   "ayuda": "Tests, QA y revisión adversarial"
  },
  {
   "id": "orquestacion",
   "nombre": "Orquestación",
   "ayuda": "Routers, subagentes, contexto largo"
  },
  {
   "id": "docs",
   "nombre": "Escritura / Docs",
   "ayuda": "Documentación, prosa, commits"
  },
  {
   "id": "research",
   "nombre": "Research / Datos",
   "ayuda": "Búsqueda, scraping, traducción"
  },
  {
   "id": "vision",
   "nombre": "Visión / Imagen",
   "ayuda": "Capturas, OCR, multimodal"
  },
  {
   "id": "local",
   "nombre": "Local / self-host",
   "ayuda": "Ollama, llama.cpp, privacidad"
  },
  {
   "id": "simples",
   "nombre": "Tareas simples",
   "ayuda": "Grunt work, boilerplate, commits"
  },
  {
   "id": "valor",
   "nombre": "Calidad/precio",
   "ayuda": "Valor dentro de OpenCode Go/Zen"
  }
 ],
 "modelos": [
  {
   "nombre": "DeepSeek 4.1 Flash",
   "alias": "deepseek|ds ?4\\.1|v4\\.1 ?flash|dsv4",
   "rol": "Workhorse por defecto",
   "pega": "Bucles repetidos, caídas y contexto largo flojo",
   "r": {
    "frontend": 2,
    "backend": 3,
    "planificacion": 2,
    "motion": 2,
    "codigo": 3,
    "debug": 3,
    "tests": 2,
    "orquestacion": 2,
    "docs": 1,
    "research": 1,
    "vision": 2,
    "local": -1,
    "simples": 3,
    "valor": 3
   },
   "menciones": {
    "valor": 439,
    "docs": 28,
    "codigo": 162,
    "orquestacion": 79,
    "backend": 198,
    "tests": 92,
    "motion": 22,
    "planificacion": 42,
    "frontend": 9,
    "debug": 17,
    "local": 19,
    "simples": 13,
    "research": 8,
    "vision": 14
   },
   "sentimiento": {
    "pos": 335,
    "neg": 224,
    "total": 559,
    "pct": 60
   }
  },
  {
   "nombre": "GLM 5.3 Flash",
   "alias": "\\bglm\\b",
   "rol": "Orquestador y revisor",
   "pega": "Precio en Go y hay que babysitearlo",
   "r": {
    "frontend": 3,
    "backend": 3,
    "planificacion": 3,
    "motion": 1,
    "codigo": 3,
    "debug": 3,
    "tests": 3,
    "orquestacion": 3,
    "docs": 3,
    "research": 3,
    "vision": 1,
    "local": -1,
    "simples": 2,
    "valor": 2
   },
   "menciones": {
    "valor": 231,
    "codigo": 109,
    "backend": 42,
    "tests": 60,
    "local": 12,
    "orquestacion": 34,
    "simples": 6,
    "planificacion": 33,
    "frontend": 7,
    "motion": 11,
    "debug": 11,
    "docs": 12,
    "research": 4,
    "vision": 3
   },
   "sentimiento": {
    "pos": 192,
    "neg": 122,
    "total": 314,
    "pct": 61
   }
  },
  {
   "nombre": "Opus 5.5",
   "alias": "\\bopus\\b",
   "rol": "Arquitecto / design docs",
   "pega": "Consumo de tokens brutal",
   "r": {
    "frontend": 2,
    "backend": 2,
    "planificacion": 3,
    "motion": 3,
    "codigo": 3,
    "debug": 2,
    "tests": 3,
    "orquestacion": 3,
    "docs": 3,
    "research": 2,
    "vision": 2,
    "local": -1,
    "simples": 1,
    "valor": 1
   },
   "menciones": {
    "codigo": 53,
    "tests": 34,
    "local": 4,
    "valor": 72,
    "motion": 20,
    "planificacion": 29,
    "orquestacion": 21,
    "research": 3,
    "backend": 7,
    "debug": 8,
    "docs": 11,
    "frontend": 4,
    "simples": 3
   },
   "sentimiento": {
    "pos": 66,
    "neg": 36,
    "total": 102,
    "pct": 65
   }
  },
  {
   "nombre": "Sonnet 5.5",
   "alias": "\\bsonnet\\b",
   "rol": "Implementar tras el plan de Opus",
   "pega": "Caro en tokens",
   "r": {
    "frontend": 2,
    "backend": 2,
    "planificacion": 2,
    "motion": 2,
    "codigo": 3,
    "debug": 3,
    "tests": 3,
    "orquestacion": 2,
    "docs": 2,
    "research": 2,
    "vision": 1,
    "local": -1,
    "simples": 1,
    "valor": 1
   },
   "menciones": {
    "valor": 37,
    "docs": 5,
    "planificacion": 9,
    "tests": 7,
    "codigo": 18,
    "orquestacion": 9,
    "local": 1,
    "motion": 6,
    "debug": 3,
    "backend": 1,
    "simples": 2,
    "research": 1
   },
   "sentimiento": {
    "pos": 32,
    "neg": 19,
    "total": 51,
    "pct": 63
   }
  },
  {
   "nombre": "Haiku 5.5",
   "alias": "\\bhaiku\\b",
   "rol": "Worker barato",
   "pega": "Precio x5 al pasar de 100k de contexto",
   "r": {
    "frontend": 1,
    "backend": 1,
    "planificacion": 1,
    "motion": 0,
    "codigo": 2,
    "debug": 1,
    "tests": 2,
    "orquestacion": 1,
    "docs": 1,
    "research": 1,
    "vision": 0,
    "local": -1,
    "simples": 2,
    "valor": 2
   },
   "menciones": {
    "codigo": 6,
    "tests": 11,
    "valor": 38,
    "planificacion": 1,
    "orquestacion": 7,
    "motion": 1,
    "simples": 1,
    "backend": 2,
    "research": 1,
    "local": 1,
    "docs": 1
   },
   "sentimiento": {
    "pos": 22,
    "neg": 7,
    "total": 29,
    "pct": 76
   }
  },
  {
   "nombre": "GPT-6 Luna",
   "alias": "\\bluna\\b",
   "rol": "Volumen a bajo coste",
   "pega": "Lento en razonamiento alto",
   "r": {
    "frontend": 1,
    "backend": 2,
    "planificacion": 2,
    "motion": 0,
    "codigo": 2,
    "debug": 1,
    "tests": 2,
    "orquestacion": 2,
    "docs": 2,
    "research": 2,
    "vision": 1,
    "local": -1,
    "simples": 3,
    "valor": 3
   },
   "menciones": {
    "codigo": 45,
    "tests": 27,
    "local": 1,
    "backend": 8,
    "research": 2,
    "planificacion": 20,
    "valor": 118,
    "orquestacion": 30,
    "docs": 13,
    "motion": 9,
    "vision": 1,
    "simples": 5,
    "frontend": 1,
    "debug": 1
   },
   "sentimiento": {
    "pos": 107,
    "neg": 45,
    "total": 152,
    "pct": 70
   }
  },
  {
   "nombre": "Sol 6.1 / GPT-6",
   "alias": "\\bsol ?6|\\bsol\\b|gpt-?6",
   "rol": "Cabeza pensante eficiente",
   "pega": "Lento",
   "r": {
    "frontend": 1,
    "backend": 2,
    "planificacion": 3,
    "motion": 1,
    "codigo": 2,
    "debug": 1,
    "tests": 3,
    "orquestacion": 3,
    "docs": 2,
    "research": 2,
    "vision": 0,
    "local": -1,
    "simples": 1,
    "valor": 2
   },
   "menciones": {
    "backend": 10,
    "research": 4,
    "planificacion": 30,
    "codigo": 39,
    "tests": 33,
    "orquestacion": 26,
    "docs": 12,
    "valor": 58,
    "motion": 9,
    "local": 2,
    "frontend": 2,
    "simples": 4,
    "debug": 1
   },
   "sentimiento": {
    "pos": 58,
    "neg": 32,
    "total": 90,
    "pct": 64
   }
  },
  {
   "nombre": "Gemini 4 Argon",
   "alias": "gemini|argon",
   "rol": "Frontend y diseño visual",
   "pega": "Coste por tarea",
   "r": {
    "frontend": 3,
    "backend": 2,
    "planificacion": 2,
    "motion": 3,
    "codigo": 2,
    "debug": 2,
    "tests": 2,
    "orquestacion": 1,
    "docs": 2,
    "research": 2,
    "vision": 3,
    "local": -1,
    "simples": 1,
    "valor": 1
   },
   "menciones": {
    "local": 3,
    "tests": 16,
    "planificacion": 4,
    "codigo": 10,
    "frontend": 4,
    "backend": 19,
    "research": 8,
    "docs": 7,
    "valor": 21,
    "motion": 9,
    "orquestacion": 2,
    "debug": 2
   },
   "sentimiento": {
    "pos": 31,
    "neg": 14,
    "total": 45,
    "pct": 69
   }
  },
  {
   "nombre": "Muse Spark 1.3",
   "alias": "muse ?spark|muse ?1\\.3|\\bspark\\b",
   "rol": "Subagente rápido",
   "pega": "Benchmaxxed y entrena con tus datos",
   "r": {
    "frontend": 2,
    "backend": 2,
    "planificacion": 1,
    "motion": 1,
    "codigo": 2,
    "debug": 2,
    "tests": 1,
    "orquestacion": 2,
    "docs": -1,
    "research": 2,
    "vision": 1,
    "local": -1,
    "simples": 2,
    "valor": 3
   },
   "menciones": {
    "valor": 78,
    "orquestacion": 30,
    "simples": 4,
    "backend": 15,
    "codigo": 45,
    "docs": 12,
    "research": 4,
    "tests": 27,
    "planificacion": 11,
    "frontend": 12,
    "debug": 8,
    "motion": 7,
    "local": 3,
    "vision": 2
   },
   "sentimiento": {
    "pos": 146,
    "neg": 65,
    "total": 211,
    "pct": 69
   }
  },
  {
   "nombre": "MiMo 2.6 Flash/Pro",
   "alias": "\\bmimo\\b",
   "rol": "Implementador y mejor modelo medio",
   "pega": "Repite tool-calls y quema contexto",
   "r": {
    "frontend": 2,
    "backend": 2,
    "planificacion": 2,
    "motion": 3,
    "codigo": 3,
    "debug": 2,
    "tests": 2,
    "orquestacion": 2,
    "docs": 1,
    "research": 1,
    "vision": 2,
    "local": -1,
    "simples": 2,
    "valor": 3
   },
   "menciones": {
    "valor": 71,
    "tests": 37,
    "motion": 10,
    "planificacion": 13,
    "codigo": 41,
    "orquestacion": 14,
    "frontend": 5,
    "docs": 3,
    "backend": 7,
    "research": 5,
    "local": 3,
    "simples": 9,
    "vision": 2,
    "debug": 3
   },
   "sentimiento": {
    "pos": 118,
    "neg": 81,
    "total": 199,
    "pct": 59
   }
  },
  {
   "nombre": "Kimi K2.7 / K2.6 / K3",
   "alias": "\\bkimi\\b|\\bk3\\b",
   "rol": "Frontend y planner",
   "pega": "K3 es el más caro de Go",
   "r": {
    "frontend": 3,
    "backend": 2,
    "planificacion": 3,
    "motion": 1,
    "codigo": 3,
    "debug": 2,
    "tests": 2,
    "orquestacion": 2,
    "docs": 2,
    "research": 2,
    "vision": 2,
    "local": -1,
    "simples": 1,
    "valor": 1
   },
   "menciones": {
    "codigo": 34,
    "orquestacion": 8,
    "backend": 13,
    "valor": 26,
    "motion": 4,
    "planificacion": 11,
    "tests": 14,
    "debug": 3,
    "frontend": 5,
    "research": 2,
    "local": 3,
    "vision": 1
   },
   "sentimiento": {
    "pos": 29,
    "neg": 25,
    "total": 54,
    "pct": 54
   }
  },
  {
   "nombre": "Qwen 3.8",
   "alias": "\\bqwen\\b",
   "rol": "Local y agentes largos",
   "pega": "Overthinking",
   "r": {
    "frontend": 1,
    "backend": 2,
    "planificacion": 2,
    "motion": 0,
    "codigo": 2,
    "debug": 1,
    "tests": 1,
    "orquestacion": 3,
    "docs": 1,
    "research": 2,
    "vision": 1,
    "local": 3,
    "simples": 2,
    "valor": 2
   },
   "menciones": {
    "local": 37,
    "backend": 19,
    "tests": 17,
    "debug": 3,
    "frontend": 2,
    "valor": 30,
    "codigo": 23,
    "research": 3,
    "vision": 2,
    "planificacion": 4,
    "motion": 2,
    "docs": 2,
    "orquestacion": 13,
    "simples": 3
   },
   "sentimiento": {
    "pos": 43,
    "neg": 22,
    "total": 65,
    "pct": 66
   }
  },
  {
   "nombre": "Space Bunny (MiniMax)",
   "alias": "space ?bunny|minimax",
   "rol": "One-shot creativo",
   "pega": "Lento, token-ineficiente y retirado",
   "r": {
    "frontend": 2,
    "backend": 1,
    "planificacion": 1,
    "motion": 3,
    "codigo": 3,
    "debug": 1,
    "tests": 2,
    "orquestacion": 1,
    "docs": 1,
    "research": 1,
    "vision": 2,
    "local": -1,
    "simples": 1,
    "valor": 2
   },
   "menciones": {
    "research": 1,
    "valor": 24,
    "backend": 8,
    "tests": 24,
    "motion": 8,
    "planificacion": 2,
    "local": 3,
    "codigo": 34,
    "frontend": 6,
    "docs": 8,
    "debug": 5,
    "orquestacion": 8,
    "vision": 5,
    "simples": 2
   },
   "sentimiento": {
    "pos": 60,
    "neg": 41,
    "total": 101,
    "pct": 59
   }
  },
  {
   "nombre": "Step 5 Preview",
   "alias": "step ?5|stepfun",
   "rol": "Alternativa gratis",
   "pega": "Lento, se distrae y cae el endpoint",
   "r": {
    "frontend": 0,
    "backend": 1,
    "planificacion": 1,
    "motion": 0,
    "codigo": 2,
    "debug": 1,
    "tests": 2,
    "orquestacion": 0,
    "docs": 1,
    "research": 0,
    "vision": 0,
    "local": -1,
    "simples": 2,
    "valor": 3
   },
   "menciones": {
    "backend": 8,
    "codigo": 1,
    "valor": 2
   },
   "sentimiento": {
    "pos": 10,
    "neg": 10,
    "total": 20,
    "pct": 50
   }
  },
  {
   "nombre": "LongCat 2.5",
   "alias": "longcat",
   "rol": "Microtareas y visión barata",
   "pega": "Rompió el CLI a varios",
   "r": {
    "frontend": 2,
    "backend": 1,
    "planificacion": 0,
    "motion": 0,
    "codigo": 1,
    "debug": 1,
    "tests": 0,
    "orquestacion": 0,
    "docs": 0,
    "research": 0,
    "vision": 2,
    "local": -1,
    "simples": 2,
    "valor": 3
   },
   "menciones": {
    "codigo": 4,
    "tests": 5,
    "planificacion": 1,
    "research": 1,
    "valor": 5,
    "frontend": 1,
    "vision": 1,
    "simples": 1
   },
   "sentimiento": {
    "pos": 9,
    "neg": 14,
    "total": 23,
    "pct": 39
   }
  },
  {
   "nombre": "Ling 3.1",
   "alias": "\\bling\\b",
   "rol": "Relleno gratis",
   "pega": "Sin defensores",
   "r": {
    "frontend": 0,
    "backend": 0,
    "planificacion": 0,
    "motion": 0,
    "codigo": 1,
    "debug": 0,
    "tests": 0,
    "orquestacion": 0,
    "docs": 0,
    "research": 0,
    "vision": 0,
    "local": -1,
    "simples": 2,
    "valor": 3
   },
   "menciones": {
    "orquestacion": 1,
    "codigo": 4,
    "tests": 2,
    "docs": 1,
    "local": 1,
    "simples": 1,
    "valor": 2
   },
   "sentimiento": {
    "pos": 1,
    "neg": 4,
    "total": 5,
    "pct": 20
   }
  },
  {
   "nombre": "Nemotron 3 Ultra",
   "alias": "nemotron",
   "rol": "Orquestador por su 1M de contexto",
   "pega": "Falla tareas básicas",
   "r": {
    "frontend": 0,
    "backend": 1,
    "planificacion": 1,
    "motion": 0,
    "codigo": 1,
    "debug": 1,
    "tests": 1,
    "orquestacion": 2,
    "docs": 0,
    "research": 0,
    "vision": 0,
    "local": -1,
    "simples": 1,
    "valor": 2
   },
   "menciones": {
    "codigo": 4,
    "backend": 3,
    "valor": 4,
    "orquestacion": 2,
    "tests": 1,
    "simples": 1
   },
   "sentimiento": {
    "pos": 11,
    "neg": 9,
    "total": 20,
    "pct": 55
   }
  },
  {
   "nombre": "Cat Jam",
   "alias": "cat ?jam",
   "rol": "Trivial a 300-350 tps",
   "pega": "Inteligencia muy baja",
   "r": {
    "frontend": 0,
    "backend": 0,
    "planificacion": 0,
    "motion": 0,
    "codigo": 1,
    "debug": 0,
    "tests": 0,
    "orquestacion": 0,
    "docs": 0,
    "research": 0,
    "vision": 0,
    "local": -1,
    "simples": 2,
    "valor": 3
   },
   "menciones": {
    "tests": 1
   },
   "sentimiento": {
    "pos": 0,
    "neg": 0,
    "total": 0,
    "pct": null
   }
  },
  {
   "nombre": "big-pickle (MAI)",
   "alias": "big-?pickle",
   "rol": "Evitar",
   "pega": "Documentos y rutas alucinadas",
   "r": {
    "frontend": 0,
    "backend": 1,
    "planificacion": 0,
    "motion": 0,
    "codigo": 1,
    "debug": 1,
    "tests": 0,
    "orquestacion": 0,
    "docs": -1,
    "research": 0,
    "vision": 0,
    "local": -1,
    "simples": 1,
    "valor": 2
   },
   "menciones": {
    "planificacion": 1,
    "backend": 9,
    "research": 1,
    "valor": 1
   },
   "sentimiento": {
    "pos": 6,
    "neg": 3,
    "total": 9,
    "pct": 67
   }
  },
  {
   "nombre": "Grok 4.6",
   "alias": "\\bgrok\\b",
   "rol": "—",
   "pega": "Quema la cuota en 3 prompts",
   "r": {
    "frontend": 0,
    "backend": 1,
    "planificacion": 1,
    "motion": 0,
    "codigo": 1,
    "debug": 0,
    "tests": 0,
    "orquestacion": 0,
    "docs": 0,
    "research": 0,
    "vision": 0,
    "local": -1,
    "simples": 0,
    "valor": -1
   },
   "menciones": {
    "backend": 1,
    "local": 3,
    "codigo": 11,
    "orquestacion": 2,
    "tests": 7,
    "valor": 17,
    "debug": 1,
    "research": 1,
    "frontend": 1,
    "docs": 1
   },
   "sentimiento": {
    "pos": 13,
    "neg": 10,
    "total": 23,
    "pct": 57
   }
  }
 ],
 "presupuestos": {
  "columnas": [
   "Presupuesto",
   "Planificador",
   "Orquestador",
   "Implementador",
   "Revisor",
   "Worker barato"
  ],
  "filas": [
   [
    "$0 (free tier)",
    "Luna / Muse Spark",
    "GLM 5.3 Flash (si entra)",
    "MiMo 2.6 Flash Free · Ling 3.1",
    "Muse Spark · Space Bunny",
    "LongCat 2.5 · Step 5 · Cat Jam"
   ],
   [
    "$10 (Go)",
    "Luna max o GLM 5.3",
    "GLM 5.3 Flash",
    "DeepSeek 4.1 Flash",
    "GLM 5.3 Flash (adversarial)",
    "DeepSeek Flash · MiMo Flash"
   ],
   [
    "$20",
    "Opus 5.5 (plan + design docs)",
    "Sonnet 5.5",
    "Sonnet 5.5",
    "Sonnet 5.5",
    "Luna low/medium"
   ],
   [
    "$30-40",
    "Opus 5.5 / Sol 6.1",
    "Opus 5.5 + GLM 5.3",
    "DeepSeek 4.1 Flash + MiMo Pro",
    "GLM 5.3 Flash + Sonnet",
    "Haiku 5.5"
   ],
   [
    "Local (0 €/token)",
    "Qwen 3.8 (si te da)",
    "Qwen 3.8 contexto largo",
    "Qwen 3.6 35B A3B",
    "—",
    "Qwen local pequeño"
   ]
  ]
 },
 "precios": {
  "columnas": [
   "Modelo / plan",
   "Entrada /1M",
   "Salida /1M",
   "Cache read /1M",
   "Notas"
  ],
  "filas": [
   [
    "DeepSeek 4.1 Flash",
    "$0.15",
    "$0.60",
    "$0.003",
    "96% cache hit; 2,5x el trabajo de GLM por 20% más de coste"
   ],
   [
    "GLM 5.3 Flash",
    "$0.15",
    "$0.50",
    "$0.03",
    "92% cache hit; se siente más listo pero cuesta más por tarea"
   ],
   [
    "GPT-6 Luna (Zen)",
    "$0.10",
    "$0.50",
    "$0.01",
    "Más barato en lista que DeepSeek: la caché decide"
   ],
   [
    "Haiku 5.5",
    "$0.10",
    "$0.50",
    "—",
    "≤100k tokens; x5 de precio al pasarlos"
   ],
   [
    "Kimi K3",
    "$2.00",
    "$10.00",
    "—",
    "El más caro de Go; quema la cuota en 3 prompts"
   ],
   [
    "Mistral Large 4",
    "—",
    "—",
    "—",
    "Toda la potencia de Luna por 15x el coste"
   ],
   [
    "Go $10",
    "—",
    "—",
    "—",
    "$60 → $80 de uso DeepSeek (subida sin anunciar, 12-oct)"
   ],
   [
    "Go Plus $40",
    "—",
    "—",
    "—",
    "2x límites por 4x precio: DOA; la gente apila subs de $10"
   ],
   [
    "OpenDesign Go ($8-10)",
    "—",
    "—",
    "—",
    "$120 de crédito con DS 4.1 Flash; sin verificar, olor a CrofAI"
   ]
  ]
 },
 "benchmarks": [
  {
   "titulo": "Terminal-Bench 2.1 (89 tareas x 3 intentos)",
   "columnas": [
    "Modelo",
    "Pass@1",
    "Pass@3",
    "Tokens/intento",
    "Velocidad"
   ],
   "filas": [
    [
     "Space Bunny (retirado)",
     "52,1%",
     "66,3%",
     "~1,69M",
     "mediana 979 s"
    ],
    [
     "Step 5 Preview",
     "50,2%",
     "64,0%",
     "~0,90M",
     "el más lento"
    ],
    [
     "LongCat 2.5 Preview",
     "48,7%",
     "64,0%",
     "~0,54M",
     "mediana 784 s"
    ],
    [
     "MiMo v2.5",
     "44,2%",
     "66,3%",
     "~0,57M",
     "mediana 830 s"
    ]
   ]
  },
  {
   "titulo": "Workers gratis (8-oct): Q&A + arreglar 2 tests, timeout 420 s",
   "columnas": [
    "Puesto",
    "Modelo",
    "Puntuación",
    "Segundos"
   ],
   "filas": [
    [
     "1",
     "mimo-v2.6-flash-free",
     "100",
     "129"
    ],
    [
     "2",
     "muse-spark-1.3-contributor-free",
     "99",
     "132"
    ],
    [
     "3",
     "space-bunny-free",
     "95",
     "167"
    ],
    [
     "4",
     "longcat-2.5-preview-free",
     "92",
     "214"
    ],
    [
     "5",
     "ling-3.1-flash-free",
     "91",
     "220"
    ],
    [
     "6",
     "nemotron-3-ultra-free",
     "70",
     "257"
    ],
    [
     "7",
     "nemotron-3.5-lightning-free",
     "20",
     "422"
    ],
    [
     "8",
     "exo-free · fledge-alpha-free · ling-3.0-fin-free",
     "0 (timeout)",
     "—"
    ]
   ]
  }
 ],
 "benchmarks_notas": [
  "Animación (test del caballo): ganó Space Bunny; Exo Free lo hizo con <2M tokens frente a los 35M de Space Bunny.",
  "Bug real en C#: DeepSeek V4.1 Flash High lo resolvió por $0.042 (Luna High $0.043; Terra High $0.396).",
  "MiMo-V2.6-Pro: top open-weights del índice AA (46) y en la frontera Pareto inteligencia/coste ($0.13 por tarea).",
  "Opencode Go Bench: 43 modelos de opencode.ai/go cruzados con Artificial Analysis; el debate es si Go sirve versiones cuantizadas."
 ],
 "stealth": {
  "columnas": [
   "Nombre público",
   "Qué era en realidad",
   "Cómo se supo"
  ],
  "filas": [
   [
    "Space Bunny",
    "MiniMax M3.1",
    "Filtraba etiquetas <minimax>; tokenizer coincide con M2/M3"
   ],
   [
    "Exo Free",
    "Router a GPT/Claude (probablemente Haiku 5.5); murió en horas",
    "Se cayó al llegar tráfico"
   ],
   [
    "Fledge Alpha",
    "Router: DeepSeek 4.1 + Kimi (¿K3?) + un tercero; con visión",
    "Fingerprint de tokenizer"
   ],
   [
    "big-pickle",
    "MAI de Microsoft AI (varía con el tiempo)",
    "Se autodelata al preguntarle"
   ],
   [
    "Cat Jam",
    "«CatJam by LitterBox AI»; se sospecha Groq",
    "300-350 tps y respuesta del propio modelo"
   ],
   [
    "Hy4 Preview",
    "Probablemente MiniMax / Space Bunny",
    "Comparativas de la comunidad"
   ],
   [
    "Union Alpha",
    "Se especuló Mistral",
    "Conferencia en España y contexto"
   ],
   [
    "CrofAI",
    "Wrapper de OpenRouter con hasta 20x de margen",
    "Auditoría de la comunidad → cerró"
   ],
   [
    "«greg-2-super» (OpenRouter)",
    "Ruta a Kimi K2.7 Code",
    "Nombres de ruta filtrados"
   ]
  ]
 },
 "banderas": {
  "columnas": [
   "Señal",
   "Detalle"
  ],
  "filas": [
   [
    "Bucles y repeticiones",
    "DeepSeek 4.1 repite bucles; MiMo 2.6 repite tool-calls idénticas; Muse 1.3 da 8 rondas de review sin terminar"
   ],
   [
    "Datos de entrenamiento",
    "Los modelos «Contributor» (Muse Spark) y Space Bunny entrenan con tus prompts según la doc de Go"
   ],
   [
    "Cuotas que se agotan",
    "Kimi K3 y Grok 4.6 queman la cuota en 3 prompts; el free tier se agota «en minutos» en horas punta"
   ],
   [
    "Límites opacos",
    "El límite gratis de Zen no es público y varía; cambios de precio/límite sin anuncio (DeepSeek $60→$80)"
   ],
   [
    "Cuantización",
    "Lo que sirve Go no siempre es el modelo oficial: GLM 5.3 Flash es FP8 completo, pero el debate es constante"
   ],
   [
    "Estabilidad",
    "Endpoints caídos (Step 5), y 70-87 tok/s en Go frente a 270 t/s de la API directa de DeepSeek"
   ],
   [
    "Seguridad",
    "OpenCode Desktop 2.0.26 (Windows): el permiso external_directory no salta; OpenChamber subió 1,86 GB a su relay"
   ],
   [
    "Rompe-instalaciones",
    "LongCat 2.5 Preview obligó a reinstalar el CLI a varios usuarios"
   ]
  ]
 },
 "noticias": [
  {
   "titulo": "Mistral just released Large 4 \"Le Chonk\" 🔥",
   "score": 449,
   "comentarios": 59,
   "fecha": "2026-10-06 13:07",
   "sub": "opencodeCLI",
   "url": "https://www.reddit.com/r/opencodeCLI/comments/1wz259q/mistral_just_released_large_4_le_chonk/"
  },
  {
   "titulo": "Claude Haiku 5.5 benchmarks (better than GPT-6 Luna)",
   "score": 315,
   "comentarios": 39,
   "fecha": "2026-10-07 18:15",
   "sub": "opencodeCLI",
   "url": "https://www.reddit.com/r/opencodeCLI/comments/1x03xwj/claude_haiku_55_benchmarks_better_than_gpt6_luna/"
  },
  {
   "titulo": "OpenCode v2 finally has a status line, and it's fully customizable",
   "score": 237,
   "comentarios": 35,
   "fecha": "2026-10-01 16:52",
   "sub": "opencodeCLI",
   "url": "https://www.reddit.com/r/opencodeCLI/comments/1wv4obz/opencode_v2_finally_has_a_status_line_and_its/"
  },
  {
   "titulo": "Mistral just released Large 4 \"Le Chonk\" 🔥",
   "score": 236,
   "comentarios": 43,
   "fecha": "2026-10-06 13:08",
   "sub": "opencode",
   "url": "https://www.reddit.com/r/opencode/comments/1wz25lb/mistral_just_released_large_4_le_chonk/"
  },
  {
   "titulo": "Step 5 Preview is FREE on OpenCode for a week 🔥",
   "score": 205,
   "comentarios": 33,
   "fecha": "2026-10-08 14:46",
   "sub": "opencodeCLI",
   "url": "https://www.reddit.com/r/opencodeCLI/comments/1x0sumz/step_5_preview_is_free_on_opencode_for_a_week/"
  },
  {
   "titulo": "Openchamber is actually pretty good.",
   "score": 194,
   "comentarios": 71,
   "fecha": "2026-10-04 16:17",
   "sub": "opencode",
   "url": "https://www.reddit.com/r/opencode/comments/1wxjlar/openchamber_is_actually_pretty_good/"
  },
  {
   "titulo": "Animated Horse - Space Bunny",
   "score": 141,
   "comentarios": 78,
   "fecha": "2026-10-02 21:25",
   "sub": "opencode",
   "url": "https://www.reddit.com/r/opencode/comments/1ww5o7y/animated_horse_space_bunny/"
  },
  {
   "titulo": "Step 5 Preview is FREE on OpenCode for a week 🔥",
   "score": 139,
   "comentarios": 18,
   "fecha": "2026-10-08 14:47",
   "sub": "opencode",
   "url": "https://www.reddit.com/r/opencode/comments/1x0suys/step_5_preview_is_free_on_opencode_for_a_week/"
  },
  {
   "titulo": "I made this guide to help the community ! 🤖",
   "score": 133,
   "comentarios": 15,
   "fecha": "2026-10-04 03:54",
   "sub": "opencode",
   "url": "https://www.reddit.com/r/opencode/comments/1wx617h/i_made_this_guide_to_help_the_community/"
  },
  {
   "titulo": "Exo Free - Frontier level - Wow",
   "score": 131,
   "comentarios": 47,
   "fecha": "2026-10-07 03:12",
   "sub": "opencode",
   "url": "https://www.reddit.com/r/opencode/comments/1wzm1ah/exo_free_frontier_level_wow/"
  },
  {
   "titulo": "Ling-3.1-flash is now FREE on OpenCode 🔥",
   "score": 130,
   "comentarios": 9,
   "fecha": "2026-10-02 16:34",
   "sub": "opencodeCLI",
   "url": "https://www.reddit.com/r/opencodeCLI/comments/1wvyfsz/ling31flash_is_now_free_on_opencode/"
  },
  {
   "titulo": "FIRST in my bloodline to get restricted from using muse spark",
   "score": 130,
   "comentarios": 58,
   "fecha": "2026-10-03 13:50",
   "sub": "opencode",
   "url": "https://www.reddit.com/r/opencode/comments/1wwnrdz/first_in_my_bloodline_to_get_restricted_from/"
  },
  {
   "titulo": "space bunny now costs money",
   "score": 124,
   "comentarios": 41,
   "fecha": "2026-10-06 07:19",
   "sub": "opencode",
   "url": "https://www.reddit.com/r/opencode/comments/1wyw9lc/space_bunny_now_costs_money/"
  },
  {
   "titulo": "Anthropic just introduced Claude Haiku 5.5 🔥",
   "score": 119,
   "comentarios": 7,
   "fecha": "2026-10-07 18:03",
   "sub": "opencodeCLI",
   "url": "https://www.reddit.com/r/opencodeCLI/comments/1x03mgl/anthropic_just_introduced_claude_haiku_55/"
  }
 ],
 "meta": {
  "generado": "2026-10-13 16:01 UTC",
  "subs": {
   "opencode": 1629,
   "opencodeCLI": 607
  },
  "hilos": 2185,
  "comentarios": 18407,
  "unidades": 20592,
  "ventana_dias": 45,
  "fuente_datos": "Arctic Shift API (arctic-shift.photon-reddit.com)"
 }
};
