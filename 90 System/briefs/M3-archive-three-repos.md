---
classification: internal
task: M3
owner: "@code"
status: done   # lead, 7 Oct (session 30): steps 1–5 done; D78
models: ["claude-opus-5-5 (Cowork, draft; lead)", "gpt-6.1-sol (Codex consult, high)"]
created: 2026-10-06
---
# M3 · Archive ui-design-agent, claude-blueprint and agentic-ios-app

## Goal (one sentence)
Take three inactive repos out of `~/Work` and out of active use on GitHub, reversibly and without losing anything.

## Why (David, 6 Oct, via Cowork, Q66)
They are not part of the second-brain work. Archiving keeps `~/Work` down to live projects. Q66 = local move **and** GitHub archive.

## Facts checked by Cowork (6 Oct, read-only)
- No live reference to the three in the vault or `dbrain-runtime`; only dated history (log, PROGRESS, M1/M2 briefs, handoff notes). Leave those as they are.
- M1 gate: all three were 0 ahead / 0 uncommitted on 6 Oct (ui-design-agent `d4dfc44`, claude-blueprint `3ed6463`, agentic-ios-app `fac922b`). Q58: the ui-design-agent patient fixture is invented (David).
- Not checked (Cowork can't see it): `~/.claude`, `~/.codex`, VS Code, launch agents, symlinks into `claude-blueprint`.

## Steps
1. **Pre-flight, per repo:** `git --no-optional-locks status --short` empty and `@{u}..HEAD` = 0. Anything else → stop, queue for David (D68), do not commit on his behalf.
2. **Reference check, named files only:** `grep -n` for the three names and their `~/Work/...` paths in these configuration files, where they exist: `~/.claude/settings.json`, `~/.claude/settings.local.json`, `~/.claude/CLAUDE.md`, `~/.codex/config.toml`, `~/.codex/*.config.toml`, `~/Library/LaunchAgents/*.plist`, both repos' `.claude/settings*.json`, and VS Code's `~/Library/Application Support/Code/User/settings.json` and `.../User/globalStorage/storage.json` (recent workspaces). **Never read** `~/.codex/auth.json`, session or history folders, or any credential store. Symlinks: `find ~/Work -maxdepth 3 -type l` and `find ~ -maxdepth 1 -type l`, which lists no folder's contents and never enters `~/Archive` (data policy v0.5). Any live hit other than dated history or dead `settings.local.json` entries → stop and queue it. **Amended 7 Oct (Q71 (a), David):** the 13 dead `Read`/additional-directory lines for the old ui-design-agent paths (`~/Documents/UI-Design-Agent/...`, `~/dev/ui-design-agent/...`) in `~/.claude/settings.json` are also exempt: the paths are absent and none points at `~/Work/<name>`. Do not edit that file (hard limit). Any *other* hit still stops the run.
3. **Move:** each to `~/Work/_archive/<name>` (target-absent and real-parent check first, as in M2). Verify: source gone, target present, `git fsck --full` exit 0, HEAD unchanged.
4. **GitHub:** `gh repo archive <owner>/<name> --yes` for each (reversible with `gh repo unarchive`). Confirm with `gh repo view <owner>/<name> --json isArchived` for each. This is a remote change: David approved it in Q66; it still goes through the permission prompt.
5. **Record:** Outcome below (before/after heads, gh results), a PROGRESS decision row (final D-number), `log.md`, handoff note.

## Files in scope
This brief; `log.md`; PROGRESS; TASKS; OPEN_QUESTIONS (its "Updated" line only; added 7 Oct by the lead, per Cowork's committed 09:55 handoff note "close records (PROGRESS, TASKS, OPEN_QUESTIONS)"); `90 System/handoff.md`; `90 System/for-david.md` (clear Q66, cleared 6 Oct; and Q71, 7 Oct). Outside the vault: the three folders' location only. No edits inside the three repos.

## Done when
- [x] Three folders in `~/Work/_archive/`, fsck clean, heads unchanged.
- [x] All three `isArchived: true` on GitHub.
- [x] No live reference left (step 2 output recorded; the 13 exempt Q71 lines and 7 VS Code history entries remain, both outside the rule).

## Constraints
No deletion, no force-push, no commit inside the three repos. Reversible only.

## Review
**Lead review of Cowork's entry (Q65, Q66, this brief, handoff block), 6 Oct (session 28), Codex `gpt-6.1-sol` (review profile), high, read-only.** Round 1 FAIL on this brief: (1) `find ~ -maxdepth 3` would traverse `~/Archive/medispring-infi`, which data policy v0.5 forbids agents to list; (2) a recursive `grep` over `~/.codex` would read its credential store (`auth.json`). Should-fix: name the repository in `gh repo view`; include VS Code in step 2; and, in the handoff, the BENCH check (`--help` doesn't load `dev.json`), the committed M2 follow-up row, and the old block's "no push beyond M2" line. The lead fixed step 2 (named files only, no credential stores, no traversal into `~/Archive`) and step 4 here; the handoff points go in the lead's close note.

**Lead review of Cowork's Q71 entry (this brief's status, step 2 amendment and 7 Oct note; for-david Q71; handoff note), 7 Oct (session 30), Codex `gpt-6.1-sol` (review profile), high, read-only, Tier 1:** PASS, no findings. The first call hung (no output after 41 minutes, 0% CPU; stdin was left open) and was killed; the rerun with stdin closed and a 15-minute cap passed. Committed `a0e0726`.

**Close records (session 30), Codex `gpt-6.1-sol` (review profile), high, read-only, Tier 1.** Round 1 FAIL. Blocker: OPEN_QUESTIONS changed but was not in Files in scope, and scope still said "clear Q66" (fixed above, citing the 09:55 handoff note). Should-fix, logged, not applied: D77 says changed Tier 1 notes in 10–40 carry `review_status: codex-reviewed`; PROGRESS, TASKS and OPEN_QUESTIONS have never carried it, so whether tracking files fall under that line goes to Cowork. Nit, applied: "out of `~/Work`" now reads "out of `~/Work`'s top level".
Round 2 PASS: round 1 findings resolved or logged; one nit (extra blank line at end of file) applied.

## Outcome
**6 Oct (session 29), lead `claude-opus-5-5`. Stopped at step 2 (its stop rule); nothing moved, nothing archived on GitHub.**
- **Step 1 pre-flight: PASS.** ui-design-agent `d4dfc44` (branch `claude/design-system-scaffold-RvDiy`), claude-blueprint `3ed6463` (`feature/new-branch`), agentic-ios-app `fac922b` (`main`): working trees clean, 0 ahead; every local branch tracks an upstream with nothing ahead; no stashes. GitHub repos: `David-T13Consulting/UI-Design-Agent`, `CLAUDE-Blueprint`, `agentic-ios-app`.
- **Step 2 reference check: hits.** `~/.claude/settings.json`: 13 lines, `Read(...)` allow rules and additional directories for `~/Documents/UI-Design-Agent/...` and `~/dev/ui-design-agent/...`. VS Code `globalStorage/storage.json`: 7 lines, recent-workspace entries for `~/Documents/CLAUDE-Blueprint`, `~/Documents/UI-Design-Agent`, `~/dev/claude-blueprint`. All other named files: 0 hits (both `~/.codex` profiles, `~/.claude/settings.local.json`, the vault's `.claude/settings*.json`, VS Code `settings.json`, 7 launch agents). No symlinks in `~/Work` (depth 3); `~` depth 1 only `Google Drive`. Every referenced path is absent on disk (moved by M1/M2), and none points at `~/Work/<name>`, so the move would not change them.
- **Consultation (D74), Codex `gpt-6.1-sol` (review profile), high, read-only:** asked whether these are "live hits" under step 2's rule. Advice: **STOP**. The `~/.claude/settings.json` entries are permission grants in active user-level configuration; they are ineffective while the paths are absent, but the brief's exception covers only `settings.local.json`. The VS Code entries can count as history. The lead followed the advice: no edit to the settings file (hard limit), M3 `blocked-on-david`, **Q71** in for-david.

**7 Oct, Cowork: Q71 answered (a) by David.** Run M3 as written with the step 2 exemption above. David tidies `~/.claude/settings.json` himself later, or approves an exact diff. The lead re-runs step 2 first and stops on any hit not in the Outcome list above.

**7 Oct (session 30), lead `claude-opus-5-5`. M3 done; Q71 recorded here and cleared from for-david.**
- **Step 1 pre-flight (re-run): PASS.** Same heads as session 29, working trees clean, every local branch tracking its upstream with nothing ahead, no stashes; `~/Work/_archive/<name>` absent for all three.
- **Step 2 reference check (re-run): no hit outside the session 29 list.** `~/.claude/settings.json` 13 lines (exempt, Q71 (a); not edited); VS Code `storage.json` 7 recent-workspace entries (history); every other named file 0 hits (`~/.claude/CLAUDE.md` absent; `dbrain-runtime` has no `.claude/settings*.json`). Symlinks: none in `~/Work` (depth 3); `~` depth 1 only `Google Drive`. The four old paths are still absent.
- **Step 3 move: PASS.** `mv` to `~/Work/_archive/<name>` after the target-absent and real-parent check. Source gone, target present, `git fsck --full` exit 0, HEAD unchanged: ui-design-agent `d4dfc448e878daf8ad446b0bc0cbf970cad4374d`, claude-blueprint `3ed646326f7dfd541ac02e7b3b77109781bc3536`, agentic-ios-app `fac922b552af4707be9b320c1ee3d649b2f2209f`. `~/Work` now holds `CLAUDE.md`, `Dbrain2`, `dbrain-runtime`, `_archive`, `_external`, `_snapshots`.
- **Step 4 GitHub: PASS.** Before: `David-T13Consulting/UI-Design-Agent`, `CLAUDE-Blueprint`, `agentic-ios-app` all `isArchived=false`, private. `gh repo archive --yes` exit 0 for each; after: all three `isArchived=true`. Reversible with `gh repo unarchive`.
- **Step 5 record:** this Outcome, PROGRESS D78 and session 30, `log.md`, TASKS, OPEN_QUESTIONS, for-david (Q71 cleared), handoff note. No deletion, no force-push, no commit inside the three repos.
