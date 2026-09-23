# Riesgos, verificaciones y decisiones

Actualizado el **2026-09-23**. Estados:
- **CERRADO**: verificado con datos.
- **MITIGADO**: resuelto en el diseño; falta medirlo.
- **ABIERTO**.

## 1. Lo ya verificado el 2026-09-23

| Qué | Cómo | Resultado |
|---|---|---|
| Competencia | Búsqueda en la web y en GitHub; se leyeron el README y el ROADMAP de DeclaRenta, y MiCartera por resultados de búsqueda | DeclaRenta (GPL, gratis, 13 brókeres, sin IA), MiCartera (de pago) y AceleraFiscal ya calculan. **Ninguna tiene IA, conciliación con la AEAT, recuperador de retenciones ni doble motor.** |
| DeclaRenta funciona como motor | Se clonó el commit `3f88031`, se compiló con `tsup` y se ejecutó la **CLI real** `convert -f json` | Funciona. Salida grabada en `tests/fixtures/declarenta/`. Solo necesita red hacia el BCE si hay divisas distintas del EUR. |
| Formato de intercambio | Flex XML canónico generado a mano y procesado por DeclaRenta | Ganancia 78,60 € y DDI de Alemania 1,50 de 2,64 retenidos: **coincide con el cálculo a mano**. |
| Trampa de las comisiones | Lectura de `src/parsers/ibkr.ts` | El parser lee `ibCommission`, no `commission`. Documentado. |
| Límite del convenio | Lectura de `src/engine/double-taxation.ts` | Solo EE. UU. tiene un 15 % explícito; el resto usa un 15 % por defecto. No calcula el exceso reclamable (nuestro hueco). |
| Formatos de Trade Republic y Degiro | Cabeceras de las fixtures de DeclaRenta | Documentados en `referencias/formatos-brokers.md`. |
| Librerías | PyPI e inspección del SDK instalado | `anthropic` 1.8 (parse y fallbacks), `mcp` 2.2 (`MCPServer`), `chromadb` 1.5. |

## 2. Riesgos

| ID | Riesgo | Estado | Mitigación / siguiente paso |
|---|---|---|---|
| **R1** | Alguien ya hace esto con IA | MITIGADO | No se encontró ninguno. Repetir la búsqueda antes del lanzamiento (T-F8.1). Aunque apareciera uno, el doble motor y el enfoque local y open source siguen siendo diferenciales. |
| **R2** | Un error fiscal perjudica a una persona real | MITIGADO | Doble motor con discrepancias visibles, «la IA nunca calcula», borradores para revisar, descargo, tests con las reglas legales y casos publicados para que asesores los revisen. |
| **R3** | Dependencia de DeclaRenta: cambia el formato, se abandona o cambia la licencia | MITIGADO | Commit fijado, salidas grabadas, adaptador aislado y motor propio en la F7 para los casos principales. |
| **R4** | Formato de los datos fiscales de la AEAT desconocido | **ABIERTO** | T-F0.2: el usuario descarga su PDF y se describe su estructura. Si no se puede extraer bien, el conciliador pasa a entrada manual de los importes del borrador. |
| **R5** | Casillas renumeradas en la Renta 2026 | ABIERTO | T-F0.4 (en abril de 2027, cuando se publique el manual): se actualiza `casillas_2026.json`. Nunca van en el código. |
| **R6** | Sin red a PLACSP, BCE, sheetjs, AEAT… en el entorno cloud de Claude Code | ABIERTO | Los tests nunca usan red. `make declarenta` y los spikes se ejecutan en tu PC. Opcional: permitir `data-api.ecb.europa.eu`, `cdn.sheetjs.com` y `github.com` en *Environment → Network access*. |
| **R7** | Coste de la IA | MITIGADO | Caché de prompt, registro de coste por llamada y S4 para medir. El cálculo no necesita IA. |
| **R8** | Privacidad: el usuario manda datos financieros a una API | MITIGADO | Local-first. Aviso y consentimiento por documento. No se guardan NIF ni IBAN. Demo sin ficheros reales. |
| **R9** | Legal: parecer asesoramiento de inversión | MITIGADO | ADR 0004 y evaluación de rechazo al 100 %. |
| **R10** | Estacionalidad: nadie mira la Renta en verano | ACEPTADO | Se lanza en abril. El MCP y el recuperador de retenciones tienen uso todo el año. |
| **R11** | Inyección de prompt en los PDF | MITIGADO | Extracción sin herramientas y asistente solo con herramientas de lectura locales (§7.6 del diseño). |
| **R12** | Datos de convenios incorrectos | MITIGADO | `convenios.json` solo con países verificados en el BOE, con fuente. El resto: «sin datos». |

## 3. Spikes de la F0

Se ejecutan en tu PC. Las instrucciones están en `spikes/README.md`.

| Spike | Qué responde | Regla de decisión |
|---|---|---|
| **S1**: DeclaRenta en local | ¿`make declarenta` funciona en tu máquina? ¿Qué devuelve con tus extractos reales? ¿Cuadra con tu Renta del año pasado? | Si no compila: usar la imagen Docker `drumsergio/declarenta` (está PENDIENTE comprobar que existe y qué etiqueta tiene) y actualizar el ADR 0002. |
| **S2**: tus datos fiscales AEAT | ¿Qué estructura tiene el PDF? ¿Se lee el texto con pypdf? | Si tiene capa de texto: el conciliador con IA sigue como está diseñado. Si no: extracción con visión y, como plan B, entrada manual. |
| **S3**: informe fiscal de Trade Republic y un extracto no soportado | ¿Qué secciones tienen? ¿Traen totales para el cuadre? | Si no hay totales: el cuadre se hace contra la suma de la columna y se marca la operación para revisión obligatoria. |
| **S4**: coste en tokens | Tokens por documento con `count_tokens` (sin generar) | Si supera 0,50 USD por documento con Opus 5: evaluar Sonnet 5 en la evaluación de F3 (ADR 0005). |
| **S5**: competencia a mano | Probar DeclaRenta web, MiCartera y AceleraFiscal con los mismos extractos; leer r/SpainFIRE | Anotar qué hace cada una. Si alguna ya concilia con la AEAT o calcula el exceso reclamable, replantear el diferencial antes de la F4. |

## 4. Resultados de los spikes

_Pendiente._

| Spike | Fecha | Resultado | Decisión |
|---|---|---|---|
| S1 | | | |
| S2 | | | |
| S3 | | | |
| S4 | | | |
| S5 | | | |

## 5. Preguntas abiertas

| # | Pregunta | Quién | Estado |
|---|---|---|---|
| P1 | Estructura del PDF de datos fiscales de la AEAT | S2 | Abierta |
| P2 | Valores de `category`/`type` de Trade Republic para compras y ventas | S1 / código de DeclaRenta | Abierta |
| P3 | Límites de los convenios y formularios de reclamación de DE, CH, FR, NL e IE | T-F6.1 (BOE y webs oficiales) | Abierta |
| P4 | Formato de los avisos del JSON de `declarenta convert` con divisas y pérdidas bloqueadas (las claves de primer nivel ya están verificadas) | T-F1.7 | Abierta |
| P5 | Consultas DGT V2422-20 y V0583-16 (criterio de divisas) | T-F7.0 | Abierta |
| P6 | Fecha de inicio de la campaña de la Renta 2026 | Abril de 2027 | Abierta |
| P7 | ¿Existe la imagen Docker `drumsergio/declarenta` y con qué etiquetas? | S1 | Abierta |
