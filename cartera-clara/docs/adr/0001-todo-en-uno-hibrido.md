# ADR 0001: Producto todo en uno con motor híbrido por fases

**Fecha:** 2026-09-23 · **Estado:** Aceptado

## Contexto
La idea original era construir un calculador fiscal multibróker propio. Al verificar la competencia encontramos DeclaRenta, que es open source y gratuito y ya cubre 13 brókeres y los modelos 100, 720, 721 y D-6, pero no tiene IA. Un calculador propio empezaría muy por detrás. Lo que no existe es la capa de IA: importador, conciliación con la AEAT, explicación y recuperación de retenciones.

## Decisión
Cartera Clara es un producto **todo en uno** para el usuario, con el motor por fases:
1. **F1-F6:** DeclaRenta calcula y Cartera Clara aporta toda la capa de IA y de producto.
2. **F7:** motor propio en Python para el alcance principal (acciones y ETF, FIFO, 2 meses, dividendos y doble imposición), **validado contra DeclaRenta**.
3. **Siempre:** los dos motores se comparan y cualquier discrepancia se muestra.

## Alternativas descartadas
- **Solo motor propio:** meses para igualar lo que ya existe.
- **Solo capa de IA sin motor propio:** es menos tuyo y te deja sin la historia del doble motor.

## Consecuencias
- La interfaz `motores/base.py` es común a los dos motores.
- El proyecto depende de Node para el motor de referencia (ADR 0002).
