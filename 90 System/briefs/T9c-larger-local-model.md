---
classification: internal
task: T9c
owner: "@code"
status: in-progress   # session 55: step 1 answered (Q144); step 2 download running; step 3 runner written, waits for Codex (Tier 2) and David's approval
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
1. **Candidates and budget (with David, Tier 2 measurement input).** Propose at most two candidates from the ledger with: exact file and revision, size, licence (must allow the December demo, T9 rule 1), expected peak memory with an 8k context inside 24 GiB with the phone service's needs, and llama.cpp support on the pinned build or the one newer build. Disk: models use about 17 GB of the 25 GB budget after Q143 (Q8), so a model of about 16 GB needs David to raise the budget or remove an old file. **Stop and ask David** (for-david, or in session) for the candidates, the budget and the window. Nothing is downloaded before his answer.
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

## Run notes, session 55 (21 Oct, lead `claude-opus-5-5`)
- **Step 1 done (Q144, David in session):** candidates Google `gemma-4-12B-it-qat-q4_0-gguf` (rev `29d097773436`, `gemma-4-12b-it-qat-q4_0.gguf`, 6,975,879,296 bytes, sha256 `93567e57a8fe10b2…`) and `gemma-4-26B-A4B-it-qat-q4_0-gguf` (rev `d1c082be9cf3`, `gemma-4-26B_q4_0-it.gguf`, 14,439,363,584 bytes, sha256 `3eca3b8f6d7baf21…`); both Apache-2.0 (licence rule 1 met), ungated, same family and quantisation as C2; the 26B-A4B is a mixture-of-experts model also measured on Scaleway in PV1 step 5. Disk: the four models that failed T9/T9b deleted on David's word (11.8 GB); Q8 budget 30 GB; 26.2 GB after download. Window: tonight, once the runner passes review and David approves it. Manifest: runtime `artifacts/t9c-2026-10-21/manifest-pre-download.json` (C2's pin copied from T9b's manifest).
- **Step 2:** download of the two pinned files started (each to `.part`, size and sha256 checked against the manifest before rename); load check follows under the no-network sandbox.
- **Step 3 (Tier 2):** `experiments/t9c_compare.py` on T9b's pattern: order C2 G12 G26 C2 G26 G12 C2; T9's server flags and request signature unchanged for all three; timeouts 120 s (C2) and 300 s (G12, G26); evidence under `artifacts/t9c/`. `tests/test_t9c_compare.py` (9 synthetic tests) and T9b's tests pass. Uncommitted: Codex is at its usage limit until 18:38; then review and David's approval before the dry check and the run.

## Review
- Review 1/2 · T9c step 3 — Codex `gpt-6.1-sol` (review profile, high, read-only): **PASS**. Should-fix, applied: synthetic tests that a wrong size, a wrong hash or a changed runtime stop the run before any block (12 tests OK). **Approved by David (Q151)**; committed; run tonight.

## Outcome
