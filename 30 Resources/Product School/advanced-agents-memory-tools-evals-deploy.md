---
classification: public
status: draft
updated: 2026-10-01
tags: [product-school, advanced-agents, memory, rag, mcp, evals, deployment, days/4-6]
---

# Advanced AI agents: memory, tools, evals and deployment (days 4–6)

Second half of the Product School **Advanced AI Agents** certification. First half (anatomy, patterns, multi-agent archetypes): [[advanced-agents-design-and-teams]]. Hub: [[30 Resources/Product School/README|Product School hub]]. Own-words synthesis; thresholds are course heuristics, not industry standards.

## 1. Memory: the persistence shift
An agent without memory restarts every session; with memory it carries context, preferences and history across sessions. That makes it more useful and creates a new risk surface. Principle: **memory is a user trust contract**: users must know what is kept, why, and for how long.

| Memory type | What it holds | Typical use |
|---|---|---|
| Episodic | What happened in past interactions | Continuity, "last time you asked…" |
| Semantic | Stable facts and preferences | Personalisation |
| Vector / embedding | Searchable representation of unstructured content | Retrieval by meaning |
| External / linked | Pointers to systems of record (CRM, docs) | Fresh facts without copying data |

| Memory risk | Mitigation |
|---|---|
| Data leakage | Data minimisation, scoped access |
| Memory bias (old behaviour overrides new) | Bias monitoring, periodic review |
| Knowledge drift (facts go stale) | Source validation, TTL / expiry |
| Cost growth | Storage-cost monitoring, pruning |

**SMART memory governance:** Scoped, Monitored, Auditable, Retrievable, Timed (expiry).

## 2. RAG: giving the agent knowledge
Pipeline: raw data → extraction → chunking → embedding → vector DB; at query time: query → embedding → retrieve → LLM → response. PM ownership: **retriever recall** (did we fetch the right chunks), **knowledge-base governance** (what is allowed in, who owns freshness) and **generator synthesis** (does the answer stay faithful to sources). Trade-off: each retrieval adds latency per turn. Typical examples: product Q&A over a workspace, code assistants over a repo, search overviews.

## 3. Tool access: API vs CLI vs MCP
- **MCP** (Model Context Protocol): standard client-server connector, the "USB-C for AI". Scoped permissions and audit trails make it safer than ad-hoc integrations.
- **MCP vs A2A:** MCP is vertical (agent ↔ system); A2A is horizontal (agent ↔ agent).
- **Secure-MCP checklist:** define access scope; set expiry/TTL on grants; log every MCP event; human review for write actions; test for data leakage.

## 4. Why agents fail differently
Four sources of new failure: multi-step reasoning, external tool use, persistent memory, collaboration complexity.

| Failure mode | PM requirement | Detection metric |
|---|---|---|
| Tool misuse | Allow-lists, parameter validation | % failed tool calls |
| Reasoning loops | Step and budget caps | Loops per run |
| Memory drift | Expiry, validation | Accuracy score over time |
| Handoff failure (multi-agent) | Explicit contracts | Handoff success rate |

**Debugging stack:** governance layer (policy, limits) → action layer (tools) → reasoning layer (instructions, context). Work from symptom to root cause; e.g. bad answer from a RAG agent is either bad instructions or missing data, so check what was retrieved first.

## 5. Evals: four types
| Eval | Question | Course target |
|---|---|---|
| Functional | Did it complete the task? | ≥85% task success |
| Reliability | Same input, same result? | <5% variance |
| Safety | Did it stay inside policy? | 0 violations |
| Factual | Is it grounded in sources? | ≥90% match |

Gates sit **before** (pre-release suites), **during** (runtime guardrails) and **after** (monitoring) a run. Memory/RAG targets from the course: recall ≥85%, hallucination <5%, drift <10%, latency <1 s, trust score >0.8. Practical points: test with live vs mock data deliberately; schedule recurring runs; track deflection/containment (cases handled minus abandonment). **Evals are a team sport:** AI engineer builds harness, PM defines pass criteria, SMEs label edge cases, analysts watch dashboards. Tooling examples: Braintrust, Galileo, LangSmith. Related: [[ai-trust-evals-and-reliability]].

## 6. The business of autonomy
Five value drivers: adoption acceleration, revenue expansion, operational leverage, trust and governance, innovation speed; each pairs a value, a risk and a mitigation. Trust has four layers (governance, reliability, accountability, transparency); aim to scale inside the "safe scale zone". Speed is argued to be the main moat now. Monetisation moves from seats toward usage, outcome and hybrid pricing ([[ai-unit-economics-and-pricing]]).

## 7. Deployment readiness
Before launch: value hypothesis, named liability owner (e.g. an AI safety council), visible trust signal, and scaling logic gated by the **autonomy ladder** (L1 human review of everything; L2 needs <10% human intervention and <1% critical failure to advance).

**Risk-gated rollout:** shadow mode → internal beta (dogfood) → phased exposure (1% → 10% → 100%).
**Post-launch signals:** eval pass %, policy violations, escalation (HITL) rate, drift index, autonomy compliance %, mean time to debug. Drift is tracked at several levels, including model-version drift.
**Handoff to engineering:** logic spec, data requirements, failure protocol, level of autonomy. Ownership differs: startups = builder, enterprises = governor.

## Use for David
Maps directly onto the evaluation-and-governance layer of the [[10 Projects/AI Second Brain/03_Product_School_Playbook|playbook]]: the four eval types, SMART memory and the autonomy ladder are reusable client frameworks (anonymised) for banking and healthcare contexts. See also [[ai-governance-and-compounding]].
