---
classification: internal
review_status: approved
---
# Tasks — AI Second Brain Project

**Updated:** 22 Oct 2026 (session 59: PL1 step 7 done append-only, D143 review rule in AGENTS.md) · **Plan:** [[10 Projects/AI Second Brain/04_Roadmap|04_Roadmap]] §4, stages 1–3 · **Target:** demo-ready Fri 18 Dec 2026 (Q29)

Open items only, one line each; detail lives in the linked brief or the roadmap. The pre-pivot list, with every item's full wording and history, is archived at [[40 Archive/AI Second Brain/TASKS-pre-pivot-2026-10-19]] (exact text in git `e7b558e`); older done items are in [[10 Projects/AI Second Brain/TASKS-archive|TASKS-archive]]. Owner tags per D63 and Q17; conventions at the end.

## ▶ Stage 1 · Second brain on the Mac (20 Oct–1 Nov, hard stop) — [[90 System/briefs/PL1-mac-second-brain|PL1]]

- **Focus until 1 Nov (D143):** only PL1 steps 7–8 and the one-Shortcut "Brain" item. Frozen to stage 3: P1.4 step 1, AS1 step 4, M-inj
- [ ] `@david` ⭐ **PL1 step 8:** G2 check by voice from the phone (remember, recall, Correct, recall), plus the P2.8 phone check. Step 7 done 22 Oct (append-only, runtime `0fbf8f6`, Q172)
- [ ] `@code` **One Shortcut "Brain"** (Q163, David 22 Oct: option B): one input step for voice or typing, fixed first-word routing to the remember flow (gate unchanged), "Brain Key" separate; after step 8's G2 check; triggers "note" and "save" (Q164), typed answers shown only, Siri runs spoken (Q165); re-run the phone check
- [ ] `@code` **P2.7** retention-after-downtime test (D126), while on the Mac
- [ ] `@cowork` Revise `90 System/skills/weekly-desktop-digest/SKILL.md` for the five Codex blockers (handoff, 9 Oct); the lead re-reviews

## Stage 2 · Second brain with Claude Code (2–8 Nov)
- [ ] `@cowork` Draft the **PL2** brief: Claude Code vault skills adapted from an LLM-wiki skill (ingest, query, lint), git-diff approval, use from the phone through the Claude app, same evaluation set as stage 1
- [ ] `@code` **PL2** build; one raw capture ingested into connected notes with David's approval
- [ ] `@code` **T4.1** Versioned evaluations: the same question set scored at L0 (stage 1) and L3 (stage 2), deterministic checks first; then a calibrated certainty percentage for answers, spoken and shown, only once these evaluations can back it (David, Q149)
- [ ] `@codex` **P2.1** Independent review of the retrieval cases; keep an untouched acceptance subset — [[90 System/briefs/P2.1-review|P2.1-review]]

## Stage 3 · Hosted, EU (9 Nov–6 Dec)
- [ ] `@david` **PV1 step 3:** Scaleway account, budget alert, API key in the Keychain (service `dbrain-scaleway`, account `dbrain`; Q134); cap alert €50 (Q135)
- [ ] `@code` **PV1 steps 5–7:** measure Mistral Small 3.2, Gemma 4 26B-A4B, Qwen3.8-27B, Qwen3-235B against the baseline; switchboard core (ceiling rules, decision log, badge) — [[90 System/briefs/PV1-rented-models-and-switchboard|PV1]]
- [ ] `@cowork` Draft the **PV2** brief: EU server (Hetzner Cloud DE vs Scaleway FR), read-only vault sync, Open WebUI + Open Relay, voice, cutover from the Shortcut
- [ ] `@code` **PV2** build (D136; replaces P4.1, P4.3); "Wrong" moves to Open WebUI feedback (P2.7)
- [ ] `@code` Router across L0 Mac, L1 Scaleway, L3 Claude: task classifier, routing table from eval scores, escalate once, soft budget alert (D138)
- [ ] `@david` Claude API key into the Keychain for the L3 route
- [ ] `@code` **G1-inj** Read-path injection suite: S1–S3 done 22 Oct (Q166); baseline on the phone's model: **I and A fail**, X and D clean, A2 inconclusive; G1's injection item unmet until M-inj — [[90 System/briefs/G1-inj-read-path-injection|G1-inj]]
- [ ] `@david` **M-inj** approve the mitigation brief (Q167; output check first, then evidence framing) and say whether its measurement may rerun on the live server — [[90 System/briefs/M-inj-answer-injection-mitigation|M-inj]] · **Frozen until stage 3 (D143)**
- [ ] `@code` 🔴 **Trace question hashes:** salt per install or drop; filenames in traces are personal data (D126); before traces live on the server
- [ ] `@code` **AS1 step 4** startup check (narrowed Q155 (a), OS-enforced Q160; rebuilt on in-process `sandbox_init`, Q168, Q170; parked a third time 22 Oct, session 58, on who can call the checks unconfined; fix unreviewed; next: D74 consult, fresh review); **step 5** rescoped: close the D110 Air exception when the service moves to the server — [[90 System/briefs/AS1-agent-setup-hardening|AS1]] · **Frozen until stage 3 (D143)**
- [ ] `@code` **R1** Profile, allowlist and per-vault policy from configuration, before C1 (D126)
- [ ] `@cowork` **C0** connector brief; `@cowork` design, `@code` build **C1** personal calendar, read-only (cut first if late)
- [ ] `@code` **P4.4** Away-from-home test on each device class
- [ ] `@code` **Agent topology (option A, David 21 Oct):** router ceiling rule processing=local-only → L0 for health beyond training, finances and transatlantic-move material; C1 reader quarantined (no tools, structured output); data-policy edit per Q-cowork-21a/21b answers (protected; approved by David 21 Oct) — [[10 Projects/AI Second Brain/02_Architecture/agent-topology-proposal-2026-10-21|proposal]]

## Operate and demo (7–13 Dec; demo Fri 18 Dec)
- [ ] `@code` **T5** Eval dashboard · **T6** reliability contract · **P6.1** backup and restore drill · **P6.3** monitoring, redaction, retention checks
- [ ] `@code` **Ops (D126):** retention for backups and audit logs; release bound to exact code, model, prompt and corpus versions; incident procedure
- [ ] `@cowork` **T8** Governance one-pager (Q28)
- [ ] `@code` **P6.2** Pinned releases and rollback · **P6.4** demo package (needs its own authorisation) · **T13** two rehearsals with a controlled failure, synthetic fictional-client scenario
- [ ] `@code` **T12** Security checks: write tests before stage 1 writes, remote-access checks before the stage 3 server is exposed, full audit before the demo
- [ ] `@code` **C2** personal mail, read-only, after the demo unless time remains; **P4.2** offline capture queue (D54), after the demo

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

## Carried over, to reassess after the stage 1 and stage 3 measurements
- [ ] `@code` **P2.5** Layers beyond F3 (F0–F3 done): rerun on the stage 1 model and the rented models first; scope new layers only if they still fail — [[90 System/briefs/P2.5-answer-accuracy|P2.5]]
- [ ] `@code` **P2.6** Date library behind the fail-closed wrapper: keep only if the rented models still misread dates — [[90 System/briefs/P2.6-date-resolution|P2.6]]
- [ ] `@code` **P1.4** four-axis retrofit (Q153 b, started 22 Oct): brief committed; step 1 dry run (Tier 2) parked again 22 Oct (session 58) after reviews 1/2 and 2/2 (labels admitted that YAML would not read; fixes uncommitted); next: D74 consult on a positive admission rule, fresh review; step 2 report to David after; applying needs David — [[90 System/briefs/P1.4-four-axis-retrofit|P1.4]] · **Frozen until stage 3 (D143)**
- [ ] `@code` **M5** Retrieval corpus with retention evidence; bilingual query expansion
- [ ] `@code` **T7** Evidence UX: the level badge and evidence states, phone screen in stage 1, Open WebUI in stage 3

## Parked or cut by the pivot (history in the archive)
- **Resumed (D141):** T9b step 4 runs in stage 1 to pick the Mac model (Q119 approved 21 Oct).
- **Cut (D134, D135, D136):** the host order (D107); P2.3 "Air versus dedicated host" (replaced by PV1 step 5); P4.1 web app and P4.3 server voice (stage 1 uses on-device iPhone speech; stage 3 Open WebUI); P5.1, P5.2 and T11 (replaced by the router, measured in W3 and W7); P2.4 follow-ups (retire with the Shortcut).
- **Parked as before:** T10 additional human users; S5 governance items in [[00 Inbox/2026-10-13-1115-multi-agents-governances-improvements|inbox]].

## Wiki and vault upkeep
- [ ] `@cowork` Triage `assistant-scope-ideas` and `how-to-automate-pm-job` at the next weekly pass, then lint
- [ ] `@david` Triage `00 Inbox/2026-10-01 New-project scaffold.md` later (Q12); fix its `source:` line then
- [ ] `@code` Remaining OQ-13 retention, ID and metadata details
- [ ] `@code` Automate lint once writes exist (stage 1); fixes stay approval-gated
- [ ] `@cowork` **Project-alignment**, parked; touches many notes, David approves the exact diff — [[90 System/briefs/project-alignment|brief]]
- [ ] `@david` Weekly-review task ID and first-run output into [[90 System/weekly-local-model-review]] (D60); the review should now also watch rented-model prices and terms

## Backlog / someday
- [ ] `@david` Second domain, after G1 (OQ-11)
- [ ] `@david` **Personal data wave 1** (D69, data-policy §4a): gated on P1.4 plus a lint check of the four axes on new notes
- [ ] `@code` **Personal data wave 2** (D69), local-only: gated as before; with no local host it now needs L0 or a new decision (D135)
- [ ] `@david` Migrate Apple Notes to markdown
- [ ] `@david` Retrieve the 4 Product School capstone tools from the LMS
- [ ] `@david` 🔴 **Product School / NN/g follow-ups (1 Oct):** revoke the bot token and redact the meeting passcodes in the Advanced Agents PDF (all copies); export and ingest the remaining notes and decks — full wording in the archive
- [ ] `@cowork` Script a short screen-recorded walkthrough of the router demo for LinkedIn (brand), after stage 3

## Conventions
`🔴` security-sensitive · `⭐` high-leverage · owner tags `@code` `@cowork` `@codex` `@david` (D63, default rule Q17, edge cases Q28). Tick items as you go, then move them to the archive at session close. An unrecorded task is a lost task.
