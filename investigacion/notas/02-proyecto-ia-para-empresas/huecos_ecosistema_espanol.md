# Gaps in the Spanish B2B software ecosystem for a Spain-specific AI agent (as of Sept 2026)

Method note: these notes come from about 20 web searches. Most direct page fetches were blocked by the network egress proxy (hazrevista.org, tendios.com, merca2.es, holded.com, startups-espanolas.es), so many findings rely on search-result snippets and were not read in full. Figures from secondary outlets or vendor blogs are marked as such. Where no reliable source was found, the item is listed under Gaps.

## 1. Public procurement (licitaciones): market size, data, tools, gaps

### Takeaway
Spanish public procurement is very large, about €180bn in 2025, and PLACSP publishes machine-readable daily ATOM/CODICE feeds. Several tools already cover finding tenders and summarizing pliegos (Tendios, Gobierto, LicitaIA, PliegoBot). The less crowded space is an agent that works through the whole bid for an SME: checking solvency against the company's own data, preparing the DEUC/sobres, drafting the memoria técnica, and doing post-award follow-up.

### Cited Findings
- Spanish public procurement reached about €180,700M in 2025. According to OIReScon, the total amount tendered on the procurement platforms was €143,921.76M, up 27.81% year on year. More than 169,700 tenders were run, and volume grew 32% — [Inmodiario](https://inmodiario.com/181/87165/la-contratacion-publica-supera-los-180-000-millones-y-exige-filtrar-mejor-las-licitaciones/); [APTIE](https://aptie.org/noticias-sobre-tendencias/espana-alcanza-los-180-600-millones-en-licitaciones-publicas-pero-deja-desiertos-4-011-millones/) (APTIE reports €180,600M and €4,011M in tenders declared void or unawarded)
- SMEs formalized 67.5% of contracts in 2025. That is a share of the **number** of contracts, not of their value, and I did not find the share of value — [Inmodiario](https://inmodiario.com/181/87165/la-contratacion-publica-supera-los-180-000-millones-y-exige-filtrar-mejor-las-licitaciones/)
- Concentration: "Only 100 companies accounted for 53% of public procurement in 2025" (headline only; the page was blocked) — [Revista Haz](https://hazrevista.org/transparencia/2026/04/solo-100-empresas-concentraron-53-ciento-contratacion-publica-2025/)
- Ayuntamiento de Madrid awarded €2,516M in 2025, and 65.15% of the winning bidders were SMEs, compared with the EU "satisfactory" threshold of 60% — [El Diario de Madrid](https://www.eldiariodemadrid.es/articulo/madrid/madrid-adjudico-2516-millones-contratos-publicos-2025-mas-pymes-concurrencia/20260618141019134460.html)
- PLACSP open data: daily and monthly ATOM syndication in CODICE 2.07 XML. Each ZIP holds .atom files of up to 500 entries each, linked with "next". There are separate datasets for (a) contractor profiles excluding contratos menores, (b) aggregated platforms (regional platforms that republish), and (c) contratos menores — [PLACSP Datos Abiertos](https://contrataciondelsectorpublico.gob.es/wps/portal/DatosAbiertos); [Hacienda](https://www.hacienda.gob.es/es-ES/GobiernoAbierto/Datos%20Abiertos/Paginas/LicitacionesContratante.aspx); [datos.gob.es aggregation dataset](https://datos.gob.es/en/catalogo/e05250001-licitaciones-publicadas-en-la-plataforma-mediante-mecanismos-de-agregacion-excluyendo-los-contratos-menores)
- An academic paper (OBCP) documents problems with access to and reuse of procurement open data — [OBCP PDF](https://obcp.es/sites/default/files/2022-06/Rub%C3%A9n%20Mart%C3%ADnez%20-%20Datos%20abiertos%20en%20el%20%C3%A1mbito%20de%20la%20contrataci%C3%B3n.pdf)
- Third parties already redistribute the PLACSP ZIPs and BDNS data (ContratacionAbierta.com) — [ContratacionAbierta](https://contratacionabierta.com/descargas/)
- **Tendios** (Barcelona, founded 2023 by Xavier Creus and Albert Riera) raised €2M. It has about 30 employees, and its clients include Telefónica, Acciona, SEAT, ADIF, the Ministerio de Defensa and Ford. Its SaaS uses AI to detect opportunities, analyze risk, draft documents and forecast expiries. Its client base leans toward large companies and the public sector — [Computerworld](https://www.computerworld.es/article/3996955/la-startup-espanola-tendios-cierra-una-ronda-de-financiacion-de-dos-millones-de-euros.html); [El Español](https://www.elespanol.com/invertia/disruptores/ecosistema-startup/startups/20250626/startup-quiere-acabar-caos-licitaciones-tecnologia-mejor-antidoto-opacidad/1003743821742_0.html)
- **Gobierto Redactor para empresas** is an AI assistant for writing bids that draws on past offers and private documentation — [Gobierto blog](https://www.gobierto.es/blog/gobierto-redactor-para-empresas-prepara-tus-ofertas-de-licitaciones-con-inteligencia-artificial); [Gobierto help](https://contratos.gobierto.es/ayuda/empresas/redactor/asistente-de-redaccion-con-ia)
- **LicitaIA** searches TED and PLACE by CPV, province and budget. It takes an uploaded pliego PDF and returns a summary of requirements, deadlines and risk clauses — [LicitaIA](https://licitaia.org/)
- **PliegoBot** works on the buyer side: it generates PPT/PCAP documents aligned with the LCSP — [PliegoBot](https://www.pliegobot.com/)
- The public buscador on Plataforma PYME (Ministerio de Industria) already exists — [Plataforma PYME](https://plataformapyme.es/es-es/herramientas-digitales/Paginas/buscador_licitaciones.aspx)
- AlertaLicita (alerts) publishes 2025 statistics — [AlertaLicita](https://alertalicita.com/es/ano-2025-licitaciones-en-cifras/)

### Inferences
- Finding and alerting on tenders, and summarizing pliegos, is becoming commoditized: at least 4 or 5 Spanish players already do it. A new agent needs to go further along the workflow:
  1. Automatic solvency checks. Cross-check the economic solvency (turnover over the last 3 years, from Holded/A3/Sage or the Registro Mercantil accounts) and technical solvency (similar contracts, clasificación empresarial ROLECE) against the pliego, and give a go/no-go decision with reasons.
  2. Pre-filling the DEUC/ESPD and the administrative documentation for sobre A.
  3. Drafting the memoria técnica for sobre B against the evaluation criteria (juicio de valor), with a score simulation.
  4. Economic analysis for sobre C, using historical award data from PLACSP (typical discounts per contracting body/CPV and abnormally low offer thresholds).
  5. Post-award follow-up: guarantees, invoicing through FACe, payment to the SME.
- The concentration figure (100 companies take 53%) against SMEs taking about 67% of contracts by number suggests SMEs win many small contracts but little of the value. That is a plausible argument for tooling aimed at mid-sized tenders.
- Historical award data (winners, discounts, number of bidders) is available as open data, so an "award-probability predictor" is technically feasible.
- Data complexity is itself a moat: CODICE XML, aggregated platforms (Catalonia, Madrid, Basque Country, Andalusia and others publish through aggregation) and contratos menores in a separate dataset.

### Gaps
- I found no reliable source for the % of Spanish SMEs that actually **bid**; there is only the share of contracts they win. The EU Single Market Scoreboard has related indicators, but I could not verify them.
- Average number of bidders per tender in 2025 (OIReScon publishes it in its annual report; not verified).
- Vortal, Doc2Tender and "Tenders.ai"-type tools: no Spain-specific evidence found. Vortal is best known as a Portuguese e-procurement platform. Pricing for Tendios, LicitaIA and Gobierto was not found.
- I could not verify whether any tool generates the complete DEUC or checks ROLECE automatically.

## 2. Grants and financing (CDTI, ENISA, NextGen/PERTE, Kit Digital, Kit Consulting)

### Takeaway
Grant search is already served (FANDIT, and many consultancies), and the BDNS has a public REST API with no authentication. The gap is an agent that drafts technical reports (memorias técnicas) and budgets for CDTI/NEOTEC/regional calls and supports justification afterwards. Granter, a Portuguese company that won at South Summit Madrid 2026, is already moving into that space, which both validates the idea and means there is a competitor.

### Cited Findings
- In 2026 there are more than 15 active grant programs for digitalization and AI, ranging from €2,000 (Kit Digital) to over €1M (CDTI). The list includes Kit Consulting (up to €24,000), CDTI (from €175,000), ENISA (participative loans of €25,000–300,000) and NEOTEC (up to €250,000) — [Hiberus Booster](https://www.hiberusbooster.com/guias/subvenciones-digitalizacion-ia/); [Upliora](https://www.upliora.es/blog/ayudas-subvenciones-ia-pymes-espana-2026) (secondary guides)
- "The hardest part of these calls is not applying for the aid, it is writing a good memoria técnica and then delivering the project on time" — [Hiberus Booster](https://www.hiberusbooster.com/guias/subvenciones-digitalizacion-ia/) (consultancy opinion)
- Kit Digital: the last two calls closed at the end of October 2025. More than 10,700 agentes digitalizadores were registered, and the justification phase is still running — [Red.es](https://www.red.es/es/actualidad/noticias/kit-digital-cierra-las-dos-ultimas-convocatorias-que-quedaban-abiertas-tras-mas); [Acelera pyme](https://www.acelerapyme.gob.es/en/kit-digital)
- Kit Consulting: according to a consultancy, Orden TDF/39/2026 removes the program's closing date and requires unspent funds to be reinvested, but new applications had not opened as of August 2026 — [Proment Consulting](https://promentconsulting.com/2026/08/24/kit-consulting-2026-nueva-convocatoria-fondos-remanentes/) (secondary; not verified in the BOE)
- An IA 2026 aid program call was published — [Iberley](https://www.iberley.es/subvenciones/convocatoria-programa-ayudas-inteligencia-artificial-2026-27214364); IDAE INNOVAE 2026 offers €115M — [Ecosistema Startup](https://ecosistemastartup.com/idae-innovae-2026-115me-para-startups-de-automatizacion-energetica/)
- **BDNS/SNPSAP**: reformed in autumn 2023 to provide a REST API returning JSON, documented in Swagger, with no authentication and no published limits. It has 29 endpoints covering deadlines, budgets, beneficiary types, sectors, regions, EU funds and regulatory bases — [datos.gob.es BDNS](https://datos.gob.es/en/catalogo/e05250001-base-de-datos-nacional-de-subvenciones); [infosubvenciones Swagger](https://www.infosubvenciones.es/bdnstrans/doc/swagger); client libraries: [bdns-fetch (GitHub)](https://github.com/cruzlorite/bdns-fetch), [Apify actor](https://apify.com/albydev/bdns-subvenciones-espana)
- **FANDIT** (Spain) is a grant database with a search engine, a "Radar", alerts and, since April 2025, 3 AI assistants built on its vectorized database, including a "subsidy advisor" — [MuyPymes](https://www.muypymes.com/2025/04/10/fandit-asistentes-ia-busqueda-gestion-subvenciones); [El Referente](https://elreferente.es/entrevistas/fandit-simplifica-subvenciones/)
- **Granter** (Portugal) covers the full grant cycle with AI: search, requirement checks, **drafting applications** and post-award management. It claims more than 3,000 companies, €21.3M in grants processed and a 73% cut in preparation time. It won the Fintech & Insurtech vertical at South Summit Madrid 2026 — [TodoStartups](https://www.todostartups.com/3/187222/startup-granter-ganadora-vertical-fintech-insurtech-south-summit-madrid-2026); [The Officer](https://theofficer.es/granter-simplifica-el-acceso-a-subvenciones/)

### Inferences
- Search (the BDNS API plus alerts) offers little differentiation. Novelty and value lie in:
  (a) An agent that reads the company's real data (Holded/A3: headcount, turnover, R&D spend) and calculates eligibility and the eligible budget.
  (b) Drafting a memoria técnica structured to the call's scoring criteria (CDTI PID, NEOTEC, regional calls).
  (c) Justification: gathering invoices and payment proofs from the ERP and the bank, and building the cuenta justificativa. This is painful and poorly served. Kit Digital justification is still active and involves more than 10,700 agents.
  (d) Linking grants and tenders, since BDNS and PLACSP both come from Hacienda and are both open.
- Granter's award at a Spanish event suggests Spanish investors and juries value "grants plus AI drafting". A Spanish product would compete with it.

### Gaps
- I did not verify whether CDTI or ENISA publish their calls or awards in a separate machine-readable format beyond BDNS.
- No data was found on the success rate of NEOTEC/CDTI applications or the cost of grant consultancies (success fees are usually 8–15%, but I have no source).
- The current status of PERTE/NextGen in 2026 (the RRF ends in 2026) was not verified.

## 3. Integration with Spanish SME software APIs (Holded, Factorial, Sage/A3, bank data, AEAT, eInforma)

### Takeaway
Holded now has an official API v2 and a remote MCP server (OAuth 2.1), and Factorial is reachable via Apideck's unified MCP. Connecting an agent to Spanish SME software is therefore less of a barrier than it was, which also means "just connecting to Holded" is no longer a differentiator. Value comes from agents that combine several Spanish sources (ERP + bank + AEAT + BORME + PLACSP/BDNS) with knowledge of Spanish rules. VeriFactu has been postponed to 2027, and that deadline is a compliance trigger.

### Cited Findings
- Holded offers a remote MCP server (OAuth 2.1 over Streamable HTTP) that lets AI assistants work with invoicing, accounting, contacts, products, treasury, HR and time tracking. It also provides a REST API, webhooks and official SDKs in TS, Python, Go and PHP — [Holded developers MCP](https://www.holded.com/developers/mcp) (via search snippet; fetch blocked); third-party guides to API v2 and its limits: [ceroone](https://ceroone.com/2026/07/28/api-holded-v2-mcp-limites/), [francodesystems](https://francodesystems.com/holded-api-v2)
- There is a community MCP server for Holded — [nubiia-dev/mcp-holded](https://github.com/nubiia-dev/mcp-holded); unified APIs for Holded — [Apideck](https://www.apideck.com/integrations/holded), [Unified.to](https://unified.to/integrations/holded)
- Factorial is reachable through Apideck's MCP server — [Apideck Factorial MCP](https://www.apideck.com/mcp-server/factorialhr)
- VeriFactu: RDL 15/2025 (BOE of 3 Dec 2025) postponed it to 1 Jan 2027 for companies subject to Corporate Income Tax and to 1 Jul 2027 for the self-employed. Software producers had to adapt by 29 Jul 2025 — [Grupo Albatros](https://grupoalbatros.org/2026/02/23/verifactu-aplazamiento-2027-rdl-15-2025/); [verifactu.com](https://www.verifactu.com/el-nuevo-calendario-de-verifactu-guia-tras-el-aplazamiento-a-2027/); [KPMG tax alert](https://assets.kpmg.com/content/dam/kpmgsites/es/pdf/2025/09/tax-alert-verifactu-calendario-adaptacion-sistemas-facturacion-23580700-4.pdf.coredownload.inline.pdf)
- eInforma offers an API for Companies with developer documentation — [developers.einforma.com](https://developers.einforma.com/); [eInforma API](https://www.einforma.com/api). Axesor (Experian group) sells company reports — [Axesor](https://www.axesor.es/informes-empresas.aspx)
- CaixaBank has a PSD2 API Store (payment initiation and account consent) — [CaixaBank API Store](https://www.caixabank.es/empresa/bancadistancia/api-store.html)

### Inferences
- An ERP connector can be built in days because of MCP. The defensible parts are Spanish domain logic (modelos 303/111/115/347/349, SII, VeriFactu, IRPF withholdings, the 60-day payment rule) and cross-referencing data sources.
- A3 (Wolters Kluwer) and Sage (Sage 50/200, Contasol) are mostly on-premise or desktop at gestorías. That is likely a real gap: agents for gestorías that sit on top of A3/Sage through exports or files. This is not verified with sources.
- The gap between VeriFactu arriving in 2027 and billing software already being adapted suggests an opportunity in auditing or migrating invoicing records rather than in issuing invoices.

### Gaps
- Public API details for A3 (Wolters Kluwer a3innuva API), Sage Active/Sage 200 and Contasol were not verified. Contasol appears to have no public API (unconfirmed).
- Enable Banking pricing and coverage for Spain were not found (the search returned nothing specific).
- No verified information on AEAT web services beyond VeriFactu/SII (for example the DEH/NEO notifications API, or sending tax returns through a colaborador social).
- CNMV open data was not investigated because of limited time.

## 4. BORME / Registro Mercantil as B2B intelligence

### Takeaway
The BOE exposes BORME through an open-data API. LibreBOR offers a JSON API with alerts, bormeparser is open source, and bormeapi.com normalizes BORME-A in English. Using BORME events as sales triggers (new companies, capital increases, appointments, insolvency) is technically easy and partly served. There is little evidence that anyone offers an agent that turns those events into actions in a CRM or into credit risk decisions for SMEs.

### Cited Findings
- The BOE publishes BORME through an open-data API listed on datos.gob.es — [datos.gob.es BORME API](https://datos.gob.es/en/catalogo/ea0040819-diario-oficial-borme/resource/50c83bd5-2034-4145-a12a-92d62790ddd0)
- **bormeparser** is an open-source Python parser for BORME — [GitHub](https://github.com/PabloCastellano/bormeparser); **LibreBOR** began in 2014 as a university degree project. It parses BORME every morning and offers a JSON REST API over HTTPS, plus alerts: an email whenever a monitored company appears in the supported bulletins, also available through the API. It returned from 5 years in maintenance mode with a new version — [LibreBOR docs](https://docs.librebor.me/); [alerts](https://docs.librebor.me/tutorial/alerts/); [Medium](https://libreborme.medium.com/nueva-versi%C3%B3n-de-librebor-bfe3cd7fbd02)
- **bormeapi.com** offers BORME-A company notices normalized in English (appointments, capital changes, insolvency) — [bormeapi.com](https://bormeapi.com/)
- Axesor (Experian) has a large repository of companies, positions, directors and links — [datos.gob.es Axesor](https://datos.gob.es/en/companies/axesor); eInforma offers an API — [eInforma](https://www.einforma.com/api)

### Inferences
- The raw data layer is solved and cheap. A possible gap is a BORME trigger agent: daily events → ICP filter (CNAE, province, capital) → enrichment (eInforma/web) → personalized email or CRM task. Examples: "new SL in your sector → offer an accounting service"; "capital increase → offer financing or software"; "director change → new decision-maker"; "concurso → cut credit to that customer". This is useful for gestorías, banks, B2B SaaS and suppliers.
- It could be combined with PLACSP (awarded companies = companies with cash flow and a need for guarantees or financing) and BDNS (companies that received grants).

### Gaps
- I found no specific Spanish startup that sells "BORME-triggered sales automation" with AI. Infocif/Informa/Axesor offer monitoring but I could not verify whether they have agent or CRM automation features.
- LibreBOR pricing and bormeapi.com pricing and ownership were not verified.

## 5. Collections, morosidad and cash-flow forecasting for pymes

### Takeaway
The pain is well documented and quantified: an 80.5-day average payment period against a legal limit of 60, only 30.4% of invoices paid on time, and an estimated financial cost of about €1,957M for SMEs. I found no clearly funded Spanish startup focused on AI collection agents for SMEs connected to Holded/A3. Content and consultancy pieces about "AI collection agents" exist, which points to demand without a dominant product.

### Cited Findings
- CEPYME Morosidad Observatory: the average payment period was 80.5 days in 2025, above the legal maximum of 60. For SMEs it was 78.3 days in Q4 2025, compared with 79.2 in Q4 2024. Only 30.4% of invoices were paid on time, down from 32.6% in 2024. Construction is the worst sector at 96.5 days — [CEPYME Observatorio II S 2025](https://cepyme.es/observatorio-de-morosidad-ii-semestre-2025/); [El Diario de Madrid](https://www.eldiariodemadrid.es/articulo/economia/morosidad-empresas-espana-2025-pmp-supera-limite-legal-repunta-morosidad/20260410161618127037.html)
- The financial effort from trade debt was €1,957M for SMEs in Q4 2025, down from €2,284M in Q4 2024 — [Forbes España](https://forbes.es/economia/901516/el-coste-financiero-de-las-pymes-derivado-de-la-morosidad-baja-hasta-los-1-957-millones-a-cierre-de-2025/)
- A consultancy guide says AI collection agents cut defaults by 20–45% and DSO by 8–20 days in a medium-sized Spanish company. Implementation costs are €40k–120k, running costs €1.5k–6k per month, and payback 6–12 months. These are **consultancy estimates without disclosed methodology** — [Hiberus Booster](https://www.hiberusbooster.com/guias/automatizar-cobros-morosidad-ia/)
- Santander's Innovation Challenge picked 12 AI projects from 3,401 employee ideas. At least 5 are domain-specific agents, including one for **cash flow** — [Ecosistema Startup](https://ecosistemastartup.com/santander-escoge-12-proyectos-ia-de-3-401-ideas-de-empleados/)

### Inferences
- The €40k–120k implementation cost that consultancies quote suggests the micro-pyme and small-pyme segment is not served. That points to a pre-built agent plugged into Holded/Contasol that:
  (a) prioritizes debtors by risk, using BORME concurso notices and eInforma;
  (b) sends reminders by email or WhatsApp in Spanish or Catalan;
  (c) generates a burofax, a monitorio claim or a requerimiento with the legal wording;
  (d) forecasts 13-week treasury from the ERP and bank data.
- The Ley 3/2004 legal angle (60 days, late-payment interest, the new Ley de Creación y Crecimiento de Empresas sanctioning regime and the requirement for e-invoicing between companies) adds Spanish-specific content that generic tools such as Chaser, Upflow or Kolecto do not have.

### Gaps
- I did not confirm the specific functionality in Spain of Qonto, Payhawk, Kolecto or Invoinet for collections or forecasting (no searches returned verifiable data).
- I found no Spanish startup funded in 2025–2026 specifically for AI collections.
- The date B2B e-invoicing becomes mandatory (Ley Crea y Crece, pending regulation) was not verified in this session.

## 6. Spanish AI-agent startups funded in 2025–2026 and investor interest

### Takeaway
There is strong evidence of VC interest in AI agents in Spain. Record funding in H1 2025 was driven by AI, and Tendios (procurement) raised €2M. Much of the "AI agents for SMEs" coverage in Spanish media is about foreign companies (Naïve, Lassie), so there is room for local vertical players. Several aggregated figures come from low-quality sites and need verification.

### Cited Findings
- Spanish startups raised a record €1,950M in H1 2025, with AI as the main driver — reported in the context of [Computerworld/Tendios](https://www.computerworld.es/article/3996955/la-startup-espanola-tendios-cierra-una-ronda-de-financiacion-de-dos-millones-de-euros.html) (search snippet)
- Tendios raised €2M (see Section 1) — [Computerworld](https://www.computerworld.es/article/3996955/la-startup-espanola-tendios-cierra-una-ronda-de-financiacion-de-dos-millones-de-euros.html)
- Konvo AI raised a €3.5M seed (Sept 2025) and Nilo raised €4M led by Supercell (Sept 2025). Neither is B2B back-office — [Startups Oasis](https://startupsoasis.substack.com/p/22-10-startups-espanolas-de-ia-revolucionando) (newsletter; snippet)
- Vidext (Spanish, AI video) raised €8M, with clients including Iberdrola and CAF (Aug 2026) — [Merca2](https://www.merca2.es/2026/08/23/vidext-ronda-startup-espanola-ia-2441003/)
- Factorial raised €10M, which appears in a newsletter headline — [Ecotechers](https://www.ecotechers.com/p/batalla-rondas-pre-semilla-millones-factorial-ia-eu-inc) (context not verified)
- Naïve, with $28.5M Series A led by Nexus, YC and others, is **not Spanish** (Palo Alto, Berkeley founders) but got wide coverage in Spanish media — [Dealroom](https://dealroom.co/news/143604-na-ve-raises-28-5m-series-a-to-let-ai-agents-run-companies/); [Goodwin](https://www.goodwinlaw.com/en/news-and-events/news/2026/08/announcement-technology-goodwin-advises-naive-28-5-million-series-a)
- Lassie raised €35M (a16z), presented in Spanish media as "AI agents for SMEs are VC's next big bet" — [Merca2](https://www.merca2.es/2026/06/04/lassie-financiacion-startups-ia-2389800/) (not verified whether it is Spanish; probably not)
- Aggregated claims such as "the Spanish AI ecosystem raised €420M in 2025–26 (+85%)" and "average Series A €8.5M" come from low-quality blogs and should not be used without checking — [Javadex](https://www.javadex.es/blog/startups-ia-espanolas-mejores-rompiendo-2026)
- Anthropic opened an office in Madrid (Sept 2026) and names Santander, CaixaBank, BBVA, Telefónica, Konecta, Amadeus, Ferrovial and Indra as clients. It says Spain adopts Claude 2.7 times more than its size would predict — [WWWhatsnew](https://wwwhatsnew.com/2026/09/22/anthropic-oficina-madrid-primera-espana-claude-2026/); [Consumidor Global](https://www.consumidorglobal.com/tecnologia/anthropic-ensena-sus-cartas-en-espana-con-santander-caixabank-telefonica-entre-sus-clientes_20483_102.html)
- El Referente keeps a list of 15 Spanish fintechs "redefining finance" — [El Referente](https://elreferente.es/startups/15-startups-espanolas-que-estan-redefiniendo-el-futuro-de-las-finanzas/)

### Inferences
- Investors are rewarding vertical agents with measurable ROI and enterprise clients (Tendios: Telefónica, Acciona). A proposal that shows hours saved per tender or grant, or DSO reduced, fits that pattern.
- Anthropic's Madrid office and large Spanish enterprise adoption make it a good time to present a Spain-specific agent that uses MCP (Holded MCP plus custom MCP servers for PLACSP, BDNS and BORME).

### Gaps
- There is no reliable consolidated list of Spanish AI agent startups funded in 2025–2026 in back-office, legal or fiscal. Pages at startups-espanolas.es were blocked or are low quality. Sifted and El Referente should be checked directly.
- Amounts and dates for Spanish gestoría or fiscal AI players were not verified.

## 7. Spanish hackathons and challenges sponsored by companies

### Takeaway
There are public and corporate challenges with a B2B or SME angle: the AESIA/Ministerio hackathon on responsible AI for industry and SMEs (May 2026), Santander's internal challenge with finance agents, AI Tinkerers Barcelona (structured finance) and PTE Disruptive challenges. I found no verified open challenges from Holded, Factorial, Inditex, Mercadona Tech, Glovo, Cabify or Idealista in 2026.

### Cited Findings
- AESIA and the Open AI Community (Ministerio para la Transformación Digital) held the Responsible and Open AI Hackathon in Industry (May 2026). It focused on real challenges from industry and SMEs, with "viable, demonstrable and reusable" solutions — per search summary; source: [WWWhatsnew/related results](https://wwwhatsnew.com/2026/09/22/anthropic-oficina-madrid-primera-espana-claude-2026/) (the original AESIA source was not located)
- Santander Innovation Challenge: 12 AI projects chosen from 3,401 ideas, including agents for corporate CRM, wealth management, cash flow, risk and product design (internal, employees) — [Ecosistema Startup](https://ecosistemastartup.com/santander-escoge-12-proyectos-ia-de-3-401-ideas-de-empleados/)
- AI Tinkerers Barcelona: Structured Finance Hackathon 2026 — [AI Tinkerers](https://barcelona.aitinkerers.org/p/structured-finance-hackathon-2026)
- ESIC and BBVA hackathon on sustainability for young professionals — [ESIC](https://www.esic.edu/noticias/esic-y-bbva-impulsan-la-sostenibilidad-en-un-hackathon-para-jovenes-profesionales)
- PTE Disruptive (technology platform) publishes talent challenges — [PTE Disruptive retos](https://ptedisruptive.es/talento/retos/)
- South Summit Madrid 2026 has vertical competitions (Granter won Fintech & Insurtech) — [TodoStartups](https://www.todostartups.com/3/187222/startup-granter-ganadora-vertical-fintech-insurtech-south-summit-madrid-2026)

### Inferences
- The most accessible routes to visibility appear to be South Summit and 4YFN verticals, AI Tinkerers, AESIA/Ministerio hackathons and corporate open-innovation programs (BBVA Open Innovation, Telefónica Open Future/Wayra). The corporate programs are not verified in this session.

### Gaps
- Specific 2026 challenges from Holded, Factorial, Inditex, Mercadona Tech, Glovo, Cabify or Idealista were not found.
- The original AESIA source for the May 2026 hackathon could not be fetched.

## Summary of white spaces (synthesis, not independent evidence)
1. **End-to-end SME bid agent**: solvency check against the ERP and Registro Mercantil, DEUC, a memoria técnica written to the scoring criteria, and a discount recommendation based on PLACSP history. Data: PLACSP ATOM/CODICE (open), TED. Competitors: Tendios (enterprise), Gobierto, LicitaIA.
2. **Grant agent covering drafting and justification**: BDNS API (open, no auth) plus ERP data, with a focus on the justification phase. Competitors: FANDIT (search), Granter (PT, drafting).
3. **Collections and treasury agent for micro-pymes**: Holded MCP plus PSD2 banking plus BORME concurso notices plus Spanish legal templates (burofax, monitorio). Pain: 80.5 days average payment period and only 30.4% of invoices paid on time.
4. **BORME trigger agent for B2B sales and credit risk**: LibreBOR/BOE API plus eInforma plus CRM.
5. **Compliance copilot for gestorías on A3/Sage/Contasol**: VeriFactu in 2027 and Spanish tax modelos. Evidence for this one is weak; it needs further research.
