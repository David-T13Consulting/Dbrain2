---
classification: internal
note_type: plan
review_status: approved
created: 2026-09-07
updated: 2026-10-21
source: David's decisions of 19 and 21 Oct 2026 (Q119-Q121, Q127-Q131, Q136-Q137; D134-D141) and the sovereignty router proposal
---
# The Roadmap — Rented-compute second brain with a sovereignty router

**Rewritten 19 October 2026 after the pivot (D134–D140); re-sequenced 21 October into three stages (D141).** David decided not to buy hardware and to rent compute (Q121), and chose option A, pivot now (Q127–Q131). The plan before the pivot, including the S1–S6 stages, the 9 Oct amendment and the original H1/H2/H3 rationale, is kept at [[40 Archive/AI Second Brain/04_Roadmap-pre-pivot-2026-10-19]] (a working copy from 19 Oct afternoon; the exact pre-pivot text is in git at `e7b558e`). Design detail and sources: [[10 Projects/AI Second Brain/02_Architecture/sovereignty-router-proposal-2026-10-19|sovereignty router proposal]]. Demo of the target: [[10 Projects/AI Second Brain/05_App_Prototype/sovereignty-router-demo.html|sovereignty-router-demo.html]].

## 1 · What stays the same

- **End goal (David, 9 Oct, verbatim):** *"I need a second-brain AI-powered system available through text and voice on my phone, watch, macbook (and tesla) to be my source of knowledge (vault(s): personal and professional), have access to my context (MCPs to emails, calendar, documents, etc) and must be able to improve itself, learn and built itself from bits of information I throw at it."*
- **The thesis:** the personal system is the substrate; the evaluation and governance layer is the product. Demonstrate that AI can be made trustworthy enough for a regulated business, measured on David's own system first.
- **Demo-ready Fri 18 Dec 2026** (Q29).
- **Red line and data policy unchanged.** No client or counterparty confidential information enters the system. Data policy §1 and §5 already allow `public` and `internal` content to a model API once the provider's terms are verified; wave 2 sensitive material stays gated (it now needs L0 or a new decision).
- **Release gates G1–G4** (D126) stay: G1 reliable read-only assistant with a read-path injection suite; G2 safe memory writes (remember, recall, correct from the phone); G3 sensitive or professional use (data policy v1.0, before any work account); G4 one scoped, audited connector at a time.
- **"Learning"** means approved memory writes, corrections that replace facts, every confirmed failure becoming a regression case, and skills and prompts improved against those cases. No retraining.
- **Language:** English and French (D121).
- **Evaluation evidence:** the 10 dev cases read a frozen copy of the pre-pivot roadmap section 0, outside the live roadmap (Q136), so every level is compared on the same text.

## 2 · What changed

**19 Oct (pivot, D134–D140):**

| Before | Now | Decision |
|---|---|---|
| Local inference on the Air, then a Mac mini host | No hardware purchase; rented models from an EU provider (Scaleway) for the hosted stage | D134, D135 |
| One local model chosen by T9/T9b | Switchable sovereignty levels behind one gateway; a router picks the level and model per request | D135, D138 |
| Phone Shortcut "Ask Brain", custom S4 voice build | For the hosted stage: Open WebUI on a rented EU server + Open Relay iOS app; the dbrain query service answers behind it | D136 |
| Up to 5 reviews per Tier 2 step | 1 Codex review per step, 2 for Tier 2 and security-boundary steps | D137 |
| S5 coordinator, curator and checker | The router is the coordinator; the answer check is the checker | D135 |

**21 Oct (three stages, D141):** David wants small wins in three stages, each usable on its own: **(1) a second brain on the Mac**, local, reachable from the phone over Tailscale with voice and vault updates; **(2) a second brain with Claude Code** working directly in the vault; **(3) a hosted, GDPR/EU-friendly second brain** that brings the three together behind the router. They are three levels of one system: same vault, same query service, same evaluation set. T9b step 4 resumes to pick the Mac's model (amends D140).

## 3 · Architecture

```
Stage 1   iPhone Shortcut ─(Tailscale)─► Mac Air: dbrain query service + local model      [level L0]
Stage 2   Claude Code (Mac, or the Claude app remotely) ─► vault skills: ingest, query, lint  [level L3]
Stage 3   iPhone (Open Relay) ─► Open WebUI (EU server) ─► dbrain ─► switchboard (LiteLLM) ─► L0 Mac · L1 Scaleway · L3 Claude
```

| Level | Meaning | Example | US CLOUD Act exposure |
|---|---|---|---|
| L0 | Own machine: nothing leaves David's hardware | Mac Air with the local model (a rented single-tenant GPU would also sit here; not planned) | None |
| L1 | EU-owned provider, EU data centres | Scaleway (Paris), hosting Qwen, Gemma and Mistral models | None claimed; `unverified` (sub-processors to be checked) |
| L2 | US cloud, EU region | Claude or Mistral on AWS Bedrock Frankfurt | Yes |
| L3 | US frontier, global | Claude API, Claude Code | Yes |

L0 is available only while the Mac is awake and on Tailscale.

**Router rules (D138, D139):**
1. **Ceiling by rules only.** Effective level = strictest of: David's toggle, classification of the retrieved notes, connector tier, a client watch-list hit in the question. Unknown or unlabelled means strictest.
2. **Client tier:** L1 or stricter until G3 passes and the T0.7 lawyer review is done.
3. **Task classifier at the floor level** (at L0 when the ceiling is L0), so the question never leaves the strictest allowed level to be routed.
4. **Model choice:** first model in an eval-derived routing table that is inside the ceiling; escalate once to a stronger model on `incomplete`, same ceiling.
5. **No looser fallback.** If nothing inside the ceiling can answer, the reply says so and nothing is sent elsewhere.
6. **Overrides:** automatic routing with a visible level badge on every answer; manual override can only make a request stricter.
7. **Budget:** soft monthly cap, alert at €50 (Q135); the cap never loosens the level.
8. **Whole-vault jobs** (embeddings, wiki maintenance) run at the strictest level in use.
9. **Decision log:** one text-free line per request (level, ceiling reasons, task type, model, cost, latency, verdict).

**Expected cost of the hosted stage** (estimates; about 50 questions a day): EU server about €10/month; a Scaleway everyday model about $3–18/month depending on the model; Claude for the questions allowed above L1 about $20–50/month. Typical total €40–60/month. That rented models beat the local one is an expectation, `unverified` until PV1 step 5 measures it.

## 4 · Delivery plan to 18 Dec, in three stages

| Stage | Dates | Work | Done when |
|---|---|---|---|
| **Stage 1 · On the Mac** | 20 Oct–**1 Nov, hard stop** | Finish PV1 step 4 (adapter, already in progress) and freeze the dev-case evidence (Q136); pick the Mac's model (T9b step 4, with David); voice on the phone (iPhone dictation in, spoken answer out, built into the Shortcut); restore test (T4.2); vault updates from the phone: "remember …" becomes a proposed exact change, approved on the phone, written by one writer; P2.8 phone check — [[90 System/briefs/PL1-mac-second-brain\|PL1]] | From the phone over Tailscale, by voice: ask and hear a cited answer; remember a fact, approve it, recall it in a fresh session, correct it without the old version resurfacing. Nothing leaves the Mac. Unfinished parts move to stage 3 |
| **Stage 2 · With Claude Code** | 2–8 Nov | Vault skills for Claude Code adapted from an LLM-wiki skill (ingest, query, lint); every change is a git diff David approves; the same evaluation questions scored for stage 1 and stage 2; usable from the phone through the Claude app | One raw capture ingested into connected notes with David's approval; the evaluation set scored at L0 and L3 side by side |
| **Stage 3 · Hosted, EU** | 9 Nov–6 Dec | Scaleway key (David) and measurement of Qwen, Gemma and Mistral models against the baseline (PV1 step 5); switchboard with ceiling rules, decision log and badge (PV1 step 6); rented EU server, Open WebUI + Open Relay, voice, cutover from the Shortcut (PV2); router across L0 Mac, L1 Scaleway and L3 Claude, with task classifier and routing table; read-path injection suite (G1-inj); personal calendar read-only (C1, cut first) | The phone works with the Mac off; each answer shows its level; the same question routed to three levels with reasons and cost; injection suite passes |
| **Operate and demo** | 7–13 Dec | Backup and restore drill, eval dashboard, governance one-pager, pinned releases, two rehearsals with a fictional client and a controlled failure | Two repeatable demos, no unexplained failures |
| **Demo week** | 14–18 Dec | Buffer; demo-ready Fri 18 Dec | — |

**Running track** (golden dataset, taxonomy v2, running corrections) continues alongside. **Workstream W** (data policy v1.0, gate G3) continues; work accounts (C3) and personal mail (C2) come after the demo unless time remains.

**Gates:** G2 (safe writes) at the end of stage 1, on L0; G1 (reliable read-only, with injection suite) and G4 (C1) in stage 3; G3 after the demo unless W finishes early.

## 5 · Cut order if the plan slips

Cut in this order: (1) C1 calendar moves after the demo; (2) the task classifier, falling back to rules-only routing; (3) the L3 route inside the hosted router (stage 2 still covers Claude). **Never cut:** ceiling rules with no looser fallback, the restore test before any write, the injection suite before any connector, the red line.

## 6 · Task mapping

TASKS is the checklist and PROGRESS the record. Old task IDs keep their numbers; what each became is listed in TASKS › Carried over and Parked or cut. The full pre-pivot task list is archived at [[40 Archive/AI Second Brain/TASKS-pre-pivot-2026-10-19]].
