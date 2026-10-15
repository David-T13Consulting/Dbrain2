---
classification: internal
task: T9b
owner: "@code"
status: in-progress   # steps 1-3 this run (Q115 (a)); step 4 needs David's window
models: []
created: 2026-10-15
source: David, 15 Oct (asked Cowork to add TwIL-LM3-Pro to the model-comparison brief); D99; weekly local-model review 15 Oct (benchmark ledger, README shortlist, approved as unverified under Q114)
review_status: proposed
note_type: brief
---
# TwIL-LM3-Pro Q4_K_M trial against the T9 default (T9b)

T9/M6 is closed (run 8 Oct, C2 adopted as D105) and its protocol was frozen before results, so this is a follow-up brief, not an edit of T9's candidate list. T9 keeps a one-line pointer here.

## Goal (one sentence)
Measure webAI's TwIL-LM3-Pro (Q4_K_M GGUF, official repo) on the same cases and pipeline as T9, side by side with the current default C2 (Gemma 4 E4B QAT Q4_0) in the same window, so David has local evidence, not publisher claims, for his wish to show the model in the demo (D99).

## What this trial can and cannot decide
- **It reports evidence; it picks nothing.** T9's selection rule, gate 1, requires a licence that allows the commercial December demo. TwIL-LM3-Pro ships under the webAI Non-Commercial License 1.0 (grant limited to non-commercial research and educational use; recorded as a fact, David 9 Oct). D99 (licence question open) is untouched. The results note applies gates 2 to 6 for information and marks gate 1 as "not met by the licence text; D99 open". Any change of default is David's decision (Tier 2) and is not part of this brief.
- **The hypothesis behind it is `unverified`** (approved as such, Q114): that formal-logic training transfers to rule application and evidence checking (S5). The T9 dev cases are cited question answering, not evidence checking, so this trial tests only whether the model can answer plainly, cite correctly and stay safe on them. A result for S5 would need its own cases; none are proposed here.
- Publisher figures (Track A/B, vendor-only, from the model card) are not reused as results.

## Candidates

| # | Model and file | Publisher of the file | Size | Role |
|---|---|---|---:|---|
| C2 | Gemma 4 E4B QAT Q4_0 (`676c3507…`, on disk, pinned in T9) | Google (`4b4a2c1d`) | 5.15 GB | Reference, re-measured in the same window (the 8 Oct numbers used another session and cannot be compared on drift) |
| TW | `TwIL-LM3-Pro-Q4_K_M.gguf` from `webAI-Official/TwIL-LM3-Pro` at revision `4214aaa4020cd51ac418dc6c7243c076665a811d` (read 15 Oct; model API sha unchanged since 30 Sep) | webAI (official repo) | 2.09 GiB (≈ 2.25 GB) | Trial model; 3.66B parameters, Granite 4.2 3B fine-tune, text only |

**Download:** exactly one file, TW, direct to the target path outside the vault, no Hugging Face cache copy, no `mmproj`, no other quant, no safetensors. The lead writes a pre-download manifest first (repository, immutable revision, file name, size, full SHA-256 read from the publisher's metadata at that moment). If the revision, size or hash differs from the manifest, or the revision has moved past `4214aaa4`, the file is not used and the change comes back to David as a new candidate.

**Budget (Q8, 20 GB; 25 GB in total after M6b, D100):** the lead recounts disk occupied by model weights and runtimes before downloading. T9's planned total was ≈ 18.25 GB; adding ≈ 2.25 GB (and ≈ 0.1 GB if a newer llama.cpp build is needed) must stay within 25 GB. If the recount does not fit, stop and ask David (deleting files is his call, hard limit).

## Protocol (T9's, with three declared changes, fixed before measuring)
Same as T9 unless listed: P2.2 pipeline on the three-file `devcases` corpus, lexical retrieval, 4 chunks, the P2.2 prompt, each model's own chat template, temperature 0, seed 42, prompt cache off, context 4096, `-np 1`, `-t 4`, `-ngl 99`, no network (sandbox as in T9), outputs only to `dbrain-runtime/artifacts/` through the write guard, the 10 platform dev cases only, reserved acceptance and running-domain cases never run. Aggregation: nearest-rank p50/p95, peak RSS, per-case verdicts by the lead and by Codex judging blind.

1. **Runtime:** one pinned build for both models. b11146 if it loads TW (the Granite 4.2 architecture is unverified there); otherwise one newer release (v0.6.0, 5 Oct, or later) pinned in the manifest, **with C2 re-measured on that build**. The T9 numbers on b11146 stay as evidence and are never mixed with the new build's. If the build changes after measuring starts, all blocks are discarded.
2. **TW has two configurations, because its model card requires thinking** (publisher guidance, read 8 and 15 Oct: `--temp 0`, `-cnv`, at least 2048 output tokens for the thinking block; reasoning is not switched off):
   - **TW-A, card configuration:** `max_tokens` 2048, thinking on. Request timeout raised from 120 s to 300 s for TW-A only; a timeout still counts as not correct and enters latency with its elapsed time.
   - **TW-B, T9-identical configuration:** `max_tokens` 320, thinking off if the chat template supports switching it off, otherwise run as is. A truncated thinking block with no answer is a malformed reply (not correct; on an unanswerable case it fails the safety gate).
   - Latency of TW-A against C2 is **not like for like** (up to 2048 against 320 generated tokens); the note says so next to every comparison.
3. **Block order (7 blocks):** C2 · TW-A · TW-B · C2 · TW-B · TW-A · C2. C2's scored blocks are positions 1 and 7; position 4 is a drift check only (same 25 % rule and re-run rule as T9). Each TW configuration has two scored blocks, so n = 20 each. 180 s cool-down before every block; machine state recorded before and after each. Expected duration about 1.5 to 2.5 hours depending on TW-A's thinking length; David is told the upper bound before starting.
4. **Safety and quality:** T9's gates 2 and 3 unchanged (zero invented citation ids, zero unsupported citations, both unanswerable cases declined in substance; Q counted only when both judges mark correct in both blocks). Gate 1 is reported, not applied (see above).

## Steps (each fits one review cycle; the lead cuts further if a step does not)
1. **Manifest and disk recount (Tier 0/1a).** Read TW's revision, size and SHA-256 from the publisher; recount Q8 disk; write the pre-download manifest to `dbrain-runtime/artifacts/`. Stop if the revision moved or the budget does not fit.
2. **Download and load check.** Fetch the one file; verify the hash; load it on b11146 under the sandbox with a warm-up request (not scored); if it fails to load, try the one newer pinned build; if that fails too, record TW as excluded with the error and stop (Done when 1 allows this).
3. **Runner extension (Tier 1a: synthetic data, temp folder only).** Add the two TW configurations, the per-configuration timeout and the 7-block order to `experiments/t9_compare.py` (or a sibling script) with tests; the pre-run manifest enforces code, corpus, request signature and case contents as in T9.
4. **Measuring window with David** (Q115: on power, lid open, Low Power Mode off, phone service stopped, no heavy work, no Codex calls). Run under `caffeinate -dimsu`.
5. **Judging and results note.** Lead judges first and saves verdicts; Codex judges a masked packet blind. Draft note `10 Projects/AI Second Brain/02_Architecture/t9b-twil-lm3-pro-<date>.md` (`review_status: draft`, Q7) with numbers, per-case verdicts, the gates applied step by step and the three declared changes; add to `index.md` and `log.md`.
6. **Queue the outcome for David** in `for-david.md`. Proposed rows for the Local AI ledger and `text-and-vision.md` are queued, not written, unless David asks (as for T9, Q84 (a)).

## Files in scope
- `~/Work/dbrain-runtime/` (runner, `artifacts/`); one model file outside the vault next to the existing ones.
- This brief; TASKS; `index.md`; `log.md`; `90 System/for-david.md`; `90 System/handoff.md`; PROGRESS (session close).
- The dated results note named in step 5.
- **Not in scope:** the default model, `mvp/run-all.sh`, the prompt, retrieval, the T9 pins and results, `30 Resources/Local AI/` (Cowork's weekly review owns those notes), anything on the new host.

## Inputs / context to read first
- [[90 System/briefs/T9-M6-model-comparison|T9/M6]] (frozen protocol, rule, review record) and [[10 Projects/AI Second Brain/02_Architecture/t9-model-comparison-2026-10-08|its results]]; D99, D105.
- [[30 Resources/Local AI/benchmark-ledger]] (entries 2026-10-08 and 2026-10-15) and [[30 Resources/Local AI/sources]] for the TW card, formats and licence reading.

## Done when (checkable)
1. TW is measured in both configurations alongside C2 under the protocol above, or TW is excluded with its reason recorded (revision moved, hash mismatch, budget, does not load).
2. The results note is written as a draft with numbers, per-case verdicts, gates applied step by step, and the declared differences from T9.
3. Codex has re-judged the per-case verdicts blind to the lead's.
4. The outcome is queued for David; nothing changes the default model or the licence position (D99).
5. Exactly one new model file was downloaded; it matches its pin; disk stayed within the Q8 total.

## Constraints
- Synthetic dev cases only; no client or personal data; the file stays on David's machine outside the vault and is not redistributed.
- The licence is recorded as a fact (David, 9 Oct); the trial is an internal development evaluation and does not settle whether a client-facing demo is covered (D99, not legal advice).
- Results are development evidence on the Air, not D56 acceptance.
- Commit only after the review tier's pass (AGENTS.md › Review tiers).

## Run notes (session 50, 15 Oct, lead `claude-opus-5-5`)
- **Q115 → (a)** (David, in session): steps 1–3 this run; he names the measuring window afterwards.
- **Step 1.** The pin had moved: `webAI-Official/TwIL-LM3-Pro` head is `144a3ccb31264deadcf68bc5a1d58f621e497d03` (9 Oct 18:12 UTC, PR #1 "Replace Q4_K_M GGUF with new build (TwIL-LM3-Pro-q4km-im)", author's comment "a much better 4-bit quantization"). The Q4_K_M file there is 2,244,011,744 bytes, SHA-256 `8a7e0f48af1feea9a107e17e2c03e8ad8d0c397c47a5dae4a73b3d92e3533377`; at `4214aaa4` it was 2,244,011,456 bytes, `7a3edb4e…e161`. The 15 Oct weekly review's "model API sha unchanged since 30 Sep" was therefore wrong (the review had flagged conflicting registry fields as unresolved). Stopped and asked David: **Q116 → pin the new 9 Oct file.** Licence field unchanged (`webai-non-commercial-license-ver.-1.0`).
- **Disk recount (Q8, 25 GB):** models folder 18.33 GB (embeddings 2.73 included), venvs 1.14 GB, llama.cpp 0.03 GB: 19.50 GB; with TW 21.74 GB; with a newer llama.cpp build about 21.85 GB. Fits.
- **Pre-download manifest** written: `dbrain-runtime/artifacts/t9b-2026-10-15/manifest-pre-download.json` (TW at `144a3ccb`, C2 as pinned in T9, the recount).
- **Step 2 done.** One file fetched with `curl` from the `resolve/144a3ccb…` URL straight to `~/Library/Application Support/dbrain/models/` as `.part` (no Hugging Face cache, nothing else): 2,244,011,744 bytes, SHA-256 `8a7e0f48…3377`, both equal to the manifest; then renamed. **Load check** (scratch script, unscored warm-ups, b11146 at its T9 pin, under the T9 no-network sandbox, network denial proven first; evidence `artifacts/t9b-2026-10-15/loadcheck/`): loads on **b11146**, so no newer build is needed and C2 needs no re-measure on another build. TW-B flags (T9's, `--reasoning off`, 320): answer in 0.86 s, `finish_reason` stop, no reasoning text: **the chat template honours thinking off**. TW-A (`--reasoning on`, 2048): 6.82 s, stop, 657 characters of thinking returned apart in `reasoning_content`, clean answer in `content` (200 completion tokens).
- **Step 3 done** (Tier 1a; runtime `c573ff2`). `experiments/t9b_compare.py` runs T9's runner with the three declared changes only: order C2 TWA TWB C2 TWB TWA C2 (C2 scored at 1 and 7, position 4 a drift check with T9's 25 % rule and re-run rule); per configuration only the thinking switch, token cap and timeout differ (C2 off/320/120 s; TWA on/2048/300 s; TWB off/320/120 s); one request signature per configuration in the pre-run manifest (C2 and TWB equal T9's); evidence under `artifacts/t9b/`. `t9_compare.py` gained hooks whose defaults keep T9's behaviour (a test checks T9's order, baseline, signature and child command are unchanged). `tests/test_t9b_compare.py`: 11 synthetic tests (order, scored positions, n = 20 per configuration, drift re-run, flags differ only in the thinking switch, caps and signatures, the capped adapter, a signature mismatch voids the run). Suite 486 OK, secret scan clean. Not yet in a Codex batch.
- **Dry check** with the committed runner (`--dry-check`, label `2026-10-15-dry1`, cool-down 0, warm-up only, no dev case): pins, network denial and all three configurations OK. Warm-up 6.2 s (C2), 17.6 s (TWA), 9.0 s (TWB); peak server RSS 5.16 GiB (C2), 2.52 GiB (TW). Evidence `artifacts/t9b/dry-2026-10-15-dry1/`.
- **Step 4 duration, for David:** seven 180 s cool-downs (21 min) plus the blocks: about 45–75 min if TWA's thinking stays near its warm-up time; upper bound about 2.5 h if every TWA case ran to its 300 s timeout (2 × 10 × 5 min) and one drift re-run happened.
- Note: the D108 tripwire refused the first download command because curl's `--fail` flag put "fail" after "Application Support" in the command text; the same command with `-f` ran. The store was never named or touched.

## Review
## Outcome
