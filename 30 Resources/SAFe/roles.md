---
classification: internal
status: draft
updated: 2026-10-01
tags: [safe, roles, governance, lens/pl, lens/pgm, lens/tc]
---

# Roles

Who does what, how they relate, who to cast in each role, and what happens to managers. The casting
guidance (attributes and candidate pools) comes from the *Mapping Organisational Roles* toolkit and is
the part most useful in a transformation.

## Role map by level

| Level | Role | One-line accountability | 6.0 notes |
|---|---|---|---|
| **Team** | **Product Owner (PO)** | Content authority for the team backlog; accepts stories | — |
| | **Scrum Master / Team Coach (SM/TC)** | Servant leader and coach for the team; facilitates team events, removes impediments | **[6.0]** renamed from Scrum Master; broadened to coaching, also for Kanban teams |
| | Agile Team members | Define, build, test and deliver increments | — |
| **ART** | **Release Train Engineer (RTE)** | Chief servant leader and coach of the ART; owns the process, flow and improvement | — |
| | **Product Management (PM)** | Content authority for the ART backlog: vision, roadmap, features, WSJF | — |
| | **System Architect (SA)** | Technical authority for the ART: architectural runway, enablers, NFRs | 5.1: "System Architect/Engineering" |
| | **Business Owners (BO)** | Small group accountable for governance, compliance and ROI of the ART's solution; assign business value to PI objectives | — |
| | System Team | Builds and maintains the CI/CD and integration environment; helps integrate and demo | A 6.0 platform/enabling team pattern |
| | Shared Services | Specialists used by several teams (UX, security, data, compliance) | — |
| **Large solution** | **Solution Train Engineer (STE)** | The RTE role at Solution Train level | — |
| | **Solution Management** | The PM role at solution level; owns the solution backlog and capabilities | — |
| | **Solution Architect** | The SA role at solution level; owns solution intent and cross-ART architecture | — |
| | Suppliers | Internal or external providers integrated into cadence | — |
| **Portfolio** | **LPM** (function, not one person) | Strategy and investment funding, agile portfolio operations, lean governance | — |
| | **Epic Owner** | Shepherds an epic through the portfolio Kanban: hypothesis, lean business case, MVP | — |
| | **Enterprise Architect** | Technology strategy across value streams; enabler epics | — |
| | **APMO** (Agile PMO / VMO) | Runs portfolio syncs, coordinates lean budgeting and governance, harvests execution patterns | Some enterprises call it a VMO |
| **Change** | **LACE** | Guiding coalition that runs the transformation as an Agile team | See [[transformation-playbook]] |
| | **SPC** | Certified change agent who trains and coaches | **[2024+]** Advanced SPC (ASPC) added |
| **AI-Native** | **AI Value Architect** **[AI-Native]** | Coaches AI adoption, unlocks value from AI tools, bridges business/tech on risk, legal, data and ethics, optimises outcomes | See [[ai-native-safe#9. Roles]] |

## Content vs technical vs process authority

The three-way split behind every SAFe level. Most dysfunctional ARTs have blurred it.

| Authority | Team | ART | Solution | Portfolio |
|---|---|---|---|---|
| **Content: what and why** | PO | Product Management | Solution Management | LPM / Epic Owners |
| **Technical: how** | Team | System Architect | Solution Architect | Enterprise Architect |
| **Process: flow and improvement** | SM/TC | RTE | STE | APMO / LACE |
| **Business accountability** | — | Business Owners | Business Owners / customer | LPM fiduciaries |

## RACI: key ART decisions and activities

R = responsible, A = accountable, C = consulted, I = informed.

| Activity | PM | PO | RTE | SA | BO | Teams | SM/TC |
|---|---|---|---|---|---|---|---|
| Vision and ART roadmap | **A/R** | C | I | C | C | I | I |
| ART backlog prioritisation (WSJF) | **A/R** | C | I | C (enablers) | C | I | I |
| Feature definition and acceptance | **A/R** | C | I | C | I | C | I |
| Team backlog and story acceptance | I | **A/R** | I | C | I | C | C |
| Architectural runway and NFRs | C | C | I | **A/R** | I | C | I |
| PI Planning preparation and facilitation | R (content) | R (team content) | **A/R** (event) | R (arch briefing) | C | C | R |
| Business value scoring of PI objectives | C | C | I | I | **A/R** | C | I |
| ART Sync / dependency and risk management | C | C | **A/R** | C | I | C | R |
| System Demo | R | R | **A** | R | C | R | C |
| I&A problem-solving workshop | C | C | **A/R** | C | C | R | R |
| Release decision | **A** | C | R | C | C | I | I |
| ART metrics and predictability reporting | I | I | **A/R** | I | I | C | C |

## Casting the roles: attributes and candidate pools

The toolkit's core advice: **cast on attributes, not on current job title.**

| Role | Must-have attributes | Good candidate pools | Watch-outs |
|---|---|---|---|
| **SM/TC** | Servant leader; influence over authority; empathy; protects the team; thinks beyond the current iteration | Testers (proven developer relationships), project managers, developers, team leads, external hires | Must not be the team's line manager. Ex-devs must not solution for the team |
| **PO** | Understands the customer; communicates bluntly; business sense; enough tech knowledge; negotiator; trusted; courage; vision | **Business analysts** (often already doing the PO work), SMEs, PMs, systems engineers, domain experts, architects | "Too busy, I have a real job" PO. Domain experts arguing with the team as an expert, not as PO. Rotating POs as the work changes |
| **RTE** | Trusted servant leader; programme-execution expertise; systems thinker; persuades rather than commands; can push back on executives | Programme/project managers, experienced SMs, Lean-Agile coaches, SPCs | Command-and-control PMs who can't make the shift. The toolkit says the RTE is "5× harder than SM", and external RTEs struggle |
| **PM** | Domain and market knowledge; balance (business demand vs capacity); hypothesis-driven; forward-thinking; builds consensus; messaging/positioning | Existing product managers, PMs/programme managers, UX architects, marketing/technical marketing, BAs or POs stepping up | SMEs without the time; a "throw requirements over the wall" habit |

### Push, pull, or hybrid?

| Approach | How | Effect |
|---|---|---|
| **Push** | Management assigns roles | Fast, but breeds resistance and attrition |
| **Pull** | Role personas posted; people apply | High engagement; works well early in a transformation |
| **Hybrid** (recommended) | Published role guidelines, people apply, the manager reviews readiness and commits support | Balances choice and organisational control |

**Timing.** Identify people for roles once value streams are defined, then train them *before* they
start in the role. Training is partly a security signal: it shows the organisation is investing in
them. Communicate neither too early (nothing concrete to say yet) nor too late (behind the rumour mill).

## What happens to managers

The toolkit's three roles for managers in SAFe:

1. **Lead the mission.** Set the mission with minimal constraints; act as Business Owner; sit in the
   LACE or APMO; co-create strategy; remove impediments.
2. **Develop people.** Coaching, career and skills development, compensation and performance, removing
   demotivating policies, honest feedback.
3. **Act as lean-thinking manager-teachers.** Embody the mindset and teach it.

Train managers in the team-level classes too (SAFe for Teams, Scrum Master). Early Agile failed in
part because it cut managers out, and they resisted. Make sure nobody leaves the roles conversation
thinking "I'm not on the Big Picture, should I update my CV?"

## Use it as…

- **PL:** if you're the PM or Solution Manager, your power is WSJF plus vision. Protect the PM/PO
  split and don't become a super-PO.
- **PgM:** the RTE is the natural landing role for programme managers, but only with a servant-leader
  shift. Use the RACI to settle "who decides" fights quickly.
- **TC:** role mapping is the change-management workstream. Run it explicitly, with personas, a pull or
  hybrid process and a communication plan.

## Related

[[events-and-cadence]] · [[product-management-and-po]] · [[pi-planning-and-execution]] · [[transformation-playbook]] · [[lean-agile-leadership]]
