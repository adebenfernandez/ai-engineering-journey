# ADR 0003: Parser CODICE propio en lugar de datasets de terceros

**Fecha:** 2026-09-23 · **Estado:** Aceptado

## Contexto
`BquantFinance/licitaciones-espana` publica 8,7 M de registros de PLACSP en parquet. Su parser (`nacional/licitaciones.py`) no extrae `LowerTenderAmount` ni `HigherTenderAmount`, ni criterios con peso, ni documentos, y sus ficheros van por Git LFS o en ZIP de 1,34 GB.

## Decisión
Un parser propio (`ingesta/codice.py`) sobre los ZIP oficiales, que extrae exactamente los campos de `referencias/codice-placsp.md`.

## Consecuencias
- Hay que mantener el parser. Se mitiga con fixtures reales de distintos meses (R13).
- Control total sobre el corte temporal que necesita el backtest (fechas de publicación y de adjudicación).
