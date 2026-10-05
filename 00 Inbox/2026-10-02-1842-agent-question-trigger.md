---
captured: 2026-10-02T18:42:00+02:00
source: conversation-with-cowork
classification: internal
status: unprocessed
tags: []
---
# How does Cowork learn that Claude Code has a question?

David asked to park this for later triage. Capturing it decides nothing and changes no rule.

**The gap (David's question):** if Claude Code is blocked or has a question, what triggers Cowork to ask him? Today nothing does. Cowork only runs when David opens a session. Claude Code (on the Mac) can't message Cowork (in the cloud). Under D68, a question written to `90 System/for-david.md` waits until David next opens Cowork. Meanwhile the lead parks that brief and carries on with any other open brief.

**Options Cowork proposed:**
| | How David finds out | Setup | Trade-off |
|---|---|---|---|
| A. Pull (today) | Next time he opens Cowork | none | A question can wait for days |
| B. Lead sign-off | Claude Code ends every run with one line: "N decisions waiting, open Cowork". It points to the queue but doesn't ask the question | one rule in AGENTS.md | Free; missed if David has walked away |
| C. Scheduled check | A scheduled task reads `for-david.md` every few hours and pushes to the phone only if something is open | one scheduled task, needs the computer | Reaches him anywhere; only while the Mac is on, with a small recurring cost |

Cowork's recommendation was B now, and C if B proves insufficient. Not decided.
