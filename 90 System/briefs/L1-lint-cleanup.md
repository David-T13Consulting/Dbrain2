---
classification: internal
task: L1 (provisional; lead assigns the final ID)
owner: "@code"
status: done   # phases 0–1; phases 2–6 superseded
models: ["claude-opus-5-5 (lead, phases 0–1)", "gpt-6.1-sol (review)"]
created: 2026-10-06
---
# Clean up after the 5 Oct lint, and move both repos off iCloud

> Written by Cowork, 6 Oct 2026, at David's request ("a detailed plan for Claude Code to clean up this mess"). Source: the lint entry `## [2026-10-05] lint | weekly` in `log.md`. David answered §0 on 6 Oct (Cowork recorded the answers). **Held by David's 08:57 directive (handoff.md): only Phases 0–1 may run. Phase 0 is done, and Phase 1 was done except the parked items (lead, 6 Oct). Phases 2–6 wait for David to lift the hold; Phase 2 needs him present. Phase 3 also waits for D-b.** Phases 0–1 only; see the superseded section.

## Goal (one sentence)
Make the tracking files match what git actually says, fix every lint finding David approves, and move `Dbrain2` and `dbrain-runtime` out of iCloud-synced `~/Documents` before iCloud damages either repository.

## Why the iCloud move is urgent (evidence, 5 Oct)
- `.git/objects` holds 12 sync-conflict copies named `<hash> 2`, and they can't be read ("Resource deadlock avoided" = iCloud has evicted the file, Optimize Mac Storage). `git fsck --connectivity-only` is still clean, so nothing is lost **yet**.
- Mechanism: iCloud syncs file by file and doesn't know what git is. It can (a) evict object, index or pack files, so git sees errors mid-command; (b) create `X 2` copies when a file is rewritten while an earlier version is still syncing; (c) sync a half-written `index` or `index.lock` to another Mac. Any one of these can corrupt the repo silently. Only the lead commits (D63), but it commits in fast bursts (four commits in the same second on 6 Oct), and Cowork and the lead write vault files at the same time. Both make race (b) more likely.
- The off-site copy is stale: `origin/master` on GitHub is at 1 Oct, **43 commits behind on 5 Oct, 50 on 6 Oct**. Today the only other copy is iCloud itself, which is the thing causing the damage.
- Data policy: iCloud is an external processor holding every note, including the wave-1 kids' logistics. Wave 2 (D69) needs "cloud agents provably unable to reach the files" and a tested deletion rule covering backups. A vault inside iCloud Drive can't meet either.

## §0 Decisions for David (answers recorded here by Cowork)
| # | Decision | Recommended | Answer |
|---|---|---|---|
| D-a | Where the repos go | **A: `~/Work/Dbrain2` and `~/Work/dbrain-runtime`** (outside every iCloud-synced folder). Alternatives: B `.nosync` rename plus a symlink at the old path; C keep the working tree in iCloud and move only `.git` out | A, `~/Work` (David, 6 Oct) |
| D-b | Backups after the move | Time Machine (local, hourly) **plus** a push to the private GitHub remote at the end of every lead run. Pushing is a hard limit, so this needs either David's OK each time or an AGENTS.md change (David's own edit) | **Open.** David has no Time Machine and asked whether GitHub alone is enough. Cowork's answer and proposal are in Phase 3 |
| D-c | Strip the §3a details the lead held back: the regional contact details in the waste note and the identifying uniform detail in the scouts note | Yes | Yes (David, 6 Oct) |
| D-d | `.claude/settings.local.json` (allows `git add *`, `git commit *`, Codex exec) | Add to `.gitignore`. It's per-machine; the shared rules live in `settings.json` | Yes (David, 6 Oct) |
| D-e | AGENTS.md: rename `D-cowork-9` to `D74` on line 81 (hard limit: AGENTS.md) | Yes, exactly that one-token diff | Yes, exactly that diff (David, 6 Oct) |
| D-f | index.md: add the 8 entries in Phase 4 (rule 8) | Yes, as worded there | Yes, as worded (David, 6 Oct) |
| D-h | Where the AI models live | Outside iCloud, not backed up | David, 6 Oct: they stay in `~/Library/Application Support/dbrain/models/` (not iCloud-synced); the SHA-256 manifest in git is their backup (M1) |
| D-g | Glossary entries for Tailscale, LTHR, four-axis classification, personal-data waves, token handling (rule 8: definitions are structured knowledge) | Lead drafts, David approves the wording before commit | Yes: lead drafts, David approves the wording (David, 6 Oct) |

## Files in scope (agent may touch only these)
- `90 System/handoff.md`, `90 System/for-david.md`, `90 System/briefs/P2.2.md`, `90 System/briefs/L1-lint-cleanup.md` (this file), `90 System/lint-checklist.md`
- `10 Projects/AI Second Brain/` : `PROGRESS.md`, `TASKS.md`, `CLAUDE.md`, `CAPTURE.md`, `README.md`, `memory/projects/ai-second-brain.md`, `memory/glossary.md`, `06_Delivery_Plan_S2-S6.md`
- `index.md`, `log.md`, `.gitignore`
- `AGENTS.md` **only** for the D-e diff, and only after David approves it
- `00 Inbox/2026-10-05-1232-household-waste-collection-2026.md`, `00 Inbox/2026-10-05-1235-child-a-scouts-2026-27.md` **only** for the D-c deletions
- Phase 2 path updates: every vault file that contains `~/Documents/Dbrain2` or `~/Documents/dbrain-runtime` (list them in Outcome first), `.claude/settings.json` (paths only), and in `dbrain-runtime` the files that hard-code those paths
- Outside both repos, **with David present**: Obsidian's vault list, the login item `Ask Brain.command`, Claude Code and Codex config paths. Cowork's connected folder and the claude.ai project instructions are changed by David

## Inputs / context to read first
`AGENTS.md` (multi-agent rules, hard limits) · `log.md` lint entry of 5 Oct · `90 System/handoff.md` (both lead sections) · `git log --oneline -25` · this brief

---

> **Phases 0–1 below are historical** (done in sessions 20–21). Their freeze and queue instructions no longer apply; the current hold and release are in handoff.md.

## Phase 0 — Freeze and snapshot (no approval needed; read-only plus one file outside the vault)
1. No autonomous run ("pick up the loop") until Phase 2 is done. Cowork doesn't edit vault files during Phases 0–2 (David tells the other Cowork sessions).
2. Make every file local: in Finder, right-click `~/Documents/Dbrain2` and `~/Documents/dbrain-runtime` → **Keep Downloaded**. Check: `find ~/Documents/Dbrain2 ~/Documents/dbrain-runtime -flags +dataless | wc -l` must print `0`. If it doesn't: `find … -type f -exec cat {} + > /dev/null` forces the download; check again.
3. Health check, both repos: `git fsck --full` (record the output in Outcome). Expected: dangling blobs at most, no `missing`/`corrupt`.
4. The 12 `* 2` files: for each one, `cmp "<hash> 2" "<hash>"`. Record "identical" or "differs". Delete nothing (hard limit). (Superseded: the move now uses `mv` (M2), so they travel along and are removed at clean-up.)
5. Snapshot outside iCloud: `git bundle create ~/Work/_snapshots/Dbrain2-2026-10-06.bundle --all` and the same for `dbrain-runtime`; `git bundle verify` both. Also copy the **uncommitted** files listed by `git status --porcelain` into `~/Work/_snapshots/uncommitted-2026-10-06/`, keeping their paths.

**Done when:** 0 dataless files, fsck output recorded, both bundles verified, uncommitted copies made.

## Phase 1 — Reconcile tracking with git, then commit the queue (still at the old path)
The uncommitted work is what's most at risk, so it is committed **before** the move.
1. **handoff.md.** For each queue entry, compare its files with git: `git diff --quiet HEAD -- <files>` plus the commit log. Q45 (`c56bd74`), Q46 (`d4fae04`) and Q54 (`377757e`) look committed already. Confirm, then remove those rows and fix the entry count. Mark the lead's "session 19 … nothing committed" section superseded by session 20, with a pointer to `4b5e91f`. Don't delete it (audit trail).
2. **PROGRESS.md.**
   - Keep the uncommitted session 19 entry; add one line: "Superseded the same evening: session 20 passed round Q and committed P2.2 (`4b5e91f`, runtime `c8b3b7b`)."
   - Add the missing **session 20** entry: rounds P–Q, Q53 accepted risks, the commits.
   - Add a **D74** row to the decision log: second pair of eyes when stuck (Q45), the "pick up the loop" trigger (Q52), accepted risks don't block (Q53), as committed in `c56bd74`.
   - D71 is committed with the captures (`b7db7da`); leave it as it is.
   - Fix "Current state": header date/session, **Phase** "S1 closed, S2 under way", **Schedule** "dated S2–S6 plan exists, proposed (`f9c014e`)".
3. **P2.2 brief:** `status: done`, Outcome = `4b5e91f` / `c8b3b7b`. **TASKS.md:** tick P2.2 (✅ 5 Oct).
4. **AGENTS.md (D-e, only if David approved it):** `D-cowork-9` → `D74` on line 81. Nothing else in that file.
5. **D-c deletions (only if approved):** remove the regional contact details from the waste note and the identifying uniform detail from the scouts note (the lead's 5 Oct flags name them). Replace each with nothing, not with a placeholder. Then the four wave-1 captures can be committed as their handoff entries describe.
6. **Q13–Q17 wording** (held since session 15): change Q13 to "redaction declined by David", as the lead asked.
7. Commit in this order, each after its Codex pass: bookkeeping (1–3, 6) → AGENTS diff (4) → wave-1 captures (5) → the remaining handoff entries (Q47–Q51, Q55 drafts, briefs P2.5/P3.0/P4.1, D-cowork-10, codex-review-checklist, course-map procedure, lint log entry). Use the suggested messages. Split handoff-only edits from content entries, as the lead asked.

**Done when:** `git status --porcelain` lists only `.claude/settings.local.json` and the parked items documented in handoff.md; handoff queue is empty or contains only items David still holds; PROGRESS shows session 20 and D74.

## Phases 2–6: superseded 6 Oct (Cowork)
- **Phase 2 (the move)** → [[90 System/briefs/M1-backup-push|M1]] (commit and push every repo) and [[90 System/briefs/M2-move-and-repoint|M2]] (move to `~/Work` with `mv -n`, re-point the paths; needs David present). These replace the clone-and-rsync method: on the same disk, `mv` is a rename that keeps `.git` and the uncommitted work intact.
- **Phase 3 (backups)** → GitHub push in M1. An independent backup (Backblaze) and Obsidian on the iPhone are parked by David.
- **Phases 4–6 (lint fixes, out-of-date statements, lint re-run)** → a new brief, written by Cowork after M2, in the new location. One brief per commit batch, as AGENTS.md requires.
- **Scope of this brief is therefore Phases 0–1 only.** Phase 0 is done (lead, session 20). Phase 1 is done: B1 was committed as `1c5038c` (session 21). This brief is `done` once it's committed.

## Constraints (vault rules that especially apply)
- Hard limits (AGENTS.md): no AGENTS.md edits beyond D-e, no deletions, no push, no permission-setting changes, no login-item or launch-agent changes without David present and agreeing at that moment.
- Never overwrite another agent's uncommitted work: Phase 1 commits it first.
- If any `fsck` shows `missing` or `corrupt`, **stop**: restore from the Phase 0 bundle and report. Don't attempt repair.
- If a `* 2` object file differs from its original, record it. Don't merge or delete.
- Retry limit and second-pair-of-eyes rule as in AGENTS.md.

## Review
Recorded in `90 System/handoff.md` (lead notes, sessions 20–22): B8 failed review in sessions 20 and 21; its findings were addressed by restructuring this brief into Phases 0–1 plus M1/M2. Reviewer Codex `gpt-6.1-sol`, high, read-only. Lead `claude-opus-5-5`.
## Outcome
Models: lead `claude-opus-5-5`; reviewer `gpt-6.1-sol` (high, read-only).
- Phase 0 (session 20): 0 dataless files; `git fsck --full` clean in both repos (dangling objects only, plus the 12 `* 2` names); all 12 `* 2` copies identical to their originals; bundles verified in `~/Work/_snapshots/`.
- Phase 1 (sessions 20–21): handoff reconciled; PROGRESS session 20 and D74; P2.2 `done`; AGENTS.md D-cowork-9 → D74 (`e00c4a4`); §3a details removed and the four wave-1 captures committed (`b7db7da`, `28d3697`, `88eef41`, `a53a6d7`); lint entry `0f81cac`; B1 bookkeeping `1c5038c`.
- Phases 2–6: superseded by M1 (done, session 22) and M2.
