---
classification: internal
domain: ai-second-brain
sensitivity: ordinary
sharing: private
source: "Codex proposal [[90 System/agent-setup-change-proposals-2026-10-13]], triaged by Cowork with David, 13 Oct 2026"
created: 2026-10-13
review_status: unreviewed
policy_note: "Parked by David's decision (13 Oct): not part of AS1. Revisit at S5 (multi-agent execution) or when a listed trigger occurs. No brief, no build until David names an item."
---
# Multi agents governances improvements

Parked items from the 13 Oct agent-setup proposal. What is being done now is in [[90 System/briefs/AS1-agent-setup-hardening|AS1]] (proposals 3, 5 with 1 folded in, 2, the rule part of 8, and 9).

| From proposal | Item | Cowork's recommendation (13 Oct) | Revisit when |
|---|---|---|---|
| 1 | Narrow shell approvals instead of keeping broad `Bash` | Not chosen: David kept Q54 plus the protected-file commit gate (AS1 step 3) | A protected file is found changed outside an approved commit, or unattended runs move to the Mac mini |
| 4 | Isolate parked, unreviewed work so later steps don't test over it | Simple version first: save each parked step as a patch file with its base commit and file list, outside the repo; worktrees per brief only if that proves insufficient | Next time a parked step's edits sit in the tree while another step runs, or any test result is found to include parked work |
| 6 | Bound the whole run (time, spend, waits, consultations) | Minimal: a wall-clock limit per run and command timeouts. Persisted spend counters across restarts: not now | A run hangs or overruns; or at S5 |
| 7 | Run record with ownership lease, heartbeat, idempotent resume | Reject for now: one lead session at a time, one person | Two lead sessions ever run at once, or S5 multi-agent jobs start |
| 8 | Test suite for the trust boundary (forged approvals, planted instructions, conflicting rules, reviewer unavailability, parked-step contamination) | Fold into G1-inj (read-path injection) rather than a separate suite; the rule itself is in AS1 | G1-inj brief is sized; or before S3 writes |
| 10 | Split AGENTS.md into a short entry point plus linked loop, review and model-routing policies | Defer; 213 lines is manageable. Only if AS1 step 1 shows the single file causes contradictions | AGENTS.md passes ~300 lines, or a rule conflict recurs after AS1 |

General caution (Cowork, 13 Oct): the governance layer is growing faster than the product (~130 decisions). Pick these up only when a trigger fires, not because they are on a list.
