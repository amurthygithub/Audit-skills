---
uc_id: UC-01
title: "SaaS FedRAMP Moderate via Agency Authorization — the FIPS 199 high-water mark across C=Moderate/I=Low/A=Low yields overall Moderate, the Moderate baseline selects 323 controls, and 5 SAR findings get POA&M deadlines = identified-date + the 30/90/180 ConMon SLA"
industries: [saas-technology]
frameworks: [FedRAMP-Rev5, FedRAMP-Authorization-Act-2022, OMB-M-24-15, NIST-SP-800-53r5]
inputs:
  system: "Acme Cloud Suite (CSO) — Acme SaaS, Inc.; Agency Authorization, sponsoring agency Department of Example (data/seeds/uc-01-input.json)"
  fips199: "per-objective FIPS 199 impact — confidentiality Moderate, integrity Low, availability Low (data/seeds/uc-01-input.json)"
  sar_findings: "5 SAR findings, each with a severity and identified_date 2025-03-01 (F-001/F-002 High, F-003/F-004 Moderate, F-005 Low) (data/seeds/uc-01-input.json)"
procedure:
  - "chunks/02-impact-levels-and-baselines.md — Categorize the system: the FIPS 199 overall impact is the high-water mark = max(C, I, A) over Low<Moderate<High [FIPS-199 §categorization]; C=Moderate, I=Low, A=Low -> overall Moderate."
  - "chunks/02-impact-levels-and-baselines.md — Select the baseline from the overall impact: Low 156 / Moderate 323 / High 410 [FEDRAMP-REV5-BASELINES §counts]; Moderate -> 323 controls (tailored 800-53 Rev 5, not a separate catalog [NIST-800-53R5 §baselines])."
  - "chunks/03-authorization-paths.md — Confirm the path: Agency Authorization is the operative Rev 5 path; the sponsoring agency's AO grants the ATO; the JAB P-ATO is retired [OMB-M-24-15 §authority]."
  - "chunks/04-the-authorization-package.md — Place the findings: each open SAR finding becomes a POA&M item the CSP maintains [FEDRAMP-PLAYBOOK §ssp]."
  - "chunks/06-continuous-monitoring.md — Compute each POA&M remediation deadline = identified_date + the ConMon SLA for the finding's severity: 30 days high/critical, 90 moderate, 180 low [FEDRAMP-CONMON §monthly]."
  - "SKILL.md §1-§11 — route the engagement through the categorization -> baseline -> package -> ConMon procedure."
expected_outputs:
  classification: "FEDRAMP_MODERATE"
  overall_impact: "Moderate"
  baseline: "Moderate"
  baseline_controls: 323
  poam_open: 5
  poam:
    - {id: "F-001", severity: "High", remediation_due: "2025-03-31"}
    - {id: "F-002", severity: "High", remediation_due: "2025-03-31"}
    - {id: "F-003", severity: "Moderate", remediation_due: "2025-05-30"}
    - {id: "F-004", severity: "Moderate", remediation_due: "2025-05-30"}
    - {id: "F-005", severity: "Low", remediation_due: "2025-08-28"}
oracle:
  - "overall_impact recomputed as the high-water mark max(C, I, A) over {Low<Moderate<High} == 'Moderate'; classification == FEDRAMP_MODERATE"
  - "baseline_controls looked up from the overall impact via {Low:156, Moderate:323, High:410} == 323 (NOT hardcoded to one value — the lookup is keyed on the derived level)"
  - "each POA&M remediation_due recomputed = identified_date + {High/Critical:30, Moderate:90, Low:180} days: F-001/F-002 2025-03-01+30=2025-03-31, F-003/F-004 +90=2025-05-30, F-005 +180=2025-08-28"
  - "poam_open == 5 (one item per SAR finding)"
  - "expected-seed agreement: uc-01-expected.json fields equal the recomputed values"
data_refs:
  - data/seeds/uc-01-input.json
  - data/seeds/uc-01-expected.json
tests:
  - tests/test_fedramp_authorization_oracle.py::test_uc_01_oracle
  - tests/test_fedramp_authorization_metamorphic.py::test_uc01_raising_an_objective_to_high_flips_baseline
  - tests/test_fedramp_authorization_metamorphic.py::test_uc01_finding_order_invariance
  - tests/test_fedramp_authorization_adversarial.py::test_uc01_missing_fips199_refuses
  - tests/test_fedramp_authorization_adversarial.py::test_uc01_invalid_objective_refuses
token_baseline: "not yet measured — see telemetry/baseline.md"
status: active
---

# UC-01 — SaaS FedRAMP Moderate via Agency Authorization (Acme Cloud Suite)

## §1 Context and persona

**Acme Cloud Suite** is a fictional cloud service offering (CSO) from **Acme SaaS, Inc.**, pursuing a FedRAMP authorization through the **Agency Authorization** path with the **Department of Example** as sponsoring agency. This is the most common road to an ATO: a SaaS CSP categorizes its system, lands on a baseline, builds the package, gets assessed by a 3PAO, and then maintains the authorization through monthly ConMon.

The persona is the **CSP ISSO** who owns the authorization and must decide three things: (1) the FIPS 199 overall categorization, (2) which baseline that selects and how many controls it is, and (3) the POA&M remediation deadline for each SAR finding. The seed `data/seeds/uc-01-input.json` is the tested fixture; every number below is recomputed from it by `tests/test_fedramp_authorization_oracle.py::test_uc_01_oracle`.

## §2 Categorize the system — the FIPS 199 high-water mark

The overall system impact is the **high-water mark**: the **maximum** of the confidentiality, integrity, and availability impact levels, ordered Low < Moderate < High [FIPS-199 §categorization]. There is no averaging.

| FIPS 199 objective | Impact (seeded) |
|---|---|
| Confidentiality | Moderate |
| Integrity | Low |
| Availability | Low |

The maximum across the three is **Moderate** (confidentiality drives it). So the **overall impact is Moderate** — the single Moderate objective pulls the whole system to Moderate even though integrity and availability are Low.

## §3 Select the baseline — Moderate → 323 controls

The overall impact selects the FedRAMP Rev 5 baseline, and each baseline has a fixed control count [FEDRAMP-REV5-BASELINES §counts]:

| Overall impact | Baseline | Controls |
|---|---|---|
| Low | Low | 156 |
| **Moderate** | **Moderate** | **323** |
| High | High | 410 |

Acme is **Moderate → the Moderate baseline → 323 controls** (classification `FEDRAMP_MODERATE`). These are **tailored NIST SP 800-53 Rev 5 controls** — the same catalog IDs (AC-2, SI-2, …), tailored up from 800-53B's 287 Moderate baseline; not a separate FedRAMP catalog [NIST-800-53R5 §baselines]. The CSP authors the SSP describing how each of the 323 controls is implemented [FEDRAMP-PLAYBOOK §ssp].

The lookup is **keyed on the derived level**, not hardcoded: the metamorphic test proves that raising any single objective to High flips the overall impact to High and the baseline to **410** (`test_uc01_raising_an_objective_to_high_flips_baseline`).

## §4 The authorization path — Agency Authorization

Acme pursues **Agency Authorization**, the operative Rev 5 path, with the Department of Example as sponsoring agency. The sponsoring agency's **authorizing official (AO)** makes the ATO decision; the **JAB and its P-ATO are retired** and the current authorizer is the statutory FedRAMP Board [OMB-M-24-15 §authority; FEDRAMP-ACT-2022 §3610]. The path does not change the categorization or the control count — it determines who grants the ATO.

## §5 POA&M remediation deadlines — date + severity SLA

Each of the 5 SAR findings becomes a POA&M item, and each item's **remediation deadline = its identified-date + the FedRAMP ConMon SLA for its severity** [FEDRAMP-CONMON §monthly]:

- **High / Critical → 30 days**
- **Moderate → 90 days**
- **Low → 180 days**

All five findings were identified on **2025-03-01**, so the deadlines compute as:

| Finding | Control | Severity | SLA (days) | Remediation due (identified-date + SLA) |
|---|---|---|---|---|
| F-001 | AC-2 | High | 30 | 2025-03-31 |
| F-002 | SI-2 | High | 30 | 2025-03-31 |
| F-003 | AU-6 | Moderate | 90 | 2025-05-30 |
| F-004 | CM-6 | Moderate | 90 | 2025-05-30 |
| F-005 | CP-9 | Low | 180 | 2025-08-28 |

**POA&M open: 5** (one item per finding). The dates are derived by date arithmetic — `2025-03-01 + 30 = 2025-03-31`, `+ 90 = 2025-05-30`, `+ 180 = 2025-08-28` — not stored labels. The CSP carries these through monthly ConMon until each is remediated or formally deviated.

## §6 Oracle — every number is derivable

`tests/test_fedramp_authorization_oracle.py::test_uc_01_oracle` recomputes every figure independently from `uc-01-input.json` — no value is echoed from `uc-01-expected.json`:

- `overall_impact` recomputed as the high-water mark `max(C, I, A)` over `{Low<Moderate<High}` == **Moderate**; `classification == FEDRAMP_MODERATE`.
- `baseline_controls` looked up from the derived level via `{Low:156, Moderate:323, High:410}` == **323** — keyed on the derived impact, not hardcoded to one value.
- Each `remediation_due` recomputed as `identified_date + {High/Critical:30, Moderate:90, Low:180}` days: F-001/F-002 → 2025-03-31, F-003/F-004 → 2025-05-30, F-005 → 2025-08-28.
- `poam_open == 5`.
- Expected-seed agreement: the `uc-01-expected.json` fields equal the recomputed values.

**Metamorphic:** raising any single objective to High flips the overall to High and the baseline to 410 (`test_uc01_raising_an_objective_to_high_flips_baseline`); reordering the findings changes none of the deadlines (`test_uc01_finding_order_invariance`). **Adversarial:** with no FIPS 199 categorization supplied the stub refuses (`INSUFFICIENT_INPUT`, `test_uc01_missing_fips199_refuses`); an objective that is not Low/Moderate/High refuses (`test_uc01_invalid_objective_refuses`).

## §7 Anti-hallucination

- **Acme Cloud Suite is fictional**; the seed is the tested fixture and this UC's source of truth. The org name, the C/I/A values, and the deadlines are exactly as seeded.
- **FIPS 199 overall impact is the high-water mark (max of C/I/A)** — Moderate here because confidentiality is Moderate; do not average [FIPS-199 §categorization].
- **The baseline counts are fixed: Low 156 / Moderate 323 / High 410** [FEDRAMP-REV5-BASELINES §counts]. 323 is the Rev 5 Moderate count (325 would be Rev 4 — wrong here).
- **FedRAMP baselines ARE tailored 800-53 Rev 5 controls, not a separate catalog** [NIST-800-53R5 §baselines]. For the catalog / RMF, use `nist-800-53-rmf`.
- **The JAB and its P-ATO are retired** — Agency Authorization is the operative path; the sponsoring agency's AO grants the ATO [OMB-M-24-15 §authority; FEDRAMP-ACT-2022 §3610].
- **ConMon SLAs are 30 / 90 / 180 days** (high-critical / moderate / low); the deadlines are derived from each finding's identified-date, never hard-coded [FEDRAMP-CONMON §monthly].
- **This is not authorization or legal advice** — the ATO is the authorizing official's risk-based decision.
