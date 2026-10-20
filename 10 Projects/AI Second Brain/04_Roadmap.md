---
classification: internal
note_type: plan
review_status: approved
created: 2026-09-07
updated: 2026-10-19
source: David's decisions of 19 Oct 2026 (Q119-Q121, Q127-Q131; D134-D140) and the sovereignty router proposal
---
# The Roadmap — Rented-compute second brain with a sovereignty router

**Rewritten 19 October 2026 after the pivot (D134–D140).** David decided not to buy hardware and to rent compute (Q121), and chose option A, pivot now (Q127–Q131). The plan before the pivot, including the S1–S6 stages, the 9 Oct amendment and the original H1/H2/H3 rationale, is kept verbatim at [[40 Archive/AI Second Brain/04_Roadmap-pre-pivot-2026-10-19]]. Design detail and sources: [[10 Projects/AI Second Brain/02_Architecture/sovereignty-router-proposal-2026-10-19|sovereignty router proposal]]. Demo of the target: [[10 Projects/AI Second Brain/05_App_Prototype/sovereignty-router-demo.html|sovereignty-router-demo.html]].

## 1 · What stays the same

- **End goal (David, 9 Oct, verbatim):** *"I need a second-brain AI-powered system available through text and voice on my phone, watch, macbook (and tesla) to be my source of knowledge (vault(s): personal and professional), have access to my context (MCPs to emails, calendar, documents, etc) and must be able to improve itself, learn and built itself from bits of information I throw at it."*
- **The thesis:** the personal system is the substrate; the evaluation and governance layer is the product. Demonstrate that AI can be made trustworthy enough for a regulated business, measured on David's own system first.
- **Demo-ready Fri 18 Dec 2026** (Q29).
- **Red line and data policy unchanged.** No client or counterparty confidential information enters the system. Data policy §1 and §5 already allow `public` and `internal` content to a model API once the provider's terms are verified; wave 2 sensitive material stays gated (it now needs L0 or a new decision).
- **Release gates G1–G4** (D126) stay: G1 reliable read-only assistant with a read-path injection suite; G2 safe memory writes (remember, recall, correct from the phone); G3 sensitive or professional use (data policy v1.0, before any work account); G4 one scoped, audited connector at a time.
- **"Learning"** means approved memory writes, corrections that replace facts, every confirmed failure becoming a regression case, and skills and prompts improved against those cases. No retraining.
- **Language:** English and French (D121).

## 2 · What changed (19 Oct)

| Before | Now | Decision |
|---|---|---|
| Local inference on the Air, then a Mac mini host | Rented models, EU provider by default (Scaleway, Mistral); no hardware purchase | D134, D135 |
| One local model chosen by T9/T9b | Switchable sovereignty levels L0–L3 behind one gateway; a router picks the level and model per request | D135, D138 |
| Phone Shortcut "Ask Brain", custom S4 voice build | Open WebUI on a rented EU server + Open Relay iOS app; the dbrain query service answers behind it | D136 |
| Up to 5 reviews per Tier 2 step | 1 Codex review per step, 2 for Tier 2 and security-boundary steps | D137 |
| S5 coordinator, curator and checker | The router is the coordinator; the answer check is the checker | D135 |
| T9b TwIL trial, M6b embedding test | T9b parked for a possible offline laptop level; M6b closes with its results note | D140 |

## 3 · Architecture

```
iPhone (Open Relay) ─┐
Mac / Obsidian ──────┼─► Open WebUI ─► dbrain query service ─► switchboard (LiteLLM) ─► L0 own GPU (EU)
Claude Code / Codex ─┘   (EU server)    retrieval, citations,     ceiling rules,         ├► L1 Scaleway / Mistral (EU)
                                         verdicts                  decision log          ├► L2 US cloud, EU region
                                                                                         └► L3 Claude API (global)
```

| Level | Meaning | Example | US CLOUD Act exposure |
|---|---|---|---|
| L0 | Own rented GPU, EU-owned host | Hetzner GEX44 (DE) | None |
| L1 | EU-owned provider, EU data centres | Scaleway, Mistral | None |
| L2 | US cloud, EU region | Claude or Mistral on AWS Bedrock Frankfurt | Yes |
| L3 | US frontier, global | Claude API | Yes |

**Router rules (D138, D139):**
1. **Ceiling by rules only.** Effective level = strictest of: David's toggle, classification of the retrieved notes, connector tier, a client watch-list hit in the question. Unknown or unlabelled means strictest.
2. **Client tier:** L1 or stricter until G3 passes and the T0.7 lawyer review is done.
3. **Task classifier at the floor level**, so the question never leaves the strictest level to be routed.
4. **Model choice:** first model in an eval-derived routing table that is inside the ceiling; escalate once to a stronger model on `incomplete`, same ceiling.
5. **No looser fallback.** If nothing inside the ceiling can answer, the reply says so.
6. **Overrides:** automatic routing with a visible level badge on every answer; David's manual override can only make a request stricter.
7. **Budget:** soft monthly cap with an alert; the cap never loosens the level.
8. **Whole-vault jobs** (embeddings, wiki maintenance) run at the strictest level in use.
9. **Decision log:** one text-free line per request (level, ceiling reasons, task type, model, cost, latency, verdict).

**Starting stack and expected cost** (estimates; usage of about 50 questions a day): EU server about €10/month; Qwen3.8-27B everyday model about $18/month; Claude Sonnet 5.5 for the questions allowed above L1 about $20–50/month; speech about $1/month. Typical total €40–60/month. Prices to be confirmed in week 1.

## 4 · Delivery plan to 18 Dec

Each week ends with checkable evidence. Weeks run Monday to Sunday; week 1 starts Tue 20 Oct.

| Week | Dates | Work | Exit evidence |
|---|---|---|---|
| **W1** | 20–25 Oct | Decisions recorded; review budget changed (D137); Scaleway terms verified against data policy §5; account and key (David); adapter for an OpenAI-compatible provider with explicit level, no fallback; dev and P2.5 cases re-run on Mistral Small 3.2, Qwen3.8-27B and Qwen3-235B against the committed baseline; switchboard core (LiteLLM, ceiling rules, decision log, level badge) on the Mac; P2.8 phone check with David — [[90 System/briefs/PV1-rented-models-and-switchboard\|PV1]] | A real question answered at L1 with badge and log line; ceiling tests pass (toggle, classification, watch-list, unlabelled, no looser fallback); measured p50/p95, verdicts and cost per model |
| **W2** | 26 Oct–1 Nov | Rented EU server (Hetzner Cloud or Scaleway) behind Tailscale; read-only vault sync; Open WebUI + Open Relay with dbrain as the answering model; voice (Whisper or Voxtral); "Wrong" moves to Open WebUI feedback (P2.7); trace hashes and secret-scanner scope fixed for the server; AS1 step 5 rescoped to the server; Shortcut path retired after cutover | Text and voice from the phone away from home with the Mac off; level badge visible; failure capture works |
| **W3** | 2–8 Nov | Task classifier; routing table for 3 task types from eval scores; escalate-once; soft budget alert; L3 route (Claude API key from David) for permitted questions | Routing decisions carry reason codes; table derived from evals; budget alert fires in a test |
| **W4** | 9–15 Nov | Restore test first (T4.2); ingest and wiki upkeep adapted from an LLM-wiki skill, changes proposed as exact git diffs, approved from the phone (P3.0–P3.3); read-path injection suite on retrieval and router (G1-inj); R1 configuration before connectors | **G1** and **G2** pass: remember, recall in a fresh session, correct without the old version resurfacing; injection suite passes |
| **W5** | 16–22 Nov | C0 connector brief; C1 personal calendar, read-only, least scope, revocable, audited | **G4** for C1: injection cases and revoke test pass |
| **W6** | 23–29 Nov | C2 personal mail, read-only; offline capture queue (P4.2, stretch) | G4 for C2 |
| **W7** | 30 Nov–6 Dec | Eval dashboard (T5); reliability contract (T6); backup and restore drill (P6.1); monitoring and retention checks (P6.3); governance one-pager (T8) | Restore drill passes; dashboard screen-shareable |
| **W8** | 7–13 Dec | Pinned releases (P6.2); synthetic demo scenario with a fictional client; two rehearsals including a controlled failure (T13); demo package (P6.4) | Two repeatable demos, no unexplained failures |
| **Demo week** | 14–18 Dec | Buffer; demo-ready Fri 18 Dec | — |

**Running track** (golden dataset, taxonomy v2, running corrections) continues alongside, as before.
**Workstream W** (data policy v1.0, gate G3) continues; work accounts (C3) come after the demo unless G3 passes first.

## 5 · Cut order if the plan slips

Cut in this order: (1) C2 mail moves after the demo; (2) offline capture queue; (3) the task classifier, falling back to rules-only routing; (4) the L3 Claude route. **Never cut:** ceiling rules with no looser fallback, the injection suite before any connector, the restore test before any write, the red line.

## 6 · Task mapping

TASKS is the checklist and PROGRESS the record. Old task IDs keep their numbers; what each became is listed in TASKS › Carried over and Parked or cut. The full pre-pivot task list is archived at [[40 Archive/AI Second Brain/TASKS-pre-pivot-2026-10-19]].
