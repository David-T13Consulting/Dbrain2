---
classification: internal
created: 2026-10-01
last_reviewed: 2026-10-01
next_review: 2026-10-08
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

## What future weekly entries must record

For published results: exact model/checkpoint, benchmark/version/split, score/unit/direction, evaluator, source URL and revision, publication date if established, retrieval date, inference/harness details and unresolved gaps. When details are missing, write “not reported”; do not imply comparability.

For local runs: model and runtime hashes, quantization, hardware/OS, context/output budget, prompt and corpus versions, language/mode, case count, development/acceptance status, cold/warm setup, concurrency, memory pressure, first-output and full latency, resource measurements, quality failures and artifact path. Model quality and runtime performance need separate interpretation.

For retrieval, measure expected-evidence recall and source support; for ASR, WER/CER and critical errors; for TTS, listening quality and first-audio delay; for images, adherence/edit preservation and seconds per image at fixed settings. Small samples cannot substantiate rare-error rates.

Refresh process: [[90 System/weekly-local-model-review]].
