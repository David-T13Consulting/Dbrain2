---
classification: internal
review_status: approved
---
# Tasks — AI Second Brain Project

**Updated:** 19 Oct 2026 (Cowork: pivot to rented compute, D134–D140) · **Plan:** [[10 Projects/AI Second Brain/04_Roadmap|04_Roadmap]] §4, weeks W1–W8 · **Target:** demo-ready Fri 18 Dec 2026 (Q29)

Open items only, one line each; detail lives in the linked brief or the roadmap. The pre-pivot list, with every item's full wording and history, is archived verbatim at [[40 Archive/AI Second Brain/TASKS-pre-pivot-2026-10-19]]; older done items are in [[10 Projects/AI Second Brain/TASKS-archive|TASKS-archive]]. Owner tags per D63 and Q17; conventions at the end.

## ▶ Next action · W1 (20–25 Oct)

- [ ] `@code` ⭐ **PV1** Rented models and the switchboard core: record, provider terms, adapter, measurement, ceiling rules, decision log, level badge — [[90 System/briefs/PV1-rented-models-and-switchboard|PV1]]
- [ ] `@david` **PV1 step 3:** Scaleway account, budget alert, API key into the macOS Keychain (never a file); set the soft-cap alert threshold (D138, placeholder €75 a month)
- [ ] `@david` **P2.8 phone check** with the lead: "is there climbing class on november 2?" from "Ask Brain 5" (PV1 step 7)
- [ ] `@code` **M6b S5** Results note, then close M6b (lexical baseline stays; D140; one review) — [[90 System/briefs/M6b-embedding-eval|M6b]]
- [ ] `@cowork` Draft the **PV2** brief (EU server, Open WebUI, Open Relay, voice, cutover) for W2, with server options (Hetzner Cloud DE vs Scaleway FR) and how the server reads the vault (read-only)
- [ ] `@cowork` Revise `90 System/skills/weekly-desktop-digest/SKILL.md` for the five Codex blockers (handoff, 9 Oct); the lead re-reviews

## W2 · EU server, phone and voice (26 Oct–1 Nov)
- [ ] `@code` **PV2** Rented EU server behind Tailscale; read-only vault sync; Open WebUI + Open Relay with dbrain as the answering model; voice (Whisper or Voxtral); Shortcut path retired after cutover (D136; replaces P4.1, P4.3, P2.4 follow-ups)
- [ ] `@code` **P2.7** "Wrong" moves to Open WebUI feedback; failure store and 1-hour window kept as in data policy §7a — [[90 System/briefs/P2.7-failure-capture-loop|P2.7]]
- [ ] `@code` 🔴 **Trace question hashes:** salt per install (key outside agent reach) or drop; filenames in traces are personal data (D126); fix before traces live on the server
- [ ] `@code` 🔴 **Secret scanner scope:** extend to the vault and handoff files, or record why not (D126)
- [ ] `@code` **P2.7 retention after downtime:** purge test at first start after downtime (D126)
- [ ] `@code` **AS1 step 4** startup check; **step 5** rescoped: close the D110 Air exception by moving the service to the server — [[90 System/briefs/AS1-agent-setup-hardening|AS1]]
- [ ] `@code` **P4.4** Away-from-home test on each device class (phone, iPad, Mac)

## W3 · Router intelligence (2–8 Nov)
- [ ] `@code` Task classifier at the floor level; routing table for 3 task types from eval scores; escalate once on `incomplete`; soft budget alert (D138)
- [ ] `@david` Claude API key into the Keychain for the L3 route
- [ ] `@code` **T4.1** Versioned evaluations per task type (deterministic checks first; model judge with human spot checks) — feeds the routing table
- [ ] `@codex` **P2.1** Independent review of the retrieval cases; keep an untouched acceptance subset — [[90 System/briefs/P2.1-review|P2.1-review]]

## W4 · Safe writes and injection suite (9–15 Nov) · gates G1, G2
- [ ] `@code` **T4.2** Rollback and independent restore test on a disposable copy, before any write
- [ ] `@code` **P3.0–P3.3** Update the brain by voice or text with approval: ingest adapted from an LLM-wiki skill, pending patches as exact git diffs bound to the base revision, one writer — [[90 System/briefs/P3.0-update-my-brain|P3.0]]
- [ ] `@code` **G2** From the phone: remember, recall in a fresh session, correct without the old version resurfacing; rejection, concurrent Obsidian edit and interrupted save included (D126)
- [ ] `@code` **G1-inj** Read-path injection suite on retrieval and router (instructions in notes, fabricated authority, exfiltration, cross-domain retrieval) — [[90 System/briefs/G1-inj-read-path-injection|G1-inj]]
- [ ] `@code` **R1** Profile, allowlist and per-vault policy from configuration, before C1 (D126)

## W5–W6 · Connectors (16–29 Nov) · gate G4
- [ ] `@cowork` **C0** Connector-technology brief with options (MCP servers vs direct read-only APIs)
- [ ] `@cowork` design, `@code` build **C1** Personal calendar, read-only, least scope, revocable, audited (W5)
- [ ] `@cowork` design, `@code` build **C2** Personal mail, read-only (W6; first cut if the plan slips)
- [ ] `@code` **P4.2** Durable offline capture queue (D54; stretch, second cut)

## W7–W8 · Operate and demonstrate (30 Nov–13 Dec)
- [ ] `@code` **T5** Eval dashboard · **T6** reliability contract · **P6.1** backup and restore drill · **P6.3** monitoring, redaction, retention checks
- [ ] `@code` **Ops (D126):** retention for backups and audit logs; release bound to exact code, model, prompt and corpus versions; incident procedure
- [ ] `@cowork` **T8** Governance one-pager (Q28)
- [ ] `@code` **P6.2** Pinned releases and rollback · **P6.4** demo package (needs its own authorisation) · **T13** two rehearsals with a controlled failure, synthetic fictional-client scenario
- [ ] `@code` **T12** Security checks: injection and write tests before W4 writes, remote-access checks before W2 exposure, full audit in W7

## Usable security · workstream W (gate G3)
- [ ] `@cowork` **W1** Draft data policy v1.0 (tier by source, contract gate, query live and persist little, read-only revocable connectors, client tier at L1 or stricter per D139, no agent access to client-tier data or tokens) — overdue
- [ ] `@cowork` draft, `@david` + lawyer **T0.7** Tower13 subcontract AI-use clause and processing annex — overdue
- [ ] `@cowork` **Client-tier vault scaffold**, after T0.7 is drafted; a separate vault, never inside Dbrain2
- [ ] `@cowork` design, `@code` build **C3** Work calendar and mail into the client-tier instance, only after G3 passes; otherwise after the demo

## Running track (unchanged by the pivot)
- [ ] `@cowork` **T3.1** Golden dataset v1, 150 rows: batches 05–06 and ~30 weekly assessments
- [ ] `@code` **T3.1** Race-times backtest from results; past readiness verdicts not labelled
- [ ] `@codex` **T3.1** Independent re-score of batch 04 — [[90 System/briefs/T3.1-batch04-rescore|T3.1 re-score]]
- [ ] `@cowork` **T3.1** Race exclusion in the `tempo_block` definition (D66)
- [ ] `@cowork` **T3.4** Session taxonomy v2, strict sequence — [[90 System/briefs/T3.4-taxonomy-v2|T3.4]]
- [ ] `@cowork` **T3.2** Adversarial rows (≥3) and coverage gaps
- [ ] `@code` **T3.3** Commit `golden-dataset.md`, versioned
- [ ] `@code` **P3.4** Regression-test and fix the reviewed running-script issues · **P3.6** freeze final running acceptance cases

## Carried over, to reassess after the W1 measurement
- [ ] `@code` **P2.5** Layers beyond F3 (F0–F3 done): rerun on rented models first; scope new layers only if they still fail — [[90 System/briefs/P2.5-answer-accuracy|P2.5]]
- [ ] `@code` **P2.6** Date library behind the fail-closed wrapper: keep only if the rented models still misread dates — [[90 System/briefs/P2.6-date-resolution|P2.6]]
- [ ] `@code` **P1.4** D59 frontmatter retrofit: brief and dry-run diff only; applying needs David
- [ ] `@code` **M5** Retrieval corpus with retention evidence; bilingual query expansion
- [ ] `@code` **T7** Evidence UX: the level badge and evidence states in Open WebUI (W2–W3)

## Parked or cut by the pivot (history in the archive)
- **Parked (D140):** T9b TwIL-LM3-Pro trial, for a possible offline laptop level; the model file stays; Q119 moot until it resumes.
- **Cut (D134, D135, D136):** the host order (D107); P2.3 "Air versus dedicated host" (replaced by PV1 step 5); P4.1 web app and P4.3 local voice (replaced by Open WebUI and rented speech); P5.1, P5.2 and T11 (replaced by the router, measured in W3 and W7); P2.4 follow-ups (retire with the Shortcut).
- **Parked as before:** T10 additional human users; S5 governance items in [[00 Inbox/2026-10-13-1115-multi-agents-governances-improvements|inbox]].

## Wiki and vault upkeep
- [ ] `@cowork` Triage `assistant-scope-ideas` and `how-to-automate-pm-job` at the next weekly pass, then lint
- [ ] `@david` Triage `00 Inbox/2026-10-01 New-project scaffold.md` later (Q12); fix its `source:` line then
- [ ] `@code` Remaining OQ-13 retention, ID and metadata details
- [ ] `@code` Automate lint once writes exist (W4); fixes stay approval-gated
- [ ] `@cowork` **Project-alignment**, parked; touches many notes, David approves the exact diff — [[90 System/briefs/project-alignment|brief]]
- [ ] `@david` Weekly-review task ID and first-run output into [[90 System/weekly-local-model-review]] (D60); the review should now also watch rented-model prices and terms

## Backlog / someday
- [ ] `@david` Second domain, after G1 (OQ-11)
- [ ] `@david` **Personal data wave 1** (D69, data-policy §4a): gated on P1.4 plus a lint check of the four axes on new notes
- [ ] `@code` **Personal data wave 2** (D69), local-only: gated as before; with no local host it now needs L0 or a new decision (D135)
- [ ] `@david` Migrate Apple Notes to markdown
- [ ] `@david` Retrieve the 4 Product School capstone tools from the LMS
- [ ] `@david` 🔴 **Product School / NN/g follow-ups (1 Oct):** revoke the bot token and redact the meeting passcodes in the Advanced Agents PDF (all copies); export and ingest the remaining notes and decks — full wording in the archive
- [ ] `@cowork` Script a short screen-recorded walkthrough of the router demo for LinkedIn (brand), after W3

## Conventions
`🔴` security-sensitive · `⭐` high-leverage · owner tags `@code` `@cowork` `@codex` `@david` (D63, default rule Q17, edge cases Q28). Tick items as you go, then move them to the archive at session close. An unrecorded task is a lost task.
