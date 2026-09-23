.PHONY: instalar calidad test lint tipos formato spikes-s1 spikes-s2 spikes-s3 spikes-s4 web mcp

# Todas las órdenes se ejecutan desde la carpeta baremo/.
MES ?= 202605

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
	uv run pytest -m "not red and not llm"

# --- Fase F0: verificación de riesgos (necesitan red con acceso a PLACSP) ---
spikes-s1:
	uv run python spikes/s1_cobertura_placsp.py --mes $(MES)

spikes-s2:
	uv run python spikes/s2_pliegos_pdf.py --ruta data/raw/licitacionesPerfilesContratanteCompleto3_$(MES).zip --n 40

spikes-s3:
	uv run python spikes/s3_codelists.py spikes/resultados/s1_licitacionesPerfilesContratanteCompleto3_$(MES).json

spikes-s4:
	uv run python spikes/s4_coste_tokens.py --pdfs data/pliegos --max 20

# --- A partir de F6/F7 ---
web:
	uv run uvicorn baremo.web.app:app --reload --port 8000

mcp:
	uv run python -m baremo.mcp_server
