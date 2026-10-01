---
classification: public
status: draft
updated: 2026-10-01
---

# Billing rules — nursing

**Governing text:** art. 8 (soins infirmiers), **current version read: in force 1 September 2026**.
**Key letter: W.** Two interpretative rules (M.B. 24.9.2025).

Rule semantics: [[billing-engine-rule-model]]. Transport of the notifications below:
[[mycarenet-services-and-flows]].

## Three nested scopes — get these right first

Nursing is the one article where the billing unit is not obvious, and three different scopes carry
different rules:

| Scope | What it governs |
|---|---|
| **Séance de soins** (care session) | A single visit. Most cumulation prohibitions bite at this level |
| **Journée de soins** (care day) | The unit for visit ranking and for all forfaits |
| Treatment period | The notification/agreement regime, with a 3-month re-notification trigger |

*(The precise definition of a* journée de soins *— whether it equals a calendar day, and how a visit
crossing midnight or a colleague's cover is treated — is not established here. To verify.)*

## Visit ranking: equal value, not reduced

| Code | Service | Coefficient |
|---|---|---|
| `425014` | **First** basic service of the care day | W 0,879 |
| `425036` | **Second** basic service of the care day | W 0,879 |
| `425051` | **Third or more** basic service of the care day | W 0,879 |

**No reduction for later visits.** Anyone porting the physiotherapy assumption (where a second daily
session is a halved code) will under-bill nursing. See [[billing-rules-physiotherapy]].

## Care-day forfaits — they replace per-act billing

Granted **once per care day for the whole of the nursing care** given. Eligibility is a dependency score
on six criteria — washing, dressing, transfer/mobility, toileting, continence, eating — at score 3 or 4.

| Code | Forfait | Coefficient | Dependency criteria |
|---|---|---|---|
| `425272` | **A** | W 3,825 | Washing **and** dressing; **and** transfer/mobility **and/or** toileting |
| `425294` | **B** | W 7,371 | Washing **and** dressing; **and** transfer/mobility **and** toileting; **and** continence **and/or** eating |
| `425316` | **C** | W 10,083 | Washing (4) **and** dressing (4); **and** transfer/mobility (4) **and** toileting (4); **and** continence **and** eating (one at 4, the other ≥3) |

### Palliative forfaits

Require both the dependency criteria **and** the palliative-patient definition of §5bis, 1°. Multiple
variants exist across rubrics:

| Code | Forfait | Coefficient |
|---|---|---|
| `427011` | PC | W 14,422 |
| `427092` | PC (other rubric) | W 17,493 |
| `427033` | PB | W 11,750 |
| `427055` | PA | *(not captured)* |
| `427136` | PA (other rubric) | W 16,253 |
| `427173` | PP (§4, 6° beneficiaries) | W 10,887 |

### Specific technical acts

`425375` — forfait per care day covering one or more specific technical acts (placing and/or monitoring
IV or subcutaneous perfusions; administering and/or monitoring parenteral nutrition): **W 8,934**.

### Forfaits are not all mutually exclusive

Diabetic-patient forfaits (rubrique VI §1, 1° and 2°) **may be cumulated** with heavily-dependent-patient
forfaits (rubrique II §1, 1°, 2°, 3° and 3°bis). Do not model "one forfait per care day" globally — model
it per rubric, with an explicit cross-rubric allowance.

## Cumulation — mostly session-scoped

| Rule |
|---|
| `424395`, `424690`, `427991`, `424852` cover **all components of the basic service** (§4, 1°) and may **not** be cumulated **in the same session** with a basic service — unless one or more technical services are performed in that session |
| `425736`, `425751`, `425073` reimbursed **only once per day** and not cumulable in the same session with **any** other article 8 service, **except a basic service** |
| Large enumerated sets (`424270, 424432, 424572, 427851, 430076, …` and `424336, 424491, 424631, 427932, …`) may not be cumulated within a single session |
| `425375`, `425773`, `426171`, `429155`, `430393` are cumulable with `423113`, `423312`, `423415`, `429170`, `430415`, `421072`, `421094`, `421116`, `429192`, `430430` **only when the injection sites differ** — an anatomical condition on cumulation |
| `429015` and `424896` **are** cumulable with all article 8 services in the same session, save the stated exceptions |
| Certain care **is** cumulable within the same day with other technical nursing services of rubric I, A and B |

## Place of care can void the whole article

Article 8 **RI 01**: no article 8 service may be attested when delivered during a hospital's *"première
prise en charge des urgences"* or *"soins urgents spécialisés"*. And placing and/or monitoring an IV or
subcutaneous perfusion may **not** be attested via article 8 when performed in a hospital, **including its
consultation service**.

This is an article-level exclusion, not a code-level one — model it as such.

## Delegation: the file is the evidence

Article 8 **RI 02**: preparing and administering medication for chronic psychiatric patients
(`425736`, `425751`, `425073`) **may** be attested as delivered by an *aide-soignant* and reimbursed,
provided the **nursing file shows each part was performed by a provider competent for it** — preparation
falls outside a care assistant's competence, administration within it. A **systematic refusal** in that
case is **unjustified**.

## The notification regime

| Rule |
|---|
| The nurse must **notify the médecin-conseil** of the attestation of certain services, per §7, 5° |
| An **electronic form** justifying the care-day forfaits or *soins de toilette* is completed by the nurse and transmitted **via the electronic network of art. 159bis §1** of the law |
| Deadline **10 calendar days**. If missed, the médecin-conseil **may nonetheless decide** to cover the care, **at the earliest from the first day** |
| A **new electronic form** is required when treatment continues beyond the notified period, when it **exceeds 3 months**, or **when the degree of physical dependency changes** |
| For `425110`, `425515`, `425913`, `427755`, `429973` performed for a beneficiary **not** meeting the rubric II/IV criteria, additional provider obligations apply (§ cited, detail not captured) |

The dependency-change trigger is the commercially interesting one: a patient's forfait tier can shift
between A, B and C, and the revenue follows only if someone re-scores and re-notifies.

## Build implications

1. **Model three scopes separately** — session, care day, treatment period. Most cumulation rules are
   session-scoped; forfaits and ranking are care-day-scoped.
2. **Never reduce later visits in a care day.** Rank them, price them equally.
3. **Dependency scoring is a revenue engine.** Six criteria, scores 3/4, driving an ~2.6× spread between
   forfait A and C. Build the scoring instrument into the clinical record, with history.
4. **Re-scoring must be prompted**, on dependency change and at the 3-month boundary, with the
   notification generated from it.
5. **Track the 10-day notification deadline** and the discretionary late-acceptance path — late is not
   automatically lost.
6. **Capture injection sites structurally**, because cumulation legality depends on them.
7. **Forfait cumulation is per rubric**, not globally exclusive — diabetic plus dependency forfaits coexist.
8. **Article-level place exclusion**: if care happened in a hospital emergency or consultation service,
   suppress the entire article 8 claim path, not individual codes.
9. **Record who performed which component** of a delegated service; RI 02 makes that the difference
   between paid and refused.

## Gaps and figures to verify

- Definition of *journée de soins*, and midnight/shared-cover handling.
- `427055` (PA) coefficient, and the full palliative rubric structure.
- Rubrics III–VI in full (specific technical acts, diabetic patients, supplementary honoraria).
- The *soins de toilette* code set and its own rules.
- The full §4 component list defining a basic service.
- Wound-care and `430000`-family interplay with article 8 billing — see [[mycarenet-services-and-flows]].

Sources: [[sources]].
