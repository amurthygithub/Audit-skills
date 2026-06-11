---
uc_id: UC-02
title: "Cloud vendor LI-SaaS readiness — an all-Low FIPS 199 categorization plus SaaS delivery makes the offering LI-SaaS (Tailored) eligible, selecting the 156-control baseline split 66 3PAO-tested + 90 CSP-attested; Moderate+SaaS would NOT be LI-SaaS"
industries: [saas-technology]
frameworks: [FedRAMP-Rev5, FedRAMP-Authorization-Act-2022, OMB-M-24-15, NIST-SP-800-53r5]
inputs:
  system: "Beacon Forms (low-impact SaaS) — Beacon Software, LLC; readiness assessment / FedRAMP Ready (data/seeds/uc-02-input.json)"
  fips199: "per-objective FIPS 199 impact — confidentiality Low, integrity Low, availability Low (data/seeds/uc-02-input.json)"
  saas_delivery: "true — the offering is delivered as SaaS (data/seeds/uc-02-input.json)"
procedure:
  - "chunks/02-impact-levels-and-baselines.md — Categorize: the FIPS 199 overall impact is the high-water mark = max(C, I, A) [FIPS-199 §categorization]; all-Low -> overall Low."
  - "chunks/02-impact-levels-and-baselines.md — Determine LI-SaaS (Tailored) eligibility: eligible iff overall impact == Low AND saas_delivery == true [FEDRAMP-REV5-BASELINES §li-saas]."
  - "chunks/02-impact-levels-and-baselines.md — If eligible, select the LI-SaaS Tailored baseline: 156 controls split 66 3PAO-tested + 90 CSP-attested [FEDRAMP-REV5-BASELINES §li-saas]."
  - "chunks/03-authorization-paths.md — Place it in readiness: this is a FedRAMP Ready / readiness-assessment context ahead of a full assessment and the AO's ATO."
  - "SKILL.md §1-§11 — route the engagement through the categorization -> LI-SaaS eligibility -> baseline procedure; Moderate+SaaS is NOT LI-SaaS (the trap)."
expected_outputs:
  classification: "LI_SAAS_ELIGIBLE"
  overall_impact: "Low"
  li_saas_eligible: true
  baseline: "LI-SaaS"
  baseline_controls: 156
  controls_3pao_tested: 66
  controls_attested: 90
oracle:
  - "overall_impact recomputed as the high-water mark max(C, I, A) over all-Low == 'Low'"
  - "li_saas_eligible recomputed = (overall_impact == 'Low' AND bool(saas_delivery)) == True; classification == LI_SAAS_ELIGIBLE"
  - "on eligibility, baseline == 'LI-SaaS', baseline_controls == 156, controls_3pao_tested == 66, controls_attested == 90 (the fixed Tailored split; 66 + 90 == 156)"
  - "expected-seed agreement: uc-02-expected.json fields equal the recomputed values"
data_refs:
  - data/seeds/uc-02-input.json
  - data/seeds/uc-02-expected.json
tests:
  - tests/test_fedramp_authorization_oracle.py::test_uc_02_oracle
  - tests/test_fedramp_authorization_metamorphic.py::test_uc02_moderate_saas_is_not_li_saas
  - tests/test_fedramp_authorization_adversarial.py::test_uc02_moderate_plus_saas_not_li_saas
  - tests/test_fedramp_authorization_adversarial.py::test_uc02_low_but_not_saas_not_li_saas
  - tests/test_fedramp_authorization_adversarial.py::test_uc02_missing_saas_flag_refuses
token_baseline: "not yet measured — see telemetry/baseline.md"
status: active
---

# UC-02 — Cloud vendor LI-SaaS readiness (Beacon Forms)

## §1 Context and persona

**Beacon Forms** is a fictional low-impact SaaS offering from **Beacon Software, LLC**, in a **readiness assessment / FedRAMP Ready** context — the founder is checking, before committing to a full assessment, whether the lighter-weight **LI-SaaS (Low-Impact SaaS, Tailored)** baseline is on the table.

The persona is the **cloud-vendor founder** who must answer one question: **is this offering LI-SaaS eligible, and if so what does that baseline look like?** The seed `data/seeds/uc-02-input.json` is the tested fixture; every value below is recomputed from it by `tests/test_fedramp_authorization_oracle.py::test_uc_02_oracle`.

## §2 Categorize — the all-Low high-water mark

The overall impact is the **high-water mark** = `max(C, I, A)` over Low < Moderate < High [FIPS-199 §categorization]:

| FIPS 199 objective | Impact (seeded) |
|---|---|
| Confidentiality | Low |
| Integrity | Low |
| Availability | Low |

All three objectives are **Low**, so the overall impact is **Low**. This is the precondition for LI-SaaS — LI-SaaS Tailored is **Low-impact only**.

## §3 The LI-SaaS eligibility test

LI-SaaS (Tailored) is available iff **both** conditions hold [FEDRAMP-REV5-BASELINES §li-saas]:

1. the overall FIPS 199 impact is **Low**, **and**
2. the offering is **SaaS-delivered** (`saas_delivery == true`).

Beacon Forms is **Low AND SaaS-delivered**, so it is **LI-SaaS eligible** (classification `LI_SAAS_ELIGIBLE`). The eligibility is derived from the two seed facts — `overall_impact == 'Low'` and `saas_delivery` — not asserted.

## §4 The LI-SaaS Tailored baseline — 156 = 66 tested + 90 attested

On eligibility, the offering uses the **LI-SaaS Tailored baseline**: **156 controls** (the same set as the Low baseline), split into:

- **66 controls 3PAO-tested** (independently assessed), and
- **90 controls CSP-attested** (the CSP attests rather than having the 3PAO test them).

`66 + 90 = 156` [FEDRAMP-REV5-BASELINES §li-saas]. The tested/attested split is the **fixed Tailored split** cited to the LI-SaaS baseline doc; the oracle uses this fixed split (it is documented but is not a flat OSCAL re-count). This lighter assessment burden is the whole point of LI-SaaS — a Low-impact SaaS offering does not need the full 3PAO test of every control.

## §5 The Moderate+SaaS trap — NOT LI-SaaS

The most common LI-SaaS misconception is that **any SaaS** can use LI-SaaS. It cannot. LI-SaaS is **Low-impact SaaS only**:

- A **Moderate** (or High) impact system, **even if SaaS-delivered**, is **NOT LI-SaaS eligible** — it takes the full **Moderate (323)** or **High (410)** baseline [FEDRAMP-REV5-BASELINES §li-saas].
- A **Low** impact offering that is **not SaaS-delivered** is **NOT LI-SaaS eligible** — it takes the full **Low (156)** baseline.

The metamorphic and adversarial tests enforce this: a Moderate categorization with `saas_delivery=true` is not LI-SaaS (`test_uc02_moderate_saas_is_not_li_saas`, `test_uc02_moderate_plus_saas_not_li_saas`); a Low-but-not-SaaS offering is not LI-SaaS (`test_uc02_low_but_not_saas_not_li_saas`).

## §6 Oracle — every value is derivable

`tests/test_fedramp_authorization_oracle.py::test_uc_02_oracle` recomputes every value independently from `uc-02-input.json` — no value is echoed from `uc-02-expected.json`:

- `overall_impact` recomputed as the high-water mark `max(C, I, A)` over all-Low == **Low**.
- `li_saas_eligible` recomputed = `(overall_impact == 'Low' AND bool(saas_delivery))` == **True**; `classification == LI_SAAS_ELIGIBLE`.
- On eligibility: `baseline == 'LI-SaaS'`, `baseline_controls == 156`, `controls_3pao_tested == 66`, `controls_attested == 90` — the fixed Tailored split, and `66 + 90 == 156`.
- Expected-seed agreement: the `uc-02-expected.json` fields equal the recomputed values.

**Metamorphic:** flipping the categorization to Moderate (keeping `saas_delivery=true`) makes it not LI-SaaS — it takes the full Moderate baseline (`test_uc02_moderate_saas_is_not_li_saas`). **Adversarial:** Moderate+SaaS is not LI-SaaS (`test_uc02_moderate_plus_saas_not_li_saas`); Low-but-not-SaaS is not LI-SaaS (`test_uc02_low_but_not_saas_not_li_saas`); a missing `saas_delivery` flag makes eligibility undeterminable and the stub refuses (`INSUFFICIENT_INPUT`, `test_uc02_missing_saas_flag_refuses`).

## §7 Anti-hallucination

- **Beacon Forms is fictional**; the seed is the tested fixture and this UC's source of truth. The CIA values, the SaaS flag, and the 66/90 split are exactly as seeded.
- **LI-SaaS is Low-impact SaaS only** — a Moderate/High system, even SaaS-delivered, takes the full Moderate (323) / High (410) baseline, not LI-SaaS [FEDRAMP-REV5-BASELINES §li-saas].
- **The LI-SaaS baseline is 156 = 66 3PAO-tested + 90 CSP-attested** [FEDRAMP-REV5-BASELINES §li-saas]; `66 + 90 = 156` (the same set as the Low baseline).
- **FIPS 199 overall impact is the high-water mark (max of C/I/A)** — all-Low here makes the system Low [FIPS-199 §categorization]. Do not average.
- **FedRAMP baselines ARE tailored 800-53 Rev 5 controls, not a separate catalog** [NIST-800-53R5 §baselines]. For the catalog / RMF, use `nist-800-53-rmf`.
- **This is readiness, not authorization** — eligibility is the start of the path; the full assessment and the AO's ATO follow. This is not authorization or legal advice.
