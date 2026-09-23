# ADR 0002: Monolito modular con DuckDB en fichero

**Fecha:** 2026-09-23 · **Estado:** Aceptado

## Contexto
Lo desarrolla una sola persona, en unos 3 meses, con una demo en local. Los datos son millones de filas históricas (analítica) y pocas escrituras concurrentes.

## Decisión
Un único paquete Python con un solo proceso web y una base de datos **DuckDB** en `data/baremo.duckdb`. Las tareas largas se lanzan con `BackgroundTasks` de FastAPI y su estado se guarda en una tabla. No hay colas, ni Redis, ni Postgres.

## Alternativas descartadas
- **Postgres + pgvector + Celery + Redis** (lo que usa Compass): son más piezas de las que hacen falta. No necesitamos búsqueda semántica porque la búsqueda es por filtros y texto.
- **SQLite:** es peor para las agregaciones analíticas del recomendador.

## Consecuencias
- DuckDB solo admite un proceso escritor. La ingesta no se ejecuta mientras la web escribe análisis; en la v1 eso se resuelve con una orden de ingesta que se lanza con la web parada o de madrugada.
- El despliegue es un solo contenedor con un volumen.
