# ai-engineering-journey

Proyectos de IA aplicada, de los primeros scripts a un producto completo.

> **Estado (sep. 2026):** eligiendo el proyecto principal. La investigación está en [`investigacion/`](investigacion/).

## Estructura

```
.
├── aprendizaje/       Los primeros pasos, en el orden en que se hicieron
│   ├── 01-tool-use/        Primeras llamadas a la API de Claude y tool use
│   ├── 02-rag-basico/      RAG con ChromaDB sobre un documento de prueba
│   └── 03-agente-rag-tfg/  Agente con herramientas y RAG sobre el TFG, servido con FastAPI y Docker
└── investigacion/     Cómo se está eligiendo el proyecto principal
    ├── informes/           01: hackathones · 02: IA para empresas · 03: finanzas e inversión
    └── notas/              Notas de investigación con fuentes
```

Cada carpeta de `aprendizaje/` se ejecuta desde dentro de ella (`cd aprendizaje/03-agente-rag-tfg && uvicorn api:app`), porque las rutas a las bases vectoriales son relativas.
