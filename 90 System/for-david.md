---
classification: internal
note_type: queue
source: cowork
review_status: approved
created: 2026-10-02
updated: 2026-10-05
---
# For David: the single decision queue

David chose a single front door on 2 Oct 2026 (option A, provisional **D-cowork-6**). **Only Cowork asks David.** Claude Code and Codex never ask him directly. They add an entry below, set the brief to `blocked-on-david`, and carry on with other work. Cowork opens every session by walking David through the open entries, writes each answer into the entry and the brief, and the lead turns answers into decisions/commits.

**Entry format:** `ID · from · brief · question · options (recommended first) · what it blocks · urgency (today / this week / whenever)`. Answered entries move to *Answered* with the date and answer; the lead clears them once they are recorded in PROGRESS/briefs.

## Open

| ID | From | Brief | Question | Options | Blocks | Urgency |
|---|---|---|---|---|---|---|
_(none open)_

## Answered
Cleared once recorded, per D68. **Q5 and Q6 were cleared on 2 Oct** — Q5 is recorded in [[90 System/briefs/P2.1-review\|P2.1-review]] (Codex may read the 6 reserved cases, read-only) and Q6 in [[90 System/briefs/D68-single-front-door\|D68]], which it closed.

| ID | Date | Answer |
|---|---|---|
| Q35 | 5 Oct | **MVP startup → (c): Terminal login item now** (`mvp/Ask Brain.command`: restarts the model or service if either stops, keeps the Air awake on power; one Terminal window stays open). **No launchd + Full Disk Access for the system Python.** Later, with the Mac mini: a dedicated signed helper with Documents access only (David, via Cowork) |
| Q26 | 5 Oct | **Wave task owners (D69 apply review, blocker 1):** wave 1 → `@david` (capture, gated on P1.4), wave 2 → `@code` (gates are build/test work), as the lead proposed (David, via Cowork) |
| Q25 | 5 Oct | **Revised data-policy v0.4 text (Q24 fixes 1–3) approved.** Lead: apply to `data-policy.md` as v0.4 (D69), with PROGRESS/TASKS/OPEN_QUESTIONS/index bookkeeping. David will approve Claude Code's edit of `data-policy.md` when its permission check asks (David, via Cowork) |
| Q24 | 5 Oct | **Data-policy v0.4 → fix all three Codex points before applying.** Cowork revised `D-cowork-7` the same day: (1) waves govern material added from 5 Oct; existing ordinary personal material is relabelled in P1.4, with anything now wave 2 flagged to David; (2) gate (e) = deletion rule tested across working copy, git history **and backups**; a purgeable repo covers git only; (3) minimise **before** capture, no town or neighbourhood, non-compliant captures deleted at triage. Approval of the revised text is Q25 (David, via Cowork) |
| Q23 | 5 Oct | **P2.2 raw measurement data location.** David asked why it would sit outside the vault at all and set the principle: **as lean as possible while keeping proper security boundaries.** Cowork's explanation: raw traces and reports stay out of the vault because (i) the vault is the corpus, so measurements inside it get measured (the run A bug), (ii) every cloud agent reads the vault, and traces contain corpus excerpts and prompts, (iii) bulky files stay out of the vault (project rule). Applying David's leanness principle: **(b) move raw data into a git-ignored folder inside `dbrain-runtime/`**, one location fewer than `Dbrain2-artifacts/`; the dated summary note stays in `02_Architecture/` (Q7). **Confirmed by David** (David, via Cowork) |
| Q21 | 5 Oct | **P2.2 support label → (a) keep strict until T4.1:** no answer is marked `supported` without the automatic fact-check; every answer still shows its citations and why it isn't supported. Word overlap alone never upgrades an answer (David, via Cowork) |
| Q22 | 5 Oct | **T2.6 → Dinant chip time 1:39:06** (David first typed 1:38:06 and corrected it immediately; 1:39:06 is right). Cowork wrote it into `readiness-calls.md`: in range (1:38:54–1:45:01), 12 s inside the fast edge, 2:51 faster than mid. T2.6 can be ticked (David, via Cowork) |
| Q20 | 5 Oct | **Data-policy v0.4 text in `D-cowork-7-personal-data-waves` approved as written** (waves + children's §3a). Lead: apply to data-policy.md as v0.4, give it a final D-number, and record it in PROGRESS (David, via Cowork) |
| Q18 | 5 Oct | **Personal data enters in gated waves, as proposed:** wave 0 (own training/HR, in force) · wave 1 ordinary personal after the P1.4 four-axis retrofit · wave 2 sensitive/local-only only after five gates (local answers without cloud fallback, cloud agents can't reach the files, synthetic leak test, trace redaction, git/backup deletion rule) · never: others' sensitive data, client, secrets. Cowork drafted data-policy v0.4 as brief `D-cowork-7-personal-data-waves` for David to approve (David, via Cowork) |
| Q19 | 5 Oct | **First wave-1 use case: kids' schedules without names** (school lunches, climbing practice and similar). Proposed children's rule in `D-cowork-7` (no names/initials, no school or club names, no health/behaviour/photos, never demoed, manual capture only), pending David's approval. OQ-11 second domain stays parked as a feature (David, via Cowork) |
| Q9 | 5 Oct | **D53 host purchase deferred; the MacBook Air is the inference host until David buys the always-on host.** Build and measure P2.2 on the Air; sustained-performance and always-on numbers wait for the host. Anything scheduled locally (e.g. the weekly model review) runs only when the Air is awake with the app open (David, via Cowork) |
| Q10 | 5 Oct | **OQ-20 → split `classification` into four axes before the P1.4 retrofit:** domain (personal/professional) · sensitivity (ordinary/sensitive) · processing permission (local-only/approved external) · sharing permission (private/approved for demo). Labels only; **no vault split now**. Retrofit once against this shape, defaults derived mechanically from the current label and folder, David reviews edge cases (health, family). Labels inform controls and never grant access by themselves; any widening of what may enter the vault still needs a deliberate `data-policy` edit. Unblocks P1.4 (David, via Cowork) |
| Q11 | 5 Oct | Weekly local-model review → **record the task ID and first-run output together after the 8 Oct run**, not before. Air must be awake with the app open Thu 09:00 (David, via Cowork) |
| Q12 | 5 Oct | `00 Inbox/2026-10-01 New-project scaffold.md` → **park untouched**: stays in the Inbox, unprocessed. Lead gives it an owner tag (`@david`, triage later) so it stops being flagged as unowned. No brief, no guardrail work from it for now (David, via Cowork) |
| Q8 | 2 Oct | *(The lead raised this as Q7, but Q7 was already taken by the results-location answer, so Cowork renumbered it.)* **(b) Yes, re-fetch now, and set the M6 standing budget:** agents may use **up to 20 GB** of disk for local model weights and runtimes, **stored outside the vault, hash-pinned, and only for models named in a brief.** Re-fetching llama.cpp + Qwen3-4B Q4_K_M (~2.5 GB, hash-verified against the 1 Oct record) is within it. Downloads beyond 20 GB, or of models no brief names, still come back to David (David, via Cowork) |
| Q7 | 2 Oct | P2.2 results location → **a dated vault note in `02_Architecture/`, `review_status: draft`**, confirmed by David later; raw data stays in `dbrain-runtime`. Resolves P2.2 review finding 7 (David, via Cowork, during the plan lint) |
| Q1–Q4 | 2 Oct | **Corrected by the lead.** The four David actually answered directly to Claude Code, before this queue went live, were: reviewer invocation (install the standalone CLI), reviewer effort (`high` stays standard), the runtime repository (`~/Documents/dbrain-runtime/` authorised) and the batch-04 scoring owner. Recorded in PROGRESS and the D64 / P2.2 briefs. **Codex reading the reserved cases was *not* among them** — it went through this queue as **Q5** instead, and David answered it on 2 Oct (yes, read-only). Historical note: while Q5 was open the lead could only state that *it* had not asked the question |
| Q0 | 2 Oct | Who scores batch 04 → `@cowork`. Done and validated by David the same day |
| Q0b | 2 Oct | Independent Codex re-score of batch 04 → yes (David told Codex directly, before this queue existed) |
