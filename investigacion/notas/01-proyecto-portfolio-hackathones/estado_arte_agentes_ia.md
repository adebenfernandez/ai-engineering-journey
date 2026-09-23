# State of the art in AI agents and LLM application engineering (Sept 2026): what a junior developer can build and show in a portfolio

Scope: an individual junior developer who already knows the Claude Messages API with tool use, basic RAG with ChromaDB, FastAPI and Docker. Research date: 2026-09-23. About 15 tool calls. Where sources are aggregators or vendor blogs, this is noted.

---

## 1. Agent frameworks and building blocks in 2026: which are mature and which are hype?

### Takeaway
The field has settled around a few layers. (1) Model provider SDKs with a built-in agent loop: the Anthropic SDK tool runner and the Claude Agent SDK; the OpenAI Agents SDK. (2) Graph or state orchestrators for durable, auditable workflows: LangGraph. (3) Type-safe structured-output frameworks: PydanticAI. (4) MCP, now a Linux Foundation standard, as the integration layer. (5) Hosted agent runtimes such as Claude Managed Agents, in public beta since April 2026. For a solo developer, a thin loop on the Anthropic SDK plus a custom MCP server plus evals usually looks more credible than a heavy multi-agent framework.

### Cited Findings
- **Claude Agent SDK**: exposes the tooling behind Claude Code (reading files, running commands, web search, editing code) as a programmable framework in Python and TypeScript. It is built around bash execution, file writes and a hook system, on the view that "a capable agent needs a real shell." — [morphllm framework comparison](https://www.morphllm.com/ai-agent-framework) (aggregator); [Medium / Data Science Collective, Sep 2026](https://medium.com/data-science-collective/the-best-agent-framework-in-2026-langgraph-vs-openai-agents-sdk-vs-claude-agent-sdk-2c64e0b378d9)
- The Anthropic Agent SDK provides an agent loop, a tool-use protocol, streaming, session persistence and OpenTelemetry observability. Releases in 2026 added sessions, checkpointing, cost tracking and telemetry export. — [Augment Code guide](https://www.augmentcode.com/guides/anthropic-agent-sdk-what-ships-vs-what-you-build) (third party)
- **Tool runner (Anthropic SDK)**: documented as an official SDK feature that runs the tool-call loop automatically. Recent releases fixed the runner so it continues after `pause_turn`, and moved the files and skills namespaces to their GA (non-beta) shapes. — [Tool runner docs](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-runner); [anthropic-sdk-python releases](https://github.com/anthropics/anthropic-sdk-python/releases). Note: sources disagree on the SDK version. One reports v0.121.0 in Aug 2026, while the search snippet cites v1.1.0 and v1.2.0 release notes. Check with `pip index versions anthropic`.
- **Claude Managed Agents**: public beta launched on the Claude Platform on 8 April 2026. It is a set of composable APIs that pairs an Anthropic-managed harness (agent loop, tool execution, sandbox container, state persistence) with infrastructure for memory, permissions and scheduled execution. Anthropic markets it as getting to production "10x faster". Netflix is cited as a user. — [Claude blog](https://claude.com/blog/claude-managed-agents); [Managed Agents overview docs](https://platform.claude.com/docs/en/managed-agents/overview); [9to5Mac, May 2026 (three new features)](https://9to5mac.com/2026/05/07/anthropic-updates-claude-managed-agents-with-three-new-features/)
- Managed Agents pricing: tokens at the standard model rates plus **$0.08 per session-hour** of `running` time. Idle time is not billed, and there is no Batch discount. Anthropic's worked example: a one-hour Opus 5 session with 50k input and 15k output tokens costs about $0.70. — [Anthropic pricing page](https://platform.claude.com/docs/en/about-claude/pricing)
- **Computer use / browser use**: now shipped as toolsets (`computer_toolset_20260801` and `browser_toolset_20260801`) that add about 4,500 and about 6,600 input tokens per request respectively, plus screenshot image tokens. — [Anthropic pricing page](https://platform.claude.com/docs/en/about-claude/pricing)
- Server tools: web search costs $10 per 1,000 searches. Web fetch has no extra charge. Code execution is free when used with the web search or web fetch tools (versions `_20260209` and later). Otherwise each org gets 1,550 free hours per month, then $0.05 per container-hour. — [Anthropic pricing page](https://platform.claude.com/docs/en/about-claude/pricing)
- **LangGraph**: a graph runtime where nodes are functions and edges are transitions, with a typed state and checkpointers that persist state at every node. Runs can resume after a crash or a human-approval pause. Described as "the production standard for stateful, auditable agentic workflows" in 2026. — [morphllm](https://www.morphllm.com/ai-agent-framework) (aggregator)
- **OpenAI Agents SDK**: its primitives are agents, handoffs, guardrails and sessions. An April 2026 overhaul added native sandboxing, sub-agents, Codex-style filesystem tools and first-class MCP support. — [morphllm](https://www.morphllm.com/ai-agent-framework)
- **PydanticAI**: best suited to type-safe structured output (extraction, form processing, classification). It is often combined with LangGraph or CrewAI when orchestration is needed. — [morphllm](https://www.morphllm.com/ai-agent-framework)
- Frameworks listed as leading open-source options (July 2026): LangGraph, LangChain DeepAgents, OpenAI Agents SDK, Claude Agent SDK, Google ADK, Pydantic AI, CrewAI, Strands Agents, Mastra, Vercel AI SDK, Microsoft Agent Framework, Agno, smolagents. Suggested defaults: Mastra for TypeScript teams, LangGraph for Python with heavy orchestration, the Agents SDK for OpenAI-committed teams. The source claims that "framework choice moves agent benchmark performance by up to 30 percentage points on identical models" (unverified vendor-blog claim). — [morphllm](https://www.morphllm.com/ai-agent-framework)
- A practitioner comparison from Langfuse that covers LangGraph, OpenAI Agents SDK, smolagents, CrewAI, AutoGen, Semantic Kernel, LlamaIndex and PydanticAI — [Langfuse blog](https://langfuse.com/blog/2025-03-19-ai-agent-comparison)
- **MCP**: Anthropic donated MCP to the Agentic AI Foundation (AAIF) under the Linux Foundation in **December 2025**. OpenAI and Block are co-founders, and AWS, Google, Microsoft, Cloudflare, GitHub and Bloomberg are supporting members. — [WorkOS, MCP in 2026](https://workos.com/blog/everything-your-team-needs-to-know-about-mcp-in-2026)
- **MCP spec 2026-07-28** (the most recent major revision): the protocol becomes **fully stateless**. The `initialize`/`initialized` handshake and the `Mcp-Session-Id` header are removed. Auth is hardened, a formal 12-month deprecation policy is set, and **interactive server-rendered UIs** and **long-running async tasks** become official extensions. — [AAIF blog: MCP 2026-07-28 migration](https://aaif.io/blog/mcp-2026-07-28-whats-changing-and-how-to-migrate); [VentureBeat](https://venturebeat.com/infrastructure/mcp-just-got-its-biggest-update-ever-heres-what-changes-for-ai-agents); [Google Developers Blog on stateless MCP](https://developers.googleblog.com/scaling-ai-agent-infrastructure-with-the-mcp-stateless-updates/)
- The MCP Registry launched in September 2025 and grew to about 2,000 server entries within months. The roadmap includes "MCP Server Cards", metadata published at `.well-known` URLs. — [WorkOS](https://workos.com/blog/everything-your-team-needs-to-know-about-mcp-in-2026)

### Inferences
- **Mature and safe to showcase**: the Anthropic SDK tool use and tool runner, MCP (a standard now, not hype), LangGraph for workflows that need checkpoints and human-in-the-loop, PydanticAI or native structured outputs for extraction. **Real but still beta**: Managed Agents. It is useful to mention, but relying on it ties the demo to a beta API. **More hype than substance for a solo portfolio**: multi-agent "crews" with role-play personas (CrewAI-style) with no measurable gain. Judges increasingly ask why you need multiple agents.
- Supporting the new stateless MCP spec (2026-07-28), for example with Streamable HTTP and no session state so the server deploys on serverless, is a concrete "up to date" signal few hobby projects have.
- Because the developer already knows raw tool use, a good story is: "I wrote the loop myself first, then compared it with the tool runner or LangGraph." That shows understanding rather than framework dependence.

### Gaps
- Could not fetch primary docs for the Claude Agent SDK or OpenAI Agents SDK changelogs (docs.anthropic.com is blocked by the proxy). Framework feature claims come mostly from aggregator blogs.
- No reliable adoption metrics (such as downloads or stars as of Sept 2026) were collected for the frameworks.

---

## 2. What makes a project "advanced": evals, observability, guardrails, structured outputs, agentic RAG, multimodal, caching, HITL, deployment

### Takeaway
The clearest signal of seniority is **systematic evaluation**: error analysis on real traces, then binary pass/fail checks (code-based first, LLM-as-judge second), tracked over time. Second come **tracing/observability** (OpenTelemetry, Langfuse), **cost engineering** (prompt caching, model routing Haiku→Sonnet, Batch) and **security thinking** (prompt-injection threat model). RAG and multimodal count only when they are measured.

### Cited Findings
- Hamel Husain and Shreya Shankar's "AI Evals FAQ" (updated Sept 2026): in their projects, **60-80% of development time** went to error analysis and evaluation, mostly looking at data rather than building automated checks. — [hamel.dev evals FAQ](https://hamel.dev/blog/posts/evals-faq/)
- Hamel's recommended order: **binary pass/fail instead of Likert scales**, **error analysis before metrics**, **code-based checks before LLM judges**. Only build an LLM-as-judge when the failure mode justifies the investment. — [Hamel Husain Substack](https://hamelhusain.substack.com/p/ai-evals-for-engineers-and-product); [Lenny's Newsletter interview](https://www.lennysnewsletter.com/p/evals-error-analysis-and-better-prompts); [Pragmatic Engineer guide to evals](https://newsletter.pragmaticengineer.com/p/evals)
- Hamel has published "evals skills" for coding agents (a repo). Evals can now be scaffolded with Claude Code or other agents. — [Evals Skills for Coding Agents](https://hamelhusain.substack.com/p/evals-skills-for-coding-agents); [hamelsmu/evals-skills](https://github.com/hamelsmu/evals-skills/blob/main/questions.md)
- Research caution on LLM judges: a 2026 arXiv paper, "Nine Judges, Two Effective Votes", finds that correlated errors undermine panels of LLM judges. Adding more judges does not add independent signal. — [arXiv 2605.29800](https://arxiv.org/pdf/2605.29800)
- The Anthropic Agent SDK ships OpenTelemetry observability and cost tracking — [Augment Code](https://www.augmentcode.com/guides/anthropic-agent-sdk-what-ships-vs-what-you-build)
- Prompt caching: automatic caching with a single top-level `cache_control`, or explicit breakpoints. A 5-minute cache write costs 1.25x the base input price, a 1-hour write 2x, and a cache read 0.1x (0.05x on Opus 5.5, 0.025x on Fable 5.1). A 5-minute cache pays off after one read. Batch API gives **50% off** and stacks with caching. — [Anthropic pricing page](https://platform.claude.com/docs/en/about-claude/pricing)
- Claude 4.6 and later models include the full **1M-token context at standard pricing** — [Anthropic pricing page](https://platform.claude.com/docs/en/about-claude/pricing)
- Claude 4.7 and later use a new tokenizer that produces about **30% more tokens for the same text**. This matters when comparing costs with older models. — [Anthropic pricing page](https://platform.claude.com/docs/en/about-claude/pricing)
- Structured outputs via tool schemas: passing a schema generates a tool the model calls to return validated, typed data (Strands docs describing the Anthropic provider) — [Strands Agents docs](https://strandsagents.com/docs/user-guide/concepts/model-providers/anthropic/)
- Human-in-the-loop: LangGraph checkpointers let a workflow pause for human approval and resume without losing state — [morphllm](https://www.morphllm.com/ai-agent-framework)
- Security: Simon Willison's "lethal trifecta" says an agent is dangerous when it has private data, exposure to untrusted content, and a way to communicate externally. MCP makes this easy to assemble by accident. Real incidents include GitHub's MCP server (private repo exfiltration via a malicious public issue), Atlassian's MCP server and Notion's agent (hidden white-on-white text in a PDF). — [Simon Willison, The lethal trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/); [Simon Willison on X re: Atlassian](https://x.com/simonw/status/1935833695874957328); [re: Notion](https://x.com/simonw/status/1969111931152634010)
- Academic threat models: "The Promptware Kill Chain" (arXiv 2601.09625); "Securing the Model Context Protocol" (arXiv 2511.20920) — [arXiv 2601.09625](https://arxiv.org/pdf/2601.09625); [arXiv 2511.20920](https://arxiv.org/pdf/2511.20920)
- Hackathon trend data: agentic AI, RAG and multimodal are cited as "the three strongest categories for high judging scores" (Devpost trend data as quoted by NextAgile; secondary source) — [NextAgile](https://nextagile.ai/blogs/gen-ai/top-hackathon-project-ideas/)

### Inferences
- A concrete "advanced" checklist for this developer:
  - A golden dataset of 30-100 real queries with binary pass/fail labels, including adversarial and out-of-scope cases.
  - An eval harness run in CI (pytest plus an LLM-judge validated against human labels, with a reported agreement rate).
  - Traces in Langfuse or another OTel backend, with per-request cost and latency shown in the README.
  - Hybrid retrieval (BM25 plus embeddings) with a reranker, plus a before/after table (recall@k, faithfulness).
  - Prompt caching on the system prompt and tools, with the measured % cache hits and $ saved.
  - Model routing: Haiku 4.5 for classification and extraction, Sonnet 5 for reasoning.
  - Structured outputs validated with Pydantic.
  - A human-approval step for irreversible actions.
  - A written threat model based on the lethal trifecta.
- Citations back to source (for example a BOE article ID or an AEMET station ID) are the main anti-hallucination feature in legal and public-data domains. They are also easy to test automatically, because you can check that each cited ID exists.
- Because the tokenizer changed, cost benchmarks in the README should name the model version.

### Gaps
- No primary 2026 sources were fetched on Langfuse features, OpenTelemetry GenAI semantic conventions status, or rerankers (Cohere Rerank, bge-reranker, Voyage). The recommendations above rely on general knowledge and need verification.
- Nothing specific was found on voice pipelines or on vision over satellite imagery with Claude in 2026.
- Claude's native "structured outputs" feature (constrained JSON output) status and name were not confirmed from primary docs, because docs.anthropic.com is blocked.

---

## 3. Is a custom MCP server for Spanish open data novel? Existing servers for BOE, AEMET, INE, Catastro, datos.gob.es

### Takeaway
**No, it is not novel on its own.** GitHub already has several MCP servers for the BOE (the most-starred has about 48 stars), AEMET (at least 6), INE (at least 6), and at least two aggregate servers covering BOE + INE + datos.gob.es + BDNS. They are all small (under 50 stars), so none dominates. A project can still stand out through (a) quality: evals, tests, stateless 2026-07-28 spec, deployed remote endpoint, registry listing; (b) a less-covered source such as **Catastro** (no dedicated MCP server found), SIGPAC/FEGA, CNIG or Copernicus; (c) combining sources into a vertical use case for a real user group rather than a generic API wrapper.

### Cited Findings (GitHub search, 2026-09-23)
- **BOE**:
  - [ComputingVictor/MCP-BOE](https://github.com/ComputingVictor/MCP-BOE): Python, **48 stars / 15 forks**, created Aug 2025, updated Aug 2026. Covers consolidated legislation, daily summaries and reference tables, with MCP plus a REST API.
  - [AnCode666/boe-mcp](https://github.com/AnCode666/boe-mcp): Python, 6 stars.
  - [anamtb/boe-mcp](https://github.com/anamtb/boe-mcp): TypeScript, 2 stars.
  - [QuantumBBoy/boe-mcp](https://github.com/QuantumBBoy/boe-mcp): 0 stars.
  - [jorditg77/subastas-boe-api](https://github.com/jorditg77/subastas-boe-api): BOE judicial auctions, REST + MCP, 3 stars.
- **Tax / AEAT**: [iMark21/aeat-mcp](https://github.com/iMark21/aeat-mcp): TypeScript, 13 stars, created March 2026. Covers IRPF, IVA, regional deductions and crypto, and uses only official sources.
- **AEMET**:
  - [AnCode666/aemet-mcp](https://github.com/AnCode666/aemet-mcp): Python, 5 stars, created April 2025.
  - [hgboro/aemet-mcp-server](https://github.com/hgboro/aemet-mcp-server): "36 real-time weather tools", 1 star.
  - [jocarrd/aemet-client](https://github.com/jocarrd/aemet-client): typed TS SDK plus MCP, "used in production at snowy.es".
  - [rldona/aemet-mcp](https://github.com/rldona/aemet-mcp), [mmillan76/aemet-mcp](https://github.com/mmillan76/aemet-mcp): both created July 2026.
  - [RaulRC/spanish-grid-mcp](https://github.com/RaulRC/spanish-grid-mcp): REE/ESIOS electricity plus AEMET, built with FastMCP.
  - Note: [Alysiadeceptive64/aemet-client](https://github.com/Alysiadeceptive64/aemet-client) looks like a copy of jocarrd/aemet-client with keyword-stuffed topics. Treat it as suspicious.
- **INE**:
  - [AnCode666/ine-mcp](https://github.com/AnCode666/ine-mcp): 2 stars.
  - [agmalaga2020/ine-universal-mcp](https://github.com/agmalaga2020/ine-universal-mcp): "deploy-ready for Render Free Tier".
  - [manalejandro/mcp-ine](https://github.com/manalejandro/mcp-ine): runs on Cloudflare Workers.
  - [pipeworx-io/mcp-ine-es](https://github.com/pipeworx-io/mcp-ine-es): an auto-generated family of servers from a vendor.
  - [dcerecedo/ine-mcp](https://github.com/dcerecedo/ine-mcp), [dlbcodes/ine-mcp](https://github.com/dlbcodes/ine-mcp).
  - [Karim-capatlas/spain-address-autocomplete](https://github.com/Karim-capatlas/spain-address-autocomplete): address normalization over 749k INE records.
- **Multi-source aggregators**:
  - [mjgmario/spanish-public-info-radar-mcp](https://github.com/mjgmario/spanish-public-info-radar-mcp): Python, 5 stars. Covers grants (BDNS), BOE/BORME, INE and datos.gob.es.
  - [aplaceforallmystuff/spain-ai-kit](https://github.com/aplaceforallmystuff/spain-ai-kit): TypeScript, 9 stars, 15 open issues, updated Sept 2026. "MCP servers connecting AI applications to Spanish government open data and legal infrastructure" (BOE, INE).
- **Catastro**: a combined query (`mcp INE spain OR catastro OR datos.gob.es`) returned **no dedicated Catastro MCP server**. datos.gob.es appears only inside the aggregator above.

### Inferences
- Pitching "the first MCP server for the BOE/AEMET/INE" would be false and easy for a juror to check. Present it instead as "an MCP server focused on X for user group Y, with evals and a deployed endpoint."
- Candidate niches that look open: **Catastro** (parcel data, cadastral references, possibly combined with SIGPAC agricultural parcels), a **combined agro-climate server** (AEMET + SIGPAC + FEGA/CAP aid calendar + BOE aid calls), **BDNS subsidy matching** for rural users, or regional open-data portals (Junta de Andalucía, Generalitat, and others).
- Contributing a PR to an existing server (for example MCP-BOE) is itself a credible portfolio signal. Recruiters value open-source collaboration.

### Gaps
- GitHub search is by keyword. Servers named differently (for example "sede-catastro", "spain-cadastre") or hosted on GitLab or PyPI only may have been missed. A follow-up search for "catastro" alone and "cadastre spain mcp" is recommended.
- The MCP Registry (registry.modelcontextprotocol.io) was not queried directly.

---

## 4. Examples of impactful AI-agent projects (public sector, agriculture, climate, finance) from 2025-2026 and what made them stand out

### Takeaway
Winning projects share a pattern: a **specific underserved user group**, an **accessible channel** (WhatsApp or voice, in local languages), integration with **official data or documents**, and an output the user can act on right away (a claim pack, a fertilizer plan, a salinity alert). Impact themes such as climate, financial inclusion and accessibility are weighted heavily. A simpler project that nails the impact story often beats a more complex one.

### Cited Findings
- **Kisan Mitra AI** (winner, AWS "AI for Bharat" Hackathon, June 2026, team Jay Jawan Jay Kisan). A GenAI assistant for digitally underserved farmers. It turns soil-health reports into fertilizer recommendations, grades crops from images, and supports voice in regional dialects. Built on Amazon Bedrock, Textract and Rekognition. — [YourStory](https://yourstory.com/2026/06/crop-insurance-conversational-analytics-ai-for-bharat-hackathon)
- A **WhatsApp-first crop-insurance claims system** from the same hackathon covers seven Indian languages. It validates documents and images with AI and generates insurer-ready claim packs. — [YourStory](https://yourstory.com/2026/06/crop-insurance-conversational-analytics-ai-for-bharat-hackathon)
- **Grameen-AI**: twelve WhatsApp-styled AI agents for Indian farmers, sellers and workers (prices, credit, health, government schemes), built for the SerpApi India Hackathon 2026 — [GitHub aditya1233745/Grammen-AI](https://github.com/aditya1233745/Grammen-AI)
- **UNDP Viet Nam Youth Digital Citizen Challenge 2025 (AI for Climate Action)**: the first prize went to an AI salinity-forecasting solution for farmers. Farming and aquaculture solutions led the rankings. — [UNDP Viet Nam](https://www.undp.org/vietnam/press-releases/ai-farming-and-aquaculture-solutions-top-youth-climate-hackathon)
- Other agriculture hackathons in 2026: the University of Illinois CDA Precision & Digital Agriculture Hackathon (March 2026) and HACK CORE 2026 (IIT Ropar ANNAM.AI + Syngenta + Google) — [Illinois CDA](https://digitalag.illinois.edu/2026/03/31/cda-celebrates-2026-cu-agtech-week-by-hosting-precision-digital-agriculture-hackathon-and-cda-conference-on-generative-ai-in-agriculture/); [CSR Universe](https://thecsruniverse.com/articles/iit-ropar-s-annam-ai-syngenta-and-google-launch-hack-core-2026-national-ai-hackathon-for-agriculture)
- GitLab AI Hackathon 2026 winners (developer-tooling agents) — [GitLab blog](https://about.gitlab.com/blog/gitlab-ai-hackathon-2026-meet-the-winners/)
- Judging commentary: "Impact themes are winning rubrics. Climate, healthcare access, financial inclusion, accessibility... A technically simpler project that nails an impact theme often beats a more complex project that ignores it." — [NextAgile](https://nextagile.ai/blogs/gen-ai/top-hackathon-project-ideas/) (secondary)
- A Spring 2026 hackathon judged AI projects "through product review" — [TechTimes](https://www.techtimes.com/articles/319046/20260625/spring-2026-hackathon-tested-ai-projects-through-product-review.htm)

### Inferences
- The Indian agri-WhatsApp pattern maps directly onto rural Spain: elderly farmers, CAP/PAC aid paperwork, SIGPAC parcels, AEMET frost and heat alerts, BOE/BOJA aid calls. A Spanish version (WhatsApp or Telegram, voice notes in Spanish and co-official languages, grounded in official sources with citations) would be on-trend and could reuse existing MCP servers as building blocks.
- What made these projects stand out: a named user, a non-technical channel, a real document workflow (claims, soil reports) and a concrete output artifact. None of the cited winners was primarily a "chat with X" interface.

### Gaps
- No detailed Spanish or EU public-sector winners (for example the datos.gob.es "Desafío Aporta", EU Datathon, or Spanish GovTech hackathons in 2026) were found in this pass. A targeted search is recommended.
- No finance-domain hackathon winners from 2026 were collected.

---

## 5. Cheap or free deployment, frontends, and WhatsApp/Telegram as the interface

### Takeaway
In 2026 **Render** is the only mainstream PaaS with a true always-free web tier (512 MB, sleeps when idle, no credit card). **Railway** and **Fly.io** no longer offer meaningful free tiers. Cloudflare Workers is a proven host for MCP servers (several Spanish INE servers use it). For non-technical rural users, a messaging-app interface is the pattern that wins hackathons.

### Cited Findings
- Render: the free Hobby plan gives web services with 512 MB RAM and 0.1 CPU at $0, with no credit card. Apps sleep after inactivity (cold start of a few seconds) but stay deployed indefinitely. Described as "the closest thing to free hosting that exists in 2026". — [Render article](https://render.com/articles/platforms-with-a-real-free-tier-for-developers-in-2026) (vendor); [DEV Community comparison](https://dev.to/pavel-hostim/render-vs-railway-vs-flyio-pricing-compared-2026-2e5p)
- Railway has no free tier. It gives about $1/month of credit, which covers only a few hours of runtime, and meters per second on top of a plan fee. — [DEV Community / hostim.dev](https://hostim.dev/blog/render-vs-railway-vs-fly-pricing/); [Railway blog](https://blog.railway.com/p/best-platforms-deploy-ai-apps-2026)
- Fly.io needs a credit card and has no free tier for new users. The trial is limited to 2 VM hours or 7 days, whichever ends first. — [saaspricepulse](https://www.saaspricepulse.com/blog/flyio-free-tier-2026); [techsy.io](https://techsy.io/en/blog/railway-vs-render-vs-fly-io)
- Existing Spanish MCP servers deployed on the Render free tier ([ine-universal-mcp](https://github.com/agmalaga2020/ine-universal-mcp)) and on Cloudflare Workers ([manalejandro/mcp-ine](https://github.com/manalejandro/mcp-ine)).
- WhatsApp-first interfaces for low-digital-literacy farmers appear among the cited 2026 hackathon winners — [YourStory](https://yourstory.com/2026/06/crop-insurance-conversational-analytics-ai-for-bharat-hackathon); [Grammen-AI](https://github.com/aditya1233745/Grammen-AI)

### Inferences
- A suggested stack:
  - A FastAPI backend in Docker on Render free (accept cold starts for demos, or ping it before the demo).
  - The MCP server on Cloudflare Workers or Render, using stateless Streamable HTTP per the 2026-07-28 spec.
  - A Telegram bot as the first channel: the Bot API is free with no business verification.
  - WhatsApp via the Meta Cloud API as a stretch goal, because it needs Business verification and has per-conversation pricing and template rules.
  - Streamlit or Gradio for a quick internal or eval dashboard.
  - Next.js only if the developer wants to signal full-stack skills.
- Hugging Face Spaces (Gradio or Docker) is still a common free demo host for ML projects, but no 2026 source confirming its current free-tier limits was retrieved.

### Gaps
- No 2026 primary source was retrieved on: Hugging Face Spaces free-tier limits, Cloudflare Workers free limits, WhatsApp Cloud API pricing in 2026 (Meta moved to per-message pricing in 2025, not re-verified), or Telegram Bot API changes. These need verification before they are quoted.

---

## 6. Costs: Claude model tiers for a hobby budget, and local models as a fallback

### Takeaway
Official prices (Sept 2026, per million tokens, input/output):
- **Haiku 4.5**: $1/$5
- **Sonnet 5**: $2/$10. The launch price was made permanent. It is cheaper than Sonnet 4.6 at $3/$15.
- **Opus 5.5**: $4/$20
- **Opus 5 / 4.x**: $5/$25
- **Fable 5.1**: $10/$50

For a hobby project, Sonnet 5 with prompt caching and Haiku 4.5 for high-volume subtasks should cost a few dollars a month at demo scale.

### Cited Findings (all from [Anthropic pricing page](https://platform.claude.com/docs/en/about-claude/pricing) unless noted)

| Model | Input | Output | Cache read | Batch input / output |
|---|---|---|---|---|
| Claude Fable 5.1 | $10 | $50 | $0.25 | $5 / $25 |
| Claude Opus 5.5 | $4 | $20 | $0.20 | $2 / $10 |
| Claude Opus 5 / 4.8 / 4.7 / 4.6 / 4.5 | $5 | $25 | $0.50 | $2.50 / $12.50 |
| **Claude Sonnet 5** | **$2** | **$10** | $0.20 | $1 / $5 |
| Claude Sonnet 4.6 / 4.5 | $3 | $15 | $0.30 | $1.50 / $7.50 |
| **Claude Haiku 4.5** | **$1** | **$5** | $0.10 | $0.50 / $2.50 |

- Sonnet 5's $2/$10 was announced as introductory pricing through Aug 31, 2026. It is now the standard price, and the planned rise to $3/$15 on Sept 1, 2026 **will not happen**.
- Claude Mythos 5 / 5.1 has limited availability at the same price as Fable. Opus 4 / 4.1, Sonnet 4 and Haiku 3.5 are retired on the first-party API.
- Fast mode for Opus 5.5, Opus 5 and Opus 4.8 costs about 2x ($8/$40 for Opus 5.5).
- US-only inference (`inference_geo: "us"`) costs 1.1x. The default is global.
- New accounts receive "a small amount of free credits".
- Anthropic's own example: 10,000 support conversations of about 3,700 tokens each on Haiku 4.5 cost about **$37**.
- Aggregators agree: "$1–$10 per million input tokens and $5–$50 per million output tokens as of September 22, 2026" — [BenchLM](https://benchlm.ai/anthropic/api-pricing); [CostGoat](https://costgoat.com/pricing/claude-api)

### Inferences
- Budget sketch: a demo with about 2k requests a month at about 5k input and 700 output tokens each on Sonnet 5 is about 10M input and 1.4M output tokens, roughly $20 + $14 = $34 before caching. With a cached 4k-token system prompt and tools, input drops substantially. Using Haiku 4.5 for routing and classification cuts cost further. Batch evals at 50% make nightly eval runs cheap.
- Local models (Ollama with Llama, Qwen, Mistral or Gemma families) are useful as an offline or privacy fallback and to show a provider abstraction layer. A good demo shows the same eval suite run against Claude and a local model with a quality/cost table.

### Gaps
- No 2026 source was retrieved on current Ollama models or their Spanish-language quality. The fallback recommendation is based on general knowledge.
- Rate-limit tiers (Start, Build, Scale) were named, but numeric limits were not retrieved.

---

## 7. Pitfalls juries flag, and regulatory considerations (EU AI Act, GDPR) for Spanish projects

### Takeaway
Juries dismiss "GPT wrappers" and generic chat demos. What they reward is a specific problem, one working feature done well, and AI used where it is actually needed. In regulated domains (legal, financial, public services), the main risks are hallucinated citations and prompt injection through tool outputs. On regulation, the **EU AI Act Article 50 transparency obligations apply from 2 August 2026** (users must be told they are talking to an AI). The high-risk (Annex III) obligations were **delayed to 2 December 2027** by the Digital Omnibus, which entered into force on 27 July 2026.

### Cited Findings
- "Judges have seen a hundred GPT wrappers." The strongest ideas "solve a specific problem, scope to a single working feature, and use AI purposefully, not as a generic LLM wrapper". AI is "table stakes, not a differentiator". — [NextAgile](https://nextagile.ai/blogs/gen-ai/top-hackathon-project-ideas/); [Reskilll blog](https://blogs.reskilll.com/50-ai-hackathon-project-ideas-for-2026-that-judges-actually-love/); [DEV: 25 AI hackathon ideas "with the hard part of each"](https://dev.to/pranjulrathour/25-ai-hackathon-project-ideas-for-2026-with-the-hard-part-of-each-1hn4) (all secondary or opinion)
- Lack of evaluation: Hamel Husain's point that most time should go to looking at data and error analysis implies that projects with no eval evidence look immature — [hamel.dev](https://hamel.dev/blog/posts/evals-faq/)
- Prompt injection and data exfiltration via MCP tools (the lethal trifecta), with real incidents at GitHub, Atlassian and Notion — [Simon Willison](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)
- **EU AI Act Digital Omnibus**: published in the Official Journal on 24 July 2026, in force since 27 July 2026. Annex III high-risk obligations moved from 2 Aug 2026 to **2 Dec 2027**; Annex I (AI embedded in regulated products) moved to **2 Aug 2028**. **Article 50 transparency was not amended and applies from 2 Aug 2026**: chatbot and GenAI providers must disclose AI interaction. The Art. 50(2) marking/watermarking deadline is **2 Dec 2026**. — [Usercentrics](https://usercentrics.com/knowledge-hub/eu-ai-act-high-risk-delay-article-50-transparency-consent/); [Gibson Dunn](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/); [Secure Privacy](https://secureprivacy.ai/blog/eu-ai-act-digital-omnibus-the-new-high-risk-ai-deadlines-after-council-approval); [Plesner](https://plesner.com/en/news/ai-act-august-2026-what-expect-delayed-standards-pending-guidance-and-digital-omnibus-ai)

### Inferences
- Pitfalls to avoid:
  1. Generic "chat with the BOE" with no user research.
  2. No eval numbers.
  3. No real users or pilot feedback. Even 5 real farmers or neighbours testing it and their quotes count.
  4. Legal or financial answers without source citations and without "this is not legal advice" framing.
  5. Claiming novelty that GitHub disproves (see section 3).
  6. Demos that depend on a sleeping free-tier server or on a beta API.
  7. An unbounded agent that can send messages and read private data (the lethal trifecta).
  8. Exposed API keys and no rate limiting or cost cap.
- Regulatory framing for a Spanish project:
  - Add an AI disclosure in the bot greeting to comply with Art. 50.
  - Avoid Annex III high-risk uses (such as eligibility for public benefits or creditworthiness) or frame the tool as informational decision support with human review.
  - GDPR: minimise personal data, avoid storing phone numbers or voice notes longer than needed, and note that Claude API calls default to global routing. EU data residency options were not verified.
  - Mentioning AESIA (the Spanish AI supervisory agency) and a short DPIA-style note in the README shows maturity.

### Gaps
- No primary source was retrieved on GDPR-specific guidance for LLM apps (EDPB or AEPD 2026 opinions) or on AESIA's current activity. This needs a follow-up search.
- Whether access to public services or benefits eligibility tools would fall under Annex III for a hobby informational bot was not legally verified.
- No first-hand hackathon judging rubrics (for example from Devpost or Spanish hackathons) were retrieved. The pitfall list relies on secondary blogs plus practitioner writing.
