---
classification: public
status: draft
updated: 2026-10-01
---

# Billing rules — laboratory, imaging and pathology

**Governing texts:** art. 17 (radiodiagnostic, specialist) · 17bis (échographies) · 17ter
(radiodiagnostic, non-specialist) · 17quater (échographies, non-specialist) · 18 (radiotherapy and
nuclear medicine) · 19 (radiotherapy application rules) · 24 and 24bis (biologie clinique) · 32
(anatomo-pathologie) · 33 / 33bis / 33ter (examens génétiques).
**Key letters: B and F** (clinical biology, in-vitro nuclear medicine), **K** (imaging and other
technical), **Q** (accreditation supplement).

Rule semantics: [[billing-engine-rule-model]].

## The one rule unique to this domain

For **clinical biology, anatomical pathology and in-vitro nuclear medicine**, the ambulatory-vs-hospitalised
code choice is determined **by the moment the prescription was established**, not by the patient's status
when the analysis is performed. Everywhere else in the nomenclature it is the moment of delivery.

Consequences, from the article 25 interpretative rules:

- Hospitalised status is deemed to begin at the **admission date and time shown on the hospitalisation
  notification document**.
- Analyses prescribed for a patient presenting urgently **may** use ambulatory numbers, provided the
  **results are known before admission and contributed to the admission decision**. This must **not** be a
  systematic procedure for patients whose condition plainly requires admission.
- If a patient is admitted, examined, then transferred to another hospital, the first hospital's analyses
  must use **hospitalised** codes.

This is the clearest case in the corpus where a billing attribute depends on a clinical judgement that
must be captured and justified at the time.

## Clinical biology (art. 24) — a constraint-satisfaction problem

Article 24 is the densest rule article in the nomenclature: **134 cumulation prohibitions**. Its
application rules are numbered and take two machine-ready shapes.

### Set cardinality — "at most N of this set"

| Rule |
|---|
| *"Au maximum trois des prestations `540013-540024`, `541693-541704`, `541715-541726`, `541774-541785`, `542172-542183`, `542334-542345` et `542356-542360` peuvent être portées en compte."* |
| *"Au maximum deux des prestations `541052-541063`, `541074-541085`, `541096-541100` et `541111-541122` peuvent être portées en compte à l'AMI."* |
| *"Au maximum 2 des prestations `547396-547400`, `547890-547901` et …"* |
| *"Au maximum deux des prestations `434313-434324`, `434335-434346`, …"* |

### Mutual exclusivity within a set

| Rule |
|---|
| `541531-541542`, `542113-542124`, `542135-542146` *"ne sont pas cumulables entre elles"* |
| `544154-544165`, `544176-544180`, `544191-544202`, `544272-544283` *"ne sont pas cumulables entre elles"* |
| `125156-125160`, `125171-125182`, `125193-125204` not cumulable with `125053-125064` and `125510-125521` |

These two shapes — `max_n_of(set)` and `mutually_exclusive(set)` — cover most of article 24 and are
directly encodable. A lab-billing engine is essentially a solver over a few hundred such constraints.

### Consultation exclusion

Article 24 §5 with article 1 §6: a **biologist's consultation** may not be cumulated with clinical-biology
services. But article 1 RI 02: a physician recognised in **both** internal medicine **and** clinical
biology may bill consultation `102034` **plus** biology acts, provided the consultation meets the
nomenclature's criterion. When acting as a biologist on analyses requested by other physicians, that same
doctor may **not** attest a consultation — only the analyses.

## Imaging (art. 17 and relatives)

| Rule | Source |
|---|---|
| Radiodiagnostic fees may **never** be cumulated with fees for a **practice consultation** (art. 17 §2). The radiologist's consultation is reimbursable **only** where it is unrelated to any radiodiagnostic act — whether that act precedes, accompanies or follows it (art. 2 RI 07) | art. 17 §2 |
| `459535-459546` reimbursable **only once per year** | art. 17 |
| A fee *"n'est payable qu'une fois par prescription quel que soit le nombre de prestations pratiquées"* — **once per prescription**, however many services the radiologist performs in response | art. 17 |
| A fee *"payable au maximum une fois par 24 heures"* — once per **rolling 24 hours**, not per calendar day | art. 17 |
| `450354-450365` not cumulable the same day with `460972`, **unless** those forfait fees are due for another service | art. 17 |

Two cap scopes here appear nowhere else and break naive counters: **per prescription** and **per rolling
24 hours**.

The **specialist vs non-specialist split** is structural: articles 17 and 17bis are for recognised
radiodiagnostic specialists; 17ter and 17quater provide parallel series for non-specialists. The
qualification gate selects the article, not merely the code.

## Radiotherapy and nuclear medicine (art. 18–19)

Article 19 carries the application rules, including planning preconditions — e.g. services are conditional
*"pour autant que le planning visé sous le numéro d'ordre 444393-… "* be present, and contact therapies are
treated as an exception to a general rule. Article 19 also governs where services may be performed.

*(Articles 18 and 19 were retrieved and mined for density but not enumerated here — see gaps.)*

## Build implications

1. **Implement the prescription-time status rule** for biology, pathology and in-vitro nuclear medicine as
   a separate code-selection path from everything else.
2. **Capture the admission timestamp from the hospitalisation notification document** as the authoritative
   boundary, not a derived or clinical value.
3. **Make the "contributed to the admission decision" exception an explicit, justified, audited flag**,
   with monitoring for systematic use — the text expressly forbids making it routine.
4. **Model article 24 as a constraint solver**, not as per-code validation: `max_n_of(set)` and
   `mutually_exclusive(set)` over code sets, evaluated across the whole requisition.
5. **Add cap scopes for *per prescription* and *per rolling 24 hours*.** Both are time- or
   document-anchored rather than calendar-anchored.
6. **Let qualification select the article** (17/17bis vs 17ter/17quater), then the code.
7. **Block radiology consultation plus radiology act by default**, with a narrow, justified override for
   the genuinely unrelated consultation.

## Gaps and figures to verify

- The **complete numbered application-rule list of article 24** — only samples captured. This is the
  single largest remaining extraction job in the nomenclature, and the highest value for a lab engine.
- Articles 18, 19, 24bis, 32, 33, 33bis, 33ter: retrieved but not enumerated.
- The **Q accreditation supplement** conditions and amounts for accredited pharmacist-biologists and
  accredited science graduates.
- Which specific fee is the "once per prescription" and "once per 24 hours" one — the code was not captured
  with the rule.
- Whether article 24's rules are published anywhere in machine-readable form.

Sources: [[sources]].
