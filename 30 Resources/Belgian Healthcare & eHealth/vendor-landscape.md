---
classification: public
status: draft
updated: 2026-10-01
---

# Vendor landscape

Who already sells software into Belgian ambulatory care. Everything here is from **publicly published
lists and public positioning only** — no confidential product internals, roadmaps, customers or
unpublished commercial terms of any vendor.

## The authoritative market map is a compliance list

MyCareNet publishes, per sector and per service, the list of **approved software** (*logiciels
agréés*). For doctors it runs to more than 30 packages. That list doubles as the market map, and it has
a property no analyst report has: **it is granular per service**, so you can see which vendors have
certified which capabilities.

Services listed separately for doctors: Member Data · Chapter IV agreements · DMG · tariff consultation
· invoicing · eAttest V3 · insurability.

## Approved packages for doctors

As published on the MyCareNet list dated **30 September 2026**, for the Member Data service — the
broadest list and therefore the best proxy for "who is in this market":

| Vendor | Product(s) |
|---|---|
| AMS Solutions | Octopus 1.0 |
| Assos Care | Topaz |
| Cegeka Healthcare | Prodoc |
| CompuGroup Medical Belgium | Daktari |
| Compusoft | Clinninet |
| Corilus | CareConnect, CareProvider |
| Crossuite | Crossuite |
| CTG | EID Software |
| DC Systems | RisOnWeb |
| Dhealth | My lifeline |
| EasyToCare | Easytar |
| Euresisoft | euMedic 2.0 |
| Eyefile | Eyefile |
| Health Data Management Partners | Health One, Nova |
| MediPortal | Mediris |
| Medispring | Medispring |
| Medsoc | Sofia HealthCare |
| nexuzhealth | nexuzhealthpro |
| Offimed | Medinect |
| Rosa | Rosa |
| Samka | Medical Management System |
| Sylho Group | Doctor Manager |
| Tarimed | Medinect |
| TDM3 | TDM3 |
| Ximeo | eoRis / eoNis |
| Xperthis | OmniPro |
| ZORGI | Oazis |

Certified for **Chapter IV agreements** — a narrower and therefore more telling list: Assos Care,
Cegeka Healthcare, CompuGroup Medical, Corilus, Eyefile, Health Data Management Partners,
HealthConnect, Medicalsoft, MediPortal, Medispring, nexuzhealth, Offimed, PCSOL, TakTik, The Virtuous
Circle, Xperthis.

Note the gap between the two lists. Appearing in one does not imply the other, and the narrower lists
are a good signal of depth of institutional integration.

## How to read this market

**1. It is crowded but shallow.** Thirty-plus approved packages in a country of ~11 million is not a
market lacking suppliers. It is a market where many suppliers cleared a compliance bar. Differentiation
on "we are approved" is therefore impossible.

**2. Several distinct business shapes coexist.**

| Shape | Examples from the list | Implication |
|---|---|---|
| Independent GP-record vendors | Medispring, Health One/Nova, Daktari, Prodoc, Medinect | The direct comparison set for a GP record |
| Platform/roll-up groups | Corilus, Xperthis | Breadth across sectors, likely consolidation appetite |
| Hospital-network originated | nexuzhealth (VZN KU Leuven lineage) | Hospital-first, extending outward |
| Scheduling/front-office first | Rosa, Crossuite | Came in through agenda and patient access, not the record |
| Specialty and niche | Eyefile, RisOnWeb, Clinninet | Deep in one discipline |

The scheduling-first entrants are the interesting ones strategically: they prove that the **front office
is a viable wedge into a market whose incumbents hold the record.**

**3. The record and the practice are sold separately today.** The list is full of record systems; it is
not full of integrated practice-management-plus-record-plus-finance systems. That gap is real, and it
is the reason practices assemble a record, a separate agenda, an accountant, a social secretariat and
spreadsheets.

**4. Price floors are at zero.** Free or free-tier offerings exist in this market, and an annual
practice premium partly offsets licence cost for GPs who qualify. Published price points appear in the
Belgian medical press (young-doctor tariffs, free editions) — **verify current figures directly with
vendors or the press before relying on any of them.** The commercial consequence is that competing on
licence price is unattractive; competing on total cost including administrative time is the available
position. See [[software-homologation-and-obligations]] for the premium mechanics.

**5. Approval is per service, so entry is incremental.** A newcomer need not match an incumbent's full
certification set to be usable for a defined workflow.

## Adjacent categories

| Category | Notes |
|---|---|
| **Maisons médicales tooling** | Capitation centres have specific needs (registrations, forfait reconciliation, multidisciplinary rostering). Pricare is commonly cited for this segment *(not on the lists consulted — to verify)* |
| **Connectivity** | iCure / Cardinal, with the Free Health Connector, sits beneath several products rather than competing with them. See [[integration-architecture]] |
| **Patient-facing scheduling** | Doctena, Progenda and similar *(to verify)* — adjacent to Rosa and Crossuite |
| **Accounting and payroll** | Fiduciaries and social secretariats, typically outside any clinical product. The "orchestrate rather than rebuild" boundary |
| **Hubs and regional platforms** | CoZo, RSW, Abrumet, Vitalink are infrastructure, not competitors. See [[clinical-data-sharing-and-standards]] |

## Public claims worth knowing

- **Homologation and labelling are marketed features.** Vendors advertise being eSanté-homologated and
  INAMI-labelled, and explicitly market access to the telematics/practice premiums — confirming that
  the premium is a recognised purchase driver, not a theoretical one.
- **Platform firsts are marketed** — e.g. Medinect's public claim to be the first and only INAMI-agreed
  GP record available on iPad. Mobile-native remains differentiating enough to advertise, which is
  itself informative about incumbent UX.

## Build implications

1. **Do not differentiate on compliance.** Thirty-plus vendors have it. Compliance is the entry ticket;
   experience, integration breadth and measurable administrative savings are the product.
2. **Use the per-service lists to pick a certification sequence** that matches your wedge.
3. **The integrated practice gap is the opening**, not the record itself. The record is well supplied;
   the joins between record, agenda, billing, finance and HR are not.
4. **Front office is a proven entry point.** Rosa and Crossuite got in without owning the record.
5. **Assume consolidation pressure.** Roll-ups in the list mean both competitive response and a
   plausible exit path.
6. **Price against total cost including administrative labour**, since licence price has a zero floor.

## Gaps and figures to verify

- The full per-service approved lists (only Member Data and Chapter IV were captured).
- Market share, installed base and revenue per vendor — **no reliable public source identified**.
- Pricare's current status and position in the maisons médicales segment.
- Current pricing for each named product.
- Equivalent approved-software lists for nurses, physiotherapists and dentists, which matter for
  multidisciplinary centres.
- Which vendors are actually multidisciplinary versus single-profession.

Sources: [[sources]].
