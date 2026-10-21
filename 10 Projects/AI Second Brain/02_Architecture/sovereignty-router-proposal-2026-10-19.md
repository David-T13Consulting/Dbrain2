---
classification: internal
domain: ai-second-brain
sensitivity: ordinary
sharing: private
source: Cowork session with David, 19 Oct 2026 (GitHub, Reddit-cited and vendor research; David's decisions in session)
created: 2026-10-19
review_status: unreviewed
note_type: proposal
owner: "@david"
status: approved
---
# Sovereignty router and rent-not-buy plan (proposal, 19 Oct 2026)

**Status: approved 19 Oct 2026; re-sequenced into three stages 21 Oct (D141); review fixes of 21 Oct applied (L0 redefined, CLOUD Act and quality claims marked unverified, Dutch out of scope per D121)** (Q121, Q127–Q131 → D134–D140); the plan now lives in [[10 Projects/AI Second Brain/04_Roadmap|04_Roadmap]]. Demo: [[10 Projects/AI Second Brain/05_App_Prototype/sovereignty-router-demo.html|sovereignty-router-demo.html]] (simulated data; also published as a private Claude artifact "Dbrain Sovereignty Router").

## David's decision (19 Oct, stated in session)
- **No hardware purchase. Compute is rented online.** Supersedes the Mac mini order (D53, D107) and answers Q121. Recorded as D134.
- Asked for: reuse of existing building blocks instead of building each layer; an architecture with switchable sovereignty levels and a configurator-style cost view; an orchestrator that routes every request.

## Diagnosis (Cowork)
Building blocks exist for most layers. The larger cause of slow progress is process weight: about 130 decisions, up to 5 reviews per Tier 2 step. Renting compute and reusing components removes roughly half the remaining plan; the rest needs lighter review (Q129).

## Reuse findings, by layer
| Layer | Today | Reusable | Verdict |
|---|---|---|---|
| Model | 4B local on the Air; T9b; host order | Scaleway Generative APIs (Paris, iliad group, HDS + ISO 27001): Qwen3.8-27B, Qwen3-235B, Mistral Small 3.2, Gemma 4, whisper-large-v3, qwen3-embedding-8b; listed about $0.15–0.75 per 1M input tokens | Rent |
| Speech EN/FR | S4 local ASR planned | Scaleway whisper-large-v3 (listed $0, verify); Mistral Voxtral (EN, FR; also covers Dutch, out of scope under D121), $0.003/min batch, $0.006/min realtime, realtime weights Apache 2.0 | Rent |
| Phone and voice | Shortcut "Ask Brain 5" | Open WebUI (self-hosted) + Open Relay iOS app ($4.99; CallKit voice, STT/TTS, citations) | Reuse; dbrain query service plugs in as a model |
| Vault structure | PARA, frontmatter, AGENTS.md | claudesidian (2.6k stars, inactive 6 months); Karpathy LLM-wiki pattern (raw, wiki, schema; ingest, query, lint) | Keep ours; borrow the pattern's vocabulary |
| Ingest / wiki upkeep (S3) | Custom writer | AgriciDaniel/claude-obsidian (MIT), sdyckjq-lab/llm-wiki-skill, Ar9av/obsidian-wiki (validation after writes) | Adapt one; keep git-diff approval as the governance layer |
| Always-on agent | none | OpenClaw (MIT, 200k+ stars) | Avoid: malicious skills, exposed instances, CVEs; useful as a counter-example |
| Packaged second brain | none | Khoj (AGPL; hosted service closed 15 Apr 2026) | Skip |
| Gateway | none | LiteLLM (open source, OpenAI-compatible, budgets, logging); EUrouter (managed, see [[30 Resources/AI Vendors/eurouter]]) | LiteLLM |

RunPod and Modal not recommended: US companies, cold starts of about 10–50 s break the 8 s target unless kept warm.

## Sovereignty levels
| Level | Meaning | Example | US CLOUD Act exposure |
|---|---|---|---|
| L0 | Own machine (redefined 21 Oct, D141: the Mac Air; a rented GPU is not L0 and its exposure is not assessed) | Mac Air local model | None: no provider receives the request |
| L1 | EU-owned provider, EU data centres | Scaleway, Mistral | None claimed; `unverified` (Mistral's privacy policy §7 allows some non-EU service providers) |
| L2 | US cloud, EU region | Claude or Mistral on AWS Bedrock Frankfurt | Yes (contractual protection only) |
| L3 | US frontier, global | Claude API | Yes |

L2 costs about 10% more than L3 (regional endpoint premium, Anthropic pricing page) for residency without changing legal exposure; useful mainly where client procurement requires it.

## Architecture
Clients (iPhone via Open Relay, Mac, Claude Code/Codex) → Open WebUI → dbrain query service (retrieval, citations, verdicts) → switchboard (LiteLLM on a small EU server) → L0 / L1 / L2 / L3.

Rules:
1. The toggle is a ceiling. Effective level = strictest of: David's toggle, classification of retrieved notes, connector tier, client watch-list hit in the question.
2. No fallback to a looser level. Unavailable means the answer says so.
3. Every answer carries a level badge (level, provider, model, cost), logged with the trace.
4. Whole-vault jobs (embeddings, wiki maintenance) run at the strictest level in use.

## Orchestrator (recommended option B)
Per request: (1) retrieve notes on the server, no model call; (2) set the ceiling by rules only, unknown or unlabelled means strictest; (3) classify the task with a small model at the floor level; (4) pick the first model in an eval-derived routing table that sits inside the ceiling and the monthly budget; (5) answer and check (supported, incomplete, withheld), escalate once to a stronger model on incomplete, same ceiling; (6) log the decision with reason codes.

| Option | Build | Explainable | Fit at about 50 questions a day |
|---|---|---|---|
| A. Rules only | 2–3 days | Fully | Yes, saves little money |
| **B. Rules + classifier + eval routing table** | about 1.5 weeks | Fully, reason codes | Yes; recommended |
| C. Learned router (RouteLLM-style) | months | Poorly | No, not enough data |

B turns the golden dataset into the routing table and replaces S5's coordinator and checker rather than adding to S5.

## Cost configurator (estimates)
Usage assumed: 50 questions a day, about 6,000 tokens in and 500 out each, plus 5M in and 1M out a month of wiki upkeep, 10 voice minutes a day. €1 ≈ $1.10 assumed.

| Item | Level | Monthly |
|---|---|---|
| Base: EU server (Open WebUI, LiteLLM) | L1 | about €10 (estimate, not checked) |
| Base: Mistral Small 3.2 | L1 | about $3 |
| Base: speech (Voxtral batch) | L1 | about $1 |
| Upgrade: Qwen3.8-27B | L1 | +$15 |
| Upgrade: Qwen3-235B | L1 | +$12 |
| Own GPU, Hetzner GEX44 20 GB | L0 | +€184, €79 one-time, about 13B models max (unverified) |
| Claude Haiku 5.5 | L3 | about $2.50 total |
| Claude Sonnet 5.5 | L3 | +$47 |
| Claude Sonnet 5.5, Bedrock EU | L2 | +$52 |
| Claude Opus 5.5 | L3 | +$97 |
| EUrouter Plus instead of LiteLLM | L1 | +€39 plus 9% on tokens |

Typical mix (personal on Sonnet, professional on Qwen 27B): about €40–60 a month. Claude prices from Anthropic's pricing page (checked 19 Oct); Scaleway prices from a third-party catalogue (models.dev via Mastra); Hetzner from a third-party article.

## Revised plan to 18 Dec (option A, if approved)
| Week | Work |
|---|---|
| 1 | Scaleway account and DPA read; query service adapter to Scaleway; rerun dev cases on 27B; D46 and data policy amendment drafted for David's approval |
| 1 | Switchboard: LiteLLM with ceiling rules, decision log, level badge |
| 2 | Open WebUI behind Tailscale; Open Relay on the phone; voice working; task classifier and routing table for 3 task types |
| 3–4 | Ingest and wiki upkeep from an LLM-wiki skill with git approval (S3, G2); escalate-once on incomplete |
| 5–6 | Personal calendar and mail connectors, read-only (C1, C2) |
| 7 | Eval dashboard; injection suite (G1-inj) |
| 8 | Demo rehearsal |

**Cut:** Mac mini order (D53, D107), T9b, M6b embedding evaluation, custom Shortcut path, S4 local voice build. **Keep:** golden dataset, G1-inj, verdict logic, workstream W, no client data. **Correction (19 Oct evening):** no data-policy change is needed for this plan. Data policy §1 and §5 already allow `public` and `internal` content to a model API once the provider's terms are verified; the local-only architecture came from D45 and D53, superseded by D134–D135. (D46 is about runtime boundaries and stands.)

## Why it serves both priorities
Brand: "same question at L1, L2, L3, with quality, cost and legal exposure side by side" is a demo for EU banks, Belgian healthcare and US asset managers. US return: L1 default in Europe, L3 default for US clients, same architecture.

## Open checks before any reliance
- Scaleway DPA, sub-processors, retention; whether whisper-large-v3 is really $0.
- Hetzner GEX44 price and availability.
- All model quality figures in the demo are illustrative; real routing scores come from the golden set.

## Sources
- Community LLM-wiki implementations: https://srisatyalokesh.is-a.dev/learn-ai/best-llm-wiki-community-implementations/
- claudesidian: https://www.sourcepulse.org/projects/16162920
- Khoj review: https://www.promptquorum.com/de/power-local-llm/khoj-ai-second-brain-review
- OpenClaw overview: https://www.mindstudio.ai/blog/what-is-openclaw-ai-agent
- Open Relay: https://apps.apple.com/us/app/-/id6759630325
- Scaleway model prices: https://mastra.ai/models/providers/scaleway.md
- EU GPU providers: https://www.qovery.com/blog/eu-gpu-cloud-providers-gdpr-compliant-inference-patient-data
- EU inference providers 2026: https://dev.to/valeria_bernhardt_c9473b7/choosing-an-eu-hosted-inference-provider-a-2026-comparison-5d5h
- Voxtral Transcribe 2: https://mistral.ai/news/voxtral-transcribe-2
- Hetzner vs RunPod: https://findstack.com/resources/runpod-vs-hetzner-ollama
- RunPod vs Modal vs Lambda: https://www.premai.io/blog/serverless-llm-deployment-runpod-vs-modal-vs-lambda-2026/
- Claude pricing and data residency: https://platform.claude.com/docs/en/about-claude/pricing
- LiteLLM overview: https://blog.elest.io/litellm-stop-burning-money-on-llm-apis-virtual-keys-cost-tracking-and-guardrails/
