---
classification: internal
status: draft
updated: 2026-10-01
---

# Discovery research — how notes get in, and where they go

## The admissibility gate

**Decided 1 October 2026.** Research notes gathered as part of an employer engagement are that
employer's work product and **do not enter this vault**, regardless of how much time has passed since
the engagement ended. Confidentiality obligations outlive restrictive covenants.

This specifically rules out the existing nurse interview material from David's Medispring role. It has
not been read or ingested.

| Source of a research note | Admissible? | Classification |
|---|---|---|
| Interview David runs himself, independently, for this venture | ✅ | `internal` |
| Desk research from published sources | ✅ | `public` if it belongs in the knowledge base |
| Research conducted for an employer or client | ❌ **never** | — |
| Anything containing patient data | ❌ **never** | — |

### Third parties in notes (data-policy §3)

Interviewees are third parties. So:

- **Minimised form only**: first name plus the context needed. No surname, no employer, no contact
  details, no anything sensitive (§2.4).
- Prefer a **participant code** (`P1-physio`, `P2-nurse`) in synthesis notes, with the identity mapping
  kept **outside the vault** if it is needed at all.
- Notes mentioning a third party are **never screen-shared in a demo**.
- Get explicit consent to record and to use quotes, and note that consent in the file.

## Where notes go (per D49)

```
Verbatim notes / transcripts
  └─ 40 Archive/Inbox/YYYY-MM-DD-HHmm-<slug>.md     untouched, archived
       cited from synthesis via a `source:` frontmatter key

Synthesis, per persona
  └─ 10 Projects/Healthcare Practice OS/05_Research/
       persona-physio.md · persona-nurse.md · persona-manager.md · persona-gp.md
       pain-points.md        cross-cutting, quantified
       jobs-to-be-done.md    what each role is actually trying to get done

Anything that turns out to be durable industry knowledge
  └─ propose it into 30 Resources/Belgian Healthcare & eHealth/ as `public`
```

## Per-interview note template

```markdown
---
classification: internal
status: raw | synthesised
date: YYYY-MM-DD
participant: P<n>-<role>          # code, not a name
role: physiotherapist | nurse | practice manager | GP | other
setting: solo | group practice | maison médicale (forfait) | maison médicale (acte) | other
headcount: <n>
consent: recorded yes/no · quotes yes/no
source: "[[40 Archive/Inbox/YYYY-MM-DD-HHmm-<slug>]]"
---

## Context
Who they are in minimised form, their setting, their current tool stack.

## Current workflow, step by step
For each step: who does it, in which tool, how many minutes, how often, what goes wrong.

## Quantified pain
Minutes per day/week · error rate · rework · money lost or delayed. Numbers, not adjectives.

## What they have tried
Workarounds, spreadsheets, abandoned tools, and why each failed.

## Direct quotes
Verbatim, attributed to the participant code only.

## Surprises
Anything that contradicted an assumption. These are the most valuable lines in the file.

## Open questions for next interview
```

## What makes a good interview here

Three rules, in order of how often they get broken:

1. **Ask about the last time it happened, not about preferences.** "Walk me through the last rejected
   invoice" beats "would you like better invoicing".
2. **Get the minutes.** A pain you cannot quantify cannot be prioritised, and cannot be shown back to a
   practice manager as a euro figure.
3. **Never pitch.** The moment you describe a solution, the data stops.

## Interview guides

- [[10 Projects/Healthcare Practice OS/05_Research/interview-guide-physio|interview-guide-physio]]
- [[10 Projects/Healthcare Practice OS/05_Research/interview-guide-nurse|interview-guide-nurse]]

Both are grounded in verified mechanics from
[[30 Resources/Belgian Healthcare & eHealth/billing-rules-and-cumulation|billing-rules-and-cumulation]],
so the questions land on real constraints rather than generic workflow talk.
