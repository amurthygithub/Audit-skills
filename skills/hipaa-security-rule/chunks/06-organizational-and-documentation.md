---
chunk_id: 06-organizational-and-documentation
parent_skill: hipaa-security-rule
topic: "§164.314 organizational requirements (BAA content, group health plans) and §164.316 policies, procedures, and documentation (6-year retention)"
load_when: "user asks about BAA required provisions, subcontractor flow-down, group health plan requirements, policy documentation, or the 6-year retention rule"
---

# Chunk 06 — Organizational Requirements and Documentation

Two sections close out Subpart C's requirements [CFR-45-164-Subpart-C]: §164.314 (**2 standards** — organizational requirements, with implementation specifications designated "(Required)" inline) and §164.316 (**2 standards** — policies and procedures, and documentation, the latter with **3 Required specs**). Together they are the paper spine of the rule: what contracts must say and what records must exist.

## 1. Business associate contracts or other arrangements — §164.314(a)(1)

The contract or other arrangement required by §164.308(b)(3) must meet §164.314(a)(2)(i), (ii), or (iii), as applicable.

### 1.1 Required BAA provisions — §164.314(a)(2)(i)

The contract must provide that the business associate will:

| Provision | Cite | Content |
|-----------|------|---------|
| (A) Comply | §164.314(a)(2)(i)(A) | "Comply with the applicable requirements of this subpart" — the BA takes on Subpart C directly |
| (B) Subcontractor flow-down | §164.314(a)(2)(i)(B) | In accordance with §164.308(b)(2), ensure subcontractors that create, receive, maintain, or transmit ePHI on the BA's behalf "agree to comply with the applicable requirements of this subpart" via a compliant contract or arrangement |
| (C) Incident reporting | §164.314(a)(2)(i)(C) | "Report to the covered entity any security incident of which it becomes aware, including breaches of unsecured protected health information as required by § 164.410" (the §164.410 mechanics are Subpart D — pointer only) |

A complete BAA check therefore tests **four** things: the three provisions above **plus** the existence of the written contract or other arrangement itself (§164.308(b)(3), Required). The UC-03 worked example (`use-cases/uc-03-baa-and-checklist.md`) runs exactly this check against a clause list with seeded omissions.

### 1.2 Other arrangements and subcontractors

- **Other arrangements (§164.314(a)(2)(ii)):** a CE complies if an arrangement per §164.504(e)(3) is in place (e.g., between governmental entities).
- **Subcontractor contracts (§164.314(a)(2)(iii)):** the (a)(2)(i)/(ii) requirements apply to BA-subcontractor contracts "in the same manner" as to CE-BA contracts — the chain extends all the way down, each link holding the satisfactory assurances for the next.

### 1.3 Output template — BAA provision checklist

```yaml
baa_check:
  agreement: "<counterparty / date>"
  provisions:
    - {cite: "164.308(b)(3)", provision: written_contract, present: true}
    - {cite: "164.314(a)(2)(i)(A)", provision: comply_with_subpart, present: true}
    - {cite: "164.314(a)(2)(i)(B)", provision: subcontractor_flowdown, present: false}
    - {cite: "164.314(a)(2)(i)(C)", provision: incident_reporting, present: true}
  missing: ["subcontractor_flowdown"]
```

## 2. Requirements for group health plans — §164.314(b)

Unless the only ePHI disclosed to a plan sponsor is summary/enrollment information under §164.504(f)(1)(ii)-(iii) or disclosed per a §164.508 authorization, a **group health plan must ensure its plan documents** provide that the sponsor will reasonably and appropriately safeguard ePHI it handles for the plan. The (Required) implementation specifications — §164.314(b)(2)(i)-(iv) — demand plan-document amendments obligating the sponsor to:

1. Implement administrative, physical, and technical safeguards that reasonably and appropriately protect the confidentiality, integrity, and availability of the plan's ePHI;
2. Ensure the §164.504(f)(2)(iii) adequate separation (plan vs. sponsor) is supported by reasonable and appropriate security measures;
3. Ensure any agent receiving the information agrees to implement reasonable and appropriate security measures; and
4. Report to the group health plan any security incident of which it becomes aware.

This standard is the one most often missed in non-healthcare organizations — any employer sponsoring a self-insured plan can be in scope (see `industries/financial-services.md`).

## 3. Policies and procedures — §164.316(a)

Implement reasonable and appropriate policies and procedures to comply with Subpart C, "taking into account those factors specified in § 164.306(b)(2)(i), (ii), (iii), and (iv)" — the flexibility factors reach the paperwork too. The standard "is not to be construed to permit or excuse an action that violates any other" requirement, and policies may change at any time **provided the changes are documented and implemented** in accordance with the subpart.

## 4. Documentation — §164.316(b)

Maintain policies and procedures in **written (which may be electronic) form**, and keep a written record of any action, activity, or assessment the subpart requires to be documented (risk analyses, dispositions, incident outcomes, training records, evaluations).

| Spec | Title | Designation | Requirement |
|------|-------|-------------|-------------|
| §164.316(b)(2)(i) | Time limit | (Required) | **Retain 6 years** "from the date of its creation or the date when it last was in effect, whichever is later" |
| §164.316(b)(2)(ii) | Availability | (Required) | Make documentation available to the persons responsible for implementing the procedures it covers |
| §164.316(b)(2)(iii) | Updates | (Required) | "Review documentation **periodically**, and update as needed, in response to environmental or operational changes" |

**Retention vs. review — never conflate:** 6 years is the §164.316(b)(2)(i) **retention** floor for documentation. The **review** obligation (§164.316(b)(2)(iii)) says "periodically" with **no stated cadence** — any fixed interval (e.g., the 3-year review cycle this skill's UC-02 fixtures use as a staleness threshold) is a **HOUSE CONVENTION** chosen by the engagement, never an HHS/OCR requirement. A superseded policy must still be retained 6 years from when it was last in effect.

## 5. Anti-hallucination notes for this chunk

- §164.314's implementation specifications are designated **(Required)** inline — there are no Addressable specs in the organizational standards.
- The three documentation specs are all **(Required)**: 6-year retention, availability, periodic updates (3 R / 0 A).
- The BAA content requirements are exactly §164.314(a)(2)(i)(A)-(C); breach-notification *mechanics* (§164.410 timing, content) are Subpart D and out of this skill's scope — the BAA must reference the reporting duty, nothing more is encoded here.
- Group health plan obligations attach to **plan documents**, not a BAA — the sponsor is not the plan's business associate.
- Do not present any fixed policy-review interval as regulatory text.
