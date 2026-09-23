# ADR 0005: Modelos de Claude y cómo se eligen

**Fecha:** 2026-09-23 · **Estado:** Aceptado; se revisa con S4 y las evaluaciones de F3 y F5

## Decisión
- `CC_MODELO_EXTRACCION` y `CC_MODELO_PRINCIPAL` valen `claude-opus-5` por defecto. Solo se leen en `config.py`.
- Adaptive thinking, `effort` medium para extraer y high en el asistente, y fallbacks ante rechazo en las llamadas síncronas a Opus 5.
- **Para cambiar el modelo de extracción a `claude-sonnet-5`:** tiene que perder 2 puntos o menos en la evaluación del importador **y** el coste medio con Opus 5 tiene que superar 0,50 USD por documento (S4).

## Referencia de precios (2026-09, USD por millón de tokens, entrada/salida)
Opus 5 5/25 · Sonnet 5 2/10 · Haiku 4.5 1/5. Lectura de caché ×0,1; Batch −50 %.
