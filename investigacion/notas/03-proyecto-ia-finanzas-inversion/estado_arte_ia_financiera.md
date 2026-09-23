# Estado del arte: agentes LLM para finanzas e inversión (2024-2026)

> Notas de investigación, 23 de septiembre de 2026. Las estrellas de GitHub proceden de la API de GitHub consultada ese día. El proxy de salida bloqueó arxiv.org, nof1.ai, business-standard.com y aitradearena.com, así que varias cifras vienen de fragmentos de buscador y no de una lectura del texto completo. Las marco como tales.

## 1. Proyectos open source de IA financiera que se hicieron virales

### Takeaway
El segmento de "equipo de agentes LLM que analiza una acción" (ai-hedge-fund, TradingAgents y sus clones) es con diferencia el más viral: más de 100k estrellas en el caso de TradingAgents. Ninguno de estos proyectos demuestra rentabilidad fuera de muestra. Su atractivo es narrativo y visual (personas de Buffett o Munger, debates entre analistas alcistas y bajistas, "una firma de trading simulada"), no el rigor. En 2026 la idea ya es un commodity, con forks por mercado (China, A-shares).

### Cited Findings
**Estrellas a 23/09/2026 (API de GitHub)** — [búsqueda de GitHub](https://github.com/search?q=repo%3ATauricResearch%2FTradingAgents):
| Repo | Estrellas | Forks | Creado | Qué es |
|---|---|---|---|---|
| TauricResearch/TradingAgents | 108.284 | 20.732 | 28/12/2024 | Framework multiagente que imita una firma de trading |
| OpenBB-finance/OpenBB | 73.406 | 7.597 | 12/2020 | "Open Data Platform for analysts, quants and AI agents" (se reposicionó como capa de datos para agentes) |
| virattt/ai-hedge-fund | 63.685 | 11.164 | 29/11/2024 | "An AI Hedge Fund Team" con personas de inversores famosos |
| microsoft/qlib | 48.775 | 7.717 | 08/2020 | Plataforma de quant con ML; ahora integrada con RD-Agent |
| HKUDS/Vibe-Trading | 33.884 | 5.523 | 01/04/2026 | "Your Personal Trading Agent" (MCP, backtesting, multiagente) |
| hsliuping/TradingAgents-CN | 31.960 | 6.684 | 06/2025 | Fork de TradingAgents en chino |
| virattt/dexter | 27.618 | 3.414 | 14/10/2025 | "An autonomous agent for deep financial research" (TypeScript) |
| HKUDS/AI-Trader | 22.534 | 3.423 | 23/10/2025 | "100% Fully-Automated Agent-Native Trading" |
| AI4Finance-Foundation/FinGPT | 21.282 | 3.018 | 02/2023 | LLM financieros open source (fine-tunes en HF) |
| AI4Finance-Foundation/FinRL | 16.381 | 3.513 | 07/2020 | Aprendizaje por refuerzo profundo para trading |
| microsoft/RD-Agent | 14.729 | 1.928 | 04/2024 | Agente que automatiza la I+D (minería de factores y modelos sobre Qlib) |
| AI4Finance-Foundation/FinRobot | 8.068 | 1.360 | 02/2024 | Plataforma de agentes financieros |
| simonlin1212/TradingAgents-astock | 3.533 | 900 | 13/05/2026 | TradingAgents adaptado al mercado A de China |

- Crecimiento: una fuente de prensa cripto daba a ai-hedge-fund "51,7k estrellas y más de 9k forks" en su momento. Hoy tiene 63,7k, así que sigue creciendo — [KuCoin News](https://www.kucoin.com/news/flash/ai-hedge-fund-buffett-and-munger-agents-go-open-source-on-github); [PANews](https://panews.io/articles/019d8b96-c479-76fe-8854-f2f5f3e594e8).
- ai-hedge-fund: los agentes son personas LLM de inversores (Buffett, Munger, Graham, Lynch, Druckenmiller), "cuyo juicio es la ventaja". Debaten sobre los mismos datos y se fuerza un consenso. Soporta 13 proveedores de LLM, trae un módulo de backtesting y **no ejecuta operaciones reales**: es "solo educativo" — [KuCoin News](https://www.kucoin.com/news/flash/ai-hedge-fund-buffett-and-munger-agents-go-open-source-on-github); [repo](https://github.com/virattt/ai-hedge-fund).
- TradingAgents (paper arXiv 2412.20138): agentes especializados (analista fundamental, de sentimiento, de noticias y técnico, investigadores alcista y bajista, trader, equipo de riesgo). El backtest cubre **solo del 1 de enero al 29 de marzo de 2024** con AAPL, GOOGL y AMZN, y da un retorno acumulado del 23-27%. El periodo es muy corto y cae dentro del conocimiento de los modelos que se usaron — [arXiv](https://arxiv.org/abs/2412.20138); [DEV Community](https://dev.to/sangrokjung/tradingagents-v024-a-multi-agent-llm-framework-that-simulates-an-entire-trading-firm-g2e).
- TradingAgents se justifica como remedio al sesgo de confirmación de un único prompt gigante (cinco capas de roles), y su propio aviso reconoce que el rendimiento depende del modelo, la temperatura, el periodo y los datos — [DEV Community](https://dev.to/sangrokjung/tradingagents-v024-a-multi-agent-llm-framework-that-simulates-an-entire-trading-firm-g2e); [GitHub](https://github.com/tauricresearch/tradingagents).
- Crítica académica a esta familia de agentes: TradeTrap ("¿son fiables y fieles los agentes de trading basados en LLM?") señala que se presta poca atención a la fiabilidad, la consistencia y la robustez ante perturbaciones realistas. Un paper de septiembre de 2026 estudia cómo se propagan señales adversariales entre los agentes de un sistema multiagente de trading — [TradeTrap, arXiv 2512.02261](https://arxiv.org/pdf/2512.02261); [Contagion on the Trading Floor, arXiv 2609.19789](https://arxiv.org/pdf/2609.19789).
- En operativa real, la distancia entre el retorno simulado y el real es grande por costes de transacción, slippage y cambios de régimen — [Pinggy blog](https://pinggy.io/blog/best_ai_trading_agents/) (blog divulgativo, fuente débil).
- **Alpha Arena (Nof1), temporada 1**: seis LLM con 10.000 USD cada uno operando perpetuos cripto en Hyperliquid con dinero real (finales de 2025). DeepSeek V3.1 ganó un +10,11% y GPT-5 perdió un −39,73%. También participaron Qwen 3 Max, Claude 4.5 Sonnet, Gemini 2.5 Pro y Grok 4 — [Yahoo Finance/SCMP](https://finance.yahoo.com/news/deepseek-outperforms-ai-rivals-real-093000567.html); [nof1.ai](https://nof1.ai/).
- Alpha Arena, fase de acciones tecnológicas de EE. UU. (2026, temporada 1.5): la cartera en conjunto perdió cerca de un tercio del capital y solo hubo 6 resultados en beneficio de 32. El mejor fue Grok 4.20 en la variante en la que conocía el rendimiento de sus rivales. Nof1 prepara una temporada 2 con búsqueda web, más razonamiento, más fuentes y varios pasos. Solo lo he leído en el fragmento del buscador; el artículo estaba bloqueado — [Business Standard](https://www.business-standard.com/markets/news/ai-bots-auditioning-for-wall-street-trading-are-mostly-losing-money-126050701793_1.html).
- Críticas a Alpha Arena: una sola instancia de seis modelos en un horizonte muy corto, así que la muestra no vale nada, el ranking no significa nada y no se puede reproducir. El resultado es indistinguible de un paseo aleatorio. Los modelos operaban con apalancamientos de hasta 15x, sin herramientas y con un prompt que "induce alucinaciones" — [Boris Again (Substack)](https://borisagain.substack.com/p/why-alpha-arena-is-literally-the). Titular de prensa: "los modelos occidentales pierden un 80% del capital en una semana" — [Bitcoin Magazine](https://bitcoinmagazine.com/business/alpha-arena-reveals-ai-trading-flaws-western-models-lose-80-capital-in-one-week).
- Surgen alternativas y réplicas de las "arenas" (AI Trade Arena: "dimos 100.000 USD a 5 LLM para operar acciones durante 8 meses") — [aitradearena.com](https://www.aitradearena.com/research/we-ran-llms-for-8-months); [traderank.ai](https://www.traderank.ai/blog/alpha-arena-alternatives-2026).

### Inferences
- Viralidad ≈ narrativa antropomórfica (Buffett como agente, un comité que debate) + una demo con UI + un nombre ambicioso ("hedge fund", "trading firm") + un solo comando para ejecutarlo. La calidad metodológica no influye.
- Los mercados chino y de A-shares tienen su ecosistema propio de forks con decenas de miles de estrellas. No he encontrado un equivalente europeo o español: parece un hueco.
- Tendencia 2025-2026: los repos virales se desplazan de "equipo de agentes que emite una señal" a "agente de investigación profunda" (dexter) y a "agente personal con MCP" (Vibe-Trading), y OpenBB se reposiciona como capa de datos para agentes.

### Gaps
- No he encontrado hilos concretos de Hacker News con críticas a ai-hedge-fund. La búsqueda no los devolvió.
- No tengo series temporales de estrellas (star-history) ni datos de difusión en LinkedIn o X. El crecimiento se infiere solo de las fechas de creación y el total actual.
- No he podido leer de primera mano el informe técnico de Nof1 ni los resultados finales de la temporada 1.5 (dominios bloqueados).

## 2. Investigación y benchmarks: LLM para análisis financiero y trading

### Takeaway
Leer documentos financieros y hacer cálculos con ellos sigue lejos de estar resuelto. En tareas de analista agénticas realistas, los mejores modelos rondan el 50-60% de acierto en 2026, y los errores numéricos son el cuello de botella. En trading, los benchmarks libres de contaminación muestran que la mayoría de los agentes LLM no baten a comprar y mantener.

### Cited Findings
- **FinanceBench** (Islam et al., 2023): preguntas y respuestas con evidencia sobre filings públicos. GPT-4-Turbo con retrieval falló o se negó a responder en el 81% de las preguntas. En 8 configuraciones "realistas": 47% correctas, 26% incorrectas y 27% fallos. Solo cambiar el orden del prompt (contexto antes de la pregunta) mueve a GPT-4-Turbo del 25% al 78% — [Emergent Mind (resumen)](https://www.emergentmind.com/topics/financebench-dataset). Nota: la cifra de ">10.000 tripletas" es la del conjunto completo; la muestra abierta es menor.
- **Vals AI Finance Agent Benchmark** (arXiv 2508.00828): tareas realistas de analista (análisis cualitativo y cuantitativo, comparables, resultados trimestrales, disclosures, modelización) — [arXiv](https://arxiv.org/pdf/2508.00828); [Vals AI](https://www.vals.ai/home).
- Finance Agent v2 (2026): según agregadores, el mejor en septiembre de 2026 ronda el 60-61% (BenchLM cita a "Gemini 3.8 Flash" con 61,4%; llm-stats da otro líder con 0,598). Un artículo afirma que GPT-5.5 se queda en el 52%. **Poca fiabilidad**: son agregadores secundarios y se contradicen entre sí sobre el líder — [BenchLM](https://benchlm.ai/benchmarks/financeagentv2); [llm-stats](https://llm-stats.com/benchmarks/finance-agent-v2); [KuCoin blog](https://www.kucoin.com/blog/can-ai-replace-financial-analysts-in-2026-vals-ai-finance-agent-v2-reveals-gpt-5-5-hits-just-52-percent-accuracy).
- Vals Excel Modeling Benchmark (vía agregador): el mejor modelo pasa el 87% de las comprobaciones de fórmulas pero solo el 61% de las de números. La precisión numérica es el cuello de botella — [AIMultiple](https://aimultiple.com/finance-llm) (secundaria).
- **FinBen** (NeurIPS 2024 Datasets & Benchmarks): benchmark holístico. Su parte de QA numérico usa FinQA (preguntas de analistas sobre filings del S&P 500 de 1999 a 2019, con razonamiento numérico de varios pasos) y TAT-QA (tablas de informes anuales con texto corto, preguntas más extractivas) — [FinBen, NeurIPS](https://proceedings.neurips.cc/paper_files/paper/2024/file/adb1d9fa8be4576d28703b396b82ba1b-Paper-Datasets_and_Benchmarks_Track.pdf).
- Alucinaciones numéricas: una línea activa de trabajo en 2025-2026 (FRED, HalluBench/FinReflectKG, "Confidently Wrong", "Fighting Numerical Hallucinations via Data-centric Compilation"). Un paper de SSRN concluye que la **verificación determinista (recalcular simbólicamente) supera al chain-of-thought** y generaliza a TAT-QA — [SSRN, Thokal](https://papers.ssrn.com/sol3/Delivery.cfm/6856159.pdf?abstractid=6856159&mirid=1); [arXiv 2605.31064](https://arxiv.org/html/2605.31064); [arXiv 2507.20930](https://arxiv.org/pdf/2507.20930).
- El fine-tuning financiero no elimina las alucinaciones numéricas ("When Financial Fine-tuning Fails", septiembre de 2026) — [arXiv 2609.04806](https://arxiv.org/html/2609.04806).
- **StockBench** (octubre de 2025): benchmark libre de contaminación para operar acciones durante varios meses, con precios, fundamentales y noticias diarias. Evalúa GPT-5, Claude-4, Qwen3, Kimi-K2 y GLM-4.5. **La mayoría no bate a comprar y mantener**, y ser bueno en conocimiento financiero estático no se traduce en trading rentable — [arXiv 2510.02209](https://arxiv.org/abs/2510.02209); [stockbench.github.io](https://stockbench.github.io/).
- Otros benchmarks: INVESTORBENCH (decisiones financieras con agentes), FinTradeBench, BizFinBench.v2 (evaluación online y offline con datos de usuarios reales), AlphaForgeBench (diseño de estrategias de principio a fin), Scale PRBench-Finance, y FinVerBench (validez y calibración al verificar estados financieros) — [INVESTORBENCH](https://arxiv.org/pdf/2412.18174); [FinTradeBench](https://arxiv.org/pdf/2603.19225); [BizFinBench.v2](https://arxiv.org/pdf/2601.06401); [AlphaForgeBench](https://arxiv.org/html/2602.18481v2); [Scale PRBench](https://labs.scale.com/leaderboard/prbench-finance); [FinVerBench](https://arxiv.org/html/2605.29586).
- Sin ground truth: GAUGE propone evaluar modelos financieros construidos por agentes sin una "respuesta dorada" — [arXiv 2607.24889](https://arxiv.org/pdf/2607.24889).
- Benchmarks de forecasting libres de contaminación por construcción, con eventos posteriores al corte (por ejemplo, el Mundial 2026 frente a una casa de apuestas) — [arXiv 2607.17765](https://arxiv.org/pdf/2607.17765).

### Inferences
- "Leer un 10-K y responder bien" funciona para extraer datos, pero falla en cálculos de varios pasos y en recuperar el fragmento correcto. Un proyecto serio debe separar la extracción (LLM con cita) del cálculo (código).
- Que las cifras de líderes de benchmark difieran entre agregadores indica que conviene citar la fuente primaria (vals.ai) y la fecha de la foto.

### Gaps
- No he podido verificar en fuente primaria (vals.ai) la tabla actual de Finance Agent v2. Los nombres de modelos de los agregadores no están confirmados.
- No he encontrado cifras actualizadas de 2026 de FinQA o TAT-QA con modelos frontera (probablemente estén saturados, pero no está confirmado).
- No encontré el estudio "LLMs as stock pickers" con nombre propio aparte de StockBench, Look-Ahead-Bench y AI Trade Arena.

## 3. Trampas metodológicas

### Takeaway
La trampa central y específica de los LLM es el **sesgo de anticipación (look-ahead) guardado en los pesos**: el modelo ya "sabe" qué pasó durante su periodo de entrenamiento. Por eso cualquier backtest anterior a la fecha de corte está contaminado aunque el pipeline de datos sea impecable. En 2025-2026 la literatura lo ha cuantificado: el Sharpe cae entre un 50% y un 72% y el alfa se hunde en cuanto se sale de la ventana de conocimiento. A esto se suman los problemas clásicos: supervivencia, sobreajuste, costes, muestras pequeñas y alucinaciones numéricas.

### Cited Findings
- **Profit Mirage** (arXiv 2510.07920, octubre de 2025): FinGPT, FinMem, FinReport y Hedge-Agents declaraban retornos anualizados de dos o tres cifras en backtests (EE. UU., Hong Kong, A-shares) que desaparecen al pasar la fecha de corte. **El Sharpe cae entre un 50% y un 71,85%** tras cerrarse la ventana de conocimiento, aunque el mercado estuviera estable. Causa: el corpus de entrenamiento incluye explicaciones a posteriori de movimientos de precio. Publican FinLake-Bench (evaluación robusta a filtraciones) y FactFin (perturbaciones contrafactuales) — [arXiv](https://arxiv.org/abs/2510.07920); [ResearchGate](https://www.researchgate.net/publication/396373592_Profit_Mirage_Revisiting_Information_Leakage_in_LLM-based_Financial_Agents).
- **Look-Ahead-Bench** (arXiv 2601.13770, enero de 2026): mide el sesgo en flujos de trabajo realistas, no con preguntas de memoria. **DeepSeek 3.2 pasa de +20,73% de alfa anualizado dentro de muestra a −1,04% fuera**. Pitinf-Large, un LLM point-in-time, pasa de +6,02% a +7,32%. Llama 3.1 8B y 70B también muestran sesgo. Código en GitHub — [arXiv](https://arxiv.org/abs/2601.13770); [benstaf/lookaheadbench](https://github.com/benstaf/lookaheadbench); [vBase blog](https://www.vbase.com/blog/llm-alpha-look-ahead-bias/).
- **Detecting Lookahead Bias in LLM Forecasts** (Gao, Jiang, Yan; arXiv 2512.23847): la parte de la capacidad predictiva que dependía de resultados memorizados por empresa y día desaparece cuando el modelo ya no puede haberlos memorizado. Es una "firma de memorización" útil como test — [arXiv](https://arxiv.org/pdf/2512.23847).
- Mitigaciones propuestas: (a) modelos entrenados con un corte estricto y datado (DatedGPT, arXiv 2603.11838; Pitinf); (b) ajustar los logits con dos modelos pequeños, uno "a olvidar" y otro "a retener" (arXiv 2512.06607); (c) FinCAD, decodificación consciente del contexto en inferencia (arXiv 2605.24564: "Summoning the Oracle to Slay It"); (d) HindsightBench, un protocolo de auditoría de caja negra (arXiv 2607.18867); (e) puntuaciones ajustadas por filtración temporal (arXiv 2608.02985) — [DatedGPT](https://arxiv.org/html/2603.11838); [2512.06607](https://arxiv.org/abs/2512.06607); [2605.24564](https://arxiv.org/abs/2605.24564); [HindsightBench](https://arxiv.org/pdf/2607.18867); [Temporal Leakage](https://arxiv.org/pdf/2608.02985).
- Un LLM con corte en 2025 ya ha visto cómo se movieron NVIDIA, Microsoft y Netflix entre 2010 y 2020. Este sesgo vive en los pesos y es invisible a una auditoría del pipeline de datos — [arXiv 2605.24564](https://arxiv.org/html/2605.24564).
- Muestra pequeña y suerte: una semana de buena racha es estadísticamente normal y no demuestra capacidad (crítica a Alpha Arena) — [Boris Again](https://borisagain.substack.com/p/why-alpha-arena-is-literally-the).
- Los agentes basados en LLM son poco fiables y consistentes ante perturbaciones (TradeTrap), y las señales adversariales se contagian entre agentes — [2512.02261](https://arxiv.org/pdf/2512.02261); [2609.19789](https://arxiv.org/pdf/2609.19789).
- El backtest de TradingAgents (tres meses de 2024, tres megacaps tecnológicas) es un ejemplo de manual de ventana corta, universo sesgado hacia los supervivientes y un periodo que los modelos base conocen — [arXiv 2412.20138](https://arxiv.org/abs/2412.20138).

### Inferences
- Cualquier cifra de backtest de un agente LLM anterior a la fecha de corte del modelo debería tratarse por defecto como no creíble. Lo mínimo honesto es mostrar a la vez la cifra antes y después del corte.
- También son relevantes, aunque no los he documentado aquí con fuente específica de LLM: el sesgo de supervivencia (usar los componentes actuales de un índice), los datos no point-in-time (fundamentales reexpresados), los costes y el slippage, el snooping por probar muchos prompts o modelos sobre el mismo periodo, y el no determinismo de los LLM (repetir cada ejecución N veces).
- El coste de inferencia es una trampa práctica: un comité de ~10 agentes por ticker y día multiplica las llamadas.

### Gaps
- No he encontrado un estudio con cifras de coste en dólares por decisión de estos frameworks multiagente.
- No he encontrado un estudio específico sobre sesgo de supervivencia en agentes LLM. Es conocimiento general de finanzas cuantitativas, sin fuente citada aquí.

## 4. Qué haría destacar en 2026 a un proyecto individual técnicamente impresionante y honesto

### Takeaway
"Hedge fund multiagente" ya está muy visto (más de 100k estrellas repartidas en decenas de clones). La diferenciación creíble está en **evaluación honesta y libre de contaminación**, **números verificables con cita al documento** y un **nicho sin cubrir** (mercado español o europeo con filings ESEF/XBRL, en español). El proyecto debería vender rigor y transparencia, no rentabilidad.

### Cited Findings
- La ruta creíble que marca la literatura: evaluar solo después de la fecha de corte del modelo (walk-forward o en vivo), o usar modelos point-in-time, y publicar la caída de alfa o Sharpe antes y después del corte — [Look-Ahead-Bench](https://arxiv.org/abs/2601.13770); [Profit Mirage](https://arxiv.org/abs/2510.07920).
- Comparar siempre con comprar y mantener: en StockBench la mayoría de agentes no lo bate — [StockBench](https://arxiv.org/abs/2510.02209).
- La verificación determinista y el recálculo simbólico superan al chain-of-thought para los números financieros. Esto justifica calcular con herramientas (Python o SQL) y no con el LLM — [SSRN](https://papers.ssrn.com/sol3/Delivery.cfm/6856159.pdf?abstractid=6856159&mirid=1).
- Las arenas en vivo atraen mucha atención (Alpha Arena), pero reciben críticas por su muestra pequeña, el apalancamiento y la falta de reproducibilidad. Una arena con paper trading, muchas semillas, intervalos de confianza y registros públicos respondería directamente a esas críticas — [Boris Again](https://borisagain.substack.com/p/why-alpha-arena-is-literally-the); [Business Standard](https://www.business-standard.com/markets/news/ai-bots-auditioning-for-wall-street-trading-are-mostly-losing-money-126050701793_1.html).
- Datos europeos disponibles: ESEF/iXBRL es obligatorio para los informes anuales de emisores en mercados regulados de la UE. filings.xbrl.org ofrece los paquetes ESEF, un visor y versión xBRL-JSON, con un índice en JSON. ESMA publica un toolkit en Python (esef_toolkit). La mayoría de países no tiene API propia — [XBRL International](https://www.xbrl.org/news/xbrl-international-launches-filings-xbrl-org-for-esef-filings/); [xbrl.org, nuevas filings](https://www.xbrl.org/news/new-esef-filings-and-countries-available-catch-up-on-filings-xbrl-org/); [ESMA esef_toolkit](https://github.com/European-Securities-Markets-Authority/esef_toolkit).
- Los forks por mercado (TradingAgents-CN con 32k estrellas, TradingAgents-astock con 3,5k) demuestran demanda de versiones localizadas por mercado e idioma — [GitHub CN](https://github.com/hsliuping/TradingAgents-CN); [GitHub astock](https://github.com/simonlin1212/TradingAgents-astock).
- El giro hacia la "investigación profunda" (dexter, 27,6k estrellas en menos de un año) indica que un agente que investiga y cita puede ser tan atractivo como uno que opera — [virattt/dexter](https://github.com/virattt/dexter).

### Inferences
Posibles ingredientes para destacar, de más a menos diferenciador:
1. **Evaluación libre de contaminación como producto**: un leaderboard de paper trading en vivo solo con fechas posteriores al corte de cada modelo, con decisiones registradas y sellado de tiempo (hash o commit antes de conocer el resultado), N ejecuciones por decisión, intervalos de confianza y comparación con comprar y mantener y con el índice. Se puede contar como "el anti-Alpha Arena".
2. **Una "prueba de memorización" como feature**: aplicar la idea de Look-Ahead-Bench o de la firma de memorización a cualquier estrategia que suba el usuario, y mostrar la caída antes y después del corte.
3. **Números con cita obligatoria**: cada cifra enlaza al hecho XBRL o a la página del filing. El cálculo se hace en SQL o Python y hay una evaluación propia (tipo FinanceBench) sobre empresas del IBEX o del Euro Stoxx con respuestas verificadas.
4. **Nicho España/UE en español**: filings ESEF (filings.xbrl.org), CNMV y el IBEX 35. No he encontrado un equivalente viral (hay que confirmarlo con una búsqueda en GitHub).
5. **Enfoque de finanzas personales o de explicación** (análisis de una empresa para un inversor minorista, con riesgos citados) en lugar de señales de compraventa. Además reduce el riesgo regulatorio de parecer asesoramiento.
6. Coste por análisis medido y publicado, y evals en CI.

### Gaps
- No he verificado si ya existe un proyecto open source relevante enfocado en ESEF o IBEX con LLM. Hace falta una búsqueda específica en GitHub.
- No he revisado las implicaciones regulatorias (MiFID II o CNMV sobre recomendaciones de inversión automatizadas) de publicar señales. Conviene investigarlo aparte.
- No he encontrado datos sobre qué tipo de publicación (LinkedIn o X) generó la viralidad de cada repo.
