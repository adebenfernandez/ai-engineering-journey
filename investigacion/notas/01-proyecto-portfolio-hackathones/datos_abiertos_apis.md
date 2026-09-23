# Open data sources and public APIs in Spain, Galicia and the EU for AI projects (state as of September 2026)

Method note: about 25 web searches, run on 2026-09-23. Anything under "Cited Findings" comes from a linked source, though many links are search-result summaries of official pages rather than full-page reads. Anything under "Inferences" marked (prior knowledge, unverified) comes from background knowledge and needs checking against the official docs before use.

## Weather/climate: AEMET OpenData, MeteoGalicia, Open-Meteo

### Takeaway
Open-Meteo is the quickest option for a demo: no key, JSON, and a generous free tier, but it is for non-commercial use only and needs CC BY 4.0 attribution. AEMET is the official Spanish source. It needs a free key sent by email, uses a two-step call pattern, and has a limit of about 40–50 requests per minute, so it should be cached server-side. MeteoGalicia is the best source for Galicia at high resolution: WRF 4 km/12 km and SWAN/MOHID ocean models through THREDDS (NetCDF/GRIB), plus JSON/RSS station services.

### Cited Findings
- AEMET OpenData is a REST API. The free API key is requested with an email address at opendata.aemet.es. — [AEMET OpenData](https://opendata.aemet.es/centrodedescargas/info); [datos.gob.es blog on public APIs](https://datos.gob.es/en/blog/apis-public-administrations-which-ones-are-there-and-how-use-them)
- AEMET uses a two-call pattern. The first request returns JSON whose `datos` field holds a temporary URL, and a second request to that URL returns the actual data. Both calls count toward the rate limit. — [AEMET FAQ PDF](https://opendata.aemet.es/centrodedescargas/docs/FAQs150217.pdf); [Roaming Workshop tutorial](https://theroamingworkshop.cloud/b/en/1357/using-the-open-data-api-aemet-opendata/)
- Sources disagree on the AEMET rate limit: some say 50 requests per minute, others 40 per minute per user, with possible extra per-resource limits. A GitHub project hit these limits and had to decouple AEMET calls from user requests using a cache. — [AEMET FAQ](https://opendata.aemet.es/centrodedescargas/docs/FAQs150217.pdf); [dia-gachas issue #22](https://github.com/danilopgon/dia-gachas/issues/22)
- MeteoGalicia runs a THREDDS server (thredds.meteogalicia.gal; mandeo.meteogalicia.es/thredds). It serves operational numerical-model output in NetCDF, GRIB and HDF, including WRF at 4 km and 12 km, a historical WRF archive, and the SWAN (waves) and MOHID (ocean) models. — [THREDDS MeteoGalicia](https://thredds.meteogalicia.gal/); [WRF 4km catalog](https://mandeo.meteogalicia.es/thredds/catalog/modelos/wrf/rawoutput/wrf_4km/catalog.html); [datos.gob.es entry](https://datos.gob.es/en/catalogo/a12002994-servidor-thredds-de-meteogalicia); [SWAN/MOHID update note](https://www.meteogalicia.gal/datosred/infoweb/numerico/thredds/actualizacionThredds_20130129_gl.pdf)
- MeteoGalicia also offers JSON/RSS web services, for example daily data from weather stations. Community clients exist: the Python `meteoGalicia-api` package, and MeteoMapGal, a real-time map built on 100+ stations. — [JSON daily station service doc](https://www.meteogalicia.gal/datosred/infoweb/meteo/docs/rss/JSON_EstacionsDiarios_es.pdf); [meteogalicia-api](https://github.com/Danieldiazi/meteogalicia-api); [MeteoMapGal](https://github.com/Bateas/MeteoMapGal)
- Open-Meteo free tier: fewer than 10,000 calls per day, 5,000 per hour and 600 per minute. No key is needed. It is non-commercial only (for example, no sites with subscriptions or ads), and data is licensed CC BY 4.0. Paid plans cover commercial use. — [Open-Meteo Terms](https://open-meteo.com/en/terms); [Licence](https://open-meteo.com/en/licence); [Pricing](https://open-meteo.com/en/pricing)

### Inferences
- For a hackathon, use Open-Meteo for forecasts and historical/ERA5 data because there is no key and one call does the job. Add AEMET or MeteoGalicia when you need official station observations or warnings, which also gives the project an "official source" story.
- AEMET's two-step pattern, and its temporary URLs that sometimes fail, call for retry logic and a local cache. Reports of intermittent 429 and 5xx errors are common in community forums (prior knowledge, unverified).
- AEMET data licensing: reuse is allowed with attribution under the AEMET legal notice (prior knowledge, unverified).

### Gaps
- I could not confirm whether MeteoGalicia's REST/RSS services need a key in 2026, or what their rate limits are. MeteoGalicia's current WMS endpoints were not checked.

## Earth observation: Copernicus Data Space Ecosystem, EFFIS, NASA FIRMS, Copernicus Land/Emergency

### Takeaway
CDSE provides free Sentinel-1/2 data and processing: Sentinel Hub APIs within a free-tier quota and openEO with 10,000 credits per month, after free registration. It is well suited to crop, NDVI or burn-scar projects. NASA FIRMS is the simplest wildfire API: a free MAP_KEY with 5,000 transactions per 10 minutes, returning CSV. EFFIS provides free WMS/OWS layers (fire danger, hotspots, burnt areas of 30 ha or more). Historical extracts require a request form.

### Cited Findings
- All CDSE functions are free for general users within predefined quotas. Large-scale download or processing falls under commercial terms. — [CDSE](https://dataspace.copernicus.eu/)
- Each free-tier user gets 40,000 processing units (Sentinel Hub) plus 10,000 openEO credits. CDSE recommends the platform for hackathons. — [CDSE hackathon news](https://dataspace.copernicus.eu/news/2024-12-9-how-and-why-use-copernicus-data-space-ecosystem-hackathons)
- Every CDSE user receives 10,000 free openEO credits per month. Copernicus Service/Collaborative Ground Segment users get 20,000 per month. More credits can be bought through CREODIAS. — [openEO CDSE](https://dataspace.copernicus.eu/ecosystem/services/openeo); [Credit usage docs](https://documentation.dataspace.copernicus.eu/APIs/openEO/credit_usage.html)
- Pitfall: forum users report running out of free openEO credits unexpectedly. Credit cost depends on the CPU, memory and time a job uses, so it is not always predictable. — [CDSE forum thread](https://forum.dataspace.copernicus.eu/t/clarification-on-openeo-free-tier-credit-calculation-unexpected-quota-exhaustion/5037)
- Sentinel Hub on CDSE is free within the user quota. Beyond it, commercial Sentinel Hub on CREODIAS is available. — [Sentinel Hub CDSE](https://dataspace.copernicus.eu/ecosystem/services/sentinel-hub)
- NASA FIRMS: a free MAP_KEY allows 5,000 transactions per 10-minute window. Large requests, such as 7 days of data, count as several transactions. The limit resets after 10 minutes, and higher limits can be requested. It offers Area, Country and Data-availability APIs with MODIS, VIIRS (S-NPP, NOAA-20, NOAA-21) and Landsat detections. — [FIRMS MAP_KEY](https://firms.modaps.eosdis.nasa.gov/usfs/api/map_key/); [FIRMS Area API](https://firms.modaps.eosdis.nasa.gov/api/area/); [FIRMS Python tutorial](https://firms.modaps.eosdis.nasa.gov/content/academy/data_api/firms_api_use.html)
- EFFIS: data are freely accessible, mostly through a WMS/OWS server, and the data-and-services page gives sample URLs. The Current Situation viewer shows fire danger forecasts up to 6 days ahead, daily hotspots and fire perimeters. Burnt-area layers cover the last 7 days and the season to date. Only burnt areas of about 30 ha or more are mapped. Historical or raw perimeters require a data request form. — [EFFIS data and services](https://forest-fire.emergency.copernicus.eu/applications/data-and-services); [EFFIS applications](https://forest-fire.emergency.copernicus.eu/applications); [EFFIS downloads instructions](https://forest-fire.emergency.copernicus.eu/downloads-instructions)
- The EFFIS fire-events database is also published as a JRC dataset on data.europa.eu. — [data.europa.eu JRC fire events](https://data.europa.eu/doi/10.2905/JRC.AJKEPV8)

### Inferences
- Python clients: `sentinelhub-py`, `openeo`, and STAC/OData catalog search on CDSE (prior knowledge, unverified for 2026 endpoints). Sentinel-2 revisit is about 5 days, and clouds over Galicia are a major practical problem for optical imagery. Sentinel-1 SAR avoids clouds.
- EFFIS's 30 ha threshold means small Galician fires, which are very frequent, will be missing. For small-fire detection, combine FIRMS hotspots with Sentinel-2 dNBR.
- Copernicus Land Monitoring Service (CORINE, HR layers) and Copernicus Emergency Management Service (rapid mapping activations) are free downloads after registration (prior knowledge, unverified in this session).

### Gaps
- I did not verify the current CDSE Sentinel Hub per-minute request limits, EFFIS WFS availability (vs WMS only), or the CLMS/CEMS access methods for 2026.

## Agriculture/land: SIGPAC, Catastro, MAPA, IGN/CNIG, Banco de Terras, SIAR

### Takeaway
SIGPAC now has cloud services at sigpac-hubcloud.es: WMS, OGC API Features (WGS84 GeoJSON for parcels, declared crops and landscape elements), vector tiles and an ATOM bulk download. These make it realistic for a hackathon. Catastro's INSPIRE WFS is free with no key, but each query is capped at 1 km² and 5,000 parcels, and the data is refreshed twice a year.

### Cited Findings
- FEGA offers SIGPAC cloud services: WMS (ISO 19128), OGC API Features for parcel (recinto), declared crop and landscape element layers in WGS84, a code-list service, a query service, a graphic-output service, vector tiles, and an ATOM download service. The declared-crop data is from the previous campaign. — [FEGA SIGPAC Nube](https://www.fega.gob.es/es/pepac-2023-2027/sistemas-gestion-y-control/sigpac/nube-de-sigpac); [SIGPAC service catalog](https://sigpac-hubcloud.es/); [OGC API](https://sigpac-hubcloud.es/ogcapi?f=html); [FEGA news](https://www.fega.gob.es/es/noticias/node-16528); [Agrodigital, Sep 2025](https://agrodigital.info/2025/09/26/servicios-nube-sigpac-fega/)
- SIGPAC ATOM bulk download: https://www.fega.gob.es/atom/es.fega.sigpac.xml — [FEGA SIGPAC Nube](https://www.fega.gob.es/es/pepac-2023-2027/sistemas-gestion-y-control/sigpac/nube-de-sigpac)
- MAPA keeps a directory of agriculture spatial services. — [MAPA IDE directory](https://www.mapa.gob.es/es/cartografia-y-sig/ide/directorio_datos_servicios/agricultura)
- Catastro INSPIRE: WFS 2.0 at http://ovc.catastro.meh.es/INSPIRE/wfsCP.aspx, queried only through StoredQueries (no SQL). CadastralParcel requests are limited to 1 km² and 5,000 features, and CadastralZoning to 25 km² and 500 features. There are also Addresses (wfsAD) and Buildings WFS services. Complete downloads by municipality come through ATOM, updated twice a year. — [Catastro INSPIRE](https://www.catastro.hacienda.gob.es/webinspire/index.html); [CP WFS doc](https://www.catastro.hacienda.gob.es/webinspire/documentos/inspire-cp-WFS.pdf); [IDEE presentation](https://www.idee.es/resources/presentaciones/JIIDE15/20151104/16_ServiciosINSPIRE_D.GCatastro.pdf); [gmlcatastral.es guide](https://gmlcatastral.es/recursos/wfs-catastro)

### Inferences
- Catastro also runs the non-INSPIRE OVC web services (lookups by cadastral reference or coordinates, SOAP/REST-style XML) (prior knowledge, unverified). Protected personal data such as owners and values is not open.
- IGN/CNIG offers PNOA orthophotos (WMS/WMTS), LiDAR and MDT elevation models as free downloads under CC BY 4.0 from the CNIG Centro de Descargas (prior knowledge, unverified in this session).
- SIAR (MAPA agroclimatic irrigation station network) provides ET0 and station data. It has historically been available via a web download and a key-based API (prior knowledge, unverified).
- Banco de Terras de Galicia (Agader) publishes land-bank parcels through its own viewer. I found no evidence of a public API.

### Gaps
- No searches were run for the SIAR API, Banco de Terras or IGN/CNIG. Their 2026 status is unverified.

## Sea: INTECMAR, Puertos del Estado, Copernicus Marine, lonxas (pescadegalicia)

### Takeaway
Copernicus Marine is the most API-friendly source: free registration, the `copernicusmarine` Python toolbox, and IBI regional 10-day forecasts for physics, waves and biogeochemistry. Galician data (INTECMAR closures, pescadegalicia fish-market sales) is valuable and newsworthy, but it comes through web pages and viewers rather than documented APIs, so expect scraping or bulk files. Aggregated fish-market statistics are also in IGE and datos.gob.es.

### Cited Findings
- Copernicus Marine IBI products: waves (hourly, 10-day forecast, updated daily), physics (10-day forecast, updated daily) and biogeochemistry (daily means, 10-day forecast, updated weekly), plus multi-year reanalyses. Access is through data.marine.copernicus.eu with free registration and the `copernicusmarine` Python toolbox. — [IBI Physics](https://data.marine.copernicus.eu/product/IBI_ANALYSISFORECAST_PHY_005_001/description); [IBI Waves](https://data.marine.copernicus.eu/product/IBI_ANALYSISFORECAST_WAV_005_005/description); [IBI BGC](https://data.marine.copernicus.eu/product/IBI_ANALYSISFORECAST_BGC_005_004/description); [Toolbox docs](https://toolbox-docs.marine.copernicus.eu/en/v2.0.0/usage/quickoverview.html)
- INTECMAR (under the Consellería do Mar) monitors biotoxins and harmful phytoplankton and publishes the open/closed status of production zones (mussel-raft polygons). Context: a toxin episode in May 2026 closed nearly all Galician rafts; by 23 September 2026 about 90% were open. — [Xunta press release](https://www.xunta.gal/es/notas-de-prensa/-/nova/025813/intecmar-autoriza-reapertura-14-poligonos-bateas-tres-zonas-marisqueo-ante-evolucion); [Atlántico, May 2026](https://www.atlantico.net/galicia/presencia-toxinas-obliga-cerrar-practicamente_1_20260513-4274587.html); [Moncloa.com, Sep 2026](https://www.moncloa.com/2026/09/23/produccion-mejillon-galicia-bateas-abiertas-3436356/)
- A published ML study uses INTECMAR data to predict precautionary closures caused by lipophilic toxins. — [arXiv 2402.09266](https://arxiv.org/pdf/2402.09266)
- Pescadegalicia.gal has first-sale data from 65 Galician fish markets, a newer interactive query tool, and yearbooks. In a recent year, the markets handled 3.3 million transactions, about 126,000 t and over €412M. — [Xunta press](https://www.xunta.gal/notas-de-prensa/-/nova/87968/pescadegalicia-gal-conmemora-suas-duas-decadas-traballo-debullando-actividade); [Estatísticas](https://www.pescadegalicia.gal/gl/estatisticas)
- Fish-market sales by species (quantity and value) are also available as IGE tables and as a datos.gob.es dataset, "Primera venta de productos pesqueros frescos". — [IGE selector 5861](https://www.ige.gal/igebdt/selector.jsp?COD=5861&paxina=001&c=0301004); [datos.gob.es](https://datos.gob.es/en/catalogo/a12002994-primera-venta-de-productos-pesqueros-frescos1)

### Inferences
- An INTECMAR closure predictor that combines Copernicus Marine BGC/SST, MeteoGalicia MOHID and upwelling indices, and historical closures is a strong Galician-themed AI demo. The main risk is collecting historical closure labels (scraping or asking INTECMAR).
- Puertos del Estado publishes buoy, tide-gauge and wave-forecast data (Portus) with public download and OPeNDAP/THREDDS access (prior knowledge, unverified).

### Gaps
- I could not confirm a machine-readable INTECMAR endpoint (API/JSON/WMS) or its licence. Puertos del Estado was not searched. Whether pescadegalicia has a download API is unverified.

## Government: datos.gob.es, abertos.xunta.gal, BOE, DOG, BDNS, PLACSP, INE, IGE

### Takeaway
These are strong, key-free sources for legal and public-administration RAG or agent demos. The BOE open-data REST API covers daily summaries (sumarios) and consolidated legislation. BDNS has a public REST API with Swagger docs and no authentication. The INE JSON API (Tempus3) needs no key. PLACSP offers daily and monthly ATOM feeds in CODICE XML: it is heavy but complete.

### Cited Findings
- BOE API: REST, GET over HTTPS, output format chosen with the Accept header (XML/JSON). Endpoints include `https://boe.es/datosabiertos/api/legislacion-consolidada/id/{ID}`, `/boe/sumario/{AAAAMMDD}`, `/borme/sumario/{AAAAMMDD}`, plus auxiliary tables. An MCP server for the BOE already exists on GitHub. — [BOE datos abiertos API](https://www.boe.es/datosabiertos/api/api.php); [APIconsolidada.pdf](https://www.boe.es/datosabiertos/documentos/APIconsolidada.pdf); [APIsumarioBOE.pdf](https://www.boe.es/datosabiertos/documentos/APIsumarioBOE.pdf); [MCP-BOE](https://github.com/ComputingVictor/MCP-BOE)
- BDNS: an official REST API from the IGAE at infosubvenciones.es/bdnstrans/api, with Swagger/OpenAPI docs, JSON output, public access, no authentication and no published limits. The database holds roughly 350k–650k calls for grants (convocatorias) and about 10.5M awards (concesiones); third-party figures vary. There is a Python client (`bdns-fetch`) and several commercial wrappers (AyudaScan, BuscoAyudas, Apify). — [datos.gob.es BDNS](https://datos.gob.es/en/catalogo/e05250001-base-de-datos-nacional-de-subvenciones); [bdns-fetch PyPI](https://pypi.org/project/bdns-fetch/); [AyudaScan](https://ayudascan.com/blog/que-es-bdns-base-datos-nacional-subvenciones)
- PLACSP: open datasets of tenders (excluding minor contracts), tenders aggregated from regional platforms, and minor contracts. They are distributed as daily and monthly ATOM feeds in CODICE XML, with 500 entries per file chained through `atom:link`. — [PLACSP Datos Abiertos](https://contrataciondelsectorpublico.gob.es/wps/portal/DatosAbiertos); [Hacienda dataset page](https://www.hacienda.gob.es/es-ES/GobiernoAbierto/Datos%20Abiertos/Paginas/LicitacionesContratante.aspx); [datos.gob.es aggregated tenders](https://datos.gob.es/en/catalogo/e05250001-licitaciones-publicadas-en-la-plataforma-mediante-mecanismos-de-agregacion-excluyendo-los-contratos-menores)
- INE JSON API: `https://servicios.ine.es/wstempus/js/{idioma}/{función}/{input}[?params]`, for example `DATOS_TABLA/{id}` and `OPERACIONES_DISPONIBLES`. Formats include JSON, CSV, PC-Axis and XLSX. Coverage is all cyclical (sub-annual) statistical operations plus some structural ones. — [INE API reference](https://www.ine.es/dyngs/DAB/index.htm?cid=1100); [Tempus3](https://www.ine.es/dyngs/DAB/index.htm?cid=1105)
- Abertos.xunta.gal (Xunta open-data portal) provides its catalog in RDF and RSS, with data in CSV, ODS, XLSX and iCal. — [Abertos catalog](https://abertos.xunta.gal/footer/catalogo); [RDF catalog](https://abertos.xunta.gal/busca-de-datos.rdf)

### Inferences
- datos.gob.es has a documented catalog REST API (apidata) and a SPARQL endpoint, with no key (prior knowledge, unverified in this session).
- The DOG (Diario Oficial de Galicia) publishes daily summaries with RSS. I know of no documented REST API (prior knowledge, unverified).
- IGE has a table database (igebdt) with CSV/PX export. An IGE API exists but its current documentation was not checked.
- A grant finder or recommender (BDNS + BOE + DOG) or a public-tender copilot (PLACSP) is a demo-able RAG project with no keys at all.

### Gaps
- BOE API rate limits were not found. The abertos.xunta.gal API/CKAN status is unclear: the search found only RDF/RSS. DOG and IGE APIs were not verified.

## Energy/finance: REE/ESIOS, CNMV, Banco de España, PSD2 aggregators, idealista

### Takeaway
ESIOS provides PVPC and market prices with a free personal token, requested by email to consultasios@ree.es and usually issued within about 24 hours. The endpoint is api.esios.ree.es; the old apidatos.ree.es endpoint was dropped by the major clients. The Banco de España JSON statistics API needs no key. Open banking has changed: GoCardless Bank Account Data (formerly Nordigen) stopped accepting new signups in July 2025, and Enable Banking's free "restricted" mode is the practical replacement for personal projects. The official idealista API is effectively closed to individuals.

### Cited Findings
- ESIOS: request a free personal token by email to consultasios@ree.es (usually within 24 hours). Authenticate with the `x-api-key` header; the legacy `Authorization: Token token=...` header is also accepted. The main endpoint is api.esios.ree.es. The `aiopvpc` library (Home Assistant) removed support for apidatos.ree.es. — [Home Assistant PVPC](https://www.home-assistant.io/integrations/pvpc_hourly_pricing/); [aiopvpc changelog](https://github.com/azogue/aiopvpc/blob/master/CHANGELOG.md); [HA issue #84071](https://github.com/home-assistant/core/issues/84071); [datons ESIOS tutorial](https://datons.com/en/blog/esios-api-con-python-automatiza-analisis-red-electrica-espana)
- Banco de España: a JSON web service gives access to everything in the Statistics section and in BIEST. It supports "latest data" and "series list" requests, and series codes are found through BIEST or the CSVs. There is an R client (`tidyBdE`). — [BdE API](https://www.bde.es/webbe/en/estadisticas/recursos/api-estadisticas-bde.html); [tidyBdE](https://rdrr.io/cran/tidyBdE/man/bde_series_api.html)
- GoCardless Bank Account Data (formerly Nordigen) has not accepted new accounts since July 2025. Existing accounts keep working. — [GoCardless new signups disabled](https://bankaccountdata.gocardless.com/new-signups-disabled); [DEV article](https://dev.to/johnfrandsen/gocardless-bank-account-data-alternatives-what-to-use-when-signups-are-disabled-326d); [gocardless-to-csv issue #4](https://github.com/adept/gocardless-to-csv/issues/4)
- Enable Banking offers self-serve signup, a JWT REST API and a free "Restricted Production" mode limited to accounts you link and whitelist yourself (personal use). Paid plans are needed to access third-party accounts. Spanish banks mostly expose PSD2 through Redsys. Firefly III and Actual-type tools use it as the GoCardless replacement. — [Enable Banking linked accounts](https://enablebanking.com/docs/api/linked-accounts/); [Enable Banking Spain](https://enablebanking.com/docs/markets/es/); [Firefly III docs](https://docs.firefly-iii.org/tutorials/data-importer/eb/); [Open Banking Tracker free APIs 2026](https://www.openbankingtracker.com/guides/free-open-banking-apis)
- Tink is described as having gone enterprise-only under Visa (secondary source). — [DEV article](https://dev.to/johnfrandsen/gocardless-bank-account-data-alternatives-what-to-use-when-signups-are-disabled-326d)
- Idealista: API keys are issued only after you describe your project through an access request. Secondary sources say access is limited to vetted partners. Many scraping services exist, which likely violate the terms of service. — [idealista access request](https://developers.idealista.com/access-request); [yagueto/idealista-api](https://github.com/yagueto/idealista-api)

### Inferences
- For housing projects without idealista, use INE housing price indices, MITMA/MIVAU official housing prices and rental indices, Catastro, and notary statistics (prior knowledge, unverified).
- CNMV publishes registry data and some open datasets but has no well-known public REST API (prior knowledge, unverified).
- REE also has the public REData API (apidatos.ree.es/es/datos/...), which serves demand and generation without a token. This is different from the ESIOS PVPC endpoint that aiopvpc dropped (prior knowledge; worth verifying, because sources conflict over whether "apidatos" is deprecated or just no longer used by aiopvpc).

### Gaps
- Tink's developer tier status in 2026 was not verified from a primary source. CNMV was not searched. ESIOS rate limits were not found.

## Health/other: Sanidad, SERGAS, Camino de Santiago, DGT, MITECO

### Takeaway
DGT's National Access Point (nap.dgt.es) publishes real-time traffic incidents in DATEX II. Note that the v3 feed was scheduled for retirement on 12 January 2026 and the new v3.6 simplified profile replaces it. The other sources in this area were not verified in this session.

### Cited Findings
- NAP DGT: "Incidencias DGT DATEX2 v3.6 (NUEVO)" covers the state road network except the Basque Country and Catalonia. "Incidencias DGT DATEX2 v3" is marked "A EXTINGUIR 12/01/2026" (being retired on that date). The NAP also has SRTI safety-related traffic information as Linked Open Data (EU Reg. 886/2013). — [NAP v3.6](https://nap.dgt.es/dataset/incidencias-dgt-datex2-v3-6); [NAP v3 deprecated](https://nap.dgt.es/dataset/incidencias-dgt-datex2-v3); [SRTI LOD](https://nap.dgt.es/dataset/incidencias-de-trafico-srti-en-formato-lod-datex-ii)

### Inferences
- The Ministerio de Sanidad publishes open data such as hospital discharge records (CMBD/RAE, on request), the national catalog of hospitals, and waiting lists. SERGAS publishes waiting lists and some indicators, mainly as PDF or HTML (prior knowledge, unverified).
- The Oficina del Peregrino (Pilgrim's Office in Santiago) publishes pilgrim statistics on its website (monthly or yearly tables). No API is known (prior knowledge, unverified).
- MITECO provides reservoir levels (embalses), air quality, and the forest-fire statistics database (EGIF) with delays. Many of these are CSV or WMS through the MITECO IDE (prior knowledge, unverified).

### Gaps
- Sanidad, SERGAS, the Pilgrim's Office and MITECO were not searched because of the tool budget.

## Best sources for a hackathon or portfolio demo (reliability, no bureaucracy for keys)

### Takeaway
Tier 1, usable immediately with no key: Open-Meteo, BOE API, BDNS API, INE JSON, Banco de España JSON, SIGPAC OGC API, Catastro INSPIRE WFS, DGT NAP. Tier 2, free key issued in minutes or up to a day: AEMET (email), NASA FIRMS (MAP_KEY), CDSE and Copernicus Marine (registration), ESIOS (email, about 24 hours). Avoid for short timeframes: idealista (vetting), GoCardless (signups closed), Tink (enterprise), and EFFIS historical data (request form).

### Cited Findings
- Open-Meteo needs no key and allows 10k calls per day for non-commercial use. — [Open-Meteo Terms](https://open-meteo.com/en/terms)
- BDNS needs no authentication. — [datos.gob.es BDNS](https://datos.gob.es/en/catalogo/e05250001-base-de-datos-nacional-de-subvenciones)
- CDSE promotes itself for hackathons, with 40k processing units and 10k openEO credits. — [CDSE hackathon news](https://dataspace.copernicus.eu/news/2024-12-9-how-and-why-use-copernicus-data-space-ecosystem-hackathons)
- The FIRMS key is free with 5,000 transactions per 10 minutes. — [FIRMS MAP_KEY](https://firms.modaps.eosdis.nasa.gov/usfs/api/map_key/)
- The ESIOS token takes up to about 24 hours by email. — [Home Assistant PVPC](https://www.home-assistant.io/integrations/pvpc_hourly_pricing/)
- GoCardless signups are closed. — [GoCardless](https://bankaccountdata.gocardless.com/new-signups-disabled)

### Inferences
- Demo ideas that combine these sources:
  1. Galician wildfire risk and early detection: FIRMS, Open-Meteo/MeteoGalicia, Sentinel-2 dNBR, EFFIS danger.
  2. Mussel-raft (batea) closure predictor: INTECMAR, Copernicus Marine IBI, MeteoGalicia.
  3. Grant and legal copilot (RAG over BOE, DOG and BDNS).
  4. Parcel advisor: SIGPAC OGC API, Catastro, Sentinel-2 NDVI, SIAR ET0.
  5. PVPC-aware appliance scheduler: ESIOS.
  6. Fish-market price forecasting: pescadegalicia or IGE.
- Request the email-issued keys (AEMET, ESIOS) days before a hackathon. Cache every official API response, because AEMET's limits and temporary URLs cause failures during live demos.
- Licensing: most Spanish public-sector data falls under the reuse law (Ley 37/2007 / RD 1495/2011), which allows reuse with attribution. Open-Meteo's non-commercial clause matters if the portfolio project is turned into a product (legal basis is prior knowledge, unverified).

### Gaps
- Uptime and reliability were not measured. Rankings are based on the access model, not on monitored availability.
