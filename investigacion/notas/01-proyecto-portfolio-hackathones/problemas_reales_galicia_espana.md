# Unsolved problems in Galicia and Spain (2025-2026) that software and AI could address

Research date: 2026-09-23. Method: about 22 web searches (the fetch tool was blocked for elcorreogallego.es, so some figures come from search-result snippets of news articles, not from the full text). Figures marked "(snippet)" should be checked against the full article before anyone quotes them publicly. Several pages on "existing solutions" come from general knowledge and not from a searched source. These are labelled as inferences and are not cited.

## Agriculture / rural: minifundio, land abandonment, Banco de Terras, PAC paperwork, vineyard disease

### Takeaway
Galicia's main structural problem is fragmented land. There are about 11 million rural parcels and 1.7 million owners of rustic land, but only about 44,000 primary-sector workers. About 512,000 ha of productive farmland is abandoned. The main barrier to reusing it is **finding and identifying the owners**, and that is a data and matching problem. PAC digitalisation (SIEX / Cuaderno Digital de Explotación) is being phased in over 2026-2028, which opens a window for smallholder tools.

### Cited Findings
- Galicia has **512,308 ha of abandoned farmland with high productive capacity (~16% of the territory)**. About 10% of communal forest (montes vecinais), roughly 70,000 ha, is also abandoned. The Xunta plans to bring abandoned montes vecinais into the Banco de Terras. — [Campo Galego](https://www.campogalego.es/la-xunta-proyecta-incorporar-al-banco-de-terras-montes-vecinales-en-abandono/)
- **More than 11 million rural parcels = 28.5% of Spain's total**, while Galicia is only 5.85% of Spain's area. Fragmentation and the difficulty of *identifying or locating owners* are among the main barriers to recovering land. — [Campo Galego](https://www.campogalego.es/la-xunta-proyecta-incorporar-al-banco-de-terras-montes-vecinales-en-abandono/)
- Galicia has **1.7 million owners of rustic land but only ~44,000 primary-sector workers** (headline, Sept 2026). — [El Correo Gallego](https://www.elcorreogallego.es/galicia/2026/09/20/galicia-1-7-millones-propietarios-134479671.html) (headline and snippet only; the fetch was blocked)
- The Banco de Terras was created in 2007. The average rent is **€58 per plot / €115 per ha**. The average plot offered is **0.5 ha** (Lugo 0.66 ha, Pontevedra 0.34 ha). — [El Correo Gallego](https://www.elcorreogallego.es/galicia/el-banco-de-tierras-la-salvacion-para-muchos-agricultores-gallegos-JE11730393) (snippet; date of the figures not confirmed)
- The PAC digital farm notebook (CUE) has been voluntary since 1 Jan 2024. Electronic recording of phytosanitary treatments via SIEX becomes mandatory nationally from **1 Jan 2027** for farms receiving PAC aid, with the full CUE from **1 Jan 2028**. Galicia follows the 2027 date. Castilla y León and Andalucía (farms >25 ha) required it from 2026. — [Visualnacert](https://visualnacert.com/cuaderno-digital-explotacion-agricola-fechas-obligaciones-2026-2028/); [Revista Agricultura](https://www.revistaagricultura.com/Noticias/Noticia/9512/cuaderno-digital-explotacion-voluntario-hasta-2027); [Santander blog](https://www.bancosantander.es/blog/pymes-negocios/siex)
- Paper format is still allowed for farms not otherwise required to go digital, as a concession to farmers facing technology barriers. — [Revista Agricultura](https://www.revistaagricultura.com/Noticias/Noticia/9512/cuaderno-digital-explotacion-voluntario-hasta-2027)
- Vineyards: in 2025 DO Ribeiro had its **worst harvest since records began** and is working on a "new model". Rías Baixas had a record 47.5M kg in 2025. Galicia as a whole harvested almost 76M kg. — [La Región](https://www.laregion.es/o-ribeiro/d-ribeiro-trabajara-nuevo-modelo_1_20251010-4011657.html); [Galiciapress](https://www.galiciapress.es/articulo/economia/2025-10-25/5478246-termina-mayores-vendimias-historia-galicia-casi-76-millones-kilos-uva-24)
- 2026 Rías Baixas: average production losses of **10.6% (vs 5.5% the year before)**, from flower drop, frost, hail, wind, pests and diseases. The harvest was over 45.8M kg, the earliest campaign ever. — [El Correo Gallego](https://www.elcorreogallego.es/economia/2026/09/14/vendimia-rias-baixas-supera-45-134280236.html) (snippet)
- Mildew aid for 2026 requires growers to **document** that the 2025 harvest was clearly below average **and** that anti-mildew treatments were applied correctly. This is a record-keeping burden. — [Isagri](https://www.isagri.es/blog/ayudas-mildiu-vinedo-2026)

### Inferences
- **Owner identification for abandoned land** is a clear "AI + open data" gap. It would mean cross-referencing Catastro (open cadastral data and INSPIRE parcels), SIGPAC, the Banco de Terras offer and fire-strip notification data to suggest likely owners or heirs and pool plots into viable units. Nobody seems to solve this at scale. The Banco de Terras is a passive listing of small plots.
- The 2027 SIEX deadline means tens of thousands of Galician smallholders (mostly older) will have to log treatments digitally. Existing commercial field-notebook apps (e.g. Visualnacert, Locatec, Agroptima, not checked in depth) target professional or larger farms. A **voice/WhatsApp-first, Galician-language treatment logger** that exports SIEX-compatible records and also serves as evidence for mildew/damage aid is a plausible niche.
- Mildew risk models exist (weather-based, e.g. from MeteoGalicia/EVEGA advisories; not verified here). The gap is probably in pushing plot-level alerts to small growers, not in the models themselves.

### Gaps
- I did not find a searched source for the **current number of Banco de Terras contracts or hectares mobilised**, or its budget.
- I found no quantified figures on the PAC paperwork burden (hours/cost per farmer) for Spain or Galicia.
- I did not research irrigation or soil monitoring specifically (Galicia is mainly rain-fed, so this is lower priority).

## Wildfires: 2025 season, fuel-strip (franxas) obligations, early warning

### Takeaway
2025 was Galicia's third-worst fire year in 50 years (~118,764 ha), and 86% of it was in Ourense. Enforcement of fuel-strip clearing is weak. In 2025 there were 244,199 parcels inspected, 64,839 non-compliance notices and roughly one in three inspected parcels uncleared. A new law (announced Sept 2026) widens strips to 100 m and raises fines to €100,000. That will greatly increase the need to **identify responsible owners, notify them and verify clearing**.

### Cited Findings
- The official Xunta total for 2025 is **118,763.5 ha burned**, the third worst in the series after 1989 (198,998 ha) and 1978 (119,634 ha). **86% of the burned area was in Ourense**, which was in emergency situation 2 from 12 to 26 August. The Ourense fires were the three largest in Galician history. **A Rúa/Larouco burned 44,424 ha**, the largest ever. The post-2025 fire plan puts **74% of high-risk locations in Ourense**. — [El Correo Gallego](https://www.elcorreogallego.es/galicia/2026/04/06/plan-incendios-forestales-galicia-catastrofe-2025-128779340.html); [SomosComarca](https://www.somoscomarca.es/articulo/actualidad/valdeorras-epicentro-peor-verano-incendios-galicia-mas-90000-hectareas-arrasadas-ourense/20250901102007202789.html)
- Spain as a whole had its worst season since 1994, with **>382,000 ha by 21 Aug 2025**. The EU (EFFIS) said 2025 was the worst year on record in hectares. — [Euronews](https://www.euronews.com/green/2025/08/21/spains-sees-worst-wildfire-season-since-1994-with-382000-hectares-burned-so-far-in-2025); [Infobae](https://www.infobae.com/tag/sistema-europeo-de-informacion-sobre-incendios-forestales)
- One year on, residents of the affected Ourense areas say "se sigue pasando muy mal" (it is still very hard). — [El Español](https://www.elespanol.com/treintayseis/actualidad/provincia-de-ourense/20260813/ano-oleada-incendios-arraso-ourense-sigue-pasando-mal/1003744352168_0.amp.html)
- Lei 3/2007 requires owners to clear secondary strips around homes by **31 May** each year. Last year the Xunta **inspected 244,199 parcels, and Seaga sent 64,839 non-compliance notices** to municipalities. Compliance is weak because of owner neglect, lack of resources, or forestry firms that cannot handle the volume. **About one in three inspected parcels was not clean.** — [El Correo Gallego](https://www.elcorreogallego.es/galicia/2026/03/25/tres-fincas-inspeccionadas-xunta-pasado-no-cumplia-limpieza-128373071.html) (snippet)
- In 2025 there were **226 fines** for not clearing, and the number is rising. Fines of about €900 are typical for missing the 31 May deadline. — [GaliciaE](https://www.galiciae.com/articulo/galicia/multas-limpiar-fincas-evitar-fuegos-van-mas-226-2025/20260531101012107883.html); [Galiciapress](https://www.galiciapress.es/articulo/economia/2026-05-23/5892648-multas-900-euros-no-gestionan-fajas-biomasa-antes-31-mayo)
- The **new Galician fire law (Sept 2026)** makes clearing a direct legal obligation (not subsidiary). It doubles strips in strategic zones **from 50 to 100 m** and sets fines of **up to €100,000**. It goes to Parliament in October. — [elEconomista](https://www.eleconomista.es/infraestructuras-servicios/noticias/14015475/09/26/la-xunta-duplica-a-100-metros-la-franja-antiincendios-y-convierte-su-limpieza-en-obligacion-legal-directa.html); [El Ideal Gallego](https://www.elidealgallego.com/galicia/2026-09-21/nueva-ley-de-incendios-sanciones-de-hasta-100-000-euros-por-incumplir-la-limpieza-de-franjas-880375.html)
- A single municipality, Culleredo, issued **6,000 notices** to clear secondary strips. — [ACoruñaXa](https://acorunaxa.com/es/news/emiten-6-000-avisos-en-culleredo-para-limpiar-las-franjas-secundarias-de-los-montes/84167/)

### Inferences
- The notification pipeline is huge and manual: 64,839 notices, then municipalities, then owners who are often unknown, dead or emigrated. The tools that could help are:
  1. a citizen tool that answers "does my parcel fall in a strip, and what must I do by 31 May?" using Catastro plus strip GIS layers;
  2. satellite (Sentinel-2) change detection to pre-verify clearing before inspections;
  3. a marketplace matching owners with local clearing contractors.
- The problem overlaps with the land-abandonment owner-identification problem, so one data layer could serve both.

### Gaps
- I found no source on how many notified owners are unknown or unreachable, or on specific early-warning or detection tools in use (cameras, satellite). Worth checking the Xunta's PLADIGA plan.

## Sea and fisheries: marisqueo, mussel closures, lonxas

### Takeaway
There are two severe, well-quantified crises:
1. **Mussel**: record-long toxin closures, with all Galician bateas polygons closed in May 2026 and 2025 output at a historic low of 177,638 t.
2. **Bivalves**: lonxa sales of bivalves fell 52% in 10 years, and high-value clams fell by ~87-89%, driven by low-salinity mortality after heavy rain.

Both are forecasting and monitoring problems.

### Cited Findings
- Nov 2025: **41 of 52 mussel polygons (~80%) closed** because of lipophilic toxins, and about 90% within days. Every polygon in the Pontevedra, Vigo, Baiona and Muros-Noia rías was closed. — [El Debate](https://www.eldebate.com/espana/galicia/20251111/alerta-toxinas-casi-80-poligonos-bateas-mejillon-cerrados_353774.html); [Telecinco](https://www.telecinco.es/noticias/galicia/20251118/bateas-mejillones-cerradas-toxina_18_017606263.html)
- May 2026: INTECMAR ordered the **closure of all (more than 50) mussel polygons in Galicia** because of a red tide (Dinophysis acuminata). — [El Español/Quincemil](https://www.elespanol.com/quincemil/economia/20260519/poligonos-bateas-galicia-cerrados-debido-toxina/1003744251759_0.html); [El Debate](https://www.eldebate.com/espana/galicia/20260519/galicia-ordena-cierre-todos-poligonos-bateas-galicia-expansion-marea-roja_419264.html)
- 2025 mussel production was a **historic minimum of 177,638 t**, attributed to red tide. — [El Debate](https://www.eldebate.com/espana/galicia/20260519/galicia-ordena-cierre-todos-poligonos-bateas-galicia-expansion-marea-roja_419264.html) (snippet)
- Lonxa bivalve sales fell from **7.77M kg (2015) to 3.74M kg (2025), −52%**. **Almeja babosa −89% (1,079 → 116 t)**, **almeja fina −87% (548 → 70 t)** and **berberecho −80%+**. — [Galiciapress](https://www.galiciapress.es/articulo/economia/2026-09-15/6015356-galicia-perdido-mitad-marisco-diez-anos); [elDiario.es](https://www.eldiario.es/galicia/desplome-marisco-galicia-cae-mitad-decada_1_13517426.html); [El Debate](https://www.eldebate.com/espana/galicia/20260920/radiografia-hundimiento-marisco-gallego-lonjas-pierden-52-bivalvos-diez-anos_460191.html)
- Cause: freshwater and low-salinity events (autumn 2022, winter 2023, early-2026 storms). Mortality in March 2026 was **berberecho 89%, japonesa 66%, babosa 96% and fina 31%**. The Xunta mobilised **€22.7M** for bank recovery. — [Moncloa.com](https://www.moncloa.com/2026/09/18/desplome-marisco-galicia-bivalvos-almeja-babosa-3433513); [Xataka](https://www.xataka.com/magnet/a-puertas-verano-marisco-gallego-se-enfrenta-a-su-particular-via-crucis-uno-marcado-clima-vedas-toxinas)
- On-foot harvesting permits fell from **3,826 (2015) to 3,179 (2025), −16.9%**. — [Galiciapress](https://www.galiciapress.es/articulo/economia/2026-09-15/6015356-galicia-perdido-mitad-marisco-diez-anos)

### Inferences
- INTECMAR already publishes daily closure status and oceanographic data. MeteoGalicia runs ocean and river models. The gap is **prediction**: forecasting closures a few days ahead (HAB forecasting from upwelling, temperature and phytoplankton counts) and **salinity-mortality early warnings** for shellfish banks from river discharge and rain forecasts, so cofradías can harvest early or move stock. A small team could build a forecasting and alert layer on existing open data. That is technically ambitious but feasible, and highly relevant.
- Lonxa price and volume data (Plataforma Tecnolóxica da Pesca / pescadegalicia.gal, not verified here) could feed price-transparency or demand-forecasting tools for mariscadoras.

### Gaps
- I did not verify fishing-quota issues or the state of lonxa digitalisation (electronic auctions are known to exist, but I did not source that).
- There is no quantified € loss for bateas closures in 2025-2026 from a primary source.

## Public administration: bureaucracy, subsidy access, digital divide, depopulation

### Takeaway
Subsidies go unclaimed at a massive scale because of lack of awareness and complexity. More than 50% of SMEs never apply, about 25% abandon an application once started, and about 60% of 2024 state subsidies were still undistributed. Meanwhile only 37.5% of people aged 65-74 interact with e-government. Galicia's ageing (26.9% aged 65+, over 30% in Lugo and Ourense) makes the divide worse.

### Cited Findings
- **More than 50% of SMEs do not apply for public aid because they do not know about it**, and **1 in 4 abandon an application because of complexity**. — [MuyPymes](https://www.muypymes.com/2025/10/02/mitad-pymes-ayudas-publicas-desconocimiento)
- "Almost half the money available is never requested". About **60% of 2024 subsidies still undistributed**, and only ~22% of 2024 funds executed by May. — [Merca2](https://www.merca2.es/2025/07/23/ia-subvenciones-publicas-2215924/); [Emprendedores](https://emprendedores.es/ayudas/subvenciones-adjudicacion/) (secondary sources; the underlying source, probably IGAE/BDNS, was not verified)
- CEOE complains that EU funds have not reached SMEs because of bureaucracy (Aug 2026). — [Autónomos y Emprendedores](https://www.autonomosyemprendedor.es/articulo/autonomos/gobierno-dice-que-70-ayudas-europeas-han-sido-pymes-ceoe-critica-burocracia/20260819135819055483.html)
- INE 2023: only **37.5% of people aged 65-74** interacted with the administration online in the last 12 months. INE 2024: only **35.9% of people over 74** use the internet regularly. — [Yahoo/EFE](https://es-us.noticias.yahoo.com/brecha-digital-mayores-37-5-163532672.html); [UGT study, May 2025](https://www.ugt.es/sites/default/files/Microsoft%20Word%20-%20Def.%20ESTUDIO-MAYORES%20Y%20EXCLUSI%C3%93N%20TECNOL%C3%93GICA%20VF%2009052025.pdf)
- A news report (May 2026) covers people losing benefits because they cannot use digital channels ("Mi abuelo no tiene ordenador y se ha quedado sin ayuda"). — [Moncloa.com](https://www.moncloa.com/2026/05/28/brecha-digital-administracion-3380228/)
- Galicia is **26.9% aged 65+**, projected **33.1% by 2039**. Average age is **48.5** (2025). **Lugo is 30.2% and Ourense 32.3%** aged 65+, with average ages of 50.5 and 51.4. — [Galiciae](https://www.galiciae.com/articulo/galicia/2039-uno-cada-tres-gallegos-habra-cumplido-65-anos/20260523050000107763.html); [Galiciapress](https://www.galiciapress.es/articulo/ultima-hora/2026-02-20/5779990-envejecimiento-poblacion-gallega-eleva-edad-media-485-anos-2025); [elDiario.es](https://www.eldiario.es/galicia/retrato-galicia-envejecida-reto-cuidados-soledad-cuatro-personas-mayor-65-anos_1_11260959.html)

### Inferences
- **Subsidy matching** is the most "AI-agent-shaped" opportunity. BOE, DOG and BDNS (Base de Datos Nacional de Subvenciones, open API) are all public. An agent could parse calls, extract eligibility rules and match them to a citizen, SME or farm profile, then help fill in forms. Commercial players exist (e.g. consultancies, TaxDown for some citizen aid; startup landscape not verified). The gap is **Galician-language, DOG-focused, citizen- and smallholder-oriented** matching, not just SME matching.
- For the elderly, the need is assisted channels (phone or voice agents, family-delegated flows) rather than yet another website.

### Gaps
- There are no hard numbers on the DOG's annual volume of calls or the Xunta's unexecuted budget share.
- I did not find Galicia-specific e-administration usage data by age.

## Personal finance: literacy, fraud, bills, social tariffs

### Takeaway
Only 53% of Spanish adults answer three basic financial questions correctly (2021, the latest published ECF). Cyber-fraud is now about 20% of all crime: 429,677 computer frauds in 2025, and 51-65 is the most-victimised age group. Energy social tariffs reach only about a third of eligible households: 2.45-2.87M households (~10M people) miss out.

### Cited Findings
- Banco de España ECF 2021: **53% answered all three questions correctly** (inflation, compound interest, diversification), +2 pp vs 2016. The inflation question was answered correctly by 65%. — [BdE Cliente Bancario](https://clientebancario.bde.es/pcb/es/blog/Encuesta_sobre__f04e08accd0b361.html); [Aula Financiera](https://www.aulafinancieraydigital.es/2023/11/los-espanoles-mejoran-sus-niveles-de-competencias-financieras)
- Ministry of the Interior: **488,426 cybercrimes in 2025**, ~20% of all known crime. **429,677 were computer frauds** (+4%). There were **383,285 victims (+9.3%)**, and the most common age band was **51-65**. **146,737 were victims of card-related fraud.** — [Interior](https://www.interior.gob.es/opencms/es/detalle/articulo/Los-ciberdelitos-representaron-en-2025-casi-el-20-por-ciento-de-la-criminalidad-total-en-Espana/)
- Kaspersky-based report: digital scams cost victims **€577 on average**, and **69% are never reported**. — [Moncloa.com](https://www.moncloa.com/2026/06/26/espana-kaspersky-estafas-3390303/) (vendor-sourced figure; treat with caution)
- Bono social eléctrico: **more than 60% of eligible households do not receive it**. That is **2.45-2.87M households (~10M people)**. Only 6.4% of households receive it, against an eligible 18.7-21.1%. 24.4% of Spaniards do not know what it is. The INE figure for energy poverty is 27% of households (by some measure). — [Diario Socialista, Sept 2026](https://diariosocialista.net/2026/09/18/el-bono-social-electrico-solo-llega-a-un-tercio-de-los-hogares-que-pueden-recibirlo/) (partisan outlet reporting a study; the underlying source was not verified); a counterpoint is that more than half of large families and pensioners who receive it may not need it — [Infobae](https://www.infobae.com/espana/2026/03/13/la-polemica-del-bono-social-electrico-mas-de-la-mitad-de-las-familias-numerosas-y-los-pensionistas-que-cobran-la-ayuda-no-la-necesitan-sobre-todo-en-madrid/)

### Inferences
- These are "benefit take-up" problems (bono social, subsidies, rent aid). An agent that reads a household's situation or a bill (with consent), checks eligibility and pre-fills the application is a strong, measurable project idea. It could also compare PVPC with the free market.
- For fraud, the gap is a **real-time "is this a scam?" checker** for SMS, WhatsApp and calls, aimed at older users and their families. Banks and INCIBE (017 helpline) exist, but they are reactive.

### Gaps
- I did not find whether a 2025/2026 ECF edition has been published. The latest confirmed data is 2021.
- I did not research IRPF complexity metrics, PVPC bill-comprehension data or bank fee levels.

## Housing: rents, tourist flats, public aid

### Takeaway
Rents in Galician cities keep rising: Santiago €704 (+8% y/y), Vigo €726 and A Coruña ~€865 per month. Demand pressure is up to 42 applicants per listing. Santiago's tourist-flat regulation is now firm and the supply of flats is falling. Public aid (Bono Alquiler Joven, €12.95M for 2025-26) is allocated first-come-first-served until the budget runs out.

### Cited Findings
- Average Galician rent is **€780/month (+4% vs 2025)**. Demand rose from **35 to 42 interested people per listing** (end-2025 → early 2026). — [El Correo Gallego](https://www.elcorreogallego.es/galicia/2026/04/28/alquiler-galicia-sube-780-euros-santiago-a-coruna-vigo-129617872.html) (snippet)
- Santiago new leases: **€704.1 (June 2026), +€52 / +8% y/y**, and the number of new contracts is falling. Vigo **€726.2**. A Coruña **€10.81/m², ~€865** for a typical flat. — [El Correo Gallego](https://www.elcorreogallego.es/santiago/2026/08/31/alquiler-dispara-santiago-704-euros-133800125.html); [El Correo Gallego](https://www.elcorreogallego.es/santiago/2026/08/19/alquileres-santiago-subida-precio-vivienda-133464292.html) (snippets)
- Tourist flats in Santiago (INE): **420 in May 2026 vs 661 in Aug 2024 (−36.5%)**, while the REAT registry listed 831 at an earlier point, a data discrepancy. New VUTs are banned in the historic centre, and the TSXG confirmed the regulation as final (July 2026). — [El Correo Gallego](https://www.elcorreogallego.es/santiago/2026/08/31/oferta-vivienda-turistica-santiago-reduce-133712449.html); [Moncloa.com](https://www.moncloa.com/2026/07/07/tsxg-confirma-regulacion-pisos-turisticos-santiago-3396183)
- The Xunta publishes VUT data via its Sistema de Intelixencia Turística. — [Turismo de Galicia AEI](https://aei.turismo.gal/es/alojamientos/viviendas)
- Bono Alquiler Joven Galicia 2025: applications from 28 Feb to 28 Mar 2025, with **€12,954,936** over 2025-26. Applications are **denied when budget runs out, in chronological order of registration**. — [DOG 20/2/2025](https://www.xunta.gal/dog/Publicados/2025/20250220/AnuncioC3Q2-070225-0001_es.html); [IGVS](https://igvs.xunta.gal/es/ayudas/programa-bono-alquiler-joven-vi482e)

### Inferences
- The gap between registered VUTs (REAT) and actual listings (INE web-scraped) suggests room for an **illegal/unregistered tourist-flat detector** that matches Airbnb/Booking listings against REAT, of use to municipalities. The EU short-term rental registry regulation (applicable 2026) adds relevance.
- First-come-first-served aid rewards speed and literacy. A notifier and prep assistant (so documents are ready the day a call opens in the DOG) directly improves someone's odds.

### Gaps
- I found no data on Bono Alquiler Joven application versus award numbers, or on payment delays in Galicia.
- I did not research Vigo or A Coruña VUT figures.

## Health: waiting lists, rural access, loneliness

### Takeaway
SERGAS itself expects surgical wait times to stay flat or rise in 2026 in most areas. Galicia is losing family doctors (181 retirements in 2025-26, with 26 family-medicine training posts unfilled). About 137,600-139,700 people aged 65+ live alone.

### Cited Findings
- 2026 SERGAS management agreements forecast surgical wait times will **stay the same or increase in most health areas**. Ourense's target is **61.5 days**, and Lugo's is **54 days (June)/55 (Dec)**. Waits are "~70 days" across most specialties. — [infoLibre](https://www.infolibre.es/politica/xunta-preve-mantener-aumentar-espera-quirurgica-2026-mayoria-areas-sanitarias_1_2148262.html); [El Progreso](https://www.elprogreso.es/articulo/lugo/sergas-asume-que-ano-lucenses-esperaran-mas-tiempo-operarse/202602060500001943797.html)
- Waiting lists keep growing after the pandemic (April 2026 data). — [Galiciapress](https://www.galiciapress.es/articulo/sanidad/2026-04-17/5847633-datos-listas-espera-prueban-cada-vez-hay-gallegos-esperando-consultas-cirugias)
- Case report: a cancer patient waited 7 months for surgery with no date (July 2026). — [Moncloa.com](https://www.moncloa.com/2026/07/18/listas-espera-galicia-paciente-cancer-sergas-3401812/)
- **66 doctors retiring in 2025 and 115 in 2026 (181 fewer in two years)**. **36 of 207 specialised-training posts were unfilled (8.2%)**, 26 of them in family medicine. The Xunta proposes letting foreign-trained doctors skip the MIR exam and paying extra to doctors who take on vacant patient lists. — [Galiciapress](https://www.galiciapress.es/articulo/sanidad/2026-06-16/5920775-vacante-8-plazas-formacion-sanitaria-especializada-galicia-mayoria-medicina-familiar); [COPE](https://www.cope.es/emisoras/galicia/noticias/pulso-galicia-reforma-atencion-primaria-bajara-exigencia-medico-centro-salud-20251106_3247067.html); [Redacción Médica](https://amp.redaccionmedica.com/secciones/parlamentarios/galicia-anuncia-un-paquete-de-mejoras-salariales-para-trabajar-en-primaria-9296)
- Loneliness: **137,619 people aged 65+ lived alone in Galicia in 2024**, 70% of them women (another source gives 139,700). Loneliness and ageism are hurting older people's mental health. — [elDiario.es](https://www.eldiario.es/galicia/retrato-galicia-envejecida-reto-cuidados-soledad-cuatro-personas-mayor-65-anos_1_11260959.html); [El Correo Gallego](https://www.elcorreogallego.es/sociedad/2026/07/29/soledad-edadismo-lastran-salud-mental-132882889.html)

### Inferences
- SERGAS publishes waiting-list data every six months by area. A **transparency dashboard** is easy, but its impact is limited. More useful would be triage or paperwork help for the doctor shortage, such as clinical note summarisation in Galician. That requires institutional partnerships and faces high regulatory barriers for a small team.
- Loneliness: phone- and voice-based companion or check-in agents for the ~138k people living alone, coordinated with concellos' home-help services. The Xunta already runs teleassistance programmes (not verified here), so the gap is proactive and conversational contact.

### Gaps
- I found no figures on consultorios without a doctor in rural Galicia, or on travel time to care.

## Energy: wind conflicts, energy communities, self-consumption

### Takeaway
Wind is locked in legal back-and-forth. The TSXG annulled dozens of Xunta authorisations and blocked 64 projects. The Supreme Court (2026) validated the Xunta's procedure and revived them, but the TSXG keeps annulling individual parks (A Ruña III). Local opposition and uncertainty persist. I did not source data on energy communities.

### Cited Findings
- **64 wind projects blocked** by Galician courts were reactivated after Supreme Court rulings validated the Xunta's environmental procedure. — [Xataka](https://www.xataka.com/energia/64-proyectos-bloqueados-judicialmente-ahora-vuelven-a-estar-marcha-galicia-tribunal-supremo-les-ha-dado-razon)
- Supreme Court ruling 651/2026 (27 May) overturned the TSXG annulment of the Bustelo park (Greenalia). Shared grid infrastructure does not make several parks a single project. — [Adiante Galicia](https://www.adiantegalicia.es/medio-rural/2026/05/30/el-tribunal-supremo-revoca-la-anulacion-del-parque-eolico-bustelo-dictada-por-el-tsxg.html); [Energías Renovables](https://www.energias-renovables.com/eolica/el-supremo-avala-que-los-parques-e-20260604)
- The TSXG has nonetheless annulled other parks (A Ruña III, and one after the EU court endorsement), raising legal-certainty alarms. — [Energías Renovables](https://www.energias-renovables.com/eolica/el-tsxg-tumba-el-parque-e-20251029); [elDiario.es](https://www.eldiario.es/galicia/anulado-permiso-parque-eolico-primera-sentencia-galicia-aval-europeo-tramitacion-xunta_1_12722126.amp.html)

### Inferences
- There are possible civic-tech angles: a map of wind projects with their legal status and public consultation deadlines, or a tool that helps neighbours and comunidades de montes read environmental impact studies (EIA) with an LLM and submit allegations. The other side is helping rural collectives set up energy communities or shared self-consumption (paperwork, allocation coefficients). This is lower confidence, as I had no data on communities.

### Gaps
- I found no sourced numbers on energy communities in Galicia, self-consumption growth or the number of wind projects being processed.

## Tourism: Camino de Santiago

### Takeaway
The Camino hit a record **530,987 pilgrims in 2025 (+6%)**, and 45.7% of them walked the Camino Francés. Growth is concentrated on the last 100 km and in peak months, which strains albergues, Santiago's housing and services.

### Cited Findings
- **530,987 pilgrims certified in 2025**, the first year above 500k, against **499,180 in 2024**. 53.4% were women, and ~297k came from abroad (43,980 US, 26,680 Italy, 24,356 Germany). — [Diario de Santiago](https://www.diariodesantiago.es/camino-de-santiago/el-camino-de-santiago-bate-record-en-2025-y-supera-los-530-000-peregrinos/); [Religión en Libertad](https://www.religionenlibertad.com/espana/260103/camino-santiago-bate-propio-record-530-000-peregrinos-2025_115820.html)
- The Camino Francés had 242,175 pilgrims (45.7%), the Portuguese route 100,835 (19%) and the Portuguese Coastal route ~89,700 (17%). — [Diario de Santiago](https://www.diariodesantiago.es/camino-de-santiago/el-camino-de-santiago-bate-record-en-2025-y-supera-los-530-000-peregrinos/)
- Almost 300,000 pilgrims from 183 countries had arrived by the end of July 2025. — [El Correo Gallego](https://www.elcorreogallego.es/santiago/2025/08/03/camino-records-300-000-peregrinos-120302832.html)

### Inferences
- The gaps are **load balancing**: real-time albergue availability across the network of public (Xunta) and private hostels, stage-level crowding forecasts and nudging people to alternative routes (Invierno, Primitivo, Inglés). The Oficina del Peregrino publishes stats. Public albergues are first-come, first-served, with no booking. This is a concrete multilingual agent use case, but commercial Camino apps (e.g. Buen Camino, Wise Pilgrim) already cover guides, so any new tool would have to compete on live data.

### Gaps
- I found no quantified albergue capacity or overcrowding incidents, and no Santiago tourism-tax data.

## Other striking problems / cross-cutting

### Takeaway
One pattern runs through most of the sectors above: **rights and obligations fail because people cannot find, understand or act on public information in time**. This covers bono social take-up (~1/3), SME subsidies (>50% never apply), first-come-first-served housing aid, fire-strip obligations (64,839 notices) and SIEX obligations for older smallholders. The underlying data is largely open: BOE/DOG/BDNS, Catastro, SIGPAC, INTECMAR, MeteoGalicia, IGE/INE and Copernicus.

### Cited Findings
- See the figures above for the bono social ([Diario Socialista](https://diariosocialista.net/2026/09/18/el-bono-social-electrico-solo-llega-a-un-tercio-de-los-hogares-que-pueden-recibirlo/)), SMEs ([MuyPymes](https://www.muypymes.com/2025/10/02/mitad-pymes-ayudas-publicas-desconocimiento)), fire strips ([El Correo Gallego](https://www.elcorreogallego.es/galicia/2026/03/25/tres-fincas-inspeccionadas-xunta-pasado-no-cumplia-limpieza-128373071.html)) and the digital divide ([Yahoo/EFE](https://es-us.noticias.yahoo.com/brecha-digital-mayores-37-5-163532672.html)).

### Inferences (ranked shortlist for a small AI + open-data team)
1. **Galician parcel intelligence**: Catastro + SIGPAC + strip layers + Sentinel-2. It answers "what must I do with my land (fire strips, SIEX, Banco de Terras)?" and detects cleared/uncleared strips. It serves both the 64,839-notice fire problem and the 512k ha abandonment problem.
2. **Shellfish/mussel early warning**: toxin-closure and low-salinity mortality forecasts from INTECMAR + MeteoGalicia data. The pain is acute and quantified (all polygons closed, −52% bivalves).
3. **DOG/BOE/BDNS benefits agent**: eligibility matching and form pre-fill for citizens, smallholders and the elderly, in Galician. This targets the take-up gaps (bono social, rent aid, subsidies).
4. **Scam checker for older people**, focused on the 51-65+ group, 383k victims/year.
5. **Tourist-flat compliance matcher** (listings vs REAT) for concellos.

### Gaps
- I have not verified the existing startups or public tools for each idea. Competitive scanning should come before committing.
- I did not cover: IRPF complexity, PVPC bill data, bank fees, fishing quotas, lonxa digitalisation, irrigation/soil or energy communities (numbers). These need follow-up searches.
