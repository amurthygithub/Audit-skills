---
uc_id: UC-01
title: "Health-tech SaaS BA conducts a Security Rule risk analysis and dispositions all 22 addressable implementation specifications (12 decision-required walked end-to-end)"
industries: [saas-technology]
frameworks: [CFR-45-164-Subpart-C, NIST-SP-800-66-Rev2, HHS-SRA-Tool]
inputs:
  org: "CareSync Relay — fictional business associate, 40 staff, fully remote, AWS (commercial) hosted, ePHI for 12 covered-entity provider groups"
  risk_records: "15 risks (asset, threat, vulnerability, likelihood 1-3, impact 1-3) from data/seeds/uc-01-risks.json"
  addressable_register: "all 22 addressable specs from the fact-sheet identifier list, each with environment facts; 12 flagged decision_required (data/seeds/uc-01-addressable-register.json)"
  as_of_date: "2026-06-01"
procedure:
  - "chunks/02-risk-analysis-and-management.md — Conduct the 164.308(a)(1)(ii)(A) risk analysis: enumerate ePHI systems, score each risk likelihood (1-3) x impact (1-3), band Low <=2 / Medium 3-4 / High >=6 (house convention — the rule prescribes no scale)."
  - "chunks/02-risk-analysis-and-management.md — Feed High-band risks into the 164.308(a)(1)(ii)(B) risk management plan; note PL 116-321 recognized-security-practices documentation (mitigation, not immunity)."
  - "chunks/07-addressable-decisions-and-evidence.md — Disposition every addressable spec per 164.306(d)(3): assess; implement if reasonable and appropriate; otherwise document why not AND implement an equivalent alternative measure if reasonable and appropriate."
  - "chunks/05-technical-safeguards.md — Resolve the encryption-at-rest decision (164.312(a)(2)(iv)): Addressable as written, but derive the disposition from the environment facts (cloud-hosted, 12 CE customers, no compensating control)."
  - "SKILL.md §4 (decision logic) — apply the addressable-disposition decision tree; SKILL.md §5 (procedure templates) — populate the disposition-record template per spec."
expected_outputs:
  classification: "RISKS_15_HIGH_4"
  risk_summary: { total: 15, by_band: { High: 4, Medium: 6, Low: 5 } }
  disposition_summary: { implement: 15, alternative_measure: 3, not_reasonable_documented: 4 }
  decision_required_count: 12
  encryption_at_rest_disposition: "implement"
oracle:
  - "by_band recomputed independently from uc-01-risks.json (likelihood x impact, house bands) == {High: 4, Medium: 6, Low: 5}; total == 15"
  - "exactly 22 dispositions — one per addressable spec in the register, none invented; every spec_id exists in the fact-sheet identifier list"
  - "disposition per spec recomputed from the seed's documented assessment (164.306(d)(3) logic) == stub output; summary foots: 15 implement / 3 alternative_measure / 4 not_reasonable_documented"
  - "every alternative_measure row carries a non-empty alternative; every not_reasonable_documented row carries a justification"
  - "decision_required_count == 12 (recounted from the seed); encryption_at_rest_disposition derived == implement"
data_refs:
  - data/seeds/uc-01-input.json
  - data/seeds/uc-01-risks.json
  - data/seeds/uc-01-addressable-register.json
  - data/seeds/uc-01-expected.json
tests:
  - tests/test_hipaa_security_rule_oracle.py::test_uc_01_oracle
  - tests/test_hipaa_security_rule_metamorphic.py::test_uc01_risk_order_invariance
  - tests/test_hipaa_security_rule_metamorphic.py::test_uc01_band_monotonicity
  - tests/test_hipaa_security_rule_adversarial.py::test_uc01_empty_register
  - tests/test_hipaa_security_rule_adversarial.py::test_uc01_no_alternative_and_no_justification_still_documented_path
token_baseline: "not yet measured — see telemetry/baseline.md"
status: active
---

# UC-01 — BA risk analysis and addressable dispositions (CareSync Relay)

## §1 Context and persona

**CareSync Relay** is a fictional health-tech SaaS business associate: 40 staff, fully remote, hosted on AWS (commercial), processing ePHI for 12 covered-entity provider groups through a care-coordination API, a message relay store, and an analytics warehouse (de-identified where feasible). As a business associate it is **directly liable** for Security Rule compliance — §164.302 binds "a covered entity or business associate" since the 2013 Omnibus amendments.

The engagement produces the two anchor artifacts OCR asks for first: a **risk analysis** (§164.308(a)(1)(ii)(A), Required) and a **disposition record for every addressable implementation specification** (§164.306(d)(3)). The seeds in `data/seeds/` are the tested fixture; every number below is recomputed from them by `tests/test_hipaa_security_rule_oracle.py::test_uc_01_oracle`.

## §2 Risk analysis — 15 risks, house scoring convention

**House convention (labeled — not from the rule):** risk score = likelihood (1–3) × impact (1–3); bands **Low ≤2 / Medium 3–4 / High ≥6**. The regulation requires "an accurate and thorough assessment of the potential risks and vulnerabilities to the confidentiality, integrity, and availability" of ePHI [CFR-45-164-Subpart-C §164.308(a)(1)(ii)(A)] but prescribes no scale; NIST SP 800-66r2 and the HHS SRA Tool both leave scoring methodology to the organization.

| Risk | Asset | Threat / vulnerability | L | I | Score | Band |
|------|-------|------------------------|---|---|-------|------|
| R-01 | message relay store | ransomware / EDR gaps on two build hosts | 3 | 3 | 9 | High |
| R-02 | care-coordination API | credential stuffing / no rate limiting on legacy auth endpoint | 3 | 2 | 6 | High |
| R-03 | analytics warehouse | over-broad internal access / unused admin grants | 2 | 3 | 6 | High |
| R-04 | backup snapshots | unencrypted copy in legacy bucket / pre-KMS snapshots not migrated | 3 | 3 | 9 | High |
| R-05 | laptops | device theft / FDE attestation missing for 3 devices | 1 | 3 | 3 | Medium |
| R-06 | IdP | MFA fatigue attack / push-only second factor | 3 | 1 | 3 | Medium |
| R-07 | API gateway | DDoS-driven outage / single-region deployment | 2 | 2 | 4 | Medium |
| R-08 | message relay store | insider exfiltration / DLP alerts not reviewed weekly | 2 | 2 | 4 | Medium |
| R-09 | third-party email | ePHI in support attachments / no attachment scrubbing | 1 | 3 | 3 | Medium |
| R-10 | CI/CD pipeline | secrets sprawl / tokens in older repos | 2 | 2 | 4 | Medium |
| R-11 | vendor SDK | supply-chain compromise / no SBOM review | 1 | 1 | 1 | Low |
| R-12 | staging environment | prod data reuse / masking job optional | 1 | 2 | 2 | Low |
| R-13 | office wifi (none) | n/a (remote org) / legacy policy references unused asset | 2 | 1 | 2 | Low |
| R-14 | analytics warehouse | re-identification / k-anonymity threshold undocumented | 1 | 1 | 1 | Low |
| R-15 | status page | information disclosure / incident details over-shared | 1 | 2 | 2 | Low |

**Rollup: 15 risks — High 4 / Medium 6 / Low 5.** The 4 High-band risks (R-01, R-02, R-03, R-04) seed the §164.308(a)(1)(ii)(B) risk management plan: measures "sufficient to reduce risks and vulnerabilities to a reasonable and appropriate level." R-04 (unencrypted pre-KMS snapshots) also feeds the encryption-at-rest decision in §4 below.

## §3 Addressable dispositions — all 22 specs, one disposition each

Per §164.306(d)(3), **addressable never means optional**: assess each spec; implement it if reasonable and appropriate; otherwise document why it would not be reasonable and appropriate AND implement an equivalent alternative measure if reasonable and appropriate. CareSync Relay dispositions **all 22 addressable specs** (the fact sheet's complete addressable list):

**Disposition summary: 15 implement / 3 alternative_measure / 4 not_reasonable_documented.**

The 4 `not_reasonable_documented` specs are all facility-related physical specs (§164.310(a)(2)(i)–(iv)): CareSync Relay is fully remote with no organization-controlled facility housing ePHI systems; data-center physical controls are inherited from the cloud provider and reviewed annually via the provider's SOC 2 report. The documentation of "why not" is itself the compliance artifact — the spec is not skipped, it is dispositioned.

## §4 The 12 decision-required specs, walked end-to-end

The engagement flagged 12 specs `decision_required` (the rest carry standing dispositions from the prior cycle). Each row reuses the seed's documented assessment:

| # | Spec | Disposition | Documented assessment (from the seed) |
|---|------|-------------|----------------------------------------|
| 1 | 164.308(a)(3)(ii)(A) Authorization and/or supervision | implement | Engineering leads supervise ePHI-adjacent work; access reviewed weekly |
| 2 | 164.308(a)(3)(ii)(C) Termination procedures | implement | Same-day deprovisioning runbook through the IdP |
| 3 | 164.308(a)(5)(ii)(C) Log-in monitoring | alternative_measure | Per-application log-in monitoring is not reasonable and appropriate for a 40-person single-sign-on environment. **Alternative:** IdP anomalous-login alerting reviewed weekly; centralized SSO makes per-application log-in review redundant |
| 4 | 164.308(a)(5)(ii)(D) Password management | alternative_measure | Password management procedures are superseded by passwordless authentication. **Alternative:** passwordless WebAuthn with IdP-enforced MFA replaces password creation/rotation procedures |
| 5 | 164.308(a)(7)(ii)(D) Testing and revision procedures | implement | Annual disaster-recovery tabletop plus restore test |
| 6 | 164.310(a)(2)(ii) Facility security plan | not_reasonable_documented | Fully remote organization; no facility houses ePHI systems. Workstation protections are addressed under 164.310(b)–(c) |
| 7 | 164.310(a)(2)(iv) Maintenance records | not_reasonable_documented | No organization-controlled facility; provider maintenance records are covered by the provider's SOC 2 report |
| 8 | 164.310(d)(2)(iv) Data backup and storage | alternative_measure | Pre-movement backup is not reasonable and appropriate because endpoints are barred from storing ePHI. **Alternative:** zero-ePHI-on-endpoints policy enforced by MDM and DLP; nothing to copy before moving equipment |
| 9 | 164.312(a)(2)(iii) Automatic logoff | implement | 15-minute idle session timeout enforced at the IdP and in the application |
| 10 | 164.312(a)(2)(iv) Encryption and decryption | implement | Encryption at rest: AES-256 via cloud KMS on every datastore holding ePHI — reasonable and appropriate given cloud hosting and 12 covered-entity customers |
| 11 | 164.312(c)(2) Mechanism to authenticate ePHI | implement | Object versioning plus checksum validation on ePHI stores |
| 12 | 164.312(e)(2)(ii) Encryption (transmission) | implement | TLS 1.2+ enforced on every external connection carrying ePHI |

**The encryption-at-rest decision (row 10) is derived, not hard-coded.** §164.312(a)(2)(iv) is Addressable as written, but the environment facts force the answer: cloud-hosted multi-tenant ePHI for 12 covered entities, risk R-04 already demonstrates the cost of an unencrypted copy, and no compensating control exists. The assessed conclusion is `implement` — the oracle asserts the derivation from the seed, and the doc shows the reasoning. The 10 non-decision-required specs (e.g., 164.308(a)(3)(ii)(B) workforce clearance, 164.312(e)(2)(i) integrity controls, and the remaining facility specs 164.310(a)(2)(i)/(iii)) carry the standing dispositions recorded in the register.

## §5 Oracle — every number is derivable

`tests/test_hipaa_security_rule_oracle.py::test_uc_01_oracle` recomputes **every** number above independently from the seed files — no figure is echoed from the stub or from `uc-01-expected.json`:

- Band counts recomputed from `uc-01-risks.json` with the house formula; asserted equal to the stub output AND to the expected seed (`High 4 / Medium 6 / Low 5`, total 15).
- Disposition per spec recomputed from each register row's `reasonable_and_appropriate` / `alternative` fields via the §164.306(d)(3) logic; exactly 22 dispositions; summary foots to `15 / 3 / 4`.
- Every `alternative_measure` row must carry a non-empty alternative; every `not_reasonable_documented` row must carry a justification.
- `decision_required_count` recounted == 12; encryption-at-rest disposition derived == `implement`.
- Every `spec_id` must exist in the fact sheet §0 identifier list — no fabricated citations.

Metamorphic: reversing risk-record order changes nothing; raising a risk's impact can never lower its band. Adversarial: an empty register yields zero dispositions (never invented specs); a not-reasonable spec with no alternative falls to the documented path, never silently to `implement`.

## §6 Anti-hallucination

- **CareSync Relay is fictional**; the seeds are the tested fixture and this UC's source of truth.
- **The risk scale and bands are a house convention, labeled as such** — 45 CFR 164 prescribes no scoring methodology.
- **Addressable ≠ optional.** Every disposition path ends in documentation; "not reasonable and appropriate" without the documented why-not is non-compliance [CFR-45-164-Subpart-C §164.306(d)(3)].
- **The provider's SOC 2 report is inherited evidence for facility controls only** — overlap, not equivalence; see `industries/saas-technology.md`.
- **PL 116-321 recognized security practices are penalty/audit mitigation, not immunity** [PL-116-321].
