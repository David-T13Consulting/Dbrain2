---
classification: public
status: draft
updated: 2026-10-01
---

# Billing rules — midwifery

**Governing text:** art. 9 (accouchements), **current version read: in force 1 July 2026**.
**Key letter: V.** 7 interpretative rules.

Rule semantics: [[billing-engine-rule-model]].

## The defining structure: four delivery modes per service

Almost every midwifery service exists in **four parallel codes**, one per delivery mode. This is the
cleanest example in the whole nomenclature of mode-as-code-dimension, and it already includes telecare.

| Service | At home | In hospital | Outside home and hospital | **Via remote treatment** | Coefficient |
|---|---|---|---|---|---|
| **First** individual obstetric session | `422030` | `428094` | `428116` | `428750` | **V 21** |
| Individual obstetric session | `422052` | `428131` | `428153` | `428772` | **V 15** |
| At-risk pregnancy session, on prescription of a gynaecologist-obstetrician | `422870` | `428175` | `428190` | `428794` | **V 15** |
| At-risk pregnancy session (higher-value variant) | `422892` | `428212` | `428234` | `428816` | **V 22,5** |

On top of mode, a **working day vs weekend/public holiday** split applies to many services, producing
further code variants — article 9 carries 71 time-of-day expressions.

## Frequency cap: per pregnancy, across all modes

> *"Les prestations 422030, 428094, 428116, 428750, 422052, 428131, 428153 et 428772 sont remboursées au
> maximum douze fois par grossesse."*

**Max 12 per pregnancy**, counted across the **combined set** — first sessions and ordinary sessions, in
all four delivery modes. A per-code or per-mode counter will over-allow.

The scope is the **pregnancy**, not a calendar period. That requires an episode entity with a start, an
end and an outcome.

## Cumulation

| Rule |
|---|
| `422030, 428094, 428116, 428750, 422052, 428131, 428153, 428772, 422870, 428175, 428190, 428794, 422892, 428212, 428234, 428816` **may** be cumulated, **the same day**, with a consultation by a gynaecologist-obstetrician |
| The same set is cumulable **on the day of a miscarriage** with the miscarriage-care services `422553, 428256, 428271, 428831, 423555, 428293, …` |
| `422553, 428256, 428271, 428831, 423555, 428293, 428315, 428853` **are** cumulable with services performed the same day **during a day hospitalisation and/or a hospitalisation** |
| `423010-423021, 423032-423043, 424071-424082, 424093-424104, 424012-424023` are **not** cumulable with `474250-474261` |

Midwifery is unusual in how much it **explicitly permits** cumulation — the texts spell out allowances
rather than only prohibitions. Encode these as positive rules, not as absence of a ban.

## Miscarriage care

Dedicated codes by mode and day type, e.g. `422553` (at home, working day, V 20) and `428256` (in
hospital), *"dispensés le jour de la fausse couche"* — the care must be delivered **on the day of the
miscarriage** to attract these codes.

## Labour, delivery and supplements

| Item | Detail |
|---|---|
| Surveillance and assistance to the parturient during the **labour phase**, with its own weekend/holiday variant | art. 9 |
| `423511-423522` | **Supplement** for `423010-423021` performed **at night, at the weekend or on a public holiday** — **K 56** |
| `423533-423544` | **Supplement** for `424012-424023` in the same circumstances — **K 56** |
| `423032-423043` | Supplement for the **assistance of the treating accredited GP** (or GP with acquired rights) to `424115-424126` or `424012-424023`, including their fees |

Note these supplements carry key letter **K**, not V — a midwifery service can attract a
physician-scale supplement. Do not assume one claim uses one key letter.

For the night/weekend/holiday boundaries, use the article 26 definitions (weekend = Saturday 08:00 to
Monday 08:00; holiday = 21:00 the day before to 08:00 the day after) — see [[billing-rules-physicians]].

## Breastfeeding consultations

A separate series, split by **first vs follow-up**, **home vs hospital vs elsewhere**, and **working day
vs weekend/holiday**:

| Code | Service | Coefficient |
|---|---|---|
| `422833` | **First** breastfeeding consultation, at home, **weekend or public holiday** | V 33,75 |
| `428573` | First breastfeeding consultation, in hospital, weekend or public holiday | *(not captured)* |
| `422855` | **Follow-up** breastfeeding consultation, at home | V 19 |
| `428610` | Follow-up breastfeeding consultation, in hospital | V 19 |
| `428632` | Follow-up breastfeeding consultation, other setting | *(not captured)* |

## Documentation

The midwife must **motivate supplementary care in the beneficiary's file**, and *"fournit cette motivation
au médecin conseil et/ou au médecin traitant à leur demande"* — on request, to the médecin-conseil **and/or
the treating physician**. Note the dual recipient: unlike most articles, the treating doctor is an
entitled requester.

## Build implications

1. **Delivery mode is a first-class billing attribute** with four values including remote. Capture it per
   session; do not infer it from the patient's address.
2. **Pregnancy is an episode entity** — the 12-session cap has no calendar anchor. It needs a start, an
   expected end, an actual outcome, and the ability to span calendar years.
3. **Count caps across combined sets**, not per code or per mode.
4. **Miscarriage care is same-day-only** for its dedicated codes; the date comparison is a hard gate.
5. **Model positive cumulation allowances explicitly.** In this article the law grants rather than
   forbids, and a deny-by-default engine will under-bill.
6. **A single claim can mix key letters** (V services, K supplements). Price per line, not per claim.
7. **Expose the motivation field to two requesters** — médecin-conseil and treating physician.

## Gaps and figures to verify

- Full delivery (*accouchement*) code set and its own rules — only partially captured.
- Coefficients for `428573`, `428632` and the remaining mode variants.
- Whether the 12-per-pregnancy cap interacts with the at-risk-pregnancy codes (`422870` family), which are
  not named in the cap list.
- Postnatal care series and its caps.
- `474250-474261` — what it is, and why it excludes the listed midwifery services.
- Whether remote-treatment variants carry extra conditions (consent, technical requirements) beyond the
  code itself.

Sources: [[sources]].
