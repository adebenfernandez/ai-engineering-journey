# Fixtures de test

| Fichero | Origen | Uso |
|---|---|---|
| `codice/entry_publicada_oviedo_2026.xml` | Entrada **real** del feed de PLACSP (sindicación 643), publicada el 15/08/2026 (expediente CS2026/94, Ayuntamiento de Oviedo). Copiada del repositorio [alan-fdez/Compass](https://github.com/alan-fdez/Compass) (licencia MIT, © 2026 Alan), `backend/tests/ingestion/fixtures/codice_entry_sample.xml`. Los datos son públicos de PLACSP. | Parser: lotes, criterios con peso, garantías, solvencia, plazos, enlaces a PCAP/PPT. |
| `codice/entry_adjudicada_SINTETICA.xml` | **Sintética**, escrita a mano. Ver el comentario de cabecera. | Parser de `TenderResult` mientras no haya una real. **Sustituir** por una salida de `spikes/s1_cobertura_placsp.py` (tarea S1-c del backlog) y borrar esta. |

Reglas:
- Ningún test descarga nada de Internet. Si necesitas un caso nuevo, guarda aquí el XML o el PDF y documenta su origen en esta tabla.
- Los PDF de pliegos reales que se añadan (golden set, fase F3) van en `pliegos/` con su URL de origen y fecha de descarga en `pliegos/ORIGEN.md`.
