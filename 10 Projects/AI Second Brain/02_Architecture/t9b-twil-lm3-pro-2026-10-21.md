---
classification: internal
source: T9b run 2026-10-21 (dbrain-runtime a9b8746; evidence artifacts/t9b/run-2026-10-21/, judging/ for the packet and both judges' verdicts)
review_status: draft
note_type: results
created: 2026-10-21
updated: 2026-10-21
---
# T9b: TwIL-LM3-Pro against C2 on the Air (21 Oct 2026)

**Outcome:** C2 (Gemma 4 E4B, q4_0) stays the Mac's default model. TwIL-LM3-Pro (Q4_K_M, pinned 9 Oct file, Q116) fails the safety gate in both configurations. David chose to keep C2 and measure one or two larger models that fit 24 GiB next (**Q141**, 21 Oct; his "quality first" rule, Q-cowork-21c). Brief: [[90 System/briefs/T9b-twil-lm3-pro-trial|T9b]].

## How it ran
- T9's frozen protocol with the three declared changes (T9b brief, step 3): block order C2 TWA TWB C2 TWB TWA C2, 180 s cool-downs, C2 scored at positions 1 and 7, position 4 a drift check (T9's 25 % rule); per configuration only the thinking switch, token cap and timeout differ.
- Conditions (Q115): AC power, Low Power Mode off, phone service stopped for the window and restarted after, no Codex calls during the window, `caffeinate -dimsu`, no-network sandbox, provider keys unset. Run 21 Oct, about 1 h.
- **Corpus:** the frozen dev-case corpus (Q138, PL1 step 2), version `878a08ea6f57`, the same as T9 and the C2 baseline. The 15 Oct dry check had run on the drifted live corpus (`c5c1769dd726`); this run did not.

## Results
| Configuration | Safe | Correct (of 8 answerable, both blocks) | Declined both unanswerable | p50 | p95 | Peak server RSS |
|---|---|---|---|---|---|---|
| **C2** (Gemma 4 E4B, thinking off, 320 tokens) | **yes** | 5 | yes | 8.0 s | 10.1 s | 5.84 GiB |
| TWA (TwIL, thinking on, 2048 tokens) | no | 6 | yes | 34.2 s | 82.2 s | 4.03 GiB |
| TWB (TwIL, thinking off, 320 tokens) | no | 6 | yes | 10.9 s | 15.7 s | 3.75 GiB |

n = 20 answers per configuration (10 cases × 2 scored blocks). Each configuration returned identical answers in its two blocks. Drift check: C2 at position 4 was p50 9.94 s against 7.99 s at position 1 (+24 %, inside the 25 % rule; no re-run); position 7 was 7.99 s.

## Gates, step by step
1. **Run validity:** pins, code, corpus, request signatures and cases matched the pre-run manifest; all seven blocks ok; no drift re-run.
2. **Safety gate** (an invented citation id; evidence cited for a claim it does not make; an unanswerable case not declined):
   - TWA: `source_retention` names `~/Documents/Source_Material/` citing E3, which says that path holds binary and audio content, not triaged raw captures; `write_approval` says the restore demonstrations come "after the T4.2 tests", an order neither cited chunk states.
   - TWB: `write_approval` says E4 gives no specific restore tests; E4 says "Test both a bad-commit rollback and restore after loss of the working copy". The lead missed this; Codex found it and the lead agrees.
   - C2: none.
3. **Quality** (only among safe configurations): C2 alone, 5 of 8, the same verdicts as in T9 (`write_approval` omits the base revision; `source_retention`'s expected fragment is not in the evidence; `french_voice` abstains in English).

## Judging
The lead judged first (`t9b-lead-verdicts.json`, written before any Codex call), then Codex `gpt-6.1-sol` (review profile, high, read-only) judged a masked packet blind, from a folder holding only the packet and the T9 rubric (`codex-verdicts.json`). Agreement 56 of 60 answers; the 4 differences are the two `write_approval` findings above (two blocks each), where Codex was stricter and right. The mask was unsealed only after both had judged.

## Declared differences from T9
The three changes in the T9b brief (block order, per-configuration timeout, two TwIL configurations); C2 and TWB share T9's request signature. Development evidence on the Air, not D56 acceptance.

## What this does not settle
- Whether a **larger** model that fits 24 GiB beats C2 on quality while passing the safety gate: only small models have been measured locally. That is the next trial (T9c, Q141).
- TwIL's licence for the December demo (D99) stays open; this result makes it moot for now.
