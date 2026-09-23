# Tendencias B2B de agentes de IA (2025-2026): categorías en auge, categorías saturadas y la próxima ola

> Nota de método (septiembre de 2026): WebFetch estaba bloqueado por el proxy de salida para ycombinator.com, techcrunch.com y wikipedia.org. Por eso, casi todos los hallazgos salen de los fragmentos de los resultados de búsqueda, no de la lectura completa de las páginas. Muchas fuentes son agregadores o blogs (Substack, dev.to, blogs de marketing de proveedores), y la calidad se indica donde importa. Las cifras deben tratarse como aproximaciones y verificarse en la fuente original antes de citarlas en público.

## 1. Tandas de Y Combinator (W25-S26) y Requests for Startups: ¿qué categorías de agentes dominan?

### Conclusión principal
Las tandas de YC de 2026 tienen entre un 60 % y un 74 % de empresas de IA. El centro de gravedad se ha movido de las *aplicaciones* de agentes (W25/S25) a la *infraestructura* de agentes (W26/S26): identidad, evals, memoria, pagos, observabilidad y seguridad. Las RFS de 2026 piden "software for agents", marketplaces de capacidades que los agentes pagan en tiempo de ejecución, agentes multiplayer y chips de inferencia para cargas de trabajo agénticas.

### Hallazgos con fuente
- W26 tuvo 194 empresas, "la tanda más grande de la historia de YC", y cerca del 60 % se centra en IA (frente al 40 % en 2024). Otra fuente da un 74 % de empresas relacionadas con IA. Hay 59 servicios nativos de IA y 46 productos de software mejorados con IA — [The Agent Report](https://the-agent-report.com/2026/07/ai-agent-startup-explosion-2026-yc-ecosystem/), [Extruct AI W26 breakdown (199 empresas)](https://www.extruct.ai/research/ycw26/), [Sameer Nanda (190 empresas)](https://sameernanda.com/yc-w26-batch-analysis/). *Las cifras de tamaño de la tanda se contradicen (190/194/199) y las del porcentaje de IA también (60 % frente a 74 %).*
- El 41,5 % de W26 construye "la fontanería que hay debajo de los agentes de IA: auth, testing, seguridad, monitorización, gestión de contexto, facturación" — [BuildMVPFast W26 analysis](https://www.buildmvpfast.com/blog/yc-w26-batch-agent-infrastructure-boom) (blog; fuente de calidad media).
- El segmento de crecimiento más rápido dentro de W26 fueron las startups "agent-native", cuyo producto entero es un agente autónomo y no un SaaS con una interfaz de chat — [The Agent Report](https://the-agent-report.com/2026/07/ai-agent-startup-explosion-2026-yc-ecosystem/).
- El Demo Day de S26 fue el 10 de septiembre de 2026, con 235 empresas (la tanda más grande de la historia), un 52 % B2B y un 60 % de IA. "La tanda anterior de YC se definió por las aplicaciones de agentes; esta construye la infraestructura que hay debajo": routing, gestión de contexto, evaluación y tooling de automatización — [byteiota S26](https://byteiota.com/yc-s26-demo-day-agent-infrastructure-is-now-a-category/).
- El stack de agentes en S26 cristaliza en productos independientes: identidad (Inkbox), evaluación (Archal), memoria (Glen), economía del cómputo (Understudy Labs), pagos (Agentcard) y bucle de mejora en producción (Dialogus) — [byteiota](https://byteiota.com/yc-s26-demo-day-agent-infrastructure-is-now-a-category/).
- RFS de verano de 2026 (15 categorías, que abarcan IA, hardware, defensa, agricultura y espacio). Incluye "Inference Chips for Agent Workflows" (los chips actuales están pensados para inferencia de prompt-in/response-out, y los agentes no funcionan así) y "Software for Agents / sé tu propio forward-deployed engineer" (los agentes de programación permiten que cada usuario personalice radicalmente la interfaz de un SaaS) — [The VC Corner](https://www.thevccorner.com/p/yc-summer-2026-requests-for-startups-ideas), [Fundreef](https://fundreef.substack.com/p/ycs-summer-2026-wishlist-15-startups), [Superframeworks](https://superframeworks.com/articles/yc-summer-2026-rfs-hard-tech-pivot).
- RFS de otoño de 2026 (13 ideas, bajo el lema "AI is moving into the physical world"). Incluye tutores de IA, verificación de humanos, agentes "multiplayer" (espacios de trabajo compartidos y en directo con agentes, "más cerca de Figma que de un log de chat"), cómputo en el mar, APIs que se mantienen solas, defensa (hay un Secretario del Ejército en ejercicio implicado) y agentes que presupuestan trabajos complejos y organizan equipos — [Inc.](https://www.inc.com/lucia-auerbach/y-combinator-requests-for-startups-fall-2026/91379840), [Superframeworks Fall 2026](https://superframeworks.com/articles/yc-fall-2026-rfs-indie-hacker-plays), [Startup Fortune](https://startupfortune.com/y-combinators-fall-2026-wish-list-puts-a-sitting-army-secretary-in-the-founder-pitch-room/).
- La framing de YC para las RFS: "the next billion software users are AI agents, yet agents still can't act on their own". YC pide marketplaces de capacidades donde los agentes encuentren, paguen y usen APIs, datos, skills y servicios en tiempo de ejecución — [resumen de búsqueda de las RFS de YC](https://www.ycombinator.com/rfs) (página oficial; no se pudo leer entera).

### Inferencias
- El 90 % de la tanda de 2026 son equipos grandes con financiación, pero las categorías de las RFS que un equipo muy pequeño puede lanzar son: agentes multiplayer, APIs que se mantienen solas, personalización de interfaces de SaaS mediante agentes y marketplaces de capacidades/herramientas para agentes. Superframeworks marca explícitamente "multiplayer AI" como algo que un equipo pequeño puede sacar adelante.
- Las piezas de infraestructura de agentes (evals, memoria, identidad, pagos) son ahora "categorías" reconocidas, lo que valida a los jurados las demos open source en esas capas.

### Lagunas
- No encontré estadísticas fiables por categoría para W25/S25/F25 (en las búsquedas solo aparecía W26/S26). No se pudo leer la página oficial de las RFS de YC (bloqueada), así que la lista exacta de ideas viene de fuentes secundarias.

## 2. Startups B2B de IA con crecimiento más rápido (2025-2026): datos de tracción por vertical

### Conclusión principal
El dinero y el crecimiento se concentran en: agentes de programación/constructores de apps (Lovable, Replit, Cognition), agentes de atención al cliente (Sierra, Decagon), voz (ElevenLabs), legal (Harvey), contabilidad/finanzas (Basis, Rillet) y compras (Pivot). Los ganadores venden *trabajo terminado dentro de un flujo de trabajo concreto*, no una interfaz de chat.

### Hallazgos con fuente
- Sierra (agentes de atención al cliente para empresas) llegó a sus primeros 100 M$ de ARR en 7 trimestres y añadió otros 100 M$ en 2 trimestres más: de 0 a 200 M$ en unos 26 meses — [Startup Riders / TechCrunch summary](https://growthindex.startupriders.com/), [TechCrunch Jul 2026](https://techcrunch.com/2026/07/08/these-ai-startups-are-growing-revenue-at-faster-and-faster-rates/) (TechCrunch visto solo como fragmento de búsqueda).
- Lovable: de 0 a unos 500 M$ de ARR en unos 14 meses. Replit: de 2,5 M$ a unos 525 M$ en unos 14 meses. Mercor: de 1 M$ a unos 1.500 M$ de run-rate bruto en 17 meses — [Startup Riders Growth Index](https://growthindex.startupriders.com/).
- Cognition (Devin): de 1 M$ de ARR en septiembre de 2024 a 73 M$ en junio de 2025 — [Startup Riders](https://www.startupriders.com/p/fastest-growing-ai-startups-2026).
- Decagon (atención al cliente): Serie D de 250 M$ con una valoración de 4.500 M$ en enero de 2026 (Coatue, Index). Sacra estima unos 100 M$ de ARR en julio de 2026, frente a 44 M$ a finales de 2025 — [Sacra Decagon](https://sacra.com/c/decagon/).
- ElevenLabs (voz): Serie D de 500 M$ con una valoración de 11.000 M$ (liderada por Sequoia, en febrero de 2026). Sacra estima unos 600 M$ de ARR en junio de 2026, frente a 330 M$ a finales de 2025 — [ElevenLabs blog](https://elevenlabs.io/blog/series-d), [TechCrunch](https://techcrunch.com/2026/02/04/elevenlabs-raises-500m-from-sequioia-at-a-11-billion-valuation/), [Sacra](https://sacra.com/c/elevenlabs/).
- Harvey (legal): valoración de unos 11.000 M$ según un agregador. No encontré datos de ARR — [OpusClip blog](https://www.opus.pro/blog/hottest-ai-startups-2026) (fuente débil).
- Basis (agentes de IA para firmas contables): Serie B de 100 M$ con una valoración de 1.150 M$ (Accel, GV, Khosla), en febrero de 2026. Lo usa aproximadamente el 30 % de las 25 mayores firmas contables, en asesoría, fiscalidad y auditoría — [SiliconANGLE](https://siliconangle.com/2026/02/24/ai-accounting-startup-basis-secures-100m-1-15b-valuation-firms-adopt-agent-based-workflows/), [CPA Practice Advisor](https://www.cpapracticeadvisor.com/2026/02/24/basis-raises-100-million-to-deploy-ai-agents-for-accounting-firms/178759/).
- Rillet (ERP/contabilidad nativo de IA): unos 100 M$ captados en menos de un año (Sequoia, a16z, ICONIQ). Digits, Puzzle, Pilot, Numeric y Fondo también han levantado rondas relevantes. La escasez de CPAs en EE. UU. (más de 340.000 contables perdidos desde 2019) empuja la automatización — [Startup Fundraising accounting guide](https://startupfundraising.com/accounting-ai-fundraising) (agregador).
- Pivot (sistema operativo de compras con IA): Serie B de 40 M$ en mayo de 2026 para capacidades agénticas e integraciones con ERP. Clientes: DoorDash, Wolt, Lemonade, Flix — [FinTech Global](https://fintech.global/2026/05/26/pivot-raises-40m-series-b-to-transform-procurement-ai/).
- Ranking por "SR Momentum Score" de 2026: Lovable, Mercor, Ramp, Harvey, Perplexity, Mistral, Sierra, Replit — [Startup Riders](https://growthindex.startupriders.com/).

### Inferencias
- Patrón que funciona: agente vertical + integraciones profundas en el sistema de registro (ERP, CRM, gestión de expedientes) + precio por resultado o por tarea + auditabilidad. Atención al cliente, contabilidad y legal son las verticales probadas. Compras, seguros y operaciones de back-office son las siguientes.
- Voz es la capa horizontal con más crecimiento de ingresos (ElevenLabs casi duplicó su ARR en unos 6 meses).

### Lagunas
- No encontré datos fiables de ARR para Harvey, 11x, Clay, Artisan, Browserbase o browser-use. No pude leer en detalle el artículo de TechCrunch de julio de 2026.

## 3. Categorías saturadas o que conviene evitar

### Conclusión principal
Los AI SDR totalmente autónomos son el ejemplo más claro de categoría sobrecalentada (con churn de entre el 50 % y el 80 %). Los asistentes de notas de reuniones están muy adoptados pero comoditizados. Los chatbots genéricos de atención al cliente y de "chat con tus documentos" compiten contra Sierra/Decagon y contra las funciones nativas de las plataformas. Los constructores visuales de agentes y los frameworks genéricos de agentes están llenos (Langflow, Dify, Flowise, n8n).

### Hallazgos con fuente
- El churn anual en despliegues de AI SDR totalmente autónomos es del 50-70 %, y un proveedor conocido ronda el 80 %. 11x.ai (más de 74 M$ captados) perdió, según informaciones de principios de 2026, una parte importante de sus clientes a los pocos meses de firmar — [Tami.ai](https://tami.ai/ai-sdrs-2026/), [Digital Applied buyer's guide](https://www.digitalapplied.com/blog/ai-sdr-agents-2026-buyers-guide-landscape-pricing) (son blogs de proveedores o agencias, con interés en el tema; hay que tratarlo como indicativo).
- Los AI SDR convierten reuniones en oportunidades al 15 %, frente al 25 % de los SDR humanos. Los emails generados por IA se marcan como spam más del doble de veces. Los proveedores que ganan ahora son los modelos "híbridos" — [Harbor BD](https://www.harborbd.com/blogs/ai-sdr-outbound-results-2026), [Rework](https://resources.rework.com/news/sales-tech/ai-sdr-worth-it-2026-hybrid-model-sales-leader).
- Asistentes de notas de reuniones: hay un 75 % de probabilidad de que alguien en una reunión profesional de 2026 esté usando uno. La inteligencia conversacional la usa el 27,7 % de los equipos de campo. Es una categoría de alta adopción y muy concurrida — [Laxis report](https://www.laxis.com/blog/state-of-meeting-note-taking-2026/) (proveedor).
- Tres de los cinco repositorios de agentes con más estrellas son constructores visuales (Langflow unos 146k, Dify unos 136k, Flowise unos 51k) — [Fungies](https://fungies.io/top-github-repositories-ai-agent-frameworks-2026/), [NocoBase](https://www.nocobase.com/en/blog/github-open-source-ai-agent-projects).
- Hay más de 17.000-22.000 servidores MCP públicos (PulseMCP, julio de 2026), así que otro servidor MCP genérico no destaca — [Awesome MCP Tools](https://awesome-mcp.tools/blog/top-mcp-servers-2026), [Firecrawl](https://www.firecrawl.dev/blog/best-mcp-servers-for-developers).

### Inferencias
- Conviene evitar: RAG de "chat con tus PDFs", AI SDR de envío masivo, asistentes de notas de reuniones genéricos, otro framework o constructor visual de agentes, wrappers de servidor MCP para una API popular y chatbots genéricos de atención al cliente.
- Las categorías saturadas siguen siendo viables si se hacen *muy verticales + integradas + medidas* (por ejemplo, un agente de voz para concesionarios en español conectado a su DMS), pero no como producto horizontal.

### Lagunas
- No hay datos cuantitativos rigurosos sobre saturación (por ejemplo, número de competidores por categoría). Las cifras de churn vienen de blogs y no de datos auditados.

## 4. Categorías emergentes de 2026 (la próxima ola)

### Conclusión principal
Las capas más calientes y todavía abiertas son: pagos/comercio de agentes (x402, AP2, ACP, MPP), seguridad de agentes (varias adquisiciones grandes), evals/observabilidad, identidad/auth de agentes, memoria, marketplaces de capacidades, agentes multiplayer, agentes de proceso para industrias reguladas o ERP, y voz para pymes. Todas tienen poco "producto de referencia" y son muy demostrables.

### Hallazgos con fuente
**Pagos y comercio de agentes**
- El stack se divide en capas: AP2 (Google) para autorización/mandato, ACP (OpenAI + Stripe) para checkout, x402 (Coinbase) para pagos con stablecoins sobre HTTP 402 y MPP (Stripe/Tempo) para pagos máquina a máquina — [DEV Community](https://dev.to/lusivision/agentic-payments-in-2026-ap2-acp-and-x402-explained-2pkb), [Crossmint](https://www.crossmint.com/learn/agentic-payments-protocols-compared).
- x402 tiene la mayor tracción en producción: la V2 salió en diciembre de 2025, Stripe lo integró en Base en febrero de 2026, Cloudflare lo soporta y AWS Bedrock AgentCore Payments lo adoptó en mayo de 2026. La x402 Foundation se lanzó bajo la Linux Foundation el 14 de julio de 2026 con 40 miembros — [Openfort](https://www.openfort.io/blog/agentic-payments-landscape), [AgentLux](https://agentlux.ai/blog/the-agent-payments-showdown-x402-vs-ap2-vs-mpp-vs-acp-in-2026) (blogs; hay que comprobar las fechas).
- YC S26 incluye a Agentcard (pagos para agentes). La RFS pide marketplaces donde los agentes paguen por APIs y datos en tiempo de ejecución — [byteiota](https://byteiota.com/yc-s26-demo-day-agent-infrastructure-is-now-a-category/).

**Seguridad de agentes**
- OpenAI compró Promptfoo (pruebas de prompt injection y fugas de datos; 23 M$ captados, 86 M$ de valoración) el 9 de marzo de 2026 — [Forbes](https://www.forbes.com/sites/janakirammsv/2026/03/10/openai-acquires-promptfoo-to-embed-security-testing-into-its-agents/), [Security Boulevard](https://securityboulevard.com/2026/03/openai-acquires-security-startup-promptfoo-to-fortify-ai-agents/).
- SentinelOne compró Prompt Security (agosto de 2025, 250-300 M$). Palo Alto compró Protect AI (julio de 2025). Check Point compró Lakera (septiembre de 2025) — [Security Boulevard/Forbes resumen](https://securityboulevard.com/2026/03/openai-acquires-security-startup-promptfoo-to-fortify-ai-agents/).
- Las startups de seguridad de IA agéntica han levantado en total unos 3.600 M$. Solo en torno a RSAC 2026 (10-26 de marzo) se anunciaron más de 392 M$ — [Software Strategies Blog](https://softwarestrategiesblog.com/2026/03/28/agentic-ai-security-startups-funding-mna-rsac-2026/).

**Evals, observabilidad e infraestructura de agentes**
- En S26 hay startups independientes para evals (Archal), memoria (Glen), identidad (Inkbox) y producción/automejora (Dialogus). El 41,5 % de W26 hace infraestructura de agentes — [byteiota](https://byteiota.com/yc-s26-demo-day-agent-infrastructure-is-now-a-category/), [BuildMVPFast](https://www.buildmvpfast.com/blog/yc-w26-batch-agent-infrastructure-boom).

**MCP como estándar de facto**
- El repositorio modelcontextprotocol/servers superó las 87.500 estrellas en junio de 2026. Playwright MCP tiene unas 34,1k y GitHub MCP unas 30,8k. El 72 % de los usuarios de MCP espera usarlo más (encuesta de Zuplo, diciembre de 2025) — [Awesome MCP Tools](https://awesome-mcp.tools/blog/top-mcp-servers-2026), [guptadeepak.com](https://guptadeepak.com/the-complete-guide-to-model-context-protocol-mcp-enterprise-adoption-market-trends-and-implementation-strategies/).

**"Empleados de IA" y agentes de proceso para empresas reguladas o legacy**
- Maisa (España) vende "digital workers" auditables para industrias reguladas (bancos, automoción, energía). Ver la sección 5 — [Maisa](https://maisa.ai/agentic-insights/maisa-raises-25m-from-creandum-and-forgepoint/).
- Pivot (compras) y Rillet/Basis (contabilidad) apuestan por agentes integrados con el ERP — ver la sección 2.

**Voz para pymes**
- Beside (recepcionista con IA para pymes) captó 32 M$ (Serie A de 20 M$ liderada por EQT) y gestiona millones de llamadas al mes. Quo (antes OpenPhone) captó 105 M$. Smallest.ai captó 13 M$ (julio de 2026) para voz ultrarrápida con modelos pequeños. El 62 % de las llamadas entrantes a pymes no se atiende en horas punta (cifra de un proveedor) — [Fortune](https://www.fortune.com/2025/11/11/beside-ai-voice-startup-raises-32-million-ai-receptionist-for-small-business/), [TechCrunch](https://techcrunch.com/2026/07/31/smallest-ai-raises-13m-to-build-ultra-fast-voice-ai-that-sounds-genuinely-human/), [AgentVoice market map](https://agentvoice.com/blog/ai-voice-agents-funding-market-map/).

### Inferencias: proyectos factibles para un solo desarrollador que atraen a empresas y a jurados de hackathons
1. **Firewall o gateway de seguridad para agentes MCP** (detección de prompt injection y de "tool poisoning", políticas por herramienta, log de auditoría). La categoría está validada por adquisiciones (Promptfoo, Lakera, Prompt Security), y un proxy MCP open source es una demo pequeña y convincente.
2. **Sandbox de pagos de agentes con x402/AP2**: un agente que descubre una API, recibe un 402, paga con un mandato con límites y deja un recibo auditable. Sigue la RFS de "capability marketplace" y el impulso de la Linux Foundation.
3. **Evals y observabilidad para un vertical** (por ejemplo, un harness de evaluación para agentes de facturas o de licitaciones públicas en español con un dataset real). Las evals son una categoría reconocida en S26 y los datasets en español son escasos.
4. **Agente de licitaciones y compras públicas** (España/UE: PLACSP, TED): lee los pliegos, puntúa la adecuación y redacta la oferta. Combina las tendencias de compras (Pivot) con la de "acceso a fondos públicos" (Granter AI). Es muy demostrable con datos abiertos.
5. **Agente de voz para pymes en español** conectado a un calendario o CRM real con medición del resultado (reservas conseguidas). El mercado está validado (Beside, ElevenLabs).
6. **Agente de datos (text-to-SQL) sobre un ERP de pymes** (por ejemplo, Holded/Odoo) con MCP, controles de permisos y evals. Encaja con la tendencia de "IA para ERP/legacy".
7. **Espacio de trabajo "multiplayer" para agentes** (visibilidad compartida y en directo de las decisiones del agente): es una categoría explícita de las RFS de otoño de 2026.

### Lagunas
- No encontré cifras de financiación específicas de startups de A2A (agent-to-agent), de "text-to-SQL para negocio" ni de "IA para licitaciones". El dato del Linux Foundation/x402 viene de blogs y hay que verificarlo en linuxfoundation.org.

## 5. Startups europeas y españolas de IA destacadas (2025-2026)

### Conclusión principal
España tiene una escena de IA agéntica pequeña pero real. Maisa (digital workers para industrias reguladas, 25 M$ en seed) y Factorial (reconstruida en torno a agentes para RR. HH., finanzas e IT; Serie D de 150 M$ con un compromiso adicional de hasta 540 M$ de General Catalyst) son las referencias. En Europa, los agentes captaron unos 6.200 M€ en 2025.

### Hallazgos con fuente
- **Maisa** (Valencia/EE. UU.): seed de 25 M$ en agosto de 2025, liderada por Creandum con Forgepoint, NFX y Village Global, tras un pre-seed de 5 M$ en diciembre de 2024. Producto: Maisa Studio, "agentic process automation", que permite a "citizen developers" desplegar "digital workers" auditables en lenguaje natural. Motor propio: Knowledge Processing Unit (KPU). Pilotos en bancos globales, fabricantes de coches y energéticas. Aparece en informes Hype Cycle de Gartner — [Maisa press](https://maisa.ai/agentic-insights/maisa-raises-25m-from-creandum-and-forgepoint/), [Forgepoint](https://forgepointcap.com/perspectives/maisa-why-we-invested/).
- **Factorial** (Barcelona, fundada en 2016): reconstruyó su SaaS en torno a agentes de IA para flujos de RR. HH., finanzas e IT. Cerró una Serie D de 150 M$ liderada por General Catalyst (su primera inversión directa en la empresa), con Atomico y Four Rivers, más un compromiso de hasta 540 M$ del Customer Value Fund (no dilutivo, para financiar la adquisición de clientes). Expansión a Alemania (Múnich), Francia, Italia y Portugal — [Sifted](https://sifted.eu/articles/factorial-raise-general-catalyst-atomico-series-d).
- **GuruSup** (Valencia): seed de 1,3 M€ en abril de 2026 para una plataforma de agentes de IA para atención al cliente y automatización de procesos — [EU-Startups](https://www.eu-startups.com/2026/04/valencia-based-gurusup-raises-e1-3-million-seed-round-for-ai-customer-service-platform/).
- **THEKER** (Barcelona): Serie A de 73 M€ en junio de 2026 para robótica con IA (IA física, no agentes de software) — [EU-Startups](https://www.eu-startups.com/2026/06/barcelona-based-theker-raises-e73-million-series-a-to-accelerate-ai-robotics-deployment/).
- **Afori** (insurtech; agentes para el back-office de corredurías de seguros) y **Granter AI** (automatización del acceso a subvenciones y fondos públicos) aparecen como startups agénticas españolas destacadas — [startups-espanolas.es](https://startups-espanolas.es/top-7-startups-espanolas-de-ia-agentica-en-2026/) (agregador de baja calidad). El Referente publicó un TOP25 de startups de IA para 2026 que no se pudo leer — [El Referente](https://elreferente.es/startups/top25-startups-de-ia-a-tener-en-cuenta-para-este-2026/).
- Ecosistema español: de 309 a 959 empresas centradas en IA en un año (+210 %), y la IA es ya la tercera vertical del ecosistema — [Startup Reporter](https://www.startupreporter.eu/spain-tech-ecosystem-10000-companies-ai-growth-2026/). Otra fuente habla de 392 startups de IA y 1.600 M€ captados en 2026 — [El Ecosistema Startup](https://ecosistemastartup.com/startups-ia-espana-392-empresas-y-1-600me-captados-en-2026/). *Las cifras no concuerdan entre sí.*
- Europa: las startups de agentes de IA captaron 6.200 M€ en 429 rondas en 2025 (datos de Sifted) — [Sifted](https://sifted.eu/articles/factorial-raise-general-catalyst-atomico-series-d). Sifted publicó una lista de "19 AI agent startups to watch in 2026" (no leída) — [Sifted](https://sifted.eu/articles/19-ai-agent-startups-to-watch-in-2026-according-to-vcs).
- Un informe atribuido a Dealroom dice que el 38 % de la inversión europea en IA del primer semestre de 2026 fue a proyectos con componentes agénticos (frente al 12 % en 2024) — citado por [startups-espanolas.es](https://startups-espanolas.es/top-10-startups-ia-agentica-espana-2026-mas-financiadas) (fuente secundaria; no verificado en Dealroom).

### Inferencias
- Las oportunidades españolas se agrupan en back-office de sectores regulados (seguros, banca, administración pública, subvenciones) e integraciones con pymes (RR. HH., ERP y contabilidad en el ecosistema de Factorial/Holded). Un proyecto de portfolio que se conecte con Factorial, Holded o datos públicos españoles tiene relevancia local.

### Lagunas
- No encontré información verificada sobre Clibrain (ni sobre una posible sucesora) ni sobre funciones de IA de Holded o Fever en 2026. No confirmé la valoración ni la fecha de la Serie D de Factorial dentro de los fragmentos.

## 6. Proyectos open source de agentes de IA que se hicieron virales (2025-2026) y por qué

### Conclusión principal
OpenClaw (asistente personal de agentes con licencia permisiva, creado como proyecto de fin de semana en noviembre de 2025) es el caso de viralidad definitivo: unas 388k estrellas en agosto de 2026 y su creador contratado por OpenAI. El resto de las estrellas se concentra en constructores visuales (Langflow, Dify), agentes de programación (OpenHands) y la infraestructura de MCP y control del navegador.

### Hallazgos con fuente
- OpenClaw: Peter Steinberger (fundador de PSPDFKit) lo prototipó "en aproximadamente una hora" en noviembre de 2025. Pasó de 9k a más de 60k estrellas en pocos días a finales de enero de 2026, a más de 194-210k poco después, y a unas 388k el 26 de agosto de 2026. Se describe como el proyecto de crecimiento más rápido de la historia de GitHub, por delante de React — [N9O](https://n9o.xyz/posts/202602-steipete-openclaw-openai/), [Fortune](https://fortune.com/2026/02/19/openclaw-who-is-peter-steinberger-openai-sam-altman-anthropic-moltbook/), [GitHub Blog](https://github.blog/open-source/maintainers/openclaw-went-viral-meet-the-maintainers-building-and-securing-it/).
- Steinberger se incorporó a OpenAI el 14 de febrero de 2026 para liderar los "agentes personales de próxima generación". OpenClaw sigue siendo open source bajo una fundación independiente apoyada por OpenAI — [InfoWorld](https://www.infoworld.com/article/4132731/openai-hires-openclaw-founder-as-ai-agent-race-intensifies-2.html), [Fortune](https://fortune.com/2026/02/19/openclaw-who-is-peter-steinberger-openai-sam-altman-anthropic-moltbook/).
- El GitHub Blog dedicó un artículo a los mantenedores que "construyen y protegen" OpenClaw, lo que indica que la seguridad fue un problema importante tras la viralidad — [GitHub Blog](https://github.blog/open-source/maintainers/openclaw-went-viral-meet-the-maintainers-building-and-securing-it/).
- Otros: Langflow unos 146k, Dify unos 136k, Flowise unos 51k, AutoGen unos 60k, LangGraph unos 33k (el primero en "production-readiness"), OpenHands unos 83k. AutoGPT es históricamente el proyecto de agentes con más estrellas — [Fungies](https://fungies.io/top-github-repositories-ai-agent-frameworks-2026/), [Digital Applied](https://www.digitalapplied.com/blog/open-source-browser-computer-use-agents-2026). *Las cifras de estrellas varían según la fecha de la fuente.*
- Playwright MCP (unos 34k) y GitHub MCP (unos 31k) son los servidores MCP de proveedores con más estrellas. browser-use se distribuye también como servidor MCP — [Awesome MCP Tools](https://awesome-mcp.tools/blog/top-mcp-servers-2026), [Awesome Claude](https://awesomeclaude.ai/mcp/browser-automation).

### Inferencias: por qué se hacen virales
- (a) Utilidad personal inmediata con una sola instalación (OpenClaw funciona en tus propios canales de mensajería o en tu máquina). (b) Un creador carismático que construye en público. (c) Salir justo cuando aparece una nueva capacidad de los modelos (agentes, MCP, uso del ordenador). (d) Un nombre o mascota memorable (la "langosta"). (e) Licencia permisiva y extensibilidad (skills/plugins) que crean un ecosistema. Para un solo desarrollador: lanzar algo pequeño, divertido de enseñar en un GIF de 30 segundos, que se conecte a herramientas existentes (MCP) y que resuelva un dolor concreto.
- La viralidad trae problemas de seguridad (el caso de OpenClaw). Incorporar seguridad por defecto es tanto un diferenciador como un ángulo de "seguridad de agentes".

### Lagunas
- No encontré la ronda de financiación ni el número de estrellas actual de browser-use en esta búsqueda. Tampoco datos de adopción empresarial (clientes de pago) de OpenClaw.
