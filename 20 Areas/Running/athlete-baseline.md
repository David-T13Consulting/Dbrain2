---
classification: internal
status: confirmed by David 29 Sep 2026 (zone model); values provisional where marked
updated: 2026-09-29
---
# Athlete baseline

The source of truth for zones used in session classification. Strava's and Apple's zones are for display only.
Contains my own special-category (heart rate) data; see data-policy §4.

## Heart rate: threshold-based (Friel), LTHR = 166 bpm ⚠️ provisional
| Zone | bpm | % LTHR |
|---|---|---|
| Z1 recovery | ≤140 | <85% |
| Z2 aerobic | 141–148 | 85–89% |
| Z3 tempo | 149–156 | 90–94% |
| Z4 sub-threshold | 157–165 | 95–99% |
| Z5 threshold+ | ≥166 | ≥100% |

- **Where LTHR 166 comes from:** race averages. Jogging de Namur 10k (13 Sep 2026): 46 min, avg 167. 20km de Bruxelles (May 2026): 96 min, avg 163. 5 mile TT (Jan 2026): 38 min, avg 164.
- **To do:** re-test with a 30-minute solo all-out effort (LTHR = average of the last 20 min). Re-check against the golden dataset at T3.1.
- **Resting HR:** 49 (Apple Watch, Sep 2026).
- **Max HR: unconfirmed.** Highest reliable reading is 175 (race finish). Apple shows 182, probably age-derived. The 179 in the 18 Aug warm-up is an optical artifact.
- Wrist optical HR (Apple Watch Ultra): expect spikes at the start of runs and lag on short reps.

## Pace zones (road), from a 1:40 half marathon
| Zone | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| min/km | >5:50 | 5:50–5:01 | 5:01–4:31 | 4:31–4:13 | 4:13–3:58 | <3:58 |

Pace isn't used for intent on trail or mountain terrain. Use HR there.

## Shoes (terrain signal)
| Strava gear id | Type |
|---|---|
| 25832441 | Trail |
| 28636543 | Road |
| 21087212 | Road |

## Training source
- Plan: Runna (a Strava partner). Structured sessions sometimes carry their targets in the Strava description.
- Device: Apple Watch Ultra → Strava.
