---
classification: internal
status: confirmed by David 29 Sep 2026 (zone model); values provisional where marked
updated: 2026-09-30
---
# Athlete baseline

The source of truth for zones used in session classification. Strava's and Apple's zones are for display only.
Contains my own special-category (heart rate) data; see data-policy §4.

## Heart-rate zones, by date (Friel, % of LTHR) ⚠️ current LTHR provisional
**The only place zone values live.** Rubric, skills and scripts refer to zones by name (Z1…Z5) and read the bpm here.
Each run uses the row in effect on its date. When LTHR changes, **add a row; never edit an old one**, so past runs keep the zones that applied then.
Model: Z1 <85% · Z2 85–89% · Z3 90–94% · Z4 95–99% · Z5 ≥100% of LTHR. Columns are the upper bound (bpm) of each zone; Z5 is everything above Z4.

| effective_from | LTHR | Z1 | Z2 | Z3 | Z4 | source |
|---|---|---|---|---|---|---|
| 2025-01-01 | 166 | 140 | 148 | 156 | 165 | Race averages 2026 (see below). No earlier value known, so it's applied back to Jan 2025 as an assumption |

Checked 30 Sep 2026: Strava can't supply history. Its zones before David's manual setting (29 Sep 2026) were `MaxHeartRateFromAge` (age formula, Z4 166–179), and its run pace zones come from a single 1:40 half with no dated history.

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

## Race paces, by date: what "race effort" means on flat road
Same rule as zones: each run uses the row in effect on its date; add a row when targets change.
A tempo block on flat road = ≥15 min at or faster than the **marathon** target ([[session-types]], D29).

| effective_from | marathon | half | 10 km | 5 km | source |
|---|---|---|---|---|---|
| 2025-01-01 | 5:10/km | 4:40/km | – | – | David's own targets, stated 30 Sep 2026. Assumed to hold back to Jan 2025 |
| 2026-09-30 | 5:06/km | 4:34/km | 4:16/km | 4:03/km | Strava Performance Predictions (Progress tab), read by David 30 Sep 2026 |

**Updated monthly** from Strava Performance Predictions: a scheduled check asks David on the 1st of each month (D34). Predictions track current fitness; add a row only when a value changes.

## Shoes (terrain signal)
| Strava gear id | Type |
|---|---|
| 25832441 | Trail |
| 28636543 | Road |
| 21087212 | Road |

## Training source
- Plan: Runna (a Strava partner). Structured sessions sometimes carry their targets in the Strava description.
- Device: Apple Watch Ultra → Strava.
