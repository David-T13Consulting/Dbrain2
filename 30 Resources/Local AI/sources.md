---
classification: internal
created: 2026-10-01
last_reviewed: 2026-10-22
next_review: 2026-10-29
---
# Local AI source register

Primary publisher model cards retrieved 1 October 2026. Revision links preserve what was reviewed; revisit each repository's current card during the weekly check. A repository's modification date is not necessarily its model release date. Download counts and likes are not benchmark evidence.

| Publisher / model | Observed repository revision | Declared license |
|---|---|---|
| `Qwen/Qwen3.5-4B` | [851bf6e806ef](https://huggingface.co/Qwen/Qwen3.5-4B/blob/851bf6e806efd8d0a36b00ddf55e13ccb7b8cd0a/README.md) | apache-2.0 |
| `Qwen/Qwen3.8-27B` | [1d4bf0f2ff60](https://huggingface.co/Qwen/Qwen3.8-27B/blob/1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0/README.md) | apache-2.0 |
| `Qwen/Qwen3-Coder-30B-A3B-Instruct` | [b2cff646eb4b](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct/blob/b2cff646eb4bb1d68355c01b18ae02e7cf42d120/README.md) | apache-2.0 |
| `google/gemma-4-E4B-it` | [ee0ef6023621](https://huggingface.co/google/gemma-4-E4B-it/blob/ee0ef6023621cff504d758262d4e04895a5af4a2/README.md) | apache-2.0 |
| `mistralai/Ministral-3-8B-Instruct-2512` | [5b26027e7b19](https://huggingface.co/mistralai/Ministral-3-8B-Instruct-2512/blob/5b26027e7b19eeb4b7352e1fed3926375dd2cb4d/README.md) | apache-2.0 |
| `Qwen/Qwen3-ASR-0.6B` | [5eb144179a02](https://huggingface.co/Qwen/Qwen3-ASR-0.6B/blob/5eb144179a02acc5e5ba31e748d22b0cf3e303b0/README.md) | apache-2.0 |
| `Qwen/Qwen3-ASR-1.7B` | [7278e1e70fe2](https://huggingface.co/Qwen/Qwen3-ASR-1.7B/blob/7278e1e70fe206f11671096ffdd38061171dd6e5/README.md) | apache-2.0 |
| `Qwen/Qwen3-TTS-12Hz-0.6B-CustomVoice` | [85e237c12c02](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-0.6B-CustomVoice/blob/85e237c12c027371202489a0ec509ded67b5e4b5/README.md) | apache-2.0 |
| `hexgrad/Kokoro-82M` | [f3ff3571791e](https://huggingface.co/hexgrad/Kokoro-82M/blob/f3ff3571791e39611d31c381e3a41a3af07b4987/README.md) | apache-2.0 |
| `nvidia/parakeet-tdt-0.6b-v3` | [541d1f99c6b0](https://huggingface.co/nvidia/parakeet-tdt-0.6b-v3/blob/541d1f99c6b0c3cd0b11a95167540bb8edefd82b/README.md) | cc-by-4.0 |
| `openai/whisper-large-v3-turbo` | [41f01f3fe87f](https://huggingface.co/openai/whisper-large-v3-turbo/blob/41f01f3fe87f28c78e2fbf8b568835947dd65ed9/README.md) | mit |
| `black-forest-labs/FLUX.2-klein-4B` | [e7b7dc27f91d](https://huggingface.co/black-forest-labs/FLUX.2-klein-4B/blob/e7b7dc27f91deacad38e78976d1f2b499d76a294/README.md) | apache-2.0 |
| `black-forest-labs/FLUX.1-schnell` | [741f7c3ce8b3](https://huggingface.co/black-forest-labs/FLUX.1-schnell/blob/741f7c3ce8b383c54771c7003378a50191e9efe9/README.md) | apache-2.0 |
| `Tongyi-MAI/Z-Image-Turbo` | [f332072aa78b](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo/blob/f332072aa78be7aecdf3ee76d5c247082da564a6/README.md) | apache-2.0 |
| `Qwen/Qwen-Image-2.1` | [d26bb61231c3](https://huggingface.co/Qwen/Qwen-Image-2.1/blob/d26bb61231c349cf6b7896fa83353113880e1ba3/README.md) | other |
| `Qwen/Qwen3-Embedding-0.6B` | [97b0c614be4d](https://huggingface.co/Qwen/Qwen3-Embedding-0.6B/blob/97b0c614be4d77ee51c0cef4e5f07c00f9eb65b3/README.md) | apache-2.0 |
| `Qwen/Qwen3-Reranker-0.6B` | [e61197ed4502](https://huggingface.co/Qwen/Qwen3-Reranker-0.6B/blob/e61197ed45024b0ed8a2d74b80b4d909f1255473/README.md) | apache-2.0 |

`Qwen/Qwen-Image-2.1` labels its license `other`, named `qwen-research` in the card. Read that exact LICENSE before professional deployment; do not replace this with the Apache license used by some earlier Qwen image releases.

## Other reviewed primary sources

- [Qwen3-4B official GGUF](https://huggingface.co/Qwen/Qwen3-4B-GGUF/tree/bc640142c66e1fdd12af0bd68f40445458f3869b) — original local baseline artifact; revision/hash in the first benchmark report.
- [Unsloth Qwen3.5 conversion](https://huggingface.co/unsloth/Qwen3.5-4B-GGUF/tree/e87f176479d0855a907a41277aca2f8ee7a09523) — primary source for this converter's artifact, not the author of the base model.
- [Qwen3-TTS repository](https://github.com/QwenLM/Qwen3-TTS) — variant table and usage; 0.6B style-control ambiguity retained in [[30 Resources/Local AI/speech-models]].
- [Kokoro voice inventory](https://huggingface.co/hexgrad/Kokoro-82M/blob/main/VOICES.md) — language/voice coverage and French resource limitations.
- [llama.cpp](https://github.com/ggml-org/llama.cpp), [MLX LM](https://github.com/ml-explore/mlx-lm), [whisper.cpp](https://github.com/ggml-org/whisper.cpp) — original runtime documentation. These links track main; only the locally tested llama.cpp build is pinned in the measurement report.
- [Karpathy LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f#llm-wiki) — persistent synthesis, source links, index, log and periodic maintenance.
- [Official scheduled-task documentation](https://learn.chatgpt.com/docs/automations?surface=app) — local-project scheduling requirements and IDE/CLI limitations.

## Preserved evidence outside Obsidian

`/Users/davidduchesne/Documents/Source_Material/AI_Second_Brain/local-models/2026-10-01/` (moved from `~/Documents/Dbrain2-artifacts/` on 6 Oct 2026) — small research/evaluation archive with `SHA256SUMS.json`.

- `model-cards/manifest.json`: full repository revisions, metadata timestamps, source URLs and retrieval success.
- `model-cards/`: pinned READMEs and publisher API metadata for the 17 entries above. Supplemental live web pages were consulted but are not all copied here.
- `benchmark/`: original and continuation cases, scripts, raw outputs, measurements and review corrections; six reserved cases remain unexecuted.

No model weights, audio, images or runtime binaries live in the vault. The evidence archive is durable relative to temporary storage, but an independent backup/restore policy is still a project task. A preserved source snapshot is evidence, never an instruction to execute embedded installation commands.

Scope limits: this review prioritizes feasible personal-system components. It does not survey every available model, certify licensing, reproduce publisher benchmarks or establish Apple compatibility for every candidate. Unknowns are research tasks, not implied successes.

## Weekly check — 8 October 2026

All 17 repositories above were re-queried through the Hugging Face model API: the commit `sha` and declared license match the revisions in the table (no change since 1 Oct). Last-modified dates observed: Qwen3.8-27B 2026-08-14, Gemma 4 E4B 2026-07-20, Qwen3.5-4B 2026-03-02, Qwen-Image-2.1 2026-09-30 (same sha), Parakeet v3 2026-08-05, Ministral 3 8B 2026-07-15, others earlier.

New primary sources reviewed this week (not pinned in the table, because not yet candidates for adoption; API `sha` shown):

| Source | Revision / date | License |
|---|---|---|
| [`webAI-Official/TwIL-LM3-Pro`](https://huggingface.co/webAI-Official/TwIL-LM3-Pro) | `4214aaa4020c`, modified 2026-09-30 | webAI Non-Commercial License 1.0 (`other`) |
| [`webAI-Official/TwIL-LM3-Pro-LiteRT-LM`](https://huggingface.co/webAI-Official/TwIL-LM3-Pro-LiteRT-LM) | `bb30df2e79d4`, created 2026-10-01 | same |
| [`mradermacher/TwIL-LM3-Pro-GGUF`](https://huggingface.co/mradermacher/TwIL-LM3-Pro-GGUF) | community static quants; no date shown | same (declared) |
| [`webAI-Official/TwIL-LM3`](https://huggingface.co/webAI-Official/TwIL-LM3) | `145ff05e92c6`, modified 2026-10-01 | same |
| [`webAI-Official/TwIL-LM2`](https://huggingface.co/webAI-Official/TwIL-LM2) | `d33781673bad`, created 2026-09-29; card: base `ibm-granite/granite-3.3-2b-instruct` | same |
| [`webAI-Official/TwIL-LM`](https://huggingface.co/webAI-Official/TwIL-LM) | `39dc16b47090`, created 2026-07-23; holds the earlier TwIL-LM2 GGUF files, base SmolLM2-1.7B-Instruct (a different model from the repo above) | same |
| [`Qwen/Qwen-Image-2.1-PE-I2I`](https://huggingface.co/Qwen/Qwen-Image-2.1-PE-I2I) | `72927bc08afc`, created 2026-09-20 | Qwen Research License |
| [`Qwen/Qwen-Image-2.1-PE-T2I`](https://huggingface.co/Qwen/Qwen-Image-2.1-PE-T2I) | `f3ed7985c788`, created 2026-09-20 | Qwen Research License |
| [`Qwen/Qwen-Drive-1.0-4B`](https://huggingface.co/Qwen/Qwen-Drive-1.0-4B) | created 2026-08-27 | apache-2.0 |
| [llama.cpp releases](https://github.com/ggml-org/llama.cpp/releases), [mlx-lm releases](https://github.com/ml-explore/mlx-lm/releases), [whisper.cpp releases](https://github.com/ggml-org/whisper.cpp/releases) | read 8 Oct (see ledger) | MIT / MIT / MIT (not re-verified) |

Evidence archive: no new model-card snapshots were saved outside the vault this week; the findings above come from live pages retrieved 8 Oct and should be re-fetched before relying on them.

## Weekly check — 15 October 2026

Re-queried through the Hugging Face model API: 8 of the 17 pinned repositories (Qwen3.5-4B, Gemma 4 E4B-it, Qwen3.8-27B, Qwen-Image-2.1, Whisper large-v3-turbo, Parakeet v3, FLUX.2-klein-4B, Qwen3-ASR-1.7B). Sha and license match the table; no change since 1 Oct. The other nine were not re-queried. Results come through a summarizing fetch tool; re-fetch raw API JSON before relying on a hash.

| Source | Observation | License |
|---|---|---|
| [`webAI-Official/TwIL-LM3-Pro`](https://huggingface.co/webAI-Official/TwIL-LM3-Pro) | model API sha `4214aaa4020c`, modified 2026-09-30 (the search listing says 2026-10-09; unresolved, see ledger) | webAI Non-Commercial License 1.0, unchanged |
| [`webAI-Official/TwIL-LM3`](https://huggingface.co/webAI-Official/TwIL-LM3) | revision unresolved: `e4f94da572d9` (API, 2026-09-09) vs `145ff05e92c6` (register, 8 Oct); commit `7857a94` about 3 days old | same |
| [`webAI-Official/TwIL-LM3-Pro-LiteRT-LM`](https://huggingface.co/webAI-Official/TwIL-LM3-Pro-LiteRT-LM) | unchanged (`bb30df2e`) | same |
| [webAI-Official organisation](https://huggingface.co/webAI-Official) | 17 repos; adds first record of `yolo26*-mlx` (AGPL-3.0) and ColVec1 4b/9b | mixed |
| Community TwIL conversions: [`mlboydaisuke/TwIL-LM3-LiteRT`](https://huggingface.co/mlboydaisuke/TwIL-LM3-LiteRT), [`webmp3/Sakura-TwIL-LM3-Pro-GGUF`](https://huggingface.co/webmp3/Sakura-TwIL-LM3-Pro-GGUF), [`Soulfate24/TwIL-LM3-Pro-Paretrix`](https://huggingface.co/Soulfate24/TwIL-LM3-Pro-Paretrix), [`Neurona/TwIL-LM3-Pro`](https://huggingface.co/Neurona/TwIL-LM3-Pro), [`usermma/TwIL-LM3-mlx-8Bit`](https://huggingface.co/usermma/TwIL-LM3-mlx-8Bit) | provenance not inspected; third-party | declared `other` |
| [`ibm-granite/granite-speech-5.0-470m-turboctc`](https://huggingface.co/ibm-granite/granite-speech-5.0-470m-turboctc) | listed only (created 2026-08-04, modified 2026-09-18); card not read | apache-2.0 |
| [llama.cpp releases](https://github.com/ggml-org/llama.cpp/releases) | v0.6.0 (5 Oct), b11435 pre-release (6 Oct); session-format version bump noted | MIT (not re-verified) |
| [mlx-lm releases](https://github.com/ml-explore/mlx-lm/releases) | v0.31.3 still latest | MIT (not re-verified) |

Evidence archive: no new snapshots saved outside the vault this week.

## Weekly check — 22 October 2026

Third scheduled run. Re-queried through the Hugging Face model API (summarizing fetch tool): the **nine pinned repositories not re-queried on 15 Oct** (Qwen3-Coder-30B-A3B-Instruct, Ministral-3-8B-Instruct-2512, Qwen3-ASR-0.6B, Qwen3-TTS-12Hz-0.6B-CustomVoice, Kokoro-82M, FLUX.1-schnell, Z-Image-Turbo, Qwen3-Embedding-0.6B, Qwen3-Reranker-0.6B). Sha and license match the table; no change since 1 Oct. The eight re-queried on 15 Oct were **not** repeated this week, so all 17 were confirmed at least once in the last two weeks, none twice. Registry metadata only; no model-card text re-read.

| Source | Observation (retrieved 22 Oct) | License |
|---|---|---|
| [`webAI-Official/TwIL-LM3-Pro`](https://huggingface.co/webAI-Official/TwIL-LM3-Pro) | **Revision moved on 9 Oct.** Commit list head is `144a3cc` "Replace TwIL-LM3-Pro-Q4_K_M.gguf with new build (#1)", 2026-10-09 18:12; the organisation listing API shows lastModified 2026-10-09T18:12:15Z. `4214aaa4` (30 Sep) is the previous head. **Correction of 15 Oct:** the "sha unchanged since 30 Sep" reading was wrong (Q116); the single-repo API answer fetched today still returned `4214aaa4`, a stale summary, so use the commit page and the listing, not that answer. T9b pinned the 9 Oct file (Q116) | webAI Non-Commercial License ver. 1.0, unchanged |
| [`webAI-Official/TwIL-LM3`](https://huggingface.co/webAI-Official/TwIL-LM3) | Listing API lastModified 2026-10-08T16:21Z; head `7857a94` "Fix TwIL-LM3 model card references (#3)". This resolves the 15 Oct three-way conflict in favour of the commit page and listing; `715bde2` "v5 MGPO weights" is the last weights commit (date not shown, relative only). The sha written on 8 Oct (`145ff05e`) and the 15 Oct API reading (`e4f94da5`) are **superseded**, not re-derived | same |
| [`webAI-Official/TwIL-LM`](https://huggingface.co/webAI-Official/TwIL-LM), [`TwIL-LM2`](https://huggingface.co/webAI-Official/TwIL-LM2), [`TwIL-LM3-Pro-LiteRT-LM`](https://huggingface.co/webAI-Official/TwIL-LM3-Pro-LiteRT-LM) | TwIL-LM: head `39dc16b` (16 Aug). TwIL-LM2: unchanged since 29 Sep. LiteRT-LM bundle: unchanged (created and last modified 2026-10-01; INT4 2.19 GB, INT8 3.76 GB, context 4,096, no scores) | same |
| [webAI-Official organisation](https://huggingface.co/webAI-Official) | Listing API returns **18 repos** (15 Oct note said 17; the extra is `webAI-ColVec1-4b`, created 2026-04-05, so a counting difference, not a new repo). **No repo created after 2026-10-01.** The organisation web page showed "about 7 hours ago" for TwIL-LM and TwIL-LM3; the API shows 16 Aug and 8 Oct, so that text is not trusted | mixed |
| [`google/gemma-4-12B-it-assistant`](https://huggingface.co/google/gemma-4-12B-it-assistant) and 26B-A4B / E2B / E4B "assistant" repos | Multi-token-prediction drafters for speculative decoding (12B drafter about 0.4B parameters, BF16). First recorded here; repos date from April to August. `google/gemma-4-26B-A4B-it-assistant` created 2026-04-23, `…-qat-q4_0-unquantized-assistant` 2026-05-29, `gemma-4-12B-it-assistant` modified 2026-08-20. Revisions not pinned | apache-2.0 (12B card) |
| [`google/gemma-4-26B-A4B-it-qat-q4_0-gguf`](https://huggingface.co/google/gemma-4-26B-A4B-it-qat-q4_0-gguf), [`google/gemma-4-E2B-it-qat-q4_0-gguf`](https://huggingface.co/google/gemma-4-E2B-it-qat-q4_0-gguf) | Exist (created 2026-05-01). The 26B-A4B GGUF is the Mac's default since 21 Oct (T9c revision `d1c082be`, 14.44 GB, per the T9c note); not re-queried | apache-2.0 (declared in T9c) |
| [`ibm-granite/granite-speech-5.0-470m-turboctc`](https://huggingface.co/ibm-granite/granite-speech-5.0-470m-turboctc) | Card read: about 470M parameters, **English only**, non-autoregressive CTC, released 2026-08-25; MLX via mlx-audio 0.5.1+, GGUF via transcribe.cpp; WER shown only in charts (reported 21 Oct multilingual update incl. French: `unverified`, re-check next week) | apache-2.0 |
| Publisher listings (API, newest first) | Qwen: newest items are Qwen3.8-27B-FP8 (2026-08-13) and ASR/aligner `-hf` variants; nothing from October. Google: newest timesfm-3.0 (2026-08-28) and the Gemma 4 assistants; IBM: granite-4.2-30b/8b (2026-09-04); Mistral: Mistral-Large-3 NVFP4 (2026-09-11). The Qwen listing appears sorted by creation date and omits the 20 Sep PE-T2I/PE-I2I repos, so "no new Qwen release" stays weakly supported | various |
| llama.cpp, mlx-lm, whisper.cpp releases | llama.cpp: tags now `b11800`–`b11804` (21–22 Oct); the five newest list no Metal/Gemma 4 change. mlx-lm: v0.31.3 (22 Apr) still latest. whisper.cpp: **v1.9.5 (6 Oct, ggml 0.26.0)**, newer than the v1.9.4 recorded on 8 Oct | MIT (not re-verified) |

Evidence archive: no new snapshots saved outside the vault this week.

Related: [[30 Resources/Local AI/README]] · [[90 System/weekly-local-model-review]]
