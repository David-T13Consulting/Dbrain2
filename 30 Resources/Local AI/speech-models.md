---
classification: internal
created: 2026-10-01
last_reviewed: 2026-10-08
next_review: 2026-10-15
---
# Local speech recognition and speech output

The initial voice design should be inspectable: **microphone → speech-to-text → retrieved evidence + language model → text-to-speech → playback**. This is a recommendation for S4, not an implemented service. Keep the transcript visible so David can correct names and numbers. Preserve French captures as spoken; translation belongs to triage.

## Speech-to-text / ASR

| Candidate | Strengths and good uses | Weaknesses / what to test | License metadata |
|---|---|---|---|
| **[Whisper large-v3-turbo](https://huggingface.co/openai/whisper-large-v3-turbo)** | 809M-parameter multilingual transcription checkpoint; practical dictation baseline with established local tooling | Noise, silence, invented words, accents and names need explicit tests. Faster decoding is a tradeoff, not proof of best French accuracy | MIT |
| **[Qwen3-ASR-0.6B / 1.7B](https://huggingface.co/Qwen/Qwen3-ASR-0.6B)** | Publisher lists 30 languages including French/English and offline/streaming modes; compare the small model's latency with the larger model's accuracy | GPU benchmark throughput is not an M2 measurement. Verify an Apple-compatible backend and actual checkpoint dependencies | Apache-2.0 |
| **[Parakeet TDT 0.6B v3](https://huggingface.co/nvidia/parakeet-tdt-0.6b-v3)** | Multilingual transcription in 25 European languages, punctuation and timestamps; useful for short captures and longer recordings | Use **v3**, not English-only v2, for this comparison. NVIDIA-oriented performance claims need local reproduction; long-audio limits depend on attention mode/hardware | CC-BY-4.0 |

[whisper.cpp](https://github.com/ggml-org/whisper.cpp) provides native local Whisper inference with Apple support. A runtime is separate from a model: record both versions, the audio preprocessing and any voice-activity detector. ASR does not automatically identify who spoke; speaker diarization is another capability to evaluate only if needed.

## Text-to-speech / TTS

| Candidate | Strengths and good uses | Weaknesses / what to test | License metadata |
|---|---|---|---|
| **[Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M)** | Small speech synthesizer with preset voices; a reasonable low-memory starting candidate | French has one listed voice, `ff_siwis`, and thinner language resources than English. Test names, abbreviations, long numbers and mixed-language passages | Apache-2.0 |
| **[Qwen3-TTS 12Hz 0.6B CustomVoice](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-0.6B-CustomVoice)** | Preset voices and ten languages including French/English; streaming-oriented family | More components/memory than Kokoro; advertised minimum latency is not local evidence. Do not assume all family features exist in this checkpoint | Apache-2.0 |
| **[Qwen3-TTS 1.7B variants](https://github.com/QwenLM/Qwen3-TTS)** | CustomVoice for preset/style control, VoiceDesign for described voices, Base for reference-audio cloning | Different checkpoints for different jobs. Extra memory and runtime complexity; cloning is unnecessary for the initial spoken-answer feature | Verify exact selected artifact before use |

**Source conflict to retain:** the 0.6B CustomVoice card advertises instruction-based style control, while the [official repository's model table](https://github.com/QwenLM/Qwen3-TTS) marks instruction control for 1.7B CustomVoice and leaves it blank for 0.6B. Treat 0.6B style control as unverified. The [Kokoro voice inventory](https://huggingface.co/hexgrad/Kokoro-82M/blob/main/VOICES.md) also warns that non-English support can be thin; language availability is not a quality score.

## Acceptance evidence for voice

No speech model has been run on David's Mac in this assessment. Start with a consented French/English fixture set containing ordinary dictation, code-switching, names, dates, distances, acronyms, pauses and background noise. Keep original recordings outside the vault with agreed retention.

Measure word/character error rates, critical-name/number errors, transcription delay and real-time factor (`processing seconds / audio seconds`; lower is faster). For synthesis, measure time to first audible output, full synthesis time, pronunciation errors and David's listening ratings. Include silence, interruptions and cancellation. A fluent spoken hallucination remains a wrong answer: preserve evidence/abstention in the text stage before synthesis.

Related: [[30 Resources/Local AI/benchmark-ledger]] · [[90 System/weekly-local-model-review]]
