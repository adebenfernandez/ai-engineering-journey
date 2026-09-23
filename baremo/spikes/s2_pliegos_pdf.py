"""Spike S2: descarga una muestra de pliegos (PCAP) reales y mide si se pueden leer.

Resuelve el riesgo R3 (pliegos escaneados / descargas que fallan).
Dependencia única fuera de la biblioteca estándar: pypdf  ->  pip install "pypdf>=5"

Uso:
    python spikes/s2_pliegos_pdf.py --ruta data/raw/licitacionesPerfilesContratanteCompleto3_202605.zip --n 40

Salida:
    spikes/resultados/s2_pliegos.json  -> una fila por pliego + resumen
    data/pliegos/<sha1>.pdf            -> los PDF descargados (quedan en caché para S4)

Criterio de "tiene capa de texto": media >= 20 caracteres no blancos por página
(umbral tomado de Compass, MIT, que lo midió sobre pliegos reales).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import random
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

from pypdf import PdfReader

sys.path.insert(0, str(Path(__file__).parent))
from s1_cobertura_placsp import NS, iterar_entradas

MIN_CHARS_POR_PAGINA = 20
PAUSA_ENTRE_DESCARGAS_S = 2.0
USER_AGENT = "baremo-spike/0.1 (proyecto open source; contacto en el README del repo)"
DIR_RESULTADOS = Path(__file__).parent / "resultados"


def urls_pcap(ruta: Path) -> list[tuple[str, str, str]]:
    """Devuelve (expediente, nombre_documento, url) de cada PCAP del origen."""
    salida: list[tuple[str, str, str]] = []
    for entry in iterar_entradas(ruta):
        cfs = entry.find("cac-place-ext:ContractFolderStatus", NS)
        if cfs is None:
            continue
        expediente = cfs.findtext("cbc:ContractFolderID", default="?", namespaces=NS)
        for ref in cfs.findall("cac:LegalDocumentReference", NS):
            nombre = ref.findtext("cbc:ID", default="", namespaces=NS)
            url = ref.findtext("cac:Attachment/cac:ExternalReference/cbc:URI", default="", namespaces=NS)
            if url:
                salida.append((expediente, nombre.strip(), url.strip()))
    return salida


def medir_pdf(ruta_pdf: Path) -> dict[str, object]:
    lector = PdfReader(ruta_pdf)
    paginas = len(lector.pages)
    chars = [len("".join((p.extract_text() or "").split())) for p in lector.pages]
    media = sum(chars) / paginas if paginas else 0.0
    return {
        "paginas": paginas,
        "chars_media_por_pagina": round(media, 1),
        "paginas_sin_texto": sum(1 for n in chars if n < MIN_CHARS_POR_PAGINA),
        "tiene_capa_texto": media >= MIN_CHARS_POR_PAGINA,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--ruta", type=Path, required=True, help="ZIP/carpeta/.atom de PLACSP (el mismo que en S1)")
    parser.add_argument("--n", type=int, default=40, help="Tamaño de la muestra aleatoria")
    parser.add_argument("--semilla", type=int, default=42)
    parser.add_argument("--pdfs", type=Path, default=Path("data/pliegos"))
    args = parser.parse_args()

    candidatos = urls_pcap(args.ruta)
    random.Random(args.semilla).shuffle(candidatos)
    muestra = candidatos[: args.n]
    args.pdfs.mkdir(parents=True, exist_ok=True)

    filas: list[dict[str, object]] = []
    for expediente, nombre, url in muestra:
        fila: dict[str, object] = {"expediente": expediente, "documento": nombre, "url": url}
        destino = args.pdfs / f"{hashlib.sha1(url.encode()).hexdigest()}.pdf"
        try:
            if not destino.exists():
                peticion = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
                with urllib.request.urlopen(peticion, timeout=60) as resp:
                    fila["http"] = resp.status
                    fila["content_type"] = resp.headers.get("Content-Type")
                    destino.write_bytes(resp.read())
                time.sleep(PAUSA_ENTRE_DESCARGAS_S)
            fila["bytes"] = destino.stat().st_size
            fila["es_pdf"] = destino.read_bytes()[:5] == b"%PDF-"
            if fila["es_pdf"]:
                fila.update(medir_pdf(destino))
        except (urllib.error.URLError, TimeoutError, OSError, ValueError) as exc:
            fila["error"] = f"{type(exc).__name__}: {exc}"
        except Exception as exc:  # pypdf lanza excepciones propias con PDFs corruptos
            fila["error"] = f"pdf_ilegible: {type(exc).__name__}: {exc}"
        filas.append(fila)
        print(json.dumps(fila, ensure_ascii=False), file=sys.stderr)

    ok = [f for f in filas if f.get("es_pdf")]
    resumen = {
        "pcap_en_origen": len(candidatos),
        "muestra": len(filas),
        "descargados_ok_pdf": len(ok),
        "errores": sum(1 for f in filas if "error" in f),
        "no_pdf": sum(1 for f in filas if f.get("es_pdf") is False),
        "con_capa_texto": sum(1 for f in ok if f.get("tiene_capa_texto")),
        "escaneados": sum(1 for f in ok if f.get("tiene_capa_texto") is False),
        "paginas_mediana": sorted(int(f["paginas"]) for f in ok)[len(ok) // 2] if ok else None,  # type: ignore[call-overload]
        "paginas_max": max((int(f["paginas"]) for f in ok), default=None),  # type: ignore[call-overload]
        "mb_max": round(max((int(f["bytes"]) for f in ok), default=0) / 1e6, 2),  # type: ignore[call-overload]
    }
    DIR_RESULTADOS.mkdir(parents=True, exist_ok=True)
    salida = DIR_RESULTADOS / "s2_pliegos.json"
    salida.write_text(json.dumps({"resumen": resumen, "filas": filas}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(resumen, ensure_ascii=False, indent=2))
    print(f"\nInforme guardado en {salida}", file=sys.stderr)


if __name__ == "__main__":
    main()
