# ai-engineering-journey

Proyectos de IA aplicada, de los primeros scripts a un producto completo.

## Proyecto principal: [Baremo](baremo/)

**Cuánto ofertar, cuántos puntos sacarás y el borrador de tu oferta** para licitaciones públicas españolas. Usa datos abiertos de PLACSP, extrae los pliegos con Claude verificando cada cita, aplica reglas legales deterministas y recomienda una baja con un modelo evaluado contra adjudicaciones reales.

→ Empieza por [baremo/README.md](baremo/README.md) y el [documento de diseño](baremo/docs/00-documento-de-diseno.md).

## Estructura

```
.
├── baremo/            Proyecto principal (Python 3.12, uv, FastAPI, DuckDB, Claude API, MCP)
├── aprendizaje/       Los primeros pasos, en el orden en que se hicieron
│   ├── 01-tool-use/        Primeras llamadas a la API de Claude y tool use
│   ├── 02-rag-basico/      RAG con ChromaDB sobre un documento de prueba
│   └── 03-agente-rag-tfg/  Agente con herramientas y RAG sobre el TFG, servido con FastAPI y Docker
└── investigacion/     Cómo se eligió el proyecto
    ├── informes/           01: hackathones · 02: IA para empresas (Baremo) · 03: finanzas e inversión
    └── notas/              Notas de investigación con fuentes
```

Cada carpeta de `aprendizaje/` se ejecuta desde dentro de ella (`cd aprendizaje/03-agente-rag-tfg && uvicorn api:app`), porque las rutas a las bases vectoriales son relativas.
