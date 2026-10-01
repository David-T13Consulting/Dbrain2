---
classification: public
status: draft
updated: 2026-10-01
tags: [product-school, ai-product-strategy, governance, agents, shadow-ai, module/5]
---

# AI governance, compounding systems and shadow AI (module 5, "The Guardrails")

Product School **AI Product Strategy**, session 5. Question: *what breaks when this scales?* Compound → govern → audit. Hub: [[30 Resources/Product School/README|Product School hub]].

## Governance is a sales asset, not a compliance burden

| Claim | Verdict | Evidence cited |
|---|---|---|
| "Governance slows us down" | False | A major CRM vendor sells its trust layer as a product; the EU AI Act is live, and proof beats pitch |
| "We can manage AI tools organically" | False | A music-streaming company cut about 1,000 tools to about 15 governed ones; no audit means blind spend and leaks |
| "Agents are just automation with better UX" | False | Agents *choose actions* and chain tools; a chatbot invented policy and a court held the company liable (see [[ai-trust-evals-and-reliability]]) |

## Responsible-AI maturity: three levels

1. **Compliance:** the minimum bar (EU AI Act, GDPR/CCPA).
2. **Trust architecture:** confidence UX, evals and reliability contracts from module 4.
3. **Governance = go-to-market:** model cards, bias posture and a trust layer *in the pitch*. Most organisations plateau at level 1; the jump from compliance to sellable trust accelerates deals. (A pause of a major image-generation feature for remediation was cited as the cost of shipping ahead of guardrails.)

## Systems that compound vs systems that scale

*Scales:* volume goes up, quality stays flat, cost is linear. *Compounds:* each use makes the next smarter and lowers cost per win.

| Loop type | Meaning | Example given |
|---|---|---|
| Recursive learning | Outputs plus corrections feed the model | Language-learning lessons that adapt per learner |
| Cross-domain transfer | A win in domain A lifts domain B | A vertical software roll-up with 32 products on one stack |
| Network intelligence | Fleet patterns, privacy-gated | Shared fraud or anomaly signals |

**Compounding design sheet:** for each loop record input, output, *does it compound* (Y/N) and status (active, broken, missing); name one broken loop and the fix; note where context silos block connectivity. **Freeze test:** if you stopped shipping for three months (about one frontier-model cycle), would you still win? If yes, you are not compounding.

Worked example (a fraud product): transaction data from true and false positives feeds monthly retraining (compounds, active); the same data could update anti-money-laundering models (compounds, but missing); customer reports should update the golden dataset (does not compound yet, missing).

## Agentic vs traditional ROI

| | Traditional automation (RPA) | Agentic |
|---|---|---|
| Paths | Fixed, linear ROI | Fuzzy quality, token-cost swings |
| Edge cases | Snaps | Eats exceptions, **if governed** |

Three decision factors for agent vs RPA: **complexity** (simple and predictable → scripts; messy and edge-case-heavy → agents), **error-cost tolerance** (very low tolerance → RPA; review costs can kill ROI), **learning** (agents only pay off if feedback loops actually ship). RPA is safer and more stable where the job allows.

## Agent governance: lock these four

| Lock | Rule |
|---|---|
| **Autonomy** | Draft is not send, read is not write; define an explicit action space |
| **Tool calls** | Whitelist, rate-limit, log; every call is exfiltration risk |
| **Memory** | What persists, retention (TTL), who reads it, HIPAA or other regimes |
| **Chain** | If B fails on A's output, there is a named owner for each handoff |

Principle: principles beat model names; orchestration products need these locks regardless of vendor.

## The governance one-pager (what your CISO wouldn't redline)

Five sections plus an agent topology:

1. **Scope:** what the policy covers.
2. **Autonomy boundaries:** what the agent can do solo vs needs a human.
3. **Escalation triggers:** when humans must enter.
4. **Audit cadence:** real-time, daily, weekly, monthly or quarterly review.
5. **Regulatory exposure:** which regimes apply (EU AI Act risk tier minimal/limited/high, GDPR, sector rules).
6. **Agent topology** (if shipping agents): what each agent can do, what it cannot, who approves.

Peer drill: audit a partner's policy for **data-leak paths** (the Samsung-style paste into a public chatbot) and **promise paths** (the Air Canada-style invented policy); look for missing data classes, unclear escalation paths, agents with no human oversight, and no review cadence.

## Case: shadow AI meets real data

Employees pasted source code and meeting notes into a public chatbot; three leaks in about a month; the company banned the tool and built an internal one. Lesson: **absence of governance is a strategy failure.**

## The shadow AI audit (the PM version)

Samsung-style shadow AI is the CISO's problem (employee tool sprawl). The PM version is what **your users** quietly build with AI around your product. Four steps:

1. **Discover:** support tickets, user interviews, automation-platform recipes, forum posts, API usage patterns (large exports suggest enrichment elsewhere).
2. **Signal:** why are they reaching out? Workflow gap, trust gap, capability gap or pricing gap.
3. **Prioritise:** frequency × strategic relevance.
4. **Decide:** **build** (absorb the capability), **partner** (official integration) or **ignore**.

Target: surface at least five workarounds. Users do not file tickets called "feature request"; they paste output into a chatbot. Every workaround is a feature request you were not reading, or a capability someone else will ship first.

## Takeaways

1. Compounding beats scaling: corrections, transfer and network effects, or you are a commodity with variable costs.
2. Governance done well is a GTM asset; buyers increasingly ask for governance artefacts.
3. Shadow AI is a strategy signal, not just a compliance gap.

Relevance: the four agent locks and the governance one-pager underpin the data policy in [[10 Projects/AI Second Brain/02_Architecture/data-policy|data-policy]] and the "Governance = GTM" thesis. Next: [[ai-roadmap-and-board-pitch]]. Agent-level detail: [[advanced-agents-design-and-teams]] and [[advanced-agents-memory-tools-evals-deploy]].
