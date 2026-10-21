---
classification: internal
task: T9c
owner: "@code"
status: blocked-on-david   # step 1 (candidates, download and disk budget) needs David before anything is fetched
models: []
created: 2026-10-21
source: "David, Q141 (21 Oct, session 53) - keep C2, measure larger models; Q-cowork-21c quality first; T9b results note"
review_status: draft
note_type: brief
---
# T9c · A larger local model for the Mac (stage 1, L0)

## Goal (one sentence)
Find out whether one or two models larger than C2 that fit the Air's 24 GiB pass T9's safety gate and answer more dev cases correctly than C2, so the Mac's L0 level gets the strongest safe model (Q-cowork-21c, Q141).

## Files in scope (agent may touch only these)
- Runtime: a sibling runner `experiments/t9c_compare.py` and its tests (as `t9b_compare.py` did), `artifacts/t9c-*/`; the model files, outside the vault next to the existing ones.
- Vault: this brief; TASKS; PROGRESS; `index.md`; `log.md`; `90 System/for-david.md`; `90 System/handoff.md`; a dated results note `10 Projects/AI Second Brain/02_Architecture/t9c-<date>.md`.
- **Not in scope:** the default model (David chooses from the outcome), `mvp/run-all.sh`, the prompt, retrieval, the frozen corpus, T9 and T9b pins and results, `30 Resources/Local AI/` (Cowork's weekly review owns them).

## Inputs / context to read first
- [[90 System/briefs/T9b-twil-lm3-pro-trial|T9b]] (protocol with declared changes, judging method) and [[10 Projects/AI Second Brain/02_Architecture/t9b-twil-lm3-pro-2026-10-21|its results]]; [[90 System/briefs/T9-M6-model-comparison|T9/M6]] (frozen protocol, eligibility rule 1: a licence that allows the December demo).
- D141, D142 (critical tier at L0), Q-cowork-21c, Q141; D56 (L0 may exceed the 8 s text p95, Q-cowork-21c).
- [[30 Resources/Local AI/benchmark-ledger]] and the weekly local-model review for candidates.

## Steps
1. **Candidates and budget (with David, Tier 2 measurement input).** Propose at most two candidates from the ledger with: exact file and revision, size, licence (must allow the December demo, T9 rule 1), expected peak memory with an 8k context inside 24 GiB with the phone service's needs, and llama.cpp support on the pinned build or the one newer build. Disk: models already use about 19 GB of the 25 GB budget (Q8), so a model of about 16 GB needs David to raise the budget or remove an old file. **Stop and ask David** (for-david, or in session) for the candidates, the budget and the window. Nothing is downloaded before his answer.
2. **Manifest, download and load check** as T9b steps 1–2 (pinned revision and SHA-256, one file each, unscored warm-up under the no-network sandbox; excluded with its reason if it does not load or does not fit).
3. **Runner (Tier 2: it runs on the frozen vault corpus and leaves lasting evidence, as T9b's runner was raised, Q119; Codex pass and David's approval).** `t9c_compare.py` on T9b's pattern: C2 at both ends and in the middle as the drift check, each candidate in two scored blocks, per-configuration timeout sized from the warm-up; the frozen corpus `878a08ea6f57`; tests on the order, scored positions and manifest checks.
4. **Measuring window with David** (T9b's conditions: AC power, Low Power Mode off, phone service stopped and restarted after, no Codex calls, `caffeinate -dimsu`).
5. **Judging and results note** as T9b (lead first, then Codex blind on a masked packet from a folder holding only the packet and rubric); draft note, `index.md`, `log.md`.
6. **Outcome to David**: he chooses the Mac's default; switching the phone service to a new model is a separate step he approves.

## Done when (checkable)
1. Each candidate measured against C2 under the protocol, or excluded with its reason (licence, size, revision moved, does not load, does not fit).
2. Results note drafted with numbers, both judges' verdicts and the gates step by step.
3. Outcome answered by David; the default changes only on his word.
4. Disk stays within the budget David sets in step 1.

## Constraints (vault rules that especially apply)
- Synthetic dev cases only; nothing leaves the Mac (D141); provider keys unset; no-network sandbox.
- Safety gate before quality: "quality first" ranks safe models only (Q141 framing).
- English and French only (D121).

## Review

## Outcome
