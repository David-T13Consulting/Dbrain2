---
classification: internal
note_type: queue
source: cowork
review_status: approved
created: 2026-10-02
updated: 2026-10-09
---
# For David: the single decision queue

David chose a single front door on 2 Oct 2026 (option A, provisional **D-cowork-6**). **Only Cowork asks David.** Claude Code and Codex never ask him directly. They add an entry below, set the brief to `blocked-on-david`, and carry on with other work. Cowork opens every session by walking David through the open entries, writes each answer into the entry and the brief, and the lead turns answers into decisions/commits.

**Entry format:** `ID · from · brief · question · options (recommended first) · what it blocks · urgency (today / this week / whenever)`. Answered entries move to *Answered* with the date and answer; the lead clears them once they are recorded in PROGRESS/briefs.

**Since you last looked (7 Oct, session 30):** with your Q71 answer, **M3 is done**: ui-design-agent, claude-blueprint and agentic-ios-app are in `~/Work/_archive/` and archived on GitHub (D78). Every step of your 6 Oct clean-up run is now done; **the hold stays until you lift it**. Your 7 Oct answers are applied: the lead now pushes at the end of every run (D79; this run's commits will be pushed after review and commit; push pending), the 13 dead lines are gone from `~/.claude/settings.json`, and tracking files carry `review_status` (D80). Summary in [[log]].

## Open

| ID | From | Brief | Question | Options | Blocks | Urgency |
|---|---|---|---|---|---|---|
| Q93 | lead, 9 Oct (session 44) | [[90 System/briefs/P2.7-failure-capture-loop\|P2.7]] C5 | The "Wrong" button sends only an answer's id, as you asked. To store that question when you tap, the service must still have its text, and most answers raise no failure signal, so nothing was kept for them. Data policy §7a allows keeping question text **only when the question raised a failure signal**. Holding every recent answer, even in memory only, so that a later tap can store it, is keeping text before any signal: Codex review, 9 Oct, blocker. How should C5 work? | (a) amend §7a, your words needed: *"So that a 'wrong' tap can capture it, Ask Brain may hold the text of each recent question and its answer in the service's memory only, never on disk, for at most 24 hours; it is dropped on expiry, on restart, or once tapped, and is stored only if tapped (then it is a failure under this section). This adds to, and does not replace, the capture of questions that raise a failure signal on their own."* (recommended: keeps the feature you asked for; nothing extra reaches disk) · (b) same as (a) with a shorter window, for example 1 hour · (c) no amendment: the button only marks answers that already raised a signal; a confident wrong answer (the 9 Oct case) is counted, text-free, but not stored, so it cannot enter the automatic path from failure to test case (you could still write a synthetic case by hand) · (d) the phone sends the question back with the tap (changes your "id only" rule) | P2.7 C5 | this week |

## Answered (since 8 Oct)

Answers land here first; the lead clears each once recorded (D68). Older answered entries, moved verbatim on 8 Oct 2026 (session 38): [[90 System/for-david-archive]].

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
