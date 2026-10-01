---
captured: 2026-10-01T14:41:00+02:00
source: conversation-with-codex
classification: internal
status: unprocessed
tags: []
---
# pro/private split

David asked to capture the following assistant recommendation for later triage. This capture does not authorize a vault migration or policy change.

**Yes. I recommend separating personal and professional information before adding more sensitive material, with access enforced by the application—not just instructions telling agents to stay in their lane.**

For Dbrain2, I would use **two operational vaults and a separate demo environment**:

| Space | Contents | Default access |
|---|---|---|
| **Personal** | Your health, journal, personal finances and permitted family logistics | Personal assistant; local processing by default |
| **Professional** | Your professional knowledge, learning, positioning and permitted business notes | Professional assistant; explicitly approved tools |
| **Demo** | Synthetic examples and deliberately approved exports | Demonstration agents; no connection to either live vault |

Public reference knowledge can be shared read-only where useful. There is no need to split every topic into its own vault.

**Separate vaults help organize the boundary, but they do not enforce it.** If both agents run with unrestricted access to your Documents folder, both can still read everything. Permissions must be checked outside the model, on every retrieval and tool operation. This follows OWASP’s guidance on minimum permissions and application-enforced authorization. [OWASP](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/)

For your build, I would implement these boundaries:

- **Separate access scopes:** the professional agent cannot search, list or open personal files. Enforce this through scoped tools and sandbox/filesystem permissions.
- **Separate histories and indexes:** conversations, retrieval indexes, caches, logs and backups must preserve the same separation. A personal summary leaking into professional agent memory defeats the boundary.
- **Scoped writing:** one controlled writing mechanism can serve both vaults, but each operation receives permission for only its authorized destination and approved patch.
- **Restricted outbound access:** the personal agent should have no email-sending, publishing or unrestricted network tools by default. Online research can run separately using a deliberately limited query.
- **Explicit transfers:** moving knowledge across the boundary requires reviewing the exact information being transferred.

You can still use **one interface and one local model**. The interface should clearly show “Personal,” “Professional” or “Demo,” with a separate conversation for each. The same model weights can serve them; isolation belongs in the surrounding system, its state and its permissions.

For requests spanning both worlds, share the minimum needed. For example:

> “Help me plan work around a medical appointment.”

The professional planner usually needs “unavailable Tuesday 14:00–16:00,” not the diagnosis or medical note. A coordinator should receive that approved availability constraint without gaining access to the entire personal vault.

Your current classification is too broad for this future use. `internal` presently covers both your business material and your health information—and permits cloud processing and demonstrations of your own data. I would separate these decisions:

| Policy dimension | Example |
|---|---|
| Domain | Personal / professional |
| Sensitivity | Ordinary / sensitive |
| Processing permission | Local-only / approved external provider |
| Sharing permission | Private / explicitly approved for demo |

These labels inform controls; they must not grant access merely because an agent or imported document changes them.

**There is an important existing-policy distinction:** your own health data is allowed today, but sensitive information about family members is currently excluded. Minimal family logistics and someone else’s medical history are different categories. A new vault would not change that rule, nor would it make client-confidential material permissible. Any expansion needs a deliberate change to your [[10 Projects/AI Second Brain/02_Architecture/data-policy|data policy]].

For storage, use separate Git repositories and appropriately protected backups. Removing a note from the current folder does not remove earlier copies from Git history. If you use Obsidian Sync, its end-to-end encryption protects remote synchronization; **it does not encrypt the local vault**. Local device protection and agent permissions remain necessary. [Obsidian documentation](https://help.obsidian.md/sync/security)

**My recommended next step is to define this access matrix in S1, then test it before expanding the sensitive corpus.** Use synthetic private notes to verify that the professional agent cannot retrieve them, see their titles, receive them through another agent, or access them through logs. That would also give your showcase concrete evidence of enforced information boundaries.
