.PHONY: instalar calidad lint tipos test formato declarenta test-declarenta web mcp

# Todas las órdenes se ejecutan desde cartera-clara/.
# Versión fijada del motor de referencia (ADR 0002). Cambiarla solo con un ADR.
DECLARENTA_REPO   := https://github.com/GeiserX/DeclaRenta.git
DECLARENTA_COMMIT := 3f88031bb2a7cdcab7d3e219a32a0d460074ee6f

instalar:
	uv sync

calidad: lint tipos test

lint:
	uv run ruff check .
	uv run ruff format --check .

formato:
	uv run ruff format .
	uv run ruff check --fix .

tipos:
	uv run mypy

test:
	uv run pytest -m "not red and not llm and not declarenta"

# Descarga y compila DeclaRenta en vendor/declarenta (necesita git, Node >= 22.13 y red).
declarenta:
	rm -rf vendor/declarenta
	git clone --quiet $(DECLARENTA_REPO) vendor/declarenta
	cd vendor/declarenta && git checkout --quiet $(DECLARENTA_COMMIT) && npm ci --no-audit --no-fund && npx tsup

test-declarenta:
	uv run pytest -m declarenta

web:
	uv run uvicorn cartera_clara.web.app:app --reload --port 8000

mcp:
	uv run python -m cartera_clara.mcp_server
