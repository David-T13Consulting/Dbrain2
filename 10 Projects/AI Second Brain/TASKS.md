# Tasks — AI Second Brain Project

**Updated:** 7 Sep 2026 · **Phase:** Week 0 — Foundations · **Target:** client-ready December 2026

---

## ▶ Next action

> **T0.1 — Revoke the Telegram bot token.** 5 minutes. Do this one first; it's a live credential.

If you have a longer window, do **T0.3** (the 30-day audit prompt) then come back with 3–4 candidate workflows so we can settle **T0.4**, which unblocks all of H1.

---

## Week 0 — Foundations

*Everything here blocks H1. Target: complete by 14 Sep.*

- [x] **T0.1 · Revoke the Telegram bot token** ✅ done 8 Sep `5 min` `🔴 security`
  Token `8842032811:AAFH…` is in `00_Source_Material/Product_School/Product School - Advanced Agents.pdf` (p.2). Revoke via BotFather → `/mybots` → select → API Token → Revoke.
- [ ] **T0.2 · Rotate the four Zoom recording passcodes** `10 min` `🔴 security`
  Same PDF. Lower severity than the token but they're recordings of paid course content.
- [ ] **T0.3 · Run the 30-day audit prompt** `20 min`
  In ChatGPT/Claude: *"Look at my last 30 days of conversations. Where am I spending most of my time, and what from that list should be automated?"* Evidence-led input to T0.4. (Source: Advanced Agents, Day 2.)
- [ ] **T0.4 · Choose the showcase workflow** `45 min` `⭐ blocks everything`
  Criteria: genuinely recurrent · has a *checkable* right answer (or no golden dataset is possible) · legible to a client in <30 sec · needs **no** client-confidential data to demo.
  → Bring me 3–4 candidates and we'll pressure-test them together.
- [ ] **T0.5 · Write `data-policy.md`** `45 min`
  Three tiers (public / internal / client-confidential), red lines, what may never enter the system. Save to `02_Architecture/`.
- [ ] **T0.6 · Check your firm's AI policy** `30 min`
  The one input I can't research. Also scan two live client contracts for AI/subprocessor clauses. → resolves OQ-2.

**Week 0 gate:** you can state the showcase workflow and your red lines in one sentence each.

---

## H1 · Weeks 1–4 — Ship

*Goal: a working, instrumented vertical slice. Narrow and deep.*

### Week 1 — Vault
- [x] **T1.1** Create vault skeleton: `00 Inbox / 10 Projects / 20 Areas / 30 Resources / 40 Archive / 90 System` `30 min` ✅ done 8 Sep — built inside `~/Documents/Dbrain2` (the Obsidian vault), not this folder. See D11 in PROGRESS.md.
- [ ] **T1.2** Write `AGENTS.md` for the vault — **by hand**, 20–30 lines `1 h`
  Auto-generated ones measurably underperform (+23% cost, redundant content).
- [x] **T1.3** `git init` the vault, first commit `15 min` ✅ done 8 Sep — commit 377e8c2 in Dbrain2
- [ ] **T1.4** Migrate a *bounded* subset of knowledge — only what the showcase workflow needs `2 h`
  ⚠️ Resist importing everything. That's the collector's fallacy and it costs weeks.
- [x] **T1.5** Confirm agent is **read-only** at this stage. No MCP servers. `10 min` ✅ confirmed 8 Sep — documented in Dbrain2/90 System/README.md, no write MCP configured

### Week 2 — Skills
- [ ] **T2.1** Write success thresholds for 3 skills — **before** writing the skills `45 min`
  Format: *"handles ≥X% of cases with <Y% exceptions."* Defining "good" is your job, not an engineer's.
- [ ] **T2.2** Write `SKILL.md` #1 `1.5 h`
- [ ] **T2.3** Write `SKILL.md` #2 `1.5 h`
- [ ] **T2.4** Write `SKILL.md` #3 `1.5 h`

### Week 3 — Golden dataset ⭐
- [ ] **T3.1** Draft golden dataset v1 — 150 rows `4 h` `⭐ the showcase artifact`
  Columns: Input · Expected output · Edge case? · Judge type (rule/LLM). 20–30% edge cases.
- [ ] **T3.2** Add adversarial rows (≥3) and note coverage gaps `1 h`
- [ ] **T3.3** Commit as `golden-dataset.md`, versioned like code `15 min`

### Week 4 — Evals + write access
- [ ] **T4.1** Wire LLM-as-judge scoring against the golden set `3 h`
- [ ] **T4.2** Test backup/rollback — deliberately break something and restore it `1 h`
- [ ] **T4.3** Only after T4.2 passes: enable agent **write** access, confined to approved dirs `30 min`

**H1 gate — all four must be true:**
1. Three skills pass their stated thresholds
2. You have deliberately broken something and rolled it back
3. You can screen-share eval results
4. Zero client-confidential data has entered the system

---

## H2 · Weeks 5–9 — Validate

- [ ] **T5** Eval dashboard — metrics, judge setup, drift alerts, UX hooks `1 wk`
  Test: *can you screen-share it in a sales call?* If not, it isn't done.
- [ ] **T6** Reliability contract — metric/target/measurement/alert-threshold + escalation paths `1 wk`
- [ ] **T7** Confidence UX — 3 bands, visible reasoning, override surface, corrections feed back `1 wk`
  Build the low-confidence path deliberately — you will demo it on purpose.
- [ ] **T8** Governance one-pager — scope, autonomy boundaries, escalation triggers, audit cadence, regulatory exposure, agent topology `1 wk`
- [ ] **T9** Model + hosting decision, benchmarked against your own golden dataset `1 wk`
  2–3 options: one frontier, one open-weight, one EU-hosted. Document with the trade-off grid.

**H2 gate:** "How do you know it works?" answered with a screen. HITL% trending down. Governance one-pager survives a hostile read.

---

## H3 · Weeks 10–13 — Collaborate & package

- [ ] **T10** Multi-user layer — shared vs personal roots, RBAC as metadata filter, S.M.A.R.T. memory `1 wk`
  Get a second real human in. Two people working beats ten people designed.
- [ ] **T11** Second agent + supervisor/critic pattern, A2A logging, autonomy ceilings `1 wk`
  Only after naming the boundary you hit (skills / tools / evals).
- [ ] **T12** Security hardening + shadow-AI audit on yourself `1 wk`
- [ ] **T13** Demo build + rehearsal — twice through, no unexplained failures `1 wk`

---

## Backlog / someday

- [ ] Migrate Apple Notes → markdown (export route; no API exists)
- [ ] Retrieve the 4 Product School capstone tools from the LMS (Strategy Assembler, AI Bet Evaluator, Roadmap Builder, Pitch Builder)
- [ ] Decide relationship between this project and the Vibe Coding app+deck deliverable → OQ-5
- [ ] Self-hosted server evaluation — month 4+, only if an async workflow justifies it

---

## Conventions

`🔴` security-sensitive · `⭐` high-leverage · `T0.x` week-0 · time estimates are working time, not elapsed.
Tick items as you go. Add anything that surfaces — an unrecorded task is a lost task.
