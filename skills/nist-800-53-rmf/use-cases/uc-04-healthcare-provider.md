---
uc_id: UC-04
title: "Hospital CPOE module: FIPS-199 categorization with clinical availability floor + HIPAA safeguard -> 800-53 view"
industries: [healthcare]
frameworks: [NIST-SP-800-53-Rev5, HIPAA-Security-Rule, FIPS-199]
inputs:
  system_name: "MedFlow Clinical Orders"
  system_description: |
    Computerized provider order entry (CPOE) module at Bellbrook Regional Health
    (6,000-staff hospital system, 4 facilities). Processes PHI: medication and lab
    orders, results, clinical alerts. Order delays directly affect patient care.
    The hospital is aligning the system to 800-53 ahead of a federal health-agency
    data exchange.
  information_types: "data/seeds/uc-04-input.json (2 types; Clinical Orders and Results is patient-safety-relevant and is SUBMITTED with A: LOW on a manual-workaround rationale)"
  in_scope_hipaa_elements: ["164.312(a)(2)(ii)", "164.312(b)", "164.308(a)(7)(ii)(B)", "164.310(d)(2)(i)"]
procedure:
  - "chunks/02-categorize.md — FIPS 199 high-water-mark categorization across information types; apply the clinical availability floor (HOUSE CONVENTION, §Clinical systems note): a patient-safety-relevant information type forces A >= MODERATE; a manual-workaround rationale never lowers clinical availability without documented clinical sign-off."
  - "chunks/03-baseline.md — select the baseline from the floored overall categorization."
  - "chunks/09-crosswalk.md — for each in-scope HIPAA Security Rule element, read the 800-53 view from data/seeds/hipaa-to-800-53.json (generated from the NIST CPRT OLIR set; designation Standard/Required/Addressable carried per element; OLIR informative-reference semantics, no strength ratings)."
expected_outputs:
  fips_199_categorization:
    system_security_category: { c: MODERATE, i: MODERATE, a: MODERATE }
    overall: MODERATE
    clinical_availability_floor_applied: true
  baseline: MODERATE
  hipaa_800_53_view: "4 rows — 164.312(a)(2)(ii) (Required) -> AC-2, AC-3, CP-2; 164.312(b) (Standard) -> AU-1..AU-8 (7 controls); 164.308(a)(7)(ii)(B) (Required) -> CP-2, CP-6, CP-7, CP-8, CP-9, CP-10; 164.310(d)(2)(i) (Required) -> MP-6"
  hipaa_elements_not_in_crosswalk: []
oracle:
  type: derivability
  assertion: |
    tests/test_nist_800_53_rmf_oracle.py::test_uc_04_oracle recomputes everything
    independently from the seeds: high-water mark, floor condition (patient-safety
    flag present AND computed A < MODERATE), overall == baseline, and the HIPAA view
    as a pure lookup of data/seeds/hipaa-to-800-53.json (designation + control IDs).
    The expected-output seed must foot to the same recomputation. Unknown elements
    are reported in hipaa_elements_not_in_crosswalk, never fabricated.
data_refs:
  - "data/seeds/uc-04-input.json"
  - "data/seeds/uc-04-expected.json"
  - "data/seeds/hipaa-to-800-53.json"
tests:
  - "tests/test_nist_800_53_rmf_oracle.py::test_uc_04_oracle"
  - "tests/test_nist_800_53_rmf_adversarial.py::test_uc_04_floor_never_low_for_clinical"
  - "tests/test_nist_800_53_rmf_adversarial.py::test_uc_04_no_floor_without_clinical_flag"
  - "tests/test_nist_800_53_rmf_adversarial.py::test_uc_04_unknown_hipaa_element_not_fabricated"
  - "tests/test_nist_800_53_rmf_metamorphic.py::test_uc_04_information_type_order_invariance"
token_baseline:
  input_p50: null
  output_p50: null
status: active
---

# UC-04 — Hospital CPOE: clinical availability floor + HIPAA -> 800-53 view

## Scenario

Bellbrook Regional Health (the same covered entity as hipaa-security-rule UC-02) is
preparing its CPOE module for a federal health-agency data exchange that requires an
800-53 alignment. Two questions drive the engagement: *what is the FIPS-199 category of a
clinical system?* and *which 800-53 controls correspond to the HIPAA safeguards already in
scope from the hospital's risk analysis?*

## Step 1 — Categorize, with the clinical availability floor (chunks/02-categorize.md)

The submitted worksheet rates Clinical Orders and Results at **A: LOW** because "a paper-order
manual workaround exists." That is the exact pattern this UC exists to stop: for a system
whose outage delays medication and lab orders, a manual workaround is a contingency
*procedure*, not a basis for a LOW availability objective.

**Clinical availability floor (HOUSE CONVENTION — not FIPS 199 text):** if any information
type is patient-safety-relevant, the system availability objective is at least MODERATE.
Manual-workaround rationales never lower clinical availability without documented clinical
sign-off. FIPS 199's high-water mark applies otherwise; per-type provisional impact levels
come from SP 800-60 Vol II ([NIST-SP-800-60]) — verify against the current revision.

Result: C: MODERATE, I: MODERATE, A: LOW -> **MODERATE (floor applied)**. Overall: **MODERATE**.

## Step 2 — Baseline (chunks/03-baseline.md)

Baseline: **MODERATE** from the floored categorization.

## Step 3 — HIPAA safeguard -> 800-53 view (chunks/09-crosswalk.md)

The hospital's HIPAA risk analysis already scopes four Security Rule elements. The crosswalk
seed (generated from the NIST CPRT OLIR set [NIST-CPRT]) gives the 800-53 Rev 5.1.1 view:

| HIPAA element | Designation | 800-53 controls (OLIR informative references) |
|---|---|---|
| 164.312(a)(2)(ii) Emergency access ("break-glass") | Required | AC-2, AC-3, CP-2 |
| 164.312(b) Audit controls | Standard | AU-1, AU-2, AU-3, AU-4, AU-6, AU-7, AU-8 |
| 164.308(a)(7)(ii)(B) Disaster recovery plan | Required | CP-2, CP-6, CP-7, CP-8, CP-9, CP-10 |
| 164.310(d)(2)(i) Disposal | Required | MP-6 |

These are OLIR informative references ("supports" semantics) — implementing the 800-53
controls supports the HIPAA safeguard; it is not a compliance equivalence in either
direction. No exact/partial strength ratings exist in the source and none are asserted.

## Variations / edge cases (test_adversarial.py)

- **All-LOW clinical system:** the floor still raises A to MODERATE; C and I stay LOW.
- **No patient-safety flag:** the floor never fires — no silent escalation for
  administrative PHI systems.
- **Unknown element in scope:** reported in `hipaa_elements_not_in_crosswalk`, never
  fabricated.

## Acceptance

- [x] Seed + derivability oracle (independent recompute; view is a pure crosswalk lookup).
- [x] Floor behavior pinned by adversarial tests in both directions.
- [x] Crosswalk rows carry designation (Standard/Required/Addressable) from the
      hipaa-security-rule fact sheet; CPRT's pre-Omnibus 164.308(b)(4) citation is aliased
      with a note in the seed.
- [ ] Token baseline populated.
