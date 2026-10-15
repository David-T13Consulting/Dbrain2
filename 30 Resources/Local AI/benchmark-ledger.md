---
classification: internal
review_status: codex-reviewed
created: 2026-10-01
last_reviewed: 2026-10-15
next_review: 2026-10-22
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
| EmbeddingGemma 2 (Google) | Publisher-reported MTEB Mean(Task): Multilingual v2 61.36 (predecessor 61.15), English v2 68.46 (69.67), Code v1 78.68 (68.76); Apache-2.0. Added at David's request after this run; detail and sources in [[30 Resources/Local AI/embeddinggemma-2-evaluation]] | Publisher-reported, not reproduced; significance unknown; not rankable against Qwen3-Embedding from these numbers. Local test only under [[90 System/briefs/M6b-embedding-eval\|M6b]] |
| Runtimes | llama.cpp: pre-release b11435 (6 Oct) and release tagged v0.6.0 (5 Oct) per the releases page; notes mention Gemma 4 prefetch work and Apple-GPU Metal flash-attention / matmul kernels (publisher claim up to ~3x for speculative and batched decoding). mlx-lm latest read v0.31.3 (22 Apr; adds Gemma 4 in 0.31.2); whisper.cpp v1.9.4 (11 Sep). | Release pages read through a summarizing fetch, not release notes line by line; GitHub API returned 403. Our measured llama.cpp build is not compared or upgraded |

**License and David's wish (added at landing, 8 Oct):** David calls the POC non-commercial and wants TwIL-LM3-Pro in the demo (D99 in [[10 Projects/AI Second Brain/PROGRESS]]). Whether the license covers that is unresolved: [LICENSE §3.3](https://huggingface.co/webAI-Official/TwIL-LM3-Pro/blob/4214aaa4020cd51ac418dc6c7243c076665a811d/LICENSE.md) (rev `4214aaa4`) limits use to non-commercial research and education, and the December demo supports consulting sales. Written confirmation from webAI or a lawyer's read is advisable before the model appears in any client-facing demo.

**Shortlist for a separate bounded run (no weights downloaded here):**

1. **TwIL-LM3-Pro Q4_K_M or Q8_0 GGUF (official repo), research use only.** Reason, `unverified`: a hypothesis that its publisher-reported formal-logic results transfer to rule application and evidence checking (S5); no source measures that transfer. Small enough for the M2. Its status in [[90 System/briefs/T9-M6-model-comparison|T9/M6]] stays **watchlist only**: David's wish to use it (D99) does not establish that the license allows the demo, does not add it to T9's candidates and does not authorise a download. Conditions: David resolves the license question first; hash-pinned download inside the M6 budget; same cases as Qwen3.5-4B; at least 2048 output tokens, temp 0; reject if it cannot answer plainly outside formal logic, since the card says it is not a general assistant.
2. **Gemma 4 E4B-it (Apache-2.0, unchanged revision `ee0ef602`).** Reason: a different model family against the Qwen baselines, which the 1 Oct report asked for; llama.cpp and mlx-lm both list Gemma 4 support. Compare citation support, French/English and latency on the frozen cases.

**Gaps:** IBM Granite, Gemma 4 12B assistant variant card, Kokoro/Whisper/Parakeet release notes beyond revision/date checks, Stability, Microsoft, Apple and other publishers outside the register were not reviewed. No image/ASR/TTS recipe changes could be assessed from metadata alone. Duration of this run: not recorded. Metadata and revision checks do not complete step 2's review of publisher collections and release notes; that review is outstanding for this week.

## 2026-10-15 — weekly review (second scheduled run)

Checked 15 Oct (fired 08:00 UTC; scheduled 06:52 UTC) from primary sources through a summarizing fetch tool: Hugging Face model API, listings, commit and discussion pages, GitHub release pages. **No missed week** (previous run 8 Oct). Evidence type: **publisher metadata and registry pages only; nothing reproduced locally.** **Local benchmark not run this week:** no authorized bounded experiment was set up, and the run may not download weights. Fetch results were summarized by a small model; where two readings disagree, both are recorded and the point is marked unresolved.

**Material change: none established.** Items below are new observations or unresolved conflicts.

| Item | Observation (retrieved 15 Oct) | Evidence type / limits |
|---|---|---|
| TwIL-LM3-Pro (webAI), revision | Model API still returns sha `4214aaa4` (`4214aaa4020cd51ac418dc6c7243c076665a811d`), lastModified 2026-09-30T17:37Z. Commit list head is `4214aaa` "Update README.md"; 16 commits, from the 3 Sep initial commit to the model-card edits and renames already described on 8 Oct. **Conflict:** the Hugging Face search listing shows lastModified 2026-10-09T18:12Z for the same repo. No commit explains it; it may reflect non-commit activity. Unresolved; re-fetch the raw API response next week | Registry metadata. Model card benchmarks unchanged and **vendor-only**; no independent evaluation found (a web search returned only orcarouter.ai pages, which are secondary commentary and not evidence) |
| TwIL-LM3-Pro license | `webAI Non-Commercial License ver. 1.0` (`other`) unchanged. LICENSE.md: §2.1 broad copyright grant; §3.3 "only may be used or intended for use non-commercially", defined as "for non-commercial research and educational purposes only"; §3.5 trademark use needs webAI's prior written consent. No commercial tier, no permission mechanism and no contact for one on the license, the card, or webai.com. Watchlist: **no change** | Read via fetch summary of the LICENSE page, not verbatim against the pinned revision. Recorded as a fact (9 Oct rule); not legal advice. David's 8 Oct decision stands: POC non-commercial, model wanted in the demo (D99) |
| TwIL-LM3-Pro formats | Same files as 8 Oct on `main`: bf16 safetensors plus GGUF F16, Q4_K_M (2.09 GiB), Q5_K_M (2.43 GiB), Q6_K (2.80 GiB), Q8_0 (3.63 GiB). LiteRT-LM repo unchanged (`bb30df2e`, last modified 2026-10-01). No official MLX | Registry metadata |
| Community conversions of TwIL (provenance not inspected) | `mlboydaisuke/TwIL-LM3-LiteRT` (last modified 2026-10-13); `webmp3/Sakura-TwIL-LM3-Pro-GGUF` (created 2026-10-09); `Soulfate24/TwIL-LM3-Pro-Paretrix` (created 2026-10-08, nature unknown, possibly a derivative); `Neurona/TwIL-LM3-Pro` (2026-10-03); `mradermacher/TwIL-LM3-Pro-GGUF` (last modified 2026-10-07; 8 Oct entry called it static quants only; not re-checked); TwIL-LM3 (non-Pro) MLX conversions by `usermma` (8-bit and fp16, 15 Aug). All declare license `other` | Third-party; unverified provenance, no checksums compared to the official files. The MLX route exists only for TwIL-LM3, not Pro |
| TwIL-LM3 (non-Pro) | Three readings disagree: the 8 Oct register says `145ff05e92c6` modified 2026-10-01; today's model API says sha `e4f94da5` (`e4f94da572d9`), lastModified 2026-09-09; the search listing says lastModified 2026-10-08. Commit page (30 commits, relative dates only): newest `7857a94` "Fix TwIL-LM3 model card references (#3)" about 3 days old; `715bde2` "TwIL-LM3: v5 MGPO weights, normalised tokenizer metadata" about 22 days old (≈ late Sep). Discussions: #1 "benchmaxxed ?" (open, ~21 days, 6 reactions) and #3 (card fix). Downloads 252,498 (popularity, not evidence) | **Revision unresolved**; weights may have changed since 1 Oct (v5 MGPO). Community skepticism is a comment, not a result. Not shortlisted |
| webAI-Official org | 17 repos listed: TwIL-LM3-Pro, TwIL-LM3-Pro-LiteRT-LM, TwIL-LM3, TwIL-LM2, TwIL-LM, granite-4.2-8B (GGUF, Apache-2.0), three granite-4.2-8b LoRA adapters (no license tag), webAI-ColVec1 4b/9b and 1.1 4b/8b (`other`), five `yolo26{n,s,m,l,x}-mlx` object-detection repos (AGPL-3.0, May 2026, first recorded here). **No repo created after 1 Oct.** webai.com: still "The Private Preview is Live" with a waitlist; no pricing, licensing, version pinning or multi-device pooling information | Registry metadata and one page read. Platform claims remain unevidenced |
| Pinned repos re-queried | Sha and license match the register for 8 of 17: Qwen3.5-4B, Gemma 4 E4B-it, Qwen3.8-27B, Qwen-Image-2.1 (last modified 2026-09-30, same sha), Whisper large-v3-turbo, Parakeet v3, FLUX.2-klein-4B, Qwen3-ASR-1.7B | Registry metadata. The other nine were **not re-queried** this week |
| Other publishers (listings, summarized) | Google: Gemma 4 family incl. `gemma-4-12B-it` (created 2026-05-23) and QAT variants, all Apache-2.0, nothing modified after 2026-07-28. Mistral: Ministral 3 unchanged (2026-07-15); `Shieldstral-1.0-3B` (2026-07-16, Apache-2.0, not inspected). IBM: granite-4.2 3B/8B/30B with GGUF, fp8, mxfp4, nvfp4 variants (Aug–Sep, Apache-2.0); `granite-speech-5.0-470m-turboctc` (created 2026-08-04, modified 2026-09-18, Apache-2.0, **not inspected; possible ASR candidate**). Black Forest Labs: nothing newer than April on the listing. Qwen: newest listed item 2026-09-02, but the same listing omits items the 8 Oct entry recorded (PE-T2I/PE-I2I, 20 Sep), so "no new Qwen release" is **weakly supported** | Registry metadata; no benchmark or model-card content read. Listings came through a summarizer and may be incomplete |
| Runtimes | llama.cpp: latest release v0.6.0 (5 Oct), pre-release b11435 (6 Oct); nothing newer than the 8 Oct entry. New detail from the v0.6.0 notes: breaking `llama_batch_ext` API (`llama_process()`), `LLAMA_SESSION_VERSION` bumped to 11 and `LLAMA_STATE_SEQ_VERSION` to 4 (saved sessions/state from older builds will not load), Metal tensor-API flash attention for F16 KV and few-row MMA matmul kernels ("up to ~3x faster on Apple GPUs", publisher claim, not measured here). The notes page was truncated. mlx-lm: still v0.31.3. whisper.cpp: **not checked**. Our measured build (b11146) is not upgraded or compared | Release page read, not line by line; the GitHub API was not used |
| Secondary, not evidence | A third-party roundup (local-ai-zone.github.io, October 2026) lists Cloudflare Clef 27B and Clef-flash 9B (Apache-2.0 weights, 1 Oct), Amazon Strands Decider 2B, and a Google DiarizationLM Gemma 4 E4B GGUF (4 Oct); Microsoft MAI-Voice/Transcribe are API-only; Mistral Large 4 weights only promised. None verified at a primary source | Leads only; check primary pages next week if relevant |

**Superseded interpretations:** the 8 Oct shortlist item "Gemma 4 E4B-it as a second model family" is overtaken by T9 (8 Oct): it was run, passed the safety gate and became the default (D105). Earlier measurements are kept above. The 8 Oct statement that the mradermacher GGUF is "static quants only" is not re-verified.

**Shortlist for a separate bounded run (no weights downloaded here; max two):**

1. **TwIL-LM3-Pro Q4_K_M GGUF (official repo, `4214aaa4`), non-commercial POC use.** Reason, `unverified` hypothesis: its publisher-reported formal-logic strength (Track A macro 0.5539 vs 0.4313 for its base, vendor-only) may transfer to the rule-based evidence checking of S5; no source measures that. 2.09 GiB, so it fits beside the default on the M2 (a 3.66B-parameter model). Remains **watchlist only** in [[90 System/briefs/T9-M6-model-comparison|T9/M6]] until a brief names it; this note authorises no download. Conditions: hash-pinned file, same frozen cases as the Gemma 4 E4B default, temp 0, at least 2048 output tokens, and reject if it cannot answer plainly outside formal logic.
2. **Gemma 4 E2B-it QAT (Google, Apache-2.0; exact GGUF artifact to be confirmed).** Reason, engineering estimate: the current default (E4B) misses the 8 s p95 target in the P2.2 note (T9 p95 10.13 s); a same-family, smaller model on the same runtime tests whether latency can drop without losing the safety gate. Not measured here; E2B was not tested in T9.

**Gaps (not checked this week):** whisper.cpp release notes; Kokoro, Qwen3-TTS, Z-Image, FLUX.1-schnell and the embedding/reranker pinned repos (nine of 17 not re-queried); model-card content for Granite 4.2, Granite speech, Shieldstral and Gemma 4 12B; Stability, Microsoft and Apple publishers; independent reproduction of any TwIL result. Duration of this run: not recorded.

## 2026-10-08 — T9/M6 measured on David's M2 / 24 GiB

Frozen protocol, 10 platform dev cases, two scored blocks per model (n = 20), llama.cpp b11146, context 4096, temperature 0, `--reasoning off`. Development evidence on the Air, not the acceptance host. Detail, per-case verdicts and the rule: [[10 Projects/AI Second Brain/02_Architecture/t9-model-comparison-2026-10-08|T9 results]].

| Model (file) | p50 / p95 | Prompt / generation tok/s | Peak server RSS | Safety gate · Q (of 8) |
|---|---|---|---|---|
| Qwen3-4B Q4_K_M | 8.38 / 15.71 s | 245 / 27.7 | 5.07 GiB | fail · 5 |
| Qwen3.5-4B Q4_K_M (unsloth) | 11.17 / 18.21 s | 231 / 23.6 | 5.47 GiB | fail · 3 |
| **Gemma 4 E4B-it QAT Q4_0** (google, rev `4b4a2c1d`) | **7.98 / 10.13 s** | 238 / 27.1 | 5.72 GiB | **pass · 5**, picked; adopted as default (D105) |
| Ministral 3 8B Instruct 2512 Q4_K_M (mistralai, rev `0102285a`) | 15.58 / 23.74 s | 126 / 15.3 | 7.05 GiB | fail (one reviewer finding) · 5 |

Q counts a case only when both judges (lead and Codex, blind) mark it correct in both blocks. Answers were identical across blocks, so n = 20 measures latency only. Ten cases on a three-file corpus: a one-case difference in Q is not tested for significance.

## What future weekly entries must record

For published results: exact model/checkpoint, benchmark/version/split, score/unit/direction, evaluator, source URL and revision, publication date if established, retrieval date, inference/harness details and unresolved gaps. When details are missing, write “not reported”; do not imply comparability.

For local runs: model and runtime hashes, quantization, hardware/OS, context/output budget, prompt and corpus versions, language/mode, case count, development/acceptance status, cold/warm setup, concurrency, memory pressure, first-output and full latency, resource measurements, quality failures and artifact path. Model quality and runtime performance need separate interpretation.

For retrieval, measure expected-evidence recall and source support; for ASR, WER/CER and critical errors; for TTS, listening quality and first-audio delay; for images, adherence/edit preservation and seconds per image at fixed settings. Small samples cannot substantiate rare-error rates.

Refresh process: [[90 System/weekly-local-model-review]].
