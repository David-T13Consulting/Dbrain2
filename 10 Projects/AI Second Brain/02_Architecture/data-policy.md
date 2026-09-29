---
classification: internal
version: 0.2
status: confirmed by David 29 Sep 2026
---

# Data policy — Dbrain2 / AI Second Brain

**Red line, in one sentence:** No client or counterparty confidential information, no secrets, and no
sensitive data about anyone other than me ever enters this system. Everything else is tiered, and
the tier sits in frontmatter.

## 1 · Tiers

| Tier | What it covers | In the vault? | Sent to a model API? | Shown in a demo? |
|---|---|---|---|---|
| `public` | Anything already published or publishable: posts, course notes with nothing confidential in them, public research | ✅ | ✅ | ✅ |
| `internal` | My own personal and business material: notes, captures, my Strava/HR data, my Tower13 rates, pipeline and positioning, minimised mentions of third parties (§3) | ✅ | ✅ | ✅ my own data · ❌ third-party mentions |
| `client` | Anything containing a client's or counterparty's confidential information, names or terms | ❌ **never** | ❌ | ❌ |

The `client` tag exists so the rule can be checked (a note carrying it is a violation to be removed), not as permission to store client material.

## 2 · Never enters the system, whatever the tier

1. Client or counterparty confidential information, including deliverables, data, meeting content and contract terms
2. Secrets such as API keys, tokens, passwords and passcodes. Those go in env vars or the keychain, never in a file an agent can read
3. Government ID numbers, bank or card numbers
4. Health, financial or ID details about anyone other than me
5. Large binaries (media, PDFs, recordings). They stay outside the vault with a pointer note (rule 7)

## 3 · Third parties (family, contacts)

- Allowed in a minimised form: first name plus the context needed. Nothing sensitive (see §2.4).
- Notes that mention a third party are never screen-shared in a demo.

## 4 · My own special-category data (Strava / heart rate)

- Heart rate and training data count as health data under GDPR Art. 9. It is **my** data, used with my explicit choice.
- Tier: `internal`. It may be sent to a model API and shown in demos.
- In a demo, say this out loud: *"This is special-category data. I chose to use my own, and here's what that means for yours."* That's part of the governance story, not something to hide.

## 5 · Model providers

- Assume the default commercial API terms: **inputs and outputs are kept for about 30 days** unless a ZDR agreement exists (see `02_Critical_Assessment.md` §3).
- Anything sent to a model API must therefore be something I would accept being stored by that provider for 30 days, which means `public` or `internal` only.
- The provider and hosting choice gets re-checked against this policy at T9 (week 9).

## 6 · Tower13 commercial material and contracts

**Rule (D16, 29 Sep):** every client contract must state clearly that I use a personal AI agent. Until a
contract says so, nothing about that engagement goes into the system, **including my own notes about it**.

| Contract state | What may enter the system |
|---|---|
| States my AI agent use explicitly | My own `internal` notes about the engagement: my time, my learnings, my rates. Counterparty confidential material still never enters (§2.1). |
| Silent or ambiguous | Nothing about the engagement. |
| Restricts or bans AI use | Nothing about the engagement, and I don't use the agent on it at all. |

- My own rates, proposals, pipeline and positioning, when they don't mention an engagement, stay `internal`.
- A disclosure clause makes my own notes permissible. It never makes client data permissible. §2.1 is absolute.
- Going forward, the Tower13 contract template carries a standard AI-use disclosure clause (T0.7).

## 7 · Enforcement (current → planned)

| Control | Now | Planned |
|---|---|---|
| Classification frontmatter on every note | ✅ convention | Lint check (H1) |
| Agent access | Read-only | Write access limited to approved folders after the T4.2 rollback test |
| Secret scanning | Manual | Pre-commit scan (H1) |
| Client material physically unreachable | Kept outside any folder an agent can reach | — |
| PII in traces | n/a | Masking once tracing exists (week 12) |

## 8 · Changing this policy

Only David changes it. Record the change as a decision in `PROGRESS.md` and bump `version`.
