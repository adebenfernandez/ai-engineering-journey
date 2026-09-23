# Referencia: integración con DeclaRenta (motor de referencia)

Qué significa cada marca:
- **[VERIFICADO]**: lo he ejecutado o leído en el código fuente del commit fijado.
- **[PENDIENTE]**: hay que comprobarlo.

**Regla para Claude Code:** si necesitas un comportamiento de DeclaRenta que no está aquí, léelo en `vendor/declarenta/src/` (después de `make declarenta`). No lo supongas.

## 1. Versión fijada

| Dato | Valor |
|---|---|
| Repositorio | https://github.com/GeiserX/DeclaRenta |
| Commit | `3f88031bb2a7cdcab7d3e219a32a0d460074ee6f` (v0.58.24, 21/09/2026) [VERIFICADO] |
| Licencia | GPL-3.0 [VERIFICADO] |
| Requisitos | Node `^20.19.0 || >=22.13.0` [VERIFICADO en `package.json`] |
| Instalación | `make declarenta`: clona en `vendor/declarenta`, hace `git checkout` del commit, `npm ci` y `npx tsup`, y deja la CLI en `vendor/declarenta/dist/cli.js` [VERIFICADO] |

Nota de instalación: la dependencia `xlsx` se descarga de `cdn.sheetjs.com`. Si tu red bloquea ese dominio, `npm ci` falla. En tu PC no debería pasar. En el entorno cloud de Claude Code sí está bloqueado (riesgo R6).

Para cambiar de versión hay que escribir un ADR nuevo, volver a grabar las salidas de `tests/fixtures/declarenta/` y revisar las diferencias.

## 2. CLI [VERIFICADO]

```bash
node vendor/declarenta/dist/cli.js convert --input <fichero> [--input <fichero> ...] --year <AAAA> --format json [--prior-losses <json>] [--monodivisa]
```

- Detecta el bróker automáticamente (`--broker <nombre>` para forzarlo). Nombres: Interactive Brokers, Freedom24, Revolut, eToro, Lightyear, Flatex, Degiro, Scalable Capital, Trade Republic, Trading 212, Binance, Coinbase, Kraken.
- Si se pasan varios ficheros, hace **FIFO cruzado** entre brókeres y entre años.
- **Descarga los tipos de cambio del BCE de Internet** (`https://data-api.ecb.europa.eu/service/data/EXR/...`). Sin red hacia ese dominio falla con `ECB API error ... 403`. Por eso los tests de CI no la ejecutan (§5).
- `--monodivisa` es el modo tradicional: valora el coste en divisa al tipo del día de **compra** y mete el efecto divisa en la línea de la acción. El modo por defecto aplica el criterio de la DGT V2422-20 (ver `fiscalidad-inversiones.md` §4).
- La salida JSON va a stdout y los mensajes de progreso a stderr.

### 2.1 Estructura del JSON de `convert -f json`

Leída de `src/cli/index.ts`, función `formatReport`:

```jsonc
{
  "year": 2025,
  "casillas": {
    "0029_dividendos_brutos": "…",
    "0597_retenciones_capital_mobiliario": "…",
    "intereses_margen_no_deducible_informativo": "…",
    "0027_intereses_cuentas": "…",
    "0304_ganancias_no_derivadas_transmision_base_general": "…",
    "0328_valor_transmision_acciones": "…",
    "0331_valor_adquisicion_acciones": "…",
    "1633_valor_transmision_otros": "…",
    "1637_valor_adquisicion_otros": "…",
    "0588_deduccion_doble_imposicion": "…"
  },
  "resumen": { "ganancia_neta": "…", "perdidas_bloqueadas_antichurning": "…", "perdidas_reintegradas_antichurning": "…",
               "ganancia_neta_fx": "…", "num_operaciones": 0, "num_operaciones_fx": 0, "num_dividendos": 0 },
  "doble_imposicion_por_pais": { "DE": { "impuesto_pagado": "…", "deduccion_permitida": "…" } },
  "operaciones": [ { "isin": "…", "simbolo": "…", "fecha_venta": "AAAAMMDD", "fecha_compra": "AAAAMMDD", "cantidad": "…",
                     "importe_venta_eur": "…", "coste_eur": "…", "ganancia_eur": "…", "dias_tenencia": 0,
                     "divisa": "…", "tipo_ecb_compra": "…", "tipo_ecb_venta": "…", "bloqueada_antichurning": false } ],
  "operaciones_fx": [ /* disposiciones de divisa */ ],
  "dividendos": [ { "isin": "…", "simbolo": "…", "fecha": "AAAA-MM-DD", "bruto_eur": "…", "retencion_eur": "…", "pais": "DE" } ]
}
```

- Los importes son **cadenas con 2 decimales**. El adaptador los convierte a `Decimal`, nunca a `float`.
- Todas las claves de `casillas` se tratan como opacas y se guardan tal cual. El mapeo a número de casilla y a concepto está en `fiscalidad-inversiones.md` §6.
- **Claves de primer nivel [VERIFICADO con la CLI real el 2026-09-23]:** `year`, `casillas`, `resumen`, `doble_imposicion_por_pais`, `operaciones`, `operaciones_fx` y `dividendos`. Salida completa grabada en `tests/fixtures/declarenta/canonico_basico_2024.json`.
- **Formatos de fecha distintos:** `operaciones` usa `AAAAMMDD` y `dividendos` usa `AAAA-MM-DD`. El adaptador normaliza las dos a `date`.
- **La CLI funciona sin red si todas las operaciones están en EUR** (no pide tipos al BCE). Con otras divisas necesita acceso a `data-api.ecb.europa.eu`.
- [PENDIENTE T-F1.7] Formato de los avisos (`messages`) en la salida de la CLI con extractos reales en divisa y con pérdidas bloqueadas.

## 3. Flex XML canónico: el formato de intercambio que genera Cartera Clara

Toda operación que no venga de un fichero que DeclaRenta ya entiende (importador IA, operaciones manuales, conversiones) se exporta a un **Flex XML canónico**: un subconjunto del Flex Query de IBKR que acepta el parser `ibkr` de DeclaRenta. **Probado el 2026-09-23** con `tests/fixtures/flex/canonico_basico.xml`, que da una ganancia de 78,60 € y una deducción DDI de 1,50 €.

```xml
<FlexQueryResponse queryName="cartera-clara" type="AF">
  <FlexStatements count="1">
    <FlexStatement accountId="CC-<broker>" fromDate="AAAAMMDD" toDate="AAAAMMDD" period="Custom">
      <Trades>
        <Trade tradeID="…" accountId="…" symbol="…" description="…" isin="…" assetCategory="STK"
               currency="EUR" tradeDate="AAAAMMDD" quantity="10" tradePrice="100"
               buySell="BUY" openCloseIndicator="O" ibCommission="-1" ibCommissionCurrency="EUR" taxes="0"/>
      </Trades>
      <CashTransactions>
        <CashTransaction transactionID="…" accountId="…" symbol="…" description="… Cash Dividend" isin="…"
                         currency="EUR" dateTime="AAAAMMDD" amount="10.00" type="Dividends"/>
        <CashTransaction transactionID="…" accountId="…" symbol="…" description="… DE Tax" isin="…"
                         currency="EUR" dateTime="AAAAMMDD" amount="-2.64" type="Withholding Tax"/>
      </CashTransactions>
      <CorporateActions/><OpenPositions/><SecuritiesInfo/>
    </FlexStatement>
  </FlexStatements>
</FlexQueryResponse>
```

Reglas del exportador (obligatorias, verificadas en `src/parsers/ibkr.ts` y `src/engine/dividends.ts`):

| Campo | Regla |
|---|---|
| Comisión | Atributos **`ibCommission`** (negativa) e **`ibCommissionCurrency`**. El parser **ignora** `commission` y `commissionCurrency`, que son los que usa la fixture `ibkr-sample.xml` de DeclaRenta. |
| Venta | `quantity` negativa, `buySell="SELL"`, `openCloseIndicator="C"`. |
| Compra | `quantity` positiva, `buySell="BUY"`, `openCloseIndicator="O"`. |
| Fechas | `AAAAMMDD` en `tradeDate` y `dateTime`. |
| Tipos de `CashTransaction` admitidos | `Dividends`, `Payment In Lieu Of Dividends`, `Withholding Tax`, `Broker Interest Paid`, `Broker Interest Received`, `Bond Interest Paid`, `Bond Interest Received`, `Other Fees`, `Commission Adjustments`, `Deposits/Withdrawals` (hay más en `src/types/ibkr.ts`). |
| País de la retención | Lo deduce DeclaRenta: primero un código de 2 letras seguido de «Tax» o «WHT» en `description` (p. ej. `"ACME DE Tax"`) y, si no, el prefijo del ISIN. **El exportador escribe siempre `"<símbolo> <PAÍS> Tax"`** para no depender del ISIN. |
| `assetCategory` | `STK` para acciones y ETF en v1. |
| Atributos no necesarios | `fxRateToBase`, `proceeds`, `cost` y `fifoPnlRealized` no se escriben: DeclaRenta recalcula con el BCE. |

## 4. Comportamientos de DeclaRenta que hay que conocer

- **Doble imposición:** la deducción de cada país es el mínimo entre lo retenido y el tipo del convenio por el bruto, y además no puede superar el impuesto español sobre esa renta. En el código, `TREATY_DIVIDEND_RATES` solo define `US = 15 %`, y **cualquier otro país usa un 15 % por defecto** (`src/engine/double-taxation.ts`) [VERIFICADO]. DeclaRenta **no calcula el exceso reclamable** en origen: lo hace Cartera Clara (§8.6 del diseño).
- **Regla de los 2 meses:** el bloqueo es proporcional a la cantidad recomprada. La reintegración de la pérdida solo es automática si se procesan todos los años en una sola ejecución (`docs/casillas.md` de DeclaRenta).
- **Tipos de cambio:** los diarios del BCE; en fines de semana y festivos, el día hábil anterior.

## 5. Cómo se prueba sin red ni Node

- **CI:** el adaptador (`motores/declarenta/`) se prueba con salidas JSON **grabadas** en `tests/fixtures/declarenta/*.json`, inyectando un ejecutor falso que devuelve esas salidas.
- **En local:** `make declarenta && make test-declarenta` ejecuta los tests `@pytest.mark.declarenta` contra la CLI real y compara con lo grabado.
- **Grabar salidas nuevas:** con `uv run cartera-clara motor declarenta --grabar <fixture>` (T-F1.7). Cada grabación deja constancia del commit de DeclaRenta y de la fecha.
