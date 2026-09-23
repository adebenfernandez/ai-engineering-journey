# CLAUDE.md: Baremo

Instrucciones para Claude Code cuando trabaja dentro de `baremo/`.

## Antes de escribir código
1. Lee `docs/00-documento-de-diseno.md` §0 y la sección que cite tu tarea.
2. Coge **la siguiente tarea sin marcar** de `docs/02-backlog.md`. No te saltes tareas ni hagas dos a la vez.
3. Si la tarea toca PLACSP, lee `docs/referencias/codice-placsp.md`. Si toca temeridad o fórmulas, lee `docs/referencias/normativa-temeridad-y-formulas.md`.
4. **Si te falta un dato, no lo inventes.** Esto incluye un XPath, el significado de un código, una regla legal, un umbral, un nombre de API o una versión. Añádelo a «Preguntas abiertas» en `docs/01-riesgos-y-verificaciones.md` y pregunta al usuario.

## Órdenes (siempre desde `baremo/`)
```bash
uv sync                          # dependencias
make calidad                     # ruff check + ruff format --check + mypy --strict + pytest (sin red ni LLM)
make formato                     # aplica ruff format y ruff --fix
uv run pytest tests/motor -q     # un paquete concreto
uv run baremo --help             # CLI
```
Una tarea no está terminada hasta que `make calidad` sale en verde.

## Reglas de código
- Python 3.12 y `mypy --strict`, sin `Any` salvo en la frontera con librerías sin tipos. Pydantic v2 para todo dato que entra o sale de un módulo.
- **Nombres del dominio en español, sin tildes** (`licitacion`, `lote`, `baja`, `presupuesto_sin_iva`). Docstrings, mensajes y commits en español.
- `motor/` usa `Decimal`; `recomendador/` usa `float`. Se convierte solo en `motor/modelos.py`.
- SQL solo dentro de `src/baremo/datos/`.
- La configuración se lee solo con `baremo.config.obtener_config()`. Nunca `os.environ` directo. Nunca escribas un ID de modelo fuera de `config.py`.
- **El modelo extrae; el código decide.** Ningún veredicto ni cálculo sale de un LLM.
- Llamadas a Anthropic solo a través de `baremo.llm.cliente`, con el SDK `anthropic` 1.x: `messages.parse(output_format=...)`, o `beta.messages.parse(..., betas=["server-side-fallback-2026-07-01"], fallbacks="default")` para Opus 5. No envíes `temperature` ni `budget_tokens`. Usa `thinking={"type": "adaptive"}`.
- MCP: SDK `mcp` 2.x, `from mcp.server.mcpserver import MCPServer`. **`FastMCP` ya no existe en 2.x.**
- PDF: solo `pypdf` (ADR 0006). Nunca PyMuPDF.
- `eval` y `exec` están prohibidos en todo el proyecto.
- No añadas dependencias sin justificarlo en el commit y actualizar el §6.2 del diseño.

## Tests
- Los tests **nunca** usan red ni la API. Todo externo se prueba con fixtures (`tests/fixtures/`), `httpx.MockTransport` o un cliente LLM falso.
- Los tests que necesitan red o API llevan `@pytest.mark.red` o `@pytest.mark.llm` y se ejecutan a mano.
- Los casos legales T1-T15 y F1-F6 de la referencia son obligatorios y **no se cambian para que pase un test**.
- Toda fixture nueva se documenta en `tests/fixtures/README.md` con su origen.

## Red en el entorno cloud
En la nube de Claude Code, el proxy de salida bloquea `contrataciondelestado.es` y `contrataciondelsectorpublico.gob.es` (riesgo R8). La ingesta real y los spikes se ejecutan en el PC del usuario, o después de añadir esos dominios en *Environment → Network access*. No intentes saltarte el proxy.

## Commits
- Formato: `[T-F1.3] Descripción corta en español`.
- Marca la tarea en `docs/02-backlog.md` en el mismo commit.
- Si cambias el comportamiento, actualiza el documento de diseño en ese mismo commit.
