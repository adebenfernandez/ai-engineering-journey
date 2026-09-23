"""Spike S3: descarga las listas de códigos (codelists) oficiales de CODICE.

Resuelve el riesgo R5 (interpretar mal ResultCode, TypeCode, ProcedureCode, etc.).
Nunca se deben "suponer" los significados de los códigos: se leen de estas listas.

Uso:
    python spikes/s3_codelists.py spikes/resultados/s1_<origen>.json

Lee el campo "list_uris_codelists" que produjo S1, descarga cada .gc (formato Genericode XML)
y guarda en docs/referencias/codelists/:
    <Nombre>.gc      -> fichero original
    <Nombre>.json    -> {codigo: nombre} extraído del Genericode
Añade además la lista de resultados de adjudicación, que S1 no ve como listURI si el feed no la
declara: TenderResultCode (ver LISTAS_EXTRA).
"""

from __future__ import annotations

import json
import sys
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

DESTINO = Path(__file__).parents[1] / "docs" / "referencias" / "codelists"
# URL inferida del patrón de las demás listas. Si da 404, buscar el nombre correcto en
# https://contrataciondelestado.es/codice/cl/ y actualizar esta constante.
LISTAS_EXTRA = ["https://contrataciondelestado.es/codice/cl/2.02/TenderResultCode-2.02.gc"]


def parsear_genericode(contenido: bytes) -> dict[str, str]:
    raiz = ET.fromstring(contenido)
    codigos: dict[str, str] = {}
    for fila in raiz.iter():
        if not fila.tag.endswith("Row"):
            continue
        valores: dict[str, str] = {}
        for valor in fila:
            if not valor.tag.endswith("Value"):
                continue
            columna = valor.attrib.get("ColumnRef", "")
            texto = "".join(t.strip() for t in valor.itertext())
            valores[columna] = texto
        codigo = valores.get("code") or valores.get("Code")
        nombre = valores.get("nombre") or valores.get("name") or valores.get("Name") or ""
        if codigo:
            codigos[codigo] = nombre
    return codigos


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    informe = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    uris = sorted(set(informe["list_uris_codelists"]) | set(LISTAS_EXTRA))
    DESTINO.mkdir(parents=True, exist_ok=True)
    for uri in uris:
        nombre = uri.rsplit("/", 1)[-1].removesuffix(".gc")
        if nombre.startswith("CPV"):
            continue  # la lista CPV es enorme; se trata aparte en la ingesta
        try:
            with urllib.request.urlopen(uri.replace("http://", "https://"), timeout=60) as resp:
                contenido = resp.read()
        except urllib.error.URLError as exc:
            print(f"ERROR {uri}: {exc}", file=sys.stderr)
            continue
        (DESTINO / f"{nombre}.gc").write_bytes(contenido)
        codigos = parsear_genericode(contenido)
        (DESTINO / f"{nombre}.json").write_text(json.dumps(codigos, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"OK {nombre}: {len(codigos)} códigos", file=sys.stderr)
        time.sleep(1)


if __name__ == "__main__":
    main()
