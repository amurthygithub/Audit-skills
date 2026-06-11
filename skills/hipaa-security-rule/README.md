---
name: hipaa-security-rule
description: "HIPAA Security Rule — 45 CFR Part 164 Subpart C: 22 standards across administrative (§164.308), physical (§164.310), technical (§164.312), organizational (§164.314), and policies/documentation (§164.316) safeguards; the §164.306(d)(3) addressable-disposition logic; CE and BA direct liability. Apply this skill for Security Rule risk analyses, OCR-readiness assessments, BAA completeness checks, and right-sizing via §164.306(b)(2)."
category: audit-framework
risk: informational
source: "45 CFR Part 164 Subpart C (eCFR, as amended through 78 FR 34266, June 7, 2013); NIST SP 800-66 Rev. 2 (Final, Feb. 14, 2024)"
date_added: 2026-06-10
version: 0.1.0
status: draft
industries: [financial-services, healthcare, public-sector, saas-technology]
frameworks: [CFR-45-164-Subpart-C, NIST-SP-800-66-Rev2, HIPAA-Security-NPRM-2025, PL-116-321, CFR-45-102, HHS-SRA-Tool]
telemetry_contract: "telemetry/schema.json#/$defs/SkillInvocation"
tags: [hipaa, security-rule, ephi, healthcare, covered-entity, business-associate, risk-analysis, addressable, baa, ocr, safeguards, compliance]
---

# HIPAA Security Rule — hipaa-security-rule

The regulation skill for **45 CFR Part 164, Subpart C** ("Security Standards for the Protection of Electronic Protected Health Information"): 22 standards, the Required/Addressable implementation-specification machinery, and the §164.306(d)(3) decision logic that makes "addressable" mean *assess and document* — never *optional*. Serves both personas: the auditee building a defensible program (risk analysis, dispositions, BAAs) and the assessor checking OCR readiness.

## When to use

- A covered entity or business associate needs a Security Rule **risk analysis** (§164.308(a)(1)(ii)(A)) or a disposition record for the 22 addressable implementation specifications
- A hospital/provider compliance office wants an **OCR-readiness assessment** across all 22 standards
- A BA (SaaS vendor, consultant) needs a **BAA completeness check** against §164.314(a)(2)(i)(A)–(C) + §164.308(b)(3), or a program right-sized via the §164.306(b)(2) flexibility factors
- Anyone needs the exact (R)/(A) designation of a specification, the counting conventions (36 titled specs 14R/22A vs the 42-entry convention 20R/22A — always labeled), or verbatim decision logic

## When NOT to use

- Privacy Rule (Subpart E) or Breach Notification (Subpart D) mechanics — touchpoints only here
- HITRUST certification, 42 CFR Part 2, state privacy/breach law — out of scope
- SOC 2 engagement content (use `aicpa-soc-reporting`; the saas-technology view here covers evidence reuse — overlap, not equivalence)
- Executive cyber-maturity narratives (use `nist-csf-2`; it defers its healthcare industry view to its v1.0, which will reference INTO this skill for HIPAA rather than restate Subpart C facts)

## Use cases (3)

- **UC-01 — BA risk analysis and addressable dispositions** (CareSync Relay, 40-staff remote health-tech BA): 15-risk register (High 4 / Medium 6 / Low 5, house bands labeled), all 22 addressable specs dispositioned (15 implement / 3 alternative_measure / 4 not_reasonable_documented), encryption-at-rest decision *derived* from environment facts.
- **UC-02 — Hospital CE OCR-readiness assessment** (Bellbrook Regional Health, 6,000 staff, 4 facilities): 22-standard readiness matrix (14 implemented / 6 partial / 2 missing), prioritized gap register (High 2 / Medium 6 / Low 3), documentation-currency flags, NPRM pre-read with zero NPRM items in the current-law gap register.
- **UC-03 — Solo consultant BAA check + right-sized checklist** (Meridian HIT Consulting, headcount 1): finds exactly the 2 missing required BAA provisions (incident_reporting, subcontractor_flowdown), 10-item safeguard checklist with 3 items scaled via §164.306(b)(2)(i) — scaled, documented, never exempted (no small-entity exemption exists).

Every UC is seed-backed with **derivability oracles**: the tests recompute each expected number independently from `data/seeds/` (61 skill-local tests across oracle, metamorphic, adversarial, and structural suites, plus root-level lint/consistency/registry suites).

## 30-second quick start

```python
import sys, json
sys.path.insert(0, "skills/hipaa-security-rule/tests")  # stub executor

from hipaa_security_rule_stub import run_skill

payload = json.load(open("skills/hipaa-security-rule/data/seeds/uc-01-input.json"))
payload["risks"] = json.load(open("skills/hipaa-security-rule/data/seeds/uc-01-risks.json"))
payload["addressable_register"] = json.load(
    open("skills/hipaa-security-rule/data/seeds/uc-01-addressable-register.json"))

out = run_skill("UC-01", payload)
print(out["classification"])                    # -> "RISKS_15_HIGH_4"
print(out["disposition_summary"])               # -> {'implement': 15, 'alternative_measure': 3,
                                                #     'not_reasonable_documented': 4}
print(out["encryption_at_rest_disposition"])    # -> "implement" (derived, not hard-coded)
```

The stub is a deterministic reference executor — it demonstrates output structure and the documented house conventions; it does not perform an assessment.

## Two caveats that govern everything here

1. **The 2025 NPRM is PROPOSED, not law.** "HIPAA Security Rule To Strengthen the Cybersecurity of Electronic Protected Health Information," 90 FR 898 (Jan. 6, 2025, RIN 0945-AA22), is a **Proposed Rule only as of 2026-06-10** — verified at the Federal Register docket level; no final rule exists under the RIN. Every NPRM item in this skill is labeled PROPOSED, and the adversarial tests assert NPRM content never enters a current-law gap register. Re-verify before relying on this — a final rule may publish at any time.
2. **No crosswalk rows in v1.** The authoritative Security Rule → CSF → SP 800-53 mapping was removed from NIST SP 800-66r2 and lives online in the **NIST CPRT** (it targets CSF v1.1 and is intentionally broad). Row-level encoding is tracked as **SOX-638**; until then this skill points to CPRT/OLIR and asserts no mapping row.

## Industries covered (4)

- [financial-services](industries/financial-services.md) — group health plan sponsors (§164.314(b) plan-document amendments), insurers as CEs
- [healthcare](industries/healthcare.md) — hospital CE operations: workforce churn, medical devices/legacy systems vs §164.312, OCR readiness
- [public-sector](industries/public-sector.md) — state Medicaid/health agencies, hybrid entities, public-records vs the 6-year retention floor
- [saas-technology](industries/saas-technology.md) — BA direct liability, BAA flow-down, shared responsibility, SOC 2 evidence reuse (overlap, not equivalence)

## Cross-references to other skills

- `nist-csf-2` — executive maturity overlay; its healthcare industry view is deferred to its v1.0 — when it ships it will reference into this skill rather than restate Subpart C facts
- `nist-800-53-rmf` — control-catalog depth; HIPAA crosswalk deferred (SOX-638)
- `aicpa-soc-reporting` — SOC 2 report content for BAs reusing audit evidence
- `audit-workpapers` — finding format and workpaper structure for assessment outputs

## What this skill is NOT

- Not legal advice, and not a compliance certification — no checklist here is a safe harbor
- Not a Privacy Rule or Breach Notification skill (Subpart C / ePHI only)
- Not a crosswalk source in v1 (see caveat 2)
- Not a substitute for the entity's own risk analysis — §164.308(a)(1)(ii)(A) is the entity's obligation; this skill structures it

## Version history

- 0.1.0 (2026-06-10) — Initial build (SOX-572): 8 chunks, 4 industries, 3 seed-backed UCs, derivability-oracle test suite
