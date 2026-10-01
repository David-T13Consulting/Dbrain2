---
classification: public
status: draft
updated: 2026-10-01
tags: [product-school, ai-product-strategy, pricing, unit-economics, module/3]
---

# AI unit economics and pricing (module 3, "The Margin")

Product School **AI Product Strategy**, session 3. Question: *will this make money or bleed it?* Hub: [[30 Resources/Product School/README|Product School hub]]. Figures are as presented in class (illustrative, not verified); check vendor price pages before using them externally.

## The provocation: AI compresses margins before it expands them

| Claim | Verdict in class | Why |
|---|---|---|
| "AI will lower our costs" | **Not yet** | Inference is a variable cost. Many AI features land at about 40–60% gross margin against about 80% for classic SaaS, often as a P&L surprise |
| "Price per seat, like always" | **False** | A seat sells *access*; AI often delivers *work done*, so seat pricing under-captures value from heavy users and over-charges light ones |
| "Scale fixes the economics" | **False** | Scaling a negative-unit-economics product scales the loss. The fix is architecture and pricing, not volume |

## Classic SaaS vs the AI layer

| | Traditional SaaS | AI layer |
|---|---|---|
| Gross margin | 80%+ | 40–60% |
| Cost behaviour | Mostly fixed infrastructure (about $5–8 per user per month of COGS cited) | Variable cost per token; **power users are not average users** |

Napkin formula: **COGS per user per month = calls × tokens per call × blended $ per million tokens**. The model-tier price gap between small and frontier models is roughly 10–30× (publicly listed vendor prices; verify).

## Margin levers

1. **Model cascading** (the highest-leverage lever). A router sends most requests (about 80%) to a small, fast, cheap model and the hard minority (about 20%) to a frontier model, collapsing blended COGS. In the class example this turned a stress scenario of about −15% margin into about +30%.
2. Supporting levers: quantisation (smaller footprint), semantic caching (skip repeated queries), prompt optimisation (fewer tokens per call).
3. Design the cascade deliberately: triage model, frontier model, a routing rule, and an expected cascade ratio.

## Cost curve: map features to model tiers

| Feature | Complexity | Model tier | Cost per request | Volume share | Weighted cost |
|---|---|---|---|---|---|
| (simple task) | Simple | Small | $ | % | $ |
| (medium task) | Medium | Mid | $ | % | $ |
| (hard task) | Complex | Frontier | $ | % | $ |
| **Blended** | | | | 100% | $ per user per month |

"Estimate OK; structure beats false precision." The worked example mapped a fraud-triage product to about $40 per user per month of AI COGS, including a **human-in-the-loop** cost line (people are part of COGS).

## The margin calculator: six lines

Average requests per user per month → cost per request (blended) → monthly COGS per user → revenue per user per month → gross margin per user → gross margin %. Then **stress at 3× cost** and add a 50% price-shock scenario for vendor resilience. Rule from the notes: *if the stressed margin is below about 40% gross, fix architecture and pricing, not growth.* Vendors cut list prices over time, but stress-test anyway.

## Case: the automator that overcorrected (Klarna, as presented)

- The bet: an AI assistant handled about two thirds of support chats; press framed it as roughly 700 FTE equivalent; projected savings about $40M.
- The crack: token cost scales with usage, edge cases escalate to humans, and variable COGS replaces fixed labour, so forecasting gets messier.
- The correction: tiering plus a copilot for hard cases; humans rehired for complex cases (2025); narrative shifted from headcount to customer experience (speed, 24/7, languages). The CEO's reported remark: cost was too predominant an evaluation factor and quality suffered.
- Lesson: an **Automator** archetype ([[ai-strategy-bet-and-moat]]) optimising only cost invites a quality reversal.

## How you charge matters more than how much

| Model | What you sell | Examples cited | Share of AI products (as presented) |
|---|---|---|---|
| Seat / access | The right to use it | Figma, Slack, Notion | 59% bundle AI into the plan |
| Hybrid (base + usage) | Seat plus metered work | HubSpot, Canva AI | 23% sell as an add-on |
| Outcome / resolution | The work done | Intercom Fin, Harvey | 18% standalone product |

- **Outcome-based pricing is the most innovative** because the unit of charge matches the unit of value.
- **Labor test:** if the AI does $100/hour of human work and you sell it for a $50/month all-you-can-eat seat, you are giving value away.
- **Proof point:** GitHub Copilot at about $19/user (about 4.75× a base SaaS seat) is justified by measured speed-up (about 55% faster).
- **Product-market-pricing fit**, not just product-market fit: pick a strategy (skim, penetrate, maximise), name the **unit of work** you meter, then set base fee plus per-unit price.
- Class activity: is your hero SKU closer to **access** or **outcome**? If you price access on a product that does work, you leave value on the table.

### Bundling: leaders, fillers, killers

| Role | Meaning | AI example |
|---|---|---|
| Leader | What users come for; must-have; high willingness to pay | Core intelligence such as code autocomplete |
| Filler | Nice add-on that nudges ARPU | Summaries, translations, templates |
| Killer | Sinks the bundle if included, so sell as an add-on | Heavy inference: image generation, agent workflows |

**70% rule:** if more than ~70% of users use the AI feature, bundle it; if fewer than ~70% use it but value is high, sell it as an add-on. Pricing move: raise price on proven value; do not only shave tokens.

## The board one-pager

Before/after comparison: traditional SaaS (revenue per seat × seats, fixed COGS, gross margin %) versus AI-powered (base + usage + outcomes, variable COGS, gross margin %), then the **net margin shift** in % and gross dollars. Lower margin % can be fine if NRR and gross $ rise; script the narrative explicitly. The board message: AI compresses margins first, then wins on revenue and long-term cost reduction.

## Takeaways

1. AI economics differ structurally: variable cost, power users and edge cases.
2. Model cascading is the biggest single margin lever.
3. The pricing *model* beats the price *point*; outcome pricing captures AI value, seat pricing does not.
4. Put human-in-the-loop cost in COGS.

Related: [[ai-strategy-bet-and-moat]], [[ai-trust-evals-and-reliability]], [[ai-roadmap-and-board-pitch]] (the inference-ROI metric).
