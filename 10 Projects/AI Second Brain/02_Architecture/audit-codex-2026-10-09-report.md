---
classification: internal
source: independent Codex audit run by David, 9 Oct 2026; verbatim as pasted to Cowork
review_status: proposed
note_type: review
created: 2026-10-09
updated: 2026-10-09
---
# Dbrain2 — architecture, evaluations and trust assessment

Assessment date: 9 October 2026.

**Dbrain2 is heading in the right direction, and its plans take evaluations and guardrails seriously. The strongest parts are the constrained local query service, explicit approval boundaries, and documented release gates. The weakest parts are representative quality evidence, enforced data separation, and completing the memory-and-correction loop.**

My earlier assessment needs one qualification: conversational memory, safe updates, recovery and injection testing are missing from the running service, **but they are explicitly addressed in the plans**. This is primarily an implementation-and-verification gap, rather than a missing architectural vision.

I inspected the vault, Product School resources, runtime source and test assertions. I did not rerun tests, exercise the deployed phone service, or access the restricted failure store. Recorded test results are therefore project evidence, not fresh verification. No repository or vault files were changed.

**The architecture fits your intended system.**

Separating the Obsidian vault from runtime code is sensible. The current path is phone/desktop client → authenticated service → scoped retrieval → local model → cited response. The inference adapter enforces loopback connections, rejects redirects and neutralises ambient proxies. The model has no tool-execution interface. These are concrete restrictions, beyond instructions asking the model to behave. [Model adapter](</Users/davidduchesne/Work/dbrain-runtime/dbrain/adapter.py:195>)

The authenticated iPhone endpoint exists; the repository records successful remote use. Local speech recognition, richer conversational access, durable offline capture and supervised writes remain planned. Apple Watch and Tesla access are stretch goals. The dedicated Mac is an appropriate architectural direction, but availability, sustained performance and recovery still need acceptance evidence on that host. [Phone implementation](</Users/davidduchesne/Work/dbrain-runtime/mvp/README.md>), [delivery stages](</Users/davidduchesne/Work/Dbrain2/10 Projects/AI Second Brain/04_Roadmap.md:33>)

One terminology correction: the current retriever is deterministic **BM25 over chunks**, rebuilt per query. It is neither vector search nor a model autonomously searching files. That is a reasonable baseline; measure its failures before replacing it. [Retriever](</Users/davidduchesne/Work/dbrain-runtime/dbrain/retrieve.py:23>)

**The Product School principles are substantially reflected in the plan.**

The resources emphasise versioned evaluations, visible uncertainty, human control, scoped tools, governed memory and operational monitoring. The roadmap translates these into source IDs, exact-patch approval, independent restore, held-out evaluations and staged autonomy. It also improves on the course heuristics: confidence scores are not treated as calibrated probabilities, mandatory approvals are separated from avoidable interventions, and small datasets are not used to substantiate a sub-1% failure claim. [Course synthesis](</Users/davidduchesne/Work/Dbrain2/30 Resources/Product School/advanced-agents-memory-tools-evals-deploy.md>), [project playbook](</Users/davidduchesne/Work/Dbrain2/10 Projects/AI Second Brain/03_Product_School_Playbook.md>), [evaluation requirements](</Users/davidduchesne/Work/Dbrain2/10 Projects/AI Second Brain/04_Roadmap.md:67>)

Keep that distinction: understandable controls help users place appropriate trust, but do not compensate for unsafe or inaccurate behaviour. Likewise, learning need not mean retraining weights; approved memory corrections and regression improvements can provide useful learning.

The major capabilities stand as follows:

1. **Representative evaluations and acceptance gates — well planned, insufficiently demonstrated.**  
   There are separate platform and running-domain tracks, independent model judging, pinned development runs, and reserved cases. P2.5 specifies 30 questions covering lookup, dates, negation, abstention and synthesis, with per-type reporting and a held-out subset.

   The selected model’s recorded result remains **5/8 answerable cases correct, p95 10.13 seconds**, on ten development questions over three files. One expected answer was absent from the corpus, so that score mixes model behaviour with dataset defects. It cannot establish everyday vault reliability. [Model comparison](</Users/davidduchesne/Work/Dbrain2/10 Projects/AI Second Brain/02_Architecture/t9-model-comparison-2026-10-08.md:23>)

   Newer evidence is useful but provisional: P2.5’s 13 synthetic calendar cases expose vocabulary/date failures; its scorer remains uncommitted and the last correction unreviewed. The six “row” cases failed the full acceptance condition, although five returned the right time—this is not six wholly incorrect answers. Complete scorer review and independent expected-evidence review before using these results as a release gate. [P2.5](</Users/davidduchesne/Work/Dbrain2/90 System/briefs/P2.5-answer-accuracy.md>)

2. **Retrieval, citations and hallucination checks — implemented, with important limits.**  
   The service checks citation IDs, provides source locations, withholds when nothing is retrieved, and refuses to label an answer “supported” without a verifier. Tests explicitly demonstrate that a contradiction can share vocabulary with its source.

   That is honest engineering, but not factual verification. The planned second-pass verifier, structured schedule lookup, query expansion and contradiction handling remain unfinished. Measure retrieval coverage, answer correctness and citation support separately; also distinguish “the notes do not establish this” from “this event does not exist.” [Answer logic](</Users/davidduchesne/Work/dbrain-runtime/dbrain/answer.py:139>), [grounding tests](</Users/davidduchesne/Work/dbrain-runtime/tests/test_answer.py:140>)

3. **Prompt injection and MCP — acknowledged in plans, not yet validated end to end.**  
   The roadmap explicitly treats source content as evidence rather than executable authority and requires malicious-source tests before writes. Current read-only operation and absence of tools reduce consequences substantially.

   However, retrieved text still enters the model prompt, so malicious notes could influence answers. I found no dedicated end-to-end malicious-source suite in the inspected tests. Before MCP, add tests for instructions embedded in notes/tool results, attempted cross-domain retrieval, fabricated authority and exfiltration requests. Each connector needs independently enforced tool and parameter scopes, bounded execution, credential revocation and audit records. MCP itself supplies no safety guarantee. [Storage and permission design](</Users/davidduchesne/Work/Dbrain2/10 Projects/AI Second Brain/04_Roadmap.md:48>)

4. **Permissions and human approval — strong read boundary; write boundary remains a design.**  
   Actual controls reject path escapes, symlink traversal and hard-linked notes. Tests attempt reads through adversarial paths and compare vault contents before/after queries, including the traced CLI path. [Scope tests](</Users/davidduchesne/Work/dbrain-runtime/tests/test_scope.py:50>), [read-only tests](</Users/davidduchesne/Work/dbrain-runtime/tests/test_readonly.py:34>)

   Planned writes bind approval to an exact patch and base revision, reject stale approvals, and use one deterministic writer. This is the right design. It needs tests for rejection leaving no changes, concurrent Obsidian edits, approval replay, partial failures and crash recovery. Voice approval should identify the precise pending proposal rather than treating an ambiguous “yes” as authorisation. [Write brief](</Users/davidduchesne/Work/Dbrain2/90 System/briefs/P3.0-update-my-brain.md>)

5. **Persistent memory — substantial lifecycle design, not yet connected.**  
   Plans cover durable sources, stable IDs, facts versus interpretations, contradictions, review state, corrections and forgetting. Current requests contain only one question; neither conversational continuity nor approved memory updates is implemented.

   Remaining design detail includes which conversational facts become memory, expiry/revalidation by memory type, correction propagation to derived notes, and preventing deleted facts from reappearing through cached history or later ingestion. The “forget” path must distinguish removing an active fact from purging every retained copy. [Memory plan](</Users/davidduchesne/Work/Dbrain2/10 Projects/AI Second Brain/04_Roadmap.md:48>), [capture/correction specification](</Users/davidduchesne/Work/Dbrain2/90 System/briefs/P3.0-update-my-brain.md:27>)

6. **Personal, client and cloud isolation — the most consequential boundary still to finish.**  
   Dbrain2 excludes client-confidential material; a separate client workspace is explicitly planned. Sensitive personal data has access-test and deletion prerequisites. However, the phone currently uses a whole-permitted-vault profile, and cloud development agents can read permitted vault content.

   More importantly, **D110 records an accepted Air exception**: Claude Code shell restrictions are imperfect, and some screen-control paths remain untested. The planned dedicated macOS service user on the Mac mini should replace that exception. Verify separation with synthetic markers across files, search, logs, backups and agent tools before admitting sensitive data. Labels and separate folders alone are insufficient. [Recorded exception](</Users/davidduchesne/Work/Dbrain2/10 Projects/AI Second Brain/DECISIONS.md:128>), [client requirements](</Users/davidduchesne/Work/Dbrain2/10 Projects/AI Second Brain/02_Architecture/client-tier-workspace-requirements.md>)

7. **Secrets, logging and retention — meaningful implementation, incomplete privacy coverage.**  
   Keychain-backed authentication, token rotation tooling, a self-testing secret scanner, text-minimised traces and guarded log destinations exist. Failure-store code implements private files, atomic capture, audit reconciliation, deletion and 90-day retention; synthetic tests cover these behaviours.

   Limits matter: the secret scanner covers the runtime repository, not every source; traces retain filenames and deterministic question hashes, which should not be treated as anonymous. The retention sweep runs while the service runs, so test restart cleanup after extended downtime. Establish retention for backups and audit logs, not only failure records. [Trace contents](</Users/davidduchesne/Work/dbrain-runtime/dbrain/trace.py>), [retention tests](</Users/davidduchesne/Work/dbrain-runtime/tests/test_failures.py:288>)

8. **Monitoring and improvement — capture works; the corrective loop is incomplete.**  
   The project records a planted end-to-end failure capture and deletion. It plans local triage, synthetic regression cases, leak screening and held-out scoring.

   The digest/regression loop is not delivered, and the user’s “wrong” action is blocked by a retention-policy decision. Automatic signals can miss a confidently wrong answer; correct declines can also inflate failure counts. Track detection quality and successful corrections, not simply collected failures. The lexical leak checker has adversarial tests but is not proof of anonymisation. Add a concise incident procedure: stop exposure, revoke access, preserve permitted evidence, assess impact, repair and verify. [Failure-loop status and scope](</Users/davidduchesne/Work/Dbrain2/90 System/briefs/P2.7-failure-capture-loop.md>)

9. **Recovery, versioning and deployment — concrete gates, still open.**  
   Model hashes, benchmark manifests, request signatures and restart scripts exist. The roadmap explicitly separates Git rollback from independent restore and specifies zero lost confirmed captures.

   Backup/restore, reproducible deployment and upgrade rollback remain open tasks. Turn the recorded regression results into an enforced release decision tied to exact code, model, prompt and corpus versions. Reconcile stale documentation—the runtime README still describes an older default model and repository state. A successful process restart is not a demonstrated recovery. [Launcher](</Users/davidduchesne/Work/dbrain-runtime/mvp/run-all.sh>), [open operational work](</Users/davidduchesne/Work/Dbrain2/10 Projects/AI Second Brain/TASKS.md>)

For selected cloud services, require a specific approved data flow and verified provider terms: purposes, data categories, retention, training use, subprocessors, deletion and applicable transfer arrangements. Professional processing requires assessing controller/processor responsibilities; international transfers have separate conditions. Local hosting alone establishes neither GDPR nor AI Act compliance. AI Act assessment depends on the actual use and role. [EDPB responsibilities](https://www.edpb.europa.eu/sme/learn-the-basics/data-controller-or-data-processor_en), [EDPB transfers](https://www.edpb.europa.eu/sme/be-compliant/international-data-transfers_en), [Commission AI Act guidance](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)

Tesla documents Grok connectors, but a supported connection to your private Dbrain service remains unverified. Keep it outside the core release; connected information introduces external processing. [Tesla documentation](https://www.tesla.com/support/grok)

**I recommend four ordered release gates:**

- **Reliable read-only assistant:** reviewed representative evaluations, honest abstention, source-injection tests and measured host performance.
- **Safe memory writes:** independent restore first; exact approval, stale-edit rejection, idempotent capture and correction/deletion tests.
- **Sensitive or professional use:** enforced service/cloud/client separation, tested retention and explicit provider/data-flow approval.
- **Additional autonomy and integrations:** one scoped MCP connector at a time, proven revocation, monitoring and benefit over the single-agent baseline.

**The next practical milestone should be one tested “remember → recall → correct” workflow from the phone.** Complete the relevant evaluation and restore prerequisites, then demonstrate an approved benign fact surviving restart, being recalled with its source in a fresh session, and being corrected without the old version resurfacing. Include rejection, a concurrent edit and an interrupted save. That would connect the project’s substantial governance design to the daily experience you actually want.
