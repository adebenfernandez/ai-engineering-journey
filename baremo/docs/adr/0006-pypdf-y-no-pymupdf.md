# ADR 0006: pypdf para PDF; nada de PyMuPDF

**Fecha:** 2026-09-23 · **Estado:** Aceptado

## Contexto
PyMuPDF extrae mejor el texto y las tablas, pero su licencia es **AGPL-3.0**, incompatible con distribuir Baremo como MIT sin liberar todo bajo AGPL. pypdf es BSD.

## Decisión
Se usa pypdf para el texto por página y para trocear PDF. Las tablas difíciles (el «Cuadro de características») las lee Claude directamente del PDF (§8.4.2), y la verificación de citas tolera el orden roto (`VERIFICADA_DESORDENADA`).

## Consecuencias
- El texto de pypdf a veces sale con el orden de las tablas roto. Lo absorbe el estado `VERIFICADA_DESORDENADA`.
- Si hace falta extraer tablas de forma determinista, se evaluará `pdfplumber` (MIT) en un ADR nuevo.
