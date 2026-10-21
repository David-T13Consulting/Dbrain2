---
classification: internal
source: M6b S4 scored run 12 Oct 2026 (dbrain-runtime 0736b29; artifacts/m6b/s4-20261012-1344/, scores.json sha256 8249d633c2e8a34e…, hashes.json 6c9efb0db09e4d0a…)
review_status: draft
note_type: results
created: 2026-10-21
updated: 2026-10-21
---
# M6b: embedding retrieval against the lexical baseline (run of 12 Oct 2026)

**Outcome: no measured benefit; the lexical baseline stays** (protocol item 7). Neither embedding model recovers a case the lexical baseline missed, and both lose at least one case it found. Brief: [[90 System/briefs/M6b-embedding-eval|M6b]]; D140 closes M6b with this note.

## What was compared (protocol items 1–6, frozen 9 Oct)
| Arm | Model | Settings |
|---|---|---|
| A | Lexical baseline, as in `retrieval-v1` | — |
| B | `google/embeddinggemma-2`, revision `914f7f89142e` | text path only, float32, documented query/document prompts, 768 d and 256 d re-normalized |
| C | `Qwen/Qwen3-Embedding-0.6B`, revision `97b0c614be4d` | query instruction, full dimension, float32 |

Same 26-chunk corpus and 10 cases for every arm; expected-evidence labels frozen in D124 (passage ids); `source_retention` is the corpus-gap case, reported apart; `unknown_gpu` and `unknown_password` are unanswerable. Each arm ran in its own sandboxed process with the network blocked; input hashes match the frozen ones. Small n: counts only.

## Per-case outcomes
Recall@3 / recall@5 (1 = the expected passage is there), and wrong-evidence passages in the top 3.

| Case | A lexical | B 768 d | B 256 d | C Qwen3 0.6B |
|---|---|---|---|---|
| local_stage | 1 / 1 · 2 | 1 / 1 · 2 | 1 / 1 · 2 | 1 / 1 · 2 |
| client_policy (C9 only, D124) | 0 / 0 · 3 | 0 / 0 · 3 | 0 / 0 · 3 | 0 / 0 · 3 |
| write_approval | 1 / 1 · 2 | 1 / 1 · 2 | 1 / 1 · 2 | **0 / 0** · 3 |
| media_storage | 1 / 1 · 2 | 1 / 1 · 2 | 1 / 1 · 2 | 1 / 1 · 1 |
| query_navigation | 1 / 1 · 2 | **0 / 0** · 3 | **0 / 0** · 3 | **0 / 0** · 3 |
| remote_voice | 1 / 1 · 2 | 1 / 1 · 2 | 1 / 1 · 2 | 1 / 1 · 2 |
| french_voice (French query, English plan) | 0 / 0 · 3 | 0 / 0 · 3 | 0 / 0 · 3 | 0 / 0 · 3 |
| source_retention (corpus gap, apart) | — · 3 | — · 3 | — · 3 | — · 3 |
| unknown_gpu (unanswerable) | — · 3 | — · 3 | — · 3 | — · 3 |
| unknown_password (unanswerable) | — · 3 | — · 3 | — · 3 | — · 3 |
| **Total, 7 answerable** | **5 / 5** | 4 / 4 | 4 / 4 | 3 / 3 |
| Wrong in top 3, 9 scored cases (answerable only) | 22 (16) | 23 (17) | 23 (17) | 23 (17) |

Recorded, not a criterion: load cold / warm and peak RSS: B 4.2 s / 1.1 s, 4.0 GB; C 3.4 s / 0.4 s, 6.1 GB.

## Protocol item 7, step by step
"Accept as a retrieval candidate only if it recovers at least one miss the lexical baseline had (including the French query against the English plan) without adding wrong-evidence hits in the top 3."
1. **Lexical misses:** `client_policy` and `french_voice` (recall 0 at 3 and 5).
2. **Recovered by B (either dimension)?** No: both stay 0. **By C?** No: both stay 0.
3. Item 7's first condition fails for B and C, so neither is accepted; the second condition is not needed. For the record, both also add wrong-evidence hits overall (23 against 22) and lose cases A found (B: `query_navigation`; C: `query_navigation`, `write_approval`).
4. **Decision under the protocol:** no measured benefit; keep the lexical baseline. Step S6 (whole-vault second pass) does not apply: it runs only if S5 shows a recovered miss.

## Limits
- Seven answerable cases on a 26-chunk corpus: this rules out a clear benefit on these cases, not a benefit on the whole vault or on French questions in general.
- The French miss is shared by every arm; a bilingual retrieval fix is tracked separately (M5, query expansion).
- **Quoted beside the result, not scored (D124):** the 1 Oct manual review credited the lexical baseline with equivalent client-policy wording and counted 6 of 7 answerable cases with evidence in the top 3, the French query the one miss (`continuation_manual_review.json` totals, as recorded in the M6b brief's S3 entry). It names no passage, so `client_policy` is scored on C9 only here, as item 7 requires. B and C were not reviewed for equivalent wording.

## Proposed follow-ups (for David)
- No row change proposed for `30 Resources/Local AI/` beyond noting "no measured benefit on the M6b cases" for both models, if David wants it there (queued, not written).
- Disk: the two embedding models (about 2.7 GB) and the `m6b-py312` venv (1.1 GB) can be kept for a later bilingual test or removed; David's call.
