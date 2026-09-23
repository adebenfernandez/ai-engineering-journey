# ADR 0007: Local-first con SQLite

**Fecha:** 2026-09-23 · **Estado:** Aceptado

## Decisión
- Aplicación local de un solo usuario. Los datos van en `data/cartera.db` (SQLite, biblioteca estándar), `data/chroma/` y `data/tipos_bce.sqlite`. `data/` nunca se versiona.
- No hay cuentas, servidor propio ni telemetría.
- La demo pública es otra instancia con `CC_DEMO=1` y datos sintéticos, sin subida de ficheros.

## Alternativas descartadas
- **DuckDB:** innecesario para miles de operaciones.
- **Postgres:** exige un servidor.
- **SaaS:** plantea problemas de privacidad y dudas legales al procesar datos de terceros (ver el diseño §11).
