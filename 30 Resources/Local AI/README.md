---
classification: internal
created: 2026-10-01
last_reviewed: 2026-10-22
next_review: 2026-10-29
status: maintained research; deployment choices provisional
---
# Local AI — understanding and choosing models

Local AI is a collection of components, not one model that does everything. This guide connects current, verified model releases to the second-brain build. It is a representative shortlist, not an exhaustive leaderboard or a claim that every entry is the latest release.

David requested this knowledge base and weekly benchmark updates on 1 October 2026. **The initial research is complete; the weekly review was activated by David on 1 October (D60) and its first scheduled run was 8 October, the second 15 October and the third 22 October.** See [[90 System/weekly-local-model-review]] for the procedure and operating record.

## Read in this order

1. [[30 Resources/Local AI/model-fundamentals]] — weights, runtimes, quantization, memory, context and agents.
2. [[30 Resources/Local AI/text-and-vision]] — answering, reasoning, coding and understanding documents/images.
3. [[30 Resources/Local AI/speech-models]] — speech recognition, speech synthesis and the voice pipeline.
4. [[30 Resources/Local AI/image-models]] — generating and editing images.
5. [[30 Resources/Local AI/retrieval-models]] — finding evidence before answering.
6. [[30 Resources/Local AI/benchmark-ledger]] — dated published results and our own measurements, kept distinct.
7. [[30 Resources/Local AI/sources]] — exact model-card revisions and preserved evidence.

## What to try in this project

These are engineering recommendations, not accepted deployment decisions.

| Need | Starting position | Evidence needed before selection |
|---|---|---|
| Cited vault answers | Continue small quantized language-model experiments; Qwen3-4B and Qwen3.5-4B now have local development results | Correct evidence retrieval, supported citations, abstention and French/English reliability |
| Alternative language/vision model | Gemma 4 E2B/E4B or Ministral 3 8B | Exact artifact/runtime compatibility, latency and memory on this Mac |
| Voice capture | Compare Whisper turbo with Qwen3-ASR; Parakeet v3 is another multilingual candidate | David's French/English, mixed speech, names, numbers, silence and background noise |
| Spoken answers | Compare Kokoro with Qwen3-TTS | Intelligibility, French pronunciation, first-audio delay and cancellation |
| Image creation | FLUX.2 klein 4B is a candidate; keep this outside the initial QA critical path | Working Apple-compatible runtime, actual memory and generation time |
| Better search | Fix corpus coverage and French query handling first | Demonstrated retrieval failures before introducing embeddings or reranking |
| Multi-agent operation | Roles may share one model sequentially | Measured checker benefit, bounded jobs, permissions and failure recovery |

The measured host is an M2 Mac with 24 GiB unified memory. This supports small-model experiments; it does not prove that several models can run together acceptably. The current build order remains [[10 Projects/AI Second Brain/04_Roadmap|S1–S6]]. Larger model downloads, runtime upgrades and rollout remain separate from weekly research.

## Next local candidates (22 Oct shortlist; replaces the 15 Oct list)

1. Gemma 4 26B-A4B-it QAT Q4_0 (the Mac's default since 21 Oct, Q152) with Google's `-it-assistant` multi-token-prediction drafter, latency only. The default's T9c p95 of 13.8 s is above D56's 8 s target. Doubtful by Google's own documentation for a mixture-of-experts model at batch size 1, and llama.cpp support is reported for E2B/E4B drafters only (secondary source), so the first step is a read-only support check; drop it if unsupported. Engineering estimate, not measured.
2. Qwen3-ASR-1.7B against Whisper large-v3-turbo on French/English synthetic dictation, only if the lead confirms local ASR is needed (stage-1 voice currently uses iPhone dictation); no local ASR number exists. Granite Speech 5.0 is English-only and excluded.

TwIL-LM3-Pro (webAI Non-Commercial License 1.0, unchanged on 22 Oct; no commercial tier or written permission found) is **not shortlisted**: T9b (21 Oct) measured it and it failed the safety gate in both configurations; C2 stayed. It remains on the weekly watchlist, and a new revision (the publisher replaced its Q4_K_M file on 9 Oct) or an independent evaluation would justify a re-test. Both candidates above need a separate, authorized, bounded run; no local benchmark ran on 22 Oct. Detail in [[30 Resources/Local AI/benchmark-ledger]].

## Evidence labels

- **Measured here:** a recorded local run with exact configuration and limitations.
- **Publisher-reported:** a model card, paper or original project report; not independently reproduced here.
- **Engineering estimate:** a reasoned expectation, explicitly unmeasured.
- **Unverified:** missing evidence or conflicting sources. Keep the gap visible.

This follows the persistent, linked synthesis and maintenance approach in [Karpathy's LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f#llm-wiki). Sources, interpretations and local experiments remain distinguishable; new claims amend the guide while dated results remain intact.
