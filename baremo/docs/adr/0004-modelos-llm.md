# ADR 0004: Modelos de Claude y cómo se eligen

**Fecha:** 2026-09-23 · **Estado:** Aceptado; se revisa con los resultados de S4 y del golden set

## Decisión
- `modelo_principal = claude-opus-5` y `modelo_extraccion = claude-opus-5` por defecto. Ambos se configuran en `.env`; el código nunca escribe un ID de modelo fuera de `config.py`.
- Adaptive thinking; `effort` `medium` para extraer y `high` para redactar. Fallbacks ante rechazo (`fallbacks="default"`, beta `server-side-fallback-2026-07-01`) en las llamadas síncronas.
- Se puede cambiar la extracción a `claude-sonnet-5` si, **en el golden set**, pierde 2 puntos de exactitud o menos y el coste de Opus 5 supera 0,50 USD por pliego (regla D4).

## Alternativas descartadas
- **Modelos gratuitos vía OpenRouter** (como Compass): el objetivo del portfolio incluye dominar la API de Anthropic (salida estructurada, caché, batch, citations y PDF nativo).
- **Haiku 4.5 para extraer:** tiene un contexto de 200k, lo que limita los PDF a 100 páginas, y no hay evidencia de su calidad con pliegos.

## Consecuencias
- Cada llamada deja su coste registrado, y la elección se justifica con datos en `docs/resultados/`.
