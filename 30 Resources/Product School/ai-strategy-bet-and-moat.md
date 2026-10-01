---
classification: public
status: draft
updated: 2026-10-01
tags: [product-school, ai-product-strategy, moat, strategy, module/1-2]
---

# AI strategy: the bet and the moat (modules 1–2)

Part of the Product School **AI Product Strategy** certification (6 sessions, 2026.1 cohort). Hub: [[30 Resources/Product School/README|Product School hub]]. This page covers **M1 The Bet** and **M2 The Moat**. Own-words synthesis of David's course notes and slide captures; figures are as presented in class and unverified.

## The premise: five assumptions that break with AI

| Traditional product strategy assumes | With AI |
|---|---|
| A feature works or it doesn't | Outputs are **probabilistic**: accuracy, hallucination, drift |
| Infrastructure scales predictably | Inference cost scales with **usage**, not users |
| Your product competes with other products | Your feature can become a **platform checkbox** overnight |
| Software does what it says | Users must be **convinced** to trust uncertain output |
| Annual planning cycles | Capabilities change **weekly**: make bets, not plans |

Each of the six modules attacks one of these. See [[ai-unit-economics-and-pricing]] (cost), [[ai-trust-evals-and-reliability]] (trust), [[ai-governance-and-compounding]] (scale) and [[ai-roadmap-and-board-pitch]] (planning).

## M1 The Bet: diagnose, discover, decide

- **AI strategy in one sentence:** use AI to test, ship and iterate faster. The product need not be labelled "AI"; AI is one possible solution, not the point.
- **Exercise:** answer "what's our AI strategy?" in three sentences, privately, before the course reframes it.
- **Probabilistic thinking.** Leaders want commitments; models produce distributions. The skill is to replace "ship X by Q3 for Y result" with "70% this hits Y; here is how we will know, and when we stop" (bets plus **kill criteria**).
- **Discovery is too slow.** Classic research and synthesis takes 6–8 weeks; AI-assisted discovery should take days. Case as presented: Notion compressed an AI-editor insight loop to about 4 days using AI clustering and synthetic users, while incumbents were still synthesising.
- **Non-consumption wins.** Products that win create new behaviours rather than fight for old category labels (Shopify, Gamma, Granola cited). Example from the notes: Gamma expected big corporations and was adopted by small groups wanting to communicate a message.
- **Two starting points** (show of hands): AI added to an existing product, or AI-native (intelligence is the core, not a sidebar). Same playbook for both.

### Five AI value archetypes

| Archetype | What it does | Margin shape | Governance load | Example given |
|---|---|---|---|---|
| Automator | Replaces tasks | Volume play, cost pressure | High if errors hurt | UiPath |
| Copilot | Augments people | Scales with seats | Human in the loop | GitHub Copilot |
| Oracle | Surfaces hidden signals | Premium pricing | High, drives decisions | Palantir |
| Creator | Makes new assets | Copycats fast | Low unless regulated | Midjourney |
| Orchestrator | Chains agents and tools | High value, infra spend | Autonomy risk | Zapier AI |

Use it to avoid saying "AI" as if it were one economic profile.

### Three-axis diagnostic (score each 1–5)

1. **Contextual moat:** workflow depth × switching cost. 1 = generic wrapper, 5 = deeply embedded proprietary context.
2. **Data advantage:** a proprietary signal that compounds. 1 = no unique data, 5 = compounding proprietary dataset.
3. **Platform exposure:** could OpenAI, Google, Apple or Microsoft ship your hero feature natively, and how fast? 1 = big tech ships it tomorrow, 5 = years to replicate.

Output: three scores, a rationale each, one **named attacker** per axis, and a single top vulnerability with a confidence level. Honest scoring matters: all 5s means you have not looked hard enough, and a partner stress-test surfaces what self-assessment misses.

**Prototype requirement:** a clickable prototype of the bet in about 15 minutes with a vibe-coding tool, because "a working prototype in 15 minutes beats a strategy deck in 15 days". The prototype is evidence, not decoration.

## M2 The Moat: why won't this be copied in 6 months?

Three steps: **map** where defensibility lives, **stress-test** who attacks from where and how fast, **protect** with vendor portability.

### The eight moats

| Moat | What defends | Example |
|---|---|---|
| Data | Proprietary data that compounds with usage | Bloomberg, Gartner |
| Workflow | Deep process embedding that raises switching cost | Salesforce, SAP, ServiceNow, Workday |
| Regulatory | Compliance certifications rivals must earn from scratch | Palantir; Revolut (permissions) |
| Distribution | Owned channel controlling discovery and adoption | Apple App Store, Spotify, Netflix |
| Ecosystem | Third-party integrations that lock in interdependence | Shopify, Atlassian |
| Network | Each user raises value for all users | LinkedIn, Instagram, Airbnb, Uber |
| Physical | Hardware or infrastructure hard to copy | Tesla, SpaceX |
| Scale | Unit economics that improve with volume | AWS |

You need **one that is real**, not all eight. For AI products, **data and workflow matter most**.

### Features get eaten; workflows survive

- Case: a ~$1.5B AI-writing "wrapper" collapsed from rapid growth to a steep decline when ChatGPT made AI writing free and native everywhere. Wrappers are features, and features get absorbed by platforms.
- **Workflow depth spectrum** (switching cost): chatbot (switch in a day) → in-document assistant → embedded in editor + PR + CI → operating system (switching = rebuilding the business). Test: *can users switch in a weekend? If yes, you are in trouble.*
- Distinguish **workflow gravity** from a nice UI.

### The moat isn't your data, it's your loops

Having data is no longer an advantage by itself (example from the notes: a user stays with one assistant because it already knows them, not because the model is better). What matters is a mechanism that makes data **compound**. Ask: when a user corrects your AI, does that signal disappear, trigger a support ticket, or automatically improve the system?

Three data types that compound: **corrections** (user fixes become proprietary training signal), **preferences** (every edit builds a taste profile), **domain context** (industry knowledge generic models lack).

### Data flywheel scoring (four loops, 1–5 each)

| Loop | Question | 1 | 5 |
|---|---|---|---|
| Correction | Do users fix AI output, and is the signal captured and reused? | No capture | Automated retraining |
| Preference | Does it learn individual/team preferences over time? | Stateless | Deep personalisation |
| Domain context | Does use in one area improve quality in adjacent areas? | Siloed | Cross-domain transfer |
| Network | Does each user/team improve the product for everyone? | Isolated | Strong network effects |

The weakest loop is the biggest vulnerability: that is where competitors attack.

### Encroachment: who attacks, from where, with what

Three vectors, each with an **attacker**, **time-to-threat** and **% of value at risk**:

1. **Platform encroachment:** which platform could ship your core feature natively, and how long would it take?
2. **Vertical competitor:** which startup builds the same thing deeper in one niche, with data you lack?
3. **Adjacent expansion:** which neighbour could add your feature as "one more thing", with a distribution edge?

**90-day encroachment drill (pair exercise):** the *defender* presents scored loops and top threat; the *encroacher* plays Head of Product at a rival and presents a 90-day plan to steal the weakest loop's users (weeks 1–4 what they ship, 5–8 how they poach, 9–12 why users don't return); swap roles. The discomfort is the point: if the partner's plan sounds realistic, the moat has a crack.

### Kill switch: swap any AI vendor in under 48 hours

| Layer | Requirement |
|---|---|
| Abstraction layer | No direct provider API calls in product code (an internal "AI gateway") |
| Multi-model routing | Tasks route by cost, latency and quality; if a provider fails, traffic shifts |
| Eval harness | Automated tests prove the new provider meets the quality bar |

Audit rows: provider, abstraction, routing, eval; each with current state, a risk level and a 48-hour action plan, ending in a portability score (full, partial, none). Trigger test from the notes: *if the vendor raises prices 50% or quality drops, what can you do?* **If you cannot swap in 48 hours, that is not a strategy, it is a dependency.**

## Takeaways

1. AI strategy is probabilistic: bets with kill criteria replace promises.
2. Data in a database is not a moat; **loops that compound** are.
3. Self-assessment is always generous; use a partner attack to find blind spots.
4. Vendor portability is strategy, not operations.

## Cross-links

- Digest with action items for David's own build: [[10 Projects/AI Second Brain/03_Product_School_Playbook|03_Product_School_Playbook]].
- Overlap with this vault's own design: the kill-switch audit maps to the local-model fallback decision in [[30 Resources/Local AI/README|Local AI]].
