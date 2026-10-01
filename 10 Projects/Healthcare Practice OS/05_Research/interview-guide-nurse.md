---
classification: internal
status: draft
updated: 2026-10-01
---

# Interview guide — home / community nurse (infirmier·ère)

60 minutes. Goal: a quantified map of the care day, the forfait scoring burden, and the inbound-message
problem.

Mechanics referenced here are verified against nomenclature article 8 — see
[[30 Resources/Belgian Healthcare & eHealth/billing-rules-and-cumulation|billing-rules-and-cumulation]]
and [[30 Resources/Belgian Healthcare & eHealth/mycarenet-services-and-flows|mycarenet-services-and-flows]].
Use them as probes, not as a lecture.

## 0 · Setup (3 min)

Consent to record and to quote. Nothing identifying leaves the notes. You are not selling.

## 1 · Context (5 min)

- Self-employed, a group, a service, or employed by a centre? How many nurses?
- Patient population: how many on a dependency forfait, how many palliative, how many act-by-act?
- Tools: record, route planning, billing, agenda. Mobile or desktop? Which one in the car?
- Do you work with *aides-soignants*? How is work split?

## 2 · Walk me through yesterday's round (15 min)

Chronological. For each patient visit: what care, what recorded, when recorded, where recorded, on what
device, and what had to be redone later at a desk.

Key probe: **when in the day does the data actually get entered?** At the bedside, in the car, or at
10pm at the kitchen table? That gap is the product opportunity and the compliance risk at once.

## 3 · The care day and visit ranking (8 min)

- How many times a day do you visit the same patient? What drives a second or third visit?
- **The 1st, 2nd and 3rd+ basic service of a care day are separate codes at the same value.** Does your
  software pick the right rank automatically, or do you? Has the rank ever been wrong?
- What counts as a "care day" when a visit crosses midnight, or when a colleague covers one of the visits?
- When two nurses see the same patient in a day, who bills what, and how do you coordinate?

## 4 · Forfait scoring — the money question (12 min)

Dependency forfaits A, B and C are granted **once per care day for all nursing care**, and which one
depends on scoring the patient on washing, dressing, transfer/mobility, toileting, continence and
eating. The coefficients differ by roughly a factor of three between A and C, so scoring *is* revenue.

- Walk me through the last time you scored a patient. What did you use, how long did it take, who
  checked it?
- How confident are you that your scores are right? Have you ever been audited or corrected?
- What happens when a patient's dependency changes — who notices, how fast is it re-scored, and how long
  before the forfait changes?
- Do you ever suspect you are **under**-scoring? *(Listen hard. Under-billing is invisible and therefore
  rarely raised, which makes it a strong wedge.)*
- Palliative patients have their own forfait set requiring both dependency criteria and the palliative
  definition. How does a patient get onto that, and how long does it take?
- The specific-technical-acts forfait (perfusions, parenteral nutrition) — when does that apply instead,
  and who decides?

## 5 · Agreements and inbound messages (8 min)

This is the part most software handles badly.

- To get a forfait you notify the fund and the médecin-conseil decides. Walk me through the last
  request: what you sent, how long you waited, how you learned the answer.
- **Funds send you unsolicited messages** — a médecin-conseil's decision after a visit, a closure
  because the patient moved to another provider, a rectification. *How do you find out?* Email, post, a
  screen in your software, a colleague?
- Have you ever **missed** one? What was the consequence?
- Who is responsible for noticing these when you are on holiday?

Listen for: whether these arrive as a real inbox with escalation, or as a list nobody opens. The
specification actually obliges software to ensure the nurse receives them — so if they are being missed,
the current tool is failing a stated requirement.

## 6 · Delegation and the record as evidence (5 min)

- For care partly performed by an *aide-soignant*: how is that recorded?
- **Reimbursement can depend on the nursing file showing that each part was done by someone competent
  for it.** Does your record capture who did which part, or just that the care happened?
- Has a claim ever been refused over this?

## 7 · Place of care traps (4 min)

- Do you ever provide care in a hospital or its consultation service? *(Article 8 cannot be used there,
  and perfusions specifically cannot — has that ever caught you out?)*
- Rest homes, temporary addresses, patients staying with family — does the billing change? Who works
  that out?

## 8 · Getting paid, and quantifying (8 min)

- Insurability checks: when, how, and what happens when someone is not in order?
- Rejections: walk me through the last one — cause, time to fix, money delayed.
- End of month: what do you reconcile and for how long?
- **How many hours a week is administration?** What would you do with that time?
- What have you tried that failed?
- Who decides about software? Anything I should have asked?

## Hypotheses to kill or confirm

| # | Hypothesis | Verdict |
|---|---|---|
| H1 | Data is entered hours after care, from memory | |
| H2 | Forfait scoring is under-claimed, not over-claimed | |
| H3 | Fund-initiated messages are routinely missed | |
| H4 | Re-scoring after a dependency change lags by weeks | |
| H5 | Delegation to care assistants is recorded too thinly to defend a claim | |
| H6 | Mobile is where the work is, desktop is where the admin is, and nothing bridges them | |
