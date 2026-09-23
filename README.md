# ai-engineering-journey

Proyectos de IA aplicada, de los primeros scripts a un producto completo.

## Proyecto principal: [Cartera Clara](cartera-clara/)

**Tu Renta de inversor, clara.** Reúne todos tus brókeres. El cálculo fiscal lo verifican dos motores independientes ([DeclaRenta](https://github.com/GeiserX/DeclaRenta) y un motor propio en Python). La IA lee tus extractos y tus datos fiscales de Hacienda, calcula cuánto te deben otros países por exceso de retención y te lo explica todo **sin inventarse un número**. Es local, open source (GPL-3.0) y tiene servidor MCP.

→ Empieza por [cartera-clara/README.md](cartera-clara/README.md) y el [documento de diseño](cartera-clara/docs/00-documento-de-diseno.md).

## Estructura

```
.
├── cartera-clara/     Proyecto principal (Python 3.12, uv, FastAPI, SQLite, Claude API, MCP, DeclaRenta)
├── aprendizaje/       Los primeros pasos, en el orden en que se hicieron
│   ├── 01-tool-use/        Primeras llamadas a la API de Claude y tool use
│   ├── 02-rag-basico/      RAG con ChromaDB sobre un documento de prueba
│   └── 03-agente-rag-tfg/  Agente con herramientas y RAG sobre el TFG, servido con FastAPI y Docker
└── investigacion/     Cómo se eligió el proyecto
    ├── informes/           01: hackathones · 02: IA para empresas · 03: finanzas e inversión (origen de Cartera Clara)
    └── notas/              Notas de investigación con fuentes
```

Cada carpeta de `aprendizaje/` se ejecuta desde dentro de ella (`cd aprendizaje/03-agente-rag-tfg && uvicorn api:app`), porque las rutas a las bases vectoriales son relativas.
