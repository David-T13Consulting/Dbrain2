---
classification: public
status: draft
updated: 2026-10-01
---

# Sources

Everything in this knowledge base traces to a source listed here. All web sources retrieved
**1 October 2026**; this domain changes at least annually, so treat figures as "as at that date".

**Reliability convention used across the pages:**

| Tier | Meaning |
|---|---|
| **Primary** | The institution that owns the fact: INAMI, the eHealth platform, NIC/CIN (MyCareNet), official journals |
| **Secondary** | Medical press, unions, federations, vendor documentation. Useful, often clearer, not authoritative |
| **General knowledge** | Stated from background knowledge, flagged *(to verify)* inline. Not sourced in this pass |

## Primary — eHealth platform

| Source | URL | Used for |
|---|---|---|
| eHealth portal home | `https://www.ehealth.fgov.be/fr` | Mission, action plan 2026–2029, EHDS, Be-SafeShare, ProSanté |
| Basic services index | `https://www.ehealth.fgov.be/ehealthplatform/fr/services-de-base` | The eleven basic services |
| I.AM | `https://www.ehealth.fgov.be/ehealthplatform/fr/gestion-integree-des-utilisateurs-et-des-acces-iam` | Authentication means, generic authorisation model, professional-registry check |
| End-to-end encryption | `https://www.ehealth.fgov.be/ehealthplatform/fr/systeme-de-cryptage-end-to-end` | ETKDepot vs KGSS, uses in eHealthBox and Recip-e |
| Reference directory (Metahub) | `https://www.ehealth.fgov.be/ehealthplatform/fr/repertoire-des-references` | Metahub role, who may access, relation to Consent/Therlink/Exclusions |
| **eHealth API portal** | `https://portal.api.ehealth.fgov.be/` | The full API catalogue, protocols, versions, FHIR R4 identification |
| Service status | `https://status.ehealth.fgov.be/` | Operational monitoring; hubs/metahub procedure pages |
| KMEHR standards | `https://www.ehealth.fgov.be/standards/kmehr/en/` | KMEHR as XML schema + reference tables + transactions |
| Therapeutic links news (2026) | `https://www.ehealth.fgov.be/nl/news/2026/ehealth-therapeutic-links-meer-informatie-over-de-totstandkoming-van-de-therapeutische-relaties-en-het-gebruik-van-de-identiteitskaart` | Creation of therapeutic relationships, duration, eID use |

## Primary — INAMI / RIZIV

| Source | URL | Used for |
|---|---|---|
| INAMI home | `https://www.inami.fgov.be/fr` | Role, sections, web programmes |
| Nomenclature | `https://www.inami.fgov.be/fr/nomenclature` | Structure, NomenSoft, publication channels, downloads, no public API |
| NomenSoft search | `https://webappsa.riziv-inami.fgov.be/Nomen/fr/search` | Code and tariff lookup |
| **Software vendors** | `https://www.inami.fgov.be/fr/professionnels/autres-professionnels/fournisseurs-de-logiciels` | Check digits (mod 97/83/79 + new 89), document justificatif, rounding, diabetes code changes, Recip-e v4, contacts |
| eHealth technical info & registration for vendors | `https://www.inami.fgov.be/fr/themes/esante/informations-techniques-et-enregistrement-pour-les-fournisseurs-de-logiciels-destines-aux-dispensateurs-de-soins` | SAMv2, VIDIS, PSS antimicrobiens, eReferral, integration modes, test sessions |
| eReferral for home nurses | `…/fournisseurs-de-logiciels-prescription-de-renvoi-electronique-pour-les-infirmiers-a-domicile-ereferral` | FHIR test server, 2026 test windows, Smals GitHub |
| Action plan 2026–2029 | `https://www.inami.fgov.be/fr/themes/esante/plan-d-action-interfederal-esante-2026-2029` | Three axes, BIHR, governance |
| Prime de pratique intégrée | `https://www.inami.fgov.be/fr/professionnels/professionnels-de-la-sante/medecins/interventions-financieres/prime-de-pratique-integree` | 2025 amounts, eligibility, application window, payment route |
| Premium conditions detail | `…/prime-de-pratique-integree/description-des-conditions-de-la-prime-de-pratique-integree-en-medecine-generale` | Parameter conditions |
| Maisons médicales | `https://www.inami.fgov.be/fr/professionnels/etablissements-et-services-de-soins/maisons-medicales` | Capitation arrangement |
| Forfait agreements with OAs | `…/maisons-medicales/conclure-un-accord-de-paiement-forfaitaire-avec-les-o-a` | Agreement mechanics |
| Patient registration | `https://webappsa.riziv-inami.fgov.be/Nomen/fr/409614/pdf/53931` | Registration of the beneficiary |
| DMG management | `https://www.inami.fgov.be/fr/professionnels/professionnels-de-la-sante/medecins/qualite-des-soins/gerer-le-dossier-medical-global-dmg-de-votre-patient` | DMG / eDMG |
| Mandatory electronic prescription | `…/medicaments/prescrire-un-medicament/obligation-de-prescrire-les-medicaments-de-facon-electronique` | E-prescription obligation |

## Primary — nomenclature articles and interpretative rules

Retrieved and read in full as PDFs on 1 October 2026. These are the basis of
[[billing-rules-and-cumulation]]. Index page: `https://www.inami.fgov.be/fr/nomenclature/nomenclature-textes`
(stated as updated through the *Moniteur belge* of 31 July 2026).

| Article | Subject | Version read | URL |
|---|---|---|---|
| **1** — interpretative rules | General rules (aesthetic interventions, biologist cumulation) | M.B. 13.3.2002 | `…/SiteCollectionDocuments/nomenclatureart01_interpretation.pdf` |
| **2** — text | Consultations, visits, opinions, psychotherapy | in force 1.3.2022 | `…/SiteCollectionDocuments/nomenclatureart02_20220301_20220301_02.pdf` |
| **2** — interpretative rules | 19 pages of Q&A: home vs practice, night visits, specialist home visits, *avis* cumulation | M.B. 22.4.2026 | `…/SiteCollectionDocuments/nomenclatureart02_interpretation.pdf` |
| **7** — text | **Physiotherapy** — session codes, second-session-of-day rules §§11–12, cerebral palsy, lymphoedema caps | in force since 1.5.2014 + Erratum M.B. 14.5.2014 | `…/SiteCollectionDocuments/nomenclature-art07.pdf` |
| **7** — interpretative rules | Physiotherapy Q&A | — | `…/SiteCollectionDocuments/nomenclatureart07_interpretation.pdf` |
| **8** — text | **Nursing** — basic services by rank in the care day, forfaits A/B/C, palliative PA/PB/PC/PP, specific technical acts | in force 1.9.2026 | `…/SiteCollectionDocuments/nomenclatureart08_20260901_01.pdf` |
| **8** — interpretative rules | Emergency-care exclusion; *aide-soignant* delegation | M.B. 24.9.2025 | `…/SiteCollectionDocuments/nomenclatureart08_interpretation.pdf` |
| **15** — interpretative rules | Surgery: the 100%/50% distinct-operative-field rule, K120/N200/I200 hospital threshold | M.B. 24.6.2003 | `…/SiteCollectionDocuments/nomenclatureart15_interpretation.pdf` |

All paths are relative to `https://www.inami.fgov.be`.

### Full corpus retrieval (1 October 2026)

A second pass retrieved the **complete nomenclature**: all **63 article texts** and **45 interpretative-rule
documents**, totalling ~4.9 million characters, then mined for rule-bearing language. This is the basis of
[[nomenclature-map]], [[billing-engine-rule-model]] and the eight per-profession pages.

| Resource | URL pattern |
|---|---|
| Article index | `/fr/nomenclature/nomenclature-textes` |
| Article page (per article) | `/fr/nomenclature/nomenclature-textes/nomenclature-article-<n>` — where `<n>` is `1`…`37`, `14-a`…`14-n`, `17bis`, `17ter`, `17quater`, `24bis`, `27-1`, `28-ss-1-7`, `28-ss-8`, `28-1`, `29-1`, `33bis`, `33ter`, `35bis` |
| Article text PDF | `/SiteCollectionDocuments/nomenclatureart<NN>_<YYYYMMDD>_<nn>.pdf` — **the current version is the link with a single date**; historical versions carry a second (end) date, and `_portee` files are scope documents |
| Interpretative rules PDF | `/SiteCollectionDocuments/nomenclatureart<NN>_interpretation.pdf` — a stable, guessable pattern |

**Current versions confirmed read** include art. 1 (1.11.2025), 2 (1.7.2026), **7 (1.7.2026)**,
**8 (1.9.2026)**, 9 (1.7.2026), 5/6 (1.6.2026), 17 (1.7.2026), 20 (1.9.2026), 24 (1.9.2026),
26 (1.9.2026), 28/1 (1.7.2026), 30 (1.5.2024), 31 (1.8.2026), **36 (1.9.2026)**, **37 (1.9.2026)**.

**Six articles could not be retrieved in a current version** — the article page offered no open-ended
PDF, so a dated one was taken: **27, 28 §1–7, 28 §8, 29, 35, 35bis**, some dating from **2012–2014**.
Anything drawn from these is flagged in [[billing-rules-devices-and-aids]] and must be re-checked.

**Correction made during this pass.** An earlier draft cited physiotherapy `560011` as the lead 30-minute
session code, from the text in force since 2014. The current 1 July 2026 text leads with a **`567xxx`
series** (including a new intake code at the first session of a treatment) and retains `560011` as a
§10-limited fallback. Both affected pages were corrected. The lesson is recorded in
[[billing-engine-rule-model]]: reference data needs effective dates, and so does the rule set.

### Mining method

Rule-bearing sentences were extracted by pattern across the whole corpus — cumulation prohibitions and
allowances, frequency caps, minimum intervals, age conditions, médecin-conseil agreement, prescription
requirements, reductions, supplements, time-of-day and operative-field language — then counted per article
to locate complexity, and read in context before being written up. Counts appear in [[nomenclature-map]].
**648 numbered *règles interprétatives*** exist across the 45 interpretative documents.

Derived artefacts (extracted text, per-article rule counts) were kept in the session scratchpad and are
**not** in the vault: they are reproducible from the URL patterns above, and the vault's large-file rule
applies.

Secondary, used only for orientation and explicitly flagged in the page: INAMI/Le Spécialiste coverage
of urgent-visit supplements and the consultation/vaccination cumulation reminder; Medi-Sphere on
teleconsultation codes. **Caution:** general web searches on "cumulation rules" surface a large volume
of **French (France)** material — ameli.fr, l-idel.fr, omniprat.org, appines.fr — which does **not**
apply in Belgium. Nothing from those sources was used.

## Primary — MyCareNet (NIC / CIN)

| Source | URL | Used for |
|---|---|---|
| MyCareNet home | `https://fra.mycarenet.be` | Service catalogue, sector list |
| Services for doctors | `https://fra.mycarenet.be/services-par-secteur/médecins` | Doctor-facing services |
| **Approved software, doctors** | `https://fra.mycarenet.be/services-par-secteur/médecins/logiciels-agréés-médecins` | The vendor list (page dated 30 Sep 2026) |
| eAttest | `https://fra.mycarenet.be/services-généraux/eattest` | Flow, synchronicity, rollout dates, 1 Sep 2025 obligation, paper fallback |
| Invoicing presentation | `…/facturation-tiers-payant/présentation-service-facturation` | INAMI layout, record types 10–90, 5% threshold |
| **Invoicing flow** | `…/facturation-tiers-payant/flux-service-facturation` | `920000`, `931000`, `920999`, `920098`, `920099`, `920900` |
| Insurability flow | `…/assurabilité/flux-service-assurabilité` | `801000`/`801900`, synchronous, flat vs XML |

## Primary — legal

| Source | URL | Used for |
|---|---|---|
| Quality Law, 22 April 2019 | `https://www.ejustice.just.fgov.be/eli/loi/2019/04/22/2019041141/justel` | Art. 33 record contents, art. 35 retention |
| Patient rights brochure | `https://www.health.belgium.be/sites/default/files/media/files/2025-11/brochure_droits_des_patients_16-01-2025.pdf` | Patient rights (2002 law) |
| APD note on patient-record data | `https://www.autoriteprotectiondonnees.be/publications/note-sur-le-traitement-de-donnees-provenant-de-dossiers-de-patients.pdf` | Processing data from patient records |

## Secondary

| Source | Used for | Caution |
|---|---|---|
| iCure / Taktik FHC documentation and repos — `github.com/taktik/freehealth-connector`, `github.com/icure/freehealth-connector`, `icure.gitbook.io/icure/interoperability/freehealth-connector`, `icure.com` | FHC capabilities, AGPL-3.0, MMU, protocol translation, 22 e-services claim | Vendor's own claims about its product |
| Recip-e — `https://recip-e.be/fr/documentation/`, `https://recip-e.be/fr/prestataire-de-soins-de-sante-prescripteur/` | v4 connector, documentation and registration route | — |
| CM / Mutualité chrétienne — `https://www.cm.be/en/careproviders/doctors/patient-data`, `https://www.mc.be/b2b/prestataires/outils-electroniques/recip-e` | Hubs, metahub federation, Recip-e | A fund's explainer |
| Abrumet / Brussels Health Network — `brusselshealthnetwork.be` | Brussels hub, COCOM designation, ePrescription FAQ | — |
| Vitalink — `https://www.vitalink.be/uw-gegevens-raadplegen` | Flemish vault | — |
| CoZo — `https://www.cozo.be/ehealth` | Flemish hub | — |
| Agoria — `https://www.agoria.be/en/themes/industry-clusters/healthtech/belgian-ehealth-ecosystem-tests-international-standard-hl7-fhir` | FHIR as 2019 roadmap priority; Belgian profiling stage 1 resource list | Industry federation |
| Maison Médicale Couleurs Santé — `https://couleurssante.be/comment-ca-marche/` | Worked forfait example, Feb 2026, per-discipline amounts | One centre's published figures |
| Fédération des maisons médicales — `maisonmedicale.org` | Capitation history and calculation | Advocacy body |
| ABSyM/BVAS, GBO, Medi-Sphere, Le Spécialiste, ZORGI blog | Premium conditions and parameters in plain language; DMG rules | Unions, press and a vendor |
| Ordomedic — `ordomedic.be` | Quality Law deontological difficulties | — |
| Wikipedia / CEUR / arXiv on KMEHR | KMEHR history, Sumehr labelling since 2005, KMEHR→FHIR transformation | Academic/encyclopaedic |
| ict-reuse.be — Therlink integration | Consent/TherLink/TherExclusion as REST services | Government reuse catalogue |
| MDR/AI Act commentary (tandemhealth.ai, hlc.com, zechmeister-solutions.com, NCBI PMC11607523) | SaMD qualification, MDR↔AI Act simultaneity, MDCG guidance, new AI Act obligations | Law firms and vendors. **Not legal advice** |

## Local specification archive — pointer note

Per the large-files rule (vault rule 5 / `90 System/README.md`), these stay **outside the vault and
ungit-tracked**. They are official NIC/CIN message brochures — published specifications, not
confidential material.

**Path:** `~/Downloads/Energy & Home/` — in three subfolders. *(Filed under an unrelated folder name;
worth relocating to something findable, after which this pointer must be updated.)*

| File | Version / date | Contents |
|---|---|---|
| `forfait ABC/410000 - message forfait - v02r02 - 20170309.pdf` | v02 R02, 2017 | New request or closure of home-nursing forfait A/B/C/toilette; full zone layout, paired error zones |
| `forfait ABC/4109xx - message reponse forfait - v02r01.pdf` | v02 R01 | Fund responses `410900` (agreement) / `410999` (refusal) |
| `forfait ABC/410908 - message visite mc cloture accord - v02r01.pdf` | v02 R01, 2014 | Advising-physician decision after a visit, agreement closure, rectification. Fund-initiated. States the software must ensure the nurse receives these |
| `soins palliatifs/420000 - message palliatif - (v01r02).pdf` | v01 R02, 2012 | Notification of a palliative-care request |
| `soins palliatifs/4209xx - reponse oa - message palliatif - (v01r01).pdf` | v01 R01 | Fund responses `420900` / `420999` |
| `techniques spécifiques/430000 - message PTS - v01r08.pdf` | v01 R08, 2023-03 | Specific technical services: new request, extension, additional wound care |
| `techniques spécifiques/891000 - accuse de reception - v01r00.pdf` | v01 R00, 2009 | Generic acknowledgement; full segment-300 zone layout |

These supplied the **flat-file anatomy** in [[mycarenet-services-and-flows]]: the segment 100/200/300
structure, the 1024-vs-901 character asymmetry, the zone-level field definitions, the paired error
zones, and the flat-file-or-XSD choice.

**Caveat carried through to every page using them:** versions range from 2009 to 2023. The structural
patterns are almost certainly still valid; **specific zone positions and lengths must be re-checked
against current NIC/CIN documentation before any implementation.**

## Scope note on David's own material

David's own notes on a healthcare venture (an Odoo-based practice system) are held outside the vault
and were used **only to scope this knowledge base** — to decide which domain topics a builder needs.
No venture strategy, positioning, pricing, targets or contract terms were carried into these pages, by
agreement and per `data-policy.md` §2.1 and §6.

One figure reached these pages through that route and is flagged accordingly: **≈250 maisons médicales
with >600,000 registered patients (2023)**, which his notes attribute to Prospective Jeunesse. It is
recorded as secondary and unverified in [[reimbursement-and-financial-flows]].

## Known coverage gaps

Collected from the *Gaps and figures to verify* sections across the pages. The largest:

1. **No zone-level detail for `801000`/`801900` or the `920000` record types 10–90** — the two most
   commercially important message families.
2. **Onboarding and environment specifics** for the eHealth platform (ACC/PROD, prerequisites, SLAs).
3. **Current versions** of all MyCareNet message layouts.
4. **Terminology landscape** (SNOMED CT, ICPC-2, ICD-10-BE, LOINC, ATC, CNK) — entirely unverified.
5. **Market sizing per vendor** — no reliable public source identified.
6. **Therapeutic-link durations** by type.
7. **The 7th vs 8th premium parameter** distinction for medical-home GPs.
8. **Legal basis mapping** under GDPR for each processing purpose.
9. **Key-letter monetary values** — the conversion mechanism is confirmed (art. 1 §3: a conventionally
   fixed euro value per letter) but the values themselves were not retrieved.
10. **Article 24's complete numbered application-rule list** — the single largest remaining extraction
   job, and the highest value for a laboratory billing engine.
11. **Current versions of articles 27, 28 §1–7, 28 §8, 29, 35, 35bis.**
12. **Coefficients for article 36 (speech therapy) R-letter codes** — rules captured, values not.
