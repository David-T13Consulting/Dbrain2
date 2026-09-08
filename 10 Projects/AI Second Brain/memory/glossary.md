# Glossary — the decoder ring

Three sources, three vocabularies. This is the full list; the ~20 most-used live in `CLAUDE.md`.

## Sources

| Term | Meaning |
|---|---|
| **Prisme One** | French AI bootcamp / community by Eliott Meunier. Source of the personal architecture (vault, skills, context layers). Screenshots: `00_Source_Material/Prisme_One_Webinar/` |
| **OS IA** | Prisme One's name for the whole personal AI operating system |
| **Product School** | Certification provider. Two relevant courses here: *AI Product Strategy* and *Advanced Agents*. A third, *Product Strategy*, is mostly general PM |
| **Vibe Coding** | A *different* Product School stream — the one the Claude Project instructions reference (Lovable/Supabase/GitHub). Relationship to this project is OQ-5 |

## Architecture

| Term | Meaning |
|---|---|
| **Second brain** | The static-context layer: who you are, offers, vision, style, standing knowledge. Lives as markdown |
| **Dynamic context** | What changes daily — clients, deals, live projects. A database layer. Not built yet |
| **Capacités / Skills / Fiches process** | Documented methods the agent executes. `SKILL.md` files |
| **SKILL.md** | Open standard for a reusable agent capability. YAML frontmatter, loads on demand. Portable across Claude Code, Copilot, Cursor, Codex, OpenCode |
| **AGENTS.md** | Root-level instructions file telling an agent how to work in a repo/vault. Vendor-neutral standard under the Agentic AI Foundation. ~28% median runtime reduction when present. Write by hand |
| **CLAUDE.md** | Claude-specific working memory. Can `@import` AGENTS.md |
| **PARA** | Projects / Areas / Resources / Archive — folder taxonomy from Building a Second Brain |
| **IPCRA** | Prisme One's framework for structuring static context. Referenced in the webinar but never fully shown |
| **Agentic search** | Agent greps and reads files directly at runtime. **Our retrieval choice** |
| **RAG** | Retrieval-Augmented Generation — embed, index, vector-lookup. Not used here initially; see `03_Product_School_Playbook.md` §6.1 for the trigger conditions |
| **Just-in-time retrieval** | Keep lightweight references (paths), load content through tools at runtime, rather than pre-loading |
| **Context rot** | Model performance degrading as the context window fills |

## Trust & evaluation

| Term | Meaning |
|---|---|
| **Golden dataset** | 150-row labelled truth set, versioned in git. Three jobs: regression, domain anchor, **proof for buyers**. *"Your receipts."* |
| **Eval** | A test of model/agent output against a defined standard |
| **Eval regression** | % of changes that keep scores positive on the golden set. Target 100% |
| **LLM-as-a-judge** | Automated scoring calibrated against the gold set. *"Who judges the judge? Your golden dataset"* |
| **Reliability contract** | Metric / target / measurement / alert-threshold table, committed to the repo |
| **Confidence UX** | Three bands: >90% full answer · 50–90% softened, no hard commitments · <50% withhold + escalate |
| **HITL** | Human-in-the-loop. Must be a *shrinking queue*, not permanent babysitting |
| **Hallucination rate** | % of responses unsupported by context. Target <1%; >5% very bad |
| **Drift velocity** | Rate of accuracy decay. <0.5%/week good. Not instrumented at our volume |
| **Recall accuracy** | % of relevant facts the retriever finds. ≥85% |
| **RAGAS** | Open framework of RAG evaluation metrics (ragas.io) |
| **Trust score** | Composite eval metric, RAGAS-style. >0.8 |

## Governance & security

| Term | Meaning |
|---|---|
| **Autonomy ceiling** | How far an agent role may act before requiring human review. *"Your primary risk management lever"* |
| **S.M.A.R.T. memory** | Scoped · Monitored · Auditable · Retrievable · Timed |
| **Zero trust** | Assume no implicit trust; verify every access |
| **RBAC** | Role-Based Access Control |
| **PII masking** | Redacting personal data — including **in the traces**, the commonly forgotten leak path |
| **TTL** | Time-to-live. How long memory or a token persists before expiry |
| **Shadow AI** | Ungoverned AI tools in use without approval. Samsung: 3 leaks in ~1 month |
| **Responsible AI maturity** | 3 levels: 1 Compliance → 2 Trust architecture → 3 **Governance = GTM** |
| **ZDR** | Zero data retention. Landscape reversed Aug 2026 — see `01_Key_Topics_Summary.md` §3 |
| **CLOUD Act** | US law giving US authorities reach over data held by US-parented providers |
| **EU AI Act Art. 50** | Transparency obligations, in force 2 Aug 2026. Text disclosure applies only to content published to inform the public on matters of public interest |

## Agents

| Term | Meaning |
|---|---|
| **MCP** | Model Context Protocol. *Vertical* — agent → system/tool. "USB-C for AI" |
| **A2A** | Agent-to-Agent. *Horizontal* — agent → agent |
| **Supervisor / critic agent** | An agent whose job is reviewing other agents' output |
| **Tool poisoning** | Malicious instructions embedded in an MCP tool description |
| **Rug pull** | An MCP server silently redefining a tool after you approved it |
| **RPA** | Robotic Process Automation. Fixed paths. Safer than agents for simple, predictable, low-error-tolerance work |
| **Max iterations** | Cap on agent loop cycles. Stops runaway token burn |

## Strategy

| Term | Meaning |
|---|---|
| **H1 / H2 / H3** | Three Horizons, AI-compressed: H1 ship 0–4wk · H2 validate 1–3mo · H3 explore 3–6mo. **Revisit monthly** |
| **Moat** | Defensibility. For AI specifically: data and **workflow**. Features get eaten; workflows survive |
| **Compounding vs scaling** | Scaling = ↑volume, flat quality, linear cost. Compounding = each touch makes the next better. Test: *freeze 3 months — still win? Then you're not compounding* |
| **Model cascading** | Route cheap queries to cheap models, expensive ones to frontier models. Margin protection |
| **Collector's fallacy** | Capturing information and mistaking it for having learned it. The main way second brains fail |
| **Slow burn** | Prisme One: Capturer → Accumuler → Exécuter |
| **Showcase workflow** | The one task the system will do excellently for the demo. Not yet chosen — OQ-1 |

## People & tools mentioned in sources

| Name | What |
|---|---|
| **Eliott Meunier** | Creator of Prisme One |
| **Obsidian** | Markdown knowledge base app. Recommended independently by both Prisme One and Product School |
| **Cloudron** | Self-hosting platform. Out of scope until month 4+ |
| **n8n** | Workflow automation. Out of scope for now |
| **NocoDB / Supabase** | Open-source database layers (dynamic context) |
| **Langflow** | Visual agent builder used in the Advanced Agents course |
| **Braintrust / Galileo / LangSmith / Rise** | Eval tooling named in the course |
| **Dispatch** | Claude feature: message from phone, work runs on your Mac. See `CAPTURE.md` |
