# Fuentes de datos y APIs financieras para un desarrollador en solitario (septiembre 2026)

> Nota de método: el proxy de salida bloqueó las páginas de precios oficiales de FMP, EODHD, Finnhub, Tiingo, CoinGecko y datos.gob.es, así que varios precios vienen de agregadores secundarios (findmymoat, qveris, apicostcalc y parecidos) o de fragmentos de resultados de búsqueda. Se marcan como **[secundaria]**. Conviene verificarlos en la web del proveedor antes de decidir. Las fuentes primarias (SEC, BCE, BdE, GLEIF, OpenFIGI, Anthropic, Massive y GoCardless) se consultaron directamente o a través de sus propias páginas.

## 1. APIs de datos de mercado (precios, fundamentales y cobertura de España/BME)

### Takeaway
Ninguna API barata de mercado permite **mostrar los datos en una web pública** con el plan estándar: FMP, Tiingo, Finnhub y EODHD exigen una licencia aparte de "display/redistribution", que suele costar cientos de dólares al mes. Para cubrir la Bolsa de Madrid, lo más barato y documentado es EODHD (bolsa "MC", desde unos 20 €/mes, solo para uso personal). yfinance y Stooq siguen funcionando, pero son frágiles y no dan ningún derecho de licencia.

### Cited Findings
**Polygon.io, ahora Massive**
- Polygon.io pasó a llamarse Massive.com el 30 de octubre de 2025. Las cuentas y los datos no cambian, `api.polygon.io` seguirá funcionando "durante un periodo prolongado" y `api.massive.com` ya funciona en paralelo — [Massive blog](https://massive.com/blog/polygon-is-now-massive); [National Law Review](https://natlawreview.com/press-releases/polygonio-now-massive)
- Precios 2026: Starter 29 $/mes, Developer 99 $, Advanced 199 $ y All-Access 399 $. El plan gratuito permite 5 llamadas/min con datos retrasados 15 min. El plan Enterprise se negocia aparte — [qveris [secundaria]](https://qveris.ai/guides/polygon-pricing-optimized/)
- Cubre acciones, opciones, índices, forex, cripto y futuros por REST, WebSocket y flat files S3. Está centrado en EE. UU. — [api-evangelist/polygon-io](https://github.com/api-evangelist/polygon-io)

**Alpha Vantage**
- El plan gratuito permite 25 peticiones/día y 5/min. Los planes premium cuestan 49,99 $, 99,99 $, 149,99 $, 199,99 $ y 249,99 $/mes por 75, 150, 300, 600 y 1.200 peticiones/min, respectivamente — [qveris [secundaria]](https://qveris.ai/guides/alpha-vantage-pricing-alternative/?lang=en); [Macroption](https://www.macroption.com/alpha-vantage-api-limits/)

**Financial Modeling Prep (FMP)**
- Para mostrar o redistribuir datos de FMP hace falta un "Data Display and Licensing Agreement" específico. Solo el plan Enterprise incluye display y redistribución — [FMP Terms of Service](https://site.financialmodelingprep.com/developer/docs/terms-of-service) (visto a través del resumen del buscador; la página está bloqueada por el proxy); [FMP pricing](https://site.financialmodelingprep.com/pricing-plans)
- Según TrustRadius hay "2 planes desde 139 $". El dato es dudoso: FMP tiene más niveles, algunos más baratos, y no pude verificarlo — [TrustRadius [secundaria]](https://www.trustradius.com/products/financial-modeling-prep/pricing)
- FMP entró como conector oficial de Claude en mayo de 2026 — [Anthropic, finance agents](https://www.anthropic.com/news/finance-agents)

**EODHD**
- El plan gratuito da 20 llamadas/día, con EOD y fundamentales limitados de EE. UU. Planes de pago: EOD All World 19,99 €/mes, EOD+Intraday 29,99 €, Fundamentals 59,99 € y All-in-One 99,99 €. Los planes personales **no permiten uso comercial** y los planes B2B empiezan en unos 399 $/mes — [EODHD pricing](https://eodhd.com/pricing); [findmymoat [secundaria]](https://www.findmymoat.com/tools/eodhd)
- Cubre la bolsa de Madrid con el código `MC`: acciones y ETF en EUR, por ejemplo `IBEXA.MC` — [EODHD exchange MC](https://eodhd.com/exchange/MC)

**Finnhub**
- El plan gratuito permite 60 llamadas/min, con cotizaciones en tiempo real de EE. UU., noticias de empresas, fundamentales básicos, forex y cripto. La licencia es no comercial: si la app se monetiza o redistribuye datos, hace falta un plan de pago — [apicostcalc [secundaria]](https://apicostcalc.com/finnhub.html); [Finnhub pricing](https://finnhub.io/pricing)

**Tiingo**
- El plan gratuito incluye EOD de EE. UU., noticias, dividendos y splits. Los planes Individual y Commercial son solo para uso interno, y mostrar o redistribuir datos requiere una licencia aparte — [Tiingo pricing](https://www.tiingo.com/about/pricing); [findmymoat [secundaria]](https://www.findmymoat.com/tools/tiingo)

**Twelve Data**
- Dice cubrir más de 90 bolsas, con tiempo real europeo a través de Cboe Europe. Tiene página propia para la Bolsa de Madrid (XMAD). Funciona con un modelo de créditos, sin permanencia. Separa los precios "Individual" de los "Business"; lo segundo sugiere que el uso comercial va por otra vía — [Twelve Data XMAD](https://twelvedata.com/exchanges/XMAD); [Twelve Data pricing](https://twelvedata.com/pricing); [Business pricing](https://twelvedata.com/pricing-business)

**Marketstack (APILayer)**
- El plan gratuito da 100 peticiones **al mes**, solo EOD, 1 año de histórico y unas 70 bolsas. El plan de pago más barato cuesta unos 8,99 $/mes por 10.000 peticiones — [Marketstack FAQ](https://marketstack.com/faq); [qveris [secundaria]](https://qveris.ai/guides/stock-api-free-comparison)

**Nasdaq Data Link (antes Quandl)**
- Los datasets gratuitos WIKI de precios de EE. UU. ya no están disponibles (**deprecado**) — [QuantConnect docs](https://www.quantconnect.com/docs/v2/writing-algorithms/datasets/nasdaq/data-link); [Nasdaq WIKIP](https://data.nasdaq.com/databases/WIKIP)

**Alpaca**
- El plan gratuito da REST con 15 min de retraso, WebSocket en tiempo real solo con datos de IEX y 200 peticiones/min. Algo Trader Plus cuesta 99 $/mes e incluye SIP completo, opciones OPRA y 10.000 peticiones/min. Solo cubre EE. UU. — [Alpaca Market Data FAQ](https://docs.alpaca.markets/us/docs/market-data-faq); [Alpaca docs](https://docs.alpaca.markets/us/docs/about-market-data-api)

**yfinance (no oficial)**
- Scrapea endpoints web de Yahoo, que limita o bloquea IPs cuando recibe muchas peticiones. Los errores `YFRateLimitError: Too Many Requests` siguen apareciendo en 2025 y 2026 (por ejemplo, en marzo de 2026 en TradingAgents) — [yfinance issue #2411](https://github.com/ranaroussi/yfinance/issues/2411); [TradingAgents #437](https://github.com/TauricResearch/TradingAgents/issues/437); [discusión #2431](https://github.com/ranaroussi/yfinance/discussions/2431)
- Se recomienda combinar `requests_cache` con un limitador de unas 2 peticiones cada 5 segundos — [yfinance issue #2289](https://github.com/ranaroussi/yfinance/issues/2289)
- Streamlit Community Cloud sufre bloqueos habituales porque comparte IPs — [Streamlit forum](https://discuss.streamlit.io/t/yfratelimiterror-too-many-requests-rate-limited-try-after-a-while/111207)

**Stooq**
- Hacia el 1 de abril de 2026, Stooq empezó a exigir un `apikey` para las descargas CSV. Se obtiene resolviendo un CAPTCHA en la web o pidiéndolo por correo a www@stooq.com. Hay un tope diario de peticiones ("Exceeded the daily hits limit") — [qf-localc README_STOOQ](https://github.com/qalydon/qf-localc/blob/master/README_STOOQ.md); [api-evangelist/stooq](https://github.com/api-evangelist/stooq)

**BME directo**
- LSEG distribuye los datos de BME Spain como feed institucional — [LSEG BME Spain](https://www.lseg.com/en/data-analytics/financial-data/pricing-and-market-data/equities-market-data/bme-spain)

### Inferences
- Para una web **pública** que muestre precios, el coste real no es la API (20–100 $/mes) sino la licencia de display, que empieza en unos 399 $/mes según EODHD B2B y se negocia en los demás. Hay dos salidas baratas: mostrar solo datos derivados o agregados (métricas calculadas, sin series de precios crudas), o usar fuentes públicas sin restricciones, como SEC/XBRL, BCE e INE.
- Para una herramienta **local u open source**, lo razonable es que cada usuario ponga su propia API key (BYOK) de EODHD, FMP o Finnhub, con yfinance y Stooq como respaldo. Así no hay redistribución: cada usuario acepta los términos del proveedor.
- Cobertura del IBEX 35, de mejor a peor documentada: EODHD (`.MC`), Twelve Data (XMAD), yfinance (`.MC`) y Marketstack. Polygon/Massive, Alpaca y Tiingo están centrados en EE. UU.

### Gaps
- No pude verificar en fuente primaria los precios actuales de FMP (las páginas están bloqueadas) ni el precio exacto de las licencias de display de Tiingo y Finnhub, que se negocian por contrato.
- No encontré el precio de Twelve Data para Madrid ni si el tiempo real de Cboe Europe incluye BME.
- No investigué el coste de una licencia directa de BME Market Data para mostrar el IBEX en tiempo real o con retraso.

## 2. Filings y fundamentales (SEC EDGAR, ESEF, CNMV, Registro Mercantil, OpenFIGI y GLEIF)

### Takeaway
En EE. UU., SEC EDGAR/XBRL es gratis, oficial y de dominio público: la mejor base para fundamentales. En Europa, filings.xbrl.org publica los informes ESEF (incluidos los españoles) en JSON. La CNMV ofrece búsqueda web y alertas por correo, pero no encontré ninguna API REST documentada. GLEIF y OpenFIGI son gratuitos y sirven para mapear identificadores (LEI, ISIN y FIGI).

### Cited Findings
- **SEC EDGAR**: la API `data.sec.gov` (submissions, companyfacts, companyconcept y frames) es gratuita. Exige un User-Agent con email de contacto (sin él devuelve 403) y un máximo de 10 peticiones/s; si se supera, la IP queda bloqueada unos 10 minutos. Hay un volcado completo en `companyfacts.zip` — [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces); [SEC Accessing EDGAR Data](https://www.sec.gov/edgar/searchedgar/accessing-edgar-data.htm); [dealcharts [secundaria]](https://dealcharts.org/blog/sec-edgar-api-guide)
- **filings.xbrl.org** (XBRL International): repositorio de informes ESEF de la UE y el Reino Unido, incluida España, organizado por LEI, fecha, sistema y país. Publica el paquete original, un visor y una versión xBRL-JSON. Tiene una API JSON limitada cuyo formato "puede cambiar". Existe un cliente de Python comunitario, `xbrl-filings-api` — [filings.xbrl.org about](https://filings.xbrl.org/about.html); [docs](https://filings.xbrl.org/docs/about); [lsalmela/xbrl-filings-api](https://github.com/lsalmela/xbrl-filings-api)
- **CNMV**: tiene buscadores web de "Otra información relevante" (OIR), información privilegiada y hechos relevantes de IIC, además de suscripción a alertas por correo según entidad o tipo. El dataset "Consulta de Hechos Relevantes registrados en la CNMV" aparece en datos.gob.es — [CNMV OIR](https://www.cnmv.es/portal/otra-informacion-relevante/resultado-oir?dias=30&lang=en); [CNMV información privilegiada](https://www.cnmv.es/portal/informacion-privilegiada/consulta-ip?lang=en); [datos.gob.es](https://datos.gob.es/en/catalogo/ea0002583-consulta-de-hechos-relevantes-registrados-en-la-cnmv)
- **Registro Mercantil**: las cuentas anuales se depositan con el programa D2. Los modelos para 2026 se fijaron por resoluciones de la DGSJFP del 19 de mayo de 2026 (BOE del 29 de mayo de 2026) — [SuperContable](https://www.supercontable.com/boletin/H/articulos/novedades_modelos_cuentas_anuales_2025_presentacion_registro_mercantil_2026.html); [sede.registradores.org](https://sede.registradores.org/sede/sede-corpme-web/informacion-y-ayuda/documentacion-descargas/registro-mercantil/)
- **OpenFIGI** (Bloomberg): gratuito. Sin API key, `/mapping` admite 25 peticiones cada 6 s y 10 jobs por petición; con una key gratuita el límite sube — [OpenFIGI docs](https://www.openfigi.com/api/documentation); [OpenFIGI overview](https://www.openfigi.com/api/overview)
- **GLEIF**: API gratuita y sin registro, basada en la Golden Copy y actualizada 3 veces al día. Incluye relaciones de nivel 2 y mapeo de LEI a BIC e ISIN — [GLEIF API](https://www.gleif.org/en/lei-data/gleif-api); [GLEIF access & use](https://www.gleif.org/en/lei-data/access-and-use-lei-data)

### Inferences
- Una tubería de fundamentales para empresas españolas cotizadas podría ser esta: LEI (GLEIF) → ESEF en filings.xbrl.org (xBRL-JSON) → métricas → cruce con ISIN y FIGI (GLEIF/OpenFIGI) → precios de EODHD o yfinance. Todas las piezas salvo los precios son gratuitas.
- La CNMV casi seguro obliga a scrapear HTML para seguir la OIR en tiempo real. Es información pública, pero habría que respetar las condiciones de uso de su web.

### Gaps
- No pude abrir la ficha de datos.gob.es (bloqueada por el proxy) para confirmar el formato del dataset de la CNMV (¿API, RSS o XML?) ni su licencia.
- No encontré la tarifa actual de las notas simples y certificaciones de cuentas anuales del Registro Mercantil. Hace falta consultar registradores.org, y parece que no existe una API masiva gratuita.
- No confirmé si la SEC mantiene exactamente el límite de 10 peticiones/s en 2026; solo aparece en guías secundarias y en la página "Accessing EDGAR Data".

## 3. Fondos y ETF: posiciones (holdings), ISIN y documentos KID

### Takeaway
iShares y otras gestoras publican CSV de posiciones por producto, y hay scrapers open source para descargarlos, pero no encontré ninguna API oficial ni términos que permitan redistribuirlos. Los KID PRIIPs **tienen que publicarse gratis** en la web del fabricante por ley, lo que los convierte en una fuente ideal para que una IA los lea: costes, indicador de riesgo (SRI) y escenarios.

### Cited Findings
- iShares publica un CSV descargable de posiciones en cada página de ETF (por ejemplo, IVV) — [Fabio Baruffa, blog](https://fabiobaruffa.com/get-the-sp500-list)
- Hay scrapers open source (`talsan/ishares`, `etf-scraper`) que avisan de que no se responsabilizan de posibles infracciones de los términos de las gestoras — [talsan/ishares](https://github.com/talsan/ishares); [ETF-Scraper](https://github.com/nikulpatel3141/ETF-Scraper)
- **PRIIPs**: el fabricante debe elaborar el KID y publicarlo en su web antes de ofrecer el producto a minoristas, y el KID debe estar disponible gratuitamente. El reglamento se aplica desde el 1 de enero de 2018 — [CSSF PRIIPs](https://www.cssf.lu/en/priips/); [FCA PRIIPs](https://www.fca.org.uk/firms/priips-disclosure-key-information-documents); [CNB Q&A](https://www.cnb.cz/en/faq/Questions-and-answers-on-the-PRIIPs-KID/)
- Morningstar da datos de fondos (fair value, moat, estrellas y NAV) a través de un conector de Claude, que exige una suscripción de Morningstar — [Morningstar connector](https://claude.com/connectors/morningstar); [tutorial](https://claude.com/resources/tutorials/using-morningstar-for-investment-research)

### Inferences
- Leer y comparar KID con IA es técnicamente viable: los PDF son públicos y siguen una plantilla regulada. Legalmente parece de bajo riesgo si se enlaza al documento original y se muestran extracciones propias, pero no he verificado los derechos de autor de cada gestora.
- Un comparador de costes de fondos basado en KID (costes totales, SRI y escenarios) sería un hueco claro, porque no depende de licencias de datos de mercado.

### Gaps
- No revisé los términos de uso de justETF ni de iShares/BlackRock sobre scraping; la legalidad sigue sin confirmar.
- No encontré ninguna API pública de la CNMV para fichas o KID de fondos registrados en España, aunque existen datasets de IIC en datos.gob.es según el catálogo de la CNMV.

## 4. Datos macro (BCE, Banco de España, FRED, Eurostat e INE)

### Takeaway
BCE y Banco de España ofrecen APIs oficiales gratuitas sin clave. FRED es gratuito pero algunas series tienen copyright de terceros que impide redistribuirlas comercialmente. Para una web pública, las fuentes europeas son las más seguras.

### Cited Findings
- **ECB Data Portal**: API SDMX 2.1 REST en `https://data-api.ecb.europa.eu/service`, gratuita, sin registro ni clave y en formatos CSV, SDMX-JSON y XML — [ECB Data Portal SDMX](https://data.ecb.europa.eu/help/getting-data-web-services-sdmx); [API overview](https://data.ecb.europa.eu/help/api/overview); [findmymoat [secundaria]](https://www.findmymoat.com/tools/ecb-data-portal)
- **Banco de España**: servicio web JSON que da acceso por URL a las series de la sección de Estadística y de BIEST, con peticiones de "último dato" y "lista de series". Hay paquete de R `tidyBdE` y descargas completas — [BdE API estadísticas](https://www.bde.es/webbe/en/estadisticas/recursos/api-estadisticas-bde.html); [BdE descargas completas](https://www.bde.es/webbe/en/estadisticas/recursos/descargas-completas.html); [tidyBdE](https://rdrr.io/cran/tidyBdE/man/bde_series_api.html)
- **FRED**: las series con aviso de copyright pertenecen a terceros (por ejemplo, S&P/Case-Shiller). Para usarlas más allá del uso personal hay que pedir permiso al propietario, y tampoco se puede volcar FRED entero y presentarlo como producto propio — [FRED API Terms of Use](https://fred.stlouisfed.org/docs/api/terms_of_use.html); [FRED legal](https://fred.stlouisfed.org/legal); [St. Louis Fed, uso ético](https://www.stlouisfed.org/publications/page-one-economics/2021/10/15/ethical-use-of-data-with-fred)

### Inferences
- Eurostat e INE tienen APIs públicas (Eurostat SDMX/JSON e INE Tempus/JSON) con reutilización permitida con atribución. No lo verifiqué en esta sesión; ver Gaps.

### Gaps
- No verifiqué en esta sesión las APIs de Eurostat ni de INE, ni sus licencias. Es muy probable que permitan reutilización (Eurostat bajo la política de la Comisión Europea, INE bajo la Ley 37/2007), pero falta la cita.

## 5. Noticias y sentimiento (GDELT, NewsAPI, RSS y Reddit)

### Takeaway
GDELT es gratuito y apto para análisis. El plan gratuito de NewsAPI.org solo sirve para desarrollo (no para producción) y su plan comercial cuesta 449 $/mes o más. La API de Reddit ya **no** tiene registro autoservicio desde finales de 2025, así que no es viable para un proyecto nuevo.

### Cited Findings
- **GDELT**: APIs JSON gratuitas en tiempo real (DOC 2.0, GEO y TV) con búsqueda de texto completo y cliente de Python `gdelt-doc-api` — [GDELT data](https://gdeltproject.org/data.html); [GDELT DOC 2.0](https://blog.gdeltproject.org/gdelt-doc-2-0-api-debuts/); [gdelt-doc-api](https://github.com/alex9smith/gdelt-doc-api)
- **NewsAPI.org**: el plan Developer da 100 peticiones/día gratis, prohíbe expresamente el uso en producción o comercial, entrega artículos con unas 24 h de retraso y solo un mes de histórico. Los planes de pago cuestan desde unos 449 $/mes — [NewsAPI pricing](https://newsapi.org/pricing); [apicostcalc [secundaria]](https://apicostcalc.com/newsapi.html)
- **Reddit**: el plan gratuito es no comercial, con unas 100 consultas/min con OAuth. Desde finales de 2025, por la "Responsible Builder Policy", todo cliente OAuth nuevo, gratuito o de pago, necesita aprobación manual (2–4 semanas y posible rechazo). El uso comercial se cita en unos 0,24 $ por 1.000 llamadas, con mínimos de unos 12.000 $/mes, pero **no hay tarifa oficial publicada** — [SocialCrawl [secundaria]](https://www.socialcrawl.dev/blog/reddit-data-api-2026); [prowlo [secundaria]](https://prowlo.com/blog/reddit-api-pricing); [octolens [secundaria]](https://octolens.com/blog/reddit-api-pricing)

### Inferences
- Para noticias en español sobre cotizadas españolas, la combinación más barata sería la OIR de la CNMV (fuente oficial), los RSS de medios económicos (Expansión, Cinco Días o elEconomista, pendiente de revisar sus términos) y GDELT.

### Gaps
- No revisé los RSS concretos de los medios financieros españoles ni sus términos de reutilización.
- Las cifras de Reddit vienen todas de blogs secundarios; no hay fuente oficial.

## 6. Oferta de Claude/Anthropic para finanzas y servidores MCP open source

### Takeaway
Anthropic tiene una oferta de finanzas madura: Claude for Financial Services desde julio de 2025, conectores con S&P, FactSet, Morningstar, PitchBook, LSEG, Moody's y otros, y desde mayo de 2026 plantillas de agentes y un repositorio open source con licencia Apache 2.0. Casi todos los conectores exigen suscripción al proveedor de datos, así que no sirven como fuente gratuita para un proyecto personal. Lo que sí sirve es el repositorio como referencia de arquitectura.

### Cited Findings
- **Claude for Financial Services**, julio de 2025: añadió conectores con S&P Capital IQ, Daloopa, Morningstar y PitchBook, además de S&P Global y Morningstar — [Anthropic, Claude for Financial Services](https://www.anthropic.com/news/claude-for-financial-services); [Advancing Claude for FS](https://www.anthropic.com/news/advancing-claude-for-financial-services)
- El plugin central de análisis financiero incluye conectores con Daloopa, Morningstar, S&P Global, FactSet, Moody's, MT Newswires, Aiera, LSEG, PitchBook, Chronograph y Egnyte. Pueden requerir suscripción o API key del proveedor — [Claude Help Center](https://support.claude.com/en/articles/13851150-install-financial-services-plugins)
- **5 de mayo de 2026**: 10 plantillas de agentes (pitch builder, earnings reviewer, model builder, market researcher, valuation reviewer, reconciliador del libro mayor, cierre mensual, auditor de estados financieros, KYC screener, entre otras); add-ins para Excel, PowerPoint y Word; nuevos conectores con Dun & Bradstreet, Fiscal AI, **Financial Modeling Prep**, Guidepoint, IBISWorld, SS&C Intralinks, Third Bridge y Verisk; y una app MCP de Moody's con datos de más de 600 millones de empresas. Se ofrecen como plugins en Claude Cowork y Claude Code en todos los planes de pago, y como Claude Managed Agents en beta. El anuncio cita Claude Opus 4.7 con un 64,37 % en el Finance Agent benchmark de Vals AI — [Anthropic, finance agents](https://www.anthropic.com/news/finance-agents)
- El repositorio `anthropics/financial-services` (Apache 2.0) reúne agentes, bundles de skills y conectores MCP. Todo está en markdown/JSON y no requiere infraestructura — [GitHub anthropics/financial-services](https://github.com/anthropics/financial-services); [knowledge-work-plugins/finance](https://github.com/anthropics/knowledge-work-plugins/tree/main/finance)
- Hay servidores MCP comunitarios basados en yfinance, como `9nate-drake/mcp-yfinance` — [mcp-yfinance](https://github.com/9nate-drake/mcp-yfinance)

### Inferences
- Un proyecto de portfolio diferencial podría ser un servidor MCP open source de **datos públicos europeos y españoles** (CNMV OIR, ESEF de filings.xbrl.org, BCE, BdE y KID). No encontré ninguno equivalente y cubriría un hueco que los conectores de pago no cubren, porque están centrados en EE. UU. y en instituciones.

### Gaps
- No busqué de forma exhaustiva servidores MCP de finanzas en GitHub (EDGAR, FRED, etc.); solo tengo el ejemplo de yfinance.

## 7. Open banking en España (2026)

### Takeaway
GoCardless Bank Account Data (antes Nordigen) no admite registros nuevos. Enable Banking es la alternativa autoservicio más práctica en la UE y es gratuita para cuentas propias. PSD3 y PSR tienen acuerdo político desde noviembre de 2025. FIDA (open finance) está estancada en trílogo y no se espera antes de 2029–2030.

### Cited Findings
- GoCardless muestra "new signups disabled" para Bank Account Data; las integraciones existentes siguen funcionando — [GoCardless](https://bankaccountdata.gocardless.com/new-signups-disabled); [adept/gocardless-to-csv #4](https://github.com/adept/gocardless-to-csv/issues/4)
- Enable Banking ofrece registro autoservicio, API REST con JWT, SDK y un modo "Restricted Production" que permite usar en vivo las cuentas propias en lista blanca sin pagar. Proyectos como Firefly III y Kleos lo están adoptando como reemplazo — [DEV Community](https://dev.to/johnfrandsen/gocardless-bank-account-data-alternatives-what-to-use-when-signups-are-disabled-326d); [firefly-iii #10753](https://github.com/firefly-iii/firefly-iii/issues/10753); [Kleos #53](https://github.com/NeoLorenzo/Kleos/issues/53); [Open Banking Tracker](https://www.openbankingtracker.com/guides/free-open-banking-apis)
- **PSD3/PSR**: acuerdo político provisional del Consejo y el Parlamento el 27 de noviembre de 2025. La publicación en el DOUE se esperaba en el 2.º trimestre de 2026. **FIDA** va por separado: el trílogo está parado desde principios de 2026. El mejor escenario es un acuerdo en 2026 y aplicación hacia 2029; el escenario base, aplicación entre finales de 2029 y 2030 — [Crassula](https://crassula.io/guides/licenses/psd3-psr/); [financexmagazine](https://www.financexmagazine.com/post/open-banking-s-quiet-reset-psd3-inches-to-print-fida-wobbles-and-baas-finally-picks-a-lane)

### Inferences
- Para una herramienta local de finanzas personales: Enable Banking en modo restringido con las cuentas del propio usuario. Para una app pública con cuentas de terceros hace falta un contrato de pago (Enable Banking o Tink) o ser AISP registrado ante el BdE, lo que para un desarrollador en solitario es un obstáculo serio.

### Gaps
- No encontré los precios públicos de Enable Banking ni de Tink para producción.
- No confirmé si PSD3/PSR se publicaron finalmente en el DOUE en 2026.

## 8. Cripto (CoinGecko)

### Takeaway
El plan Demo de CoinGecko es gratuito, da 10.000 llamadas al mes y exige atribución. Basta para prototipos.

### Cited Findings
- Plan Demo gratuito: 10.000 llamadas/mes y exige atribución pública. Los planes de pago empiezan en unos 35 $/mes (300 llamadas/min y 100.000 al mes) — [CoinGecko learn](https://www.coingecko.com/learn/best-free-crypto-api); [CoinGecko pricing](https://www.coingecko.com/en/api/pricing)
- Hay un **conflicto** sobre el precio: costbench dice que el pago empieza en 29 $/mes — [costbench [secundaria]](https://costbench.com/software/blockchain-data-api/coingecko-api/free-plan/). También hay dudas sobre el límite por minuto del Demo: el resumen del buscador indica 100/min, pero páginas antiguas citan 30/min — [CoinGecko support](https://support.coingecko.com/hc/en-us/articles/4538771776153-What-is-the-rate-limit-for-CoinGecko-API-public-plan)

### Inferences
- Para una app pública, CoinGecko Demo con atribución es probablemente la única fuente de precios de mercado mostrable gratis de todo este catálogo, pero hay que confirmarlo en sus términos.

### Gaps
- No pude abrir la página de precios oficial (bloqueada) para resolver el conflicto entre 29 y 35 $ y el límite por minuto.

---

### Recomendación de stack (inferencia del investigador, no cita)
**(a) App web pública:** SEC EDGAR/XBRL + filings.xbrl.org (ESEF) + GLEIF/OpenFIGI + BCE/BdE (INE y Eurostat por verificar) + KID PRIIPs (enlazados, con extracciones propias) + CNMV OIR + GDELT + CoinGecko Demo con atribución. Los **precios de acciones y ETF** son el punto débil: hay que evitar mostrar series crudas o presupuestar una licencia de display (unos 399 $/mes o más con EODHD B2B, o negociarla con Twelve Data, FMP o Massive). Nunca usar yfinance ni Stooq para mostrar datos en público.

**(b) Herramienta local/open source:** el mismo núcleo gratuito más BYOK (el usuario pone su propia key de EODHD, que cubre BME `.MC` desde unos 20 €/mes, o de FMP o Finnhub) con yfinance y Stooq como respaldo, caché local y límite de peticiones. Enable Banking en modo restringido para las cuentas propias. Se podría exponer todo como un servidor MCP de datos públicos europeos.
