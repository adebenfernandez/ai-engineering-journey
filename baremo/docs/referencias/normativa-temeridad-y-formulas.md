# Referencia: ofertas anormalmente bajas y fórmulas de puntuación económica

El paquete `baremo.motor` implementa esta referencia. **Todo es determinista y sin LLM.** Los casos de prueba de este documento son obligatorios: cada uno se convierte en un test parametrizado de `tests/motor/`.

> Aviso para el código y para la interfaz: Baremo calcula una **estimación orientativa**. La decisión sobre si una oferta es anormalmente baja la toma la mesa de contratación, después de un trámite de audiencia (art. 149 LCSP).

## 1. Marco legal

- **Ley 9/2017 (LCSP), art. 149.** Cuando el único criterio es el precio, se aplican los parámetros del reglamento, salvo que el pliego diga otra cosa. Cuando hay varios criterios, los parámetros **tienen que venir en el pliego**.
- **RD 1098/2001 (RGLCAP), art. 85.** Parámetros por defecto según el número de licitadores. Es lo que implementa `calcular_temeridad_rglcap85`.
- **RGLCAP, art. 86** (empresas del mismo grupo). **Fuera de alcance en v1.** La interfaz debe avisar: «si hay empresas del mismo grupo, el cálculo cambia».

**Tarea obligatoria antes de cerrar la F2:** contrastar el texto del art. 85 de este documento con el BOE consolidado (BOE-A-2001-19995) y dejar el enlace y la fecha de consulta en el docstring del módulo.

### 1.1 Texto operativo del art. 85 RGLCAP

Se consideran, en principio, desproporcionadas o temerarias las ofertas que estén en estos supuestos:

1. **Un licitador:** la oferta es inferior al presupuesto base de licitación en más de 25 unidades porcentuales.
2. **Dos licitadores:** la oferta es inferior en más de 20 unidades porcentuales a la otra oferta.
3. **Tres licitadores:** las ofertas inferiores en más de 10 unidades porcentuales a la media aritmética de las ofertas presentadas. Para calcular esa media se excluye la oferta más alta si supera la media en más de 10 unidades porcentuales. En cualquier caso, es desproporcionada la baja superior a 25 unidades porcentuales.
4. **Cuatro o más licitadores:** las ofertas inferiores en más de 10 unidades porcentuales a la media aritmética de las ofertas presentadas. Si alguna oferta supera esa media en más de 10 unidades porcentuales, se calcula una nueva media solo con las ofertas que no la superan. Si quedan menos de tres, la nueva media se calcula con las tres ofertas más bajas.

### 1.2 Las dos interpretaciones de «unidades porcentuales» (ADR 0005)

La doctrina no es uniforme, así que el motor implementa **las dos** y la interfaz muestra cuál se usa:

- **`relativa`** (por defecto): «inferior en más de X unidades porcentuales a R» significa `oferta < R × (1 − X/100)`, y «superior en más de X» significa `oferta > R × (1 + X/100)`. El tope de 25 del caso 3 significa `oferta < B × 0,75`.
- **`puntos_baja`**: se trabaja con la baja de cada oferta en puntos, `b_i = (B − o_i) / B × 100`. «Inferior en más de X a la media» significa `b_i > media(b) + X`, y «superior en más de X» significa `b_i < media(b) − X`. Con dos licitadores es `b_i > b_otro + 20`, y con uno, `b_i > 25`.

«Más de» es **estricto**: si la oferta cae justo en el umbral, **no** es temeraria.

## 2. Contrato de la función

```python
from decimal import Decimal
from typing import Literal
from pydantic import BaseModel

Interpretacion = Literal["relativa", "puntos_baja"]


class ResultadoTemeridad(BaseModel):
    interpretacion: Interpretacion
    n_ofertas: int
    media_inicial: Decimal | None  # None si n < 3
    ofertas_excluidas_de_media: list[Decimal]
    media_final: Decimal | None
    umbral_oferta: Decimal | None  # oferta por debajo de la cual es temeraria (relativa), si aplica
    temerarias: list[Decimal]  # ofertas temerarias, en el orden de entrada
    motivos: dict[str, str]  # str(oferta) -> "media" | "tope_25" | "un_licitador" | "dos_licitadores"


def calcular_temeridad_rglcap85(
    presupuesto_base_sin_iva: Decimal,
    ofertas_sin_iva: list[Decimal],
    interpretacion: Interpretacion = "relativa",
) -> ResultadoTemeridad: ...
```

Validaciones de entrada (lanzan `ValueError`): `presupuesto_base_sin_iva > 0`; `1 ≤ len(ofertas)`; cada oferta `> 0`. Una oferta mayor que el presupuesto se admite, pero se registra un aviso en el log.

Aritmética: siempre `Decimal`, sin redondear hasta mostrar el resultado. Las medias se calculan con `sum(...) / Decimal(n)`.

## 3. Casos de prueba obligatorios

Los importes están en euros sin IVA. Los resultados esperados de T1-T15 y F1-F3 se comprobaron el 2026-09-23 con una implementación de referencia independiente. Si un test no los reproduce, el fallo está en la implementación, no en esta tabla.

| # | Interpretación | B | Ofertas | Esperado `temerarias` | Por qué |
|---|---|---|---|---|---|
| T1 | relativa | 100.000 | [74.000] | [74.000] | 1 licitador: umbral 75.000 y 74.000 < 75.000 |
| T2 | relativa | 100.000 | [75.000] | [] | «más de» es estricto: 75.000 no es < 75.000 |
| T3 | relativa | 100.000 | [60.000, 80.000] | [60.000] | 2 licitadores: 80.000 × 0,80 = 64.000 y 60.000 < 64.000 |
| T4 | relativa | 100.000 | [64.000, 80.000] | [] | 64.000 no es < 64.000 |
| T5 | relativa | 100.000 | [76.000, 90.000, 95.000] | [76.000] | media 87.000; 95.000 no supera 95.700, así que no se excluye; umbral 78.300; el tope de 75.000 no aplica |
| T6 | relativa | 100.000 | [78.000, 80.000, 100.000] | [] | media 86.000; 100.000 > 94.600 y se excluye; nueva media 79.000; umbral 71.100 |
| T7 | relativa | 100.000 | [70.000, 80.000, 100.000] | [70.000] | media 83.333,33; se excluye 100.000; nueva media 75.000 y umbral 67.500, que no alcanza a 70.000; sí la alcanza el **tope de 25** (70.000 < 75.000), motivo `tope_25` |
| T8 | relativa | 125.000 | [80.000, 85.000, 90.000, 120.000] | [] | media 93.750; 120.000 > 103.125 y se excluye; nueva media 85.000; umbral 76.500 |
| T9 | relativa | 125.000 | [70.000, 85.000, 90.000, 120.000] | [70.000] | media 91.250; se excluye 120.000; nueva media 81.666,67; umbral 73.500 |
| T10 | relativa | 100.000 | [50.000, 60.000, 90.000, 95.000] | [50.000] | media 73.750; 90.000 y 95.000 > 81.125; quedan 2 (< 3), así que la media va sobre las 3 más bajas: 66.666,67; umbral 60.000; 60.000 no es < 60.000 |
| T11 | relativa | 100.000 | [66.000, 76.000, 78.000, 80.000] | [66.000] | media 75.000; ninguna > 82.500; umbral 67.500 |
| T12 | puntos_baja | 100.000 | [66.000, 76.000, 78.000, 80.000] | [] | bajas [34, 24, 22, 20], media 25; 34 no es > 35. **Mismo caso que T11 con distinto resultado:** es la demostración de que la interpretación importa |
| T13 | puntos_baja | 100.000 | [74.000] | [74.000] | baja 26 > 25 |
| T14 | puntos_baja | 100.000 | [60.000, 80.000] | [] | bajas 40 y 20; «más de 20 puntos» exige 40 > 40, que es falso. Compárese con T3 (`relativa`), donde el mismo caso sí es temerario |
| T15 | puntos_baja | 100.000 | [59.000, 80.000] | [59.000] | bajas 41 y 20; 41 > 40 |

Parámetros propios del pliego: si la extracción (§8.4 del diseño) devuelve `temeridad.fuente = "pliego_propio"` con parámetros estructurados, se usa `calcular_temeridad_parametrica(B, ofertas, parametros)`, que recibe:

```python
class ParametrosTemeridadPliego(BaseModel):
    referencia: Literal["media_ofertas", "presupuesto_base", "media_bajas"]
    umbral_puntos: Decimal  # p. ej. 10 → "más de 10 unidades"
    interpretacion: Interpretacion
    excluir_superiores_a_media_en: Decimal | None  # p. ej. 10, o None si el pliego no lo dice
```

Si el pliego describe algo que no cabe en este esquema, se devuelve `no_calculable = true` con la cita literal. **No se aproxima.**

## 4. Fórmulas de puntuación económica

Notación: `B` = presupuesto base sin IVA; `o_i` = oferta i sin IVA; `baja_i = (B − o_i) / B`; `Pmax` = puntos máximos del criterio precio; `o_min` = oferta más baja admitida; `baja_max = (B − o_min) / B`; `n` = número de ofertas admitidas.

| `tipo` | Fórmula | Parámetros extra |
|---|---|---|
| `proporcional_inversa` | `P_i = Pmax × o_min / o_i` | — |
| `lineal_bajas` | `P_i = Pmax × baja_i / baja_max`, que equivale a `Pmax × (B − o_i) / (B − o_min)` | — |
| `lineal_con_saciedad` | `P_i = Pmax × min(baja_i, u) / min(baja_max, u)` | `u` = umbral de saciedad (fracción; 0,15 = 15 %) |
| `expresion` | expresión aritmética segura (§4.2) | `expresion: str` |
| `no_simulable` | — | la interfaz muestra la cita literal y no simula |

Casos límite obligatorios:
- Si `baja_max == 0` en `lineal_bajas` o `lineal_con_saciedad`, la división es 0/0: se lanza `FormulaIndefinida` y la interfaz dice «el pliego no define este caso».
- Las ofertas temerarias **no** se excluyen automáticamente del cálculo de puntos. La función recibe la lista de ofertas **admitidas** y quien la llama decide.

### 4.1 Casos de prueba (Pmax = 60, B = 100.000)

| # | Tipo | Ofertas | Puntos esperados |
|---|---|---|---|
| F1 | proporcional_inversa | [80.000, 90.000, 100.000] | [60, 53,3333…, 48] |
| F2 | lineal_bajas | [80.000, 90.000, 100.000] | [60, 30, 0] |
| F3 | lineal_con_saciedad (u = 0,15) | [80.000, 90.000, 100.000] | [60, 40, 0] |
| F4 | expresion `"Pmax * (B - o_i) / (B - o_min)"` | [80.000, 90.000, 100.000] | [60, 30, 0] (igual que F2) |
| F5 | lineal_bajas | [100.000, 100.000] | lanza `FormulaIndefinida` |
| F6 | expresion `"__import__('os')"` | [80.000] | lanza `ExpresionNoPermitida` |

Comparación: con `Decimal`, redondeando a 4 decimales solo en el assert.

### 4.2 Evaluador de expresiones seguro

- **Prohibido usar `eval` o `exec`.** Se parsea con `ast.parse(expr, mode="eval")` y se recorre el árbol con una lista blanca de nodos.
- **Nodos permitidos:** `Expression`, `BinOp` (`Add`, `Sub`, `Mult`, `Div`, `Pow`), `UnaryOp` (`USub`, `UAdd`), `Constant` (solo `int` o `float`, que se convierten a `Decimal(str(x))`), `Name` (solo las variables de abajo), `Call` (solo `min`, `max` y `abs`, sin argumentos con nombre).
- **Variables permitidas:** `Pmax`, `B`, `o_i`, `o_min`, `o_max`, `o_media`, `baja_i`, `baja_max`, `baja_media`, `n`.
- `Pow`: el exponente debe ser una constante entre −3 y 3, para evitar cálculos gigantes.
- Longitud máxima de la expresión: 300 caracteres.
- Cualquier otro nodo lanza `ExpresionNoPermitida`, con el nombre del nodo en el mensaje.

## 5. Simulador (usa §3 y §4)

```python
def simular_puntuacion_precio(
    formula: FormulaEconomica, presupuesto: Decimal, mi_baja: Decimal, ofertas_rivales: list[Decimal]
) -> Decimal: ...


def curva_puntos(
    formula: FormulaEconomica,
    presupuesto: Decimal,
    ofertas_rivales: list[Decimal],
    bajas: list[Decimal],  # p. ej. de 0 a 0,40 en pasos de 0,005
) -> list[tuple[Decimal, Decimal, bool]]:  # (baja, puntos, es_temeraria_estimada)
    ...
```

`es_temeraria_estimada` se calcula con `calcular_temeridad_rglcap85`, o con la versión paramétrica si el pliego trae parámetros propios, sobre `ofertas_rivales + [mi_oferta]`.
