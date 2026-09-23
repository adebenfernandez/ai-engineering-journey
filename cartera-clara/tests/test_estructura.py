"""Comprueba que el esqueleto importa y que las fixtures de referencia existen."""

import importlib
import json
from pathlib import Path

import pytest

from cartera_clara.config import Config

PAQUETES = [
    "cartera_clara",
    "cartera_clara.cli",
    "cartera_clara.config",
    "cartera_clara.libro",
    "cartera_clara.importadores",
    "cartera_clara.exportadores",
    "cartera_clara.motores",
    "cartera_clara.divisas",
    "cartera_clara.llm",
    "cartera_clara.importador_ia",
    "cartera_clara.aeat",
    "cartera_clara.retenciones",
    "cartera_clara.conocimiento",
    "cartera_clara.agente",
    "cartera_clara.web",
    "cartera_clara.mcp_server",
]
FIXTURES = Path(__file__).parent / "fixtures"


@pytest.mark.parametrize("nombre", PAQUETES)
def test_paquete_importa(nombre: str) -> None:
    importlib.import_module(nombre)


def test_config_por_defecto(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    monkeypatch.chdir(tmp_path)  # sin .env
    config = Config()
    assert config.modelo_principal == "claude-opus-5"
    assert config.dir_datos == Path("data")


def test_fixture_flex_canonica_y_su_resultado_verificado() -> None:
    assert (FIXTURES / "flex" / "canonico_basico.xml").is_file()
    esperado = json.loads((FIXTURES / "flex" / "canonico_basico.esperado.json").read_text(encoding="utf-8"))
    # Valores obtenidos con DeclaRenta el 2026-09-23 (ver tests/fixtures/README.md).
    assert esperado["disposal_0"]["gainLossEur"] == "78.6"
    assert esperado["doubleTaxation"]["byCountry"]["DE"] == {"taxPaid": "2.64", "deductionAllowed": "1.5"}


@pytest.mark.parametrize(
    "fichero",
    ["trade-republic-sample.csv", "degiro-transactions-sample.csv", "degiro-account-sample.csv", "ibkr-sample.xml"],
)
def test_fixtures_de_brokers_presentes(fichero: str) -> None:
    assert (FIXTURES / "brokers" / fichero).is_file()


def test_salida_grabada_de_declarenta_coincide_con_el_oraculo() -> None:
    """La salida real de la CLI (grabada) y el oráculo del motor (librería) cuentan lo mismo."""
    cli = json.loads((FIXTURES / "declarenta" / "canonico_basico_2024.json").read_text(encoding="utf-8"))
    assert cli["casillas"]["0328_valor_transmision_acciones"] == "479.00"
    assert cli["casillas"]["0331_valor_adquisicion_acciones"] == "400.40"
    assert cli["casillas"]["0588_deduccion_doble_imposicion"] == "1.50"
    assert cli["dividendos"][0]["retencion_eur"] == "2.64"
