---
classification: internal
---
# Capture Protocol — talking to the system on the go

**Purpose:** get a thought out of your head and into the vault with zero friction, while walking, between meetings, or anywhere you aren't at the desk.

**Principle** (from Prisme One's "slow burn"): **Capturer → Accumuler → Exécuter.** Capture is not processing. The whole point is that it costs you nothing in the moment.

---

## How it works with Dispatch

Dispatch lets you message Claude from your phone; the work runs on your Mac and results come back to you. It is **one continuous conversation**, reachable from phone or desktop.

```
   Phone (dictate)  ──►  Dispatch  ──►  Mac (Claude Desktop)  ──►  00 Inbox/
        walking            queue           must be awake         (vault root)
```

### The magic word

Start the message with **`capture:`** — then just talk.

> *"capture: the governance one-pager should probably lead with regulatory exposure not scope, because that's what a CISO reads first"*

Claude will:
1. Write it to `~/Documents/Dbrain2/00 Inbox/YYYY-MM-DD-HHmm-<slug>.md` (the vault root, not this project folder)
2. Transcribe faithfully — cleaning up only dictation artifacts ("um", doubled words, mangled punctuation)
3. **Not** process, expand, research, or ask follow-up questions
4. Reply with one line: what was captured, where it went

That's it. No decisions required from you while walking.

### Other on-the-go verbs

| Say | Claude does |
|---|---|
| `capture: …` | Raw dump to inbox. No processing. |
| `task: …` | Appends to `TASKS.md` backlog |
| `question: …` | Appends to `OPEN_QUESTIONS.md` |
| `decision: … because …` | Appends to the decision log in `PROGRESS.md` |
| *"what's next?"* | Reads `TASKS.md`, replies with the next action only |
| *"where am I?"* | Two-line status from `PROGRESS.md` |

Keep these few and memorable. If you can't remember the verb, `capture:` always works — triage sorts it out later.

---

## ⚠️ The constraint you need to know

**Dispatch runs on your Mac. The Mac must be awake with Claude Desktop open.**

If your Air is shut in a bag, the task won't execute. Because Dispatch is one continuous conversation, the message isn't lost — it should run when the machine is available — but don't assume instant capture.

**Recommended belt-and-braces:** for anything you'd genuinely hate to lose, dictate into your phone's native voice memo or notes app as well. Zero dependency, works in a tunnel. Batch-import to the inbox later.

**Settings worth checking on the Mac:** System Settings → Lock Screen → *Turn display off on power adapter: Never*, and Battery → *Prevent automatic sleeping on power adapter*. If you want capture to work reliably while you're out, the machine needs to stay awake on power.

---

## The inbox file format

```markdown
---
captured: 2026-09-07T14:32
source: dispatch-voice
classification: internal
status: unprocessed
tags: []
---

[Faithful transcription of what you said.]
```

`classification` defaults to `internal`. If the capture mentions anything client-specific it must be marked `client` — and per the standing rules, client-confidential material does not belong in this system at all.

---

## Triage — the other half

Capture without triage is a junk drawer. **Weekly, 20 minutes:**

1. Open `00_Inbox/`, oldest first
2. For each note, one of four fates:
   - **Act** → becomes a task in `TASKS.md`
   - **File** → move into the vault, add real frontmatter and links
   - **Merge** → fold into an existing note
   - **Delete** → most captures. This is fine and expected.
3. Empty the inbox. An inbox that never empties is a reading list.

**The six-week check:** if the inbox is growing and nothing has shipped *out* of the system, stop capturing and start producing. That's the collector's fallacy, and it's the most common way a second brain quietly fails.

---

## Setting it up

- [ ] Confirm Dispatch is enabled in the Claude desktop app
- [ ] Check the Mac sleep settings above
- [ ] Test it: dictate one `capture:` from your phone while away from the desk, then confirm the file landed
- [ ] Add a phone shortcut/widget for Claude if it saves you a tap

Do the test walk before you rely on it. A capture path you haven't tested is a capture path that will fail on the one thought you actually needed.
