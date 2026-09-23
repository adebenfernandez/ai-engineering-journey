"""Spike S1: mide qué campos trae de verdad el feed ATOM/CODICE de PLACSP.

Resuelve los riesgos R1 (enlaces a pliegos) y R2 (datos de adjudicación para el backtest).
Solo usa la biblioteca estándar para que se pueda ejecutar en cualquier máquina.

Uso:
    # 1) Descargar y analizar un mes concreto (necesita red con acceso a PLACSP)
    python spikes/s1_cobertura_placsp.py --mes 202605

    # 2) Analizar un ZIP ya descargado, o una carpeta con ficheros .atom, o un .atom/.xml suelto
    python spikes/s1_cobertura_placsp.py --ruta data/raw/licitacionesPerfilesContratanteCompleto3_202605.zip

Salida:
    spikes/resultados/s1_<origen>.json -> métricas de cobertura
                                          (umbrales de decisión en docs/01-riesgos-y-verificaciones.md)
    spikes/resultados/s1_ejemplos/     -> hasta 5 entradas adjudicadas con LowerTenderAmount
                                          (reales si el origen es PLACSP), para sustituir la
                                          fixture sintética de tests.
"""

from __future__ import annotations

import argparse
import io
import json
import sys
import urllib.request
import xml.etree.ElementTree as ET
import zipfile
from collections import Counter
from collections.abc import Iterator
from pathlib import Path

URL_MES = (
    "https://contrataciondelsectorpublico.gob.es/sindicacion/sindicacion_643/"
    "licitacionesPerfilesContratanteCompleto3_{mes}.zip"
)

NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "cac": "urn:dgpe:names:draft:codice:schema:xsd:CommonAggregateComponents-2",
    "cbc": "urn:dgpe:names:draft:codice:schema:xsd:CommonBasicComponents-2",
    "cac-place-ext": "urn:dgpe:names:draft:codice-place-ext:schema:xsd:CommonAggregateComponents-2",
    "cbc-place-ext": "urn:dgpe:names:draft:codice-place-ext:schema:xsd:CommonBasicComponents-2",
}
ATOM_ENTRY = "{http://www.w3.org/2005/Atom}entry"
DIR_RESULTADOS = Path(__file__).parent / "resultados"


def _xml_streams(ruta: Path) -> Iterator[tuple[str, io.BufferedIOBase]]:
    """Devuelve (nombre, flujo binario) de cada fichero ATOM/XML dentro de la ruta."""
    if ruta.is_dir():
        for fichero in sorted(ruta.rglob("*")):
            if fichero.suffix.lower() in {".atom", ".xml"}:
                with fichero.open("rb") as flujo:
                    yield fichero.name, flujo
    elif ruta.suffix.lower() == ".zip":
        with zipfile.ZipFile(ruta) as zf:
            for nombre in sorted(zf.namelist()):
                if nombre.lower().endswith((".atom", ".xml")):
                    with zf.open(nombre) as flujo:
                        yield nombre, flujo  # type: ignore[misc]
    else:
        with ruta.open("rb") as flujo:
            yield ruta.name, flujo


def iterar_entradas(ruta: Path) -> Iterator[ET.Element]:
    """Itera los <entry> de todos los ficheros sin cargar el XML entero en memoria."""
    for _nombre, flujo in _xml_streams(ruta):
        for _evento, elem in ET.iterparse(flujo, events=("end",)):
            if elem.tag == ATOM_ENTRY:
                yield elem
                elem.clear()


def _txt(elem: ET.Element | None, ruta: str) -> str | None:
    if elem is None:
        return None
    nodo = elem.find(ruta, NS)
    return nodo.text.strip() if nodo is not None and nodo.text else None


def analizar(ruta: Path, dir_ejemplos: Path) -> dict[str, object]:
    c: Counter[str] = Counter()
    estados: Counter[str] = Counter()
    result_codes: Counter[str] = Counter()
    list_uris: set[str] = set()
    ejemplos_guardados = 0
    dir_ejemplos.mkdir(parents=True, exist_ok=True)

    for entry in iterar_entradas(ruta):
        c["entradas"] += 1
        cfs = entry.find("cac-place-ext:ContractFolderStatus", NS)
        if cfs is None:
            c["sin_contract_folder_status"] += 1
            continue
        for nodo in cfs.iter():
            uri = nodo.attrib.get("listURI")
            if uri:
                list_uris.add(uri)
        estados[_txt(cfs, "cbc-place-ext:ContractFolderStatusCode") or "?"] += 1

        if cfs.find("cac:LegalDocumentReference/cac:Attachment/cac:ExternalReference/cbc:URI", NS) is not None:
            c["con_pcap_url"] += 1
        if cfs.find("cac:TechnicalDocumentReference/cac:Attachment/cac:ExternalReference/cbc:URI", NS) is not None:
            c["con_ppt_url"] += 1
        if cfs.find(".//cac:AwardingCriteria/cbc:WeightNumeric", NS) is not None:
            c["con_criterios_con_peso"] += 1
        if cfs.find("cac:ProcurementProjectLot", NS) is not None:
            c["con_lotes"] += 1
        if _txt(cfs, "cac:ProcurementProject/cac:BudgetAmount/cbc:TaxExclusiveAmount"):
            c["con_presupuesto_sin_iva"] += 1

        resultados = cfs.findall("cac:TenderResult", NS)
        if resultados:
            c["con_tender_result"] += 1
            c["tender_results_total"] += len(resultados)
        tiene_lower = False
        for tr in resultados:
            result_codes[_txt(tr, "cbc:ResultCode") or "?"] += 1
            for campo in (
                "cbc:ReceivedTenderQuantity",
                "cbc:LowerTenderAmount",
                "cbc:HigherTenderAmount",
                "cbc:SMEAwardedIndicator",
                "cbc:AwardDate",
                "cac:WinningParty/cac:PartyIdentification/cbc:ID",
                "cac:AwardedTenderedProject/cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount",
                "cac:AwardedTenderedProject/cbc:ProcurementProjectLotID",
            ):
                if _txt(tr, campo):
                    c[f"tr_con_{campo.split(':')[-1]}"] += 1
            tiene_lower = tiene_lower or bool(_txt(tr, "cbc:LowerTenderAmount"))

        if tiene_lower and ejemplos_guardados < 5:
            ejemplos_guardados += 1
            destino = dir_ejemplos / f"entry_adjudicada_{ejemplos_guardados}.xml"
            destino.write_bytes(ET.tostring(entry, encoding="utf-8"))

    total = c["entradas"] or 1
    total_tr = c["tender_results_total"] or 1
    porcentajes_entrada = {
        k: round(100 * c[k] / total, 1)
        for k in (
            "con_pcap_url",
            "con_ppt_url",
            "con_criterios_con_peso",
            "con_lotes",
            "con_presupuesto_sin_iva",
            "con_tender_result",
        )
    }
    porcentajes_tender_result = {
        k: round(100 * v / total_tr, 1) for k, v in sorted(c.items()) if k.startswith("tr_con_")
    }
    return {
        "origen": str(ruta),
        "entradas": c["entradas"],
        "tender_results_total": c["tender_results_total"],
        "pct_sobre_entradas": porcentajes_entrada,
        "pct_sobre_tender_results": porcentajes_tender_result,
        "estados_expediente": dict(estados.most_common()),
        "result_codes": dict(result_codes.most_common()),
        "list_uris_codelists": sorted(list_uris),
        "ejemplos_guardados": ejemplos_guardados,
    }


def descargar_mes(mes: str, destino_dir: Path) -> Path:
    destino_dir.mkdir(parents=True, exist_ok=True)
    url = URL_MES.format(mes=mes)
    destino = destino_dir / Path(url).name
    if not destino.exists():
        print(f"Descargando {url} ...", file=sys.stderr)
        urllib.request.urlretrieve(url, destino)
    return destino


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    grupo = parser.add_mutually_exclusive_group(required=True)
    grupo.add_argument("--mes", help="AAAAMM, p. ej. 202605")
    grupo.add_argument("--ruta", type=Path, help="ZIP, carpeta o fichero .atom/.xml")
    parser.add_argument("--raw", type=Path, default=Path("data/raw"), help="Dónde guardar los ZIP descargados")
    args = parser.parse_args()

    ruta = descargar_mes(args.mes, args.raw) if args.mes else args.ruta
    informe = analizar(ruta, DIR_RESULTADOS / "s1_ejemplos")
    DIR_RESULTADOS.mkdir(parents=True, exist_ok=True)
    salida = DIR_RESULTADOS / f"s1_{Path(ruta).stem}.json"
    salida.write_text(json.dumps(informe, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(informe, ensure_ascii=False, indent=2))
    print(f"\nInforme guardado en {salida}", file=sys.stderr)


if __name__ == "__main__":
    main()
