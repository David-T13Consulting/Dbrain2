---
classification: internal
task: Q77
owner: "@code"
status: done
models: [claude-opus-5-5 (lead), gpt-6.1-sol (review)]
source: "David's Q77 (a), via Cowork, 7 Oct (D91); Claude Code permissions docs, https://code.claude.com/docs/en/permissions (rule matching); git-push docs, https://git-scm.com/docs/git-push (what each push form does); both read 8 Oct 2026"
review_status: proposed
note_type: decision
created: 2026-10-08
updated: 2026-10-08
---
# Q77: wildcard deny list for force pushes (draft for David's OK)

## Goal (one sentence)
Replace the vault's prefix-only force-push deny rules with wildcard rules that also catch force, mirror, delete and `+` refspec pushes when an option sits after the remote or branch, or `git` carries `-C`/`-c` before `push`.

## Files in scope (agent may touch only these)
- This brief; [[90 System/for-david]] (Q79); `index.md` (one link); TASKS, PROGRESS, `log.md` at session close.
- **Not** `.claude/settings.json`: permission settings are a hard limit. The lead applies the list there only after David's OK of the exact text below, as its own Tier 2 commit.

## Inputs / context to read first
- D85, D86, D91 in PROGRESS; Q75 and Q77 (cleared, recorded in D86 and D91).
- What each push form does (forced `+` refspec, `--mirror`, `--delete`, empty-source `:ref` deletion, `--prune`): git-push documentation, https://git-scm.com/docs/git-push.
- How Claude Code matches Bash rules (permissions docs, read 8 Oct 2026): `*` matches any text, spaces included, at any position; `:*` works only at the end. A Bash rule matches the command text as written, so `Bash(git push *)` misses `git -C . push …`, `git -c … push …` and `git 'push' …`. Deny rules apply when **any** part of a compound command (`&&`, `;`, `|`, subshells, `$(…)`) matches. The docs warn that argument-constraining patterns are fragile.

## Proposed list (exact text for David's OK)
Thirteen rules. They replace the 12 current `deny` entries (all `git push --force`, `-f`, `--force-with-lease`, `--force-if-includes` prefixes, with and without `-C <repo>`); every one of them is covered below.

```json
"deny": [
  "Bash(*git*push*--force*)",
  "Bash(*git*push* -f*)",
  "Bash(*git*push* -uf*)",
  "Bash(*git*push* -vf*)",
  "Bash(*git*push* -qf*)",
  "Bash(*git*push* +*)",
  "Bash(*git*push*--mirror*)",
  "Bash(*git*push*--delete*)",
  "Bash(*git*push* -d*)",
  "Bash(*git*push* :master*)",
  "Bash(*git*push* :main*)",
  "Bash(*git*push* :refs/*)",
  "Bash(*git*push*--prune*)"
]
```

| Rule | Catches | Example blocked |
|---|---|---|
| `*git*push*--force*` | `--force`, `--force-with-lease[=…]`, `--force-if-includes`, any position | `git push origin master --force`; `git -C ~/Work/Dbrain2 push --force-with-lease=master` |
| `*git*push* -f*` and the `-uf`/`-vf`/`-qf` rules | short force flag, alone or bundled | `git push -f`; `git push origin -fu master`; `git push -uf origin master` |
| `*git*push* +*` | a `+` refspec (forced update) | `git push origin +HEAD:master` |
| `*git*push*--mirror*` | mirror push (overwrites and deletes remote refs) | `git push --mirror origin` |
| `*git*push*--delete*`, `* -d*` | branch or tag deletion | `git push origin --delete master`; `git push -d origin v1` |
| `*git*push* :master*`, `:main*`, `:refs/*` | deletion by empty source refspec of the two protected branches or any full ref (a rule ending in `:*` is avoided: Claude Code reads a final `:*` as its trailing-wildcard suffix, not as a literal colon) | `git push origin :master`; `git push origin :refs/heads/main` |
| `*git*push*--prune*` | deletes remote branches with no local match | `git push --prune origin` |

The leading `*` also covers an absolute path (`/usr/bin/git`), `env` and `git -C <dir>` / `git -c <key=value>` before `push`.

## Known gaps (accepted only if David OKs the list)
- **Other bundles of the short flags:** `-f` first is covered whatever follows (`-fu`, `-fvq`); `-uf`, `-vf`, `-qf` are listed; others with `f` not first (`-nf`, `-uvf`) and `-d` not first (`-vd`) are not.
- **Quoting and whitespace, for the rules that need a literal space** (`-f`, `-uf`/`-vf`/`-qf`, `+`, `-d`, `:master`/`:main`/`:refs/`): a quoted flag or refspec (`git push "-f" origin master`, `git push origin "+HEAD:master"`) or a tab before it is not matched. The `--force`, `--mirror`, `--delete` and `--prune` rules still match quoted or tab-separated forms.
- **Empty-source deletion of other refs:** `git push origin :feature` (a short name other than `master`/`main`) is not matched; `--delete`/`-d` forms are.
- **Indirection:** a shell alias, a git alias (`git config alias.p "push --force"`, already an `ask` rule), a script file, a variable holding the flag (`F=--force; git push $F`), or `gh api` calls to the refs endpoint. These are the fragile cases the docs warn about; the lead's rule "never force-push" stays the guard for them, as since D85.
- **False positives:** any command that contains `git`, then `push`, then one of these strings is denied, for example `git commit -m "do not push --force"` or `git log --grep push -d…`. The lead rewords such a command; no rule needs to be loosened.
- GitHub-side protection (D86) stays off unless David buys GitHub Pro (Q77 (b), not chosen).

## Done when (checkable)
**This draft (Tier 1, session 36):** the brief holds the exact list, the coverage table and the gaps; Q79 is queued; `.claude/settings.json` is unchanged.

**Applying it (later, Tier 2):**
1. David has OK'd the list above, or a changed version, word for word (Q79).
2. The lead replaces the 12 `deny` entries in `.claude/settings.json` with the approved list, nothing else in the file changed; Codex reviews the diff (Tier 2, security settings); committed and pushed.
3. A dry check, with no push run: each example in the table is matched by at least one rule (checked against the patterns, not by running the command).

## Constraints (vault rules that especially apply)
Hard limit: security or permission settings always ask David. Never test by force-pushing. Commit and push (no force) at the end of the run (D79, D90).

## Review
Codex `gpt-6.1-sol` (review profile, high, read-only), session 36. **Round 1 FAIL:** `Bash(*git*push* :*)` ends in Claude Code's legacy `:*` suffix, so it would not match a literal colon (blocker; replaced by `:master*`, `:main*`, `:refs/*`); two scope blockers were concurrent Cowork edits in the shared tree, not part of this diff (excluded); should-fixes: gaps list (quoted flags, `-vd`), scope and Done-when split (applied). **Round 2 PASS:** all table examples matched; the seven normal push forms the lead uses (`git push`, `git push origin master`, `git -C … push`, `… push origin main`, `-u`, `--dry-run`, `--follow-tags`) stay allowed; all 12 current entries covered. Should-fixes applied: quoting gap limited to the space-dependent rules; git-push docs cited; Q79 wording narrowed.

## Outcome
**8 Oct (session 37):** David answered Q79 (a): the list as written. The lead replaced the 12 `deny` entries in `.claude/settings.json` with the 13 rules above, nothing else in the file changed (valid JSON, 13 entries); Tier 2 Codex review of the settings diff (see the commit); no force push was run to test it. Recorded as D97. Done-when 3 (each table example matched by a rule) was checked by the reviewer against the patterns in session 36, round 2.
