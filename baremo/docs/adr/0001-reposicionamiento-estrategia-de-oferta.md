# ADR 0001: Baremo es estrategia de oferta, no radar de licitaciones

**Fecha:** 2026-09-23 · **Estado:** Aceptado

## Contexto
La idea original («Baremo v0») era un agente que acompañaba a la pyme de principio a fin. Su pieza central era decidir, con citas, si la empresa cumplía la solvencia. Al verificar riesgos encontramos **Compass** (github.com/alan-fdez/Compass, MIT, activo en septiembre de 2026), que ya resuelve el radar (ingesta de PLACSP con búsqueda híbrida) y el veredicto «¿puedo presentarme?» con citas verificadas, con un nivel de acabado alto (296 tests, golden set de 25 pliegos). Compass deja fuera a propósito el precio, los borradores, el OCR y el despliegue alojado.

## Decisión
El valor de Baremo está en **«¿cuánto ofrezco y cuántos puntos saco?»**: fórmula económica del pliego, umbral de temeridad, baja recomendada con backtest contra adjudicaciones reales, y borradores. El encaje de solvencia se mantiene como apoyo, pero no es el diferencial. No se construye radar ni alertas.

## Alternativas descartadas
- **Competir con Compass en su terreno:** aportaría poco y sería difícil de defender ante un jurado.
- **Contribuir a Compass en lugar de crear un proyecto propio:** es legítimo, pero no cumple el objetivo de tener un proyecto propio para el portfolio. Queda abierta la opción de colaborar más adelante.

## Consecuencias
- El recomendador (§8.5) y el motor (§8.3) pasan a ser el núcleo del proyecto.
- El README y la demo reconocen a Compass.
