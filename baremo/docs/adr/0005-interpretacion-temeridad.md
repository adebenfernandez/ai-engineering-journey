# ADR 0005: Dos interpretaciones de «unidades porcentuales» en el art. 85 RGLCAP

**Fecha:** 2026-09-23 · **Estado:** Aceptado

## Contexto
«Inferior en más de 10 unidades porcentuales a la media» se aplica en la práctica de dos maneras: en relación con la referencia (`o < media × 0,9`) o en puntos de baja (`b_i > media(b) + 10`). Dan resultados distintos: en los casos T11 y T12 de la referencia, la misma oferta es temeraria con una interpretación y no con la otra.

## Decisión
El motor implementa las dos (`Interpretacion = Literal["relativa", "puntos_baja"]`). Por defecto usa `relativa`, que es la más prudente porque marca temeraria antes. La interfaz dice qué interpretación usa y permite cambiarla. Si el pliego define sus propios parámetros, mandan esos.

## Consecuencias
- Hay más tests: T12, T14 y T15 cubren la interpretación en puntos.
- Mensaje al usuario: «Consulta el pliego; la mesa de contratación decide».
