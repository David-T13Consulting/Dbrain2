---
classification: public
status: draft
updated: 2026-10-01
tags: [product-school, ai-product-strategy, roadmap, metrics, board-pitch, module/6]
---

# AI roadmap, metrics and the board pitch (module 6, capstone "The Pitch")

Product School **AI Product Strategy**, session 6. Question: *how do you get this funded, shipped and adopted?* Integrate → translate → present. Hub: [[30 Resources/Product School/README|Product School hub]].

## Roadmap ≠ strategy

| Claim | Verdict | Note |
|---|---|---|
| "Our roadmap IS our strategy" | False | A roadmap is decisions made visible; features without a thesis hide the thinking. Strategy is the *why*, roadmap the *how and when*. "A roadmap without a strategy is a to-do list with deadlines" |
| "AI metrics = product metrics" | False | Add quality and cost signals *with* MAU and retention |
| "A great product sells itself" | False | AI adds messy demos, scarier errors and security reviews; necessary is not sufficient. A great product may also not stay great |

## Three horizons, compressed

An AI-adapted three-horizons model, **revisited monthly and measured in months, not years** (6 months maximum; things change too fast).

| Horizon | Horizon length | Confidence | Purpose |
|---|---|---|---|
| H1 Ship | 0–4 weeks | High | Execution and shipping to **gain credibility**; funds H2 |
| H2 Validate | 1–3 months | Medium | Bets with validation and **kill criteria**; the living strategy |
| H3 Explore | 3–6 months | Low | Small investments; are we seeing behaviour shifts? |

## The six AI metrics boards ask for

| Metric | Meaning | Board concern | Good / bad (course heuristics) |
|---|---|---|---|
| Hallucination rate | % of outputs with fabricated info | Liability | Good below ~1%; above ~5% is very bad (industry-specific) |
| Drift velocity | Speed of accuracy decay | Silent failure | Good below ~0.5% per week; bad above ~2% per week |
| Confidence distribution | Histogram of response confidence in production | Quality | Avoid a "fat middle": responses should be sure, or flagged as guesses |
| HITL rate | % needing human intervention | Scalability | Should stay small or fall; linear growth is bad, it must compound |
| Inference ROI | Revenue gained per $ of inference | Margin | Around 10% or more is good; below ~3% is bad |
| Eval regression | % of model changes that keep passing the golden set | Reliability | Target 100% |

"Durability beats hype; retention = quality." Thresholds are course heuristics, not standards; calibrate per industry and risk.

## Four board questions, three buckets

| Bucket | Question |
|---|---|
| **The case** (bet + moat) | 1. Why invest? 2. Why can't this be copied? |
| **The model** (margin) | 3. Does the math hold? |
| **The risks** (contract + guardrails) | 4. Trust, failure modes, scale? |

**Do not open with the model; open with the thesis.** Different audience means a different pitch: a board wants defensibility and economics; a CTO wants reliability and cost; founders want why-now and unfair advantage. Pick the real person you are pitching.

Pitch structure: **thesis, why now, what's defensible, economics, risks, ask** (state dollars, headcount and months; specific beats vague). Likely audience questions: why fund this and not X; moat at 6 months; margin under stress; kill plan.

Case: **Duolingo**. After the "GPT-4 inside" narrative stopped landing, mixed investor reaction pushed the story towards "does AI improve learning?" Fix: AI *extends the loop*; published outcomes and decks led with retention and learning. A related case: **Notion** reframed from a technology-first story to *learning-loop improvement*.

## The capstone: the living strategy repo

The deliverable of the whole certification is a **version-controlled repository** (not a document or deck), one component per module:

| Folder | Content |
|---|---|
| `01-the-bet` | Three-axis diagnostic + working prototype |
| `02-the-moat` | Data flywheel scoring, 90-day encroachment plan, kill-switch audit |
| `03-the-margin` | Cost curve, pricing model, board one-pager |
| `04-the-contract` | Golden dataset, confidence UX, reliability contract |
| `05-the-guardrails` | Compounding system, governance one-pager, shadow AI audit |
| `06-the-pitch` | Roadmap, board pitch, generated README |

Flow: components feed an assembler that generates a README, then a pitch builder tailored to one audience; the **board simulation** is 5 minutes presenting from the repo (no slides), 3 minutes of hard Q&A by a role-playing partner, in groups of two or three.

## Takeaways

1. Open with the thesis, not the model.
2. Add six AI-specific metrics to the board dashboard.
3. Plan in horizons of weeks to six months, not annual cycles.
4. Keep strategy as a living, versioned artefact.

## Using this for Tower13 and the second brain

The "living strategy repo" pattern is the same shape as this vault: plain markdown in git, one folder per decision area. The six metrics map onto the eval work in [[10 Projects/AI Second Brain/02_Architecture/success-thresholds|success-thresholds]]. Prior modules: [[ai-strategy-bet-and-moat]], [[ai-unit-economics-and-pricing]], [[ai-trust-evals-and-reliability]], [[ai-governance-and-compounding]].
