---
uc_id: UC-03
title: "Solo HIT consultant BA checks a proposed BAA against the §164.314(a)(2)(i) required provisions and builds a right-sized 10-item safeguard checklist (3 items scaled via §164.306(b)(2) — never exempted)"
industries: [healthcare, saas-technology]
frameworks: [CFR-45-164-Subpart-C, NIST-SP-800-66-Rev2, HHS-SRA-Tool]
inputs:
  org: "Meridian HIT Consulting — fictional solo business associate consultant (headcount 1); systems: laptop, SaaS EHR access, email, cloud storage"
  baa_terms: "4 proposed BAA clauses (data/seeds/uc-03-baa-terms.json); required-provision set per 164.314(a)(2)(i)(A)-(C) plus 164.308(b)(3)"
  as_of_date: "2026-06-01"
procedure:
  - "chunks/06-organizational-and-documentation.md — Check the proposed BAA against the required provisions: comply with Subpart C (164.314(a)(2)(i)(A)); subcontractor flow-down per 164.308(b)(2) (164.314(a)(2)(i)(B)); security-incident reporting including 164.410 breaches (164.314(a)(2)(i)(C)); written contract (164.308(b)(3))."
  - "chunks/01-scope-and-general-rules.md — Apply the §164.306(b)(2) flexibility factors to right-size the safeguard program: size/complexity/capabilities, technical infrastructure, costs, probability and criticality of risks. Flexibility scales the HOW, never the WHETHER."
  - "chunks/07-addressable-decisions-and-evidence.md — Document the implement decision for laptop encryption (164.312(a)(2)(iv) is addressable — the decision record is the evidence)."
  - "SKILL.md §4 (decision logic) — required-provision completeness check; SKILL.md §5 (procedure templates) — populate the per-system checklist template."
expected_outputs:
  classification: "BAA_MISSING_2"
  baa_check:
    present_provisions: [comply_with_subpart, written_contract]
    missing_provisions: [incident_reporting, subcontractor_flowdown]
  checklist_summary: { items: 10, scaled_down: 3 }
oracle:
  - "missing_provisions recomputed from the clause seed vs the regulatory required set == exactly [incident_reporting, subcontractor_flowdown] (the 2 seeded omissions)"
  - "the required-provision set == {comply_with_subpart, subcontractor_flowdown, incident_reporting, written_contract} (164.314(a)(2)(i)(A)-(C) + 164.308(b)(3))"
  - "every checklist cfr_cite exists in the fact-sheet identifier list — no fabricated citations"
  - "checklist foots: 10 items, 3 scaled_down; every scaled_down item carries a 164.306(b)(2)(i) scaling rationale"
data_refs:
  - data/seeds/uc-03-input.json
  - data/seeds/uc-03-baa-terms.json
  - data/seeds/uc-03-expected.json
tests:
  - tests/test_hipaa_security_rule_oracle.py::test_uc_03_oracle
  - tests/test_hipaa_security_rule_metamorphic.py::test_uc03_clause_order_invariance
  - tests/test_hipaa_security_rule_adversarial.py::test_uc03_complete_baa_no_missing
  - tests/test_hipaa_security_rule_adversarial.py::test_uc03_unknown_system_contributes_nothing
token_baseline: "not yet measured — see telemetry/baseline.md"
status: active
---

# UC-03 — Solo consultant BAA check and right-sized safeguard checklist (Meridian HIT Consulting)

## §1 Context and persona

**Meridian HIT Consulting** is a fictional solo health-IT consultant — one person, a laptop, SaaS EHR access granted by clients, email, and cloud storage. A new hospital client sent a draft business associate agreement, and Meridian needs two things: (1) does the BAA contain everything the Security Rule requires, and (2) what does a defensible Security Rule program look like at headcount 1?

The Security Rule applies to Meridian in full. **There is no small-entity exemption** — §164.302 binds every covered entity and business associate. What the rule offers instead is §164.306(b) flexibility of approach: the same standards, implemented in a way that fits "the size, complexity, and capabilities" of the organization. Flexibility scales the HOW; Required specifications stay required at every size.

## §2 BAA completeness check — 2 of 4 required provisions missing

The contract required by §164.308(b)(3) (written contract or other arrangement, Required) must provide that the business associate will [CFR-45-164-Subpart-C §164.314(a)(2)(i)]:

| Provision key | Source | What the clause must say | In draft? |
|---------------|--------|--------------------------|-----------|
| comply_with_subpart | 164.314(a)(2)(i)(A) | BA will comply with the applicable requirements of Subpart C | yes (C-1) |
| subcontractor_flowdown | 164.314(a)(2)(i)(B) | per 164.308(b)(2), subcontractors that create, receive, maintain, or transmit ePHI agree to the same requirements via a compliant contract | **missing** |
| incident_reporting | 164.314(a)(2)(i)(C) | BA reports to the CE any security incident it becomes aware of, including breaches of unsecured PHI as required by §164.410 | **missing** |
| written_contract | 164.308(b)(3) | the assurances are documented in a written contract or other arrangement | yes (C-2) |

**Result: `missing_provisions = [incident_reporting, subcontractor_flowdown]`** — exactly the two seeded omissions, recomputed by the oracle from the clause list, never echoed. The draft's other clauses (C-3 permitted uses, C-4 return/destruction at termination) are common BAA terms rooted in the Privacy Rule's contract requirements — fine to keep, but they are not part of the Subpart C required set this check tests.

Even a solo consultant needs the flow-down clause: if Meridian ever hands ePHI to a subcontractor (a transcription service, a backup vendor acting on its behalf), §164.308(b)(2) makes Meridian responsible for obtaining the same satisfactory assurances downstream.

## §3 The right-sized 10-item safeguard checklist

Built per system from the seed (`laptop`, `saas_ehr_access`, `email`, `cloud_storage`) plus a base set every BA needs. **10 items, 3 of them `scaled_down`** via the §164.306(b)(2)(i) size factor — scaled, documented, never skipped:

| # | CFR cite | Action | Scaled? |
|---|----------|--------|---------|
| 1 | 164.308(a)(1)(ii)(A) | Conduct and document a risk analysis covering every system touching ePHI | no |
| 2 | 164.308(a)(2) | Designate a security official | **yes** — size factor 164.306(b)(2)(i): the solo practitioner serves as the security official; designation is documented, not delegated |
| 3 | 164.308(a)(5) | Complete and document annual security awareness training | **yes** — size factor 164.306(b)(2)(i): a formal multi-role training program is scaled to documented annual self-administered training |
| 4 | 164.316(b)(2)(i) | Retain all Subpart C documentation for 6 years | no |
| 5 | 164.310(c) | Physically secure the workstation; auto-lock screen; full-disk encryption | no |
| 6 | 164.312(a)(2)(iv) | Encrypt local storage (addressable — document the implement decision) | no |
| 7 | 164.308(a)(4) | Limit EHR access to the minimum accounts and roles the engagement requires | no |
| 8 | 164.312(d) | Authenticate every EHR session under the consultant's own identity — enable MFA where the EHR offers it (good practice; an MFA mandate is NPRM-PROPOSED, not current Subpart C) | no |
| 9 | 164.312(e)(1) | Use encrypted transmission for any message carrying ePHI | no |
| 10 | 164.308(a)(7)(ii)(A) | Maintain retrievable exact copies of any ePHI the practice stores | **yes** — size factor 164.306(b)(2)(i): provider-managed versioned storage satisfies the backup requirement for a solo practice |

Note what scaling does and does not do: item 1 (risk analysis, Required) and item 4 (6-year retention, Required) are **not scaled** — Required specifications carry no disposition flexibility. Items 2, 3, and 10 keep the full obligation; only the implementation form shrinks to fit a one-person practice, and each scaled item carries its documented §164.306(b)(2)(i) rationale. Item 6 is the addressable-spec pattern in miniature: encryption of the laptop is addressable as written, and the documented implement decision is the compliance artifact.

## §4 Oracle — every number is derivable

`tests/test_hipaa_security_rule_oracle.py::test_uc_03_oracle` recomputes independently from the seeds: the required-provision set is asserted to be exactly the regulatory four; `missing_provisions` is re-derived from the clause list (== `[incident_reporting, subcontractor_flowdown]`); every checklist `cfr_cite` must exist in the fact sheet §0 identifier list; the checklist foots to 10 items / 3 scaled_down, and every scaled item must carry a scaling rationale. Metamorphic: clause order never changes the result. Adversarial: a BAA with all four provisions reports nothing missing; an unrecognized system contributes zero checklist items (the base 4 remain — nothing fabricated).

## §5 Anti-hallucination

- **Meridian HIT Consulting is fictional**; the seeds are the tested fixture.
- **No "small entities are exempt" claim — no such exemption exists.** §164.306(b)(2) flexibility scales implementation; it never waives a standard or a Required specification.
- **The required-provision set checked here is the Subpart C set** (§164.314(a)(2)(i)(A)–(C) + §164.308(b)(3)). Privacy Rule BAA content (§164.504(e)) is out of this skill's scope — the draft's permitted-uses and return/destroy clauses belong to that regime.
- **"Other arrangements" (§164.314(a)(2)(ii)) exist** for government entities meeting §164.504(e)(3) — this UC checks the contract path only.
- **The 10-item checklist is an engagement work product, not a safe harbor** — completing it does not certify compliance; the risk analysis (item 1) drives everything else.
