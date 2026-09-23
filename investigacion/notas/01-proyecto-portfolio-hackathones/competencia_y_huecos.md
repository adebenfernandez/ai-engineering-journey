# Competitive landscape and white space for a Galicia/Spain AI-agent portfolio project (as of Sep 2026)

Method note: Web search worked, but WebFetch was blocked by the egress proxy for most primary domains (xunta.gal, elreferente.es, euronews, eleconomista, arxiv, mancomun.gal). So many findings below rest on search-result snippets and aggregated summaries of the linked pages, not full-page reads. Treat numeric claims as "reported by the linked source". Pricing and traction data was sparse; the Gaps sections say where.

## 1. Agritech in Spain/Galicia (smallholders, minifundio, viticulture)

### Takeaway
Spanish agritech is crowded at the farm-management and compliance layer (SIEX digital field notebooks: VisualNACert/Agroptima, Isagri, Locatec, oSIGris) and at drones (Hemav). Galician viticulture is getting public, DO-level disease-alert infrastructure (Ribeira Sacra weather stations, Fitovit, alert app). There is room for a low-cost, conversational, Galician-language "field copilot" that turns the new mandatory SIEX obligations and the DO alert data into plain-language actions for tiny, fragmented plots.

### Cited Findings
- Galicia ranks 4th among Spanish regions for agritech entrepreneurship (7.38% of entrepreneurs). Activity is still concentrated in Madrid, Catalonia and Castilla y León. — [MuyPymes, Dec 2025](https://www.muypymes.com/2025/12/24/aumentan-startups-inversion-agrifoodtech-nacional); [Revista Alimentaria](https://revistaalimentaria.es/industria/food-tech/el-ecosistema-agrifoodtech-espanol-resiste-aumentan-las-startups-pese-a-la-caida-de-la-inversion)
- The Spanish agrifoodtech ecosystem has more startups but less investment. — same sources as above
- Recarbo: a Galician digital platform for digitalising agricultural and livestock operations. It is listed in El Referente's "Top15 new Agrotech wave". — [El Referente Top15](https://elreferente.es/startups/top15-la-nueva-ola-agrotech-que-digitaliza-el-campo/) (snippet only; the page could not be fetched)
- SIEX (the national information system for farms) and the mandatory digital farm notebook: registering phytosanitary treatments was due to become mandatory in Jan 2026 (unless Spain requested an extension). Registering fertilisers and producing a Fertilisation Plan became mandatory from 1 Jan 2026. Further obligations follow up to 2028. — [VisualNACert](https://visualnacert.com/cuaderno-digital-explotacion-agricola-fechas-obligaciones-2026-2028/); [VisualNACert SIEX](https://visualnacert.com/siex-cuaderno-campo-digital/)
- VisualNACert (which owns Agroptima) sits in the Ministry of Agriculture's mixed working group for SIEX. — [VisualNACert](https://visualnacert.com/cuaderno-de-campo-digital-siex-eng/)
- The market has free options from the Administration plus paid professional tools. One provider (Locatec AgroGEST) quotes €495 in pay-per-use mode for partners. — [Locatec pricing](https://locatec.es/cuanto-cuesta-el-cuaderno-de-campo-digital-precios-descuentos-y-ayudas/); [Locatec](https://locatec.es/cuaderno-de-campo-digital/)
- Other SIEX notebook vendors: Isagri, oSIGris. — [Isagri](https://www.isagri.es/software-agricola/cuaderno-campo/); [oSIGris](https://osigris.com/siex/news04.php)
- Hemav is described as the world's 4th-largest drone operator and the 1st in agriculture. Spraying drones in Spain cost €8,000–28,000, about 40% cheaper than in 2021. More than 1,200 RPAS operators registered phytosanitary drone activity in 2024 (MAPA data). — [Interempresas](https://www.interempresas.net/Smart_Cities/Articulos/211228-La-espanola-Hemav-cuarta-operadora-mundial-de-drones-y-primera-en-agricultura.html); [CultivoTech](https://cultivotech.com/drones-para-fumigar-precios-espana/)
- Ribeira Sacra DO (with the Lugo and Ourense provincial councils) is building a network of viticulture weather stations that feed Fitovit and a free, proprietary alert system for winegrowers. It sends personalised alerts and risk maps based on humidity, temperature and historical data. — [COPE, Sep 2025](https://www.cope.es/emisoras/galicia/lugo-provincia/lugo/noticias/viticultores-ribeira-sacra-dispondran-informacion-real-sobre-factores-climaticos-prevenir-enfermedades-vides-20250912_3212495.html); [COPE, Jul 2026](https://www.cope.es/emisoras/galicia/lugo-provincia/lugo/noticias/datos-climaticos-real-herramientas-tecnologicas-facilitarle-vida-viticultor-d-ribeira-sacra-digitaliza-20260728_3411447.html)
- Ribeira Sacra uses drones and AI for "heroic viticulture" (May 2026). — [COPE, May 2026](https://www.cope.es/emisoras/galicia/lugo-provincia/lugo/noticias/ribeira-sacra-apoya-drones-e-inteligencia-artificial-revolucionar-viticultura-heroica-20260526_3371438.html); [Agronews](https://agronews.com/es/es/news/agrosfera/2026-04-26/86508)
- A "persistent mildew" outbreak in Ribeira Sacra caused notable harvest losses in June 2025. — [COPE, Jun 2025](https://www.cope.es/emisoras/galicia/lugo-provincia/lugo/noticias/viticultores-ribeira-sacra-luchan-mildiu-persistente-amenaza-arruinar-parte-cosecha-uva-20250618_3171498.html)
- The 2025 Spanish harvest trend was robotics, UAVs and AI for vineyards on complex terrain facing labour shortages. — [search summary citing MuyPymes/Revista Alimentaria](https://www.muypymes.com/2025/12/24/aumentan-startups-inversion-agrifoodtech-nacional)

### Inferences
- The incumbents target professional farms and cooperatives. Elderly part-time Galician smallholders (minifundio) are underserved by form-heavy notebook software. They are likely to face the new SIEX obligations with the least support.
- The DO alert systems output raw risk data. None of the sources shows an assistant that turns a mildew risk into a concrete action and then logs the treatment in SIEX format, in Galician, via voice or WhatsApp.
- Hardware-heavy ideas (drones, IoT) are poor portfolio demos. A software agent built on public weather and parcel (SIGPAC) data is demo-able.

### Gaps
- No pricing found for VisualNACert/Agroptima or Hemav revenue. The El Referente list could not be fetched, so the full Top-15 names are missing.
- No data found on the cost of smallholder soil/IoT sensor kits in Galicia.
- The Xunta's own digital-agriculture programmes (e.g. the Fitovit ownership model and the Xunta SIEX app) were not verified.

## 2. Wildfire prevention (Galicia/Spain)

### Takeaway
Detection is well covered by the Xunta: 241 cameras, AI smoke detection in XeoCode, drones, and the new citizen alert app ALume. The weakest link is prevention compliance by landowners. The Xunta's "faixas secundarias" viewer tells an owner, by cadastral reference, whether a parcel must be cleared. But notifications give only 15 days, and nothing guides the owner through who to hire, cost, deadlines, filing an appeal (alegación) or proving compliance. That is a clear agent-shaped gap.

### Cited Findings
- 2025 fires in Galicia burned more than 118,000 ha. Pladiga 2026 adds brigades, cameras, AI and digital tools. — [Ecoticias](https://www.ecoticias.com/medio-ambiente/incendios-en-galicia-pladiga-prevencion); [Pladiga 2026, Medio Rural](https://mediorural.xunta.gal/es/temas/defensa-monte/pladiga-2026)
- ALume is a free Xunta app (Android/iOS) for reporting a fire with geolocation "in three clicks". It launched around June 2026. — [GaliciaE](https://www.galiciae.com/articulo/galicia/galicia-estrena-app-movil-alume-alertar-incendios-incorpora-ia-detectar-focos/20260616140310108166.html); [Telecinco](https://www.telecinco.es/noticias/galicia/20260622/alume-aplicacion-xunta-incendio-forestal-alertar_18_019473397.html); [Noticias Galicia](https://www.noticiasgalicia.com/articulo/galicia/nueva-app-permitira-alertar-incendios-galicia-solo-tres-clics/20260323155710156692.html)
- XeoCode (the internal fire-management app) gets AI detection of smoke and ignition, with automatic alerts followed by human verification. The camera network grows 30% to 241 cameras at 111 points and detects at more than 15 km (up to 25 km in good conditions). Surveillance drones come via a Medio Rural–Abanca agreement. — [Xunta press note](https://www.xunta.gal/es/notas-de-prensa/-/nova/022747/xunta-amplia-los-mecanismos-deteccion-temprana-incendios-forestales-con-una-nueva); [Facenda press note on AI in the fire platform](https://www.conselleriadefacenda.gal/es/-/a-xunta-introduce-o-uso-de-intelixencia-artificial-na-plataforma-tecnoloxica-de-loita-contra-os-incendios-que-e-xa-un-referente-en-espana-e-europa)
- Galicia is betting on AI and satellites against megafires (Jul 2026 coverage). — [Euronews](https://www.euronews.com/next/2026/07/24/spains-galicia-region-bets-big-on-ai-and-satellites-to-prevent-summer-megafires); [Yahoo](https://es-us.noticias.yahoo.com/galicia-apuesta-ia-sat%C3%A9lites-prevenir-123858712.html)
- Spanish startups in the space cover infrared cameras, satellite alarms and "digital shepherds" (GPS-collared goats and sheep for grazing biomass). — [El Referente, 10 fire startups 2025](https://elreferente.es/actualidad/prevencion-extincion-y-reforestacion-10-startups-que-marcan-la-diferencia-en-la-lucha-contra-los-incendios/) (snippet only)
- Dryad (Germany) launched the Gen-4-Pro Silvanet sensor in May 2026. It detects CO, VOCs and particles in the smouldering phase and sends data direct-to-satellite via Kinéis. No Galicia deployment was found. — [Morningstar/BusinessWire](https://www.morningstar.com/news/business-wire/20260510819235/dryad-launches-gen-4-pro-silvanet-wildfire-sensor-setting-new-standard-in-ultra-early-fire-detection); [Dryad](https://www.dryad.net/wildfiresensor)
- Faixas secundarias (Law 3/2007) are 50 m strips around villages and isolated houses. Owners must keep vegetation under 20 cm and remove pyrophytic species. A public Xunta viewer shows affected parcels by cadastral reference, but only in municipalities with an approved municipal prevention plan. The clearing deadline in notifications is 15 calendar days. — [Visor de faixas, mapas.xunta.gal](https://mapas.xunta.gal/es/utilidades-y-publicaciones/actualidad/visor-de-fajas-secundarias); [Valdeorras de Cerca](https://www.valdeorrasdecerca.com/nuevo-sistema-de-gestion-de-biomasa-en-el-entorno-de-las-aldeas-contra-los-incendios-con-un-visor-publico/)
- Municipalities publish their own explainers and alegación templates. This shows owners need hand-holding. — [Catoira, how to check parcels plus appeal template](https://catoira.gal/es/2023/11/29/modelo-de-alegacions-as-notificacions-de-seaga-sobre-xestion-de-biomasa/); [Culleredo](https://www.culleredo.es/es/node/8064); [Barbadás](https://www.barbadas.es/informacion-importante-sobre-a-obrigatoria-limpeza-de-predios-para-previr-incendios/); [Valdoviño](https://www.concellodevaldovino.com/xestion-da-biomasa-nas-faixas-secundarias/)
- The Xunta inspects parcels in the biomass strips, with municipal brigades in support. — [Xunta](https://www.xunta.gal/es/notas-de-prensa/-/nova/80694/xunta-comienza-con-inspeccion-del-estado-gestion-biomasa-las-fajas-secundarias); [Cedeira](https://www.cedeira.gal/a-xunta-esta-a-inspeccionar-as-parcelas-situadas-nas-faixas-de-xestion-de-biomasa-no-municipio-de-cedeira/?lang=es)

### Inferences
- **Strongest white space in this research:** a "¿Teño que rozar a miña leira?" agent. It takes a cadastral reference or a map click and returns:
  - whether the parcel falls in a faixa, and the rule that applies (50 m, <20 cm, species);
  - deadlines and fine risk;
  - a draft alegación, or a request to the concello to do the work;
  - a list of subsidies or cooperatives (e.g. SEAGA or local contractors);
  - a photo check of "cleared vs not cleared" with a vision model.

  It uses public open GIS data, is locally resonant after the 2025 fire season, and competes with no startup found.
- Emigrant or absentee owners (common in Galicia) who inherit parcels are a natural audience. This is inferred, not sourced.

### Gaps
- Could not confirm whether the faixas viewer has an API or WFS layer. Checking mapas.xunta.gal manually is recommended.
- No data found on fine amounts, or on the number of notifications per year.

## 3. Aquaculture / mussels / sea

### Takeaway
R&D is active (CETMAR's BATEAS monitoring raft, Mar Technologies 5.0's AI raft pilot, Pleamar-funded MoMeNTO, red-tide biosensors, ML research on closure prediction). But closures are frequent and sometimes near-total (May 2026). No farmer- or mariscador-facing assistant that consumes INTECMAR closure and oceanographic data was found.

### Cited Findings
- Mar Technologies 5.0 (Mos, Pontevedra) is running the "Mar Span" pilot: a motorised, sensor-equipped raft with a digital twin. An AI algorithm manages 500 ropes remotely so that phytoplankton exposure is even. — [Atlántico, Jan 2025](https://www.atlantico.net/economia/empresa-mos-probara-primera-batea_1_20250112-3358097.html)
- In the Xunta/CETMAR "BATEAS" project (2025), a monitored raft in Arousa tracks water temperature and salinity at depth, weather, and rope weight in real time. — [Xunta](https://www.xunta.gal/es/notas-de-prensa/-/nova/016185/xunta-refuerza-investigacion-sobre-cultivo-mejillon-con-proyecto-bateas); [Galiciapress](https://www.galiciapress.es/articulo/economia/2025-09-01/5412093-proyecto-bateas-xunta-impulsa-investigacion-sobre-cultivo-mejillon-rias-gallegas); [Diario de Arousa](https://www.diariodearousa.com/articulo/vilagarcia/batea-monitorizada-conocer-circunstancias-evoluciona-mejillon-proyecto-xunta-arousa-5412135)
- MoMeNTO is a Pleamar-programme project for real-time monitoring of raft mussel culture, aimed at climate resilience. — [Pleamar](https://www.programapleamar.es/proyectos/momento-monitorizacion-en-tiempo-real-del-cultivo-de-mejillon-en-batea-herramientas-para)
- ITCL, Dominion, the University of Burgos and ANFACO are working on red-tide prediction for mussel areas using biosensors. — [ITCL](https://itcl.es/aparicion-en-prensa/el-sexto-sentido-tecnologico-del-mejillon/)
- A drone plus AI project aims to "save the mussel" in the Ría de Vigo. — [VigoÉ](https://www.vigoe.es/ciencia-y-tecnologia/drones-e-inteligencia-artificial-se-alian-para-salvar-el-mejillon-en-la-ria-de-vigo/)
- May 2026: marine toxins forced the closure of practically all Galician raft polygons. — [Atlántico, 13 May 2026](https://www.atlantico.net/galicia/presencia-toxinas-obliga-cerrar-practicamente_1_20260513-4274587.html); [El Economista](https://www.eleconomista.es/industria/noticias/13918684/05/26/alerta-por-toxinas-en-galicia-cierran-casi-todos-los-poligonos-de-mejillones.html); [Cantabria Económica](https://www.cantabriaeconomica.com/la-economia-hoy/cerrados-todos-los-poligonos-de-bateas-de-galicia-por-la-extension-de-la-marea-roja/)
- Academic ML work exists on predicting precautionary closures caused by lipophilic biotoxins and on HAB (harmful algal bloom) impact in Galicia. — [arXiv 2402.09266](https://arxiv.org/pdf/2402.09266); [arXiv 2402.09271](https://arxiv.org/pdf/2402.09271) (authors and affiliations not verified; fetch blocked)
- INTECMAR monitors oceanography, biotoxins, chemical pollution, microbiology and pathology, and closes zones with toxins. — [EU Civil Protection Knowledge Network](https://civil-protection-knowledge-network.europa.eu/organisations/instituto-tecnoloxico-para-o-control-domedio-marino-de-galicia-intecmar)

### Inferences
- A demo-able gap: an agent that reads the daily INTECMAR polygon status plus oceanographic data. It would answer "¿abre mañá o polígono Arousa C?". It would also estimate the probability of reopening, with a baseline model inspired by the arXiv work, and push alerts via Telegram or WhatsApp to bateeiros, mariscadoras and restaurant buyers.
- Mussel-sector startups found are hardware and R&D-consortium heavy, so a software/data layer is open.

### Gaps
- Not verified: whether INTECMAR publishes closure status in machine-readable form (API or CSV) versus HTML or PDF. This is critical for feasibility and needs checking.
- No sector size figures were captured (number of rafts, tonnes, value) because the fetches were blocked.

## 4. GovTech: subsidies and bureaucracy

### Takeaway
AI subsidy finders are now crowded: FANDIT (with AI assistants and a public API), BuscoAyudas, SubvenIA, Ayudas.ai, IGS, plus consultancies. They target companies and the self-employed. Public administrations are moving too: the national AI assistant for Mi Carpeta Ciudadana is planned for 2027, and the Xunta's GobTec strategy funds AI proofs of concept. The gap is citizen-side, Galician-language, end-to-end "execution" (eligibility check, filled form, document checklist, deadline tracking) for specific high-friction Xunta procedures, rather than another search engine.

### Cited Findings
- FANDIT (Spain) launched AI assistants in April 2025, including a subsidy advisor and a search assistant, built on a vectorised subsidies database. It opened an API so anyone can plug an AI model into its database. It also automates expense-justification reports. — [MuyPymes, Apr 2025](https://www.muypymes.com/2025/04/10/fandit-asistentes-ia-busqueda-gestion-subvenciones); [FANDIT](https://fandit.es/)
- BuscoAyudas is an AI search engine over more than 50,000 BDNS calls. It produces summaries, requirement analysis, difficulty classification and a fit score. — [BuscoAyudas](https://www.buscoayudas.es/)
- SubvenIA monitors the BOE and 18 regional bulletins daily, with AI filtering for the self-employed, SMEs and startups. — [SubvenIA](https://subvenia.net/)
- Other players: Ayudas.ai, and the IGS startup subsidy finder. — [Ayudas.ai](https://ayudas.ai/); [IGS](https://www.institutogestionsubvenciones.com/buscador-subvenciones-startups/)
- The Xunta already runs its own subsidy finder (Portal OVE, buscador-subvencions.xunta.gal). — [Xunta Buscador (IG530B example)](https://buscador-subvencions.xunta.gal/es/detalle-procedemento-iframe?codtram=IG530B&ano=2026&numpub=1&lang=es)
- Spain's government plans an AI assistant in Mi Carpeta Ciudadana during 2027 to guide users through procedures. — [Xataka](https://www.xataka.com/robotica-e-ia/gran-plan-espanol-para-ia-no-va-solo-superordenadores-tambien-quiere-poner-asistente-tu-carpeta-ciudadana)
- Municipal AI chatbots are sold commercially (Useit, Muniverso). — [Useit](https://useit.es/productos/chatbots-ia-agentes-virtuales-ayuntamientos); [Muniverso](https://muniverso.com/ayuntamientos/)
- The Xunta's "Estratexia do Espazo GobTec Galicia" (Jul/Aug 2026): the administration identifies public-interest challenges and tests AI, data, cybersecurity and 5G solutions via proofs of concept and sandboxes. It co-creates with Galician ICT companies, startups, universities and technology centres. — [Consellería de Facenda](https://www.conselleriadefacenda.gal/es/-/a-xunta-incorporara-solucions-innovadoras-baseadas-en-ia-datos-e-5g-para-mellorar-os-servizos-publicos-e-a-relacion-coa-cidadania); [El Progreso](https://www.elprogreso.es/articulo/galicia/xunta-incorporara-ia-datos-5g-optimizar-servicios-publicos-atencion-ciudadana/202608061202361989899.html); [El Ideal Gallego](https://www.elidealgallego.com/galicia/2026-07-16/la-xunta-mejora-los-servicios-publicos-gracias-a-soluciones-con-ia-datos-y-5g-868086.html)

### Inferences
- A generic "subsidy finder" project would look derivative next to FANDIT, BuscoAyudas and SubvenIA. To stand out, a project should:
  - pick one vertical, for example rural landowners (biomass clearing, forestry aid, Banco de Terras), the elderly (dependency, teleassistance), or smallholders (SIEX, PAC);
  - act rather than search: prefill forms, build document checklists and track deadlines;
  - work in Galician (Proxecto Nós resources);
  - possibly consume FANDIT's API for the database layer. That is a smart "integrator" signal to recruiters.
- GobTec's challenge-driven, proof-of-concept model means a demo framed as "a public-interest challenge plus a working sandbox prototype" matches exactly what the Xunta says it wants.

### Gaps
- No pricing or traction found for FANDIT, BuscoAyudas, SubvenIA or Ayudas.ai.
- No named Xunta citizen chatbot or AI assistant for procedures was confirmed for 2026.

## 5. Personal finance for Spanish users (including scam protection for the elderly)

### Takeaway
Aggregation and budgeting (Fintonic and alternatives) and tax filing (TaxDown, which uses AI agents and partners with BBVA) are mature. Anti-fraud is sold to banks (Veridas etc.), not to families. The gap is a family-facing "second opinion" agent for older people: forward a suspicious SMS, call transcript or screenshot and get a verdict plus a script of what to do. Localised to Spanish and Galician scam patterns.

### Cited Findings
- Fintonic reportedly has more than 1.5 million active users (other claims say more than 2 million). It is free, aggregates more than 150 Spanish institutions via PSD2, and is licensed by the Banco de España for account information and payment initiation. — [Fintonic blog](https://www.fintonic.com/blog/fintonic-la-app-que-ha-revolucionado-la-gestion-de-las-finanzas-personales/); [Google Play](https://play.google.com/store/apps/details?id=com.fintonic&hl=en_US) (user figures are self-reported; the sources conflict)
- Fintonic alternatives are listed by Banktrack and others. — [Banktrack](https://banktrack.com/blog/alternativas-fintonic); [Las Finanzas Personales](https://www.lasfinanzaspersonales.org/post/41-apps-finanzas-personales)
- TaxDown: an AI copilot supports every conversation, and about half of the returns under review are first analysed by AI agents (4 hours reduced to 10 minutes). More than 85,000 BBVA customers used it in the last campaign. 33% of them saved an average of €305.40 (€6.2M in total). The CEO's stated goal is "your tax return filing itself". — [El Debate, May 2026](https://www.eldebate.com/tecnologia/20260515/alvaro-falcones-taxdown-gracias-ia-vamos-conseguir-declaracion-renta-haga-sola_417099.html); [BBVA](https://www.bbva.com/es/es/salud-financiera/los-clientes-de-bbva-que-usan-taxdown-ahorra-una-media-de-300-euros-en-la-declaracion-de-la-renta/); [Rankia](https://www.rankia.com/blog/irpf-declaracion-renta/4544898-que-taxdown-como-funciona)
- 2026 bank-scam patterns: SMS that appear in the bank's genuine thread, fake apps, AI-generated fake news and celebrity interviews pushing investment platforms. Older people are singled out as more exposed. — [¡Hola!, May 2026](https://www.hola.com/al-dia/20260512901012/estafas-bancarias-2026-apps-falsas-ia-sms-perfectos/); [EconomíaFinanzas](https://www.economiafinanzas.com/estafas-bancarias-en-espana-operacion-policial-falsas-noticias-con-ia-y-como-proteger-tus-ahorros/); [AEB](https://www.aebanca.es/ciberseguridad/conoce-las-estafas-y-fraudes-financieros-en-la-era-de-la-inteligencia-artificial/)
- Veridas (Spain) sells injection-attack detection and liveness checks, which are B2B identity tools. — [BusinessWire](https://www.businesswire.com/news/home/20250210004671/es)

### Inferences
- Budgeting apps and IRPF optimisation are poor choices for a portfolio project, because they compete directly with well-funded incumbents.
- A "scam shield for grandparents" (a WhatsApp or Telegram agent in Spanish/Galician with an optional family-member escalation) is emotionally strong, easy to demo live, and not covered by the B2C players found.

### Gaps
- No Spanish B2C startup was found that focuses on scam detection for the elderly. Absence was not exhaustively verified.
- Bankin and Finizens were not researched.

## 6. Rural and elderly services

### Takeaway
Companion AI for older people already exists, including a Galician player (Serenia, a UVigo spin-off, more than 16,000 users). Differentiation must therefore come from practical rural errands (procedures, medication, transport, fire-strip notices, scams) rather than companionship alone.

### Cited Findings
- In Galicia, 23.1% of the population is over 65, and 15–20% of older people live alone (the highest share in Spain). 26.7% of the population is rural. About 100,000 older people are lonely. — [GaliciaE on Serenia](https://www.galiciae.com/articulo/galicia/serenia/20251001125758104093.html)
- Serenia is a UVigo spin-off: a conversational AI companion (text or voice) with more than 16,000 users in 15 countries. — [GaliciaE](https://www.galiciae.com/articulo/galicia/serenia/20251001125758104093.html)
- CuidadIA's "ANA" is an AI that phones older people daily. — [Ecosistema Startup](https://ecosistemastartup.com/cuidadia-lanza-ana-la-ia-que-llama-cada-dia-a-los-mayores/)
- The Diputació de València reinvented teleassistance with AI, home visits and a neighbour network. — [Valencia Extra](https://www.valenciaextra.com/es/politica/la-diputacio-de-valencia-reinventa-la-teleasistencia-para-mayores-inteligencia-artificial-visitas-a-domicilio-y-una-red-vecinal-contra-la-soledad_589235_102.html)
- A new teleassistance service is running in Galicia. Rural areas lag in connectivity and digital skills. — [Solidaridad Intergeneracional](https://solidaridadintergeneracional.es/wp/una-nueva-teleasistencia-que-aporta-mas-seguridad-a-las-personas-mayores-en-galicia/); [Sociedad Cinco Uno](https://www.sociedadcincouno.org/2026/07/19/tecnologia-para-personas-mayores-recursos-tendencias-e-innovacion-para-un-envejecimiento-mas-autonomo/)

### Inferences
- Voice-first on a plain phone line or WhatsApp voice notes, in Galician, fits the connectivity and skills constraints.
- Combining this with the fire-strip, subsidy and scam modules gives a single "rural concierge" agent with tool use. That is a stronger agent demo than a companion chatbot.

### Gaps
- Serenia's pricing and business model were not found.

## 7. Innovation programme signals (what funders want solved)

### Takeaway
Galician funders consistently signal:
- AI applied to public services (GobTec proofs of concept and sandboxes);
- AI in industry (IA360);
- RIS3 priorities in agrarian and marine biotechnology, decarbonisation and advanced manufacturing;
- Galician-language AI (Proxecto Nós, with the Carballo LLM built at CiTIUS/CESGA).

Wildfire (Pladiga 2026) and red tides are the most salient public crises of 2025–26.

### Cited Findings
- Galicia's AI strategy is the "Estratexia Galega de IA 2030 – Cara a unha Galicia Intelixente" (AMTEGA). The Galicia Digital 2030 update (Feb 2025) adds about 20 measures, including a Galician data strategy and a regional plan to promote AI. — [AMTEGA IA 2030](https://amtega.xunta.gal/es/evento/estrategia-gallega-de-inteligencia-artificial-2030-hacia-una-galicia-inteligente); [AMTEGA EGD2030](https://amtega.xunta.gal/es/estrategia-galicia-digital-2030); [ESMARTCITY](https://www.esmartcity.es/2025/02/13/actualizacion-estrategia-galicia-digital-2030-amplia-objetivos-conectividad-competencias-digitales)
- GobTec Galicia is a challenge-based model with proofs of concept and sandboxes, built with the ICT ecosystem. — [Facenda](https://www.conselleriadefacenda.gal/es/-/a-xunta-incorporara-solucions-innovadoras-baseadas-en-ia-datos-e-5g-para-mellorar-os-servizos-publicos-e-a-relacion-coa-cidadania)
- GAIN "Industria Innova 2026" (up to €30M; open 17 Jan–17 Mar 2026) is aligned with RIS3 2021-2027 priorities: agrarian and marine biotechnology, decarbonisation, circular economy, energy efficiency and smart manufacturing. — [DOG 16/1/2026](https://www.xunta.gal/dog/Publicados/2026/20260116/AnuncioO92-181225-0003_es.html); [Deducible](https://deducible.es/ayudas-industria-innova-2026-hasta-30-millones-de-euros-para-impulsar-la-innovacion-industrial-en-galicia/)
- GAIN "IA360 2026" funds experimental development and application of AI in Galician industry and its value chain. — [Oficina do Autónomo](https://oficinadoautonomo.gal/es/portfolio/6421)
- IGAPE's 2026 calls cover innovation, digitalisation, internationalisation and startups. — [IPLUS|F](https://www.iplusf.com/convocatoria-igape-2026-subvenciones-para-impulsar-la-innovacion-y-el-crecimiento-empresarial-en-galicia/)
- Proxecto Nós (Xunta, run by CiTIUS and the Instituto da Lingua Galega at USC) produced Carballo, a 1.3B-parameter GPT-style LLM for Galician. It was trained at CESGA on CorpusNós (about 2.1B words). Microsoft collaborates. — [CiTIUS](https://citius.gal/es/news/news/carballo-the-first-large-scale-language-model-in-history-for-galician-is-born-at-usc/); [Xunta/Microsoft](https://www.xunta.gal/es/notas-de-prensa/-/nova/015589/proxecto-nos-situa-galicia-mapa-inteligencia-artificial-europea-mano-microsoft); [nos.gal](https://nos.gal/en/proxecto-nos/about-us)

### Inferences
- A project that uses Proxecto Nós resources (Carballo, or its Galician ASR/TTS if available) for a public-interest challenge touches three funder priorities at once: Galician language, AI in public services, and a rural or marine crisis.

### Gaps
- Not researched: ENIA 2024 specifics, CDTI or Fundación Barrié challenges, Cotec reports, and CORDIS projects.
- Gradiant and CITIC programmes were not covered.
- Xunta innovative public procurement (CPI) challenge lists were not retrieved.

## 8. What Galician recruiters and hackathon judges find memorable

### Takeaway
HackUDC (A Coruña) is Galicia's largest hackathon and emphasises open AI. Recent national AI prizes went to socially framed, locally specific, crisis-oriented projects: AI for coastal wave-surge prevention, and AI for autistic pupils. Local problem plus open AI plus visible social impact is the winning pattern.

### Cited Findings
- HackUDC 2026 is the largest hackathon in Galicia. It promotes open AI among university talent, with strong involvement from Galician tech companies. — [Mancomún](https://mancomun.gal/es/novas/hackudc-2026-se-consolida-como-el-mayor-hackathon-de-galicia-e-impulsa-la-ia-abierta-entre-el-talento-universitario/) (winners not retrieved)
- The winner of the OdiseIA4Good 2026 hackathon was "Aula +", AI that builds pedagogical memory for classrooms with autistic pupils. — [Fundación Pablo VI](https://www.fpablovi.org/noticias/2213-hackathon-2026-la-inteligencia-artificial-al-servicio-de-los-colectivos-mas-vulnerables)
- A project using AI to prevent "golpes de mar" (coastal wave surges) won Samsung's national AI prize. — [Samsung News](https://news.samsung.com/cl/un-proyecto-que-aprovecha-la-ia-para-la-prevencion-de-los-golpes-de-mar-se-alza-con-el-primer-premio-nacional-de-inteligencia-artificial-de-samsung)
- AESIA runs a "responsible and open AI in industry" hackathon. — [digital.gob.es](https://digital.gob.es/en/digitalizacion/comunidad-IA-de-codigo-abierto/eventos-sedia/hackathon-ia-abierta-e-industria-)

### Inferences
- Candidate white-space projects, ranked by novelty, demo-ability and fit with funder signals:
  1. **Faixas/rozas agent for landowners.** Cadastral reference goes in; the output is obligations, deadline, cost estimate, a draft alegación or request to the concello, and a photo compliance check. It uses the Xunta GIS viewer, is in Galician, and no competitor was found.
  2. **Red-tide / polygon reopening assistant for bateeiros and mariscadoras.** It combines INTECMAR data, a closure-probability baseline and WhatsApp alerts. This depends on whether INTECMAR data is machine-readable.
  3. **Rural concierge voice agent for older people** (in Galician), with tools covering scam triage, fire-strip notices, subsidy and dependency procedures, and medication reminders. It differs from Serenia or ANA by acting, not just keeping company.
  4. **Smallholder vine copilot.** It turns Ribeira Sacra/Rías Baixas mildew alerts into an action and logs the treatment in SIEX format. It is voice-first for part-time growers.
- Projects to avoid, because the space is crowded: generic subsidy search engines, budgeting apps, IRPF optimisers, and camera-based fire detection (the Xunta already does it).

### Gaps
- HackUDC 2026 winners and recruiter-side opinions were not retrieved (fetch blocked). No sourced quotes from Galician recruiters were found.
