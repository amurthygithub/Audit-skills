---
name: audit-category-pointer
description: "Pointer to a library of 4 specialized Audit skills — ISACA, COSO, AICPA SOC, and Audit Workpapers. Use when working on IT audit, internal controls, SOC reporting, or audit documentation tasks."
category: audit
risk: safe
source: custom
date_added: "2026-05-25"
tags: [audit, isaca, coso, aicpa, soc, itgc, sox, workpapers, compliance, governance]
---

# Audit Capability Library

This is a **pointer skill**. The 4 specialized Audit skills are stored on disk to keep your startup context minimal.

## Available skills in this category

- **isaca-audit-methodology** — ISACA CISA audit methodology, COBIT 2019 (40 objectives), ITAF standards, ITGC/ITAC testing, risk-based audit planning, 5-part observation format, maturity assessment.
- **coso-internal-controls** — COSO 2013 ICIF (17 principles, 77 points of focus), COSO 2017 ERM, SOX 404 readiness, PCAOB AS 2201 top-down approach, deficiency classification (material weakness/significant deficiency/deficiency).
- **aicpa-soc-reporting** — AICPA SOC 1/2/3 reporting, 64 TSP Section 100 criteria, CUECs/CSOCs, bridge letters, management assertions, opinion determination, SOC for Cybersecurity/Supply Chain.
- **audit-workpapers** — Audit workpaper standards (AS 1215, AU-C 230), sampling methodology (MUS/PPS, attribute, variables), evidence hierarchy, 5-part finding format, engagement completion, opinion determination.

## How to load a skill

1. Identify the skill name above matching your task.
2. Read its `SKILL.md` from the skill directory:
   - `/Users/akshaya.murthy/.config/opencode/skills/audit-category-pointer/<skill-name>/SKILL.md`
3. Follow those instructions to complete the request.

> Do not guess best practices — always read from the skill file first.

## Quick reference: Which skill to use?

| Task | Skill |
|------|-------|
| IT audit planning, COBIT assessment, ITGC/ITAC testing | isaca-audit-methodology |
| SOX 404, internal control evaluation, deficiency classification | coso-internal-controls |
| SOC 1/2/3 scoping, TSC criteria, service org reporting | aicpa-soc-reporting |
| Workpapers, sampling, evidence documentation, findings | audit-workpapers |