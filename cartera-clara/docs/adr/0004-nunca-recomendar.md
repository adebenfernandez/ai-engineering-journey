# ADR 0004: Nunca recomendar inversiones ni planificación fiscal

**Fecha:** 2026-09-23 · **Estado:** Aceptado

## Contexto
Según MiFID II y ESMA (2023), es asesoramiento de inversión una recomendación personalizada, es decir, presentada como idónea o basada en las circunstancias de la persona. Un descargo no evita que algo se considere asesoramiento. Ver el informe `investigacion/informes/03…`.

## Decisión
- Cartera Clara **describe y calcula** sobre operaciones pasadas del usuario. **Nunca:**
  - recomienda comprar, vender o mantener;
  - pide perfil de riesgo, edad u objetivos;
  - sugiere estrategias fiscales («vende para compensar»).
- El asistente rechaza esas peticiones y redirige a información general de `docs/referencias/`. Lo comprueba una evaluación de 30 preguntas que tiene que pasar al 100 % (T-F5.5).
- Descargo en cada pantalla y documento: «Borrador para revisar. No es asesoramiento fiscal ni de inversión».

## Consecuencias
Hay funciones atractivas que no se harán («optimizador fiscal»). Es lo que permite publicarlo con tranquilidad.
