---
chunk_id: 07-addressable-decisions-and-evidence
parent_skill: hipaa-security-rule
topic: "The §164.306(d)(3) addressable-disposition workflow, disposition record template, and evidence catalog per safeguard family (auditee-leaning)"
load_when: "user asks whether an addressable spec can be skipped, how to document a disposition or alternative measure, or what evidence to prepare per safeguard"
---

# Chunk 07 — Addressable Decisions and Evidence

This is the auditee-leaning workflow chunk. The Security Rule's signature mechanism is the addressable implementation specification — **22 of the 36 titled specs in the Appendix A matrix are (Addressable)** (titled-spec convention; see `chunks/01 §6.2`) [CFR-45-164-Subpart-C]. "Addressable" is a *decision obligation*, never an exemption: every addressable spec ends in a documented disposition, and those disposition records are exactly what an OCR reviewer or auditor asks for first after the risk analysis.

## 1. The decision logic — §164.306(d)(3), nothing else

For each addressable specification, the entity must:

1. **Assess** whether the specification "is a reasonable and appropriate safeguard in its environment, when analyzed with reference to the likely contribution to protecting electronic protected health information"; and
2. As applicable —
   - **(A) Implement** the specification if reasonable and appropriate; **or**
   - **(B)** if implementing it is *not* reasonable and appropriate: **(1) document why** it would not be reasonable and appropriate, **and (2) implement an equivalent alternative measure** if reasonable and appropriate.

Three and only three dispositions follow (the enum used by this skill's UC fixtures):

| Disposition | When | Documentation owed |
|-------------|------|--------------------|
| `implement` | Assessment concludes reasonable and appropriate | The assessment + the implemented control |
| `alternative_measure` | Not reasonable and appropriate as specified, but an equivalent alternative is | Why-not rationale + the alternative and its equivalence |
| `not_reasonable_documented` | Neither the spec nor an alternative is reasonable and appropriate | Why-not rationale (and why no alternative is reasonable and appropriate) |

The assessment leans on the §164.306(b)(2) flexibility factors (size/complexity, technical capability, cost, risk probability/criticality) and on the risk analysis (`chunks/02`). Cost alone is a weak justification when risk criticality is high.

## 2. Procedure — the disposition workflow

1. **Enumerate** all addressable specs in scope (the full set is 22 titled (A) specs across §§164.308/310/312; the fact-sheet identifier list is canonical).
2. **Gather environment facts** per spec: systems affected, existing controls, constraints.
3. **Assess** reasonableness and appropriateness with explicit reference to the spec's likely contribution to protecting ePHI.
4. **Decide and record** one disposition per spec using the template in §3.
5. **Route documentation** into §164.316(b): written form, retained 6 years, available to implementers, reviewed periodically (cadence is the entity's documented choice — see `chunks/06 §4`).
6. **Re-assess** when the environment changes (§164.306(e) maintenance) — a disposition is dated, not permanent.

## 3. Output template — disposition record (UC-01 fixture shape)

Field names match the UC-01 seed/oracle contract exactly:

```yaml
addressable_disposition:
  spec_id: "164.312(a)(2)(iv)"            # must be one of the 22 addressable spec IDs
  name: "Encryption and decryption"
  family: technical                        # administrative | physical | technical
  decision_required: true                  # flagged for this engagement's active review
  reasonable_and_appropriate: true         # the 164.306(d)(3)(i) assessment outcome
  alternative: null                        # required (non-empty) iff disposition = alternative_measure
  justification: "Cloud-hosted ePHI at scale; provider-native volume and database encryption available at negligible cost; no compensating control offsets exposure of unencrypted storage"
  disposition: implement                   # implement | alternative_measure | not_reasonable_documented
```

Derivation rule (as implemented by the skill's reference stub): `reasonable_and_appropriate: true` → `implement`; otherwise a non-empty `alternative` → `alternative_measure`; otherwise → `not_reasonable_documented`. An `alternative_measure` record without a stated alternative is invalid. The UC-01 worked example (`use-cases/uc-01-ba-risk-analysis.md`) carries all 22 addressable specs through this template, walking the 12 `decision_required` ones in full.

## 4. Evidence catalog per safeguard family

What an auditee should have on hand, keyed to where each item is required:

| Family | Core evidence |
|--------|---------------|
| Cross-cutting (§§164.306/316) | Current risk analysis; risk-management plan; full addressable disposition register; policy set with revision history; 6-year documentation archive |
| Administrative (§164.308) | Security-official designation; access authorization and termination records; training completion (incl. management); sanction policy + application records; incident log with outcomes; backup/DR/emergency-mode plans and test artifacts; periodic evaluation reports; BAA inventory |
| Physical (§164.310) | Facility security plan; visitor/access logs; security-relevant maintenance records; workstation-use policy; media-disposition policy with sanitization/destruction certificates; asset-movement logs |
| Technical (§164.312) | Unique-ID account inventory; break-glass procedure + usage log; session-timeout and encryption configuration (or dispositions); logging configuration and review artifacts; integrity-mechanism configuration; authentication policy; transmission-encryption configuration per ePHI flow |
| Organizational (§164.314) | Executed BAAs with the (a)(2)(i)(A)-(C) provisions; subcontractor flow-down agreements; amended plan documents (group health plans) |

Evidence quality bar: **dated, attributable, and regenerable** — a screenshot with no date and no system identifier is weak; a configuration export with timestamp and source is strong.

## 5. SOC 2 evidence reuse (BAs) — overlap, not equivalence

A BA holding a SOC 2 Type II report can **reuse evidence** (access reviews, logging, change management, availability controls) for many Security Rule asks, but the frameworks are **not equivalent**: SOC 2 criteria do not map 1:1 to Subpart C specs, a SOC 2 opinion is not a HIPAA compliance determination, and HIPAA-specific artifacts — the §164.308(a)(1)(ii)(A) risk analysis, the addressable disposition register, BAA chains — have no SOC 2 counterpart. Label any reuse as overlap and keep the gap list explicit (see `aicpa-soc-reporting` for the SOC side).

## 6. Auditee preparation checklist

1. Risk analysis current and scoped to **all** ePHI (the first document requested).
2. Disposition register complete: one record per addressable spec, none blank, dates within the entity's own documented review cycle.
3. Evidence catalog (§4) mapped to the 22 standards before the request list arrives.
4. BAA chain verified down through subcontractors.
5. Documentation archive demonstrably reaches back 6 years (§164.316(b)(2)(i)).

## 7. Anti-hallucination notes for this chunk

- The disposition enum and field names above are this skill's **fixture contract** (house structure); the underlying three-way logic is regulatory — §164.306(d)(3) verbatim. Do not invent additional dispositions (e.g., "accepted risk" is not one — risk acceptance language belongs in the risk-management record, not the disposition enum).
- There are exactly **22 titled addressable specs** (11 administrative, 6 physical, 5 technical). A disposition register with any other count is wrong.
- Documenting why-not without considering an equivalent alternative measure is an **incomplete** §164.306(d)(3)(ii)(B) record — the alternative-measure question must be answered, even if the answer is "none is reasonable and appropriate."
- A SOC 2 report never substitutes for the risk analysis or the disposition register.
