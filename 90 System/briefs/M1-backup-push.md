---
classification: internal
task: M1 (provisional; lead assigns the final ID)
owner: "@code"
status: done   # gate met 6 Oct (session 22)
models: [claude-opus-5-5, gpt-6.1-sol]
created: 2026-10-06
---
# Back up every repo to GitHub before the move off iCloud

> Written by Cowork, 6 Oct 2026. This merges the folder-migration plan from David's other Cowork thread into the L1 clean-up (this thread is now the only one). **Approved by David on 6 Oct:**
> - push (hard limit, approved for this brief only);
> - the parked work moves uncommitted;
> - the leftover changes in the other repos must be committed;
> - medispring-infi is decided after Cowork's scan.
>
> Step 2 of the move, the move itself and the path rewrite, is brief [[90 System/briefs/M2-move-and-repoint|M2]], which needs David present. One brief per commit batch, because AGENTS.md says "commit only at the end of a brief".

## Goal (one sentence)
Every repo that moves has its committable work committed and pushed to a private GitHub remote, so that GitHub holds a complete copy before anything leaves iCloud.

## Snapshot Cowork took, 6 Oct 09:50 CEST (re-check in step 1)
| Repo (current path) | Branch | Uncommitted | Unpushed | Remote | Note |
|---|---|---|---|---|---|
| `~/Documents/Dbrain2` | master | 13 | **50** | origin (GitHub) | parked items listed in handoff.md stay uncommitted |
| `~/Documents/dbrain-runtime` | main | 8 | n/a | **none** | MVP-phone code, `make-shortcut.sh`, `t9_compare.py` stay uncommitted (parked) |
| `~/dev/claude-blueprint` | feature/new-branch | 7 | 0 | origin | 2 modified + untracked `agent_harness/`, `concepts/`, `evals/` (100 KB), `.claude/settings.json`, `.claude/settings.local.json`; `.venv` 9 MB already ignored |
| `~/dev/ui-design-agent` | claude/design-system-scaffold-RvDiy | 31 | 0 | origin | design-system components; no file over 1 MB |
| `~/dev/agentic-ios-app` | main | 0 | 0 | origin | nothing to do |
| `~/dev/Agentic hackathon Team/Equipe-5` | feat/liquid-glass-ui | 0 | 0 | third party | **never push** (not David's repo) |
| `~/dev/Agentic hackathon` | no git | | | | moves to `_archive` in M2 as is |
| `~/dev/medispring-infi` | main | 106 | 0 | origin | **out of scope**: wait for David's decision on Cowork's scan |

Stale `cowork-stale-index.lock` files sit in the Dbrain2, dbrain-runtime, medispring-infi and ui-design-agent `.git` directories (renamed by the other Cowork thread; git ignores them). medispring-infi also has `index.stash.39302.lock` from 26 Feb. Leave them all for the clean-up.

## Files in scope (agent may touch only these)
- **Added 6 Oct after session 21:** dbrain-runtime `models/MANIFEST.md` (new) and `.gitignore` (`.DS_Store`); ui-design-agent `MessagePreview.stories.tsx`, only as David's Q58 answer says.
- Dbrain2: the files of the B1 bookkeeping item in handoff.md (PROGRESS, TASKS, the P2.2 brief, `for-david.md`, `handoff.md`), this brief, `log.md`, and `index.md` (the brief's own catalog entry; added by the lead in session 22 after review).
- dbrain-runtime: `.gitignore` only (if the secret scan needs an ignore rule). No code.
- claude-blueprint: `.gitignore` (add `.claude/settings.local.json` and `.venv/`), plus the leftover files listed above, committed as they are.
- ui-design-agent: the 31 leftover files, committed as they are.
- GitHub: create **one** new private repo, `David-T13Consulting/dbrain-runtime`.

## Steps
**Steps 1–5 were done in session 21 (6 Oct), apart from the manifest: see Outcome. The original step list is in git history (handoff row) and the Outcome.** What remains, after David answers Q57 and Q58 in `for-david.md`:
1. **Model manifest (Q57, if (a)):** write `models/MANIFEST.md` in dbrain-runtime: model name, source URL, SHA-256 and local path for each model in `~/Library/Application Support/dbrain/models/` and for the T9 candidates. Take the hashes from the files, not from memory.
2. **ui-design-agent (Q58 = a):** David confirmed the fixture name is invented; the 31 files go into the commit as they are (no edit). Nothing is committed in this step; the commit is step 5.
3. **dbrain-runtime `.DS_Store`:** add `.DS_Store` to its `.gitignore`.
4. **Review:** one Codex pass over each repo's full diff. The pass checks scope, secrets **and the data policy** (§3/§3a: no real third-party or health data). On a fail, follow D72: fix and re-review, at most five reviews, then park.
5. **Commit and push, only now, at the end of the brief:** one commit per repo (dbrain-runtime: manifest + `.gitignore`; ui-design-agent: the 31 files on its branch), then push those branches. No force-push.
6. **Gate:**
   - every repo in scope shows `@{u}..HEAD` = 0;
   - uncommitted = 0, except the documented parked items (Dbrain2: Cowork briefs under review, the Q12 note; dbrain-runtime: the 7 parked MVP/T9 files).
   Record the counts under Outcome, set status `done`, add a "Lead → Cowork" note, and stop.

## Constraints
- Push only the branches named here. No force-push, no branch deletion, no history rewrite.
- Never push Equipe-5. Never touch medispring-infi.
- Any secret-scan hit, or a remote that isn't private, means stop and report. Don't fix by rewriting history.
- Don't read or copy `.env*` files anywhere.

## Review
Reviewer: Codex `gpt-6.1-sol` (review profile), effort high, read-only. Lead: Claude Code `claude-opus-5-5`. Every review checked secrets, client material and the data policy, not only scope (Codex's brief-review blocker 3).
| Item | Verdict | Notes |
|---|---|---|
| Step 2, B1 bookkeeping (Dbrain2) | PASS | 5 should-fix/nits, carried to the session close: TASKS Next action predated M1; session 19 "five failed reviews" (four failed, round L passed); Q13 and superseded L1 queue rows; Q55 row gate wording |
| This brief, M2 and L1 (handoff entry) | **FAIL** | Blockers: (1) M1 and M2 commit mid-brief, against "commit only at the end of a brief"; (2) step 4's model manifest is outside Files in scope, and the step order pushes before it; (3) "scope and secrets only" for steps 5–6 skips the data-policy check; (4) M2 asks David directly instead of via `for-david.md`. Should-fix: L1 parked-items Done-when, L1's stale clone claim and Phase 0–1 instructions, M2's fsck recovery path. Back to Cowork; not committed |
| Step 5, claude-blueprint leftovers | PASS | First pass strayed into ui-design-agent (prompt named it); re-run scoped to the repo. Should-fix: `.claude/settings.json` holds gh CLI permission rules (committed as the brief says) |
| Step 6, ui-design-agent leftovers | **FAIL** | Blocker: a Storybook fixture names a patient next to a prescription expiry; synthetic provenance unconfirmed (Q58). Not committed, not pushed |
| This brief, M2 and L1 (handoff entry), re-review in session 22 | **FAIL** | Prior findings 2–8 resolved; 1 still open here (step 2 said "commit", fixed in this brief). New blockers, all M2: push authorised migration-wide while M1's approval is "for this brief only" (Q60); `~/Work/_snapshots/` outputs not in Files in scope; medispring-infi is move-only but the pre-flight and gate inspect "every repo". Should-fix: M2 says seven folders, moves eight; L1 line 80 still points at M1 step 2 for B1; L1 is `done` with empty `models`, Review and Outcome. M2 and L1 back to Cowork, uncommitted; this brief is committed with the session 22 close |
| Remainder step 1+3, dbrain-runtime manifest + `.gitignore` (session 22) | PASS | Codex verified all four sizes and hashes against the files. Should-fix applied: B0 license `apache-2.0` from the model card at the pinned revision (the lead re-fetched it to confirm) |
| Remainder step 2, ui-design-agent 31 entries / 52 files (session 22) | PASS | Q58 fixture treated as decided. Should-fix, not applied (outside "as they are"): `.gitignore` covers `.env` and `.env.local` but not other `.env.*` variants. Noted, not blocking: an illustrative lab-result message addressed to David in `MessagePreview.stories.tsx` line 19; no sign it is a real record |

## Outcome
**Lead, 6 Oct (session 21).** Ran to the gate except ui-design-agent (Q58) and the manifest (Q57); status `blocked-on-david`.

Step 1 re-check, 6 Oct (vs. Cowork's 09:50 snapshot):
| Repo | Uncommitted | Unpushed | Difference |
|---|---|---|---|
| Dbrain2 | 14 | 50 | +1 untracked: M2 brief written after the snapshot |
| dbrain-runtime | 8 | no remote | same |
| claude-blueprint | 6 | no upstream | `feature/new-branch` had no remote branch; it sat on `origin/main` with no own commits. `.claude/settings.local.json` is already ignored by David's global git ignore, hence 6 not 7 |
| ui-design-agent | 31 | 0 | same |
| agentic-ios-app | 0 | 0 | same |
| Equipe-5, medispring-infi | not touched | | medispring-infi has no upstream on `main` (out of scope) |

Secret scan (`dbrain-runtime/secret_scan.sh`, self-test passed each time): clean on Dbrain2 `git log -p origin/master..master`, dbrain-runtime `git log -p --all`, and the leftover files of claude-blueprint (26) and ui-design-agent (52). No `.env*` file was read or copied.

Done:
- Step 2: B1 committed, vault `1c5038c` (its step-2 commit is the brief's own instruction).
- Step 3: Dbrain2 remote `PRIVATE`; pushed with the session close commit.
- Step 4: `David-T13Consulting/dbrain-runtime` created **PRIVATE**; `main` pushed (`c8b3b7b`), upstream set. Manifest not added (Q57).
- Step 5: claude-blueprint `.gitignore` + leftovers committed `3ed6463` on `feature/new-branch` and pushed (new remote branch); no merge, no branch deleted.
- Step 6: ui-design-agent not committed or pushed (Q58).

Gate, measured after the pushes:
| Repo | `@{u}..HEAD` | Uncommitted | Note |
|---|---|---|---|
| Dbrain2 | 0 after the close push (see handoff note) | 9 + `.claude/settings.json` | all documented: Cowork's failed or held briefs (L1, M1, M2, D-cowork-10, checklist, P2.5, P3.0, P4.1), the Q12 scaffold note, Cowork's new settings entry (not in the 10:05 release) |
| dbrain-runtime | 0 | 8 | 7 parked (MVP-phone code: `config.py`, `serve.py`, `sandbox-smoke.sb`, `mvp_smoke.py`, `tests/test_serve.py`, `mvp/`; `t9_compare.py`) + an undocumented `.DS_Store` (not ignored; `.gitignore` edits are limited to secret-scan needs) |
| claude-blueprint | 0 | 0 | |
| ui-design-agent | 0 | 31 | **gate not met**, Q58 |
| new repo visibility | `PRIVATE` | | |

No force-push, no branch deleted, no history rewritten. Equipe-5 and medispring-infi not touched. Commits were made at the close of the run except B1 (step 2).

**Lead, 6 Oct (session 22): remainder done, gate met; status `done`.** Lead `claude-opus-5-5`; reviewer Codex `gpt-6.1-sol` (review profile), high, read-only; each review checked scope, secrets and the data policy.
- Step 1 (Q57): `models/MANIFEST.md` written; the four SHA-256 values were computed from the files on 6 Oct and match the pins (T9 pre-download manifest for C1–C3, `t9_compare.py` for B0).
- Step 2 (Q58): the 31 entries (52 files) committed as they are, no edit.
- Step 3: `.DS_Store` added to dbrain-runtime's `.gitignore`.
- Secret scan (`secret_scan.sh`, self-test passed) clean on the exact files committed in both repos.
- Step 5: dbrain-runtime `6c7763e` on `main`, pushed (`c8b3b7b..6c7763e`); ui-design-agent `d4dfc44` on `claude/design-system-scaffold-RvDiy`, pushed (`02e8e6a..d4dfc44`). Both remotes `PRIVATE`. No force-push, no branch deleted, no history rewritten; Equipe-5 and medispring-infi not touched.

Gate (step 6), measured after the pushes:
| Repo | `@{u}..HEAD` | Uncommitted | Note |
|---|---|---|---|
| Dbrain2 | 0 before this close commit; pushed with it | 11 before this close | documented: Cowork's briefs and checklist (D-cowork-10, P2.5, P3.0, P4.1 and others under review), the Q12 scaffold note, Cowork's `for-david.md` and `handoff.md` edits |
| dbrain-runtime | 0 | 7 | the 7 documented parked items (MVP-phone code, `t9_compare.py`) |
| claude-blueprint | 0 | 0 | |
| ui-design-agent | 0 | 0 | |
