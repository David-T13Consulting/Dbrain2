---
classification: public
status: draft
updated: 2026-10-01
---

# Billing rules — physiotherapy

**Governing texts:** art. 7 (kinésithérapie), **current version read: in force 1 July 2026**. **Key letter: M.** Related but distinct: art. 22 (*physiothérapie* —
physical-medicine services performed by physicians) and art. 23 (its application rules).

> **Do not conflate article 7 with articles 22–23.** Article 7 is physiotherapists (key letter M).
> Articles 22–23 are physical medicine performed by physicians. Article 23 forbids cumulating article 22 II
> services the same day with physiotherapy services.

Rule semantics: [[billing-engine-rule-model]].

## Code selection

Four determinants, all of which change the code for the same clinical act:

| Determinant | Variants |
|---|---|
| **Setting** | Practice **outside** a hospital · practice **inside** a hospital · practice in an **organised medical service** · the **patient's home** |
| **Duration** | Average personal input of 15 / 20 / 30 minutes — art. 23: the code corresponds to the *effective* duration |
| **Rank in the day** | First session vs **second session of the day** (own codes, §§11 and 12) |
| **Pathology category** | Ordinary pathology, restricted lists, lymphoedema, cerebral palsy |

Worked coefficients (practice outside hospital unless noted):

| Code | Service | Coefficient |
|---|---|---|
| `567011` / `567055` | Individual session, average personal input **30 minutes** — the lead session codes in the current text | **M 24** |
| `567033` / `567070` | **Intake of the patient at the 1st session of a treatment** | M 6 |
| `560011` | Individual session, 30 minutes — **fallback when `567011` cannot be attested** given the §10 limitations | M 24 |
| `561352` | Individual session, 20 minutes | M 16 |
| `560523` | Individual session, 15 minutes | M 12 |
| `560696` / `561396` | Individual session 15 min — **2nd session of the day**, per §11 | **M 12** |
| `561433` / `561455` / `561470` | Individual session 15 min — **2nd session of the day**, per §12, practice outside hospital / in hospital / in organised medical service | M 12 |
| `560092` | Examination by the physiotherapist, consultative | M 24 |
| `561411` | Written report | M 14,5 |
| `639332`… | Manual lymphatic drainage | M 48 |
| `639494`… | Lymphatic drainage, exceptional cases | M 96 |

**M 24 → M 12 is half**, but for a session specified at 15 rather than 30 minutes. It is a shorter
service, not a penalty.

The current (1.7.2026) text introduces a **`567xxx` series** alongside the retained `560xxx`/`561xxx`
codes, including a distinct **intake code at the first session of a treatment**. A billing engine built
on an older text will select the wrong lead code — another reason reference data needs effective dates.

## The second session of the day (§§11–12)

The single most operationally loaded rule in the article:

1. Unless the nomenclature or the médecin-conseil provides otherwise, a second session **may** be
   attested the same day.
2. It **may only be charged if performed at least 3 hours after the previous one**.
3. It is justifiable **only if indispensable to the beneficiary's state of health**.
4. The **motivation must be kept available to the médecin-conseil and must appear in the patient's file**.
5. The médecin-conseil **may intervene at any time and refuse reimbursement** if unjustified, notifying a
   motivated decision to the beneficiary with a copy to the physiotherapist, **taking effect at the latest
   the day after notification**.

*(§§11 and 12 both govern a second daily session and map to different code series; what exactly
distinguishes them — to verify.)*

## Restricted code sets

### Cerebral palsy — `560755, 560873, 560991, 561116, 561212, 564476, 561304`

- Beneficiaries **under 21** whose cerebral motor impairment **began before their 7th birthday**.
- Proof by **medical report**, held available to the médecin-conseil and **referenced in the patient file**.
- Attestable **once per day**.
- **Not cumulable the same day** with other art. 7 §1 services — **except** the "written report" codes
  (`560711, 560836, 560954, 561072, 561190, 564454, 561411`), with which cumulation **is** allowed.

### Lymphoedema

- `639332, 639354, 639376, 639391, 639413, 639796, 639446, 639450, 639461, 639472`: max **120 per calendar
  year, once per day** (M 48).
- `639494, 639516, 639531, 639553, 639575, 639811, 639601, 639612, 639623, 639634` (M 96): for
  **exceptional pathological situations with perimetry showing a >30% difference versus the contralateral
  limb**, max 120 per calendar year, once per day.
- **Combined across both sets, the total may not exceed 120 sessions per calendar year** — a naive
  per-code counter will over-allow.
- Proof of the diagnostic, perimetric, volumetric or lymphoscintigraphic access criteria must be held for
  the médecin-conseil.

## Physical medicine by physicians (art. 22–23) — for contrast

| Rule | Source |
|---|---|
| Art. 22 II services **not cumulable the same day** with physiotherapy services | art. 23 |
| Art. 22 II b) fees not cumulable with specialist consultation fees for specialists with access, **save enumerated exceptions** | art. 23 |
| `558095-558106`, `558132-558143`: max **60 times, over a maximum of six months** | art. 23 |
| `558434-558445`: max **104 times per insured**, only **after** the rehabilitation series `558810-558821`, `558014-558025`, `558832-558843` or `558994`, **for the same pathological situation** | art. 23 |
| Series `558994`: attestable **only once per insured** | art. 23 |
| Multidisciplinary treatment: the treating physician sends the médecin-conseil a standard notification with the **affection code from a limitative list** and the start date | art. 23 |
| A **register per calendar year** must be available to the médecin-conseil, the SECM medical inspector and peer-review bodies | art. 23 |
| Vertebral pathology in socio-professional reintegration requires the **médecin-conseil's agreement** | art. 23 |

## Build implications

1. **Setting is part of the billing key.** Four code series for one clinical act; a therapist working
   across a practice and home visits needs setting captured per session.
2. **Record actual session start and end times.** The 3-hour test and the duration-determined code both
   depend on measured, not scheduled, time.
3. **Capture the second-session justification at the point of care**, in a structured field, and store it
   in the patient record — it is a payment condition and it is revocable.
4. **Model the médecin-conseil's refusal as an inbound event** with an effective date (day after
   notification) that reverses expected revenue.
5. **Implement combined-set annual caps** for lymphoedema, not per-code counters.
6. **Encode the cerebral-palsy exception precisely**: cumulation forbidden *except* written reports.
7. **Keep art. 7 and art. 22 strictly separate**, and implement the cross-article same-day exclusion.
8. **Sequencing preconditions exist** (art. 23's "only after this series, same pathology") — your engine
   needs treatment-episode history, not just a counter.

## Gaps and figures to verify

- What distinguishes §11 from §12 for the second daily session.
- Full enumeration of art. 7 §1 categories and the restricted pathology lists (F/E lists), including
  session allowances per category and the agreement regime for each.
- The full `567xxx` series (at least 20 codes observed) and how it maps onto the retained
  `560xxx`/`561xxx` codes by setting.
- The §10 limitations that make `560011` apply instead of `567011`.
- Art. 22's own service list, not enumerated here.

Sources: [[sources]].
