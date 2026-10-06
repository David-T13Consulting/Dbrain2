---
classification: internal
task: M2 (provisional; lead assigns the final ID)
owner: "@code"
status: blocked-on-david   # Q63 (session 25): residual reachability of the medispring-infi archive
models: ["claude-opus-5-5 (lead)", "gpt-6.1-sol (review)"]
created: 2026-10-06
---
# Move the repos to ~/Work and re-point every path

> Written by Cowork, 6 Oct 2026. Runs only after [[90 System/briefs/M1-backup-push|M1]] has passed its gate. **`blocked-on-david`:**
> - David must be at the Mac;
> - Cowork sets the status to `open` when he says so;
> - then David says "pick up the loop".
>
> Decisions behind it, all David's on 6 Oct:
> - code root `~/Work` (single location; `~/dev` is absorbed);
> - projects go to `~/Documents/AI Projects/`;
> - the parked work moves uncommitted;
> - models stay out of iCloud.

## Goal (one sentence)
All git repos live in `~/Work`, outside iCloud, unchanged and with nothing lost, and every live path points there.

## Target layout
```
~/Work/                      (not iCloud)
  Dbrain2/   dbrain-runtime/   claude-blueprint/   agentic-ios-app/   ui-design-agent/
  _external/Equipe-5/
  _archive/agentic-hackathon/       (was ~/dev/Agentic hackathon, no git)
  _snapshots/                       (bundles from L1 Phase 0 and step 2 below)
~/Library/Application Support/dbrain/models/   stays put: not iCloud-synced, and the manifest is in git (M1)
```
`medispring-infi`: **archive** (David, 6 Oct; GitHub repo stays private). Move it as-is with `mv -n` to `~/Work/_archive/medispring-infi`; no commit, no clean-up, no agent access afterwards (no Cowork connection, never linked from the vault). Then `~/dev` is empty and is removed at clean-up.

## Files in scope
- **The moves:** the eight folders in step 3. Nothing else is moved.
- **Snapshot outputs (new files, outside both repos):** `~/Work/_snapshots/{pre,post}-move-<repo>-status.txt`, `~/Work/_snapshots/{pre,post}-move-<repo>-head.txt`, `~/Work/_snapshots/<repo>-<YYYY-MM-DD>.bundle`, `~/Work/_snapshots/uncommitted-<repo>-<YYYY-MM-DD>.tar`, and `~/Work/_snapshots/medispring-infi-files-{pre,post}.txt`. `<repo>` is one of the git repos moved here, never medispring-infi.
- **Path rewrite:** live config and docs that contain `Documents/Dbrain2`, `Documents/dbrain-runtime` or `Dbrain2-artifacts`. List them with `grep -rln` first and record the list under Outcome. Known places:
  - vault: `.claude/settings.json` (both the `~/…` and the `/Users/davidduchesne/…` forms), `90 System/{for-david, handoff, weekly-local-model-review}.md`;
  - briefs: T9-M6, MVP-phone, P2.2, L1, M1, this one;
  - `30 Resources/Local AI/sources.md`;
  - AI Second Brain: CLAUDE.md, README, PROGRESS (current state only), TASKS, OPEN_QUESTIONS, CAPTURE, `memory/context/stack.md`, `memory/projects/ai-second-brain.md`, the two `02_Architecture` result notes;
  - runtime: `README.md`, `mvp/README.md`, `run_dev_cases.py`, `measure.sh` and any other script;
  - `~/.codex` profile paths.
- **Closing records (step 8):** `log.md` (append one entry), `10 Projects/AI Second Brain/PROGRESS.md` (session entry, decision row), `10 Projects/AI Second Brain/TASKS.md`, `90 System/handoff.md` (Lead → Cowork note), `90 System/for-david.md` (queue entries), and this brief (status, models, Review, Outcome).
- **Not rewritten:** dated history, i.e. `log.md` entries, PROGRESS session entries, decision rows, `artifacts/*.stdout` evidence. Rewriting evidence falsifies the audit trail.
- **AGENTS.md:** contains no `~/Documents` path (checked 6 Oct), so it isn't edited.
- **`.claude/settings.json`:** the uncommitted `additionalDirectories` entry (not from this thread's Cowork; listed in handoff) names the old paths. David answered Q59 (a): Cowork removed it on 6 Oct. In step 5, add `additionalDirectories` for `~/Work/dbrain-runtime` and `~/Library/Application Support/dbrain` (approved by David as part of this path rewrite).
- `Dbrain2-artifacts` references become `~/Documents/Source_Material/AI Second Brain/`. Cowork moves that folder itself after this brief.

## Steps
0. **Run from `~/Work`, not from inside a repo** (Terminal, `cd ~/Work && claude`; pointer in `~/Work/CLAUDE.md`). A session started inside Dbrain2 or dbrain-runtime loses its working directory when the folder moves. Use absolute paths.
1. **Freeze (David):** quit Obsidian and VS Code, stop `Ask Brain.command` and the MVP service, close every other Claude Code, Codex and Cowork session.
2. **Pre-flight:**
   - `find ~/Documents/Dbrain2 ~/Documents/dbrain-runtime -flags +dataless | wc -l` must be 0. If it isn't, force the download (`find … -type f -exec cat {} + > /dev/null`) and check again.
   - For every moved git repo **except medispring-infi**, save `git status --porcelain` to `~/Work/_snapshots/pre-move-<repo>-status.txt` and `git log -1 --format=%H` to `pre-move-<repo>-head.txt`. For medispring-infi, record a filesystem-only listing instead: `find ~/dev/medispring-infi -type f | sort | wc -l` and `du -sk`, into `medispring-infi-files-pre.txt`. Never run git in it.
   - Refresh the bundles for Dbrain2 and dbrain-runtime, and tar their **uncommitted** files (`git status --porcelain` list) into `~/Work/_snapshots/uncommitted-<repo>-<date>.tar`. This refreshes the older Phase 0 copy in `uncommitted-2026-10-06/` and is the up-to-date copy of the parked work outside the working tree.
3. **Move with `mv -n`.** It's the same APFS volume, so `mv` is a rename and `.git` stays as it is. In this order:
   - agentic-ios-app, claude-blueprint, ui-design-agent;
   - `Agentic hackathon Team/Equipe-5` → `_external/Equipe-5`;
   - `Agentic hackathon` → `_archive/agentic-hackathon`;
   - `medispring-infi` → `_archive/medispring-infi` (only the move; its `.git` locks stay for clean-up);
   - dbrain-runtime, then Dbrain2.
   After each one, check that the source is gone and the target exists. `-n` skips silently on a name collision.
   The 12 `* 2` conflict copies in Dbrain2's `.git` move along; they're removed at clean-up.
4. **Gate per git repo (all except medispring-infi):**
   - `git fsck --full`: no missing or corrupt objects. The "bad sha1 file" lines for the `* 2` names are expected.
   - `git log -1 --format=%H`, saved to `post-move-<repo>-head.txt`, equals `pre-move-<repo>-head.txt` (`diff`).
   - `git status --porcelain`, saved to `post-move-<repo>-status.txt`, equals `pre-move-<repo>-status.txt` line for line (`diff`).
   - On any mismatch: stop, and move the repo back with `mv -n`.
   - **medispring-infi (filesystem check only):** the same file count and `du -sk` at the new path, saved to `medispring-infi-files-post.txt`. No git command.
5. **Rewrite the paths** per Files in scope. Then `grep -rn "Documents/Dbrain2\|Documents/dbrain-runtime\|Dbrain2-artifacts"` over both repos, `~/.claude`, `~/.codex` and `~/Library/LaunchAgents` may return only the dated history kept on purpose. List those hits under Outcome.
6. **Re-point the tools (David, with the lead's checklist):**
   - Obsidian → *Open folder as vault* `~/Work/Dbrain2`, then remove the old entry.
   - VS Code: reopen the folders and update any workspaces.
   - System Settings → Login Items: re-add `~/Work/dbrain-runtime/mvp/Ask Brain.command`.
   - The Shortcut needs no change (it calls the HTTP endpoint).
   - Cowork: connect `~/Work/Dbrain2` and `~/Work/dbrain-runtime`.
   - claude.ai project instructions: `~/Documents/Dbrain2/` → `~/Work/Dbrain2/` (Cowork drafts the text).
7. **Smoke test:**
   - runtime `python3 -m unittest discover -s tests -t .`;
   - `GET /health`;
   - one question from the iPhone (it must cite a note);
   - Obsidian shows today's notes;
   - `git status` and `git log -1` work from `~/Work/Dbrain2` (the commit in step 8 is the real write test).
8. **Record and commit (end of brief):**
   - a provisional decision row "Repos move to `~/Work`, off iCloud; models stay in Application Support; projects to `~/Documents/AI Projects/`" (the lead assigns the D-number);
   - a PROGRESS session entry, TASKS, a `log.md` entry and a "Lead → Cowork" note in `handoff.md`, all written **before** the review so they go into the commit.
   - Commit the path rewrite and the records: one commit per repo, each after a Codex pass.
   - Then push Dbrain2 and dbrain-runtime **once each**, no force-push. Approved by David on 6 Oct (Q60 (a)): one push of each repo at the end of M2, after the Codex pass.
9. **Stop.**

## After this brief (not the lead's)
- **Cowork:** move `~/Documents/Claude/Projects/*` and `~/Claude/Projects/Consulting` into `~/Documents/AI Projects/`, and `~/Documents/Dbrain2-artifacts/local-models` into `~/Documents/Source_Material/AI Second Brain/`. Don't touch `~/Claude` or `~/Claude/Scheduled`.
- **The rest of the lint clean-up** (index entries, capture template, out-of-date statements, lint re-run) gets its own brief in the new location.
- **Clean-up, each delete with David's OK:**
  - the empty old folders;
  - the `cowork-stale-index.lock` files and medispring's old stash lock;
  - the `* 2` files;
  - `Equipe-5/node_modules` and `.next`;
  - optionally the claude-blueprint `.venv`.
  Without delete permission, files go to a `_to_delete/` folder.
- **Last, after every clean-up (David, 6 Oct):** a pseudonym rule that replaces real names with Belgian comics characters. It needs its own brief, a data-policy amendment (§3a bans nicknames today), an alias key kept outside the vault, and a lint check for real names. Cowork drafts it.
- **Parked by David:** Obsidian on iPhone (the phone loses vault access until he chooses; Obsidian Sync is recommended) and an independent backup (Backblaze recommended).

## Constraints
- Hard limits: AGENTS.md, login items, deletions and anything touching medispring-infi each need David's yes at that moment.
- Never commit the parked work to get a clean tree.
- An fsck error **other than** the expected `bad sha1 file` lines for the `* 2` names means stop and report. Restore committed history from the bundle and the parked uncommitted work from the step 2 tar; bundles don't hold uncommitted files.

## Review
- **Brief review, session 23, round 1 (Codex `gpt-6.1-sol`, high, read-only): FAIL.** Blockers: `log.md` and the other closing records weren't in Files in scope; step 4 compared status alone against a pre-move file that also held the hash. Should-fix: "only copy" of the parked work ignored the Phase 0 copy; the handoff note came after the commit; L1 lacked model IDs; for-david's summary still called Q60 new. All fixed by the lead (separate status and head files, closing records listed, note moved before review).
- **Round 2: PASS**, committed `fa1a0f9`. Two should-fixes, recorded under Outcome.
- **Amendment review, session 24 (Codex `gpt-6.1-sol`, high, read-only): FAIL, not committed.** Reviewed: Cowork's 6 Oct amendment (status comment, steps 0–1: lead in VS Code with only `~/Work` open; the handoff header's session-location line). Blockers: (1) with the lead's workspace at `~/Work`, step 3 puts medispring-infi (`_archive/medispring-infi`) inside it, against "no agent access afterwards" and data-policy §7 (a location alone is not proof of unreachability) → **Q62**; (2) step 1's "check with David" bypasses the single front door (D68): route the freeze confirmation through Cowork and record it before step 2. Should-fix: "Leave the moved folders alone in VS Code until the end" conflicts with step 6 reopening them, so name the endpoint; append the revised Q61 answer to Outcome rather than overwrite the Terminal record; limit the reviewer exception to the lead-invoked, read-only `codex exec --profile review`. No secrets, client content or third-party personal data in the diff.
- **Amendment review 2, session 25 (Codex `gpt-6.1-sol`, high, read-only): FAIL, not committed.** Reviewed: Cowork's reworked amendment (Q62 (a) `~/Archive`, reachability check, freeze via Cowork, should-fixes; for-david Q62/Q56; handoff header). Resolved: the D68 blocker and all three session 24 should-fixes. Blockers: (1) the reachability check (location plus a `grep "Archive"` over some settings files) does not prove unreachability: it misses ancestor grants, inherited or command-line permissions, Codex and Cowork access, symlinks; require a check of effective reachable roots that fails closed; (2) "no agent access afterwards" conflicts with step 4's agent-run filesystem check at the new path and with "locks stay for clean-up": David runs the post-move check, the archive is excluded from agent clean-up, any deletion needs fresh approval via D68. Should-fix: the Goal says all git repos live in `~/Work` (medispring-infi exception); for-david's summary still calls Q62 open. **Lead fixes, in the working tree, not yet re-reviewed:** blocker 2 and both should-fixes; for blocker 1, a proposed fail-closed check of configured roots (realpath, ancestors, Claude Code, Codex, Cowork), not yet re-reviewed. **Its remainder is David's call (Q63):** the lead and Codex run as his user with shell access, so no configuration check proves they are blocked, and §7 requires that now (P1.3 only schedules the verification). Options: split medispring-infi off M2, a temporary §7 exception under §8, or verified enforcement first.
- **Close review 1, session 25 (same reviewer): FAIL.** Reviewed: the lead's close records (Q63, PROGRESS, TASKS, log, handoff note, this brief's Review/Outcome) with Cowork's Q62/Q56 answers. Blockers: Q63 option (b) overstated the protection (Claude Code's sandbox and deny rules are not equivalent, and cover neither Codex nor Cowork); Q63 presented a temporary §7 exception as plain risk acceptance, while §8 requires David's decision in PROGRESS and a policy version bump. Should-fix: drop "the move doesn't make it worse"; clear Q62 from Answered; call the configured-roots check proposed and not re-reviewed. All fixed: Q63 reframed with split-off (recommended), §7 exception under §8, or verified enforcement for every agent and route.
- **Close review 2: FAIL (bookkeeping).** Q63 blockers resolved. Blocker: this brief didn't record close review 1 or count it. Should-fix: the revised Q61 line said the Terminal record is "above" (it is below); PROGRESS pointed to a review result it didn't give. All fixed.
- **Close review 3:** the review this commit carries; its verdict is in the commit message.
## Outcome
- **Cowork, 6 Oct (after session 24):** Q62 answered (a): archive at `~/Archive/medispring-infi`. Freeze confirmed by David via Cowork: the Claude desktop app, the ChatGPT app, Obsidian and the MVP service off; VS Code with only `~/Work`; the ChatGPT background helper and the idle Codex app-server accepted by David. **Q61, revised answer** (appended; the Terminal record below stands as history): no `claude` CLI is installed, so the lead runs in VS Code with `~/Work` as its working folder.
- **Session 23 (6 Oct):** models: lead `claude-opus-5-5`; reviewer Codex `gpt-6.1-sol` (high, read-only). Not started. The step 1 freeze is not met. Obsidian and the MVP service (port 8765) were stopped, but VS Code, the Claude desktop app and the ChatGPT/Codex app were running, and the lead itself runs inside VS Code with `~/Documents/Dbrain2` as its working folder. Queued as **Q61**; nothing moved, no snapshot written. **Q61 answered by David via Cowork (6 Oct):** the lead runs M2 in Terminal from `~/Work` (step 0, pointer `~/Work/CLAUDE.md`), with absolute paths; the vault's `.claude/settings.json` doesn't load from there, so expect permission prompts. Cowork set the status back to `open`. Should-fix from brief review round 2, to apply when M2 runs: the intro (line 11) and status must agree; L1's D-b row still points to the removed Phase 3 (L1 is closed; fix it in the lint follow-up brief).
- **Session 24 (6 Oct):** models: lead `claude-opus-5-5`; reviewer Codex `gpt-6.1-sol` (high, read-only). Run from VS Code with `~/Work` as the working folder (Cowork's amended step 0, uncommitted; the committed step 0 still says Terminal). Cowork's amendment to steps 0–1 failed review (see Review), so it stays uncommitted and **M2 did not start: nothing moved, no snapshot written.** Freeze state, checked read-only by the lead, not confirmed with David: Obsidian, the Claude desktop app, the ChatGPT app and the MVP service (port 8765) not running; a ChatGPT background helper (running since 23 Sep) and the VS Code Codex extension's idle app-server running; no process held files in either repo. Status `blocked-on-david` on Q62. Session 23's should-fix (intro line 11 vs status) is still open.
- **Session 25 (6 Oct):** models: lead `claude-opus-5-5`; reviewer Codex `gpt-6.1-sol` (high, read-only). Run from VS Code with `~/Work` as the working folder. Cowork's reworked amendment failed review 2 (see Review); the lead fixed what it could and queued **Q63** (residual reachability). **M2 did not start: nothing moved, no snapshot written.** Status `blocked-on-david` on Q63. Reviews of this brief in session 25: 4 of 5 (amendment review 2, close reviews 1–3).
