---
classification: internal
task: D77             # was provisional D-cowork-10; final number assigned by the lead, 6 Oct (session 29)
owner: "@code"        # David approved 5 Oct (Q55, with amendment); lead applies, David approves the AGENTS.md diff
status: open          # lead, 6 Oct (session 29): AGENTS.md text applied (D77); pre-commit check, calibration file and ~/.codex prompt waited for the hold, lifted 7 Oct (D81); not started
models: ["claude-opus-5-5 (Cowork, draft; lead)", "gpt-6.1-sol (Codex reviewer, high)"]
created: 2026-10-05
---
# Review tiers: cut review load without weakening the hard gates

> **Historical record (labelled 13 Oct 2026, AS1 step 1).** The tiers, review units and conforming edits below are those of 5–6 Oct, including the note under "Decision proposed" and the Review section it points to. The current rules are in [[AGENTS]] (Review tiers, Review before commit, Review failures; D127); where this brief differs, AGENTS.md wins.

## Goal (one sentence)
Match review effort to risk, so bookkeeping and mechanical changes stop waiting on Codex and on David, while domain claims, rules and anything client-facing keep a human gate.

## Why (David, 5 Oct, via Cowork)
"Everything feels slow." David agreed to (A) parallel readers with one writer and (C) batched approvals, plus letting Codex take over part of his reviews. He questions whether checking everything that enters the vault is productive.

**Evidence from the vault (5 Oct):**
- 39 commits since 1 Oct; about 20 of them record answers or decisions (`Record Q…`, D-numbers). Under Q40 each one needed a Codex pass and its own commit.
- `handoff.md` holds 12 entries waiting for a lead run; Cowork cannot commit (D49).
- P2.2 went through about 16 review rounds (B–Q) before passing. Q53 (accepted risks) and Q46 (fail closed) ended the arms race only after the fact. Reviews had no severity bar written down in advance.
- AGENTS.md rule 4 ("propose, don't populate") applies to every note entering 10–40 as structured knowledge, whatever its risk.

**Diagnosis:** the agents are not the bottleneck. Uniform review is: every change, however trivial, pays the same Codex round and often a David round.

## Decision proposed
*Superseded in part (lead, 6 Oct): where this proposal differs from the Review section below (David's Q55 amendment and the AGENTS.md text he approved in Q65), the Review section governs. In particular, recording David's answers is Tier 1, not Tier 0.*

### 1 · Three review tiers
| Tier | Covers | Gate before commit | David sees it |
|---|---|---|---|
| **0 · Mechanical** | Recording David's answers verbatim (for-david, PROGRESS, TASKS, OPEN_QUESTIONS, log, index), handoff bookkeeping, frontmatter/link/format fixes, Inbox captures, moving files the lint found | Deterministic checks only (§3). **No Codex review** | No |
| **1 · Standard** | Briefs, drafts, specs, summaries of sources David supplied, skills, eval scripts, runtime code outside the security boundary, notes in 10–40 that carry no Tier 2 claim | Codex review against `90 System/codex-review-checklist.md` + §3 checks; auto-commit on pass | Weekly digest + random sample (§4) |
| **2 · Gated** | (a) Domain claims David would repeat to a client: banking, asset management, Belgian healthcare/medtech regulation · (b) decisions (D-numbers) and changes to the rules (AGENTS.md, CLAUDE.md, data policy, model policy) · (c) anything shown in a client demo or published · (d) security-boundary code in `dbrain-runtime` · (e) any claim tagged `unverified` · (f) anything Codex marks `escalate` | Codex review + §3 checks + **David's approval**, batched (§5) | Yes |

When in doubt, the higher tier. The author proposes the tier in the brief; Codex may raise it, never lower it.

### 2 · Provenance rule (replaces "David fact-checks everything")
Every factual claim in a Tier 1 or 2 note cites its source: a `[[wikilink]]`, a path in `~/Documents/Source_Material/`, or a URL. A claim with no source carries `unverified`. Codex checks that each cited source **exists and supports the claim**; it does not judge whether the claim is true (Claude and Codex can share the same wrong belief). Only Tier 2 claims and `unverified` claims reach David.

### 3 · Deterministic gates (all tiers, no LLM judgment)
Run by a vault pre-commit check, built by the lead (this is the planned H1 control in data-policy §7):
1. Secret scan (reuse `dbrain-runtime/secret_scan.sh` patterns) → block.
2. Every changed `.md` has `classification: public | internal`; `client` → block and stop (lint M5).
3. No file over 1 MB, no PDF/media extensions (lint M7).
4. Wikilinks in changed files resolve (lint M2) → warn, not block.
A block is a stop condition (3) of the lead loop: report, never fix silently.

### 4 · Trust calibration for Tier 1 (two weeks, then review)
David spot-checks a random 1 in 5 Tier 1 commits from the weekly digest and records agree / disagree with Codex's verdict. Agreement ≥ 90% over at least 20 samples → sampling drops to 1 in 10. Below 90% → tighten the checklist, keep 1 in 5. Results logged in `90 System/reports/review-calibration.md`. This is also a client-ready eval story: the reviewer was measured before it was trusted.

### 5 · Batched approval (option C)
Tier 2 items do not interrupt David one by one. The lead lists them in `for-david.md` under a `Batch` heading with a one-line summary, the diff path and Codex's verdict. Cowork walks David through the batch once per session (existing D68 front door). Approve / reject / amend per item.

### 6 · Parallel readers, one writer (option A)
The lead may fan out read-only subagents (research, drafting, checks) in parallel; their output returns to the lead, which is the only agent writing files in that run. No worktrees, no parallel writers on `master` (keeps D50).

### 7 · Review severity bar (stops review arms races)
Codex classifies every finding as `blocker`, `should-fix` or `nit` using the checklist. Only blockers fail a review. Should-fix items are fixed in the same round if cheap, otherwise logged in the brief and carried. Nits are logged, never re-reviewed.

## Proposed AGENTS.md text (David approves before the lead applies it)
**Replace hard rule 4** with:
> 4. **Propose, don't populate, for Tier 2.** Domain claims, decisions, rule changes and client-facing content enter 10–40 only after David confirms. Tier 0 and Tier 1 changes follow "Review tiers" below. Every factual claim cites a source or is tagged `unverified`.

**Replace the bullet "No commit without a Codex pass, ever (Q40)"** with:
> - **Review tiers (D-cowork-10).** Tier 0 (mechanical, verbatim recording of David's answers): deterministic checks only. Tier 1 (standard): Codex pass against `90 System/codex-review-checklist.md`, then commit. Tier 2 (domain claims, decisions, rule changes, client-facing, security-boundary code, `unverified`, Codex `escalate`): Codex pass and David's batched approval. When in doubt, the higher tier; Codex may raise a tier, never lower it. The deterministic pre-commit check runs on every commit. While Codex is unavailable, Tier 1–2 work waits uncommitted for one batched review; Tier 0 still commits.

**Amend "Review failures (D72)"**: add after the first sentence:
> Only `blocker` findings fail a review; `should-fix` and `nit` findings are logged in the brief and do not trigger another round.

**Add to "Lanes"**:
> The lead may run read-only subagents in parallel; only the lead writes files in a run (D-cowork-10).

**Batch the handoff**: change "the lead commits them first, as their own commit" to:
> the lead commits Tier 0 handoff entries together as one bookkeeping commit; Tier 1–2 entries as their own commits.

## Files in scope
- Cowork (done in this session, uncommitted): this brief, `90 System/codex-review-checklist.md` (new), `90 System/for-david.md` (Q55), `90 System/handoff.md`.
- Lead, **after David approves Q55**: `AGENTS.md` (text above), vault pre-commit check (§3; the hook script lives in `dbrain-runtime` or `90 System/scripts/`, lead decides, tracked in git; installing the hook is a settings change, so it follows the hard-limit ask), `90 System/reports/review-calibration.md` (new), PROGRESS / TASKS / log (final D-number), `~/.codex` review prompt pointing at the checklist.
- **Held (lead, 6 Oct):** Q65 releases only the AGENTS.md text, the checklist's `review_status` and their bookkeeping. The pre-commit check, the calibration file and the `~/.codex` prompt wait until David lifts the 6 Oct hold. *(Cowork, 9 Oct: the hold was lifted 7 Oct (D81); none of the three is started.)*

## Done when (checkable)
- [x] David approves, amends or rejects Q55.
- [x] AGENTS.md carries the approved text; final D-number logged.
- [ ] Pre-commit check blocks a test commit containing a fake token and a `classification: client` note, and passes a clean one.
- [ ] `codex exec --profile review` receives the checklist and the brief's proposed tier with every review.
- [ ] First weekly digest produced with the 1-in-5 sample; calibration file started.

## Constraints
- AGENTS.md and data-policy edits are hard limits: David approves the text first.
- The tiers change **review effort only**. They do not relax: no client material, no secrets, classification on every note, large files outside the vault, the hard-limit list.
- The reviewer stays a different vendor's model (D64).

## Open points for David
1. Is "recording your answers verbatim" safe as Tier 0? Recommended yes: the answer is yours and the deterministic checks still run.
2. Calibration threshold: 90% agreement over 20 samples, or stricter?
3. Should Tier 1 notes in 10–40 carry `review_status: codex-reviewed` so you can tell them apart from notes you approved? Recommended yes.

## Review
**David, 5 Oct (Q55): approved as drafted, except open point 1 → recording David's answers is Tier 1 (Codex checks faithful recording), not Tier 0. Point 2: 90% over 20. Point 3: yes, `review_status: codex-reviewed`.**
**David, 6 Oct (Q65, via Cowork): approved the exact AGENTS.md text below.** It replaces the "Proposed AGENTS.md text" section above, which predates the Q55 amendment. Cowork added two safeguards, both approved: (1) Tier 0 keeps a Codex pass until the pre-commit check is installed; (2) Tier 2 covers "decisions David has not yet taken", so recording his own decisions stays Tier 1. The lead applies this text verbatim (line wrapping may follow AGENTS.md style), assigns the final D-number, and sets the checklist's `review_status` to `approved`. The pre-commit check (§3), the calibration file and the `~/.codex` prompt are separate lead work, not part of this text.

**Lead review of the drafts, 6 Oct (session 28), Codex `gpt-6.1-sol` (review profile), high, read-only.** Round 1 FAIL on the checklist: (1) its out-of-scope line exempted Tier 0 from Codex outright, against Q40 and Q65's safeguard; (2) R2 made region codes and club colours should-fix, against data-policy §3a.2/2a. Should-fix: mark the original proposal superseded where the Review differs; R5 to say "decisions David has not yet taken"; record that the pre-commit check, calibration and prompt work wait for the hold to lift. The lead fixed all five in the brief and the checklist (David is at the Mac). Round 2 FAIL: R2 still let child details beyond what the logistics need (§3a.2a, §3a.6) pass as should-fix; the lead made them blockers. Round 3 FAIL: the Why section said rule 4 applies to every note (it covers notes entering 10–40). Should-fix: R4's path for an uncited Tier 1 claim. The lead fixed both.

### Approved AGENTS.md text (Q65)
**Hard rule 4 → replace with:**
> 4. **Propose, don't populate, for Tier 2.** Domain claims, decisions David has not yet taken, rule changes and client-facing content enter 10–40 only after David confirms. Tier 0 and Tier 1 changes follow "Review tiers" below. Every factual claim cites a source or is tagged `unverified`.

**The bullet "No commit without a Codex pass, ever (Q40)" → replace with:**
> - **Review tiers (D-cowork-10, Q55).** Tier 0 (handoff bookkeeping, frontmatter/link/format fixes, Inbox captures, lint file moves): deterministic checks only. Tier 1 (briefs, drafts, specs, skills, eval scripts, runtime code outside the security boundary, notes in 10–40 with no Tier 2 claim, and recording David's answers, where Codex checks they were recorded faithfully): Codex pass against `90 System/codex-review-checklist.md`, then commit. Tier 1 notes in 10–40 carry `review_status: codex-reviewed`. Tier 2 (domain claims, decisions David has not yet taken, rule changes, client-facing, security-boundary code, `unverified`, Codex `escalate`): Codex pass and David's batched approval. When in doubt, the higher tier; Codex may raise a tier, never lower it. The deterministic pre-commit check runs on every commit; **until it is installed, Tier 0 also gets a Codex pass.** While Codex is unavailable, Tier 1–2 work waits uncommitted for one batched review. Calibration: David samples 1 in 5 Tier 1 commits until agreement is at least 90% over 20 samples, then 1 in 10.

**"Review failures (D72)" → add after its first sentence:**
> Only `blocker` findings fail a review; `should-fix` and `nit` findings are logged in the brief and do not trigger another round.

**"Lanes" → add:**
> The lead may run read-only subagents in parallel; only the lead writes files in a run.

**The handoff bullet ("Cowork lists its uncommitted changes…") → replace with:**
> - Cowork lists its uncommitted changes in `90 System/handoff.md`; the lead commits Tier 0 entries together as one bookkeeping commit and Tier 1–2 entries each as their own commit, then clears the entry.

### Approved conforming edits (Q68 (a), David 6 Oct 15:45)
Verbatim from the lead's Q68 entry (session 28), which David approved as option (a); in AGENTS.md "you/your" reads "David/David's".
> (1) "**Review before commit.** The lead runs Codex read-only on every diff the review tiers send to it (Tier 1–2 always; Tier 0 until the pre-commit check is installed) against these rules and records its findings in the brief." (rest of the bullet unchanged); (2) ingest: "…propose the pages to create or update, and wait for your approval of Tier 2 content (Tier 0–1 pages follow Review tiers); then write, update `index.md` and append to `log.md`." Query: "…propose it as a note (classification and sources included); file it after you confirm if it is Tier 2, otherwise under Review tiers."

## Outcome
**6 Oct (session 28), lead `claude-opus-5-5`, reviewer Codex `gpt-6.1-sol` (review profile), high, read-only.** The lead applied the approved text to AGENTS.md (provisional ID renumbered D77), with a PROGRESS decision row, a `log.md` mapping entry and the checklist set to `approved`. **Review FAIL; nothing committed.** Codex confirmed all five edits match the approved text word for word, but found (1) the existing "Review before commit" bullet still sends *each* diff to Codex, which contradicts Tier 0 once the pre-commit check exists; (2) the existing Wiki-operations lines on ingest and query still require David's confirmation for every note, which leaves Tier 1's "Codex pass, then commit" ambiguous; (3) the lead's log entry said "only" some categories reach David, omitting `unverified`, `escalate` and calibration samples. (1) and (2) need AGENTS.md wording David has not approved (hard limit), so they are **Q68** in for-david; (3) is the lead's own wording, to fix when the change lands. The lead restored AGENTS.md, PROGRESS, `log.md` and the checklist to their committed state, so no unapproved rule text sits in the working tree; D77 is not assigned yet. **Next run:** once Q68 is answered, apply the approved text plus the Q68 answer in one diff, assign the D-number, set the checklist to `approved`, review, commit.

**6 Oct (session 29), lead `claude-opus-5-5`, reviewer Codex `gpt-6.1-sol` (review profile), high, read-only.** After Q68 (a), the lead applied the Q65 text and the two Q68 edits to AGENTS.md in one diff, word for word (lines wrapped in AGENTS.md style; provisional ID renumbered **D77**), set the checklist to `review_status: approved`, added the D77 row to PROGRESS and the mapping to `log.md` (session 28's finding (3) fixed: the log names every route to David). Review: see below. Still open under this brief, held by the 6 Oct hold: the pre-commit check (§3), `90 System/reports/review-calibration.md`, and the `~/.codex` prompt. Review round 1 **PASS** (every AGENTS.md change matches the approved text after line wrapping; no other change). Should-fix applied: quoted `models:` entries, ticked the first two Done-when items; Q68's row is cleared at this run's close.
