---
classification: internal
note_type: queue
source: cowork
review_status: approved
created: 2026-10-02
updated: 2026-10-12
---
# For David: the single decision queue

David chose a single front door on 2 Oct 2026 (option A, provisional **D-cowork-6**). **Only Cowork asks David.** Claude Code and Codex never ask him directly. They add an entry below, set the brief to `blocked-on-david`, and carry on with other work. Cowork opens every session by walking David through the open entries, writes each answer into the entry and the brief, and the lead turns answers into decisions/commits.

**Entry format:** `ID · from · brief · question · options (recommended first) · what it blocks · urgency (today / this week / whenever)`. Answered entries move to *Answered* with the date and answer; the lead clears them once they are recorded in PROGRESS/briefs.

**Since you last looked (7 Oct, session 30):** with your Q71 answer, **M3 is done**: ui-design-agent, claude-blueprint and agentic-ios-app are in `~/Work/_archive/` and archived on GitHub (D78). Every step of your 6 Oct clean-up run is now done; **the hold stays until you lift it**. Your 7 Oct answers are applied: the lead now pushes at the end of every run (D79; this run's commits will be pushed after review and commit; push pending), the 13 dead lines are gone from `~/.claude/settings.json`, and tracking files carry `review_status` (D80). Summary in [[log]].

## Open

| ID | From | Brief | Question | Options | Blocks | Urgency |
|---|---|---|---|---|---|---|
| Q98 | lead, 12 Oct (session 46) | [[10 Projects/AI Second Brain/02_Architecture/client-tier-workspace-requirements\|client-tier requirements]] R5; D121; roadmap §0 amendment (D126) | Two of your rules disagree. On 9 Oct you said **English and French only** (D121: no work on Dutch or other languages unless you ask). The requirements for your future work workspace (client tier) say **French, English and Dutch**, mixed within one meeting (R5), because Brussels business meetings are like that. D121 already names the way out ("a client demo needs one"), but only you can say whether it applies. Nothing is built for Dutch today; this affects the work-tier voice tests (P4.3) and the work-mail connector (C3, W9–W10 at the earliest). Which rule wins? | (a) keep English and French only for now; R5's Dutch waits until a work-tier task actually needs it, and is then asked again (recommended: no cost today, and the conflict only matters from C3) · (b) Dutch in the work tier only, from C3 on; Dbrain2 stays English and French · (c) Dutch in both Dbrain2 and the work tier (wider than R5, which covers the work workspace only) | Nothing today; C3 and the work-tier part of P4.3 later | whenever |

## Answered (since 8 Oct)

Answers land here first; the lead clears each once recorded (D68). Older answered entries, moved verbatim on 8 Oct 2026 (session 38): [[90 System/for-david-archive]].

- **Q95 → (a)** (David, 9 Oct 17:10, via Cowork): the phone part of the "Wrong" button (Shortcut steps, restart, end-to-end check) is done at the start of the next lead run, David at the Mac with his iPhone. Fold the phone re-check on C2 (P2.4, D105) into the same session. **Not done in the 12 Oct run (session 46): David was not present and asked for it to wait for a later run with him;** `Ask Brain.command` was not restarted.
- **Q96 → (a)** (David, 9 Oct 17:10, via Cowork): install Pillow 12.3.0 into the M6b test environment only, recorded in the manifest.
- **Q97 → (a)** (David, 9 Oct 17:10, via Cowork): approve; the lead commits P2.5 F0 (with the P2.5 brief lines waiting on it) and starts F1–F3. **Done 12 Oct (session 46):** F0 committed, runtime `d584f13`; recorded in the P2.5 brief.

- **Q91 → (a), done** (David, 9 Oct 11:18, via Cowork): the sensitive and quarantined Desktop-pilot files were reviewed and **deleted by David himself**. Cowork did not open or verify the staging folder (not connected to its session). Stop condition (3) is cleared.
- **Q90 → (a)** (David, 9 Oct 11:18, via Cowork: "switch on real capture"): turn real capture on now, David present; one planted failure proves it end to end. Accepted with the D110 exceptions as stated in the question. Recorded as **D119**.

- **Q89 → (c)** (David, 9 Oct 08:37, via Cowork; Cowork had recommended (a)): narrow what `incomplete` means in the service before any real capture, and Cowork places it in the work sequence. Cowork's finding: `answer.py` labels every answer `incomplete` by design, because `supported` needs a verifier (P2.5 layer 7, T4.1) that does not exist yet. So the narrowing is a split, not the verifier: answers that are cited and grounded but unverified get their own label (`unverified`, or a reason code), and only real defects stay `incomplete` (cited an id never offered, no citation, grounding below threshold, verifier rejection). Only those defects, plus the other signals, store question text. Placed as **P2.7 step C1b**, after C1 and before C2, so C2 wires the final signal set. The full verifier stays in P2.5 layer 7, and when it lands, `unverified` answers either become `supported` or are rejected. Recorded as **D113**.
- **Review budget → Cowork's call** (David, 9 Oct 08:33: "Review limit: what should we do? do it yourself"). Cowork's rule: 5 reviews per *step* per run (a brief without steps is one step), every review counted against one step with a visible `Review n/5` line before each Codex call, a parked step stops that brief's later steps for the run, and a cap of 12 reviews per brief per run. Commit per step. Amends D72; exact AGENTS.md text in the 9 Oct 08:45 handoff entry. The smaller-steps rule (8 Oct 22:24) is recorded with it. Recorded as **D111** (small steps) and **D112** (review budget per step).

- **Q88 → (c)** (David, 8 Oct 18:08, via Cowork; Cowork had recommended (a)): **an exception to D108 on the Air.** Accept Claude Code's tripwire as it is (a deliberately disguised command could read the store; the Codex app's computer-use route is untested); David installs `/etc/codex/requirements.toml` with `sudo` to stop Codex's full-access mode; Cowork runs its own test. **Cowork's test, 8 Oct 18:08:** its file tools and its shell both refuse the store path (`~/Library/Application Support/dbrain/failures/` is outside the folders connected to Cowork; the shell runs in an isolated VM that sees only those folders). Not covered: Cowork's computer-use tools (screen control), like Codex's, and a folder grant David would approve himself. The D108 host part (dedicated macOS user on the Mac mini) stands. Recorded as **D110**.
- **Q84 → (a)** (David, 8 Oct, session 39): adopt C2 (Gemma 4 E4B) as the query-service default; write all four models' numbers into the Local AI notes. He still reads the full T9 report; the decision is made. Recorded as **D105**.
- **Q83 → (a)** (David, 8 Oct, session 39): the lead deletes the local review branch with `-D` (done, it was `f6f8979`); David deletes the GitHub copy himself. Recorded in D105.
- **Q87 → (a)** (David, 8 Oct 17:05, via Cowork): approve the test-hang fix in full (service change and test watchdog); the lead commits and pushes it. Recorded as **D109**.
- **Q86 → (a)** (David, 8 Oct 17:05, via Cowork): deny rules for the failure-store folder in each agent's settings now (Claude Code, Codex, Cowork), each proven by the access test before capture starts; the text-free audit log stays readable; on the Mac mini, a dedicated macOS user alone owns the store. The settings edits are approved by this answer (hard limit). Recorded as **D108**.
- **Q85 → (a)** (David, 8 Oct 17:05, via Cowork): Mac mini M5 Pro 18-core, 64 GB, 1 TB from Apple Belgium through the SRL, €3,669 incl. VAT (€3,032 ex VAT), ordered by Fri 16 Oct. David places the order himself. Recorded as **D107**.
