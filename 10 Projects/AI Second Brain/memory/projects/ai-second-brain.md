---
classification: internal
---
# Project — AI Second Brain

**Also called:** the second brain, the AI system, the showcase system
**Status:** Active · S1 architecture alignment; running validation alongside · Started 7 Sep 2026 · Target Dec 2026, to re-estimate
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

Amended 1 Oct (D45–D48): S1 architecture → S2 local read-only answers → S3 supervised wiki updates → S4 remote text/voice → S5 measured multi-agent execution → S6 operations/demo. Original H1/H2/H3 work packages remain as history; additional human users are deferred.

Full detail: `04_Roadmap.md`. Never summarise it from memory — read it.

## The critical path

Running was selected (D14/D15); the wiki is shared platform work (D47). Next: inventory the Mac, define acceptance criteria and benchmark local retrieval/answers. Running labels continue independently; no requirement to finish all 150 before platform experiments.

## What would make this fail

1. Building infrastructure without measured need; start with one controlled inference host
2. Claiming reliability without separate platform/domain evaluation and an untouched acceptance set
3. The vault becoming a reading list (collector's fallacy)
4. Client-confidential data entering the system
