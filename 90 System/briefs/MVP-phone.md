---
classification: internal
task: P2.4               # MVP-phone; S4 slice pulled into S2 (lead, 5 Oct)
owner: "@code"
status: in-review
models: ["claude-opus-5-5 (lead, build)", "gpt-6.1-sol (review rounds 1-3)"]
created: 2026-10-05
updated: 2026-10-05
source: for-david Q32–Q36; David's acceptance run via Cowork (handoff, 5 Oct)
review_status: proposed
note_type: decision
---
# MVP: ask the second brain a question from the iPhone (Air as host)

## Goal (one sentence)
David can ask a question on his iPhone, typed or dictated, at home or on 4G, and get a cited answer from the local model on the MacBook Air, with nothing exposed to the public internet.

## Decisions taken by David (5 Oct, via Cowork; queue Q32–Q34)
- **Network: Tailscale** (private encrypted link between David's own devices). No public endpoint, no port forwarding.
- **Client: Apple Shortcut "Ask Brain"** now. iMessage later as its own brief, gated on a leak test proving the bridge sees only one thread (it would need Full Disk Access to the whole Messages database).
- **Corpus: whole vault**, read-only. Existing exclusions stay (`.git`, `.obsidian`, binaries, reserved acceptance cases).
- **Host: the MacBook Air** until the always-on host arrives (Q30 open).

## Files in scope
- `~/Documents/dbrain-runtime/`: `dbrain/serve.py`, the whole-vault profile in `dbrain/config.py`, the opt-in hooks in `scope.py`, `index.py`, `answer.py`, `trace.py`, `mvp/`, `tests/test_serve.py`, `experiments/mvp_smoke.py` and `experiments/sandbox-smoke.sb`; `artifacts/` for logs and traces (git-ignored).
- `~/Library/Application Support/dbrain/` (pinned model and runtime copy, outside the vault).
- This brief; `90 System/for-david.md`; TASKS P2.4 and P4.1; the S2–S6 plan; `index.md` and `log.md` entries.

## Architecture
*Transport, as built:* plain HTTP inside the Tailscale (WireGuard) tunnel, not HTTPS; `tailscale serve` can add HTTPS later if the Shortcut needs it.
```
iPhone Shortcut ──HTTP inside WireGuard (Tailscale)──▶ Air: /ask service ──▶ P2.2 query service ──▶ llama.cpp (local, no cloud fallback)
     ▲                                                    │
     └────────── answer + citations + status ◀────────────┘
```

## Build steps (lead)
1. **`/ask` endpoint** in `dbrain-runtime`: `POST /ask {question}` → `{answer, citations[path + lines], status: supported|incomplete|withheld|malformed, latency_s}`. Calls the existing P2.2 service unchanged. Read-only.
2. **Bind only to the Air's Tailscale address**, never `0.0.0.0` or the LAN. Refuse anything not on the tailnet.
3. **Bearer token auth.** The token lives in the macOS Keychain and in the Shortcut, **never in a file an agent can read** (data policy §2.2). Constant-time compare; 401 on mismatch.
4. **Corpus profile `mvp-whole-vault`**: whole vault minus existing exclusions. Each citation shows its folder, so answers sourced from `00 Inbox` (unreviewed) are visibly marked as such.
5. **Guards:** 120 s request timeout, one request at a time (queue or 429), question length cap, no shell or tool execution from question text. Vault content is evidence, never instructions.
6. ~~Run as a launchd user service~~ **Amended by Q35 (David, 5 Oct): a Terminal login item** (`mvp/Ask Brain.command`) that starts at login and restarts the model or the service on crash, plus a keep-awake on power (`caffeinate -s`) while it runs. No launchd and no Full Disk Access for the system Python; a signed helper comes later on the always-on host. Traces and raw data go to the git-ignored folder in `dbrain-runtime` (Q23).
7. **Health check** `GET /health` (no vault content) so the Shortcut can say "Air is asleep or offline" instead of hanging.
8. **Shortcut recipe** for David (Cowork writes the step-by-step once the endpoint exists): Ask for Input (text or dictation) → Get Contents of URL (POST, header `Authorization: Bearer …`) → Show Result → optional Speak Text.

## David's steps
- Install Tailscale on the Air and the iPhone, same account, and turn on MagicDNS (≈15 min).
- Energy settings on the Air: prevent sleep when on power.
- Build the Shortcut from Cowork's recipe (≈10 min).

## Done when (checkable)
- From the iPhone on **home Wi-Fi** and on **4G with Wi-Fi off**: 5 questions each return an answer with citations and a status.
- A request from a device **not on the tailnet** fails; a request with a **wrong token** gets 401; a test with the network blocked shows **no cloud fallback**.
- ~~With the Air asleep, the Shortcut shows a clear "offline" message within 10 s.~~ **Amended 5 Oct (Q36): a known limitation on the Air host.** With nothing listening, the request hangs and Shortcuts offers no client timeout, so no server-side change can fix it. David accepted it; the criterion moves to the always-on host (Mac mini), which removes it. No workaround work on the Air.
- *(Added 5 Oct, acceptance fixes)* Every `/ask` response the handler produces, including its errors (400, 401, 403, 404, 411, 413, 423, 429, 503, 500), carries a readable `display`; the status line is plain language; the cited note's own line(s) are quoted under the answer, **when they share words with it**: a source with no word overlap gets no quote, and lines over 160 characters are cut with an ellipsis, so the quote is a verbatim excerpt, not always the full line. `/health` returns plain JSON for the Shortcut's own check, and errors raised by the HTTP library itself before the handler runs (a malformed request line) carry none.
- The token appears in no file under the vault or `dbrain-runtime` (secret scan clean).
- Latency recorded per request (p50/p95) alongside run B; not a D56 acceptance claim.

## Constraints
- **Branch for speculative work (D50):** build on `mvp-phone` in `dbrain-runtime`. Merge to `main` (this repository's default branch; the vault's is `master`) only after a Codex review, which is batched when the rate limit resets. David may use the branch build before review (his MVP call, 5 Oct); it is read-only.
- The open P2.2 write-path findings (round D/E) don't block this, because `/ask` writes nothing to the vault. Traces go only to the git-ignored runtime folder.
- No new cloud service other than Tailscale's coordination server, which sees device metadata, not content. Recorded as a data-flow note for T8.
- Labels stay strict (Q21): no `supported` before T4.1.
- Plan impact: an S4 slice (private remote text access) moves into S2. The lead updates the draft S2–S6 plan; voice beyond dictation, durable capture and offline queue stay in S4.

## Acceptance evidence (David, 5 Oct, via Cowork)
| Check | Result |
|---|---|
| Mac, Shortcut: "November lunch booking deadline?" | ✅ correct (Fri 16 Oct), cited Inbox note lines 16–22, marked unreviewed, 8.4 s |
| iPhone on Wi-Fi: "Climbing on Mon 2 Nov?" | ✅ correct |
| iPhone on **4G, Wi-Fi off** | ✅ reached the Air. "School on 2 Nov?": fact correct, phrasing contradictory ("Yes, there's no school on Nov 2") |
| Wrong token | ✅ refused (401, two in the service log at 13:54) · ❌ the Shortcut showed nothing: errors had no `display` |
| Air asleep | ❌ against the 10 s criterion: hangs. **Q36: accepted as a known limitation on the Air** |
| First run from the Mac | "could not connect", fine on retry. No failed request reached the service (its log starts with a 200 at 13:48:27), so the request never arrived; the start line had no timestamp, so "service not listening yet" can't be ruled in or out. A timestamp is now logged at start-up |

**Fixes made (lead, 5 Oct, on `mvp-phone`, uncommitted):**
1. **Plain status line** (`status_line`, last lines of `display`): e.g. "Not verified (no automatic fact-check yet) · from an unreviewed Inbox note"; the technical `reason` stays in the JSON.
2. **Quoted source lines:** under each numbered source, the note's own line(s) that best match the answer, verbatim, so "Yes, there's no school" sits next to "No school Mon 2 Nov". The answer's `[E3]` ids are renumbered `[1]`, `[2]` to match the listed sources.
3. **Fact first:** an MVP-only prompt adds "Start with the fact itself … Do not begin with Yes or No" and asks for 1–3 sentences. P2.2's prompt is unchanged (its pinned version `3e00bced79dc` is asserted by a test). A prompt rule lowers the risk; it does not remove it, which is why fix 2 shows the source.
4. **Readable display on every error:** 400, 401, 403, 404, 411, 413, 429, 503 and a catch-all 500 each carry a plain, generic sentence (401: "Not authorised: the token in this Shortcut doesn't match. Re-copy it from the Keychain on the Air"). A client-side timeout (Air asleep) cannot carry one (Q36).

Tests: 27 MVP tests (the 18 original, 7 for these display fixes, 2 for the client-note pause), full suite passing, secret scan clean. **David's running service picks these up only after a restart** (quit and reopen `Ask Brain.command`). The real-model smoke test was not rerun: it would collide with the running service's model port.

## Review
Codex `gpt-6.1-sol`, effort `high`, read-only (David switched the review profile from `gpt-6-astra` on 5 Oct).
- **Round 4 (5 Oct): PASS** for this documentation commit (no blocker or should-fix; one nit on the test count, fixed). It does not approve the runtime code, which waits for P2.2.
- **Round 3 (5 Oct): FAIL.** Blocker: a second gap in the client stop (a nested complex key gives a 500, no flag). Should-fix: the quote limits. Nits: the HTTPS diagram; Q34's "master". **Addressed:** both gaps documented as open in P2.2; quote limits stated; diagram corrected. Q34 is left as David wrote it (an answer is not edited); this brief records that "master" there means `main` in `dbrain-runtime`.
- **Round 2 (5 Oct): FAIL.** Blockers: the client-note stop was overstated (the padded-fence gap); acceptance was claimed complete; D59 fields and Files in scope missing. Should-fixes: HEAD pointed at `main`; Q34's "master"; HTTP vs HTTPS, the 120 s deadline and "every response" overstated. **Addressed** in this revision: each claim now states what is and is not proven, the open checks are listed, HEAD points at `mvp-phone` again.
- **Round 1 (5 Oct, brief with Q32–Q34): FAIL.** Blocker: the brief said `client` notes are "skipped and traced"; AGENTS.md rules 2–3 require stop and flag. Should-fixes: step 6 still said launchd though Q35 chose the Terminal login item; the "not yet done" list was stale; the dependency on Q35/Q36 records. Nit: `main` vs `master`. **Addressed:** a `client` note, or any label that is not plainly public/internal, now pauses the service (423, `POLICY FLAG` in the log, nothing answered); step 6 amended by Q35; David's steps marked done; `main` is this repository's branch, `master` the vault's. Q35 and Q36 are committed (`2c52dc3`, `6985ee1`).
- **The code is not in this commit.** It lives uncommitted in the `dbrain-runtime` working tree, whose HEAD is the unborn branch `mvp-phone` (the repository has no commits yet; `main` gets its first commit when P2.2 passes, and `mvp-phone` then branches from it). Q34's "merge to master" means that repository's default branch, `main`; the vault's is `master`. The code sits on top of the P2.2 code, which is **parked after its fifth review this run** (brief P2.2, round I). The branch merges only after P2.2 passes and is committed and the MVP code itself passes review.
## Outcome
**Session 17 (5 Oct), lead (`claude-opus-5-5`): steps 1–7 built on branch `mvp-phone` in `dbrain-runtime`, uncommitted, in review.**

| Step | State |
|---|---|
| 1 `/ask` | `dbrain/serve.py`: `POST /ask {question}` → `{answer, citations[{path, lines, folder, unreviewed}], status, reason, latency_s, display}`; calls `answer.ask()` unchanged. `display` is one text block for Show Result / Speak Text |
| 2 bind | Tailscale address from the Tailscale CLI, or `--host`; only 100.64.0.0/10, fd7a:115c:a1e0::/48 or loopback; refuses `0.0.0.0`, `::`, LAN; every peer checked too (403) |
| 3 token | Keychain item `dbrain-mvp-ask`, created by David with `mvp/make-token.sh` (clipboard for 120 s, never a file); read at start-up into memory; `hmac.compare_digest`; 401 otherwise |
| 4 corpus | Profile `mvp-whole-vault`: vault root, dot-folders excluded; a note with **no** `classification` is skipped and traced, not indexed. **A `client` note, or any label that is not plainly public/internal, stops the service**, with **two known gaps, both open in P2.2 round I and fixed only with P2.2**: an opening fence with trailing spaces (`--- `) is read as no frontmatter, so such a note is skipped rather than stopping; and a nested complex YAML key (`? [a, b]`) raises an uncontrolled error, so the phone gets a 500 without a `POLICY FLAG`. In both cases the note's content never reaches the model, but the stop-and-flag is not reliable until P2.2 lands (Codex review of this brief, AGENTS.md rules 2–3): every question gets 423 "Paused", the note's path goes to the Air's log as `POLICY FLAG`, nothing is answered until it is removed or relabelled (fail-closed label rule from P2.2 round G). 142 notes, 1,390 chunks, 0.08 s to index. Citations carry the folder; `00 Inbox` ones are marked unreviewed |
| 5 guards | 4 KB body, 500-character question, one at a time (429), model call timeout 110 s and socket timeout 130 s; **there is no single end-to-end 120 s deadline**, which the brief's step 5 asked for (open). No tool or shell path exists |
| 6 start-up | **Per Q35: Terminal login item** `mvp/Ask Brain.command` → `mvp/run-all.sh`: runs llama-server (loopback) and `/ask`, restarts either on exit, `caffeinate -s` for as long as it runs. No launchd, no Full Disk Access. Pinned model and runtime copied to `~/Library/Application Support/dbrain/` (`mvp/prepare-model.sh`, hash-checked; done 5 Oct) |
| 7 health | `GET /health` → `{ok, model: up/down, busy}`; no auth, no vault content |

**Tests (at that point; earlier baseline):** 18 new (`tests/test_serve.py`), 102 in all, passing; secret scan clean. **End-to-end smoke** (`experiments/mvp_smoke.py`, real model, whole vault, loopback, network blocked): health, 401 for wrong and missing token, 503 `unavailable` with the model stopped (no fallback). 10 questions, p50 21.1 s, p95 38.6 s:
- **6/10 correct** (latency target, Dinant time, children's-names rule, bank-account question declined, November lunch deadline, Halloween start).
- **2/10 confidently wrong:** climbing on 26 Oct ("yes", while quoting "none … 26 (autumn break)"); school on 2 Nov ("yes"; the note says no school).
- **2/10 missed** by retrieval (Tailscale choice; waste on 13 Oct).
- Every status `incomplete` or `withheld` (Q21), every Inbox citation marked unreviewed. The smoke test's own substring check scored 8/10; the lead's reading is the one above.

**David's setup steps: done 5 Oct** (Tailscale on the Air and iPhone, token, Login Item, Shortcut); acceptance evidence above. The Air's Tailscale address is `100.85.213.114` (from the service log); the Shortcut uses the MagicDNS name.
**Done-when checks still open:** five questions on home Wi-Fi and five on 4G (one each recorded so far, plus one from the Mac); a request from a device not on the tailnet; a re-run of the phone checks after the display fixes, which needs David to restart `Ask Brain.command`; the 120 s end-to-end deadline (step 5). Met: 4G reaches the Air; a wrong token is refused (now with a readable message); the token is in no file (scan clean); no cloud fallback (smoke test, network blocked). The Air-asleep check moved to the always-on host (Q36).
