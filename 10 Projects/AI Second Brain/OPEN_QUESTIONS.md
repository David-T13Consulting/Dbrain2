---
classification: internal
review_status: codex-reviewed
---
# Open Questions

**Updated:** 7 Oct 2026 (session 30): no change here; questions for David are in [[90 System/for-david|for-david]] (open: Q30, Q69) · Open questions block work. Resolve them or explicitly park them.

---

## 🔴 Blocking

**All five blockers raised in session 14 are answered.** The last of them, item 4, came through the queue as Q5 on 2 Oct; the other four David answered directly to the lead before the queue went live. Requirements and targets are closed (D52–D59), and the always-on host purchase (D53) still gates sustained-performance *numbers* rather than the build.

Under **D68** (single front door) questions for David no longer live here: they go to [[90 System/for-david|for-david]], and the lead records the answers in PROGRESS and the briefs.

| # | Question | Answer | Where it is recorded |
|---|---|---|---|
| 1 | Reviewer effort — `high` or the highest available? | `high` stays standard, `ultra` only when lead and reviewer are both stuck. `AGENTS.md` wording corrected | D64, closed |
| 2 | How should the lead invoke the reviewer? | Install the standalone Codex CLI. Done: `~/.local/bin/codex`, 0.160.0, and `codex exec --profile review` now works as documented | D64, closed |
| 3 | Authorise the runtime repository for application code? | Yes — `~/Documents/dbrain-runtime/`, new, local, not pushed | [[90 System/briefs/P2.2\|P2.2 brief]] |
| 4 | May Codex *read* the 6 reserved retrieval cases to check their labels? | **Yes, read-only** — no model is run on them. Answered via queue entry Q5, 2 Oct | [[90 System/briefs/P2.1-review\|P2.1-review]], now `open` |
| 5 | Who scores batch 04? | `@cowork`. Already done and validated by David the same day — terrain 100% · intent 65% · `tempo_block` 40% · vertical 90% | T3.1, PROGRESS |

**Numbering, stated once so it stops drifting.** Items 1–5 keep the order in which the lead originally **listed** them as blockers — which is the order D68's "Done when" 4 assumes — not the order anyone asked them. The lead put items 1, 2, 3 and 5 to David directly; **item 4 it did not ask** — it went through the queue as Q5 instead, under D68, and David answered it there. So **item 5 (the scoring owner) is the answered one**, exactly as that brief predicted, and **item 4 (the reserved cases) was the last to be settled** — answered 2 Oct as queue entry **Q5**, numbered that way because the queue numbers entries in the order they were written. A sixth question, **Q6**, was opened later by D68 itself and has no item number here, since it blocks nothing in this file.

## 🟡 Needed soon

### OQ-18 · Activate weekly model review — ✅ RESOLVED 1 Oct 2026
David activated the weekly review in the desktop local-project scheduler (D60). M4 closed. **Two threads remain open but block nothing:** the task ID and first-run output still need pasting into [[90 System/weekly-local-model-review]]'s activation record, and the first two runs should be reviewed before the cadence is relied on. The download/storage budget for M6 is still unset — weekly research may update published results and propose bounded tests, but not silently upgrade models or pull weights.

### OQ-17 · SAFe knowledge base currency — ⛔ CLOSED 1 Oct 2026, not resolved (D61)
David's call: the 5.1-era content is too old to be worth re-verifying, so the check will not be done. **The question is closed, not answered — so the constraint it was protecting against now stands permanently:** the SAFe pages are historical reference only and **must not be used client-facing**. Nobody has verified them against AI-Native SAFe (June 2026) or the 2024+ Disciplines. If a client engagement ever needs current SAFe material, re-obtaining the assets (membership / SPC) is a prerequisite, not an option. See `30 Resources/SAFe/sources.md`.

### OQ-19 · Product School and NN/g notes: review, credentials, remaining sources
Notes are `public`/draft and in David's own-words synthesis; course figures are instructor heuristics. Needs: credential redaction in the Advanced Agents PDF (🔴), export of three unreadable Apple Notes, decision whether to ingest remaining NN/g decks. Opened 1 Oct.

### OQ-20 · Should `classification` split into separate axes before the schema is retrofitted? — ✅ RESOLVED 5 Oct 2026
**Answer (David, queue Q10):** yes, four axes before the P1.4 retrofit: domain (personal/professional) · sensitivity (ordinary/sensitive) · processing permission (local-only/approved external) · sharing permission (private/approved for demo). **Labels only, no vault split now.** Retrofit once against this shape, defaults derived mechanically from the current label and folder, David reviews edge cases (health, family). Labels inform controls and never grant access by themselves. Unblocks P1.4. Data-policy v0.4 (D69) uses these axes and revisits the split at wave 2.
*Original question, kept:* **Blocks:** P1.4 only (the D59 frontmatter retrofit across 114 notes) · **Owner:** David.
The `pro-private-split` capture of 1 Oct argues the single `classification` axis is too coarse: `internal` currently covers both business material *and* David's health data, and permits both cloud processing and demos of his own data. It proposes four independent dimensions — **domain** (personal/professional) · **sensitivity** (ordinary/sensitive) · **processing permission** (local-only/approved external) · **sharing permission** (private/approved for demo) — plus access enforced in the application rather than by labels.
D59 deliberately kept the minimum schema narrow. If the split is likely to be accepted, design the schema once against the final shape and retrofit after; if not, P1.4 can proceed as specified. Either way the capture's **access-matrix proposal is a genuine S1 design item** that P1.3 did not cover, and the capture itself authorises no policy change: expanding what may enter the vault needs a deliberate edit to [[10 Projects/AI Second Brain/02_Architecture/data-policy|data-policy]]. Source: `00 Inbox/2026-10-01-1441-pro-private-split.md`, untriaged.

### OQ-3 · Colleague for a future two-person test (parked)
**Affects:** T10 after S6 · **Owner:** David. Additional human users no longer precede multi-agent work. Revisit when the personal service is reliable; no simulated multi-user claim in the initial demo.

### OQ-4 · Current Mac hardware and capacity
**Resolved 1 Oct by read-only measurement:** M2, 24 GiB RAM, 8 CPU cores; about 90 GiB free before download. Initial local benchmark ran successfully but exposed answer-quality failures. See [[10 Projects/AI Second Brain/02_Architecture/local-benchmark-2026-10-01|measurement record]]. Model selection, availability and sustained performance remain open; no purchase proposed.

### OQ-14 · Devices, access and host availability — ✅ RESOLVED 1 Oct 2026
**D52:** iPhone, iPad and the MacBook Air are committed clients; Apple Watch and the Tesla in-car browser are S4 stretch surfaces on the same private endpoint (the Watch needs a companion app or Shortcut; the Tesla has no CarPlay). **D53:** the service must answer any time, any place, so a dedicated always-on host (Mac mini class, 24–32 GB) replaces the Air as the inference host and the Air becomes a client. **D54:** offline means capture only — durable queue, idempotent retries, visible pending state; no on-device inference in the initial target.

### OQ-15 · Time, budget and measurable service targets — ✅ RESOLVED 1 Oct 2026
**D55:** 20+ hours a week sustained, which makes December 2026 schedulable. **D53:** €800–1,500 for the always-on host (purchase itself still a separate decision; 32 GB recommended over 24 GB because model, retrieval, local ASR and local TTS must be resident together before S5 adds roles). **D56:** cited text answer p95 < 8 s · voice push-to-talk to first spoken word < 5 s · recovery time < 8 h · recovery point zero confirmed captures. Report p50/p95 with sample counts and conditions. ⚠️ The < 5 s voice target is the likeliest to break; S4 reports the real p95 and renegotiates.

### OQ-16 · What counts as quality work in F3?
**Blocks:** P3.5 rule change only · **Owner:** David. The weekly script flags no quality for `long` + `tempo_block`. The flag is broader than strict tempo and also occurs on easy runs. Decide the qualifying evidence before changing F3; preserve and version historical expectations.

### OQ-5b · Is the Vibe Coding deliverable still active? — ✅ RESOLVED 1 Oct 2026
**Archived (D62).** Not live work. This project carries one workstream: the second brain. Supersedes D10's two-workstream scope. Nothing was moved to `40 Archive/` because it existed only as scope references in the tracking files — there were never any Vibe Coding notes. The `30 Resources/Product School/` notes are genuine knowledge and stay. If David revives it, it gets its own project folder rather than a share of this one.

---

### OQ-6 · Is LTHR really 166?
**Blocks:** nothing directly, but batch 02 (cause B) suggests it matters: 20 km de Bruxelles averaged 163 for 96 min
**Owner:** David · a 30-min solo all-out effort (LTHR = average HR of the last 20 min). Re-check zones against the golden dataset afterwards.

### OQ-7 · Should the post-race recovery window scale with race size?
**Affects:** rubric I6 (current D27: 7 days after races up to 21 km; 14 after marathon/ultra/mountain). The former flat-window description was stale.
**Owner:** decide from held-out batches. If short races (10 km) wrongly turn easy runs into "recovery", scale the window by km-effort.

### OQ-8 · Project instructions in claude.ai are stale — ✅ RESOLVED 1 Oct 2026 (David pasted the revised text; vault path, Source_Material location and D50 git convention)
**Owner:** David · they still point to `~/Desktop/AI_SecondBrain_Project/`; the vault is `~/Work/Dbrain2/10 Projects/AI Second Brain/` (since 6 Oct, M2; `~/Documents/Dbrain2/` from 8 Sep). Replacement text is at the bottom of the project doc `claude/ai-second-brain-project.md`.

### OQ-11 · Second domain: family logistics inputs (parked)
**Blocks:** nothing in S1–S6; additional production domains remain parked · **Owner:** David. Context: `00 Inbox/2026-09-30-1447-assistant-scope-ideas.md`
- Where does each source live (commune trash calendar, school menus, kids' activity schedules: site, portal, email)?
- Who else would use it if the deferred multi-user extension is taken up?
- ~~David's rule on children's data~~ ✅ answered 5 Oct (D69): data-policy v0.4 §3a. No names, initials or identifying places, minimised before capture, never demoed, manual capture only. Kids' schedules may enter as wave-1 data once P1.4 is done; the domain itself stays parked.

### OQ-12 · Wiki versus domain showcase — resolved 1 Oct
D47: running remains the established domain; supervised wiki maintenance is shared platform work. Demonstrate the complete lifecycle, with a small synthetic professional example at S6. This is the explicit scope amendment, not an additional production domain.

### OQ-13 · Durable source storage, retention and schema — ✅ RESOLVED 1 Oct 2026
**D49 (routing):** the wiki covers the entire vault (PARA + 90 System). Triage moves processed content to Projects/Areas/Resources/Archive/System by purpose; the verbatim capture moves untouched to `40 Archive/Inbox/` and the new note cites it in `source:`. Moves happen only at requested triage.
**D51 (physical location):** bulky material lives at `~/Documents/Source_Material/<project-or-topic>/`, outside the vault and git.
**D57 (IDs):** `src-<YYYYMMDDTHHmm>-<short content hash>` — survives renames and triage moves, and the hash detects duplicates and silent edits.
**D58 (audio retention):** deleted on successful transcription; the transcript becomes the retained original evidence. Consequence accepted: transcription quality is now an evidence-integrity concern, and the captures are bilingual.
**D59 (metadata):** `classification` + `source` + `review_status` + `note_type` + `created`/`updated`, on new notes; retrofit is P1.4, gated on OQ-20.
⚠️ **Not covered by these decisions, and still to be designed in T8/P6.1:** retention and deletion for *backups and git history* — removing a note does not remove earlier copies from either.

---

## Resolved

| # | Question | Answer | Date |
|---|---|---|---|
| R10 | (was OQ-10) Rubric v1.4 questions from batch 03 | G1 altitude mountain (D35) · G2 25 m/km (D39) · G3 broad flag / strict tempo (D36) · G4 uphill reps = hills (D37) · G5 long = over 15 km, long + tempo allowed (D40) · G6 misclick relabel (D38) | 30 Sep |
| R9 | (was OQ-9) Rubric v1.3 questions from batch 02 | A recovery post-race only (D27) · B two labels + race-pace tempo (D28, D29), HR off-road (D32) · C `vertical` flag (D31) · D unknown gear = no gear · E hikes aren't runs (D30) | 30 Sep |
| R8 | (was OQ-2) What does the firm's AI policy say? | No firm above Tower13. David's rule (D16): every contract must state his AI agent use explicitly, or the engagement stays out. Follow-up is T0.7 | 29 Sep |
| R7 | (was OQ-1) What is the showcase workflow? | **"Classify each run's session type from raw Strava data, roll a week into a coaching assessment — trend, effort adequacy, race-goal trajectory."** H1 = classification + trend/effort (checkable core). H2 = goal-trajectory judgment with confidence bands. Ground truth for the golden dataset comes from David labeling his own historical runs | 8 Sep |
| R1 | Showcase format? | Live system I drive, screen-shared | 7 Sep |
| R2 | "Collaborative" — which sense? | Original: humans first; amended by D45 on 1 Oct to multi-device personal service, then agents, additional humans later | 7 Sep / 1 Oct |
| R3 | Which sector to anchor security on? | Generic but strict, specialise later | 7 Sep |
| R4 | Timeline to client-ready? | 3 months | 7 Sep |
| R5 | Can Claude reach Apple Notes? | No — protected location, no API, no connector. Export to markdown is the route (and the better answer anyway) | 7 Sep |
| R6 | (was OQ-5) Does the Claude Project cover the second brain, or only Vibe Coding? | **Both.** Scope updated to carry two workstreams, second brain primary. Residual question about Vibe Coding status tracked as OQ-5b | 7 Sep |
