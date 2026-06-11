---
chunk_id: 01-scope-and-general-rules
parent_skill: hipaa-security-rule
topic: "Applicability, definitions, §164.306 general rules, Required/Addressable logic, counting conventions"
load_when: "user asks who must comply, what the Security Rule covers, Required vs Addressable, flexibility factors, or how many standards/specifications exist"
---

# Chunk 01 — Scope and General Rules

The Security Rule is 45 CFR Part 164, Subpart C: §§164.302–164.318 plus Appendix A (the standards matrix) [CFR-45-164-Subpart-C]. Statutory authority: 42 U.S.C. 1320d-2 and 1320d-4 and HITECH §13401 (Pub. L. 111-5). The text in force was last substantively amended June 7, 2013 (78 FR 34266); the original rule is 68 FR 8376 (Feb. 20, 2003), amended by the HITECH Omnibus Rule 78 FR 5566 (Jan. 25, 2013).

## 1. Applicability — §164.302

"A covered entity or business associate must comply with the applicable standards, implementation specifications, and requirements of this subpart with respect to electronic protected health information of a covered entity."

- **Regulated parties:** covered entities (health plans, health care clearinghouses, covered health care providers) **and business associates**. BAs are directly liable for Security Rule compliance since the 2013 Omnibus Rule — every obligation in Subpart C reads "covered entity or business associate."
- **Regulated data:** **ePHI only** — electronic protected health information. Paper and oral PHI are Privacy Rule (Subpart E) territory; breach notification is Subpart D. Do not attribute Subpart D/E obligations to this subpart.
- **Compliance dates (§164.318) are historical:** April 20, 2005 (April 20, 2006 for small health plans). They matter only for record-dating questions.

## 2. Definitions — §164.304 (closed list of 17 terms)

§164.304 defines exactly 17 terms: Access; Administrative safeguards; Authentication; Availability; Confidentiality; Encryption; Facility; Information system; Integrity; Malicious software; Password; Physical safeguards; Security or Security measures; Security incident; Technical safeguards; User; Workstation. Key verbatim anchors:

- **Security incident** — "the attempted or successful unauthorized access, use, disclosure, modification, or destruction of information or interference with system operations in an information system." (Attempts count.)
- **Encryption** — "the use of an algorithmic process to transform data into a form in which there is a low probability of assigning meaning without use of a confidential process or key."
- **Workstation** — "an electronic computing device, for example, a laptop or desktop computer, or any other device that performs similar functions, and electronic media stored in its immediate environment."
- **Availability** — "the property that data or information is accessible and useable upon demand by an authorized person."

"Breach" and "unsecured protected health information" are **not** defined here — they live in §164.402 (Subpart D).

## 3. General requirements — §164.306(a)

Covered entities and business associates must do four things:

1. **Ensure the confidentiality, integrity, and availability** of all ePHI the entity creates, receives, maintains, or transmits.
2. **Protect against any reasonably anticipated threats or hazards** to the security or integrity of such information.
3. **Protect against any reasonably anticipated uses or disclosures** not permitted or required under Subpart E (the Privacy Rule).
4. **Ensure compliance with this subpart by its workforce.**

"Reasonably anticipated" is the operative standard — it is what the §164.308(a)(1)(ii)(A) risk analysis exists to establish (see `chunks/02-risk-analysis-and-management.md`).

## 4. Flexibility of approach — §164.306(b)

Entities "may use any security measures" that reasonably and appropriately implement the standards and specifications (§164.306(b)(1)). In deciding *which* measures, they **must** take into account four factors (§164.306(b)(2)):

| # | Factor |
|---|--------|
| i | The size, complexity, and capabilities of the covered entity or business associate |
| ii | The entity's technical infrastructure, hardware, and software security capabilities |
| iii | The costs of security measures |
| iv | The probability and criticality of potential risks to ePHI |

Flexibility governs **how**, never **whether**. There is no small-entity exemption: a solo-practitioner BA and a 6,000-staff hospital answer to the same 22 standards, scaled through these factors. Document the factor relied on whenever a safeguard is scaled (the UC-03 worked example does this per checklist item).

## 5. Required vs Addressable — §164.306(d)

Implementation specifications are either **(Required)** or **(Addressable)** — the designation appears in parentheses after each specification's title (§164.306(d)(1)).

- **Required (§164.306(d)(2)):** the entity "must implement the implementation specifications."
- **Addressable (§164.306(d)(3)):** the entity must —
  1. **Assess** whether the specification "is a reasonable and appropriate safeguard in its environment, when analyzed with reference to the likely contribution to protecting electronic protected health information"; and
  2. As applicable: **(A) implement** it if reasonable and appropriate; **or (B)** if not reasonable and appropriate — **(1) document why** it would not be reasonable and appropriate to implement, **and (2) implement an equivalent alternative measure** if reasonable and appropriate.

**Addressable never means optional.** Every addressable specification ends in a documented disposition — implement, alternative measure, or documented-not-reasonable. The full disposition workflow, record template, and evidence expectations are in `chunks/07-addressable-decisions-and-evidence.md`.

**Maintenance (§164.306(e)):** security measures must be reviewed and modified "as needed to continue provision of reasonable and appropriate protection," with documentation updated per §164.316(b)(2)(iii). Compliance is continuous, not a one-time project.

## 6. The Subpart C map and counting conventions

### 6.1 Standards: 22 total

| Section | Family | Standards | Titled specs | Required | Addressable |
|---------|--------|-----------|--------------|----------|-------------|
| §164.308 | Administrative safeguards | 9 | 21 | 10 | 11 |
| §164.310 | Physical safeguards | 4 | 8 | 2 | 6 |
| §164.312 | Technical safeguards | 5 | 7 | 2 | 5 |
| §164.314 | Organizational requirements | 2 | (specs designated "(Required)" inline) | — | — |
| §164.316 | Policies and procedures; documentation | 2 | 3 (documentation) | 3 | 0 |
| **Total** | | **22** | | | |

### 6.2 The Appendix A matrix and the two counting conventions

Appendix A to Subpart C covers the three safeguard families only (§§164.308/310/312): **18 standards and 36 titled implementation specifications — 14 Required / 22 Addressable** (the titled-spec convention, used throughout this skill unless stated otherwise).

The widely cited "**42 implementation specifications (20 R / 22 A)**" uses an alternative convention: the matrix prints an (R) entry in the specifications column for the **6 standards that have no separately titled specs** — Assigned security responsibility (§164.308(a)(2)), Evaluation (§164.308(a)(8)), Workstation use (§164.310(b)), Workstation security (§164.310(c)), Audit controls (§164.312(b)), and Person or entity authentication (§164.312(d)) — and counts those entries as specifications. Both conventions are defensible; **always label which one a count uses and never mix them**.

### 6.3 Source-rendering artifacts (so verification greps do not mislead)

- §164.308(b)(1) (Business associate contracts and other arrangements) does **not** carry the "Standard:" prefix in the body text — a naive `Standard:` grep finds 8 administrative standards, not 9. Appendix A lists it as the 9th.
- In the eCFR rendering of the Appendix A matrix, the "(A)" for *Workforce clearance procedure* is dropped/merged in its table cell. The regulatory text controls: §164.308(a)(3)(ii)(B) is explicitly "(Addressable)".
- The matrix legend ("(R) = Required, (A) = Addressable") adds one stray (R) and (A) to any naive grep of the appendix.

## 7. Crosswalks: where mappings live (none encoded here)

This skill encodes **no crosswalk rows**. The authoritative mapping (Security Rule standards/specs → NIST CSF subcategories → SP 800-53r5 controls) was removed from SP 800-66r2 and placed online in the NIST Cybersecurity and Privacy Reference Tool (CPRT) — per Appendix D of [NIST-SP-800-66-Rev2]. That CPRT mapping targets **CSF v1.1** and is "intentionally broad," covering subcategories that align both directly and indirectly; never claim an official SP 800-66r2 mapping to CSF 2.0. Row-level extraction and encoding is tracked separately (SOX-638). Obtain mappings from CPRT or the NIST OLIR program.

## 8. Anti-hallucination notes for this chunk

- 22 standards total; 9/4/5/2/2 by family. Titled specs 21/8/7 with R/A splits 10-11 / 2-6 / 2-5. Matrix: 18 standards, 36 titled specs (14 R / 22 A); 42-entry convention = 20 R / 22 A. Label the convention every time.
- The §164.304 definition list is closed at 17 terms.
- §164.318 dates are historical only; do not present them as current deadlines.
- BAs are directly regulated — do not describe Subpart C as binding CEs only.
