# Regulación 2026-2027 que crea demanda forzada de software/IA en empresas españolas

Estado a 23 septiembre 2026. Nota metodológica: varias fuentes primarias (sede AEAT, BOE en algunos casos, Gibson Dunn, b2brouter) estaban bloqueadas por el proxy de red; muchos datos proceden de snippets de buscador de blogs de consultoras/proveedores y prensa. Se marca [SNIPPET] cuando el dato no se pudo verificar leyendo la página completa. Los aplazamientos se marcan con **APLAZADO**.

## Ranking resumido (urgencia × amplitud × gap de tooling)

| # | Norma | Fecha clave | Amplitud (empresas) | Gap de tooling | Nota |
|---|---|---|---|---|---|
| 1 | VeriFactu (RD 1007/2023) + Factura electrónica B2B (RD 238/2026) — tratarlas como un único "stack fiscal" | 1 ene 2027 (IS) / 1 jul 2027 (resto) VeriFactu; 1 oct 2027 (>8M€) / 1 oct 2028 (resto) B2B (borrador OM) | ~2,5M pymes + ~2,1M autónomos | Medio: el software ERP se adapta, pero la adopción real es mínima y hay enorme cola de micro/autónomos con Excel/Word | Máxima amplitud y fecha cierta; mercado muy competido en "software de facturación", menos en migración/conciliación/estados de pago |
| 2 | Registro horario digital (RD pendiente) | Aprobación "inmediata" anunciada 9 sep 2026; no publicado aún | Todas las empresas con asalariados | Medio-alto: exige API a Inspección, inalterabilidad; muchas pymes con papel/Excel | Alta amplitud, fecha incierta, riesgo político |
| 3 | EU AI Act — Art. 50 transparencia (2 ago 2026, ya aplicable) + inventario IA, alto riesgo aplazado a dic 2027 | 2 ago 2026 (Art. 50), 2 dic 2026 (marcado de agua 50(2)), 2 dic 2027 (Anexo III) | Toda empresa que despliegue chatbots/contenido generado; alto riesgo = subconjunto (RRHH, crédito, etc.) | Alto en pymes: pocas herramientas de inventario/gobernanza IA asequibles en español | Demanda de "AI governance lite" |
| 4 | Accesibilidad (EAA / Ley 11/2023) | Aplicable desde 28 jun 2025 | Webs/apps/e-commerce de empresas no-micro que ofrecen servicios del ámbito | Alto: 98% webs privadas no cumplen | Enforcement español aún débil |
| 5 | NIS2 (Ley Coordinación y Gobernanza Ciberseguridad) + CRA (reporting 11 sep 2026) + DORA | NIS2: ley aún en Congreso; CRA reporting ya vigente; DORA vigente desde ene 2025 | Miles de entidades esenciales/importantes; fabricantes de productos digitales; sector financiero | Medio: GRC existe pero caro; gap en pymes proveedoras y en reporting CRA | NIS2 = demanda latente que se activará con BOE |
| 6 | Canal de denuncias (Ley 2/2023) | AIPI operativa desde sep 2025; comunicación RSII hasta 10 abr 2026 | Empresas ≥50 trabajadores | Bajo-medio: mercado maduro de canales SaaS | Oportunidad en gestión/triage con IA, no en el canal |
| 7 | ESG: CSRD tras Ómnibus I, VSME, EUDR, CBAM | EUDR 30 dic 2026 (grandes/medianas), 30 jun 2027 (micro/pequeñas); CBAM definitivo desde 1 ene 2026, 1ª declaración anual 30 sep 2027; CSRD ejercicios desde 2027 solo >1000 empl. y >450M€ | CSRD directo: pocas (~5.000 en UE); indirecto (cuestionarios cadena suministro): muchas pymes | Alto para pymes proveedoras (VSME, cuestionarios); EUDR: diligencia de geolocalización | Nicho sectorial (agro, madera, café, cacao, caucho, acero/aluminio import.) |
| — | Jornada 37,5h | Rechazada en Congreso 10 sep 2025; no vigente | — | — | No es driver en 2026-27 salvo vía reglamentaria |

---

## 1. VeriFactu / Reglamento de sistemas informáticos de facturación (RD 1007/2023)

### Takeaway
**APLAZADO** otra vez (segundo aplazamiento) por el RDL 15/2025: sujetos al Impuesto sobre Sociedades antes del 1 ene 2027; resto (autónomos) antes del 1 jul 2027. Afecta a ~4,6M obligados y la adopción real en sept 2026 es residual (1,75% según prensa), lo que crea un pico de demanda concentrado en el S1 2027.

### Cited Findings
- RDL 15/2025, de 2 de diciembre (BOE 3 dic 2025) amplía plazos: contribuyentes del IS deben tener adaptados sus sistemas antes del 1 ene 2027; resto de obligados antes del 1 jul 2027 — [Noticias Jurídicas](https://noticias.juridicas.com/actualidad/noticias/20735-nueva-prorroga:-verifactu-no-sera-obligatorio-hasta-2027-para-sociedades-y-otros-contribuyentes/); [ICAM](https://web.icam.es/se-retrasa-al-2027-la-entrada-en-vigor-de-verifactu-la-nueva-normativa-de-facturacion-electronica/); [Nota informativa AEAT](https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu/nota-informativa-ampliacion-plazo-adaptacion-facturacion.html) (no se pudo abrir, bloqueada).
- Fechas anteriores: 1 ene 2026 (IS) y 1 jul 2026 (resto); justificación del aplazamiento: complejidad técnica e implantación homogénea — [fiscal-impuestos.com](https://www.fiscal-impuestos.com/aplazamiento-entrada-vigor-Verifactu-2027) [SNIPPET]
- Amplitud: con el calendario original afectaba a "casi 2,5 millones de pymes" (1 ene) y "2,1 millones de autónomos" (1 jul) — [Euronews](https://es.euronews.com/2026/04/10/el-aplazamiento-de-verifactu-genera-incertidumbre-en-pymes-y-autonomos-en-espana) [SNIPPET]
- Preparación: 38% de empresas sin plan definido y 24% sin saber cómo abordarlo (≈6 de cada 10 lejos de estar listos) — encuesta TeamSystem vía [MuyPymes](https://www.muypymes.com/2025/10/30/pymes-adaptacion-verifactu) / [ChannelPartner](https://www.channelpartner.es/fabricantes/el-62-de-las-pymes-siguen-sin-tener-un-plan-de-adaptacion-a-verifactu-segun-teamsystem/)
- "Ocho de cada diez autónomos aún no se han adaptado a VeriFactu; solo el 7% cumple plenamente" (ene 2026) — [Autónomos y Emprendedor](https://www.autonomosyemprendedor.es/articulo/autonomos/ocho-cada-diez-autonomos-aun-han-adaptado-verifactu-solo-7-cumple-plenamente-ley/20260122144822051340.html) [titular]
- Solo el 1,75% de empresas y autónomos usan VeriFactu (13 sep 2026), aunque el volumen de registros remitidos ha crecido — [The Objective](https://theobjective.com/economia/2026-09-13/verifactu-fracasa-175-empresas-autonomos-usan/) [SNIPPET; medio con línea editorial crítica con el Gobierno]
- Barreras: 4 de cada 10 autónomos citan coste; 3 de cada 10 pymes falta de formación — [Euronews](https://es.euronews.com/2026/04/10/el-aplazamiento-de-verifactu-genera-incertidumbre-en-pymes-y-autonomos-en-espana) [SNIPPET]

### Inferences
- Pico de demanda: Q4 2026–Q2 2027. Las sociedades (≈1,5–2,5M) tienen el deadline más cercano (3 meses).
- El producto "software de facturación VeriFactu" está comoditizado (Holded, Quipu, Sage, A3, Billin, Contasimple…, y la app gratuita de la AEAT). El gap no está en emitir el QR/hash, sino en: (a) migrar facturación hecha en Excel/Word o en ERPs verticales obsoletos; (b) integrar TPVs/verticales sectoriales; (c) auditar que el software declarado cumple (declaración responsable del productor); (d) asesorías/gestorías que deben migrar cientos de clientes a la vez.
- Agente IA 10x: "agente de migración" para gestorías que ingiere facturas históricas (PDF/Excel), mapea clientes/series, configura el software destino y valida los registros; y agente de soporte de primer nivel para autónomos.
- Riesgo: un tercer aplazamiento no se puede descartar dado el historial (dos ya), pero no hay evidencia en sept 2026.

### Gaps
- No se pudo verificar el número oficial de obligados ni el régimen sancionador exacto (se cita habitualmente hasta 50.000 € por ejercicio para usuarios de software no conforme y 150.000 € para productores, art. 201 bis LGT) — no verificado en esta sesión.
- No hay datos fiables de cuota de mercado de software VeriFactu.

## 2. Factura electrónica B2B obligatoria (Ley Crea y Crece, RD 238/2026)

### Takeaway
El reglamento ya está aprobado: RD 238/2026 de 25 de marzo (BOE 31 mar 2026). El borrador de Orden Ministerial fija **1 oct 2027 (facturación >8M€)** y **1 oct 2028 (resto)**; la consulta pública cerró el 8 may 2026 y la OM no consta publicada. Obliga además a comunicar estados de pago en 4 días, lo que es un nuevo flujo de datos (cobros/pagos) que casi ninguna pyme gestiona hoy de forma estructurada.

### Cited Findings
- Real Decreto 238/2026, de 25 de marzo, desarrolla el sistema de facturación electrónica obligatoria entre empresarios y profesionales y modifica el RD 1619/2012 — [BOE-A-2026-7295](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7295); [AEAT noticia 31 mar 2026](https://sede.agenciatributaria.gob.es/Sede/todas-noticias/2026/marzo/31/facturacion-electronica-obligatoria.html) (bloqueada)
- Borrador OM: 1 oct 2027 para empresas con facturación >8M€ y 1 oct 2028 para el resto; fechas definitivas dependen de la publicación de la OM en BOE; consulta pública terminó 8 may 2026 — [Docuten](https://docuten.com/es/blog/la-factura-electronica-b2b-ya-tiene-fecha-lo-que-tienes-que-saber-del-borrador-de-la-orden-ministerial/) [SNIPPET]
- Factura electrónica = fichero estructurado de lectura automatizada; plazo máximo de 4 días naturales (excl. sábados, domingos y festivos nacionales) para comunicar estados de las facturas — [Iberley](https://www.iberley.es/noticias/publicado-boe-rd-factura-electronica-obligatoria-b2b-36274) / [búsqueda] [SNIPPET]
- Formatos: EN 16931 en sintaxis CII, UBL, EDIFACT o Facturae; los usuarios de la solución pública deben usar UBL — [Iberley revista](https://www.iberley.es/revista/factura-electronica-obligatoria-b2b-claves-nuevo-sistema-1532) / [Cuatrecasas](https://www.cuatrecasas.com/es/spain/fiscalidad/art/operaciones-b2b-facturacion-electronica-obligatoria) [SNIPPET]
- La AEAT desarrolla y gestiona una solución pública gratuita que actúa como repositorio universal obligatorio de todas las facturas; incluirá app/formulario gratuito para emitir, informar estados y pagos — mismas fuentes [SNIPPET]
- Conflicto: algunas fuentes (p.ej. [B2Brouter](https://www.b2brouter.net/es/plazos-obligatoriedad-factura-electronica-b2b/)) mezclan fechas de VeriFactu (ene/jul 2027) con las de B2B; la fecha B2B correcta según borrador OM es oct 2027/oct 2028.

### Inferences
- Solapamiento VeriFactu (ene–jul 2027) + B2B (oct 2027) = 9 meses de doble cambio para grandes pymes. Oportunidad de "stack único": una herramienta que cubra VeriFactu + e-factura UBL + estados de pago.
- Gap real: la **recepción** (ingestar facturas UBL/Facturae de proveedores, conciliar con pedidos/albaranes y contabilizar) y la **comunicación de estado de pago en 4 días** (requiere conectar banca/tesorería). Los proveedores actuales (Edicom, Docuten, B2Brouter, Seres, Pagero, Sovos) están orientados a grandes; las micro usarán la solución pública gratuita de AEAT, que limita el mercado de emisión puro.
- Agente IA 10x: conciliación automática factura-pedido-pago y emisión automática de estados; clasificación contable de facturas recibidas; detección de discrepancias.

### Gaps
- OM definitiva no verificada como publicada (a 23 sep 2026).
- Régimen sancionador específico B2B no confirmado en esta sesión.
- Número de empresas >8M€ (orden de decenas de miles) no verificado.

## 3. Registro horario digital obligatorio y jornada de 37,5h

### Takeaway
Registro horario digital: el RD sigue **sin publicarse** a septiembre 2026 tras un dictamen desfavorable del Consejo de Estado (23 mar 2026) y un **aplazamiento a septiembre** pactado por Trabajo y Economía (24 jul 2026); Yolanda Díaz anunció el 9 sep 2026 que se aprobará "de inmediato". Jornada de 37,5h: **rechazada** en el Congreso (10 sep 2025), no vigente.

### Cited Findings
- 30 sep 2025: Consejo de Ministros aprueba tramitación urgente de un RD independiente de registro horario digital, separado de la reducción de jornada — [Mi Fichaje Legal](https://mifichajelegal.com/blog/real-decreto-registro-horario-digital-mayo-2026-estado-tramitacion-pymes/) [SNIPPET]
- 23 mar 2026: dictamen muy crítico del Consejo de Estado: insuficiente justificación de cargas, plazo de adaptación de 20 días naturales "manifiestamente insuficiente", algunas obligaciones requerirían rango de ley, reservas sobre protección de datos — [Mi Fichaje Legal](https://mifichajelegal.com/blog/dictamen-consejo-estado-registro-horario-digital-pymes-que-pasa-ahora/); [Copilot Gestoría](https://copilotgestoria.com/blog/consejo-estado-rechaza-registro-horario-digital-2026-que-significa-empresas-gestorias) [SNIPPET]
- 24 jul 2026: Economía y Trabajo pactan llevar el registro horario a septiembre para salvar objeciones del Consejo de Estado — [elDiario.es](https://www.eldiario.es/economia/economia-trabajo-pactan-llevar-registro-horario-septiembre-salvar-objeciones-consejo_1_13403321.html)
- 9 sep 2026: Díaz anuncia aprobación "inmediata" tras acuerdo con Economía y PSOE; a esa fecha no ha pasado por Consejo de Ministros ni BOE — [registrahora.es](https://www.registrahora.es/noticias/registro-horario-digital-aplazado-septiembre-2026) / [fichme](https://fichme.com/normativa/fichaje-digital-obligatorio) [SNIPPET]
- Contenido del borrador: sistemas deben poder enviar datos a la Inspección de Trabajo vía API REST estandarizada (inicio, fin, pausas, identificación, lugar); solo digital (prohíbe papel/Excel), registros inalterables, acceso remoto de la Inspección, sanciones de hasta 10.000 € por trabajador afectado — [controlhorario.com](https://controlhorario.com/ley-registro-horario/) (bloqueada, dato vía snippet; proveedor interesado). Nota: la sanción "por trabajador" procede de la reforma de LISOS asociada al proyecto de 37,5h, cuyo estado es incierto.
- 37,5h: Congreso rechazó la ley el 10 sep 2025 por enmiendas a la totalidad de PP, Vox y Junts; jornada máxima sigue 40h; Trabajo ha sugerido vía reglamentaria; desde abril 2026 220.000–250.000 funcionarios AGE a 35h — [Turijobs](https://www.turijobs.com/es-es/blog/jornada-laboral-de-37-5-horas-ley-y-consecuencias-para-los-trabajadores-2026/); [Securex](https://securexrrhh.com/jornada-de-375-horas-en-2026-esta-en-vigor/); [Noticias de Álava](https://www.noticiasdealava.eus/economia/2026/05/24/reforma-laboral-sindicatos-patronal-ministerio-de-trabajo-gobierno-vasco-11110417.html) ("la gran promesa que se cae de la agenda")

### Inferences
- Amplitud: todas las empresas con asalariados (del orden de 1,3–1,4M empleadoras; no verificado). Mercado de fichaje saturado (Factorial, Sesame, Woffu, Kenjo, Endalia, a3, cientos de apps), pero el requisito de API a Inspección y la inalterabilidad obligarán a re-certificar/migrar.
- Oportunidad IA 10x no en el fichaje sino en: detección de anomalías/horas extra, conciliación con nómina y convenio colectivo (hay >4.000 convenios), respuesta a requerimientos de Inspección, y cumplimiento de desconexión digital.
- Si el Consejo de Estado prevalece, el plazo de adaptación será mayor que 20 días (probablemente meses), con lo que el pico de demanda caería en 2027.

### Gaps
- Texto final del RD y plazo de adaptación desconocidos (no publicado).
- Cifra exacta de sanciones vigente (LISOS actual: 751–7.500 € por infracción grave) vs propuesta — no verificada en esta sesión.

## 4. EU AI Act: AI literacy (Art. 4), transparencia (Art. 50), Digital Omnibus, AESIA

### Takeaway
El Digital Omnibus on AI (Reglamento (UE) 2026/1744, DOUE 24 jul 2026, en vigor 27 jul 2026) **aplazó** alto riesgo Anexo III a 2 dic 2027 y Anexo I a 2 ago 2028, y **rebajó el Art. 4** (alfabetización) de obligación empresarial a deber de fomento de Comisión/Estados. El **Art. 50 NO se aplazó**: transparencia aplicable desde 2 ago 2026; marcado de agua (50(2)) 2 dic 2026.

### Cited Findings
- Reglamento (UE) 2026/1744 publicado 24 jul 2026, en vigor 27 jul 2026 — [Usercentrics](https://usercentrics.com/knowledge-hub/eu-ai-act-high-risk-delay-article-50-transparency-consent/); [Comisión Europea](https://digital-strategy.ec.europa.eu/en/news/ai-omnibus-enters-force)
- Alto riesgo Anexo III: de 2 ago 2026 a 2 dic 2027; Anexo I (productos): 2 ago 2028 — [CSA Labs](https://labs.cloudsecurityalliance.org/research/csa-research-note-eu-ai-act-omnibus-vii-deadline-delay-20260/); [Gibson Dunn](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/)
- Art. 50 no aplazado, aplica desde 2 ago 2026; watermarking 50(2) 2 dic 2026 — [aiactblog.nl](https://www.aiactblog.nl/en/posts/article-50-transparency-deadline-2-august-2026); [Usercentrics](https://usercentrics.com/knowledge-hub/eu-ai-act-high-risk-delay-article-50-transparency-consent/)
- Art. 4 reescrito: proveedores y responsables del despliegue ya no están obligados a garantizar un nivel suficiente de alfabetización; pasa a obligación de la Comisión y Estados de fomentarla, con atención a pymes; "no exige garantizar ningún nivel específico" — [lawandtechnology.eu](https://lawandtechnology.eu/en/ai-literacy-digital-omnibus-article-4-ai-act/); [casys.ai](https://casys.ai/blog/digital-omnibus-article-4-what-changed)
- Simplificaciones pyme extendidas a "small mid-caps" — [artificialintelligenceact.eu](https://artificialintelligenceact.eu/ai-act-explorer/digital-omnibus/) [SNIPPET]

### Inferences
- La demanda de "formación obligatoria en IA" (Art. 4) pierde el argumento de obligatoriedad — oportunidad degradada.
- Demanda real a corto plazo: (a) Art. 50 — avisos en chatbots, etiquetado de contenido sintético/deepfakes, marcado de agua antes del 2 dic 2026; (b) preparación Anexo III para dic 2027 en usos de RRHH (cribado de CVs), scoring crediticio, seguros — inventario de sistemas IA, clasificación de riesgo, FRIA, logs, supervisión humana.
- Gap en pymes: herramientas de AI governance (Credo AI, Holistic AI, OneTrust AI Gov, Trail) son caras y en inglés; hueco para "inventario + clasificador de riesgo + generador de documentación" en español, asequible, con agente que descubra uso de IA (shadow AI) vía SaaS/facturas.
- AESIA (A Coruña) es la autoridad española; España tramitaba un anteproyecto de ley de buen uso y gobernanza de IA con régimen sancionador — estado no verificado.

### Gaps
- Estado del anteproyecto español de ley de IA y del sandbox de AESIA (convocatorias 2025-2026) — no investigado por límite de llamadas.
- Número de empresas españolas que usan IA (INE) — no verificado.

## 5. Ciberseguridad: NIS2 (España), DORA, Cyber Resilience Act

### Takeaway
NIS2 en España sigue **sin transponer**: el anteproyecto de Ley de Coordinación y Gobernanza de la Ciberseguridad (CM 14 ene 2025) sigue en el Congreso a mediados de 2026, con dictamen motivado de la Comisión (mayo 2025). CRA: obligaciones de notificación de vulnerabilidades explotadas e incidentes graves **aplicables desde 11 sep 2026** vía la Single Reporting Platform de ENISA. DORA aplicable desde 17 ene 2025; 19 CTPP designados en nov 2025.

### Cited Findings
- Anteproyecto aprobado por CM el 14 ene 2025; a jul 2026 no publicado en BOE; en junio 2026 seguía en el Congreso — [angelortegacastro.com](https://angelortegacastro.com/ley-coordinacion-gobernanza-ciberseguridad-nis2-estado-boe/); [Legiscope](https://www.legiscope.com/blog/nis2-espana-transposicion.html) [SNIPPET]; ficha oficial [DSN](https://www.dsn.gob.es/en/node/24160)
- España incumplió el plazo de transposición (17 oct 2024); dictamen motivado de la Comisión en mayo 2025; sanciones de hasta 10M€; crea el Centro Nacional de Ciberseguridad como autoridad única — mismas fuentes [SNIPPET]
- CRA: desde 11 sep 2026 los fabricantes deben notificar vulnerabilidades activamente explotadas e incidentes graves a ENISA y al CSIRT: alerta temprana 24h, notificación 72h, informe final 14 días tras la corrección (vulnerabilidades) o 1 mes (incidentes); ENISA lanzó la SRP — [ENISA](https://www.enisa.europa.eu/news/the-cra-single-reporting-platform-is-launched); [Comisión](https://digital-strategy.ec.europa.eu/en/policies/cra-reporting); [Hogan Lovells](https://www.hlc.com/en/publications/eu-cyber-resilience-act-vulnerability-and-incident-reporting-obligations-now-apply)
- DORA: 18 nov 2025 las ESAs designaron 19 proveedores TIC críticos; se espera intensificación de la supervisión del Registro de Información en el ciclo 2026 — [EBA](https://www.eba.europa.eu/publications-and-media/press-releases/european-supervisory-authorities-designate-critical-ict-third-party-providers-under-digital); [Morgan Lewis](https://www.morganlewis.com/blogs/sourcingatmorganlewis/2025/11/dora-eu-regulators-announce-list-of-critical-ict-third-party-providers); [Orbiq](https://www.orbiqhq.com/eu-regulations/dora-compliance) [SNIPPET]

### Inferences
- NIS2: demanda latente (muchas empresas medianas en 18 sectores serán "importantes"); se disparará con la publicación en BOE, probablemente con plazos cortos de registro. Además, efecto cascada: grandes clientes NIS2/DORA ya exigen cuestionarios de seguridad a proveedores pyme — hueco para agente que rellene cuestionarios de seguridad (tipo Vanta/Drata trust center, pero asequible y en español) y mapee a ENS (Esquema Nacional de Seguridad), muy usado en España.
- CRA: afecta a fabricantes de software/hardware con elementos digitales (incluidas startups SaaS con producto distribuido); gap en procesos de PSIRT, SBOM y gestión de vulnerabilidades en pymes; plena aplicación del CRA 11 dic 2027 (dato de conocimiento previo, no verificado aquí).
- DORA: mercado cubierto por GRC grandes; hueco en proveedores TIC pyme de entidades financieras que deben aceptar cláusulas contractuales DORA.

### Gaps
- Número de entidades españolas afectadas por NIS2 (estimaciones varían) — no verificado.
- Fecha probable de aprobación de la ley NIS2 — sin fuente fiable.

## 6. ESG: CSRD tras Ómnibus I, VSME, CSDDD, EUDR, CBAM

### Takeaway
Ómnibus I (Directiva (UE) 2026/470, DOUE 26 feb 2026, en vigor 18 mar 2026) reduce CSRD a empresas >1.000 empleados y >450M€ (≈5.000 en UE, de ~50.000), transposición antes del 19 mar 2027. La demanda en pymes pasa a ser **indirecta** (cuestionarios de clientes, estándar voluntario VSME). EUDR: **aplazado** a 30 dic 2026 (grandes/medianas) y 30 jun 2027 (micro/pequeñas), Comisión dice que no habrá más aplazamientos. CBAM definitivo desde 1 ene 2026 con umbral de 50 t.

### Cited Findings
- Directiva (UE) 2026/470 publicada 26 feb 2026, en vigor 18 mar 2026; CSRD solo >1.000 empleados y >450M€; de ~50.000 a ~5.000 empresas; transposición antes de 19 mar 2027 — [Cuatrecasas](https://www.cuatrecasas.com/es/spain/sostenibilidad/art/directiva-omnibus-i); [RocaJunyent](https://www.rocajunyent.com/en/node/1917); [Corresponsables](https://www.corresponsables.com/actualidad/ue-aprueba-directiva-omnibus-eleva-umbrales-reporte/) [SNIPPET]
- Estándares voluntarios (VSME) para empresas <1.000 empleados previstos en unos cuatro meses — [búsqueda, ESG Innova / Manglai](https://www.manglai.io/blog/omnibus-esg-2026) [SNIPPET]; el "value chain cap" limita lo que grandes pueden pedir a pymes (conocimiento previo, no verificado aquí)
- EUDR: aplicación 30 dic 2026 para operadores grandes y medianos; micro y pequeños hasta 30 jun 2027; declaración simplificada única para micro/pequeños primarios; libros/periódicos fuera de alcance — [Consejo UE](https://www.consilium.europa.eu/en/press/press-releases/2025/12/18/deforestation-council-signs-off-targeted-revision-to-simplify-and-postpone-the-regulation/); [CMS](https://cms.law/en/deu/legal-updates/eu-resets-the-countdown-on-the-eudr-and-postpones-the-regulation-once-again)
- 4 may 2026: Comisión publica paquete de simplificación EUDR (informe, guía/FAQ, borrador de acto delegado sobre alcance, acto de ejecución del sistema de información) y confirma que no habrá nuevo aplazamiento — [Hogan Lovells](https://www.hoganlovells.com/en/publications/eu-deforestation-regulation-commission-publishes-simplification-package-ahead-of-december-2026); [Food Ingredients First](https://www.foodingredientsfirst.com/news/eudr-delay-april-review-uncertainty.html) [SNIPPET]
- CBAM: régimen definitivo desde 1 ene 2026; umbral de 50 t/año (excepto electricidad e hidrógeno); por encima se requiere ser declarante CBAM autorizado; solicitudes antes del 31 mar 2026 permiten seguir importando; declaración anual el 30 sep del año siguiente (primera: 30 sep 2027) — [Comisión, CBAM](https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism/cbam-definitive-regime_en); [EY](https://www.ey.com/en_gl/technical/tax-alerts/eu-adopts-cbam-omnibus-regulation)

### Inferences
- CSRD dejó de ser mercado pyme directo; la demanda restante es: (a) pymes proveedoras respondiendo cuestionarios ESG/huella de carbono de grandes clientes (EcoVadis, CDP) — agente que rellene cuestionarios a partir de facturas de energía y datos contables es un 10x; (b) informe VSME voluntario para acceso a financiación bancaria.
- EUDR: nicho con fecha dura 30 dic 2026; en España afecta a importadores/transformadores de café, cacao, soja, aceite de palma, madera/muebles/papel, caucho, ganado/cuero. Gap: recopilación de geolocalización de parcelas de proveedores y due diligence statements en TRACES; agente IA para análisis de documentos de proveedores y chequeo satelital.
- CBAM: afecta a importadores de acero, aluminio, cemento, fertilizantes, hidrógeno >50 t; primer año de compra de certificados; gap en obtención de emisiones reales de proveedores extracomunitarios.
- CSDDD: aplazada y restringida por Ómnibus (grandes >5.000 empleados según acuerdo; no verificado aquí) — irrelevante para pymes salvo cascada.

### Gaps
- Número de empresas españolas bajo CSRD tras Ómnibus y estado de transposición española (la Ley de información empresarial sobre sostenibilidad) — no verificado.
- Umbrales finales de CSDDD — no verificados en esta sesión.

## 7. Accesibilidad (European Accessibility Act / Ley 11/2023)

### Takeaway
Aplicable desde 28 jun 2025 a webs, apps y e-commerce de servicios en alcance (microempresas de servicios exentas); el 98% de las webs privadas españolas no cumple. Sanciones en España de hasta 1M€ vía RDL 1/2013, pero enforcement todavía poco visible.

### Cited Findings
- EAA aplicable desde 28 jun 2025; Ley 11/2023 transpone la Directiva (UE) 2019/882 — [CEDDD](https://ceddd.org/actualidad/acta-europea-de-la-accesibilidad-que-cambia-a-partir-del-28-de-junio/); [Tech4Access](https://tech4access.com/ley-112023/)
- Sanciones: régimen del RDL 1/2013, leves/graves/muy graves, hasta 1.000.000 €; también se citan 301–90.000 € — [Product Hackers](https://producthackers.com/es/blog/european-accessibility-act/) [SNIPPET]; posible inconsistencia entre rangos citados.
- Barómetro de Accesibilidad Web 2025: 98% de webs del sector privado no cumple; solo 2% cumple plenamente — [búsqueda: theetailers / daas-group](https://www.daas-group.com/blog/european-accessibility-act/) [SNIPPET]
- Balance "un año después" de sanciones y empresas afectadas — [Inforges](https://inforges.es/blog/european-accessibility-act/) [no leído]

### Inferences
- Gran gap de cumplimiento; tooling existente = auditores automáticos (axe, WAVE), overlays (accessiBe, UserWay; criticados por no cumplir) y consultoras. Un agente IA que audite y **genere los fixes de código** (alt text, ARIA, contraste, formularios) y la declaración de accesibilidad es un 10x plausible.
- Urgencia moderada hasta que haya sanciones visibles o demandas colectivas (asociaciones de discapacidad en España son activas).

### Gaps
- Autoridad sancionadora concreta y primeras sanciones en España — no verificadas.

## 8. Canal de denuncias (Ley 2/2023) y GDPR

### Takeaway
Obligatorio para empresas ≥50 trabajadores; la AIPI opera desde sept 2025 y desde feb 2026 habilitó el formulario de comunicación del Responsable del Sistema (plazo 10 abr 2026); multas de hasta 1M€. Mercado de canales ya maduro.

### Cited Findings
- AIPI creada por RD 1101/2024; supervisa canales y cumplimiento de Ley 2/2023 — [Edorteam](https://edorteam.com/autoridad-independiente-proteccion-informante-aipi-cumplimiento-canales-denuncias/)
- Obligatorio desde 50 trabajadores; sanciones hasta 1M€; AIPI operativa desde septiembre 2025 — [Luis Marín Economistas](https://www.luismarineconomistas.com/canal-denuncias-empresas-obligacion-ley-2-2023/); [LawAndTrends](https://www.lawandtrends.com/noticias/penal/tienes-canal-de-denuncias-la-autoridad-independiente-de-proteccion-al-informante-aai-ya-puede-sancionarte-1.html)
- Desde 10 feb 2026 formulario para comunicar el RSII; plazo hasta 10 abr 2026; "la Inspección activa el control del canal de denuncias y ya puede sancionar a las pymes con un millón de euros" — [Autónomos y Emprendedor](https://www.autonomosyemprendedor.es/articulo/pymes/inspeccion-activa-control-canal-denuncias-puede-sancionar-pymes-millon-euros/20260213165904051950.html) [SNIPPET]

### Inferences
- Oferta saturada (Whistleblower Software, EQS, Globaleaks, soluciones de despachos y asesorías). Gap marginal: triage, investigación y redacción de informes con IA dentro de plazos legales (acuse 7 días, resolución 3 meses) — mejora incremental, no 10x. Muy bajo en ranking.
- GDPR: no hay nueva obligación 2026-27 destacable en España en esta búsqueda; la cuestión GDPR aparece como límite transversal (p.ej. Consejo de Estado sobre fichaje; datos en IA).

### Gaps
- Número de empresas ≥50 trabajadores en España (orden ~30.000) — no verificado.

## Síntesis: dónde un agente IA ofrece 10x

### Takeaway
Las mejores oportunidades combinan fecha dura, millones de afectados y un trabajo de "última milla" (migración, conciliación, cuestionarios, documentación) que el software existente no resuelve: el stack fiscal VeriFactu + e-factura B2B para gestorías/pymes es el #1; registro horario (si se publica) y AI Act Art. 50/Anexo III para pymes le siguen.

### Cited Findings
- Ver secciones anteriores (todas las cifras y fechas citadas allí).

### Inferences
- **#1 Agente para gestorías/asesorías (VeriFactu + e-factura B2B + estados de pago):** el canal de distribución a millones de micro-empresas son ~decenas de miles de gestorías; automatizar migración, validación y conciliación multi-cliente. Ventana: ahora–oct 2028.
- **#2 Agente de cumplimiento laboral (registro horario + convenios):** esperar al texto del RD; construir sobre fichajes existentes (integraciones) en vez de competir en fichaje.
- **#3 "AI governance lite" en español:** inventario de IA, clasificación de riesgo, textos Art. 50, documentación Anexo III para usos de RRHH; venta a medianas empresas y consultoras.
- **#4 Accesibilidad auto-remediación** para e-commerce (Shopify/WooCommerce/PrestaShop).
- **#5 Agente de cuestionarios de proveedores** (seguridad NIS2/DORA/ENS + ESG/VSME/huella): un mismo motor RAG sobre la documentación de la pyme responde ambos tipos de cuestionario.
- **Nicho vertical:** EUDR (30 dic 2026) y CBAM (1ª declaración 30 sep 2027) para importadores concretos.
- Descartar/relegar: formación obligatoria en IA (Art. 4 rebajado), jornada 37,5h (sin ley), canal de denuncias (mercado maduro), CSRD directa en pymes (fuera de alcance).

### Gaps
- Tamaño de mercado cuantificado (gasto por empresa, precios de competidores) no investigado.
- Riesgo de nuevos aplazamientos (VeriFactu ya aplazado dos veces; registro horario bloqueado) — sin fuentes predictivas fiables.
