---
classification: internal
source: T9c run 2026-10-21-a (dbrain-runtime 8f74f8a; evidence artifacts/t9c/run-2026-10-21-a/, judging/ for the packet and both judges' verdicts)
review_status: draft
note_type: results
created: 2026-10-21
updated: 2026-10-21
---
# T9c: larger Gemma 4 models against C2 on the Air (21 Oct 2026)

**Outcome:** Gemma 4 26B-A4B passes the safety gate and answers 7 of 8 answerable dev cases correctly, against 5 for C2 (Gemma 4 E4B, the default since 8 Oct) and 5 for Gemma 4 12B, at nearly C2's typical latency. **David switched the Mac's default to the 26B-A4B (Q152, 21 Oct)**, with C2 kept as a one-restart fallback if the Air feels slow. Brief: [[90 System/briefs/T9c-larger-local-model|T9c]]. Earlier runs: [[10 Projects/AI Second Brain/02_Architecture/t9-model-comparison-2026-10-08|T9]], [[10 Projects/AI Second Brain/02_Architecture/t9b-twil-lm3-pro-2026-10-21|T9b]].

## What was compared
| Key | Model (Google, QAT Q4_0 GGUF, Apache-2.0) | Revision | File size |
|---|---|---|---|
| C2 | Gemma 4 E4B-it (default since D105) | `4b4a2c1d` | 5.15 GB |
| G12 | Gemma 4 12B-it, dense | `29d09777` | 6.98 GB |
| G26 | Gemma 4 26B-A4B-it, mixture of experts (about 4B parameters active per token) | `d1c082be` | 14.44 GB |

Candidates chosen by David (Q144) under "quality first" (Q-cowork-21c) and T9's licence rule 1 (a licence allowing the December demo). Both files hash-pinned before download and checked again before the run.

## How it ran
T9's frozen protocol on T9b's pattern: block order C2 G12 G26 C2 G26 G12 C2 (C2 scored at positions 1 and 7, position 4 the drift check), 180 s cool-downs, T9's server flags (thinking off, context 4096) and request signature for all three, timeouts 120 s (C2) and 300 s (G12, G26). Frozen corpus `878a08ea6f57` (the C2 baseline's evidence, Q138). AC power, Low Power Mode off, phone service stopped and restarted after, no Codex calls in the window, `caffeinate -dimsu`, no-network sandbox, provider keys unset.

## Results
| Configuration | Safe | Correct (of 8 answerable, both judges, both blocks) | Declined both unanswerable | p50 | p95 | Peak server RSS |
|---|---|---|---|---|---|---|
| **G26** Gemma 4 26B-A4B | **yes** | **7** | yes | 8.5 s | 13.8 s | 15.31 GiB |
| C2 Gemma 4 E4B | yes | 5 | yes | 8.3 s | 10.5 s | 5.93 GiB |
| G12 Gemma 4 12B | yes | 5 | yes | 21.7 s | 31.3 s | 15.22 GiB |

n = 20 answers per configuration (10 cases × 2 scored blocks); each configuration's two blocks returned identical answers, and C2's answers are byte-identical to its T9b answers. Drift: C2 p50 8.26 s (position 1), 8.25 s (4), 8.29 s (7). Ten cases on a three-file corpus: a two-case difference is a development signal, not a tested significance.

## Gates, step by step
1. **Run validity:** pins, code, corpus, request signatures and cases matched the pre-run manifest; all seven blocks ok; no drift re-run.
2. **Safety gate** (an invented citation id; evidence cited for a claim it does not make; an unanswerable case not declined): all three pass, by both judges.
3. **Quality among safe configurations:** G26 7, C2 5, G12 5. G26 recovers both of C2's correctable misses: `write_approval` (names binding approval to the patch and base revision) and `french_voice` (abstains in French). `source_retention` stays unanswerable from this evidence for every model (the expected fragment is outside the corpus).
4. **Latency and memory** (recorded, not the selection rule under quality first): G26's typical latency equals C2's, p95 3.3 s higher, above D56's 8 s text target, which Q-cowork-21c accepts for L0. G26 holds about 15 GiB while the phone service runs, against about 6 GiB for C2, on a 24 GiB Air.

## Judging
The lead judged first (`t9c-lead-verdicts.json`, 20:02, before any Codex call), then Codex `gpt-6.1-sol` (review profile, high, read-only) judged the masked packet blind from a folder holding only the packet and the T9 rubric (`codex-verdicts.json`). Agreement 58 of 60 answers; the two differences are G12's `media_storage`, whose combined `[E1, E2]` marker Codex counted as a citation and the lead did not; under T9's rule (a case counts only when both judges mark it correct in both blocks) G12 stays at 5.

## What this does not settle
- Real-world quality on David's own notes and in French: these are ten development cases on three files.
- Whether 15 GiB in the background is comfortable for David's other work on the Air: David will say (Q152's revisit clause).
- PV1 step 5 measures the same 26B-A4B on Scaleway (L1), which will show the same model at two sovereignty levels.
