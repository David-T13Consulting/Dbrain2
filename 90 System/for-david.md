---
classification: internal
note_type: queue
source: cowork
review_status: approved
created: 2026-10-02
updated: 2026-10-08
---
# For David: the single decision queue

David chose a single front door on 2 Oct 2026 (option A, provisional **D-cowork-6**). **Only Cowork asks David.** Claude Code and Codex never ask him directly. They add an entry below, set the brief to `blocked-on-david`, and carry on with other work. Cowork opens every session by walking David through the open entries, writes each answer into the entry and the brief, and the lead turns answers into decisions/commits.

**Entry format:** `ID · from · brief · question · options (recommended first) · what it blocks · urgency (today / this week / whenever)`. Answered entries move to *Answered* with the date and answer; the lead clears them once they are recorded in PROGRESS/briefs.

**Since you last looked (7 Oct, session 30):** with your Q71 answer, **M3 is done**: ui-design-agent, claude-blueprint and agentic-ios-app are in `~/Work/_archive/` and archived on GitHub (D78). Every step of your 6 Oct clean-up run is now done; **the hold stays until you lift it**. Your 7 Oct answers are applied: the lead now pushes at the end of every run (D79; this run's commits will be pushed after review and commit; push pending), the 13 dead lines are gone from `~/.claude/settings.json`, and tracking files carry `review_status` (D80). Summary in [[log]].

## Open

| ID | From | Brief | Question | Options | Blocks | Urgency |
|---|---|---|---|---|---|---|
| Q88 | lead (Claude Code), 8 Oct, session 40 | [[90 System/briefs/P2.7-failure-capture-loop\|P2.7]] access tests (D108) | **The D108 access test does not pass yet: how should the gaps be closed?** Codex is blocked by its sandbox (main config and review profile). Claude Code's file tools and plain shell reads are blocked, but a disguised shell command still reads the store: its shell has no OS-level boundary. Cowork is untested. Capture of real questions stays off until every agent fails the test. | **(a) Recommended:** no real capture on the Air; capture starts on the Mac mini, where the service runs as a dedicated macOS user that alone owns the store (D108's host part), an OS boundary for every agent at once. Meanwhile the lead builds and tests stage C with planted data only, in a temporary home · (b) on the Air now: move the phone service and the store to a separate macOS user (you run one `sudo` step; the login item moves) · (c) on the Air now, **an exception to D108 that you would approve**: accept Claude Code's tripwire as it is (an agent that deliberately disguises a command could read the store; the Codex app's computer-use route is also untested), you install `/etc/codex/requirements.toml` with `sudo` to stop Codex's full-access mode, and Cowork runs its own test | real capture (P2.7 stage C) | this week |

## Answered (since 8 Oct)

Answers land here first; the lead clears each once recorded (D68). Older answered entries, moved verbatim on 8 Oct 2026 (session 38): [[90 System/for-david-archive]].

- **Q84 → (a)** (David, 8 Oct, session 39): adopt C2 (Gemma 4 E4B) as the query-service default; write all four models' numbers into the Local AI notes. He still reads the full T9 report; the decision is made. Recorded as **D105**.
- **Q83 → (a)** (David, 8 Oct, session 39): the lead deletes the local review branch with `-D` (done, it was `f6f8979`); David deletes the GitHub copy himself. Recorded in D105.
- **Q87 → (a)** (David, 8 Oct 17:05, via Cowork): approve the test-hang fix in full (service change and test watchdog); the lead commits and pushes it. Recorded as **D109**.
- **Q86 → (a)** (David, 8 Oct 17:05, via Cowork): deny rules for the failure-store folder in each agent's settings now (Claude Code, Codex, Cowork), each proven by the access test before capture starts; the text-free audit log stays readable; on the Mac mini, a dedicated macOS user alone owns the store. The settings edits are approved by this answer (hard limit). Recorded as **D108**.
- **Q85 → (a)** (David, 8 Oct 17:05, via Cowork): Mac mini M5 Pro 18-core, 64 GB, 1 TB from Apple Belgium through the SRL, €3,669 incl. VAT (€3,032 ex VAT), ordered by Fri 16 Oct. David places the order himself. Recorded as **D107**.
