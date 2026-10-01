---
classification: public
status: draft
updated: 2026-10-01
tags: [product-school, ai-product-strategy, evals, trust, golden-dataset, module/4]
---

# AI trust, evals and reliability contracts (module 4, "The Contract")

Product School **AI Product Strategy**, session 4. Question: *why will users trust a probabilistic system?* Define → measure → design. Hub: [[30 Resources/Product School/README|Product School hub]].

## Trust is not accuracy

| Claim | Verdict | Reasoning |
|---|---|---|
| "Higher accuracy = more trust" | False | Trust follows **perceived control**. An 85% system with confidence scores, explanations and override beats a 95% black box |
| "Users don't care how the AI works" | False | They care about **reliability signals**: confidence, citations, "I'm not sure". Legibility is a product feature |
| "We'll add evals after we ship" | False | AI degrades silently (model drift, data shift, prompt injection). **Evals are launch infrastructure**, not technical debt |

Real-world anchors: driver-assist UIs that hand control back as confidence drops; answer engines that lead with sources. **Understandable and controllable wins, even at a lower benchmark %.**

## Golden datasets: labelled truth as ship-blocking infrastructure

Purpose, three jobs: **regression** (every prompt or model change is scored before users feel it), **domain anchor** (your definition of "good", not a public leaderboard) and **proof for buyers** ("show me how you test": the golden set is the demo).

Spec rules from the course:

- Start with about 10 cases to learn the format; ship target about 150; mature sets are 100–500 rows.
- Include **20–30% edge cases** and some **adversarial rows** (inputs that would break most systems).
- Each row: input, expected output, edge-case flag, and **judge type** (rule, LLM, or both).
- You must **write it yourself**, because it encodes your domain judgement, and **version it like code** (git). Update it when the world changes. Report dataset health: row count, edge-case share, judge mix.
- Sales test: one sentence, "here's how we test our AI."

Worked example in class: a scam-detection bot with rows such as a price far below market (rule judge), a seller with no reviews (rule judge), and an off-platform approach (LLM judge).

## Confidence UX: three modes, not one answer

| Mode | Behaviour |
|---|---|
| Confident (above about 90%) | Full answer with reasoning |
| Uncertain (about 50–90%) | Soften language, avoid hard commitments, show what is consistent with each outcome, ask the user to do more checking |
| Not confident (below about 50%) | Withhold the output, explain that the data does not settle it, escalate or block |

Plus a **user control surface**: see the AI's reasoning, correct and override, corrections feed the model or dataset, optionally adjust the confidence threshold. Capture the choices explicitly.

## Human-in-the-loop as a shrinking queue

| Crutch (anti-pattern) | Feature (design) |
|---|---|
| Review everything: cost explodes, fixes vanish | Thresholded review: low score → human, high score → auto |
| | Capture every fix as fuel for the data flywheel ([[ai-strategy-bet-and-moat]]) |
| | Escalation UX: make uncertainty visible, let the user opt in |

A healthy product shows a **falling HITL rate** over time (examples: clinician sign-off on high-risk imaging or ambient-scribe outputs).

## LLM-as-a-judge

Automated scoring calibrated against your golden set: **regression** (judge vs golden rows, continuously), **drift** (trend alerts before NPS craters), **quality gates** (live route: auto vs human vs block). Vendors (e.g. LangSmith, Braintrust) supply judges and traces; **you still own the labels**. "Who judges the judge? Your golden dataset."

## The eval dashboard spec

Think an SRE status page for model quality: **metrics** (quality, latency, confidence spread, HITL %, overrides), **judge setup** (model, rubric, golden set, thresholds), **drift alerts** (auto-ping when a trend crosses a line), **UX hooks** (scores shown in UI, citations, thumbs-up loops). Test: *if you cannot screen-share it in a sales call, it is not product-grade.*

## The reliability contract

Per metric: **target**, **measurement method**, **alert threshold**, plus an HITL architecture and consequence patterns (page someone, auto-rollback, human queue). Worked example (customer-support copilot): accuracy ~92% via weekly rubric-scored golden runs (alert below ~86%); hallucination rate under 1% from production monitoring (pause or roll back if above 2%); latency p95 under 800 ms; drift velocity under 0.5% per week (alert above 1% decay). Rule: *wrong numbers get corrected; mush doesn't.* The contract must be **specific**.

Case: **Air Canada**. A support chatbot invented a bereavement-fare policy; the customer relied on it; the airline argued the bot was a separate entity; the tribunal held the company liable. Lesson: your AI's promises are your company's promises, so you need receipts, thresholds and human-in-the-loop.

## Takeaways

1. Trust is a function of perceived control, not accuracy.
2. Golden datasets are your receipts: version them, use them as a release gate.
3. Reliability contracts are not metaphors; specify, measure and enforce.

## Relevance to the second-brain build

This is the source of the project's eval-and-governance thesis: golden labels, blind scoring, dated baselines, thresholds before output. See [[10 Projects/AI Second Brain/03_Product_School_Playbook|03_Product_School_Playbook]] and [[10 Projects/AI Second Brain/02_Architecture/success-thresholds|success-thresholds]].
