---
chunk_id: 08-enforcement-audit-and-nprm
parent_skill: hipaa-security-rule
topic: "OCR enforcement and penalty tiers (2025-adjusted, as-of-dated), audit readiness, recognized-security-practices mitigation, and the 2025 NPRM (PROPOSED only)"
load_when: "user asks about HIPAA fines/penalties, OCR audits or investigations, readiness assessment, or what the 2025 NPRM would change"
---

# Chunk 08 — Enforcement, Audit Readiness, and the 2025 NPRM

This is the auditor-leaning chunk: what enforcement exposure looks like today, how to run a readiness assessment, and what is on the regulatory horizon. **Everything in §5 is PROPOSED, not law.** This chunk is also the skill's most volatile content — re-verify the NPRM docket and the penalty table before relying on either (§6).

## 1. Civil monetary penalties — four culpability tiers

HHS OCR enforces the Security Rule under 45 CFR Part 160; penalty tiers are set at 45 CFR 160.404 and the dollar amounts are **adjusted annually for inflation** under 45 CFR 102.3 [CFR-45-102]. The amounts below are the **2025-adjusted maxima/minima as of 2026-06-10** — always restate the as-of date and check the current §102.3 table before quoting:

| Tier | Culpability | Min per violation | Max per violation | Calendar-year cap (per provision) |
|------|-------------|-------------------|-------------------|------------------------------------|
| 1 | Did not know (and would not have known with reasonable diligence) | $145 | $73,011 | $2,190,294 |
| 2 | Reasonable cause (not willful neglect) | $1,461 | $73,011 | $2,190,294 |
| 3 | Willful neglect, corrected within 30 days | $14,602 | $73,011 | $2,190,294 |
| 4 | Willful neglect, not corrected | $73,011 | $2,190,294 | $2,190,294 |

**2019 Notification of Enforcement Discretion:** OCR announced lower annual caps for tiers 1-3. That notification is **enforcement posture, not codified law** — the codified caps are the §102.3 amounts above. Label it accordingly whenever it comes up. Beyond money: resolution agreements with multi-year corrective action plans (CAPs) are the typical settlement shape, and state attorneys general hold parallel HITECH enforcement authority.

**Recognized security practices** (PL 116-321, approved Jan. 5, 2021) [PL-116-321]: HHS must *consider* 12 months of demonstrated recognized security practices when determining penalties, audit scope, and remedies — mitigation, not immunity. Build the demonstration file before the investigation (see `chunks/02 §5`).

## 2. What OCR asks for first

Investigation and audit document requests consistently lead with: (1) the **risk analysis** (§164.308(a)(1)(ii)(A)) and risk-management plan; (2) the **addressable disposition register** (`chunks/07`); (3) policies and procedures with revision history and the **6-year archive** (§164.316); (4) **BAA inventory** and chain; (5) training, incident, and activity-review records. The OCR audit protocol (hhs.gov; page is bot-walled to programmatic clients — cite in prose only) organizes line items along exactly these standards; this skill does not reproduce protocol line items.

## 3. Procedure — OCR readiness assessment

1. **Inventory** all 22 standards [CFR-45-164-Subpart-C] and assign each a status: `implemented | partial | missing`, with an evidence reference per standard.
2. **Test the anchors first:** risk analysis currency and scope; disposition register completeness; documentation retention.
3. **Prioritize gaps.** This skill's UC-02 fixtures use a **HOUSE CONVENTION gap-priority heuristic — not OCR methodology**: standard `missing` → High; `partial` → Medium; stale policy documentation → Low. Staleness is measured against the engagement's chosen review cycle (UC-02 uses 3 years — also a **house convention**; the rule says "periodically," §164.316(b)(2)(iii), with no cadence).
4. **Flag documentation currency:** any required record older than its last-effective retention window or missing from the 6-year archive is a finding.
5. **Check the mitigation file:** 12 months of recognized-security-practices evidence (§1).
6. **Report** with the readiness matrix below; keep current-law findings and horizon items (§5) in separate sections — never mix PROPOSED items into the gap list.

## 4. Output template — readiness matrix and gap list

```yaml
readiness_assessment:
  as_of_date: "YYYY-MM-DD"
  matrix:                      # exactly 22 rows, one per Subpart C standard
    - {standard: "164.308(a)(1)", status: implemented, evidence_ref: "WP-101"}
    - {standard: "164.308(a)(2)", status: partial, evidence_ref: "WP-102"}
  gaps:
    - standard: "164.310(d)(1)"
      status: missing
      priority: High           # HOUSE CONVENTION: missing -> High, partial -> Medium, stale-doc -> Low
      finding: "<condition vs criteria, per audit-workpapers 5-part pattern>"
  documentation_flags:
    - {document: "Security policy v1", last_review: "YYYY-MM-DD", note: "exceeds engagement review cycle (house convention)"}
```

The UC-02 worked example (`use-cases/uc-02-ocr-readiness.md`) runs this end to end for a 6,000-staff hospital CE.

## 5. The 2025 NPRM — PROPOSED ONLY

"HIPAA Security Rule To Strengthen the Cybersecurity of Electronic Protected Health Information," 90 FR 898 (Jan. 6, 2025), RIN 0945-AA22 [HIPAA-Security-NPRM-2025]. **Status verified at the Federal Register docket level on 2026-06-10: exactly one document exists under the RIN, type "Proposed Rule." No final rule exists.** Every item below is PROPOSED and may change or never take effect:

- **PROPOSED:** remove the Required/Addressable distinction — all implementation specifications required, with limited exceptions.
- **PROPOSED:** mandatory encryption of ePHI at rest and in transit.
- **PROPOSED:** mandatory multi-factor authentication.
- **PROPOSED:** vulnerability scanning and penetration testing on defined cadences.
- **PROPOSED:** technology asset inventory and network map.
- **PROPOSED:** annual compliance audits.

Headline level only by design — the Federal Register document is the source for detail. Advisory posture: current law governs today's obligations; the NPRM is a planning signal (entities already implementing encryption, MFA, and asset inventories are buying down both present risk and potential future compliance cost), never a present requirement.

## 6. Re-verification instruction (mandatory before use)

1. **NPRM status:** query the Federal Register docket (RIN 0945-AA22) for any document of type "Rule." If a final rule exists, §5's framing is obsolete — stop and escalate for a skill update.
2. **Penalty amounts:** check the current 45 CFR 102.3 Table 1 [CFR-45-102] — amounts adjust annually; the figures in §1 are the 2025-adjustment column as of 2026-06-10.

## 7. Anti-hallucination notes for this chunk

- Penalty amounts appear in this chunk **only**, always with the as-of date. Never quote them without checking §102.3 currency.
- The 2019 enforcement-discretion caps are posture, not codified law.
- No NPRM item may be stated as a current requirement — encryption and MFA mandates, audit cadences, and the end of "addressable" are all **PROPOSED** [HIPAA-Security-NPRM-2025].
- The gap-priority heuristic and the 3-year staleness threshold are **house conventions**, never OCR/HHS/NIST methodology.
- PL 116-321 mitigation requires 12 months of *demonstrated* practice — adoption on paper does not qualify, and it is not immunity [PL-116-321].
