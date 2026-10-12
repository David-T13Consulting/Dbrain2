---
classification: internal
source: independent Codex audit, run by David, 9 Oct 2026; pasted to Cowork verbatim
review_status: proposed
note_type: review
created: 2026-10-09
updated: 2026-10-09
---
# Independent audit, 9 Oct 2026 (Codex): architecture, evaluations and trust

**Status:** an outside review, kept as evidence. Cowork's analysis against David's end goal and the plan changes it drove are in [[10 Projects/AI Second Brain/04_Roadmap|roadmap]] §0, "Amendment of 9 October". Findings marked for the lead's evaluation are listed there; nothing in this note is a decision.

**Summary of the audit (Cowork's paraphrase; the full report is in David's chat of 9 Oct; verbatim report: [[10 Projects/AI Second Brain/02_Architecture/audit-codex-2026-10-09-report|audit report]]):**

| # | Area | Audit's finding |
|---|---|---|
| 1 | Evaluations | Well planned, insufficiently demonstrated. T9 result (5/8, p95 10.13 s, 10 questions over 3 files, one expected answer absent from the corpus) cannot establish everyday reliability. P2.5 F0 scorer uncommitted and last fix unreviewed; the six "row" failures include five right times |
| 2 | Retrieval and grounding | BM25 over chunks, rebuilt per query (not vector, not agentic search). Citation-ID checks and withholding exist; no factual verifier. Measure retrieval coverage, correctness and citation support separately; separate "notes don't establish this" from "this doesn't exist" |
| 3 | Injection and MCP | Planned, not validated. Retrieved text enters the prompt; no end-to-end malicious-source suite found. Before MCP: tests for embedded instructions, cross-domain retrieval, fabricated authority, exfiltration; per-connector scopes, bounded execution, revocation, audit |
| 4 | Permissions and approval | Read boundary strong and tested. Write boundary is design only: needs tests for rejection, concurrent Obsidian edits, approval replay, partial failure, crash recovery; voice approval must name the exact pending proposal |
| 5 | Memory | Lifecycle designed, not connected; single-question requests. Open: which conversational facts become memory, expiry by type, correction propagation, deleted facts resurfacing; "forget" vs "purge" |
| 6 | Isolation | Most consequential open boundary. Phone uses a whole-vault profile; cloud dev agents read permitted vault content; D110 Air exception. Verify separation with synthetic markers across files, search, logs, backups and agent tools before sensitive data |
| 7 | Secrets, logs, retention | Real implementation; gaps: scanner covers the runtime repo only; traces keep filenames and deterministic question hashes (not anonymous); retention sweep only runs while the service runs; no retention for backups and audit logs |
| 8 | Monitoring and improvement | Capture works, corrective loop incomplete. Track detection quality and successful corrections, not failure counts. Leak checker is not proof of anonymisation. Add an incident procedure |
| 9 | Recovery and deployment | Backup/restore, reproducible deploy and upgrade rollback open. Bind release decisions to exact code, model, prompt and corpus versions. Runtime README stale |
| — | Cloud and law | Cloud services need an approved data flow and verified terms; local hosting establishes neither GDPR nor AI Act compliance. Tesla: Grok connectors exist, a private-service link is unverified; keep out of core |

**Four release gates proposed:** (1) reliable read-only assistant; (2) safe memory writes; (3) sensitive or professional use; (4) additional autonomy and integrations, one connector at a time.

**Next milestone proposed:** one tested *remember → recall → correct* workflow from the phone, including rejection, a concurrent edit and an interrupted save.
