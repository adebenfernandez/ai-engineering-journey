# Riesgos, verificaciones y decisiones

Actualizado: **2026-09-23**. Cada riesgo tiene un estado:
- **CERRADO**: verificado con datos.
- **MITIGADO**: resuelto en el diseño; falta medirlo.
- **ABIERTO**.

Cuando un spike termine, pega su resumen en la sección «Resultados de los spikes» y aplica la regla de decisión correspondiente.

## 1. Tabla de riesgos

| ID | Riesgo | Estado | Evidencia a 2026-09-23 | Qué falta / regla |
|---|---|---|---|---|
| **R1** | Los feeds de PLACSP no enlazan de forma fiable a los PDF de los pliegos | **CERRADO** (existencia) / MITIGADO (cobertura) | En una entrada real del 15/08/2026, `LegalDocumentReference` (PCAP) y `TechnicalDocumentReference` (PPT) traen la URI `GetDocumentByIdServlet` y el `DocumentHash`. Compass (MIT) descarga y analiza PCAP reales con esas URI. | S1 mide el **% de licitaciones con PCAP**. Regla D1. |
| **R2** | El feed no publica las ofertas de todos los licitadores, así que no hay con qué evaluar la recomendación de baja | **MITIGADO** (diseño adaptado) | El feed **no** trae cada oferta. **Sí** trae, por resultado: nº de ofertas (`ReceivedTenderQuantity`), oferta más baja y más alta (`LowerTenderAmount` / `HigherTenderAmount`, columnas «Precio de la oferta más baja/alta» de OpenPLACSP), importe adjudicado y si el adjudicatario es pyme. El diseño (§8.5) predice la **baja mínima** y la **baja adjudicada**, que son medibles. | S1 mide la cobertura de cada campo. Regla D2. |
| **R3** | Pliegos escaneados sin capa de texto | **MITIGADO** | Se detectan con una media de menos de 20 caracteres por página (umbral de Compass). Claude lee el PDF de forma nativa, por visión, y lo transcribe (§8.4.2). Las citas de esos pliegos se marcan `VERIFICACION_VISUAL`. Límites del API: 32 MB y 600 páginas por petición; por encima se trocea. | S2 mide el **% de escaneados** y el tamaño de los PDF. Regla D3. |
| **R4** | Competencia: otro proyecto ya hace lo mismo | **CERRADO** (reposicionado) | **Compass** (github.com/alan-fdez/Compass, MIT, último commit el 23/09/2026) ya resuelve el radar y el «¿puedo presentarme?» con citas. Tendios se centra en grandes empresas. Se reposiciona Baremo hacia la **estrategia de oferta**: fórmula de puntos, temeridad, baja recomendada con backtest y borradores. Ver §3 del diseño. | Revisar Compass y Tendios cada mes, por si cambian de alcance. |
| **R5** | Interpretar mal los códigos de CODICE (ResultCode, TypeCode, subtipos de criterio…) | **MITIGADO** | Todo código tiene `@listURI`. S3 descarga las listas oficiales y el código lee sus significados de ellas (`ingesta/codelists.py`). | Ejecutar S3. Si `TenderResultCode` da 404, buscar su URL correcta. |
| **R6** | Coste de extracción inasumible | **MITIGADO** | Estimación: unos 60.000 tokens por pliego, que son unos 0,30 USD de entrada con Opus 5. La caché de prompt y la Batch API (−50 %) lo reducen. | S4 mide los tokens reales. Regla D4. |
| **R7** | Error con consecuencias legales: solvencia mal calculada o temeridad mal interpretada, que llevan a una oferta excluida | **MITIGADO** | «El modelo extrae; el código decide». 15 casos legales verificados con una implementación independiente. Las dos interpretaciones de «unidades porcentuales» se implementan y se muestran (ADR 0005). Descargo visible. Baremo nunca presenta nada. | Contrastar el art. 85 con el BOE consolidado antes de cerrar la F2. |
| **R8** | Sin acceso de red a PLACSP desde el entorno de desarrollo | **ABIERTO** | Desde el entorno cloud de Claude Code, `contrataciondelestado.es`, `contrataciondelsectorpublico.gob.es`, `boe.es` y `hacienda.gob.es` devuelven **403 en el proxy de salida**. GitHub y PyPI sí son accesibles. | Opción A: ejecutar la ingesta y los spikes en tu PC. Opción B: en claude.ai/code, *Environment → Edit → Network access*, añadir esos dominios a la lista de permitidos. Los tests nunca usan red (§7.3 del diseño). |
| **R9** | Bloqueo o carga excesiva sobre PLACSP | **MITIGADO** | Pausa de 2 s entre descargas de PDF, `User-Agent` identificable, caché por hash y ZIP mensuales en vez de miles de peticiones. | — |
| **R10** | Inyección de prompt a través del texto de un pliego | **MITIGADO** | Las llamadas que leen pliegos no tienen herramientas, ni red, ni ficheros; su salida es un esquema cerrado. El servidor MCP es de solo lectura. §7.5 del diseño. | ADR 0007 en la F3. |
| **R11** | AI Act (art. 50) y RGPD | **MITIGADO** | Aviso de uso de IA en la interfaz y en los DOCX. NIF guardados con hash. No se muestran nombres de personas físicas. | — |
| **R12** | Pocos datos comparables para algunos CPV u órganos | **MITIGADO** | Se recurre a medianas por `cpv2` (B1) y a la global (B0). La interfaz muestra `n_comparables`, y si es menor que 30 avisa de «poca evidencia». | — |
| **R13** | Cambios de formato en PLACSP (codelists 2.xx, rutas de sindicación) | ABIERTO | Las codelists llevan versión en la URL (2.04 a 2.11 en la misma entrada). | Tests con fixtures reales de meses distintos. Si falla un XPath, se guarda la entrada nueva como fixture. |

## 2. Reglas de decisión (se aplican con los resultados de los spikes)

| ID | Métrica (spike) | Umbral → decisión |
|---|---|---|
| **D1** | % de entradas con PCAP (S1) | ≥ 70 %: flujo A tal cual. Entre 40 % y 70 %: la ficha avisa de «sin pliego» y el recomendador funciona igual (no necesita el pliego). < 40 %: también se aceptan PDF subidos a mano por el usuario (nueva tarea en F6). |
| **D2** | % de `TenderResult` con `LowerTenderAmount` (S1) | ≥ 50 %: se predicen `baja_minima` y `baja_adjudicada`. Entre 20 % y 50 %: ambas, pero el backtest de `baja_minima` solo sobre los que la tienen, y se indica. < 20 %: solo `baja_adjudicada` y `n_ofertas`; el umbral de temeridad estimado usa la dispersión histórica de `baja_adjudicada` en lugar de la mínima y la máxima. |
| **D2b** | Ubicación del `lote_id` en `TenderResult` (S1, ejemplos guardados) | Si está en `AwardedTenderedProject/ProcurementProjectLotID`, se usa tal cual. Si no, se busca en los ejemplos reales, se documenta en `referencias/codice-placsp.md` y se cambia el parser. |
| **D3** | % de PCAP escaneados (S2) | ≤ 15 %: transcripción con LLM como está diseñada. > 15 %: el golden set debe incluir al menos 5 escaneados y se mide el coste extra. En ningún caso se usa OCR local. |
| **D4** | Mediana de tokens por pliego (S4) | Si el coste medio de extraer con Opus 5 supera 0,50 USD por pliego: evaluar Sonnet 5 en el golden set y, si la precisión cae 2 puntos o menos, cambiar `modelo_extraccion` (ADR 0004). |

## 3. Cómo ejecutar los spikes

Todo se ejecuta desde `baremo/`, con red que llegue a PLACSP (ver R8).

```bash
uv sync
make spikes-s1 MES=202605     # descarga el ZIP de mayo de 2026 (el último mes completo con adjudicaciones)
make spikes-s2 MES=202605     # 40 PCAP al azar de ese ZIP
make spikes-s3 MES=202605     # codelists a docs/referencias/codelists/
export ANTHROPIC_API_KEY=...  # solo para S4
make spikes-s4                # tokens por pliego (sin generar texto)
```

Después:
1. Copia los JSON de resumen de `spikes/resultados/` a `docs/resultados/spikes_<fecha>.md`.
2. Rellena la sección 4.
3. Aplica D1-D4.
4. Sustituye la fixture sintética de adjudicación por una real de `spikes/resultados/s1_ejemplos/` (tarea S1-c).

## 4. Resultados de los spikes

_Pendiente de ejecutar. No se puede desde el entorno de desarrollo en la nube (R8)._

| Spike | Fecha | Resultado clave | Decisión aplicada |
|---|---|---|---|
| S1 | | | |
| S2 | | | |
| S3 | | | |
| S4 | | | |

## 5. Preguntas abiertas

Añade aquí cualquier dato que necesites y no esté en la documentación. **No lo supongas.**

| # | Pregunta | Quién la resuelve | Estado |
|---|---|---|---|
| P1 | ¿Qué códigos de `TenderResultCode` equivalen a «adjudicado» y «formalizado»? | S3 | Abierta |
| P2 | ¿Qué `AwardingCriteriaSubTypeCode` identifica el criterio «precio»? En la fixture, `OBJ` con subtipo `1` se describe como «Oferta económica». | S3 | Abierta |
| P3 | ¿Qué `ContractingSystemCode` corresponde a un contrato normal frente a un acuerdo marco o un sistema dinámico? | S3 | Abierta |
| P4 | ¿Emite PLACSP elementos `deleted-entry`? | S1 (buscar en los XML) | Abierta |
| P5 | Texto exacto del art. 85 RGLCAP en el BOE consolidado | Tú, en la F2 (T-F2.0) | Abierta |
