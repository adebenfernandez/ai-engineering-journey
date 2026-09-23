# CLAUDE.md: Cartera Clara

## Antes de escribir código
1. Lee `docs/00-documento-de-diseno.md` §0 y las secciones que cite tu tarea.
2. Coge **la siguiente tarea sin marcar** de `docs/02-backlog.md`. Una tarea cada vez.
3. Según lo que toque la tarea, lee también:
   - fiscalidad → `docs/referencias/fiscalidad-inversiones.md`;
   - DeclaRenta o el Flex XML → `docs/referencias/declarenta-integracion.md`;
   - formatos de extractos → `docs/referencias/formatos-brokers.md`.
4. **Si falta un dato, no lo inventes.** Esto incluye reglas fiscales, números de casilla, límites de convenios, formularios, formatos y APIs. Apúntalo en «Preguntas abiertas» de `docs/01-riesgos-y-verificaciones.md` y pregunta al usuario.

## Órdenes (desde `cartera-clara/`)
```bash
uv sync
make calidad            # ruff + format + mypy --strict + pytest (sin red, LLM ni Node)
make formato
make declarenta         # solo en local: instala el motor de referencia
make test-declarenta    # tests contra la CLI real de DeclaRenta
uv run cartera-clara --help
```
Una tarea no está terminada hasta que `make calidad` sale en verde.

## Reglas
- **La IA nunca calcula.** Ninguna suma, conversión, FIFO ni decisión fiscal sale de un LLM (diseño §7.1).
- **Importes siempre en `Decimal`.** Nunca `float` con dinero. Para convertir texto a `Decimal` se usa la función de `importador_ia/cuadre.py`, que detecta el formato español o inglés.
- Nombres del dominio en español y sin tildes (`operacion`, `casilla`, `retencion`). Docstrings, mensajes y commits en español.
- Configuración solo a través de `cartera_clara.config.obtener_config()`. Nunca escribas un ID de modelo fuera de `config.py`.
- SQL solo en `src/cartera_clara/libro/`.
- Anthropic solo a través de `cartera_clara.llm.cliente` (SDK `anthropic` 1.x):
  - `messages.parse(output_format=...)`, o `beta.messages.parse(..., betas=["server-side-fallback-2026-07-01"], fallbacks="default")` para Opus 5;
  - `thinking={"type": "adaptive"}`;
  - nunca `temperature` ni `budget_tokens`.
- MCP: `from mcp.server.mcpserver import MCPServer`. **`FastMCP` no existe en mcp 2.x.**
- PDF: solo `pypdf`. Nunca PyMuPDF (AGPL).
- Prohibido `eval` y `exec`.
- DeclaRenta: solo por la CLI y desde `motores/declarenta.py`. Nunca copies su código TypeScript.
- Nunca se recomienda comprar o vender (ADR 0004).
- Privacidad:
  - no se guardan NIF, IBAN, nombres ni direcciones de los extractos en el libro;
  - ningún dato real en `tests/`.

## Tests
- Nunca usan red, la API ni Node. Se usan fixtures, ejecutores falsos y clientes LLM falsos.
- Marcadores: `red`, `llm`, `declarenta` (se ejecutan a mano).
- `tests/fixtures/flex/canonico_basico.esperado.json` es un **oráculo verificado**. No se modifica para que un test pase.
- Cada fixture nueva se documenta en `tests/fixtures/README.md`.

## Red en el entorno cloud de Claude Code
El proxy puede bloquear `data-api.ecb.europa.eu`, `cdn.sheetjs.com`, la AEAT y otros dominios (riesgo R6). No intentes saltarte el proxy. Lo que necesite red se hace en el PC del usuario, o después de permitir el dominio en *Environment → Network access*.

## Commits
- Formato `[T-Fx.y] Descripción`.
- La casilla del backlog se marca en el mismo commit.
- Si cambia el comportamiento, se actualiza el diseño en el mismo commit.
