---
uc_id: UC-01
title: "Full SOC 2 Type II Examination Walkthrough"
industries: [saas-technology, healthcare]
frameworks: [SOC-2-TSC-2017, COSO-2013]
inputs:
  system_description: "Multi-tenant SaaS platform, AWS IaaS, processes customer PII for 50k users."
  tsc_categories: [Security, Availability, Confidentiality]
  examination_period: "2025-01-01 to 2025-12-31 (12 months)"
  subservice_orgs: [AWS (IaaS)]
procedure:
  - "chunks/02-engagement-type-decision.md -- Classify as SOC 2 Type II (Step 2 of decision tree: TSC-based, restricted distribution)."
  - "chunks/03-tsp-criteria.md -- Scope criteria: 33 CC + 3 Availability + 2 Confidentiality = 38 criteria."
  - "chunks/06-cuec-csoc-inheritance.md -- Identify CUECs (user access provisioning, data input validation) and CSOCs (AWS carve-out)."
  - "chunks/07-opinion-lifecycle-sampling.md -- Plan sampling: daily controls 25-40 samples, monthly 2-5. Execute examination."
  - "chunks/04-report-structures.md -- Draft SOC 2 Type II report with all four sections."
  - "chunks/07-opinion-lifecycle-sampling.md -- Determine opinion: evaluate exceptions, determine if unqualified."
  - "chunks/05-assertion-bridge.md -- Produce management assertion (3-paragraph Type II format)."
expected_outputs:
  soc2_type2_report: "Complete SOC 2 Type II report with: Section I (Opinion -- Unqualified), Section II (System Description with CUECs and CSOCs), Section III (Management Assertion, 3-paragraph), Section IV (Tests of Controls and Results for 38 criteria)."
  cuec_list: "At least 4 CUECs documented and linked to specific TSC criteria."
  csoc_list: "AWS carve-out: infrastructure access, physical security, network security."
  opinion_type: "Unqualified (assuming no exceptions found)."
oracle:
  type: schema_match
  assertion: "Output contains all four SOC 2 Type II report sections; CUECs >= 4; CSOCs identified for AWS; opinion type is one of [Unqualified, Qualified]."
data_refs:
  - "data/seeds/uc-01-input.json (planned)"
tests:
  - "tests/test_oracle.py::test_uc_01_oracle (planned)"
status: stub
---

# UC-01 -- Full SOC 2 Type II Examination Walkthrough

## Scenario

CloudStack SaaS Inc. provides a cloud-based project management platform. Their enterprise customers request a SOC 2 report as part of vendor due diligence. This is their third SOC engagement (established program). They use AWS as their IaaS provider.

## Walk-through

1. Engagement Classification (chunk 02): Subject matter is TSC (not ICFR, not entity-wide cybersecurity, not manufacturing). Restricted distribution acceptable under NDA. -> SOC 2.

2. Report Type (chunk 02): Established program -> Type II. 12-month examination period: Jan 1-Dec 31, 2025.

3. TSC Scoping (chunk 03): Security always required. Availability included because CloudStack commits to 99.9% uptime SLA. Confidentiality included because customer project data is classified as confidential. Processing Integrity and Privacy not required for this engagement. Total: 33 CC + 3 A + 2 C = 38 criteria.

4. Subservice Organizations (chunk 06): AWS IaaS -> Carve-out method. AWS has its own SOC 2 report. CSOCs: infrastructure access controls, data center physical security, network security, encryption at rest. CUECs: user access provisioning, data input validation, customer-managed encryption keys, incident notification.

5. Examination (chunk 07): Daily controls (e.g., access reviews, backup verification) -> 30 samples each across 12 months. Monthly controls (e.g., vendor risk reviews) -> 4 samples each. Quarterly controls -> 4 samples each (one per quarter). Deviation rate analysis applied.

6. Report Drafting (chunk 04): SOC 2 Type II with all four sections. Section I: unqualified opinion (assuming no material exceptions). Section II: system description with CUECs and CSOCs. Section III: management assertion (3-paragraph). Section IV: tests of controls for 38 criteria.

7. Management Assertion (chunk 05): 3 paragraphs covering fair presentation, design suitability, operating effectiveness. Signed and dated.

## Output Sample

```yaml
engagement:
  soc_type: SOC-2
  report_type: Type-II
  examination_period: {start: "2025-01-01", end: "2025-12-31"}
  tsc_categories: [Security, Availability, Confidentiality]
  criteria_count: 38
subservice:
  method: carve-out
  organizations: ["AWS (IaaS)"]
  csocs: ["Infrastructure access controls", "Physical security", "Network security"]
  cuecs: ["User access provisioning", "Data input validation", "Customer-managed encryption keys", "Incident notification"]
opinion:
  type: Unqualified
  language: "In our opinion, in all material respects..."
```

## Variations

- If exceptions found: re-run through opinion determination (chunk 07 Step 5) for qualified vs adverse.
- If Privacy criteria added: scope increases to 46 criteria; add P1-P8 GDPR mapping.
- If first-time engagement: recommend Type I readiness first.
