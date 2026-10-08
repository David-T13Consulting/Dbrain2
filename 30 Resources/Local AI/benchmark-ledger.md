---
classification: internal
created: 2026-10-01
last_reviewed: 2026-10-08
next_review: 2026-10-15
---
# Local AI benchmark ledger

Append dated observations; retain earlier results. A new model card, a publisher benchmark and a measurement on this Mac are different evidence. “Checked this week” is not “released this week.”

## 2026-10-01 — initial published snapshot

These are **publisher-reported**, not reproduced here. References resolve to model cards; [[30 Resources/Local AI/sources]] pins the revisions observed. Values retain their reported scales. Do not form a cross-family ranking from differing inference budgets, benchmark versions or harnesses.

| Model | Published result observed | Interpretation / limitation |
|---|---|---|
| [Qwen3.5-4B](https://huggingface.co/Qwen/Qwen3.5-4B) | MMLU-Pro 79.1; IFEval 89.8; LiveCodeBench v6 55.8 | Knowledge, instruction and code signals; not the Q4/non-thinking vault configuration we measured |
| [Gemma 4 E4B](https://huggingface.co/google/gemma-4-E4B-it) | MMLU Pro 69.4%; LiveCodeBench v6 52.0% | Publisher's instruction-tuned evaluation; reasoning recipe and quantization differ from our experiments |
| [Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B) | SWE-bench Pro 61.7; Terminal Bench 2.1 / Terminus 73.0 | Agent/harness results, not just raw-model performance; not a forecast for the M2 |
| [Qwen3-ASR-0.6B](https://huggingface.co/Qwen/Qwen3-ASR-0.6B) | LibriSpeech clean/other WER 2.11 / 4.55; FLEURS-en 4.39 | Lower WER is better. English datasets do not establish French dictation quality |
| [Qwen3-ASR-1.7B](https://huggingface.co/Qwen/Qwen3-ASR-1.7B) | Same publisher table: LibriSpeech clean/other WER 1.63 / 3.38; FLEURS-en 3.35 | Useful within-table accuracy comparison; local speed/memory not measured |

No comparable local image or speech-synthesis benchmark exists yet. Leave those cells unmeasured rather than using marketing latency or attractive samples as scores. Do not silently transfer TTS Base-model scores to CustomVoice checkpoints.

## 2026-10-01 — measured on David's M2 / 24 GiB

| Configuration | n | Median / observed max response | Citation-ID syntax | Evidence |
|---|---:|---|---|---|
| Qwen3-4B Q4_K_M, initial prompt | 16 (8 cases repeated) | 6.37 / 9.72 s | 8/16 | [[10 Projects/AI Second Brain/02_Architecture/local-benchmark-2026-10-01|First report]] |
| Qwen3-4B, prompt-v2 | 8 | 6.76 / 12.28 s | 7/8 | Same report; development tuning |
| Qwen3.5-4B Q4_K_M, unchanged prompt-v2 | 8 | 7.41 / 9.58 s | 1/8 | [[10 Projects/AI Second Brain/02_Architecture/local-comparison-retrieval-2026-10-01|Comparison report]] |
| Qwen3.5-4B, lexical retrieval + explicit-citation prompt | 10 | 6.14 / 7.97 s | 8/10 | Different questions/context/prompt; not directly comparable |

All are development runs, not held-out acceptance. Timings are generation API latency, not full voice/remote interaction. A syntactically valid citation can support a wrong claim: the archival answer demonstrates that failure. The last row's retrieval evidence coverage was 6/7 in-corpus answerable questions, qualitatively reviewed by Codex.

## 2026-10-08 — weekly review (first scheduled run)

Checked 8 Oct from primary sources (Hugging Face model APIs/cards, GitHub release pages). **No missed weeks.** Evidence type: **publisher-reported or registry metadata only; nothing reproduced locally.** Local benchmark not run this week: no authorized bounded experiment was set up, and the run may not download weights.

**Unchanged:** all 17 pinned repositories in [[30 Resources/Local AI/sources]] still resolve to the revisions recorded on 1 Oct, with the same declared licenses. No corrected results, deprecations or license changes found for them.

**New or changed (watchlist and others):**

| Item | Observation (retrieved 8 Oct) | Evidence type / limits |
|---|---|---|
| TwIL-LM3-Pro (webAI) | Source repo `4214aaa4`, last modified 2026-09-30; card edits since creation on 3 Sep only add comparison rows (Qwen3.5-4B, a VibeThinker variant) and rename the model. Benchmarks, **vendor-only**: Track A (formal logic, n=200 per lane, greedy, 2048 new tokens with one retry at 4,096 for truncated rows, thinking on, seed 42) macro gate 0.5539 vs 0.4313 for its Granite 4.2 3B base, Qwen3-8B 0.5336, with the card itself calling the lead over Qwen3-8B within sampling noise. Track B (held-out, n=300 per dataset, greedy, generation capped at 4,096 tokens, thinking off, vLLM): 10-dataset macro 0.7901 vs 0.7942 base; does not lead the table. Harness: bf16, vLLM 0.19.1 on one H200. The card's 11.1 "ans/s" is a **derived** figure (decode tokens/s ÷ mean generation length, from a separate forced-decode protocol: 128 prompts × 512 tokens, EOS ignored), not a measured rate of completed requests. Scores measured inside 8,192 tokens | Publisher-reported, not reproduced. Card states code and tool-use were not run; FOL translation exact match 0.0100; `rule_induction` parses 56.5% |
| TwIL-LM3-Pro formats | The official source repo itself ships GGUF (Q4_K_M 2.09 GiB, Q5_K_M, Q6_K, Q8_0, F16) plus bf16 safetensors. LiteRT-LM bundle repo (`bb30df2e`, created 2026-10-01): INT4 2.19 GB, INT8 3.76 GB, context capped at 4,096, requires LiteRT-LM 0.16+. Bundle card reports **no scores**, only a Linux-CPU smoke test; no device speed measured. Community GGUF (mradermacher) remains static quants only | Corrects the 2 Oct watchlist wording "official bundles are LiteRT-LM only": GGUF is official. llama.cpp guidance in card: `--temp 0`, `-cnv`, at least 2048 output tokens (thinking block) |
| TwIL-LM3-Pro license | `webAI Non-Commercial License ver. 1.0` unchanged. LICENSE.md text read: grant limited to "non-commercial research and educational purposes only"; no commercial option and no internal-business-use clause; derivatives must carry the same limit; termination on breach. No commercial tier found | Not legal advice. **A December consulting demo is not clearly covered**; David to decide. Queued by the lead and answered: see the license paragraph below (D99) |
| TwIL-LM3 / TwIL-LM / TwIL-LM2 (webAI) | TwIL-LM3 (3.08B, SmolLM3-3B base, same non-commercial license, GGUF available); card mentions TwIL-LM3.1 and an unreleased TwIL-LM3\*. TwIL-LM2 (`webAI-Official/TwIL-LM2`, rev `d3378167`): repo created 2026-09-29 per the Hugging Face API; base `ibm-granite/granite-3.3-2b-instruct` per its card (frontmatter `base_model` and model table). Not the same as the earlier TwIL-LM2 GGUF files in `webAI-Official/TwIL-LM` (rev `39dc16b4`, created 2026-07-23, base SmolLM2-1.7B-Instruct), which the TwIL-LM2 card itself calls "the earlier, SmolLM2-1.7B-Instruct-based TwIL-LM2". Smaller and older siblings of Pro | Publisher-reported; no independent evaluation found. Not shortlisted |
| webAI other | Granite 4.2 8B mirrors and three LoRA adapters (analyst/builder/researcher; no license tag) created 30 Sep; webAI-ColVec1.1-4b/8b visual-document retrievers (Qwen3.5-based, license `other`, Aug). webai.com shows only "Private Preview is Live"; no pricing, licensing, pinning or multi-device pooling information | Unverified; platform claims still unevidenced |
| Qwen-Image-2.1-PE-T2I / PE-I2I | Created 20 Sep. Fine-tuned Qwen3.5-VL 9B (BF16) that rewrites vague generation/edit instructions into precise prompts for Qwen-Image-2.1. Qwen Research License. No benchmarks; CUDA/transformers instructions only. Parent `Qwen-Image-2.1` unchanged (`d26bb612`) Revisions: PE-T2I `f3ed7985` (last modified 2026-09-20), PE-I2I `72927bc0` (last modified 2026-09-20) | Publisher metadata; extra 9B model on top of the 7B generator is a memory cost on a 24 GiB Mac |
| Qwen-Drive-1.0-4B | Created 27 Aug, Apache-2.0, driving-specific VLM on Qwen3.5-4B; general ability reported roughly on par with the base (MMBench 85.5 vs 87.1, MMMU 72.7 vs 73.4) | Author-reported. Not relevant to this project |
| Runtimes | llama.cpp: pre-release b11435 (6 Oct) and release tagged v0.6.0 (5 Oct) per the releases page; notes mention Gemma 4 prefetch work and Apple-GPU Metal flash-attention / matmul kernels (publisher claim up to ~3x for speculative and batched decoding). mlx-lm latest read v0.31.3 (22 Apr; adds Gemma 4 in 0.31.2); whisper.cpp v1.9.4 (11 Sep). | Release pages read through a summarizing fetch, not release notes line by line; GitHub API returned 403. Our measured llama.cpp build is not compared or upgraded |

**License and David's wish (added at landing, 8 Oct):** David calls the POC non-commercial and wants TwIL-LM3-Pro in the demo (D99 in [[10 Projects/AI Second Brain/PROGRESS]]). Whether the license covers that is unresolved: [LICENSE §3.3](https://huggingface.co/webAI-Official/TwIL-LM3-Pro/blob/4214aaa4020cd51ac418dc6c7243c076665a811d/LICENSE.md) (rev `4214aaa4`) limits use to non-commercial research and education, and the December demo supports consulting sales. Written confirmation from webAI or a lawyer's read is advisable before the model appears in any client-facing demo.

**Shortlist for a separate bounded run (no weights downloaded here):**

1. **TwIL-LM3-Pro Q4_K_M or Q8_0 GGUF (official repo), research use only.** Reason, `unverified`: a hypothesis that its publisher-reported formal-logic results transfer to rule application and evidence checking (S5); no source measures that transfer. Small enough for the M2. Its status in [[90 System/briefs/T9-M6-model-comparison|T9/M6]] stays **watchlist only**: David's wish to use it (D99) does not establish that the license allows the demo, does not add it to T9's candidates and does not authorise a download. Conditions: David resolves the license question first; hash-pinned download inside the M6 budget; same cases as Qwen3.5-4B; at least 2048 output tokens, temp 0; reject if it cannot answer plainly outside formal logic, since the card says it is not a general assistant.
2. **Gemma 4 E4B-it (Apache-2.0, unchanged revision `ee0ef602`).** Reason: a different model family against the Qwen baselines, which the 1 Oct report asked for; llama.cpp and mlx-lm both list Gemma 4 support. Compare citation support, French/English and latency on the frozen cases.

**Gaps:** IBM Granite, Gemma 4 12B assistant variant card, Kokoro/Whisper/Parakeet release notes beyond revision/date checks, Stability, Microsoft, Apple and other publishers outside the register were not reviewed. No image/ASR/TTS recipe changes could be assessed from metadata alone. Duration of this run: not recorded. Metadata and revision checks do not complete step 2's review of publisher collections and release notes; that review is outstanding for this week.

## What future weekly entries must record

For published results: exact model/checkpoint, benchmark/version/split, score/unit/direction, evaluator, source URL and revision, publication date if established, retrieval date, inference/harness details and unresolved gaps. When details are missing, write “not reported”; do not imply comparability.

For local runs: model and runtime hashes, quantization, hardware/OS, context/output budget, prompt and corpus versions, language/mode, case count, development/acceptance status, cold/warm setup, concurrency, memory pressure, first-output and full latency, resource measurements, quality failures and artifact path. Model quality and runtime performance need separate interpretation.

For retrieval, measure expected-evidence recall and source support; for ASR, WER/CER and critical errors; for TTS, listening quality and first-audio delay; for images, adherence/edit preservation and seconds per image at fixed settings. Small samples cannot substantiate rare-error rates.

Refresh process: [[90 System/weekly-local-model-review]].
