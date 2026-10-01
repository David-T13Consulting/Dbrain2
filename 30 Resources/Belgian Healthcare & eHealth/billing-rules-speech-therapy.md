---
classification: public
status: draft
updated: 2026-10-01
---

# Billing rules — speech therapy (logopédie)

**Governing text:** art. 36 (logopédie), **current version read: in force 1 September 2026**.
**Key letter: R.** 8 interpretative rules.

Speech therapy is the clearest worked example in the nomenclature of a **prior-agreement regime**: almost
nothing is payable without an agreement from the médecin-conseil, obtained through a defined process with
hard retroactivity limits. If you are building an agreement workflow, model it here first.

Rule semantics: [[billing-engine-rule-model]].

## The agreement regime

| Step | Rule |
|---|---|
| **Request** | On a form whose model is approved by the Comité de l'assurance, submitted **without delay** by the *logopède* to the **médecin-conseil** of the beneficiary's insurer |
| **Prescription** | A **medical prescription** is annexed to the request, established by a prescriber named in a table in the article (with stated exceptions). An earlier provision requires the prescriber to hold an **active INAMI number** |
| **Channel** | A copy of the medical prescription and the request form are attached **electronically via eAgreement** at each treatment start |
| **Retroactivity limit** | *"L'intervention est refusée pour toute séance de bilan ou de traitement effectuée plus de 60 jours calendrier avant la date de réception de la demande par le médecin-conseil."* — **sessions more than 60 calendar days before receipt are refused** |
| **Duration** | *"L'accord ne peut porter que sur un traitement de deux ans au maximum."* — **max 2 years per agreement** |
| **Extension** | Reimbursement for extension sessions is possible **only if the médecin-conseil holds a valid notification**. The same **60-day** rule applies to extension notifications |
| **Extension form** | Must use the notification form matching the model established by the Comité de l'assurance on the proposal of the *Commission de conventions logopèdes–organismes assureurs* |

The 60-day rule is the one that costs real money: treatment started before paperwork lands is
unreimbursable beyond that window, and it applies **twice** — at initial request and at every extension.

## Session allowances by disorder

Allowances are set per disorder category (§2 subdivisions), with their own extension rules:

| Rule |
|---|
| For beneficiaries under §2, a): an agreement may be given for a maximum of **55 individual treatment sessions** |
| A service capped at **5 times per *trouble traité*** (per disorder treated) |
| `733353` — individual session of **at least 30 minutes at the beneficiary's school**, maximum **5 per calendar month** |

## Age conditions

| Rule |
|---|
| **No session of at least 60 minutes** is reimbursable for beneficiaries **under 10 years old**, *"quel que soit le type de trouble visé par le présent article"* — whatever the disorder |
| **Dysphasia**: severe receptive and/or expressive language disorders **persisting after the fifth birthday** that gravely interfere with social communication |
| Beneficiaries under §2, b), 4° aged **0 to 2 completed**: a **single agreement** may be given, running **until the eve of the third birthday** |
| Beneficiaries under §2, b), 4° aged **3 to 19 completed**: treatment may be **extended at most eight times** where treatment **began before the third birthday** |

That last pair is a genuine state machine: the extension entitlement at ages 3–19 depends on a fact about
when treatment started, years earlier.

## Cumulation

> *"Aucun bilan logopédique ou séance d'évaluation ne peut être cumulé avec une séance de traitement
> individuelle ou collective effectuée le même jour."*

**No logopedic assessment or evaluation session may be cumulated with an individual or collective
treatment session performed the same day.** Assessment and treatment are mutually exclusive within a day.

## Duration-determined codes

Sessions are published by minimum duration (at least 30 minutes, at least 60 minutes), so the code follows
**measured** duration — and interacts with the under-10 rule above, which bans the 60-minute tier entirely
for young children.

## Build implications

1. **Build the agreement state machine first.** Requested → received (timestamped) → granted → active →
   extension notified → expired. Nothing bills reliably without it.
2. **Compute the 60-day retroactivity window from the médecin-conseil's date of receipt**, not the date of
   sending, and warn the therapist *before* sessions fall outside it. This is the single highest-value
   validation in the article.
3. **Cap agreements at 2 years** and prompt for extension well before expiry.
4. **Record treatment-start date durably**, because extension entitlement at ages 3–19 depends on whether
   treatment began before the third birthday — a fact needed up to 16 years later.
5. **Enforce the under-10 ban on 60-minute sessions** at scheduling time, not at billing time; otherwise
   the therapist has already done unpaid work.
6. **Count per disorder treated**, not per patient — a patient may carry more than one disorder.
7. **School sessions carry their own monthly cap**; capture the session location.
8. **Block same-day assessment plus treatment** in the diary, not just in the claim.
9. **Validate the prescriber's INAMI number is active** at prescription time.

## Gaps and figures to verify

- **Coefficients for all R-letter codes** — not captured in this pass. Needed before any fee calculation.
- The full §2 disorder taxonomy and the session allowance attaching to each category.
- The prescriber table and its exceptions.
- Collective-session rules and their caps.
- Whether eAgreement is the sole permitted channel, and the fallback if it is unavailable.
- Rules for treatment delivered remotely, if any.

Sources: [[sources]]. The eAgreement service itself: [[mycarenet-services-and-flows]].
