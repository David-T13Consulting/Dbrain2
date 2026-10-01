---
classification: internal
---
# Project — AI Second Brain

**Also called:** the second brain, the AI system, the showcase system
**Status:** Active · Week 0 of 13 · Started 7 Sep 2026 · Target Dec 2026
**Location:** `~/Documents/Dbrain2/10 Projects/AI Second Brain/`

## What it is

A personal AI system built as **live, screen-shared proof of expertise** for consulting clients. The personal productivity system is the substrate; the evaluation and governance layer is the actual product.

Reframed from the original goal ("a personal AI system that makes me productive") because that isn't showcaseable — every creator claims it, and the demo is unfalsifiable. What is scarce: demonstrable competence at making AI trustworthy enough for a regulated business.

## Why it matters to David

He is a consulting director advising EU/US banking, US asset management, and Belgian healthcare/medtech. His clients will need **secure and collaborative** AI systems. This project is simultaneously:
1. His personal productivity system
2. A reference architecture he can walk a client through
3. Proof he has done it himself, with receipts

Commercial thesis, from his own course material: **Governance = GTM.** Level 1 maturity is compliance, where most organisations plateau. Level 3 is a governance story that closes deals.

## The three sources

| Source | Contributes | Weakness |
|---|---|---|
| Prisme One webinar | Personal architecture — vault, skills, context layers | No evals, no security, no governance; solo-creator scope |
| Product School | Rigour + commercial framing — golden datasets, eval dashboards, reliability contracts, agent governance | Enterprise framing, assumes a team, RAG-default retrieval |
| Current published practice | Mechanics and reality — agentic retrieval, Agent Skills/AGENTS.md, MCP threat model, vendor retention shifts, EU AI Act | No view on his specific goal |

Two of three land on Obsidian-style plain-markdown central memory, independently. That convergence is why the substrate choice is trusted.

## Shape of the plan

13 weeks on compressed Three Horizons. Week 0 foundations → H1 ship (weeks 1–4, ending in a golden dataset and wired evals) → H2 validate (5–9, the artifacts that make it credible) → H3 collaborate (10–13, multi-user then multi-agent, then demo rehearsal).

Full detail: `04_Roadmap.md`. Never summarise it from memory — read it.

## The critical path

**Everything depends on choosing the showcase workflow** (OQ-1 / T0.4). Without it there are no skills, no golden dataset, no evals, no demo. It must have a checkable right answer or the whole instrumentation thesis collapses.

## What would make this fail

1. Scope creep into infrastructure — the server work is fun and proves nothing
2. The golden dataset never getting written because it's boring
3. The vault becoming a reading list (collector's fallacy)
4. Client-confidential data entering the system
