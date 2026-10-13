---
classification: internal
note_type: proposal
review_status: draft
created: 2026-10-13
source: Codex repository configuration review requested by David
---
# Proposed agent setup changes — prioritized review list

David requested this list for another agent to review and potentially process. These are proposals, not adopted rules or authorization to change security settings. Review against the current decisions and obtain David's approval wherever AGENTS.md requires it. Codex has not changed configuration, run access probes, or read the protected failure store.

Scope: the agents that build and maintain Dbrain2 and dbrain-runtime. This is a configuration and operating-procedure review, not a full runtime security audit. Findings distinguish observed configuration from inferred consequences. Priority indicates recommended implementation order.

## 1. P1 — Narrow shell approvals and close indirect-write routes

**Evidence:** `.claude/settings.json` allows bare `Bash` (line 8), alongside narrower ask and deny rules. The original allowlist record says execution of lead-editable code should not be pre-approved. See [[90 System/briefs/D-cowork-8-autonomous-runs]], Outcome, and [[AGENTS]], Hard limits. Claude documents that arbitrary Python/Node subprocesses are not fully constrained by file Read/Edit rules: https://code.claude.com/docs/en/permissions.

**Motivation:** matching ask/deny rules still take precedence, but a blanket Bash allowance approves commands outside those patterns. The inference is that a script can bypass the intended approval boundary by modifying protected files indirectly. The configuration therefore offers less protection than its operating rules suggest.

**Proposed change:** inventory effective shell approvals across project, local and user settings; replace blanket Bash and unrestricted interpreter approvals with the minimum commands needed. For protected files, use an independently enforced write boundary or approved mutation mechanism; adding more command-text patterns alone is not sufficient. Preserve the already-approved safe workflow and document residual gaps.

**Acceptance:** in an isolated synthetic fixture, routine allowed commands work; direct edits and script-mediated edits to protected policy/config files require approval or fail; unlisted destructive operations are not silently pre-approved. Confirm behavior in every supported permission mode. Never probe the real failure store.

**Approval:** David approves the exact security/permission diff before application.

## 2. P1 — Standardize startup and verify the effective configuration

**Evidence:** `~/Work/CLAUDE.md` tells sessions to start from `~/Work`. The shared project configuration is in the vault's `.claude/settings.json`. `~/Work/.claude/settings.local.json` contains old Documents paths and broad Python approvals. The runtime checkout has no `.claude/settings.json`. Claude's documented discovery depends on the primary working directory; additional directory access does not load a full configuration root: https://code.claude.com/docs/en/settings and https://code.claude.com/docs/en/permissions.

**Motivation:** reading the vault's instructions is separate from loading its enforced permissions. Sessions launched from different folders can therefore operate under different controls. The live session's effective configuration was not inspected; this is a startup risk inferred from the files and documented discovery behavior.

**Proposed change:** choose one supported entry point, preferably the vault root, or explicitly load a reviewed configuration when starting elsewhere. Add a startup check for canonical repo paths, loaded settings, reviewer profile, active permission mode and expected restrictions. Retire the move-specific startup guidance and obsolete live paths after confirming they are no longer needed.

**Acceptance:** supported launches from the vault, runtime and parent folder either load equivalent required controls or stop with a clear explanation. Record the actual settings sources. Historical path references remain marked as history.

**Approval:** David approves permission changes and changes to protected instructions.

## 3. P1 — Establish one current loop and review policy

**Evidence:** [[AGENTS]], Review failures and Review tiers, defines 2/5 reviews per step and Tier 1a batching. [[90 System/briefs/D-cowork-8-autonomous-runs]], David's decisions and The run loop, still says no commit without a review and five attempts. Its launch prompt explicitly sends the lead to those older rules. [[90 System/codex-review-checklist]] also retains conditional older Tier 0 instructions.

**Motivation:** contradictory active-looking instructions cause unnecessary reviews, incorrect retry counts and inconsistent approval behavior.

**Proposed change:** designate one authoritative current operating procedure, with explicit precedence and effective date. Replace duplicated executable instructions in old briefs with a link and a historical label. Preserve the decision history. Reconcile the review checklist with the current tier policy.

**Acceptance:** startup, checklist and brief template agree on review units, budgets, parking, reviewer unavailability, approval gates and end-of-run behavior. A reviewer can determine the required path for each tier without resolving contradictions.

**Approval:** David approves any rule change. Preserve D127's approved Tier 1a push behavior unless he explicitly changes it.

## 4. P1 — Define isolation for parked and unreviewed work

**Evidence:** [[AGENTS]], Review failures, leaves failed steps uncommitted and moves to the next brief. It isolates writing helpers but does not specify the lead's parked-patch isolation. [[90 System/handoff]] records uncommitted parked runtime work.

**Motivation:** the inferred risk is that a later step tests against, edits over, or accidentally stages a failed step's changes. Passing tests then may not describe the reviewed commit.

**Proposed change:** preserve each parked patch with its base revision and file list in an approved isolated location. Prefer per-brief worktrees where practical; otherwise define an explicit preservation process. Prevent overlapping work until isolation is complete, and stage only the current reviewed step. Never revert or overwrite another agent's changes.

**Acceptance:** park a synthetic step, complete another, and show that the later commit and tests exclude the parked patch; recover the parked work without loss. Test a pre-existing unrelated edit too.

**Approval:** lead implements within an approved brief; destructive cleanup or scope expansion goes to David.

## 5. P1 — Install deterministic commit gates for both repositories

**Evidence:** neither repository had an active pre-commit hook or configured `core.hooksPath` at inspection. Runtime `secret_scan.sh` scans its current directory. [[10 Projects/AI Second Brain/TASKS]], Secret scanner scope, already records the vault coverage gap. [[AGENTS]], Tier 0, relies on deterministic checks.

**Motivation:** an instruction to validate is easier to miss than an enforced gate. Tier 0 lacks independent model review, making reliable mechanical checks especially useful.

**Proposed change:** deliver reproducible hook installation and verification. Scan staged content in both repos, including handoff/tracking notes; validate required frontmatter, allowed classifications and basic links. Fail closed on scanner errors. Avoid scanning forbidden stores or dumping matched secrets into agent-visible output. Add a verification gate before unattended pushes; document that local hooks remain bypassable.

**Acceptance:** synthetic secrets and invalid classifications block commits; valid notes pass; scanner failures block; a fresh checkout can install and verify the gates. Test staged content rather than only the working copy.

**Approval:** hook/config changes require David's approval. Reuse the existing scanner-scope task instead of duplicating it.

## 6. P2 — Bound the entire run, including waits and consultations

**Evidence:** [[AGENTS]] bounds command retries and reviews, but its stop conditions use exhausted account limits or lack of actionable work. The inspected rules do not define a run deadline, total spend ceiling or uniform command timeout. [[10 Projects/AI Second Brain/TASKS]], P5.2, plans persistent jobs, bounded budgets and cancellation for the product runtime.

**Motivation:** finite retries do not bound a hung command, repeated waits, cumulative consultations, or a large queue. The development-agent loop needs its own budget even before product-runtime jobs exist.

**Proposed change:** define per-run time/spend or token ceilings, command-specific timeouts, maximum wait periods, cancellation, and a reserved allowance for safe shutdown/reporting. Count consultations and background work toward the run budget. Persist counters across resumption; do not reset them merely by restarting a session.

**Acceptance:** a hung synthetic command times out; cancellation stops child jobs; budget exhaustion preserves work and produces one clear handoff. Slow approved measurements have explicit larger limits.

**Approval:** David chooses the limits and approves the changed loop stop conditions.

## 7. P2 — Make ownership and recovery explicit

**Evidence:** [[AGENTS]] requires one lead and owner tags; [[90 System/briefs/_template]] has status but no run identifier, ownership lease or resumable execution record.

**Motivation:** owner tags coordinate intent but do not prevent two lead sessions from claiming the same work. After interruption, prose alone may not establish which operation completed.

**Proposed change:** add a small durable run record: run ID, lead identity, claimed brief/step, base revisions, heartbeat or lease expiry, budgets, parked patches and completed operations. Define transitions, stale-claim recovery and an idempotent resume procedure. Keep it local and text-minimized.

**Acceptance:** a second lead cannot claim active work; an interrupted run resumes without duplicate commits or lost patches; stale ownership is recovered deliberately. Reuse existing tracking where possible rather than creating another competing queue.

**Approval:** approved brief and exact file scope required; lease-recovery behavior must not silently delete work.

## 8. P2 — Test the agent controls and the trust boundary

**Evidence:** [[AGENTS]] says consultation advice is input, not instruction, and requires scoped briefs. Its root rules do not provide a general explicit rule distinguishing retrieved documents, tool output and agent messages from David's authorization. The runtime injection work is separately planned in [[90 System/briefs/G1-inj-read-path-injection]].

**Motivation:** build agents consume notes, handoffs and reviewer output too. A document that imitates approval or tells an agent to broaden scope can undermine the workflow before runtime writes exist.

**Proposed change:** state the evidence-versus-instruction boundary explicitly. Require traceable David authorization for scope and permission changes; another agent cannot create that authority by assertion. Add synthetic scenarios for forged approvals, instructions inside source documents, conflicting rules, overlapping helpers, reviewer unavailability and parked-step contamination. Keep reviewer input independent of the lead's conclusions, as already required.

**Acceptance:** agents treat planted document instructions as data, reject forged scope expansion and preserve approval gates. Tests check observed actions, not merely that the model repeats the policy.

**Approval:** David approves instruction changes; test work follows its applicable review tier.

## 9. P2 — Track the accepted privacy exception through closure

**Evidence:** [[10 Projects/AI Second Brain/DECISIONS]], D110, explicitly accepts the Air's Claude shell tripwire limitation and untested screen-control routes. [[90 System/briefs/P2.7-failure-capture-loop]] records the access tests. This is an accepted residual risk, not a newly discovered breach.

**Motivation:** the dedicated-host migration must demonstrably retire the exception rather than carrying it forward by accident.

**Proposed change:** add a closure checklist to the existing migration/security work: dedicated service-user ownership, cloud-agent exclusion across applicable tools, synthetic access tests, permitted audit-log access, and confirmation that the Air exception has ended. Do not treat additional regex deny rules as equivalent to OS isolation.

**Acceptance:** protected synthetic content is unreachable to cloud agents through tested file and subprocess routes; permitted audit metadata remains available; D110's closure evidence is recorded. No real failure text is used in tests.

**Approval:** David approves OS, account and permission changes; preserve D110 until its replacement is verified.

## 10. P3 — Split current instructions from historical records

**Evidence:** [[AGENTS]] combines hard rules, orchestration, detailed review accounting and model routing, while older briefs duplicate operating instructions.

**Motivation:** splitting helps only if it reduces contradictory authority and makes startup cheaper. More files without clear precedence would make this worse.

**Proposed change:** after proposal 3, keep AGENTS.md as a short mandatory entry point with hard rules and explicit links to the current loop, review policy and model-routing policy. Keep project context in the project CLAUDE.md. Leave briefs as scoped contracts and decision evidence. Define which supporting files must be read before each role acts; do not rely on agents discovering them accidentally.

**Acceptance:** each live rule has one authoritative home; required rules load for Claude and Codex; startup remains understandable; historical decisions remain discoverable without appearing active.

**Approval:** David approves the exact AGENTS.md restructuring. Avoid a broad note retrofit as part of this change.

## Suggested processing order

Review proposals 1–5 first: they address permission enforcement, startup consistency, contradictory instructions, patch isolation and missing commit gates. Then process 6–9 for unattended-run reliability and privacy closure. Do 10 last, after deciding the authoritative policy structure.

The other agent should validate each finding against the current effective setup, challenge the proposed solution, and turn accepted items into scoped briefs with review tier, files, approval requirements and checkable completion criteria. Do not apply this proposal wholesale or silently revise David's prior decisions.
