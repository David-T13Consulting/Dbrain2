---
classification: internal
review_status: codex-reviewed
---
# Progress Tracker — AI Second Brain Project

**Last updated:** 8 Oct 2026 · **Updated by:** Claude Code (session 37, lead loop: D95–D101; T9 ready, GO for Fri 9 Oct (Q81); deny list applied; client-tier note, Inbox triage and M6b committed; weekly-review and EmbeddingGemma content back to Cowork)

---

## Current state

| | |
|---|---|
| **Phase** | S1 requirements settled; S1 exit evidence incomplete (P1.3 data-flow diagram, roots/tools list); S2 under way: P2.2 query service committed (`4b5e91f`, runtime `c8b3b7b`); MVP-phone committed (P2.4, runtime `53e5740`); repos moved off iCloud to `~/Work` (M2, done 6 Oct); clean-up done, hold lifted (D81); P2.6 and P2.7 next. Running validation in parallel |
| **Schedule** | Original 13-week ordering superseded by S1–S6. Dated S2–S6 plan exists, proposed (`f9c014e`); demo-ready Fri 18 Dec 2026 (Q29) |
| **Target** | Client-ready demo, December 2026 |
| **Status** | 🟢 Week 0 closed · Week 1 closed · Week 2: 3 skills drafted and smoke-tested · Week 3: golden dataset **70/150** runs labelled. Batch 04 held out and scored 2 Oct — terrain 100% (≥95% ✅), intent 65% (≥85% ❌); the flags have no D19 threshold, and against the always-"no" baseline of 85% `tempo_block` at 40% is far worse while vertical at 90% barely beats it. The evidence behind the v2 taxonomy (D67) |
| **Dependencies** | Devices, availability, capacity, service targets and provenance schema all settled 1 Oct (D52–D59). Remaining dependency is the always-on host purchase (D53) — the Air cannot satisfy the availability requirement. Two local candidates and initial retrieval benchmarked, not accepted. Running labels continue independently |
| **Next action** | **Session 37 (8 Oct): T9 is ready; GO for Fri 9 Oct morning (Q81, D96)**, David present, Air plugged in and quiet, phone service stopped; otherwise Mon 12 Oct. Host: option B, 48–64 GB, up to €4,000, sized by a rule fixed before the result, ordered by 16 Oct (D95). Done: deny list applied (D97), client-tier note committed (D98), Inbox triaged, M6b briefed for after T9 (D100). Back with Cowork: the 8 Oct weekly-review branch and the EmbeddingGemma note (review FAIL on provenance; then David's content OK, D101). P2.7 after T9 (D94). **Earlier:** **Session 36 (8 Oct):** David's 7 Oct answers recorded (D89 data policy v0.6, P2.7 unblocked; D90 AGENTS push wording; D91–D93); force-push deny list drafted for his OK (**Q79**); HTML lint exemption applied; client-tier note reviewed, waits for his Tier 2 OK (**Q80**); the scheduled weekly review committed on a local branch (**Q78**). **David, 8 Oct 09:11: T9 goes before P2.7 (D94)**; T9 needs him present, the window is to be scheduled; P2.7 not started. Host: no purchase; ordered after T9/M6, deadline 16 Oct (D92). **History:** **The 08:57 hold is lifted (D81, 7 Oct).** Run A (session 31) built fail-closed date reading for the phone; it was **parked** after five reviews, uncommitted. **David answered Q72 (a) (D82):** ship the supported forms only. **Run B (session 32):** the review and the one re-review each failed on one gap (seasons; then French seasons after an apostrophe), fixed once; nothing committed in the runtime; Q73 answered (b) (D83). **Run C (session 33):** the one review found six more season and period wordings with no date label; nothing committed; Q74 answered (a) (D84). **Run D (session 34):** the one review found eight wordings outside that class (French day numbers, named days); Q75 and Q76 answered (a) (D86–D88). **Run E (session 35): the phone code is committed and pushed** (review round 19 PASS); David's phone re-check is queued. GitHub refused force-push protection on the private repos: **Q77**. P2.6's files in scope are listed; its evaluation waits for David's phrase-set validation. P2.7 waits for his data-policy approval. Widening date reading is P2.6 (proposed). **Then:** answer quality (P2.5, T9), in the Q51 order as Cowork names each item. Host decision (D53) gates sustained-performance numbers |
| **Action for David** | **All six session-14 questions are answered and recorded** — his standing actions below are unaffected: D64 closed, the `dbrain-runtime` repository authorised (now `~/Work/dbrain-runtime/`), batch 04 scored by `@cowork`, and Q5/Q6 answered through the [[90 System/for-david|for-david]] queue on its first use — Codex may read the 6 reserved cases read-only (P2.1 unblocked), and nothing changes on David's side for interactive Codex (D68 closed). Then: paste the weekly-review task ID and first-run output into [[90 System/weekly-local-model-review|weekly-local-model-review]] (D60). Decide the always-on host purchase (D53; 32 GB recommended). OQ-20 is answered (queue Q10, 5 Oct); OQ-21 was not needed — David decided it himself as D66. |

### Original work-package progress — retained snapshot

Current platform gates S1–S6 are not yet passed. P1.0/P1.1 are complete; supplied-evidence comparisons and a bounded retrieval experiment have run, but retrieval/service acceptance remains open. The historical snapshot below is not a percentage-complete estimate for the new scope.

```
Week 0  Foundations    █████████░  90%   (T0.7 contract clause: future-only)
H1      Ship           ██████░░░░  60%   ← you are here (Weeks 1–2 done, Week 3 started)
H2      Validate       ░░░░░░░░░░   0%
H3      Collaborate    ░░░░░░░░░░   0%
```

### Original domain/demo gate status — current platform gates in roadmap §0

| Gate | Criteria met | Status |
|---|---|---|
| Week 0 | Workflow named · red lines stated | ✅ Met 29 Sep |
| H1 | 3 skills pass · rollback tested · evals screen-shareable · no client data | ⬜ Not met |
| H2 | Eval dashboard live · avoidable exceptions measured separately from approvals · governance review (D48) | ⬜ Not met |
| H3 | Demo runs twice, no unexplained failures | ⬜ Not met |

---

## Metrics

Not yet instrumented as a service. Start platform measurement at S2; retain running scores in their batch records. Original aspirations below are qualified by D48 and roadmap §0; no population-level reliability claim yet:

| Metric | Target | Current |
|---|---|---|
| Hallucination rate | <1% | — |
| Eval regression | 100% of changes stay positive | — |
| Avoidable exceptions | Mandatory approvals tracked separately; preserve the approval gate | — |
| Recall accuracy | ≥85% | — |

*Deliberately not tracked at this volume: drift velocity/week, confidence distribution, inference ROI, deflection rate. Know the numbers; explain why they're not instrumented yet.*

---

## Decisions and older sessions

Moved verbatim on 8 Oct 2026 (session 38, David's maintenance layout): [[10 Projects/AI Second Brain/DECISIONS|DECISIONS]] holds D1 onwards. Sessions 1–35 are in [[10 Projects/AI Second Brain/PROGRESS-archive|PROGRESS-archive]]; this file keeps the last three sessions.
Decisions that notes cite as "in PROGRESS" are in DECISIONS.


---

## Session log

Newest first. One entry per working session — what happened, what changed, where to pick up.

### Session 37 — 8 Oct 2026 · Claude Code, lead loop (09:35 block; T9 readiness; Q79/Q80; triage; M6b; queue)
**Authorization:** "pick up the loop" from David, with Q79 (a) and Q80 (a); the handoff's 8 Oct ~09:35 block first (records, T9 readiness with a go/no-go by 18:00, Inbox triage), then Q79/Q80 and the client-tier note, then the queued entries (Q78/`f25aa64`, EmbeddingGemma, M6b). No P2.7. **Ended by** the instruction's end (all items run). Lead `claude-opus-5-5`; reviewer Codex `gpt-6.1-sol` (review profile), high, read-only.

**What changed for David:** T9 can run on Friday morning with him (Q81); nothing was scored. His host can be a 48–64 GB machine up to €4,000. The agents now refuse force pushes in the forms he approved. His client-tier requirements note is in the vault, its legal points still marked for the lawyer. Two captures are triaged (a parked project-alignment brief; an EUrouter resource), and Tower13 has an area. The embedding test has a brief and a slot after T9. The weekly model review and the EmbeddingGemma note went back to Cowork for sources before he is asked to approve them.

- **09:35 item 1:** `54a511f`, D95 (host option B) and D96 (T9 window). Round 1 PASS.
- **09:35 item 2, T9 readiness:** the runner `t9_compare.py` (the 6 Oct draft) failed review three times (8, 5, 4 blockers: timeouts and malformed replies lost, server outside the sandbox, network check failing open, unchecked manifest, incomplete RSS, unpinned cases); rewritten, round 4 PASS; runtime `ae934d5`, pushed. Four models and b11146 match their SHA-256 pins; all load and answer the warm-up under the no-network sandbox (dry check, nothing scored). Dev cases re-checked on corpus `878a08ea6f57`: three points listed in the T9 brief, rule unchanged. `da3be79`; **Q81 GO**.
- **09:35 item 3:** `3a7f819`, Inbox triage. The EUrouter capture was archived to `40 Archive/Inbox/` (D49) instead of `git rm` (deleting files is a hard limit). Rounds: FAIL (uncited legal framing; boundary stricter than the policy), escalate (question 4 proposed an answer), PASS.
- **Q79:** `8034de8`, deny list applied (D97), Tier 2 PASS. **Q80:** `1cf0bfc`, client-tier note committed (D98), PASS.
- **M6b:** `d19b409` (D100: Q8 budget 25 GB, venv), round 1 FAIL (scope), round 2 PASS. **D99/D101:** `182b9df` (TwIL licence answer; Q78 route), PASS.
- **Weekly review `f25aa64` and the EmbeddingGemma desk note:** Codex content pass FAIL (Tier 2 provenance: TwIL-LM2 claims unsourced; the EmbeddingGemma note misreads the MTEB versions, one claim unsourced, one negative claim unsupported). Findings in [[90 System/handoff]] for Cowork; nothing landed; branch untouched.
- **Incident (the lead's):** a Python edit opened `90 System/for-david.md` for writing before reading it and truncated the file, wiping Cowork's uncommitted edits there (Q78 annotation, Q-cowork-1, Q-cowork-2). Restored from the lead's verbatim copy of 09:38 (Q-cowork-1's last words may differ); any later Cowork edit there is lost. Committed versions were never affected. Cowork asked to check. Every later edit in the run read before writing.
- **Not done:** project CLAUDE.md's Hosting row (24–32 GB, €800–1,500) is stale after D95; a CLAUDE.md edit asks David, so it is left for Cowork to queue.
- **Push:** runtime `ae934d5` pushed; the vault is pushed (non-force) after this close commit and checked for 0 ahead / 0 behind.

**Pick up at:** Q81 (T9 Friday or Monday, with David); Cowork's fixes to the model content, then re-review and David's content OK; the week of 12 Oct items (T0.7, client-vault scaffold).

### Session 36 — 8 Oct 2026 · Claude Code, lead loop (records; prune; Q77 draft; lint exemption; client-tier note)
**Authorization:** "pick up the loop" from David, with the handoff's 7 Oct ~19:30 block (items 1–6), a prune of executed blocks (runs A–E), and commit and push. **Ended by** David's 09:11 order (D94): items 1–4, 6 and the prune, then stop; item 5 (P2.7) not started. Lead `claude-opus-5-5`; reviewer Codex `gpt-6.1-sol` (review profile), high, read-only.

**What changed for David:** his failure-store text is now policy (v0.6), and AGENTS.md says the lead pushes without asking. The exact force-push deny list waits for his OK (Q79). The client-tier note passed review but carries legal points nobody has checked yet (tagged `unverified`), so it waits for his OK too (Q80). The weekly model review committed to a side branch on its own; he decides how it lands (Q78). No host is bought until T9/M6 (deadline 16 Oct), and T9 needs a window with him.

- **Item 1:** `8990bbe`, records batch (AGENTS.md, data-policy v0.6, for-david, handoff; D89–D93; five answers cleared; Q78). Tier 2, approved by David. Review round 1 FAIL (D93 claimed applied; Q78 tier too low), fixed; round 2 PASS.
- **Prune:** `51f332f`, "Prune executed handoff blocks (runs A–E)"; three open items carried over. Tier 0; round 1 FAIL (session 32 note missed), fixed; round 2 PASS.
- **Item 2:** `f4b09ab`, [[90 System/briefs/Q77-force-push-deny-list|Q77 deny list]] draft (13 wildcard rules) and Q79; settings unchanged. Round 1 FAIL (a final `:*` is Claude Code's trailing-wildcard suffix), fixed; round 2 PASS.
- **Item 3:** `a8a641f`, lint M5 exemption for HTML render sources. Round 1 PASS.
- **Item 4:** Q30 (b) in TASKS (no purchase; 16 Oct deadline; T9/M6 sizes it).
- **Item 6:** client-tier note, `note_type: requirements` (David's option). Review raised it to **Tier 2** (uncited legal and contract claims): the lead tagged them `unverified`, cited the whole-vault indexing, and marked the R3 audio timing as a proposed rule that differs from D58; round 3 PASS. **Not committed**: it and its index line wait for David (Q80). The three TASKS entries (T0.7 widened, client-vault scaffold, R3–R7 → P4.3) are in, all for the week of 12 Oct.
- **Weekly review incident (Q78):** at 09:03 the scheduled Cowork review created `cowork/local-model-review-2026-10-08`, switched this working tree to it and committed there (now `f25aa64`), sweeping in one lead log entry, which it later removed. The lead pointed HEAD back at `master` (`git symbolic-ref`, no file changed) and left the branch untouched. Cowork kept editing during the run (an Inbox capture deleted, `20 Areas/Tower13/`, `30 Resources/AI Vendors/`, a `project-alignment` brief, a handoff entry, a provisional queue entry): none of it is in this run's commits; the lead's read-only check found all three new notes `internal`.
- **Push:** the vault is pushed (non-force) right after this close commit and checked for 0 ahead / 0 behind; runtime unchanged this run.

**Pick up at:** Cowork's handoff block with David's decisions; Q78, Q79, Q80; scheduling T9 with David.


---

## How to resume

1. Read `CLAUDE.md` (who, what, rules)
2. Read this file (state, decisions, last session)
3. Read `TASKS.md` (▶ Next action at the top)
4. Check `OPEN_QUESTIONS.md` for anything now answerable

Then work. Before you stop, update all three.
