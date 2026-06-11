---
name: audit-category-pointer
description: "Pointer to a library of 9 specialized audit/compliance skills — ISACA, COSO, AICPA SOC, Audit Workpapers, NIST 800-53/RMF, NIST CSF 2.0, HIPAA Security Rule, PCI DSS, and SOX §302 disclosure controls. Use when working on IT audit, internal controls, SOC reporting, audit documentation, federal control baselines, cybersecurity maturity, or HIPAA security, PCI DSS payment-security, or SOX §302 disclosure-controls certification tasks."
category: audit
risk: safe
source: custom
date_added: "2026-05-25"
tags: [audit, isaca, coso, aicpa, soc, itgc, sox, workpapers, compliance, governance, nist, 800-53, rmf, fedramp, csf, hipaa, security-rule]
---

# Audit Capability Library

This is a **pointer skill**. The 9 specialized skills are stored on disk to keep your startup
context minimal. Counts and framework facts live in each skill (verified against live
sources at its G4.5 gate) — this pointer deliberately repeats none of them.

## Available skills in this category

- **isaca-audit-methodology** — ISACA CISA audit methodology, COBIT 2019, ITAF (5th Edition), ITGC/ITAC testing, risk-based audit planning, maturity assessment.
- **coso-internal-controls** — COSO 2013 ICIF and 2017 ERM, SOX 404 readiness, PCAOB AS 2201 top-down approach, deficiency classification (MW/SD/D), walkthroughs, RCM.
- **aicpa-soc-reporting** — SOC 1/2/3 engagements, Trust Services Criteria (TSP §100), CUECs/CSOCs, bridge letters, management assertions, opinion determination.
- **audit-workpapers** — workpaper standards (PCAOB AS 1215, AU-C 230, ISA 230), evidence hierarchy, sampling (MUS/attribute/variables), finding formats, engagement completion.
- **nist-800-53-rmf** — NIST SP 800-53 Rev 5 control baselines, SP 800-37 RMF steps, FIPS 199 categorization, FedRAMP context, SOC 2/ISO/PCI/HIPAA crosswalks, ATO artifacts.
- **nist-csf-2** — NIST CSF 2.0 organizational profiles, tiers, gap analysis, board-level maturity reporting, crosswalks to 800-53/ISO/SOC 2/CMMC.
- **hipaa-security-rule** — 45 CFR Part 164 Subpart C safeguards, required-vs-addressable dispositions, risk analysis, BAA requirements, OCR readiness, enforcement and (proposed) NPRM context.
- **pci-dss-assessment** — PCI DSS v4.0.1 scoping and segmentation, SAQ selection, ROC/AOC validation, defined-vs-customized approach, compensating controls, QSA workflow.
- **sox-302-disclosure-controls** — SOX §302 disclosure controls & procedures (DC&P) certification, DC&P-vs-ICFR boundary, 302-vs-404, the 6-element officer certification, disclosure committee and sub-certification cascade.

## How to load a skill

1. Identify the skill name above matching your task.
2. Read `skills/<skill-name>/SKILL.md` (the router); load the chunks its §11 routing table
   selects for your intent. In an installed environment, read the skill's `SKILL.md` from
   wherever this library was installed.
3. Follow those instructions to complete the request.

> Do not guess best practices — always read from the skill file first.

## Quick reference: Which skill to use?

| Task | Skill |
|------|-------|
| IT audit planning, COBIT assessment, ITGC/ITAC testing | isaca-audit-methodology |
| SOX 404, internal control evaluation, deficiency classification | coso-internal-controls |
| SOC 1/2/3 scoping, TSC criteria, service org reporting | aicpa-soc-reporting |
| Workpapers, sampling, evidence documentation, findings | audit-workpapers |
| FIPS-199 categorization, 800-53 baselines, ATO/POA&M, FedRAMP | nist-800-53-rmf |
| Cyber maturity profiles, board reporting, framework crosswalks | nist-csf-2 |
| HIPAA safeguards, addressable decisions, BAAs, OCR readiness | hipaa-security-rule |
| PCI DSS scoping, SAQ selection, ROC/AOC, compensating controls | pci-dss-assessment |
| SOX §302 DC&P certification, disclosure committee, sub-cert cascade | sox-302-disclosure-controls |
