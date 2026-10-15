---
classification: internal
task: T9 / M6
owner: "@code"
status: blocked-on-david   # run 2026-10-08-a done and judged; the choice of model (Q84) and the host (Q85) are David's
models: ["claude-opus-5-5 (lead, draft; readiness 8 Oct; run, lead judge and report 8 Oct)", "gpt-6.1-sol (review rounds 1-3; runner review rounds 1-4, 8 Oct; blind re-judge and report review 8 Oct)"]
created: 2026-10-05
updated: 2026-10-08
source: TASKS T9 and M6; D56; D64; Q8 (M6 budget); P2.2 run B and the 5 Oct latency sweep
review_status: proposed
note_type: decision
---
# Local model comparison for the read-only query service (T9 / M6)

## Goal (one sentence)
Choose the local model for the P2.2 query service from three named candidates and the current baseline, by a selection rule and a protocol fixed **before new comparison results are seen** (the baseline's run B and the 5 Oct sweep are already known), measured against D56.

## Candidates (all Apache-2.0, all within the M6 budget)

| # | Model and file | Publisher of the file | Size | Why it is here |
|---|---|---|---:|---|
| 0 | Qwen3-4B Q4_K_M (`7485fe6f…`, on disk, pinned 1 Oct) | Qwen (official) | 2.50 GB | **Baseline and a full contender** under the same rule; also the drift reference in the protocol |
| 1 | Qwen3.5-4B Q4_K_M (`00fe7986…`, on disk since 1 Oct) | unsloth (quantization of the official model) | 2.74 GB | Same family, newer; measured 1 Oct only on a different prompt, never on the P2.2 pipeline |
| 2 | Gemma 4 E4B instruction-tuned, QAT Q4_0, text weights only (`gemma-4-E4B_q4_0-it.gguf`, `676c3507…`) | Google (official repo `google/gemma-4-E4B-it-qat-q4_0-gguf`, rev `4b4a2c1d`) | 5.15 GB | **Another family (M6).** Quantization-aware trained by the publisher; Google's model card presents QAT as preserving quality at Q4 better than post-hoc quantization. That is the publisher's rationale, which this comparison tests, not a finding |
| 3 | Ministral 3 8B Instruct 2512 Q4_K_M (`Ministral-3-8B-Instruct-2512-Q4_K_M.gguf`, `33e7a72c…`) | Mistral (official repo `mistralai/Ministral-3-8B-Instruct-2512-GGUF`, rev `0102285a`) | 5.20 GB | **Another family (M6)**, French/English, larger: tests whether 8B buys quality worth its latency |

**Budget (Q8: up to 20 GB of disk for model weights and runtimes, outside the vault, hash-pinned, only models named in a brief; raised to 25 GB in total on 8 Oct for M6b's two embedding models, D100: T9/M6's own share stays as counted below).** Counted as disk occupied, not bytes downloaded:

| Item | GB |
|---|---:|
| Qwen3-4B, `/private/tmp` (pinned 1 Oct) | 2.50 |
| Qwen3-4B, copy in `~/Library/Application Support/dbrain/` (MVP-phone service) | 2.50 |
| Qwen3.5-4B, `/private/tmp` | 2.74 |
| llama.cpp b11146: archive 0.01 + two extracted copies 0.05 | 0.06 |
| **On disk now** | **7.80** |
| Gemma 4 E4B QAT Q4_0 (text weights only) | 5.15 |
| Ministral 3 8B Q4_K_M | 5.20 |
| One newer llama.cpp build, only if b11146 cannot load a candidate (archive + extract) | ≈ 0.10 |
| **Total** | **≈ 18.25** |

Vision projectors (`mmproj`) are not downloaded: the service is text only. No Hugging Face cache copy is kept (direct file download to the target path). Within budget with about 1.75 GB spare; removing the duplicate `/private/tmp` Qwen3-4B would free 2.50 GB, but deleting files is David's call (hard limit), so it is offered in the queue, not done.

**Pins: a pre-download manifest** is written to `dbrain-runtime/artifacts/` before anything is fetched: repository, immutable revision hash, file name, size and **full** SHA-256 for each file, read from the publisher's metadata at that moment (the 8-character prefixes above were read from the Hugging Face API on 5 Oct). A file whose revision, size or hash differs from the manifest is not used, and a changed revision is a new candidate that comes back to David. **Exception to "only these four files":** the one llama.cpp build in the table, pinned the same way, only if b11146 cannot load a candidate.

**Not candidates now:** Qwen3.8-27B and Qwen3-Coder-30B-A3B (too large for a fair 24 GiB Air run and for the budget at sensible quants), TwIL-LM3-Pro (non-commercial licence; watchlist only; David asked on 15 Oct to trial it: see [[90 System/briefs/T9b-twil-lm3-pro-trial|T9b]], a follow-up brief; this protocol stays frozen), Gemma 4 E2B (kept in reserve if every candidate misses latency badly: it is the smaller fallback in the same family as #2).

## Selection rule (fixed before measuring)
Applied in this order to **all four models, baseline included**. A model that fails a gate is out; the rule is not changed after results are seen. If it picks nothing, that is the result, and it goes to David.

1. **Eligible:** Apache-2.0 (or another licence allowing the commercial December demo), publisher-issued or verified-provenance file matching the manifest, loads on **the single pinned build every candidate runs on** (protocol), runs fully offline under the no-network sandbox.
2. **Safe (hard gate)** on the 10 dev cases, in both scored blocks: zero invented citation ids; zero answers that cite evidence for a claim the evidence does not make; both unanswerable cases declined in substance. **A violation found by either reviewer fails the gate** (the lead and Codex judge independently; disagreements are listed for David). A malformed or timed-out reply has no answer to judge: it is never a decline, so on an unanswerable case it fails the gate; on an answerable case it is simply not correct (step 3).
3. **Quality score Q:** of the 8 answerable dev cases, the number answered correctly *and* citing supporting evidence **in both blocks**. A case counts only if the lead and Codex, judging independently (Codex without seeing the lead's verdicts), both mark it correct; disagreements are listed for David and count as not correct.
4. **Quality band:** let Q_max be the highest Q among models that passed 1–2. The band is every such model with **Q ≥ Q_max − 1** (anchored to the best score, so it is not a chain of pairwise ties).
5. **Latency band, then the pick:** let P_min be the lowest Air p95 (n = 20, below) in the quality band. The latency band is every model in the quality band with **p95 ≤ 1.10 × P_min** (anchored, not pairwise). Within it, pick the lowest peak server RSS; then the smaller file; then the model id in alphabetical order. Each step is a single ordering, so the order of comparison cannot change the winner.
6. **Report against D56:** say whether the pick's Air p95 is under 8 s. The Air is not the acceptance host (D53), so this neither passes nor fails D56; if it is over 8 s, the gap is evidence for the host decision (Q30), which is David's.

The reserved acceptance cases are **never run** here: they belong to P2.1's independent review. **Running-domain cases are excluded** from this comparison: platform dev cases only, and the results say so.

## Measurement protocol (frozen)
Stated here in full, independent of the P2.2 results note, which is **uncommitted and parked under review** (5 Oct). Its sweep left **throttling versus contention unresolved**; this protocol controls order and drift instead of assuming either.

- **Pipeline:** P2.2 as in run B: the three-file `devcases` corpus, lexical retrieval, **4 chunks, `max_tokens` 320**, the P2.2 prompt (not the MVP prompt), each model's own chat template, temperature 0, seed 42, prompt cache off, thinking off where the model has it.
- **Server:** context 4096, `-np 1`, `-t 4`, `-ngl 99`, flash attention and batch sizes at the build's defaults (the sweep showed no gain from changing them).
- **Runtime:** **every model, baseline included, on one pinned build.** b11146 if it loads all four; otherwise one newer release that loads all four, pinned in the manifest, and everything is measured on it. If the build has to change after measuring has started, all blocks are discarded and the comparison restarts.
- **Block:** one model, one warm-up request (a fixed question outside the dev set, not scored, not timed), then the 10 dev cases once each, in a fixed order.
- **Order (9 blocks):** B0 · C1 · C2 · C3 · B0 · C3 · C2 · C1 · B0, where B0 is the baseline. Each candidate runs twice (once in each half). **The baseline's scored blocks are the first and the last** (positions 1 and 9), which bracket the run as the candidates' two blocks bracket its middle; the middle baseline (position 5) is a drift check only and is never scored.
- **Cool-down:** 180 s idle before every block. Machine state (load averages, `memory_pressure`, top five CPU processes) is recorded before and after each block. David is asked not to run heavy work during the window.
- **Drift:** the reference is the p50 of the first baseline block. After the baselines at positions 5 and 9, compare each with it. If one differs by more than 25 %, re-run **once** the blocks since the previous baseline, then that baseline again. **The re-runs replace the originals for scoring**; every attempt is kept as evidence. If the repeated baseline still differs by more than 25 %, **no pick is made**: the results are reported as drift-affected and the decision goes to David. Drift never quietly changes the outcome.
- **Memory:** server RSS sampled with `ps` every 0.25 s for the whole run; a model's **peak RSS is the maximum over its two scored blocks only**.
- **What counts:** only scored blocks (each candidate's two, the baseline's positions 1 and 9, or the re-runs that replaced them) feed safety, Q, latency and RSS. Warm-up requests, the drift-only baseline and superseded blocks never do; they are kept as evidence.
- **Aggregation:** per model, n = 20 (its 2 scored blocks × 10; for the baseline, positions 1 and 9), **nearest-rank p50 and p95 (rank = ⌈q·n⌉)**. A malformed reply or a timeout (120 s) counts as not correct for Q and enters latency with its elapsed time.
- **Report:** per model p50/p95 with n, prompt-reading and generation tokens/s separately, peak server RSS, per-case verdicts (lead and Codex), all pins (model, runtime, prompt, corpus, request), and the rule applied step by step.
- **Pre-run manifest, written before the first block** to `dbrain-runtime/artifacts/`: the `dbrain-runtime` commit the run uses, the corpus version hash, the request signature, the case order, the warm-up question, the server flags, and the model and runtime pins. A run whose code, corpus or request version differs from its manifest is void. The comparison starts only after P2.2 has passed review and is committed, so the pipeline it measures is a fixed commit, not the parked working tree.
- **Boundaries:** network blocked (sandbox profile as in run B), provider keys unset, outputs only to `dbrain-runtime/artifacts/` through the write guard.

## Files in scope
- `~/Work/dbrain-runtime/` (code, experiments, `artifacts/`); model files outside the vault next to the existing ones.
- A new dated results note in `10 Projects/AI Second Brain/02_Architecture/` (`review_status: draft`, as Q7), with its `index.md` / `log.md` entries.
- This brief; TASKS T9 and M6 lines; `90 System/for-david.md` (the result and the duplicate-file question go to the queue).
- Session-close bookkeeping, the lead's lane (AGENTS.md): `PROGRESS.md` and `PROGRESS-archive.md`, `90 System/handoff.md` (added 8 Oct, session 39; the protocol is unchanged).
- **Not in scope until David confirms:** `30 Resources/Local AI/` (benchmark ledger, text-and-vision). Q8 authorises bounded downloads and Q7 a draft results note; neither authorises new structured knowledge in 30 Resources (rule 8). The lead proposes those rows in the queue.

## Inputs / context to read first
- D56 (targets), D53 (host), D64 (model policy: this is the *runtime* model, chosen by evals, not by D64), Q8 (budget).
- [[90 System/briefs/P2.2|P2.2]] and its results note; the 1 Oct benchmark and comparison notes.
- [[30 Resources/Local AI/text-and-vision|text-and-vision]], [[30 Resources/Local AI/sources|sources]].

## Done when (checkable)
1. All four candidates are measured under the protocol, or an excluded candidate has its reason recorded (e.g. does not load on the pinned runtime).
2. Results note written as a draft with the numbers, per-case verdicts and the rule applied step by step; the proposed `30 Resources/Local AI` rows are queued for David, not written.
3. Codex has independently re-judged the per-case verdicts (gate 2 and the quality score) without seeing the lead's verdicts first.
4. The rule's outcome is queued for David in `for-david.md`; nothing changes the default model until he decides.
5. Downloads stayed within 20 GB and every file matches its pin.

## Constraints
- Q8: no file beyond the four named here and the one runtime exception; disk use within 20 GB as counted above; nothing inside the vault.
- **Runtime:** see the protocol: one pinned build for all four models, never a mix.
- Results are development evidence on the Air; no claim of D56 acceptance.
- Commit only after a passing Codex review.

## Open points for David (queued, not assumed)
- None needed to start: the files are named here and fit the M6 budget. The choice of model at the end is his (Done when 4).

## Review
Reviewer: Codex `gpt-6.1-sol`, effort `high`, read-only; David switched the review profile from `gpt-6-astra` on 5 Oct (the AGENTS.md model-policy line is updated in David's own pending commit).

**Round 1 (5 Oct, `gpt-6.1-sol`): FAIL**. Blockers: ambiguous selection order and non-transitive ties; protocol not fixed (cap, chunks, cool-down, drift, aggregation, reviewer disagreements, running cases); runtime confounding; for-david and 30 Resources outside scope or approval. Should-fixes: the parked P2.2 dependency, disk-based budget and a pre-download manifest with full hashes, QAT wording, a log entry. Nit: "before any result is seen". **All addressed in this revision:** the rule is now a fixed filter order with a band anchored to the best score and the baseline a full contender; the protocol is frozen in full; one build for all; Resource rows queued, not written; disk table and manifest; QAT as publisher rationale; log entry added.

**Round 2 (5 Oct, `gpt-6.1-sol`): FAIL.** Blockers: the baseline's three blocks against "both blocks" and n = 20; pairwise 10 % latency ties; drift re-runs without an aggregation rule. Should-fixes: safety disagreements and malformed replies; a pre-run manifest; the reviewer-model change; prefix length. **Addressed:** the baseline's scored blocks are positions 1 and 9 (5 is drift-only); the latency band is anchored to the fastest p95 with a single ordering after it; re-runs replace originals, all attempts kept, persistent drift means no pick; either reviewer's safety finding fails the gate and a malformed reply is never a decline; a pre-run manifest pins code, corpus, request, order and warm-up, and the comparison waits for P2.2 to be committed; the reviewer switch is recorded; "8-character prefixes".

**Round 3 (5 Oct, `gpt-6.1-sol`): PASS.** No blocker. Should-fixes applied before commit: RSS sampling and window frozen; which blocks count stated; the log summary matched to the latency-band rule. Nit: review history kept together with per-round models.

**Run report, 8 Oct (session 39), Codex `gpt-6.1-sol`, high, read-only, Tier 2, checked against the raw evidence.** Round 1 FAIL: five blockers (session-close files outside the scope list; prompt-token range wrong; whisper figure stated as a ceiling; the 30B layer-6 illustration presented categorically in Q85's options; an unsourced "within noise" claim), two should-fixes (exact URL for the €3,649 price, €3,429 marked as a calculation; "two blind judges" → only Codex was blind), one nit (archive catalog 1–35). All fixed. Round 2 PASS; one should-fix (this review record), applied. Reviewer's limitation: the retailer page for €3,649 was unreachable from its sandbox, so that price was checked by the lead only (8 Oct) and should be re-checked on apple.com/fr when ordering. **Q85 revision (8 Oct, after David: Belgium, SRL, Carlsbad):** round 1 FAIL (blocker: tax claims unsourced; should-fixes: assumptions missing from the summaries, sources not reproducible), fixed; round 2 PASS (should-fix: exact ECB source, applied). Codex `gpt-6.1-sol`, high, read-only.

## Outcome
**6 Oct:** run `2026-10-06-a` stopped after 2 of 9 blocks by David's clean-up directive; no result. Its two blocks are void for the comparison (the runner has since changed); the protocol restarts from block 1.

**Readiness, 8 Oct (session 37; handoff 8 Oct ~09:35, item 2). Nothing scored.**
- **Runner:** `experiments/t9_compare.py` (the 6 Oct draft) reviewed against this brief: rounds 1–3 FAIL (8, 5, 4 blockers: timeouts and malformed replies lost their timing, the server ran outside the no-network sandbox, the network check failed open, unrestricted output paths, no check of code/corpus/cases against the manifest, incomplete RSS measurement, warm-up not required), all fixed; **round 4 PASS**, no findings. Committed `ae934d5` on `main`, pushed. The protocol text is unchanged; the runner now enforces it. A run whose code, corpus (as each request used it), request signature or case contents differ from its pre-run manifest stops as void.
- **Pins:** the four model files and `llama-server` b11146 match their full SHA-256 pins (`7485fe6f…`, `00fe7986…`, `676c3507…`, `33e7a72c…`; runtime `41df13c1…`). No download.
- **Loads on b11146 under the sandbox, warm-up answered** (dry check `artifacts/t9/dry-2026-10-08-final`, from the clean `ae934d5` checkout; warm-up only, no dev case run): B0 6.6 s, C1 7.7 s, C2 6.9 s, C3 12.5 s; whole-process peak RSS during load and warm-up about 3.0, 3.0, 5.1 and 4.7 GiB (not the scored peak). Network denial proven by a loopback probe (EPERM inside the profile, connected outside).
- **Pipeline vs the 6 Oct pin:** runtime `c8b3b7b` → `53e5740` changed only paths (vault, bench) and added the MVP service; request signature unchanged (`3e00bced79dc`).
- **Corpus:** version `d2059877f5ba` → `878a08ea6f57`: `data-policy.md` (v0.6: version note, §7a failure store) and `AGENTS.md` (push wording) changed; the roadmap did not. **Dev-case re-check, the rule unchanged:**
  - `client_policy`: expected answer unchanged (No: local inference does not relax the policy); its fragment now sits in `data-policy.md:7-20` (lines shifted by the v0.6 note). New distractor: §7a ("a local store on the host … readable only by the local model and by David") could tempt a "yes, if local" answer; it is about failed questions, not client files. A retrieval miss already on 6 Oct.
  - `media_storage`: the §7a chunk (`data-policy.md:107-110`) also contains "outside the vault", so a model citing §7a would match the fragment with evidence about the failure store, not about PDFs. The judges' gate 2 (evidence must support the claim) applies.
  - `source_retention`: its fragment (`40 Archive/Inbox/`) has never been in this three-file corpus (checked back to 1 Oct), so no model can cite it; a miss on 6 Oct too. Not new; it costs every model the same case.
  - The other seven (two of them abstention cases, with no fragment): unchanged; fragments present.
- **Go/no-go (by 18:00, in [[90 System/for-david]]): GO for Fri 9 Oct**, on the window conditions: Air plugged in and quiet, the phone service (`Ask Brain.command`, its own model server on 18087) stopped for the window, about 60 min (9 blocks with 180 s cool-downs), up to about 2 h with drift re-runs.

**Q81 answered (a), 8 Oct (session 38), recorded as D102:** GO; David moved the window from Fri 9 Oct to **Thu 8 Oct, start 13:00** (to Cowork at 10:50, the time to the lead at 10:53). The lead finishes and commits the weekly-review fixes and stops all Codex calls by 12:45, checks the window conditions with David before block 1, and wraps the whole run in `caffeinate -dimsu`.

**Run `2026-10-08-a`, 8 Oct (session 39). Measured and judged; the choice is David's (Q84, Q85).** Full report: [[10 Projects/AI Second Brain/02_Architecture/t9-model-comparison-2026-10-08|results note]].
- **Window:** David confirmed the conditions at the start (on power, lid open, Low Power Mode off, `Ask Brain.command` stopped, no heavy work, no Codex calls); started on David's go at about 14:00 (D102 had planned 13:00). Run 14:00:53–14:45:45 under **`caffeinate -dimsu`**. Pins, code, corpus and the pre-run manifest re-checked against `dry-2026-10-08-final` before block 1: all match. David told the Air was free at 14:46.
- **Protocol:** 9/9 blocks `ok`, no void block, no timeout or malformed reply; drift −0.3 % at positions 5 and 9 (no re-run). Done when 1 met: all four measured.
- **Numbers (n = 20 each):** p95 B0 15.71 s, C1 18.21 s, C2 10.13 s, C3 23.74 s; peak server RSS 5.07, 5.47, 5.72, 7.05 GiB.
- **Judging:** the lead judged first and saved its verdicts; then Codex `gpt-6.1-sol`, effort `high`, read-only, judged a masked packet without the lead's verdicts (Done when 3). Safety: B0 and C1 fail on both judges; C3 fails on one Codex-only finding; C2 passes. Q(C2) = 5.
- **Rule outcome: C2 (Gemma 4 E4B QAT Q4_0).** p95 over 8 s on the Air (D56 reported, not decided). Queued as **Q84** (adopt the default, Resources rows) and **Q85** (host sizing by D95, recommendation Mac mini M5 Pro 64 GB / 1 TB from Apple Belgium through David's SRL, €3,669, €3,032 ex VAT; Carlsbad added as an option at David's request, ≈ €3,081–3,096 with the sales tax, assumed non-recoverable (`unverified`)) (Done when 4). Done when 5: no download; every file matched its pin.
- **Sources for Q85:** whisper.cpp memory table, README of `github.com/ggml-org/whisper.cpp` (read 8 Oct); Apple France prices, MacGeneration, "Apple lance les Mac mini M6 et M5 Pro" (Aug 2026, `macg.co/mac/2026/08/apple-lance-les-mac-mini-m6-et-m5-pro-310587`); 64 GB / 1 TB (M5 Pro 18-core CPU / 20-core GPU) at €3,649, Fnac and Darty, `labonneconfig.fr/prix-mini-pc/apple-mac-mini-m5-pro-64-go-1-to` (prices updated 8 Oct); €3,429 is a calculation, not a verified configuration; configuration list, apple.com/fr/shop/buy-mac/mac-mini (read 8 Oct; prices not shown there). TTS and service memory are `unverified` estimates (no model named). Added later on 8 Oct (David: he is in Belgium, buys through his SRL and recovers the VAT, and can buy in Carlsbad): Apple Belgium base prices read on apple.com/be-fr (€2,019 / €2,239); Apple US base $1,899 read on apple.com; US total $3,199 and Belgian €3,669 from `themacindex.com/products/mac-mini/m5-pro-18-core-64gb-1tb` (prices updated 4 Oct, read 8 Oct); Carlsbad sales tax 7.75 % (8.25 % in zip 92008), `salestaxhandbook.com/california/rates/carlsbad`; EUR/USD 1.1186, ECB euro reference rate of 8 Oct, read by the lead on 8 Oct from `ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/eurofxref-graph-usd.en.html` (7 Oct: 1.1177; the reviewer's read of the index page showed only 7 Oct, so the 8 Oct value is the lead's reading). Tax treatment (sales tax not recoverable by the SRL, import VAT recoverable, 0 % duty, deduction needing professional use) is `unverified`. Apple's configurator prices could not be read without a browser session; computer use was not available in this session.
- **Evidence:** `dbrain-runtime/artifacts/t9/run-2026-10-08-a/` (with `judging/`), outside the vault, not committed (Q23).
