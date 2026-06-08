---
uc_id: UC-01
title: "FedRAMP-bound SaaS categorizes FIPS-199 Moderate, tailors ~325 controls, inherits AC-2 from hyperscaler"
industries: [saas-technology, public-sector]
frameworks: [NIST-SP-800-53-Rev5, NIST-SP-800-37-Rev2, FIPS-199, FedRAMP-Rev5]
inputs:
  system_name: "CaseFlow Cloud"
  system_description: |
    Multi-tenant case management SaaS for federal civilian agencies. Processes
    personally identifiable information (PII) including names, contact information,
    agency-issued identifiers, and case notes for ~250,000 individuals per year.
    Hosted on AWS GovCloud (FedRAMP High authorized). Offered as a SaaS via
    the FedRAMP Marketplace; one sponsoring agency.
  information_types:
    - name: "Case Management Records"
      sp_800_60_info_type_code: "C.3.5.6"  # Public-facing case management, illustrative
      description: "PII, agency case notes, status, attachments"
      cia_baseline: {c: MODERATE, i: MODERATE, a: LOW}
      rationale: |
        Confidentiality: serious adverse effect if disclosed (privacy, identity theft).
        Integrity: serious adverse effect if modified (case outcomes, due process).
        Availability: limited adverse effect if temporarily unavailable (manual workaround).
    - name: "Authentication metadata"
      sp_800_60_info_type_code: "C.3.5.5"
      description: "Login IDs, MFA factor type, last-login timestamp"
      cia_baseline: {c: MODERATE, i: LOW, a: LOW}
      rationale: |
        Confidentiality: serious if disclosed in aggregate (account compromise).
        Integrity/Availability: limited.
  downstream_consumers:
    - "Sponsoring federal agency (primary)"
    - "Other federal agencies via FedRAMP Marketplace P-ATO"
  cloud_provider: "AWS GovCloud (US)"
  cloud_fedramp_id: "AGENCYID-CSP-AWS-GC-FEDRAMP-HIGH"
  customer_responsibility_matrix: "data/seeds/uc-01-crm.json"
procedure:
  - "chunks/02-categorize.md — Categorize using FIPS 199. Apply high-water mark across information types and CIA objectives."
  - "chunks/03-baseline.md — Select baseline. Look up Moderate; tailor via scoping, common-control designation, parameterization, and supplementation."
  - "chunks/02-categorize.md §Procedure — Document in §2 of the SSP."
  - "chunks/03-baseline.md §Procedure — Document tailoring decisions in §8 / §9 / §10 of the SSP."
  - "chunks/04-implement.md §Procedure — Document inheritance in SSP §8 and Customer Responsibility Matrix."
  - "chunks/02-categorize.md §Output template — Produce FIPS 199 Categorization output."
  - "chunks/03-baseline.md §Output template — Produce Control Selection output (highlighted: AC-2 inherited from hyperscaler)."
expected_outputs:
  fips_199_categorization:
    system_name: "CaseFlow Cloud"
    system_security_category: {c: MODERATE, i: MODERATE, a: LOW}
    overall: MODERATE
    high_water_mark: MODERATE
  baseline:
    baseline: MODERATE
    control_count: ~325  # Rev 5; Rev 5 ~325
  inheritance_summary:
    - control_id: AC-2
      status: inherited
      from: "AWS GovCloud FedRAMP High"
      narrative: "Account management for the AWS IAM layer is provided by the cloud. The SaaS implements application-layer accounts (per-tenant user accounts, role assignments, MFA enrollment) at the application tier."
    - control_id: SC-7
      status: inherited
      from: "AWS GovCloud FedRAMP High"
      narrative: "VPC, security groups, network ACLs are provided by the cloud. The SaaS implements application-layer WAF rules and API gateway policies."
    - control_id: AU-2
      status: hybrid
      from: "AWS GovCloud FedRAMP High + application"
      narrative: "CloudTrail provides cloud-side audit events. The SaaS generates application events (login, case access, export) and forwards them to the central SIEM."
  tailoring_decisions:
    - control_id: AC-2(8)
      decision: SCOPING
      rationale: "No privileged accounts are shared; the dynamic account management enhancement does not apply. Justified in SSP §9."
    - control_id: SC-8(1)
      decision: SCOPING
      rationale: "No wireless transmission of classified or sensitive data; the wireless confidentiality enhancement does not apply."
    - control_id: PT-7
      decision: SUPPLEMENT
      rationale: "PII is processed; the 800-53 Rev 5 privacy control family is added (specific authority per FIPS 199 + agency privacy officer)."
oracle:
  type: schema_match
  assertion: |
    The skill's output must satisfy:
      - system_security_category.overall == "MODERATE"
      - baseline == "MODERATE"
      - inheritance_summary includes at least: AC-2 (inherited from AWS GovCloud), SC-7 (inherited), AU-2 (hybrid)
      - tailoring_decisions includes AC-2(8) SCOPING with rationale referencing shared accounts
data_refs:
  - "data/seeds/uc-01-input.json"
  - "data/seeds/uc-01-crm.json"
  - "data/seeds/uc-01-expected.json"
tests:
  - "tests/test_oracle.py::test_uc_01"
  - "tests/test_trace.py::test_uc_01_trace"
  - "tests/test_adversarial.py::test_uc_01_dual_classification"
token_baseline:
  input_p50: null
  output_p50: null
status: active
---

# UC-01 — FedRAMP-bound SaaS categorizes FIPS-199 Moderate

## Scenario

**CaseFlow Cloud** is a multi-tenant case management SaaS used by federal civilian agencies. The system is built on AWS GovCloud (FedRAMP High authorized). The CSP is preparing for an initial FedRAMP Moderate authorization sponsored by a single agency. After authorization, the package will be published to the FedRAMP Marketplace and other agencies can issue P-ATOs.

The system processes PII for ~250,000 individuals per year. The system stores case notes, agency-issued identifiers, contact information, and attachments. Authentication is federated via the customer's IdP (SAML or OIDC) plus the SaaS's own application-layer accounts for SaaS-internal admins.

## Walk-through

### Step 1 — FIPS 199 Categorization (Skill §3.6, §5.1, §6.1)

The agent (or human) applies FIPS 199 to each information type:

- **Case Management Records (PII)** — `C: MODERATE`, `I: MODERATE`, `A: LOW`. The system security category is the high-water mark across the three: `MODERATE` overall.

- **Authentication metadata** — `C: MODERATE`, `I: LOW`, `A: LOW`. Does not change the system category (still high-water = MODERATE).

- **System security category:** `C: M, I: M, A: L → overall MODERATE` (high-water = Moderate).

The output is the FIPS 199 categorization YAML (§6.1):

```yaml
system_name: CaseFlow Cloud
system_security_category:
  c: MODERATE
  i: MODERATE
  a: LOW
overall: MODERATE
high_water_mark: MODERATE
pia_required: true
special_factors:
  - "Processes PII of ~250k individuals per year"
  - "Multi-tenant SaaS on FedRAMP-authorized IaaS"
```

### Step 2 — Baseline Selection (Skill §4.2, §5.2, §6.2)

- Baseline: **Moderate** (NIST 800-53 Rev 5 ~325 controls; Rev Rev 5 ~325 controls).
- Apply **scoping**: drop controls whose scope doesn't apply. For CaseFlow Cloud:
  - `AC-2(8)` (Dynamic Account Management) — SCOPED OUT. No shared accounts; dynamic accounts are not used.
  - `SC-8(1)` (Cryptographic Protection for Wireless) — SCOPED OUT. No wireless transmission of sensitive data.
- Apply **common-control designation**: many controls (e.g., AT-2 security awareness, AT-3 role-based training, PS-3 personnel screening) are inherited from the corporate common-controls catalog. The SSP §8 documents which.
- Apply **parameterization**: e.g., `AC-2(3)` requires account-disable on a defined trigger. Parameter: "Disable on termination within 4 business hours."
- Apply **supplementation**: add the Rev 5 privacy control family (`PT-*`) because PII is processed. The agency's privacy officer requires a PIA.

### Step 3 — Inheritance mapping (Skill §4.6, §5.3)

The CSP documents the inheritance in the Customer Responsibility Matrix (CRM):

| Control | Status | Source | Narrative |
|---------|--------|--------|-----------|
| AC-2 (Account Management — cloud-layer) | inherited | AWS GovCloud (FedRAMP High) | IAM roles, federated identity |
| AC-2 (Account Management — app-layer) | system-specific | CaseFlow Cloud | Per-tenant user accounts, role assignment, MFA enrollment |
| AU-2 (Auditable Events — cloud-layer) | inherited | AWS GovCloud | CloudTrail events |
| AU-2 (Auditable Events — app-layer) | system-specific | CaseFlow Cloud | Application events (login, case access, export) |
| SC-7 (Boundary Protection) | inherited | AWS GovCloud | VPC, security groups, network ACLs |
| SC-7 (WAF rules) | system-specific | CaseFlow Cloud | Application-layer WAF rules, API gateway policies |
| IA-2 (Identification & Auth — federation) | inherited | Customer IdP | SAML/OIDC |
| IA-2 (Identification & Auth — app) | system-specific | CaseFlow Cloud | App-layer MFA enforcement |

The output is the Control Selection YAML (§6.2), with each control tagged as `inherited | system-specific | hybrid`, source, narrative, evidence_refs, and assessment objectives met.

### Step 4 — SSP narrative (§5.3, output §6.2)

The SSP §1 (System Identification), §2 (System Environment), §8 (System Interconnections and Inheritance), §9 (Controls), §10 (Implementation Status), §13 (ISCM Strategy) document:

- The FedRAMP authorization boundary.
- The information system components in scope.
- The customer responsibility matrix.
- The control narratives (per control, with inheritance tags).
- The implementation status (Implemented, Partially Implemented, Planned, Alternative, N/A).
- The ISCM strategy (frequency, triggers, evidence retention).

## Expected Output (oracle target)

```yaml
fips_199_categorization:
  system_security_category: {c: MODERATE, i: MODERATE, a: LOW}
  overall: MODERATE
baseline:
  baseline: MODERATE
  control_count: 325
inheritance_summary:
  - control_id: AC-2
    status: hybrid  # cloud-layer inherited, app-layer system-specific
  - control_id: SC-7
    status: inherited
  - control_id: AU-2
    status: hybrid
tailoring_decisions:
  - control_id: AC-2(8)
    decision: SCOPING
  - control_id: SC-8(1)
    decision: SCOPING
  - control_id: PT-7
    decision: SUPPLEMENT
```

The oracle assertion (§`data_refs`/frontmatter):

- `system_security_category.overall == "MODERATE"`
- `baseline == "MODERATE"`
- `inheritance_summary` includes AC-2, SC-7, AU-2 with statuses (`inherited` or `hybrid`).
- `tailoring_decisions` includes AC-2(8) SCOPING, SC-8(1) SCOPING, PT-7 SUPPLEMENT.

## Variations / edge cases (test_adversarial.py)

- **V1 — Categorization drift:** if the system starts processing classified information, the categorization moves to HIGH and the baseline shifts. The skill must detect and re-baseline.
- **V2 — Inheritance invalidation:** if the CSP migrates from AWS GovCloud to a non-FedRAMP cloud, every inherited control becomes system-specific. The skill must reflect the new boundary.
- **V3 — PII volume increase:** if PII processing exceeds a threshold (e.g., 1M individuals), the Rev 5 privacy controls may become higher-priority; the AO may require a PIA refresh.
- **V4 — Compensating control challenge:** the AO challenges a compensating control on SC-13 (FIPS-validated crypto). The skill must produce a compensating-control memo that documents the alternate, why it meets the intent, and how the assessor will evaluate it.
- **V5 — Dual classification:** the SaaS serves two customers, one with PII at MODERATE and one with CUI at MODERATE. The boundary must cover both; the controls in scope may differ slightly.

## Acceptance

- [x] UC registered in `use-cases/_index.md`.
- [x] Oracle defined.
- [x] Data seeds at `data/seeds/uc-01-input.json`, `data/seeds/uc-01-crm.json`, `data/seeds/uc-01-expected.json`.
- [x] Tests at `tests/test_oracle.py::test_uc_01`, `tests/test_trace.py::test_uc_01_trace`, `tests/test_adversarial.py::test_uc_01_dual_classification`.
- [ ] Token baseline populated after instrumented run.
