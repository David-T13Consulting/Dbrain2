---
classification: internal
---
# Product School — Digested Playbook

**Source:** three course printouts (AI Product Strategy, Advanced Agents, Product Strategy), Sept 2026, with your own annotations.
**Purpose:** extract the reusable frameworks, decision rules and thresholds — and mark where they agree or conflict with the Prisme One webinar and current published practice.

---

## 0. The headline

Product School supplies **exactly the layer I flagged as the webinar's biggest blind spot**: how you know the thing works, and how you make that legible to a buyer. The two sources are close to complementary:

| | Prisme One webinar | Product School | Overlap? |
|---|---|---|---|
| Personal knowledge architecture | ✅ Core focus | ⚠️ One slide (Obsidian as central memory) | **Both land on Obsidian, independently** |
| Skills / documented process | ✅ Core focus | ➖ Implied | — |
| Evaluation & measurement | ❌ Absent | ✅ Core focus | Product School fills the gap |
| Governance & security | ❌ Absent | ✅ Core focus | Product School fills the gap |
| Commercial framing | ⚠️ Solo-creator | ✅ Enterprise/board-level | Product School is the one you can use professionally |

**The single most useful sentence in the whole set**, from the Eval Dashboard slide:

> **"Can't screen-share this in a sales call? Not product-grade."**

That is your showcase criterion, and it's the reason the roadmap now leads with instrumentation rather than productivity.

---

## 1. Trust architecture (AI Product Strategy, Day 4 — "The Contract")

### 1.1 Trust ≠ Accuracy

The course's most counter-intuitive point, and the one worth building your narrative on:

| Black box | Legible system |
|---|---|
| **95%** accurate | **85%** accurate |
| No scores, no override | Scores + sources + "not sure" |
| Surprises in production | User can correct |

> *"Understandable + controllable wins, even at a lower benchmark %."*

Anchors: Tesla/ADAS-style UIs force handoffs when confidence dips; Perplexity leads with sources. Key takeaway as stated: **"Trust is a function of perceived control, not accuracy."**

### 1.2 Golden datasets — the highest-leverage artifact

Three jobs, and note the third:

1. **Regression** — every prompt/model change, scores dip before users feel it
2. **Domain anchor** — *your* definition of "good", not a public leaderboard
3. **Proof for buyers** — *"Enterprise question: 'Show me how you test.' **This is the demo.**"*

Spec: **100–500 rows** (your note: 150 is a good start), **20–30% edge cases**, **versioned like code** in git. Structure per row: Input · Expected Output · Edge Case? · Judge Type (rule / LLM). Plus adversarial rows and coverage gaps.

Key takeaway as stated: **"Golden datasets are your receipts."**

### 1.3 Human-in-the-loop design

> *"HITL as a shrinking queue, not permanent babysitting."*

| Crutch ❌ | Feature ✅ |
|---|---|
| Review everything | Thresholded review |
| Cost explodes | Corrections ship back |
| Fixes vanish | **HITL% drops** |

Mechanics: low score → human, high score → auto. Each edit is fuel. Escalation UX makes uncertainty visible and lets the user opt in.

### 1.4 Confidence UX — three modes, not one answer

| Band | Behaviour |
|---|---|
| **Confident (>90%)** | Full answer with reasoning |
| **Uncertain (50–90%)** | Soften language, no hard commitments, show what's ambiguous, prompt further research |
| **Not confident (<50%)** | Withhold output, explain why, escalate to human queue |

User control surface: see AI reasoning/drivers · correct & override · corrections feed back into model/dataset · adjust threshold.

### 1.5 LLM-as-a-judge

Automated scoring calibrated against the gold set — regression, drift alerts, quality gates (auto vs human vs block). *"Who judges the judge? Your golden dataset."* Tooling named: LangSmith, Braintrust, Galileo, Rise.

### 1.6 Reliability contract

A metric / target / measurement / alert-threshold table, committed to the repo. Air Canada is the cautionary case: the chatbot invented a bereavement policy, the tribunal held the company liable. Stated as: **"Reliability contracts aren't metaphors. Your AI's promises are your company's promises."**

---

## 2. Guardrails & governance (Day 5)

### 2.1 Responsible AI maturity — three levels

| Level | What | Note |
|---|---|---|
| 1 · **Compliance** | EU AI Act, GDPR/CCPA | "Minimum bar" — most orgs plateau here |
| 2 · **Trust Architecture** | Confidence UX, evals, reliability contracts | The Day 4 material |
| 3 · **Governance = GTM** | Model cards, bias posture, trust layer *in the pitch* | Revenue-grade |

> **"Your Governance Framework Is a Sales Asset, Not a Compliance Burden."**

Evidence offered: Salesforce sells Einstein Trust Layer as product; enterprise buyers increasingly ask for governance artifacts; the jump from compliance to sellable trust accelerates deals. **This is your commercial thesis** — it's the bridge from "I built a personal system" to "I can advise your bank."

### 2.2 Agent governance — lock these four

| Dimension | Rule |
|---|---|
| **Autonomy** | draft ≠ send · read ≠ write · explicit space |
| **Tool calls** | whitelist · rate-limit · log — *each call is exfil risk* |
| **Memory** | what persists · TTL · who reads · regulatory class |
| **Chain** | B fails on A · named owner per handoff |

*"Principles beat model names."*

### 2.3 Agents vs RPA — three decision factors

| Factor | → RPA | → Agents |
|---|---|---|
| **Complexity** | Simple, predictable | Messy, edge-case heavy |
| **Error tolerance** | Very low tolerance | Tolerant with review |
| **Learning** | No feedback loop | Only if feedback loops actually ship |

Economics: traditional = fixed paths, linear ROI, snaps on edge cases. Agentic = token-cost swings, fuzzy quality, absorbs exceptions — *if governed*.

### 2.4 Compounding vs scaling

| Scales | Compounds |
|---|---|
| ↑ volume · flat quality · linear cost | Each touch → better next touch · ↓ cost per win |

Three loop types: **Recursive Learning** (outputs + corrections feed the model), **Cross-Domain Transfer** (a win in A lifts B), **Network Intelligence** (fleet patterns, privacy-gated).

**The test:** *"Freeze 3 months (one frontier cycle) — still win? If yes, you're not compounding."* Brutal and useful.

### 2.5 Shadow AI

Samsung: 3 leaks in ~1 month, no policy, no trail. Stated lesson: **"absence of governance = strategy failure."**

The PM-side reframe: shadow AI isn't only the CISO's tool-sprawl problem, it's what users build *around* your product. Audit flow: **Discover → Signal → Prioritize → Decide** (build / partner / ignore). Spotify's number: ~1,000 tools → 15 governed.

---

## 3. Agent architecture (Advanced Agents)

### 3.1 Sequencing rule

> **"Always start with a single agent, then refactor into multi-agent when you hit boundaries in skills, tools, or evaluations."**

This directly contradicts the instinct to build an agent team early, and it matches current published practice. Boundaries — not ambition — trigger the refactor.

### 3.2 Where to start (a genuinely good trick from your notes)

> *Ask your LLM: "look at my last 30 days of conversations, tell me where I'm spending most time, and what should be automated from that list."*

Evidence-led rather than guess-led skill selection. Worth running before writing any skill.

### 3.3 Governing agent teams

1. **Require a supervisor or critic agent** — automated oversight layer
2. **Log all agent-to-agent (A2A) messages** — non-negotiable for traceability
3. **Define autonomy ceilings per role** — *"your primary risk management lever"*

Multi-agent costs to control: max iterations (stops token burn-out loops), chat-history window (~30 days), max token per input (stops users pasting huge text), and latency — *"a big company moves slow, it's the same."*

### 3.4 Multi-agent metrics

| Metric | Tells you |
|---|---|
| Collaboration accuracy | Handoff success — is the workflow robust? |
| Redundancy rate | Are agents duplicating work? |
| Eval pass rate | Is each step meeting the bar? |
| Human intervention % | Governance health |

### 3.5 Why agents fail differently

Failures happen *invisibly*, inside reasoning chains: multi-step reasoning (flaws compound, or infinite loops), external tool use (misinterpreted results, unauthorised access attempts), persistent memory (errors and biases persist forward), collaboration complexity (handoff and arbitration failures).

### 3.6 MCP vs A2A

- **MCP** = vertical. Agent → system/tool. Scoped permissions, audit logs, least privilege. *"USB-C for AI."* Example: support agent may retrieve open cases, is denied billing modification.
- **A2A** = horizontal. Agent → agent. For workflow collaboration between agent networks.

**Secure MCP checklist** (course version):
- ☑ Define access scope — least privilege
- ☑ Create expiration rules — TTL on tokens/sessions
- ☑ Log every MCP event
- ☑ Human review for writes — HITL mandatory on modify/write
- ☑ Test for data leakage — evals that specifically probe exposure of MCP-retrieved data

### 3.7 Memory — "a user trust contract"

> *"Every memory-enabled agent must justify what it remembers, why, and for how long."*

**S.M.A.R.T. memory governance:** **S**coped · **M**onitored · **A**uditable · **R**etrievable · **T**imed.

Memory types: Episodic · Semantic · Vector/Embedding · External/Linked.

The risk of remembering: data leakage (→ minimisation + TTL), memory bias (→ diverse data + monitoring), knowledge drift (→ refresh + source validation), cost growth (→ storage strategy).

### 3.8 Zero trust + RBAC + PII masking

Stated baseline principle. PII masking applies **in the traces**, not just the store — usually available out of the box in S3 / Databricks / Snowflake. Worth noting: traces are the forgotten leak path, and this is the level of detail that reads as credible to a client CISO.

### 3.9 Evals are a team sport

Roles and their tasks, per the Agentforce-based slide:

| Role | Owns |
|---|---|
| AI engineer / agent builder | Real-world data, tweak tool calls, develop scorers |
| **Product Manager** | **Develop hypotheses, decide success criteria**, analyse results |
| Subject-matter experts | Label sample data, tweak prompts |
| Data analysts | Develop scorers, analyse results |

Note what the PM owns: **defining what "good" means**. That is the role you'd play with a client, and it's the one that doesn't require you to be an engineer.

Eval design: what are we testing (prompt or agent)? · where do scenarios come from (it can generate its own) · live or mock data · testing for what (completeness, coherence, latency) · **then schedule recurrence — daily/nightly** · monitor in analytics/observability.

---

## 4. Metrics — the full set, with my read on which matter *for you*

Course thresholds, annotated for a personal system that must scale to a client story:

| Metric | Course target | Real at personal scale? |
|---|---|---|
| **Hallucination rate** | <1% good · >5% very bad | **Yes — measure it.** Core credibility metric |
| **Eval regression** | 100% of changes stay positive on golden set | **Yes — the cheapest discipline with the highest payoff** |
| **HITL %** | Must shrink or compound, not grow linearly | **Yes — this is your compounding proof** |
| **Recall accuracy** | ≥85% | **Yes**, once you have a retrieval layer |
| **Trust score** (composite, RAGAS-style) | >0.8 | Useful, but derived — don't lead with it |
| **Drift velocity** | <0.5%/week · >2%/week bad | ⚠️ **Theatre at your volume.** Track *per model change*, not weekly |
| **Confidence distribution** | Avoid a fat middle | ⚠️ Needs volume to be meaningful |
| **Inference ROI** | >10% good · <3% bad | ⚠️ Not meaningful for a personal system; **essential in the client conversation** |
| **Deflection / containment rate** | — | ➖ Support-function metric, not yours |

**Be able to speak to all of them. Only instrument the first four.** Instrumenting metrics that are meaningless at your volume is the kind of thing a sharp client CTO will catch, and it costs you more credibility than not having them.

---

## 5. Commercial framing worth stealing

- **Moats:** for AI specifically, *data and workflow* matter most. Features get eaten by big players; **workflows survive**. The test: *"Can users switch in a weekend? Yes = trouble."*
- **The compounding question:** when a user corrects your AI, does it retrain the model (compounding) or generate a support ticket (not)?
- **Pricing:** per-seat breaks both ways under AI economics — overcharging light users, undercharging heavy ones, while costs rise per use. Outcome-based pricing works because the unit of charge matches the unit of value. AI *will* compress margins first. Mitigation: model cascading.
- **Three Horizons, AI-compressed:** H1 ship 0–4 weeks · H2 validate 1–3 months · H3 explore 3–6 months. **Revisit monthly, not annually.** This is the structure your roadmap now uses.
- **"A roadmap without a strategy is just a to-do list with deadlines."**
- **"Speed is the biggest moat now."**
- **Depth over breadth**; don't spend 60% of resources on undifferentiated work.

### The positioning slide

The whiteboard from Advanced Agents is, essentially, your job description:

```
        PM  ─────────►  Agent Era  ◄─────────  Engineer
 (pure strategy,     Taste + Judgment          (pure code,
   no building)    + Problem Shaping            no taste)
                  + Agent Orchestration
```

You are converging on that centre from the PM side. The showcase should demonstrate the centre — judgment about architecture, not just the ability to run a tool.

---

## 6. Where the three sources genuinely conflict

Worth knowing, because being able to arbitrate these *is* the expertise.

### 6.1 Retrieval: RAG vs agentic file search

- **Product School** teaches vector RAG as the default (PM ownership of retriever/knowledge-base/generator, RAGAS, recall ≥85%).
- **Current published practice** favours agentic file search over a plain-text corpus for personal and code knowledge bases — Anthropic's just-in-time retrieval guidance, and an Amazon Science result reaching ~94.5% of RAG faithfulness with no vector store.

**Both are right in context.** RAG wins at large scale, sub-second latency, and semantic-synonym search. Agentic search wins on freshness, simplicity, security (no second embedded copy) and small corpora — at higher token cost and seconds of latency.

**Resolution for you:** agentic file search for the personal vault. Introduce RAG only when you hit a condition that demands it — and be able to name the condition. *That decision rule, articulated out loud, is a better showcase moment than either architecture on its own.*

### 6.2 Multi-agent: when

Prisme One treats agents as a "shiny object" trap. Product School teaches multi-agent design in depth but gates it: single agent first, refactor at a boundary. **No real conflict** — Product School supplies the trigger condition the webinar lacks.

### 6.3 Security posture

Product School's MCP treatment is optimistic (scoped permissions, audit logs, governable). Independent security research on the MCP ecosystem is far more alarming (widespread path-traversal and injection findings, ~8.5% OAuth adoption, active CVEs). **Both are true:** MCP *as specified* is governable; MCP *as deployed in the wild* is largely not. The delta is your risk, and saying so in a client conversation is exactly the kind of nuance that separates an advisor from a vendor.

---

## 7. Immediate action items surfaced by these documents

1. **Revoke the Telegram bot token** in `Product School - Advanced Agents.pdf` (page ~2) via BotFather. Four Zoom recording passcodes are in the same file.
2. **Treat this as case zero.** A live credential sitting in a course PDF, in a folder you were about to point an agent at, is the Samsung slide happening to you. It belongs in the demo narrative — real, self-caught, and it makes the governance point better than any slide.
3. Run the *"last 30 days of conversations → what should I automate"* prompt before choosing which skills to build (§3.2).
4. Retrieve the four capstone tools from the LMS — Strategy Assembler, AI Bet Evaluator, Roadmap Builder, Pitch Builder — the Day 6 outputs are directly reusable for the client-facing narrative.
