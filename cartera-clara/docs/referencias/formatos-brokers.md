# Referencia: formatos de los extractos de los brókeres

Hay dos consumidores:
- **DeclaRenta**, que lee 13 formatos. En esos formatos **no se reimplementa nada**: el fichero del usuario se le pasa tal cual.
- El **motor propio** (F7), que lee los formatos de v1 con los parsers de `importadores/`.

## 1. Formatos del motor propio en v1

### 1.1 Trade Republic: CSV «Actividad» [VERIFICADO en la fixture de DeclaRenta]

Separador `,`, todos los campos entre comillas, decimales con punto.

```
datetime, date, account_type, category, type, asset_class, name, symbol, shares, price, amount, fee, tax,
currency, original_amount, original_currency, fx_rate, description, transaction_id, counterparty_name,
counterparty_iban, payment_reference, mcc_code
```

- `symbol` contiene el **ISIN**. En la fixture, `category` vale `CASH` o `CORPORATE_ACTION` y `type` vale `INTEREST_PAYMENT`, `DIVIDEND` o `MERGER`.
- `counterparty_iban` puede traer datos personales. El parser **no los guarda** en el libro.
- [PENDIENTE T-F0.2] La lista completa de valores de `category` y `type` para compras y ventas. Se saca de un export real tuyo (se anonimiza antes de guardarlo como fixture) o del parser de DeclaRenta `src/parsers/trade-republic.ts`.
- Otra vía para conseguir los datos: [pytr](https://github.com/pytr-org/pytr), que exporta `account_transactions.csv` a través de la API privada de Trade Republic. **No se usa en v1**, porque es una API no oficial y requiere credenciales.

### 1.2 Degiro: CSV «Transacciones» [VERIFICADO en la fixture]

Cabecera en español, 19 columnas, con columnas sin nombre para la divisa:

```
Fecha,Hora,Producto,ISIN,Bolsa de,Centro de ejecución,Número,Precio,,Valor local,,Valor,,Tipo de cambio,Costes de transacción,,Total,,ID Orden
```

- `Fecha` va en formato `DD-MM-AAAA`. `Número` es positivo en las compras y negativo en las ventas. La columna que sigue a `Precio` es la divisa del precio.
- DeclaRenta detecta el separador (coma o punto y coma).

### 1.3 Degiro: CSV «Estado de cuenta» [VERIFICADO en la fixture]

```
Fecha,Hora,Fecha valor,Producto,ISIN,Descripción,Tipo,Variación,,Saldo,,ID Orden
```

Contiene los dividendos, las retenciones, las comisiones y los movimientos de efectivo. La descripción está en texto libre.

### 1.4 Interactive Brokers: Flex Query XML [VERIFICADO]

Ver `declarenta-integracion.md` §3. Ojo con `ibCommission` frente a `commission`.

## 2. Documentos que solo lee el importador con IA (F3)

| Documento | Formato | Estado |
|---|---|---|
| Informe fiscal anual de Trade Republic | PDF | PENDIENTE T-F0.3: conseguir uno real, anonimizarlo y describir sus secciones |
| Extractos de brókeres no soportados (p. ej. MyInvestor, bancos españoles) | PDF o CSV | PENDIENTE: el usuario aporta ejemplos |
| **Datos fiscales de la AEAT** (Renta Web → «Datos fiscales») | PDF | PENDIENTE T-F0.2: conseguir el tuyo y describir su estructura. Es la entrada del conciliador (§8.5 del diseño). |

**Regla:** ningún documento real entra en el repositorio. Las fixtures de estos formatos se **reescriben a mano** con datos ficticios, conservando la estructura.
