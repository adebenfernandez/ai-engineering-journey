"""Comprueba que el esqueleto del proyecto importa y que las fixtures existen."""

import importlib
from pathlib import Path

import pytest

from baremo.config import Config

PAQUETES = [
    "baremo",
    "baremo.cli",
    "baremo.config",
    "baremo.ingesta",
    "baremo.datos",
    "baremo.motor",
    "baremo.llm",
    "baremo.pliegos",
    "baremo.recomendador",
    "baremo.borradores",
    "baremo.web",
    "baremo.mcp_server",
]
FIXTURES = Path(__file__).parent / "fixtures" / "codice"


@pytest.mark.parametrize("nombre", PAQUETES)
def test_paquete_importa(nombre: str) -> None:
    importlib.import_module(nombre)


def test_config_por_defecto(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    monkeypatch.chdir(tmp_path)  # sin .env
    config = Config()
    assert config.modelo_principal == "claude-opus-5"
    assert config.db == Path("data/baremo.duckdb")


def test_fixtures_codice_presentes() -> None:
    assert (FIXTURES / "entry_publicada_oviedo_2026.xml").is_file()
    assert (FIXTURES / "entry_adjudicada_SINTETICA.xml").is_file()
