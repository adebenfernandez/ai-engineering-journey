# Referencia: feed ATOM/CODICE de PLACSP

Estado de cada dato:
- **[VERIFICADO]**: visto en una entrada real del feed, la fixture `tests/fixtures/codice/entry_publicada_oviedo_2026.xml` (15/08/2026).
- **[CONFIRMADO EN CÓDIGO PÚBLICO]**: lo usan parsers de terceros que leen el feed real, pero no aparece en nuestra fixture.
- **[PENDIENTE S1]**: lo confirma o descarta el spike S1.

**Regla para Claude Code:** si necesitas un campo que no está en esta tabla, no lo supongas. Añádelo a «Preguntas abiertas» en `docs/01-riesgos-y-verificaciones.md` y búscalo en una entrada real guardada por S1.

## 1. Fuentes

| Fuente | URL | Notas |
|---|---|---|
| Licitaciones de perfiles del contratante en PLACSP, sin contratos menores (sindicación 643), por mes | `https://contrataciondelsectorpublico.gob.es/sindicacion/sindicacion_643/licitacionesPerfilesContratanteCompleto3_AAAAMM.zip` | ZIP con varios `.atom` encadenados. Es la fuente principal de Baremo. [CONFIRMADO EN CÓDIGO PÚBLICO] |
| La misma, por año cerrado | `.../licitacionesPerfilesContratanteCompleto3_AAAA.zip` | Para años anteriores al actual. [CONFIRMADO EN CÓDIGO PÚBLICO] |
| La misma, feed vivo | `.../sindicacion_643/licitacionesPerfilesContratanteCompleto3.atom` | Paginado con `<link rel="next">`. Sirve para la actualización diaria. [PENDIENTE S1] |
| Contratos menores (sindicación 1143) y plataformas autonómicas agregadas (sindicación 1044) | mismo dominio | **Fuera de alcance en v1.** |

Dominios que deben estar permitidos en la red donde se ejecute la ingesta: `contrataciondelsectorpublico.gob.es` y `contrataciondelestado.es` (este último para los PDF de pliegos y las codelists).

## 2. Espacios de nombres

```python
NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "cac": "urn:dgpe:names:draft:codice:schema:xsd:CommonAggregateComponents-2",
    "cbc": "urn:dgpe:names:draft:codice:schema:xsd:CommonBasicComponents-2",
    "cac-place-ext": "urn:dgpe:names:draft:codice-place-ext:schema:xsd:CommonAggregateComponents-2",
    "cbc-place-ext": "urn:dgpe:names:draft:codice-place-ext:schema:xsd:CommonBasicComponents-2",
}
```

Las fixtures reales usan prefijos distintos (`ns0`, `ns1`…). Hay que parsear **siempre por URI de espacio de nombres**, nunca por prefijo.

## 3. Campos por entrada (`atom:entry`)

Rutas relativas a `entry`. `CFS` = `cac-place-ext:ContractFolderStatus`.

| Campo Baremo | Ruta | Estado |
|---|---|---|
| `id_entrada` | `atom:id` | VERIFICADO |
| `url_detalle` | `atom:link/@href` | VERIFICADO |
| `titulo` | `atom:title` | VERIFICADO |
| `actualizado_en` | `atom:updated` (ISO 8601 con zona) | VERIFICADO |
| `expediente` | `CFS/cbc:ContractFolderID` | VERIFICADO |
| `estado_code` | `CFS/cbc-place-ext:ContractFolderStatusCode` (p. ej. `PUB`, `ADJ`) | VERIFICADO |
| `organo_nombre` | `CFS/cac-place-ext:LocatedContractingParty/cac:Party/cac:PartyName/cbc:Name` | VERIFICADO |
| `organo_nif` | `…/cac:Party/cac:PartyIdentification/cbc:ID[@schemeName="NIF"]` | VERIFICADO |
| `organo_dir3` | `…/cac:Party/cac:PartyIdentification/cbc:ID[@schemeName="DIR3"]` | VERIFICADO |
| `organo_id_plataforma` | `…/cac:Party/cac:PartyIdentification/cbc:ID[@schemeName="ID_PLATAFORMA"]` | VERIFICADO |
| `organo_tipo_code` | `CFS/cac-place-ext:LocatedContractingParty/cbc:ContractingPartyTypeCode` | VERIFICADO |
| `organo_actividad_code` | `CFS/cac-place-ext:LocatedContractingParty/cbc:ActivityCode` | VERIFICADO |
| `organo_jerarquia` | cadena de `cac-place-ext:ParentLocatedParty/cac:PartyName/cbc:Name`, de dentro a fuera, unida con ` > ` | VERIFICADO |
| `tipo_contrato_code` | `CFS/cac:ProcurementProject/cbc:TypeCode` | VERIFICADO |
| `subtipo_contrato_code` | `CFS/cac:ProcurementProject/cbc:SubTypeCode` | VERIFICADO |
| `valor_estimado` | `CFS/cac:ProcurementProject/cac:BudgetAmount/cbc:EstimatedOverallContractAmount` | VERIFICADO |
| `presupuesto_con_iva` | `…/cac:BudgetAmount/cbc:TotalAmount` | VERIFICADO |
| `presupuesto_sin_iva` | `…/cac:BudgetAmount/cbc:TaxExclusiveAmount` | VERIFICADO |
| `cpvs` | todos los `CFS/cac:ProcurementProject/cac:RequiredCommodityClassification/cbc:ItemClassificationCode`; el primero es `cpv_principal` | VERIFICADO |
| `nuts` | `CFS/cac:ProcurementProject/cac:RealizedLocation/cbc:CountrySubentityCode` | VERIFICADO |
| `duracion_valor`, `duracion_unidad` | `…/cac:PlannedPeriod/cbc:DurationMeasure` y su `@unitCode` (`DAY`, `MON`, `ANN`) | VERIFICADO (`DAY`); resto PENDIENTE S1 |
| `procedimiento_code` | `CFS/cac:TenderingProcess/cbc:ProcedureCode` | VERIFICADO |
| `urgencia_code` | `CFS/cac:TenderingProcess/cbc:UrgencyCode` | VERIFICADO |
| `sistema_contratacion_code` | `CFS/cac:TenderingProcess/cbc:ContractingSystemCode` | VERIFICADO |
| `presentacion_lotes_code` | `CFS/cac:TenderingProcess/cbc:PartPresentationCode` | VERIFICADO |
| `sara` | `CFS/cac:TenderingProcess/cbc:OverThresholdIndicator` (`true`/`false`) | VERIFICADO |
| `fecha_limite_ofertas`, `hora_limite_ofertas` | `CFS/cac:TenderingProcess/cac:TenderSubmissionDeadlinePeriod/cbc:EndDate` y `/cbc:EndTime` | VERIFICADO |
| `financiacion_ue_code` | `CFS/cac:TenderingTerms/cbc:FundingProgramCode` | VERIFICADO |
| `garantia_tipo_code`, `garantia_pct` | `CFS/cac:TenderingTerms/cac:RequiredFinancialGuarantee/cbc:GuaranteeTypeCode` y `/cbc:AmountRate`. Puede haber varias. | VERIFICADO |
| `solvencia_feed` (texto) | `CFS/cac:TenderingTerms/cac:TendererQualificationRequest/*/cbc:Description` | VERIFICADO. Suele ser genérico, p. ej. «Se aportará según el modelo de la plantilla que se anexa». **No sirve para decidir**; la fuente es el pliego. |
| `fecha_publicacion` | la menor `CFS/cac-place-ext:ValidNoticeInfo/cac-place-ext:AdditionalPublicationStatus/cac-place-ext:AdditionalPublicationDocumentReference/cbc:IssueDate` | VERIFICADO |
| `tipos_anuncio` | `CFS/cac-place-ext:ValidNoticeInfo/cbc-place-ext:NoticeTypeCode` (p. ej. `DOC_CN`, `DOC_CD`) | VERIFICADO |

## 4. Lotes y criterios

| Campo | Ruta | Estado |
|---|---|---|
| `lote_id` | `CFS/cac:ProcurementProjectLot/cbc:ID[@schemeName="ID_LOTE"]` | VERIFICADO |
| `lote_nombre` | `…/cac:ProcurementProjectLot/cac:ProcurementProject/cbc:Name` | VERIFICADO |
| `lote_presupuesto_sin_iva` / `_con_iva` | `…/cac:ProcurementProjectLot/cac:ProcurementProject/cac:BudgetAmount/cbc:TaxExclusiveAmount` / `cbc:TotalAmount` | VERIFICADO |
| `lote_cpvs` | `…/cac:ProcurementProjectLot/cac:ProcurementProject/cac:RequiredCommodityClassification/cbc:ItemClassificationCode` | VERIFICADO |
| criterios del lote | `…/cac:ProcurementProjectLot/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriteria` | VERIFICADO |
| criterios comunes | `CFS/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriteria` | VERIFICADO |
| `criterio_tipo` | `cbc:AwardingCriteriaTypeCode`: `OBJ` (evaluable con fórmula) o `SUBJ` (juicio de valor) | VERIFICADO |
| `criterio_subtipo_code` | `cbc:AwardingCriteriaSubTypeCode`. Su codelist depende del tipo: `AwardingCriteriaAutomaticallyEvaluatedSubTypeCode` o `…NotAutomatically…`. En la fixture, `OBJ` con subtipo `1` es «Oferta económica». El significado se lee de la codelist (S3). | VERIFICADO (valores); significado PENDIENTE S3 |
| `criterio_descripcion` | `cbc:Description` | VERIFICADO |
| `criterio_peso` | `cbc:WeightNumeric` | VERIFICADO |

**Reglas de negocio (obligatorias):**

1. **Licitación sin lotes.** Si no hay ningún `ProcurementProjectLot`, se crea un lote sintético con `lote_id = "0"`, cuyo presupuesto y CPV son los de la licitación. Así todas las consultas trabajan por lote.
2. **Criterios de un lote** = los criterios del propio lote **más** los comunes (`CFS/cac:TenderingTerms`). Los comunes se guardan con `lote_id = "*"`.
3. **Validación de pesos.** Si la suma de pesos de un lote no es 100 (tolerancia ±0,5), el lote se marca `pesos_incompletos = true` y no se usa el peso del feed para decidir. **Caso real en la fixture:** en el lote 6, 74 (OBJ) + 6 (común) = 80. Falta el juicio de valor, que probablemente comparte con el lote 2 («Oferta económica lotes 2 y 6»). Ante un conflicto, manda lo que se extraiga del pliego (§8.4 del diseño).
4. La suma de los presupuestos de los lotes debe coincidir con el presupuesto sin IVA de la licitación (en la fixture, 82.210 € = 82.210 €). Si no coincide, se registra un aviso en el log y no se corrige nada.

## 5. Documentos

| Documento | Ruta | Estado |
|---|---|---|
| PCAP (pliego administrativo) | `CFS/cac:LegalDocumentReference` → `cbc:ID` (nombre de fichero), `cac:Attachment/cac:ExternalReference/cbc:URI`, `…/cbc:DocumentHash` | VERIFICADO |
| PPT (pliego técnico) | `CFS/cac:TechnicalDocumentReference` (misma estructura) | VERIFICADO |
| Otros (memoria, certificados…) | `CFS/cac:AdditionalDocumentReference` (misma estructura) | VERIFICADO |
| Documentos generales | `CFS/cac-place-ext:GeneralDocument/cac-place-ext:GeneralDocumentDocumentReference` (con `cbc:FileName`) | CONFIRMADO EN CÓDIGO PÚBLICO |

Las URI de descarga tienen la forma `https://contrataciondelestado.es/FileSystem/servlet/GetDocumentByIdServlet?cifrado=…&DocumentIdParam=…`. En el XML, el `&` viene escapado como `&amp;`; el parser de XML lo desescapa. El proyecto Compass (MIT) descarga y analiza PCAP reales desde estas URI. El porcentaje de licitaciones con PCAP lo mide S1, y el de PDF legibles, S2.

## 6. Resultado de la adjudicación (`cac:TenderResult`)

Puede haber varios por entrada, normalmente uno por lote.

| Campo | Ruta (relativa a `CFS/cac:TenderResult`) | Estado |
|---|---|---|
| `resultado_code` | `cbc:ResultCode` (su significado se lee de la codelist, S3) | CONFIRMADO EN CÓDIGO PÚBLICO |
| `fecha_adjudicacion` | `cbc:AwardDate` | CONFIRMADO EN CÓDIGO PÚBLICO |
| `n_ofertas` | `cbc:ReceivedTenderQuantity` | CONFIRMADO EN CÓDIGO PÚBLICO |
| `oferta_min` | `cbc:LowerTenderAmount` («Precio de la oferta más baja» en OpenPLACSP) | CONFIRMADO en la documentación de OpenPLACSP; cobertura PENDIENTE S1 |
| `oferta_max` | `cbc:HigherTenderAmount` («Precio de la oferta más alta») | ídem |
| `adjudicatario_pyme` | `cbc:SMEAwardedIndicator` | CONFIRMADO EN CÓDIGO PÚBLICO |
| `adjudicatario_nombre` | `cac:WinningParty/cac:PartyName/cbc:Name` | CONFIRMADO EN CÓDIGO PÚBLICO |
| `adjudicatario_nif` | `cac:WinningParty/cac:PartyIdentification/cbc:ID` | CONFIRMADO EN CÓDIGO PÚBLICO |
| `importe_adjudicacion_sin_iva` | `cac:AwardedTenderedProject/cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount` | CONFIRMADO EN CÓDIGO PÚBLICO |
| `importe_adjudicacion_con_iva` | `cac:AwardedTenderedProject/cac:LegalMonetaryTotal/cbc:PayableAmount` | CONFIRMADO EN CÓDIGO PÚBLICO |
| `lote_id` del resultado | `cac:AwardedTenderedProject/cbc:ProcurementProjectLotID` | **PENDIENTE S1**. Si no existe ahí, S1 guarda ejemplos reales para localizarlo. |

**Lo que el feed NO trae:** la oferta de cada licitador. Solo el número de ofertas, la más baja, la más alta y la adjudicada. Por eso el diseño predice la **baja mínima** y la **baja adjudicada** (§8.5 del diseño), no la oferta de cada competidor.

## 7. Borrados

Si un fichero ATOM contiene elementos `{http://purl.org/atompub/tombstones/1.0}deleted-entry` con atributo `ref`, la entrada con ese `id_entrada` se marca `anulada = true`; no se borra. PENDIENTE S1: confirmar si PLACSP los emite.

## 8. Codelists

Cada código lleva un `@listURI` que apunta a su lista oficial en formato Genericode (p. ej. `https://contrataciondelestado.es/codice/cl/2.08/ContractCode-2.08.gc`). El spike S3 las descarga a `docs/referencias/codelists/*.json` con la forma `{código: nombre}`. **El código nunca asume el significado de un número:** usa esas tablas. Así, la etiqueta «Suministros» para `TypeCode=1` sale del JSON, no del código.
