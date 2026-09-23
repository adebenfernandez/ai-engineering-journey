# Fixtures de test

**Regla absoluta:** aquí nunca va un extracto real de nadie. Solo datos ficticios o anonimizados a mano (ISIN `XX…`, importes redondos, sin NIF ni IBAN).

| Fichero | Origen | Uso |
|---|---|---|
| `flex/canonico_basico.xml` | **Creado para este proyecto** (2026-09-23). Flex XML canónico: compra de 10 a 100 €, venta de 4 a 120 € (comisión 1 € cada una), dividendo alemán de 10 € con retención de 2,64 €. | Contrato del exportador (T-F1.5) y del adaptador de DeclaRenta. |
| `flex/canonico_basico.esperado.json` | Salida **real** de DeclaRenta (commit `3f88031`, v0.58.24) sobre el fichero anterior, con tipo EUR = 1, ejecutada el 2026-09-23. | Oráculo: ganancia 78,60 €; deducción DDI 1,50 €; exceso reclamable a Alemania 1,14 €. |
| `brokers/trade-republic-sample.csv` | Copiado de [DeclaRenta](https://github.com/GeiserX/DeclaRenta) `tests/fixtures/` (GPL-3.0; datos ficticios según su README). | Formato real de columnas del CSV de Trade Republic. |
| `brokers/degiro-transactions-sample.csv`, `brokers/degiro-account-sample.csv` | Ídem. | Formato de Degiro (transacciones y cuenta). |
| `brokers/ibkr-sample.xml` | Ídem. | Formato Flex Query de IBKR. **Ojo:** usa el atributo `commission`, pero el parser de DeclaRenta lee `ibCommission`; por eso en ese fichero las comisiones no cuentan. Nuestro Flex canónico usa `ibCommission`. |
| `declarenta/canonico_basico_2024.json` | Salida **real** de `node dist/cli.js convert -i tests/fixtures/flex/canonico_basico.xml -y 2024 -f json` con DeclaRenta en el commit `3f88031`, grabada el 2026-09-23. | Tests del adaptador (T-F1.8) sin Node ni red. Las demás salidas grabadas se añaden en T-F1.7. |
