---
classification: public
status: draft
updated: 2026-10-01
tags: [product-school, product-strategy, financials, unit-economics, kill-criteria, ai-leadership, modules/5-6]
---

# Product Strategy: financials, strategic bets and AI leadership (modules 5–6)

Modules 5–6 of Product School **Product Strategy**. Hub: [[30 Resources/Product School/README|Product School hub]]. Previous: [[product-strategy-leading-teams-and-influence]]. Overlaps with [[ai-unit-economics-and-pricing]] (AI-specific margin view). Own-words synthesis.

## Module 5: master product financials and strategic bets

**Product metrics vs finance metrics.** Product speaks in AARRR (acquisition: signup rate; activation: key action and time-to-first-action; retention: returning DAU/MAU; revenue; referral: NPS). Finance speaks in revenue, COGS, gross margin, OpEx, operating income. Pricing and retention drive revenue; build-vs-buy and infrastructure drive COGS; headcount is OpEx; strategic bets are judged at operating income.

**Bridging the gap.** "This will improve retention" is heard as a hypothesis with no return. Bridge: quantify via the chain, e.g. a lift in DAU correlates with a retention gain, which is worth incremental LTV per cohort, with first signal by week N and payback within X months.

**Unit economics:** LTV (ceiling on what you can spend) vs fully loaded CAC (floor on what you must earn; most CAC figures undercount sales overhead, onboarding and support, so ask what is included). **LTV:CAC** below 1:1 is burning runway, ~3:1 sustainable, above 5:1 room to accelerate. **Payback period**: shorter means more runway to act on learnings. Contribution margin shows what the product earns per customer before fixed costs.

**Reading a model you did not build (four checks):** which single assumption does the most work (what if it's 30% off)? what does the retention curve look like (optimistic retention is the most common flattering assumption; see LTV if churn is 10 points worse)? what is payback at a realistic CAC (+20%)? what are the kill criteria? **Every decision moves a number:** forward (reduce onboarding friction → 30-day retention → LTV → payback) and backward (NRR below 100% → expansion slowed or churn rose → which behaviour?). Ask in every review: which P&L line does this concern, and does it move the right way?

**What a bet actually costs:** ceiling (is the market big enough?), people beyond engineering (support, CS, implementation), opportunity cost (the team not staffed elsewhere, with someone's KPI), time to value.

**Kill criteria:** a specific, pre-agreed number that tells the team to stop before they've spent a quarter finding out. Too vague ("reassess if numbers aren't where we need by Q3") → specific but incomplete ("we will discuss next steps") → complete and actionable (threshold, date, consequence: "stop funding and reallocate the headcount before it is committed"). **Business case:** strategic bet (outcome, who, mechanism), assumptions ranked by weight, expected return (when, in board terms), kill criteria. Course example: a developer-tool company converting individuals to teams, with a conversion threshold and headcount trigger.

## Module 6: leveraging AI tools for leadership execution

**Stages of AI leverage:** (1) personal productivity (rough idea to PRD draft in minutes); (2) team capability (shared prompts and standards so quality holds and review moves faster); (3) org advantage (PRDs feed a shared system, one source of truth). Leadership lives in stages 2–3. Mapping of leadership work to captured capability: strategy (shared synthesis and pressure-test standard), prioritisation (trade-off memo for two bets you can't both fund), coaching (feedback themes before hard conversations), stakeholder alignment (pre-read plus objection set reused for every ask), financial bets (case with assumptions and kill criterion the team can defend). The capstone: encode your judgment as a portable skill file any AI tool can apply, which is the pattern behind David's own [[10 Projects/AI Second Brain/README|AI second brain]] (central memory, e.g. Obsidian, with prompts and templates so every document follows the same standards; stage 2 = everyone's notes captured automatically into central memory).

**Leading a team that builds with AI:** norms (where AI output ships alone vs needs human review, written as a one-page rule), risks (confident wrong answers, eroding skills, blurred ownership: name one skill you won't let AI absorb), culture (one named human owns each AI-assisted deliverable).

**Build, buy or partner on AI:** build when the capability is close to what makes you different; buy when it is table stakes and speed matters; partner when your edge is integrating depth you can't build. Moat test per path: what do you have that a competitor starting today couldn't assemble; what advantage from moving first can't be bought back; what does the integration give customers they couldn't get from the partner directly. AI changes costs on every path: usage-scaled infra cost, standing vendor dependency, permanent maintenance, data-ownership stakes.

**Why AI bets are hard to kill, and the fix:** name the bet with a metric (a demo is a toy, not a bet); define success thresholds and read date before launch; give a fair run but re-check the case when a model or price changes; pre-commit kill criteria and who must agree.

**Responsible AI decisions:** trust (when it is confidently wrong, does the product or the user catch it?), explainability (can we trace why it did what it did?), bias (who does it work worse for, and would that show in metrics?). The domain sets the stakes; ownership stays yours. See [[ai-governance-and-compounding]] and [[ai-trust-evals-and-reliability]].

## Course learner journey (one line each)
1 craft a defensible strategy; 2 outcome-based roadmap where each near-term bet traces to strategy; 3 diagnose team situations and open the hard conversation; 4 executive communication that aligns a stakeholder on a hard call; 5 a business case with a kill criterion sharp enough for someone outside your team to enforce; 6 judgment encoded as a skill file.
