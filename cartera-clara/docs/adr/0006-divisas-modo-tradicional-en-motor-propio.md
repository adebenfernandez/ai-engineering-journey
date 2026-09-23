# ADR 0006: El motor propio usa el modo tradicional de divisas en v1

**Fecha:** 2026-09-23 · **Estado:** Aceptado

## Contexto
DeclaRenta tiene dos modos para valores en divisa:
- **Por defecto:** la ganancia se calcula en la divisa y la diferencia se convierte al tipo del día de venta; el efecto divisa va aparte (DGT V2422-20).
- **`--monodivisa`:** el coste se valora al tipo del día de compra y el efecto divisa queda dentro de la ganancia de la acción.

El primero es más complejo: exige un FIFO de divisa con aparcamientos.

## Decisión
En v1 el motor propio implementa el **modo tradicional**, y el comparador lo enfrenta a DeclaRenta ejecutado con `--monodivisa`. La interfaz muestra los resultados de DeclaRenta en su modo por defecto como principales, e indica qué modo usa cada cifra.

## Consecuencias
- Para valores en divisa, la verificación cruzada de v1 compara el modo tradicional. En EUR los dos modos coinciden.
- El modo V2422-20 queda en «Después de v1».
