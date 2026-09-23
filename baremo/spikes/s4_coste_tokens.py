"""Spike S4: mide cuántos tokens cuesta pasar cada pliego a Claude (sin generar nada).

Resuelve el riesgo R6 (coste de extracción) con datos reales en lugar de estimaciones.
Usa el endpoint de conteo de tokens, que no genera texto (consultar su precio vigente en la
documentación de Anthropic antes de lanzarlo sobre cientos de PDFs).

Requisitos:
    pip install "anthropic>=1,<2"
    export ANTHROPIC_API_KEY=...   (o `ant auth login`)

Uso:
    python spikes/s4_coste_tokens.py --pdfs data/pliegos --max 20

Entrada: los PDF que dejó S2 en data/pliegos/.
Salida:  spikes/resultados/s4_tokens.json con tokens por pliego y coste estimado por modelo.

Precios (USD por millón de tokens de entrada) a 2026-09, de la tabla de modelos de Anthropic.
Actualizar PRECIOS_ENTRADA si cambian.
"""

from __future__ import annotations

import argparse
import base64
import json
import statistics
import sys
from pathlib import Path

import anthropic

PRECIOS_ENTRADA = {"claude-opus-5": 5.00, "claude-sonnet-5": 2.00, "claude-haiku-4-5": 1.00}
MODELOS = ["claude-opus-5", "claude-sonnet-5"]
LIMITE_BYTES_PETICION = 32 * 1024 * 1024
DIR_RESULTADOS = Path(__file__).parent / "resultados"


def contar(cliente: anthropic.Anthropic, modelo: str, pdf: Path) -> int:
    datos = base64.standard_b64encode(pdf.read_bytes()).decode("ascii")
    respuesta = cliente.messages.count_tokens(
        model=modelo,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "document", "source": {"type": "base64", "media_type": "application/pdf", "data": datos}},
                    {"type": "text", "text": "Extrae los datos del pliego."},
                ],
            }
        ],
    )
    return respuesta.input_tokens


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--pdfs", type=Path, default=Path("data/pliegos"))
    parser.add_argument("--max", type=int, default=20)
    args = parser.parse_args()

    cliente = anthropic.Anthropic()
    filas: list[dict[str, object]] = []
    for pdf in sorted(args.pdfs.glob("*.pdf"))[: args.max]:
        fila: dict[str, object] = {"pdf": pdf.name, "bytes": pdf.stat().st_size}
        if pdf.stat().st_size > LIMITE_BYTES_PETICION:
            fila["error"] = "supera 32 MB: hay que trocear el PDF por páginas antes de enviarlo"
        else:
            for modelo in MODELOS:
                try:
                    fila[f"tokens_{modelo}"] = contar(cliente, modelo, pdf)
                except anthropic.BadRequestError as exc:
                    fila[f"error_{modelo}"] = exc.message
                except anthropic.APIStatusError as exc:
                    fila[f"error_{modelo}"] = f"HTTP {exc.status_code}: {exc.message}"
        filas.append(fila)
        print(json.dumps(fila, ensure_ascii=False), file=sys.stderr)

    resumen: dict[str, object] = {"pliegos": len(filas)}
    for modelo in MODELOS:
        tokens = [int(f[f"tokens_{modelo}"]) for f in filas if f"tokens_{modelo}" in f]  # type: ignore[call-overload]
        if tokens:
            mediana = statistics.median(tokens)
            resumen[modelo] = {
                "tokens_mediana": mediana,
                "tokens_max": max(tokens),
                "usd_entrada_mediana_por_pliego": round(mediana * PRECIOS_ENTRADA[modelo] / 1e6, 4),
                "usd_entrada_mediana_por_pliego_batch": round(mediana * PRECIOS_ENTRADA[modelo] / 2e6, 4),
            }
    DIR_RESULTADOS.mkdir(parents=True, exist_ok=True)
    salida = DIR_RESULTADOS / "s4_tokens.json"
    salida.write_text(json.dumps({"resumen": resumen, "filas": filas}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(resumen, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
