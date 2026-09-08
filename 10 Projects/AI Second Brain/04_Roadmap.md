# The Roadmap — Personal AI System, Client-Demonstrable in 3 Months

**Supersedes** §5 of `02_Critical_Assessment.md`.
**Built from three sources:** the Prisme One webinar (personal architecture), Product School (rigour and commercial framing), and current published practice (mechanics, security, regulation).

**Your parameters, as confirmed:**

| | |
|---|---|
| **Showcase format** | A live system you drive — screen-shared, real tasks, in front of a client |
| **Collaborative means** | Humans sharing a governed system first; multi-agent second |
| **Security anchor** | Generic but strict — design to the tightest common denominator |
| **Horizon** | 3 months to something client-ready |

---

## 1. The strategic reframe — read this first

The webinar's endpoint is *"a personal AI system that makes me productive."* **That is not showcaseable to a consulting client.** Every creator on LinkedIn claims it, the demo is unfalsifiable, and productivity claims from a director are assumed rather than impressive.

Here is what is actually scarce, and what your Product School material hands you on a plate:

> **You are not demonstrating that AI makes you faster. You are demonstrating that you know how to make AI trustworthy enough to deploy inside a regulated business — and you have built the instrumentation to prove it on yourself first.**

The personal system is the *substrate*. The eval and governance layer is the *product*. Your own course says it twice:

- *"Golden datasets are your receipts. When a buyer asks 'how do you test this?', your golden dataset is the answer. **This is the demo.**"*
- *"Can't screen-share this in a sales call? Not product-grade."*

And the commercial thesis, straight from the Responsible AI Maturity slide: **Governance = GTM.** Level 1 is compliance, where most organisations plateau. Level 3 is a governance story that closes deals. You are building a Level 3 artifact at personal scale.

**What this changes concretely:** instrumentation moves from "phase 4, if time allows" to the H1 gate. You build the measurement layer *while* you build the first skill, not after. It is the differentiator, not the polish.

### Why this fits you specifically

The Advanced Agents whiteboard is, functionally, your job description:

```
        PM  ─────────►  Agent Era  ◄─────────  Engineer
 (pure strategy,     Taste + Judgment          (pure code,
   no building)    + Problem Shaping            no taste)
                  + Agent Orchestration
```

You are approaching that centre from the PM side, and you have the one thing engineers building the same demo usually lack: you can define what "good" means and defend it to a board. Per the *"evals are a team sport"* slide, deciding success criteria is explicitly the PM's job. Lead with that.

---

## 2. What changed from the earlier plan

| Earlier plan | Now | Why |
|---|---|---|
| Evals in phase 2, loosely defined | **Golden dataset in week 3, eval dashboard in week 5** | It's the showcase artifact, not a hygiene step |
| Model/hosting decision in phase 4 | **Week 9, decided against your own golden set** | You'll have data instead of opinions — and that's a demo moment |
| Server "conditional, possibly never" | **Explicitly out of scope** | Adds operational risk to a live demo, proves nothing to a client |
| Multi-user "not addressed" | **H3, with architecture prepared from week 1** | You confirmed humans-sharing matters |
| Security as a warning | **Designed in from week 0, demonstrated in the demo** | It's the thing you're selling |

---

## 3. The 13 weeks

Structured on Product School's AI-compressed Three Horizons — H1 ship (0–4 weeks), H2 validate (1–3 months), H3 explore (3–6 months). Revisit monthly, not annually.

### Week 0 — Foundations (~4 hours, this week)

| # | Task | Output |
|---|---|---|
| 0.1 | Revoke the Telegram token; sweep all source material for other secrets | Clean corpus |
| 0.2 | Write `data-policy.md` — three tiers (public / internal / client-confidential), red lines, what may never enter the system | 1 page |
| 0.3 | Run the *"last 30 days of conversations → where am I spending time → what should be automated"* prompt | Evidence-led candidate list |
| 0.4 | **Choose the showcase workflow** — the one thing the system will do excellently | 1 sentence |

**On 0.4 — the single most consequential decision in this plan.** Criteria: it must be something you do genuinely repeatedly; it must have a *checkable* right answer (or you can't build a golden dataset); it must be legible to a client in under 30 seconds; and it must not require client-confidential data to demonstrate. A good shape is something like *"turn a messy discovery-call transcript into a structured findings memo in my house format."* A bad shape is *"help me think"* — unmeasurable, undemoable.

**Gate:** you can state the workflow and your red lines in one sentence each.

---

### H1 · Weeks 1–4 — Ship (earn credibility)

**Goal:** a working, instrumented vertical slice. Narrow and deep, not broad.

| Week | Build | Notes |
|---|---|---|
| **1** | Vault skeleton (`00 Inbox / 10 Projects / 20 Areas / 30 Resources / 40 Archive / 90 System`), hand-written `AGENTS.md`, `git init`. Agent gets **read-only**. **No MCP servers.** | Migrate a *bounded* subset of knowledge — enough to serve the showcase workflow, nothing more. Resist the urge to import everything; that's the collector's fallacy and it costs you weeks. Write `AGENTS.md` yourself — auto-generated ones measurably underperform. |
| **2** | Three `SKILL.md` files for the showcase workflow. **Write the success threshold before the skill.** | Per the evals-team slide, defining success criteria is your job, not an engineer's. Format: *"handles ≥X% of cases with <Y% exceptions."* |
| **3** | **Golden dataset v1** — 150 rows, 20–30% edge cases, adversarial rows, versioned in git as `golden-dataset.md` | The highest-leverage artifact in the entire plan. Input · Expected output · Edge case? · Judge type (rule/LLM). This is what you screen-share when asked "how do you know it works?" |
| **4** | Wire LLM-as-judge scoring against the golden set. Enable agent **write** access — confined to approved directories, behind git, *after* testing rollback. | Verify recovery before granting write access, not after. |

**H1 gate — all four must be true:**
1. Three skills pass their stated thresholds against the golden set
2. You have deliberately broken something and rolled it back
3. You can screen-share eval results
4. Zero client-confidential data has entered the system

**What this proves to a client:** you don't guess whether AI works — you measure it, against a standard you defined.

---

### H2 · Weeks 5–9 — Validate (prove it's trustworthy)

**Goal:** the artifacts that turn a working system into a credible one.

| Week | Build | Why it earns its place |
|---|---|---|
| **5** | **Eval dashboard.** Metrics, judge setup, drift alerts, UX hooks. *"Like an SRE dashboard for your model."* | This is the screen you share. If it isn't screen-shareable, it isn't done. |
| **6** | **Reliability contract** — metric / target / measurement / alert-threshold table for the showcase workflow, plus escalation paths | Air Canada made this concrete: your AI's promises are your promises |
| **7** | **Confidence UX** — three bands (>90% / 50–90% / <50%), visible reasoning, override surface, corrections feeding back | The "trust ≠ accuracy" lesson made operational. **Build a deliberate low-confidence path — you will demo it on purpose.** |
| **8** | **Governance one-pager** — scope, autonomy boundaries, escalation triggers, audit cadence, regulatory exposure (EU AI Act / GDPR / sector), agent topology | *"One page your CISO wouldn't redline on sight."* This is the artifact that converts a technical demo into a commercial conversation. |
| **9** | **Model + hosting decision, made properly.** Benchmark 2–3 options — one frontier, one open-weight, one EU-hosted — against *your own golden dataset*. Document with the trade-off grid. | Deliberately late. You now decide with evidence, and "here's how I chose, and here's the data" is a stronger demo beat than any model name. |

**H2 gate:**
1. "How do you know it works?" is answered with a screen, not a sentence
2. HITL% is trending down across the period, not flat
3. The governance one-pager survives a hostile read by someone who isn't you

**What this proves:** you can make AI legible and governable — the Level 2→3 jump.

---

### H3 · Weeks 10–13 — Collaborate & package

**Goal:** the bridge from personal to client-deployable, plus a demo that doesn't fall over.

| Week | Build | Notes |
|---|---|---|
| **10** | **Multi-user layer (humans first).** Shared vs personal vault roots, RBAC as a metadata filter, apply S.M.A.R.T. memory governance (Scoped · Monitored · Auditable · Retrievable · Timed) | Get a second real human in — a colleague is enough. A two-person system that genuinely works beats a ten-person design that's theoretical. |
| **11** | **Second agent + supervisor pattern.** Only now. Add a critic/supervisor, log A2A messages, set explicit autonomy ceilings per role | Your own course: *refactor to multi-agent when you hit boundaries in skills, tools, or evaluations* — not before. Be able to name the boundary you hit. |
| **12** | **Security hardening + shadow-AI audit on yourself.** MCP posture (if any MCP at all), PII handling including in traces, TTL policy, data-leakage evals | Run the Discover → Signal → Prioritize → Decide audit on your own tool sprawl. The finding *is* content for the demo. |
| **13** | **Demo build and rehearsal.** Narrative, failure drills, artifact pack, twice-through dry run | Treat it as a board simulation, which is what Day 6 was training you for |

**H3 gate:** you can run the live demo twice consecutively without a failure you can't explain on the spot.

---

## 4. Architecture decisions to lock in week 1

These are cheap now and expensive later. Each one is what makes the H3 collaborative layer a configuration change instead of a rebuild.

| Decision | Choice | Rationale |
|---|---|---|
| **Storage** | Plain markdown + git | Multi-user via git rather than a database — sufficient to small-team scale, portable, auditable, and the diff history *is* your audit trail |
| **Access classification** | `classification: public\|internal\|client` in frontmatter, from the very first note | RBAC later becomes a filter, not a migration. Costs seconds now. |
| **Vault roots** | Separate `personal/` and `shared/` from day one | Never have to untangle them under time pressure |
| **Skills** | Portable `SKILL.md` files, never tool-locked config | Open standard across Claude Code, Copilot, Cursor, Codex, OpenCode and others — no lock-in, and *demonstrating* portability is itself a credibility beat |
| **Retrieval** | Agentic file search. **No vector store initially.** | Right for a personal corpus. Add RAG only on a named trigger (corpus scale, sub-second latency need, synonym-heavy search) — see `03_Product_School_Playbook.md` §6.1 |
| **Client data** | **Never enters the system.** Demo on synthetic or anonymised material | Non-negotiable. Demoing trustworthiness using another client's confidential data is an instant, unrecoverable credibility failure. |
| **Secrets** | Never in the vault. Env vars or a keychain, with a pre-commit scan | You have already had one live token in your source material |

---

## 5. The demo — sketch it now, build toward it

Since you're driving it live, design the narrative in week 0 and let it pull the build.

| Beat | Content | Time |
|---|---|---|
| **1 · Cold open** | Give the system a real task in the client's domain. It executes in your method and voice. | 60 sec |
| **2 · "But how do I know it works?"** | Golden dataset → eval dashboard → regression history. **The differentiator.** | 3 min |
| **3 · "And when it's unsure?"** | Deliberately trigger a low-confidence case. Watch it decline, explain, and escalate. | 90 sec |
| **4 · "And is it safe?"** | Governance one-pager: autonomy ceilings, memory TTL, audit trail, regulatory exposure | 3 min |
| **5 · "How does this scale to my team?"** | Multi-user layer, S.M.A.R.T. memory, RBAC via classification | 2 min |
| **6 · Close: judgment, not tools** | The decision rules — agentic vs RAG, open-weight vs frontier, agent vs RPA — each with the evidence you used | 2 min |

**Beat 3 is the one people remember.** A system that visibly declines to answer is more persuasive than one that always does. Rehearse it deliberately.

**Live-demo risk management:** rehearse against a fixed dataset; keep a recorded fallback; and pre-plan one honest failure to walk through. A director who says *"here's where this breaks, and here's how I'd contain it"* outsells one whose demo is flawless — particularly to a regulated buyer, who has learned to distrust flawless.

---

## 6. Deliberately out of scope

Naming these protects the timeline. Each has a real argument for it and a better argument for "not in these 13 weeks."

| Not building | Why |
|---|---|
| **Self-hosted VPS / Cloudron / n8n** (webinar's week 3) | Adds operational risk to a live demo and proves nothing a client cares about. Revisit in month 4+ if a workflow genuinely needs to run while you're away. |
| **A dozen MCP servers** | Direct file access covers the vault. Every server added is attack surface and a tool-selection ambiguity — both documented failure modes. |
| **Vector RAG** | Wrong tool at this corpus size. Add on a named trigger. |
| **Full knowledge migration** | Collector's fallacy. Migrate what the showcase workflow needs. |
| **Local model inference** | Capability drop is real, and the Air is fanless — it throttles under sustained load. Wrong risk to take into a live demo. |
| **A second showcase workflow** | Depth over breadth. One workflow, provably excellent. |

---

## 7. What you'll actually instrument

Four metrics, tracked from week 3. Be able to *speak* to the rest.

| Instrument | Target | Why this one |
|---|---|---|
| **Hallucination rate** | <1% | Core credibility number |
| **Eval regression** | 100% of changes stay positive on the golden set | Cheapest discipline, highest payoff |
| **HITL %** | Trending down, not flat | Your compounding proof — the difference between scaling and compounding |
| **Recall accuracy** | ≥85% | Once retrieval is live |

Deliberately *not* instrumented at this volume: drift velocity per week, confidence distribution, inference ROI, deflection rate. They need volume you won't have. **Know the numbers, explain why you're not tracking them yet** — that distinction reads as judgment. Claiming a weekly drift figure on a personal system reads as theatre, and a sharp client CTO will catch it.

---

## 8. Risks

| Risk | Likelihood | Mitigation |
|---|---|---|
| **Scope creep into infrastructure** | High — it's the fun part | §6 is a contract with yourself. Server work is month 4+. |
| **Golden dataset never gets written** | High — it's the boring part | It's the week-3 gate. Nothing proceeds without it. 150 rows is ~4 hours. |
| **Vault becomes a reading list** | Medium | Six-week check: has anything *shipped* out of the system? If not, stop capturing. |
| **Demo fails live** | Medium | Rehearse twice, fixed dataset, recorded fallback, one planned honest failure |
| **Client data leaks in** | Low but severe | Classification frontmatter from note one; synthetic data for all demos |
| **Model landscape shifts mid-build** | Certain | Decision is week 9 and documented as dated — it's a decision record, not an assumption. Vendor retention policy has already reversed once in 2026. |

---

## 9. Still open

1. **The showcase workflow itself** (task 0.4). I can help you pick it — tell me 3–4 things you do repeatedly and I'll pressure-test which is most demoable and most measurable.
2. **Your firm's AI policy.** Still the one input I can't research. It constrains §4's client-data rule and the governance one-pager.
3. **MacBook Air RAM.** Only matters if you want a local-inference story in the demo — which I'd advise against, but it's your call.
4. **Whether a colleague is available for the week-10 two-person test.** If not, I'll design a single-user simulation of the multi-user layer instead — weaker, but workable.

---

## 10. Immediate next actions

1. Revoke the Telegram bot token via BotFather
2. Run the *"last 30 days"* prompt
3. Come back with 3–4 candidate workflows and we'll choose the showcase one together
4. Then I'll scaffold the vault, `AGENTS.md`, and the first `SKILL.md` with you

*Written 7 September 2026. Revisit monthly — the Three Horizons are compressed, and so is this plan.*
