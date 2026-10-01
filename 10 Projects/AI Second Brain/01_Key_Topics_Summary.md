---
classification: internal
---
# AI Webinar — Key Topics Summary

**Source:** 67 screenshots captured Sept 2–4, 2026, from a French-language webinar/bootcamp called **"Prisme One" / "OS IA"** (creator: Eliott Meunier). Content spans two related sessions: a strategy webinar on building a personal AI operating system, and a bootcamp curriculum walkthrough (4 weeks + hackathon) plus a follow-up session on organizational impact.

**A note on scope:** this is one creator's specific method, wrapped in a paid bootcamp pitch (cost comparisons, "value estimated at X€" per module are sales framing). Treat the cost/ROI figures as illustrative, not verified — the architecture and methodology underneath are the reusable part.

---

## 1. The core idea, in one line

> **AI performance = Context × Model × Tools**, delivered through a stack you own: **Context → Interface → Model → Tools → Server**.

The pitch is that most people invest in the "Model" variable only (which model to use) and ignore Context and Tools — which is where 80% of the leverage actually is. A well-structured personal context turns any model into a system that "already knows you."

## 2. The system architecture: 3 layers of context

| Layer | French term | What it is | Where it lives |
|---|---|---|---|
| **1. Static context** ("Second Brain") | Second Cerveau | Who you are, your offers, vision, writing style, standing knowledge | Obsidian vault, PARA-like folder structure |
| **2. Dynamic context** | Contexte Dynamique / Bases de données | What changes daily: clients, deals, active projects | NocoDB / Supabase / a lightweight self-hosted CRM |
| **3. Capabilities** | Capacités / Skills / Fiches process | Your documented methods — how *you* do a task, step by step, so the AI executes in your method | Markdown "SKILL.md" files with frameworks + examples + templates |

**Obsidian vault structure shown (PARA-inspired):**
```
0 INBOX
1 PROJETS / 1 PROJECTS
2 CASQUETTES ("hats" — your roles)
3 RESSOURCES
4 ARCHIVES
5 ATTACHMENTS
Perspectives (a saved view/dashboard across the above)
```

**Skill file pattern** (repeated across multiple examples — e.g. copywriting, prospecting, ad production):
```
agent-xxx/
├── SKILL.md              ← the agent's "brain": role, method, rules
├── frameworks/           ← reference frameworks, loaded on demand
│   ├── style-univers-semantique.md
│   ├── pas-aida.md, pastor.md, schwartz.md ...
└── bibliotheque/         ← passive, reusable library (no logic itself)
    ├── 1-formats/        ← templates
    ├── 2-exemples/       ← 2–3 real calibration examples per format
    └── 3-elements-variables/
```
The framework name used for this static-context/skill design is called **IPCRA** in the source material (referenced but not detailed on-screen).

## 3. Choosing a model: three axes, explicit trade-off

| Axis | Question | Practical answer shown |
|---|---|---|
| **Performance** | Raw capability for the task | Frontier proprietary models (Claude Opus, GPT‑5.x, Gemini) generally lead |
| **Efficience** (cost/speed) | Good-enough at lower cost | Open-weight models (GLM, Kimi, Qwen, DeepSeek) at a fraction of the cost |
| **Privacy** | Where does the data go? | Proprietary API vendors (OpenAI/Anthropic-style) train on data by default in many tiers, retain logs 30–60 days, and are subject to the US CLOUD Act. Open-weight models hosted via EU/Swiss/"Zero Data Retention" (ZDR) providers avoid this. |

**Open-weight model + privacy-first hosting pairings mentioned:**

| Model | Hosting partner | Positioning |
|---|---|---|
| GLM 5.3 (flash) | synthetic.new | ~30 €/month, ZDR |
| Kimi K3 | Infomaniak (Swiss) | ZDR, Swiss data law |
| Qwen | Scaleway (French) | ZDR, health-data-grade compliance |
| DeepSeek V4 (flash) | Fireworks AI | ZDR |

> **⚠️ CORRECTED 7 Sept 2026.** This section originally carried a caveat saying that Anthropic and OpenAI "also offer zero-retention enterprise/API tiers," implying the webinar oversimplified. **That caveat was wrong.** As of August 2026 the picture reversed: Anthropic introduced a mandatory ~30-day retention requirement for business customers on its most advanced models, with zero-retention now available only by application and approval under a separate enterprise programme covering only certain models; OpenAI moved the other way with a preview of "Private Safety Processing" to preserve ZDR. Default retention for commercial API customers without a ZDR agreement is 30 days. **The webinar's privacy argument is therefore stronger than this document originally credited.** See `02_Critical_Assessment.md` §3.1 for detail and sources.

**Standing assumption to flag:** vendor data-handling policy is now a moving target, not a stable fact. Treat it as a dated decision record to be re-checked, not a settled assumption — this matters a lot given your banking/healthcare client background.

## 4. Interface layer: open-source vs proprietary

Mentioned but light on detail — the choice of *how* you talk to the model (a chat UI, an agentic coding tool, a mobile app) is separate from which model you use. Tools referenced on-screen: **OpenCode** (agentic coding interface, paired with Kimi K3), **Hermes Agent**, **OpenClaw** ("The AI that really does things" — inbox/calendar/WhatsApp automation).

## 5. Tools layer: MCP servers referenced

A large set of MCP (Model Context Protocol) integrations appeared in a sidebar in one screenshot, suggesting the "tools" layer is built from composable connectors: **NocoDB, Supabase, n8n, Metabase, Outline, Readwise, Firecrawl, Beeper, BrowserMCP, fal.ai, Whimsical, shadcn-studio**, among others.

## 6. Server layer: the self-hosted backbone

| Property | Detail |
|---|---|
| Hardware | A VPS (Virtual Private Server), ~10 €/month |
| Platform | Cloudron (self-hosting platform — "self-hosting has never been simpler") — runs chat, email, files, workflow automation (n8n-style), git, office suite, VPN, website, all as one-click apps |
| Why it matters | 1) Async work — automations and agents run while you're offline; 2) Software independence — swap models/interfaces freely, no vendor lock-in; 3) Expanded reach — the AI can act across all your tools, including writing code in them |
| Data ownership | Your data stays on infrastructure you control — explicitly framed against "an editor changing its Terms of Service tomorrow" |

**Illustrative cost comparison shown** (2024 traditional SaaS stack vs. 2026 self-hosted "Prisme One" stack):

| Category | Traditional SaaS (2024) | Self-hosted (2026) |
|---|---|---|
| CRM | HubSpot: 20,000 €/yr | NocoDB + Supabase: 0 € |
| No-code | Airtable: 2,500 €/yr | — |
| Training platform | 2,000 €/yr | 0 € |
| Slack | 1,500 €/yr | Discord: 0 € |
| Website | 1,000 €/yr | 0 € |
| Other | 5,000 €/yr | 2,000 €/yr |
| **Total** | **~32,000 €/yr, low flexibility** | **~2,000 €/yr, high flexibility** |

*(Take this delta with a grain of salt — it compares an enterprise SaaS stack to a solo/small-team self-hosted stack; the real-world migration cost of your own time isn't priced in.)*

## 7. Three mistakes the speaker calls out

1. **Badly structured context** — dumping notes with no folder logic, so the AI can't find or trust anything (fix: the static/dynamic/capabilities split above).
2. **No personal server** — relying entirely on someone else's SaaS/cloud, which caps what you can automate and where your data lives.
3. **Chasing the "shiny agent" object** — installing trendy autonomous-agent products instead of encoding your own well-defined process into a skill. (Examples shown: Hermes Agent, OpenClaw — presented as distractions, not necessarily bad tools.)

A second, more tactical version of "mistakes to avoid" (from the bootcamp-curriculum session): building skills from scratch with no template/method, and over-tuning agents/tools before you have a working process.

## 8. The bootcamp roadmap (4 weeks + hackathon)

| Week | Theme | You leave with | Nominal time cost |
|---|---|---|---|
| **1 — Fondations** | Deploy in an afternoon | Personal context captured once, system installed (~45 min), works across devices/models | 3.5–6h |
| **2 — Process & Agents** | Build your process + agents | Recurring tasks documented as skills; "CMA" method (Clarifier → Mapper → Amplifier) to decide what to automate; first working agent | 4–8h |
| **3 — Données, Serveur, Automatisations** | Data, server, automations | Own VPS deployed (~10 €/mo), workflows running unattended, mobile access | ~3–6h |
| **4 — Hackathon Business** | Accelerate | A sellable V1 offer, a prospecting + sales script built from your own positioning, a 30-day execution plan | Full "sprint" days |

## 9. Organizational / strategic framing (second session, Sept 4)

- **The delegation ladder:** Manual → Assisted (AI drafts, you validate everything) → Monitored (AI executes, you review) → Semi-autonomous (checkpoints only) → Autonomous (runs without you). Progress up this ladder requires **trust**, which is built loop by loop: reliable output → less verification needed → more delegated → more time freed → time reinvested in better methods.
- **Your value migrates to 3 roles:** the **Architect** (your judgment, encoded into the best method/skill), the **Manager** (reviewing whether a workflow is well executed), the **Strategist** (ideas, relationships, decisions).
- **"The org chart becomes workflows":** where you used to hire a *role* (job description, salary, management overhead), you now build a *workflow* (encoded method + AI execution + one accountable human).
- **The business map ("La carte")** — a full operating system view of a business, in 5 stages + one cross-cutting layer:
  Acquisition (content, ads, leads, qualification) → Vente (calls, proposals, follow-up) → Delivery (deliverables, project tracking) → Fidélisation & Support (care, upsell) → Referral (testimonials, referrals), plus **Pilotage** (metrics, reporting, decisions) running across all of them. Each stage is broken down into named workflows and skills in their live Obsidian/canvas example (e.g. `wf-prospection-outreach/skills/scraper-enrichir-nids`, with real cost data: ~$0.002/profile scraped, ~$0.005/profile enriched).

## 10. What's *not* fully captured here

A handful of screenshots (mostly Sept 3, ~13:06–13:10) repeat slide content already summarized above (the same "synthesis" and cost slides appear more than once — likely the presenter scrolled back). Nothing suggests a distinct topic was missed, but flagging this for transparency rather than claiming pixel-perfect coverage of all 67 images.

---

## What I'd suggest as your actual starting point

Given your stated goal — *"start an AI system with a second brain and an open source model"* — three honest observations before you build anything:

1. **The static-context piece (Second Brain in Obsidian) is the cheapest, lowest-risk place to start**, and is largely tool-agnostic — you can build it regardless of which model or server you end up choosing later. I'd sequence it first.
2. **"Open source model" and "self-hosted server" are two separate decisions** the source material bundles together. You can run an open-weight model (GLM/Kimi/Qwen/DeepSeek) via a hosted API today without standing up your own VPS — useful if you want to validate the context/skills approach before committing to infrastructure.
3. **Your actual constraint is probably data sensitivity, not cost.** Given your banking and healthcare client work, the privacy/CLOUD-Act argument in section 3 is the part most worth scrutinizing for your own use case — not the 32k€ vs 2k€ SaaS comparison, which is a sales angle.

I've set up a project folder to work from (see the accompanying structure) — happy to help you draft the actual context files, or pressure-test the model/hosting decision against your specific privacy requirements, whenever you want to go deeper on either.
