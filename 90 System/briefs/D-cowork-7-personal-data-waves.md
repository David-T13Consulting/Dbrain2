---
classification: internal
task: D69 (OQ-11 / P1.4 / T8)
owner: "@code"
status: done
models: ["claude-opus-5-5 (lead, apply)", "gpt-6-astra (review rounds 1-2)", "gpt-6.1-sol (review rounds 3-4)"]
created: 2026-10-05
updated: 2026-10-05
source: for-david Q18–Q20, Q24–Q25
review_status: approved
note_type: decision
---
# Data-policy v0.4: personal data enters in gated waves (D69, was provisional D-cowork-7)

## Goal (one sentence)
Define when and under which gates personal data beyond training/HR may enter Dbrain2, starting with children's schedules (no names) in wave 1.

## Decisions already taken by David (5 Oct, via Cowork; queue Q18–Q19)
- Wave gating **accepted as proposed** (below).
- First wave-1 use case: **kids' schedules without names**: school lunches/menus, climbing practice and similar activity timetables. Mostly wave 1, on top of wave 0.

## Proposed policy text (for David to approve or edit, rule 8 / policy §8)

### Waves
**Effective date (Q24 fix 1):** the waves govern material **added from 5 Oct 2026**. Ordinary personal material already in the vault under v0.3 (profile, goals) stays; P1.4 relabels it on the four axes and flags anything that would now be wave 2 for David to keep, move or remove.

| Wave | Content | Labels (Q10 axes: domain · sensitivity · processing · sharing) | Gate before entry |
|---|---|---|---|
| 0 (in force) | David's own training and HR data | personal · sensitive · approved external · approved for demo (§4, David's explicit choice) | none, already permitted |
| 1 | Ordinary personal material: routines, family logistics without names, reading, goals, non-financial planning | personal · ordinary · approved external · private | **P1.4 four-axis retrofit complete** and the lint check validates the four axes on new notes |
| 2 | Sensitive personal material: health beyond training, finances, journal | personal · sensitive · **local-only** · private | All five: (a) P2.2/P2.3 local query service answers with no silent cloud fallback; (b) cloud agents (Cowork, Claude Code, Codex, claude.ai Project) **cannot reach** wave-2 files, verified by an access test, not by labels; (c) synthetic sensitive-note leak test passes (titles, search, listings, logs, traces, agent handoffs); (d) trace redaction live; (e) a deletion rule decided **and tested** that removes an item from the working copy, git history **and every backup** (T8/P6.1) |
| never | Others' sensitive data, client material, secrets | policy §2, unchanged | — |

### Children's data rule (new §3a)
1. **No names, initials or nicknames.** Use neutral labels ("child A", "child B") or none at all.
2. **No identifying places.** No school, club or gym names, no addresses, **no town or neighbourhood**. Use generic nouns ("school", "climbing club").
2a. **Minimise before capture, not at triage (Q24 fix 3).** Combinations can identify a child even without names (times + activity + town). Capture only what the logistics need: day, time, activity type, what to bring. A capture that breaks §3a is deleted at triage, not cleaned up and kept.
3. **No health, behaviour, performance or photos** of children, whatever the tier (extends §2.4).
4. **Never shown in a demo.** Demos use a synthetic family.
5. **Manual capture only** for now (Inbox → triage). No portal, email or website integrations before month 4 (no MCP sprawl).
6. Logistics only: what, when, what to bring or prepare. This feeds the parked second domain (OQ-11) as **data, not a built feature**. No family-logistics features until the H1 gate.

### Known tension
Gate (b) will probably need a separate local-only store outside the paths granted to cloud agents. That revisits Q10 (labels only, no vault split) **at wave 2, not now**. A separate purgeable repo would help with gate (e) for git history only; backups still need their own deletion rule.

## Files in scope (once approved)
- `10 Projects/AI Second Brain/02_Architecture/data-policy.md` → v0.4 (the lead edits; only David changes policy)
- `10 Projects/AI Second Brain/OPEN_QUESTIONS.md` → OQ-11: children's-data rule answered; second domain stays parked
- `10 Projects/AI Second Brain/TASKS.md` → wave-1 entry gated on P1.4; wave-2 gates linked to P2.2/P2.3, T8, T12, P6.1
- `10 Projects/AI Second Brain/PROGRESS.md` → D69 *(added by the lead, per review)*
- `index.md`, `log.md` → lead bookkeeping
- `10 Projects/AI Second Brain/OPEN_QUESTIONS.md` → OQ-20 resolved by Q10 *(added per review round 1)*
- `90 System/for-david.md` → clear Q18–Q20, Q24–Q26 and Q10 once recorded (D68) *(added per review rounds 2 and 3)*

## Done when (checkable)
- David approves or edits the text above.
- data-policy.md is at v0.4 with the waves table and §3a, and the decision is recorded in PROGRESS with a final D-number.
- No personal data beyond wave 0 **added from 5 Oct** enters the vault before P1.4 is ticked; material already present under v0.3 is handled by the effective-date clause. *(Aligned by the lead with fix 1, per review.)*

## Constraints
- Rule 8: Cowork proposes; nothing is populated until David confirms.
- Policy §8: only David changes the policy.
- Labels inform controls; they never grant access by themselves.

## Review
**David approved the proposed text as written on 5 Oct 2026 (queue Q20).** Codex raised three points (Q24); David chose **fix all first** (5 Oct). Cowork revised the text the same day: effective date (fix 1), gate (e) wording (fix 2), minimise before capture + no town (fix 3). **David approved the revised text on 5 Oct (Q25). Ready for the lead to apply.**

### Apply review, session 17 (5 Oct): **FAIL**
Codex, `gpt-6-astra` at effort `high`, read-only, given AGENTS.md, the approved brief (HEAD) and the staged diff.
**It verified:** the policy keeps the approved substance with no unapproved expansion; the Q10 → OQ-20 fix and the §3
cross-reference are justified; D69, the ID mapping, the index and log entries are consistent; every file is `internal`
with nothing sensitive. Per D65 stop condition (2) the loop ended here: nothing from the apply is committed.

| # | Finding | Severity | State |
|---|---|---|---|
| 1 | The two new wave tasks in TASKS have no owner tags (one-queue rule) | **blocker** | Fixed: David answered Q26 (wave 1 `@david`, wave 2 `@code`); tags added in TASKS |
| 2 | `models:` entries unquoted, so YAML splits them at the comma; the lead's exact model ID is not independently established by config | should-fix | Fixed: entries quoted. The lead ID is the model the session reports itself as; config only pins `opus` |
| 3 | `note_type: brief` is outside D59's values (fact / synthesis / decision / reference) | should-fix | Fixed: `note_type: decision` |
| 4 | Q10 answered OQ-20 and unblocked P1.4, but TASKS P1.4 and OPEN_QUESTIONS OQ-20 still say it is unanswered | should-fix | Fixed: OQ-20 marked resolved by Q10 in OPEN_QUESTIONS, P1.4 text updated in TASKS |
| 5 | This brief said `done` and promised a review "below" that was not there | should-fix | Fixed: this section, status `in-review` |
| 6 | Q18–Q20 and Q24–Q25 should be cleared from the queue once recorded (D68), without touching the held rows | should-fix | Fixed: Q18–Q20 and Q24–Q26 cleared; the held Q7 and Q13–Q17 rows are untouched |
| 7 | "Verbatim except two reference fixes" understates it: the Q24 parentheticals were dropped and "policy §2" became "§2" | nit | Fixed: Outcome lists every editorial change |

### Apply re-review, session 17 (5 Oct): **FAIL**, loop stopped under D70
Same reviewer and settings, given the approved brief (`0c6e625`), Q26 and the staged diff. **It verified:** the policy
keeps the approved substance with every editorial change disclosed; round-1 findings 1 and 3–7 are fixed, and
finding 2's quoting is fixed (the lead model ID stays self-reported); the queue clearing is right and the held rows
are excluded. Under D70 a failed re-review ends the run: nothing committed.

| # | Finding | Severity | State |
|---|---|---|---|
| 1 | `log.md`: the D69 entry was inserted *before* the already-committed D70 entry, breaking append-only | **blocker** (bookkeeping) | Fixed in the working tree: D69 now appended after D70 |
| 2 | Files in scope omits `90 System/for-david.md`, which the diff changes | **blocker** (bookkeeping) | Fixed in the working tree: listed, with OPEN_QUESTIONS for OQ-20 |
| 3 | Outcome claimed "fixed and re-reviewed" while the Review held only the first FAIL | should-fix | Fixed: this section, Outcome reworded |
| 4 | PROGRESS "Action for David" still asks him to answer OQ-20 | should-fix | Fixed in the working tree: the OQ-20 clause removed from the action |

**Next run:** fresh review of the whole apply diff; commit if it passes.

### Apply review round 3, session 17 (5 Oct): **FAIL** (bookkeeping), fixed under D70
Codex **`gpt-6.1-sol`** at effort `high`, read-only (David switched the review profile from `gpt-6-astra` on 5 Oct; the run's own log reads `model: gpt-6.1-sol`). Rounds 1–2 ran on `gpt-6-astra`, the profile's model at the time; their invocation logs were overwritten by later runs, so that attribution rests on the profile history, not a kept log. It verified the waves and §3a match the approved text with the editorial substitutions disclosed, and the earlier findings fixed within scope.

| # | Finding | Severity | State |
|---|---|---|---|
| 1 | PROGRESS: D69 row inserted before the committed D70 row; the decision log is append-only | **blocker** (bookkeeping) | Fixed: D69 now follows D70 |
| 2 | Q10 still in the queue though recorded in OQ-20, PROGRESS and this brief | should-fix | Fixed: cleared, and added to Files in scope |
| 3 | Model provenance for earlier rounds not evidenced by current config | should-fix | Fixed as far as evidence allows: per-round models recorded above, with the limit stated |

### Apply re-review round 4 (5 Oct): **PASS**
`gpt-6.1-sol`, effort `high`, read-only. No blocker; one should-fix (this Outcome lagged the Review), fixed before commit.
## Outcome
**5 Oct, lead (`claude-opus-5-5`): applied and committed. `done`.** `data-policy.md` is at v0.4: new §3a (children)
and §4a (waves), with the approved text otherwise verbatim. Editorial changes only: "Q10 axes" became "OQ-20 axes" and
"Q10" in the known tension became "OQ-20" (queue IDs are cleared and mean nothing in the policy); the "(Q24 fix 1)"
and "(Q24 fix 3)" markers were dropped; "policy §2" became "§2"; the brief's "Known tension" paragraph and its "labels
never grant access" constraint became two bullets under §4a. §3 gained one line pointing children to §3a.
`D-cowork-7` → **D69** in PROGRESS and `log.md`; OQ-11's children question answered and OQ-20 marked resolved (Q10);
TASKS has the two wave tasks with owners (Q26) and P1.4 as the wave-1 gate; Q10, Q18–Q20 and Q24–Q26 cleared.
**Review history:** round 1 (`gpt-6-astra`) failed on bookkeeping and ended that run under D65 as then written;
round 2 (`gpt-6-astra`, under D70) failed on bookkeeping and stopped; round 3 (`gpt-6.1-sol`) failed on one
bookkeeping blocker, fixed in the same run under D70; round 4 (`gpt-6.1-sol`) passed.

*Historical, superseded by Q25:* **Session 16 (5 Oct), lead: not applied; `blocked-on-david` (Q24).** Committed as a record in `e1728f0` (Codex:
PASS with should-fixes). Applying v0.4 to `data-policy.md` was attempted and **refused by Claude Code's permission
check** (the policy file counts as a shared resource), so nothing in `data-policy.md`, PROGRESS, TASKS or
OPEN_QUESTIONS changed. Three wording points from Codex's review need David before or after applying (Q24). Lead
bookkeeping still to do when applying: D69 for this decision (`D-cowork-7` → D69 in `log.md`), D59 fields here,
PROGRESS added to Files in scope, `index.md` entry.
