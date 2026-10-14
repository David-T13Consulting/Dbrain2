---
classification: internal
review_status: codex-reviewed
---
# Tasks — AI Second Brain Project

**Updated:** 12 Oct 2026 (session 46) · **Phase:** S1 closing, S2 under way (dated plan: [[10 Projects/AI Second Brain/06_Delivery_Plan_S2-S6|S2–S6]], proposed) · **Target:** demo-ready Fri 18 Dec 2026 (Q29)

Open items only, one line each; detail lives in the linked brief or in the roadmap ([[10 Projects/AI Second Brain/04_Roadmap|04_Roadmap]] §0). Done items, the legacy Week 0 / H1–H3 plan and the wording of every item before 8 Oct are in [[10 Projects/AI Second Brain/TASKS-archive|TASKS-archive]]. Owner tags per D63 and Q17; conventions at the end.

## ▶ Next action

- [ ] `@code` ⭐ **P2.8 · first in the next run (David, 14 Oct):** phone stops searching the system's own notes (A1, A2: regression from the 14 Oct climbing question) and shows a phone-readable answer (B1, B2) — [[90 System/briefs/P2.8-phone-corpus-and-answer-screen|P2.8]]
- [ ] `@cowork` Revise `90 System/skills/weekly-desktop-digest/SKILL.md` for the five Codex blockers (handoff, 9 Oct); the lead re-reviews
- [x] `@code` **T9 · S2 model comparison**, run 8 Oct 14:00–14:45 with David (session 39): the rule picks C2, Gemma 4 E4B; [[10 Projects/AI Second Brain/02_Architecture/t9-model-comparison-2026-10-08|results]] — [[90 System/briefs/T9-M6-model-comparison|T9/M6]]
- [ ] `@david` **After T9:** order the host by Fri 16 Oct: Mac mini M5 Pro 64 GB / 1 TB, Apple Belgium via the SRL (D107) · weekly-review task ID and first-run output into [[90 System/weekly-local-model-review]] (D60)
- [ ] `@david` **Six-week honesty check (rule 5), due ~19 Oct:** has anything shipped out of the system? If not, stop capturing. Cowork raises it at the session nearest 19 Oct; the answer goes in PROGRESS

## S1 · Align architecture
- [ ] `@code` **AS1** Agent setup hardening, this week (David, 13 Oct): one current rulebook, commit gates in both repos with protected-file gate (Q54 kept), startup check, trust-boundary line, D110 closure checklist; absorbs the secret-scanner-scope item; rest parked in [[00 Inbox/2026-10-13-1115-multi-agents-governances-improvements|inbox]] — [[90 System/briefs/AS1-agent-setup-hardening|AS1]] · **14 Oct (session 48):** steps 1–2 done (`235361f`, `8660c18`, D132); step 3 parked after 5/5 reviews (gates built, uncommitted, not installed); next run: D74 consult on step 3, then steps 4–5
- [ ] `@code` **P1.4** D59 frontmatter retrofit across the existing notes: brief and dry-run diff only; applying it needs David (hard limit; gates personal-data wave 1)

## S2 · Prove local read-only answers
- [ ] `@codex` **P2.1** Independent review of the retrieval cases; keep an untouched acceptance subset — [[90 System/briefs/P2.1-review|P2.1-review]]
- [ ] `@code` **P2.3** Measure quality, latency, memory and sustained performance with pinned versions; Air versus dedicated host
- [ ] `@code` **P2.4 follow-ups:** ~~intermittent endpoint-test hang~~ (fixed `3cbbd40`, D109; cause not proven, watchdog in place); `mvp/README.md` date-coverage wording (in P2.6) — [[90 System/briefs/MVP-phone|MVP-phone]]
- [ ] `@code` **P2.5** Answer accuracy, layered and measured on a fixed test set; slice F0–F3 (D120): **F0 committed 12 Oct** (runtime `d584f13`, Q97 (a); whole-answer scorer; baseline row 0/6, none 2/2, negated 3/3, other 2/2); **F1 closed 12 Oct, no prompt change** (Q99); **F2 narrowed 13 Oct** (David: fire only on a bare "nothing on <date>" against a clean cited row, keep the answer, add the row) and **parked again** after 2/2 reviews (D127); uncommitted in worktree `~/Work/dbrain-runtime-f2`; Q103: new cancellation markers are should-fixes; next run: D74 consult, one review, commit; then F3 — [[90 System/briefs/P2.5-answer-accuracy|P2.5]]
- [ ] `@code` **P2.6** Date library behind the fail-closed wrapper; phrase set validated by David 9 Oct (S5 "next Monday" said on a Monday → `UNCLEAR`; today's reader answers a date there); waits for Cowork to name it as the first item of a run; a new dependency needs David's OK — [[90 System/briefs/P2.6-date-resolution|P2.6]], [[90 System/briefs/P2.6-phrase-set|phrase set]]
- [ ] `@code` **G1-inj** ([[90 System/briefs/G1-inj-read-path-injection|brief]], drafted 12 Oct; S1 next) Read-path injection suite (instructions in notes, fabricated authority, exfiltration requests, cross-domain retrieval), part of the S2 exit and gate G1 (D126); its brief sizes it; if it threatens the 23 Oct exit, the lead asks David (for-david) whether to move it to S3, and until he answers it stays part of the S2 exit — [[10 Projects/AI Second Brain/04_Roadmap|roadmap]] §0 amendment
- [ ] `@cowork` design, `@code` build **P2.7** Failure capture and regression loop; go 8 Oct (16:08); files in scope reviewed; stage L (leak check) committed `d62fdf7`; D108 deny rules applied; exception on the Air accepted (D110); Codex requirements file installed and re-test passed (8 Oct); stage C steps C1–C3b committed 9 Oct (session 42); **C4: real capture on since 9 Oct 11:41** (D119, runtime `72bf52b`, planted failure proven end to end and deleted through the store); **C5 (one-tap "wrong"): service done 9 Oct** (runtime `b3e1f1a`; 1-hour in-memory hold, D123); **phone part done 13 Oct** (session 47, with David: Shortcut "Ask Brain 5", Wrong recorded end to end); next: Cowork's follow-up brief (stage 2, stage 3, digest gating) — [[90 System/briefs/P2.7-failure-capture-loop|P2.7]]

## S3 · Supervised wiki maintenance
- [ ] `@code` **S3 exit (G2), re-anchored (D126):** from the phone, an approved benign fact survives restart, is recalled with its source in a fresh session and is corrected without the old version resurfacing; rejection, a concurrent Obsidian edit and an interrupted save included; voice approval names the exact pending proposal — [[10 Projects/AI Second Brain/04_Roadmap|roadmap]] §0 amendment
- [ ] `@code` **P3.0** Update my brain by voice or text, with approval — [[90 System/briefs/P3.0-update-my-brain|P3.0]]
- [ ] `@code` **P3.1** Durable source IDs, evidence, derived claims, contradictions and review state
- [ ] `@code` **P3.2** Pending patches with evidence, exact diff, base revision and approval binding
- [ ] `@code` **P3.3** One deterministic writer after T4.2, with path, schema and approval checks; test malicious source instructions, path escape and unauthorised writes
- [ ] `@code` **P3.4** Regression-test and fix the reviewed running-script issues
- [ ] `@cowork` **P3.5** Subsumed by T3.4 (Q14); kept for history
- [ ] `@code` **P3.6** Freeze final running acceptance cases; preserve historical scores

## W · Usable security (data policy v1.0, gate G3)
- [ ] `@cowork` **W1** Draft data policy v1.0 from the amendment's starting principles (tier by source, contract gate, query live and persist little, read-only least-scope revocable connectors, client tier local by default, no agent access to client-tier data or tokens, content as evidence, text-free audit, incident procedure; legal points `unverified` until T0.7) by Fri 16 Oct; David approves (§8) — [[10 Projects/AI Second Brain/04_Roadmap|roadmap]] §0 amendment, D126

## C · Context connectors (gate G4; each connector its own brief, scopes, injection cases and revoke test)
- [ ] `@cowork` **C0** Connector-technology brief with options (MCP servers vs direct read-only APIs: Google Calendar and Gmail, Apple Calendar through EventKit), before W7
- [ ] `@code` **R1 before C1:** the phone service takes its profile, allowlist and per-vault policy from configuration (the vault root already does, `DBRAIN_VAULT`), not the built-in `mvp-whole-vault` profile (client-tier R1; D126)
- [ ] `@cowork` design, `@code` build **C1** Personal calendar, read-only, W7 (16–20 Nov)
- [ ] `@cowork` design, `@code` build **C2** Personal mail, read-only, W8
- [ ] `@cowork` design, `@code` build **C3** Work calendar and mail into the client-tier instance, W9–W10, **only after G3 passes**; cut 0 (after the demo if G3 has not passed by Fri 13 Nov) is a proposal, not decided

## S4 · Remote text and voice
- [ ] `@code` **P4.1** Private authenticated access and mobile text UI; keep the inference endpoint private — [[90 System/briefs/P4.1-web-app|P4.1]]
- [ ] `@code` **P4.2** Durable capture queue with retries and cancellation
- [ ] `@code` **P4.3** Local push-to-talk transcription and speech output; define audio retention and deletion before recording; recording pipeline pull-forward decided after T9/M6, no build before it
- [ ] `@code` **P4.4** Away-from-home test on each device class; replace Dispatch and update CAPTURE only after the new route passes

## S5 · Measurable multi-agent execution
- [ ] `@code` **P5.1** Compare against the single-agent baseline
- [ ] `@code` **P5.2** Persistent jobs, bounded budgets, cancellation, traceable handoffs

## S6 · Operate and demonstrate
- [ ] `@code` **P6.1** Independent backup and restore
- [ ] `@code` **P6.2** Pinned releases, reproducible setup, upgrade and rollback; run regressions before upgrades
- [ ] `@code` **P6.3** Monitoring, redaction, access denial and retention checks
- [ ] `@code` **P6.4** Public-safe demo repository package (needs its own authorisation)
- [ ] `@code` **Ops (amendment point 5, D126):** retention set for backups and audit logs, not only failure records · release decision bound to exact code, model, prompt and corpus versions (with P6.2) · incident procedure: stop exposure, revoke, preserve permitted evidence, assess, repair, verify (with T8) · runtime README reconciled with today's model and repository state
- [ ] `@code` 🔴 **Trace question hashes:** traces keep an unsalted SHA-256 of the question, which a dictionary of likely questions can reverse; salt per install (key kept outside agent reach) or drop the hash; filenames in traces treated as personal data (D126)
- [ ] `@code` 🔴 **Secret scanner scope:** it is run on the runtime repo only (its target is the current folder); extend it to the vault and the handoff files, or record why not (D126)
- [ ] `@code` **P2.7 retention after downtime:** the purge runs at service start and every 6 h only while the service runs; add a test that a record past 90 days is purged at the first start after downtime, and record the residual (records outlive 90 days while the service is down) in the P2.7 follow-up (D126)

## Roadmap T-tasks (scheduled by stage)
- [ ] `@cowork` draft, `@david` + lawyer **T0.7** Tower13 subcontract AI-use clause and processing annex, signed before 2 Nov; week of 12 Oct
- [ ] `@cowork` **T3.1** Golden dataset v1, 150 rows: batches 05–06 and ~30 weekly assessments
- [ ] `@code` **T3.1** Race-times backtest from results; past readiness verdicts **not** labelled (hindsight bias)
- [ ] `@codex` **T3.1** Independent re-score of batch 04 — [[90 System/briefs/T3.1-batch04-rescore|T3.1 re-score]]
- [ ] `@cowork` **T3.1** After batch 04 is scored: race exclusion in the `tempo_block` definition (D66)
- [ ] `@cowork` **T3.4** Session taxonomy v2; strict sequence: score v1.4 on batch 04 first, then David approves the v2.0 wording, then rewrite and re-derive — [[90 System/briefs/T3.4-taxonomy-v2|T3.4]]
- [ ] `@cowork` **T3.2** Adversarial rows (≥3) and coverage gaps
- [ ] `@code` **T3.3** Commit `golden-dataset.md`, versioned
- [ ] `@code` **T4.1** Versioned evaluations, deterministic checks first, model judges with human spot checks (S2)
- [ ] `@code` **T4.2** Rollback and independent restore test on a disposable copy, before S3 writes
- [ ] `@code` **T4.3** Scoped deterministic writer after T4.2; no blanket autonomous writes
- [ ] `@code` **T5** Eval dashboard (S2 start, S6 complete)
- [ ] `@code` **T6** Reliability contract: targets before acceptance runs, verified at S6
- [ ] `@code` **T7** Evidence UX at S3; existing skill confidence scores are heuristic, so preserve escalation until reviewed
- [ ] `@cowork` **T8** Governance one-pager (Q28)
- [ ] `@code` **T10** Additional human users, parked after S6; resolve OQ-3 first
- [ ] `@code` **T11** Coordinator, curator and evidence checker with scoped tools and explicit autonomy limits; compare with the single-agent baseline (S5)
- [ ] `@code` **T12** Permissions and redaction from S2; source-injection and write tests before S3; remote-access checks before S4 exposure; full security audit at S6
- [ ] `@code` **T13** Two demo rehearsals (S6), permitted running data and synthetic fixtures only

## Local model knowledge
- [ ] `@code` **M5** Retrieval corpus with D49 retention evidence; bilingual query expansion; expected evidence reviewed independently; keep original failures and untouched provisional cases
- [x] `@code` **M6** Another model family under comparable conditions (with T9): Gemma 4 E4B and Ministral 3 8B measured 8 Oct; set separate voice fixtures and resource budgets before downloading any other modality model — [[90 System/briefs/T9-M6-model-comparison|T9/M6]]
- [ ] `@code` **M6b** EmbeddingGemma 2 vs Qwen3-Embedding-0.6B vs lexical baseline; S1 and S2 done 9 Oct (session 44: Python 3.12 venv, D122; both models fetched and verified); **S3 done 9 Oct** (runtime `98694a2`: harness, toy tests; labels D124); **S4 run 12 Oct** (Pillow per Q96, torchvision per D127 (4); no measured benefit: lexical 5/7, EmbeddingGemma 2 4/7, Qwen3 3/7), **committed 13 Oct** (runtime `0736b29`, after Q101 (a) / D130); S5 next (results note, Tier 2); never alongside a measurement run (D94, D100) — [[90 System/briefs/M6b-embedding-eval|M6b]]

## Wiki and vault upkeep
- [ ] `@cowork` Triage `assistant-scope-ideas` and `how-to-automate-pm-job` at the next weekly pass, then lint
- [ ] `@david` Triage `00 Inbox/2026-10-01 New-project scaffold.md` later (Q12: no brief and no guardrail work from it for now); fix its `source:` line then
- [ ] `@code` Remaining OQ-13 retention, ID and metadata details at P1.3/P3.1
- [ ] `@code` Automate lint at S3; fixes stay approval-gated
- [ ] `@cowork` **Project-alignment**, parked until P2.5 shows progress; touches many notes, so David approves the exact diff (hard limit) — [[90 System/briefs/project-alignment|brief]]
- [ ] `@cowork` **Client-tier vault scaffold**, week of 12 Oct, after T0.7 is drafted; needs David's folder grant; a separate vault, never inside Dbrain2; no build work in Dbrain2 or the runtime from this task — [[10 Projects/AI Second Brain/02_Architecture/client-tier-workspace-requirements|requirements]]

## Backlog / someday
- [ ] `@david` Second domain, after the H1 gate (OQ-11)
- [ ] `@david` **Personal data wave 1** (D69, data-policy §4a): gated on P1.4 plus a lint check of the four axes on new notes; no family-logistics build before the H1 gate
- [ ] `@code` **Personal data wave 2** (D69, data-policy §4a), local-only: gated on (a) P2.2/P2.3 local answers with no cloud fallback, (b) T12 access test proving cloud agents cannot reach the files, (c) T12 synthetic leak test, (d) trace redaction live, (e) deletion rule tested on working copy, git history and backups
- [ ] `@david` Migrate Apple Notes to markdown
- [ ] `@david` Retrieve the 4 Product School capstone tools from the LMS
- [ ] `@code` Infrastructure beyond the single host, only on measured need
- [ ] `@david` 🔴 **Product School / NN/g follow-ups (1 Oct):** revoke the bot token and redact the meeting passcodes in the Advanced Agents PDF (all copies); export and ingest the three Apple Notes and the remaining NN/g decks; review and promote the draft notes; the lead commits the handoff entry

## Conventions
`🔴` security-sensitive · `⭐` high-leverage · owner tags `@code` `@cowork` `@codex` `@david` (D63, default rule Q17, edge cases Q28). Tick items as you go, then move them to the archive at session close. An unrecorded task is a lost task.
