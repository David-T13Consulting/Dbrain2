---
classification: internal
note_type: queue
source: cowork
review_status: approved
created: 2026-10-02
updated: 2026-10-02
---
# For David: the single decision queue

David chose a single front door on 2 Oct 2026 (option A, provisional **D-cowork-6**). **Only Cowork asks David.** Claude Code and Codex never ask him directly. They add an entry below, set the brief to `blocked-on-david`, and carry on with other work. Cowork opens every session by walking David through the open entries, writes each answer into the entry and the brief, and the lead turns answers into decisions/commits.

**Entry format:** `ID · from · brief · question · options (recommended first) · what it blocks · urgency (today / this week / whenever)`. Answered entries move to *Answered* with the date and answer; the lead clears them once they are recorded in PROGRESS/briefs.

## Open

| ID | From | Brief | Question | Options | Blocks | Urgency |
|---|---|---|---|---|---|---|
| Q6 | `@code` (lead) | [[90 System/briefs/D68-single-front-door\|D68]] | D68 says Codex must never reach you in an interactive session, only as `codex exec` called by the lead. The lead cannot enforce that from its side: it controls its own calls, not whether you open a Codex session. Does anything need to change on your side? | **(a) Nothing — you simply will not run interactive Codex on this vault**, and D68 is enough · (b) Change a Codex setting or habit — tell the lead what and it records it in `AGENTS.md` | **Blocks D68's own closure** — its "Done when 3" is this question, so the brief sits `blocked-on-david` until you answer. The front-door rule itself is already in force in `AGENTS.md` | Whenever |
| Q5 | `@code` (lead) | [[90 System/briefs/P2.1-review\|P2.1-review]] | May Codex **read** the 6 reserved retrieval cases in order to check their labels? The brief asks it to review all 16 cases, while the constraints forbid running any model on those 6. The two instructions cannot both hold | **(a) Yes — reading is not "running"**, which is almost certainly the intent, since an independent label check is the whole point · (b) No — Codex reviews only the 10 dev cases and the 6 stay untouched · (c) Defer the 6 until the v2 taxonomy settles | P2.1's independent review. Not P2.2 | This week. Getting it wrong burns the reserved set irreversibly, which is why it was not guessed |

## Answered
| ID | Date | Answer |
|---|---|---|
| Q1–Q4 | 2 Oct | **Corrected by the lead.** The four David actually answered directly to Claude Code, before this queue went live, were: reviewer invocation (install the standalone CLI), reviewer effort (`high` stays standard), the runtime repository (`~/Documents/dbrain-runtime/` authorised) and the batch-04 scoring owner. Recorded in PROGRESS and the D64 / P2.2 briefs. **Codex reading the reserved cases was *not* among them** — it is open below as Q5. The lead can only speak for its own four questions; whether Cowork or Codex put the reserved-case question to David separately, it has no record either way, so the safe default is to leave it open |
| Q0 | 2 Oct | Who scores batch 04 → `@cowork`. Done and validated by David the same day |
| Q0b | 2 Oct | Independent Codex re-score of batch 04 → yes (David told Codex directly, before this queue existed) |
