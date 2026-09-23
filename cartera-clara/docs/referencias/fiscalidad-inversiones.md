# Referencia: fiscalidad de las inversiones de un residente en España (IRPF)

> Resumen operativo para programar el **motor propio** (F7) y para las explicaciones del asistente (F5). No es asesoramiento fiscal.
>
> Fuentes principales:
> - Ley 35/2006 del IRPF (LIRPF), texto consolidado del BOE (BOE-A-2006-20764).
> - La documentación técnica de DeclaRenta (`docs/casillas.md`, commit `3f88031`), que cita las consultas vinculantes de la DGT.
> - La sede de la AEAT.
>
> **Obligatorio antes de cerrar la F7:** contrastar cada regla con su fuente oficial y anotar el enlace y la fecha de consulta en el docstring del módulo que la implementa (T-F7.0).

Marcas: **[CONFIRMADO×2]** = coinciden dos fuentes independientes (la ley o la AEAT, y DeclaRenta o la investigación). **[PENDIENTE]** = falta confirmarlo.

## 1. Alcance del motor propio en v1

- **Incluye:** acciones y ETF cotizados (compra y venta), dividendos en efectivo con su retención en origen, comisiones, divisas EUR/USD/GBP/CHF, regla de los 2 meses y compensación de pérdidas.
- **Fuera de v1:** fondos con traspaso, derivados, cripto, bonos, *scrip dividends*, fusiones, escisiones, préstamo de valores, varios titulares y modelos 720/721/D-6. Para todo eso **manda DeclaRenta**.

## 2. Ganancias y pérdidas por venta de valores

| Regla | Contenido | Fuente | Estado |
|---|---|---|---|
| FIFO | Con valores homogéneos, se consideran vendidos los que se compraron primero. Se aplica **por valor (ISIN) sumando todas las cuentas y brókeres**. | Art. 37.2 LIRPF | CONFIRMADO×2 |
| Valor de adquisición | Precio × cantidad + comisiones + tributos de la compra | Art. 35.1 LIRPF | CONFIRMADO×2 |
| Valor de transmisión | Precio × cantidad − comisiones − tributos de la venta | Art. 35.2 LIRPF | CONFIRMADO×2 |
| Venta parcial | El coste del lote se reparte en proporción a la cantidad vendida. En la fixture canónica: 4/10 × (1.000 + 1) = 400,40 €. | Consecuencia del art. 35 | VERIFICADO con DeclaRenta |
| Regla de los 2 meses (cotizados) | Si vendes con **pérdida** y compras valores homogéneos en los 2 meses anteriores o posteriores, la pérdida **se difiere** en la parte proporcional a la cantidad recomprada, y se integra al vender esos valores. | Art. 33.5.f LIRPF; DGT V0913-08, V2481-20, V3282-18 | CONFIRMADO×2 |
| No cotizados | Igual, con una ventana de 1 año | Art. 33.5.g LIRPF | CONFIRMADO×2 (fuera de v1) |

## 3. Dividendos y doble imposición

| Regla | Contenido | Fuente | Estado |
|---|---|---|---|
| Ingreso | El dividendo **bruto**, antes de retenciones, es rendimiento del capital mobiliario | Art. 25.1.a LIRPF | CONFIRMADO×2 |
| Conversión | Al tipo del BCE del día de pago | DGT V0583-16 (según DeclaRenta) | PENDIENTE de leer la consulta |
| Deducción por doble imposición internacional | Por país: el **menor** entre (a) el impuesto pagado fuera, **limitado al tipo del convenio** × bruto, y (b) el impuesto español correspondiente a esa renta | Art. 80 LIRPF; convenios | CONFIRMADO×2 (fórmula implementada en DeclaRenta, verificada con la fixture: DE retenido 2,64; límite 15 % × 10 = 1,50) |
| Exceso reclamable | Retenido − límite del convenio × bruto. **No se deduce en España**; se reclama a la administración del país de origen. | Convenios; AEAT | CONFIRMADO×2 (en la fixture, 2,64 − 1,50 = **1,14 €**) |

**Tipos de retención en origen y del convenio.** Los usa el recuperador (§8.6 del diseño) y se guardan en `src/cartera_clara/retenciones/convenios.json` (T-F6.1) con su fuente. Valores de la investigación, **todos PENDIENTES de verificar** en el texto de cada convenio publicado en el BOE:

| País | Retención habitual en origen | Límite del convenio para dividendos de cartera | Estado |
|---|---|---|---|
| EE. UU. | 15 % con W-8BEN (30 % sin él) | 15 % | PENDIENTE |
| Alemania | 26,375 % | 15 % | PENDIENTE |
| Suiza | 35 % | 15 % | PENDIENTE |
| Francia | 25 % (12,8 % con formulario) | 15 % | PENDIENTE |
| Países Bajos | 15 % | 15 % | PENDIENTE |
| Irlanda | 25 % en general; muchos ETF domiciliados en Irlanda no reparten o no retienen | 15 % | PENDIENTE |

Regla para el código: si un país no está en el JSON, **no se inventa**. El recuperador muestra «país sin datos de convenio» y el cálculo de la deducción lo hace DeclaRenta.

## 4. Divisas

| Regla | Contenido | Fuente | Estado |
|---|---|---|---|
| Tipo de cambio | Diario del BCE; en días sin cotización, el día hábil anterior | Práctica aceptada; DGT V2324-10 y V0583-16 (según DeclaRenta). No hay una norma que imponga una fuente concreta. | CONFIRMADO×2 como práctica |
| Ganancia de un valor en divisa (modo por defecto de DeclaRenta) | La ganancia se calcula **en la divisa del valor** y solo la diferencia se pasa a euros al tipo del día de **venta**. El efecto divisa va aparte, como elemento patrimonial (casillas 1633/1637). | DGT V2422-20 y V0152-26 (según DeclaRenta) | PENDIENTE de leer las consultas |
| Modo tradicional (`--monodivisa`) | El coste se valora al tipo del día de compra y la venta al del día de venta; el efecto divisa queda dentro de la ganancia de la acción | Art. 35.1 (según DeclaRenta) | CONFIRMADO×1 |

**Decisión (ADR 0006):** el motor propio implementa en v1 el **modo tradicional** para valores en divisa, que es más sencillo. Se compara con DeclaRenta ejecutado con `--monodivisa`. El modo DGT V2422-20 queda para después de v1.

## 5. Integración en la base del ahorro

| Regla | Contenido | Fuente | Estado |
|---|---|---|---|
| Compensación | Primero se compensan entre sí las ganancias y pérdidas patrimoniales, y por otro lado los rendimientos del capital mobiliario. Si queda un saldo negativo en uno de los dos grupos, se compensa con el positivo del otro **hasta el 25 %** de ese saldo positivo. | Art. 49 LIRPF | CONFIRMADO×2 |
| Arrastre | Lo que no se puede compensar pasa a los **4 ejercicios siguientes** | Art. 49 LIRPF | CONFIRMADO×2 |
| Tramos de la base del ahorro (2025) | Hasta 6.000 €: 19 %; 6.000-50.000: 21 %; 50.000-200.000: 23 %; 200.000-300.000: 27 %; más de 300.000: 30 % | Art. 66.1 LIRPF, modificado por la Ley 7/2024 | CONFIRMADO×2 |
| Tramos del ejercicio 2026 | Se declara en la campaña de 2027 | — | **PENDIENTE**: comprobar que no cambian |

## 6. Casillas del Modelo 100 (ejercicio 2025, campaña 2026)

Según la documentación de DeclaRenta y la investigación. **Para el ejercicio 2026 (campaña 2027) hay que verificarlas contra el Manual práctico de Renta 2026 de la AEAT** (T-F0.4), porque la AEAT puede renumerarlas. El código lee el mapeo de `src/cartera_clara/aeat/casillas_<ejercicio>.json` y **no escribe números de casilla a mano**.

| Casilla | Concepto |
|---|---|
| 0027 | Intereses de cuentas, depósitos y activos financieros |
| 0029 | Dividendos brutos |
| 0328 | Valor de transmisión de acciones negociadas |
| 0331 | Valor de adquisición de acciones negociadas |
| 1633 / 1637 | Valor de transmisión / adquisición de otros elementos (divisa, cripto, opciones…) |
| 0588 | Deducción por doble imposición internacional |
| 0597 | Retenciones del capital mobiliario |

Según la investigación, el error de Trade Republic en la Renta 2025 fue meter ventas de acciones en la **0031**, que es rendimiento del capital mobiliario, cuando debían ir a 0328/0331.

## 7. Modelo 720 (solo aviso en v1; lo genera DeclaRenta)

- Hay obligación si el valor conjunto de los **valores depositados en el extranjero** supera **50.000 €** a 31 de diciembre. Si ya se presentó, hay que volver a presentarlo cuando el valor aumenta más de 20.000 €.
- Fuente: disposición adicional 18ª de la LGT y RD 1065/2007, art. 42 ter. Estado: CONFIRMADO×1; hay que verificarlo con la AEAT.
- Trade Republic: la cuenta de valores está en Alemania aunque el efectivo tenga IBAN español (según la investigación). Estado: PENDIENTE.
