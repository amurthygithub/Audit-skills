---
chunk_id: 02-risk-analysis-and-management
parent_skill: hipaa-security-rule
topic: "§164.308(a)(1) Security management process: risk analysis, risk management, sanction policy, activity review; SRA Tool; recognized security practices"
load_when: "user asks about HIPAA risk analysis/assessment, risk management, sanction policy, information system activity review, the SRA Tool, or PL 116-321 recognized security practices"
---

# Chunk 02 — Risk Analysis and Management

The **Security management process** standard — §164.308(a)(1)(i) [CFR-45-164-Subpart-C] — requires policies and procedures "to prevent, detect, contain, and correct security violations." It carries four implementation specifications, **all four (Required)**. This standard is the anchor of the entire rule: every addressable disposition, safeguard selection, and evaluation downstream cites the risk analysis, and an absent or stale risk analysis is the most common OCR enforcement finding.

## 1. The four Required specifications

| Spec | Title | Designation | Text (operative language) |
|------|-------|-------------|---------------------------|
| §164.308(a)(1)(ii)(A) | Risk analysis | (Required) | "Conduct an accurate and thorough assessment of the potential risks and vulnerabilities to the confidentiality, integrity, and availability of electronic protected health information held by the covered entity or business associate." |
| §164.308(a)(1)(ii)(B) | Risk management | (Required) | "Implement security measures sufficient to reduce risks and vulnerabilities to a reasonable and appropriate level to comply with § 164.306(a)." |
| §164.308(a)(1)(ii)(C) | Sanction policy | (Required) | "Apply appropriate sanctions against workforce members who fail to comply with the security policies and procedures of the covered entity or business associate." |
| §164.308(a)(1)(ii)(D) | Information system activity review | (Required) | "Implement procedures to regularly review records of information system activity, such as audit logs, access reports, and security incident tracking reports." |

Distinction that auditors probe: §164.312(b) (Audit controls) requires the *mechanisms* that record activity; §164.308(a)(1)(ii)(D) requires the *procedures and practice of reviewing* what those mechanisms record. Logging without review fails (D); review without logging is impossible. See `chunks/05-technical-safeguards.md`.

## 2. Procedure — risk analysis

"Accurate and thorough" means scoped to **all ePHI the entity creates, receives, maintains, or transmits** — every system, device, medium, and flow, not just the EHR. NIST SP 800-66 Rev 2 [NIST-SP-800-66-Rev2] describes the risk-assessment and risk-management activities as **cyclical and iterative** — performed initially and repeated as the environment and operations change, not a one-time artifact.

1. **Scope and inventory.** Enumerate where ePHI lives and moves: applications, databases, endpoints, removable media, backups, transmissions, BAs/subcontractors.
2. **Identify threats and vulnerabilities** per asset/flow (natural, human accidental, human malicious, environmental).
3. **Assess likelihood and impact** of each threat/vulnerability pair, considering current controls.
4. **Score and rank.** The Security Rule prescribes **no scoring scale**. This skill's UC fixtures use a **HOUSE CONVENTION, not HHS/OCR/NIST methodology**: likelihood 1-3 × impact 1-3, bands Low ≤2 / Medium 3-4 / High ≥6. Label it as the engagement's own convention in every deliverable.
5. **Document** results (the risk analysis is itself documentation subject to §164.316(b) — written form, retained 6 years, reviewed periodically).
6. **Feed risk management** (§164.308(a)(1)(ii)(B)): select and implement measures that reduce identified risks to a reasonable and appropriate level, using the §164.306(b)(2) flexibility factors; record residual-risk acceptance.

For small and medium entities, the HHS ONC/OCR **Security Risk Assessment (SRA) Tool** [HHS-SRA-Tool] operationalizes this procedure as a guided, downloadable questionnaire; using it is optional and does not by itself guarantee compliance.

## 3. Output template — risk register (house-convention scoring, labeled)

```yaml
risk_register:
  as_of_date: "YYYY-MM-DD"
  scale_note: "HOUSE CONVENTION: score = likelihood (1-3) x impact (1-3); bands Low <=2, Medium 3-4, High >=6. Not an HHS/OCR/NIST scale."
  risks:
    - id: R-01
      asset: "<system or data flow holding ePHI>"
      threat: "<threat event>"
      vulnerability: "<weakness exploited>"
      likelihood: 2          # 1-3
      impact: 3              # 1-3
      score: 6               # likelihood x impact
      band: High
      existing_controls: ["<control>"]
      treatment: "<risk-management action per 164.308(a)(1)(ii)(B)>"
  summary:
    total: 0
    by_band: {High: 0, Medium: 0, Low: 0}
```

The UC-01 worked example (`use-cases/uc-01-ba-risk-analysis.md`) walks a 15-risk register for a 40-FTE SaaS BA end to end with this template.

## 4. Sanction policy and activity review in practice

- **Sanction policy (C):** a written, graduated policy applied to workforce members; evidence is the policy plus records of application (or an attestation that no violations occurred in the period). It must cover *security* policy violations, not just privacy.
- **Activity review (D):** define which records are reviewed (audit logs, access reports, incident tracking), at what frequency, by whom, and what triggers escalation. "Regularly" is the rule's word — the cadence is the entity's documented, risk-based choice. Evidence: review procedures plus dated review artifacts.

## 5. Recognized security practices — PL 116-321

Public Law 116-321 (**approved January 5, 2021**; adds HITECH §13412, 42 U.S.C. 17941) [PL-116-321] requires HHS to **consider** whether the entity had "recognized security practices" in place **for the previous 12 months** when making certain penalty, audit, and remedy determinations. Key framing:

- **Mitigation, not immunity** — it can reduce penalties and audit scrutiny; it is not a safe harbor and not a compliance substitute.
- Recognized security practices include the NIST Cybersecurity Framework approaches and §405(d) program practices; the entity chooses and must be able to **demonstrate 12 months of operation**, not a paper adoption.
- Demonstration evidence pairs naturally with the risk analysis: dated framework assessments, control-operation artifacts, board/management review records.

## 6. Anti-hallucination notes for this chunk

- All four §164.308(a)(1) specs are **(Required)** — never describe any of them as addressable.
- The 1-3 × 1-3 scoring scale and its bands are a **house convention**; the Security Rule and SP 800-66r2 prescribe no numeric scale.
- **PL 116-321 was approved January 5, 2021 — not 2020.** SP 800-66r2 footnote 9 states "January 5, 2020"; that footnote is wrong — the statute text itself says Jan. 5, 2021. Cite the statute [PL-116-321], not the footnote.
- The SRA Tool is an aid, not a certification; completing it does not constitute compliance.
- Risk analysis is not a checklist of the 22 standards — it is an assessment of risks to ePHI; the standards gap review is a separate exercise (see `chunks/08-enforcement-audit-and-nprm.md`).
