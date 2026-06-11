---
chunk_id: 09-crosswalk
parent_skill: nist-800-53-rmf
topic: "Crosswalk to Other Frameworks (SOC 2 / ISO 27001 / HIPAA / PCI / CSF / CMMC / CJIS v6.0 / IRS-1075)"
load_when: "user asks to map a non-federal framework to 800-53 or vice versa"
---

# Chunk 09 — Crosswalk to Other Frameworks

## Procedure

The skill ships a curated crosswalk in `data/crosswalks/soc2-to-800-53-mod.json` (a representative sample, not a complete mapping). Each row maps a control ID to a target framework's clause. **Always verify the crosswalk** against the current authoritative mapping:

- AICPA SOC 2 → 800-53 mapping (per AICPA TSC appendix — 800-53 Rev 5 does not include a cross-reference appendix; use the AICPA-curated TSC to 800-53 mapping)
- ISO 27001:2022 Annex A → 800-53 published mappings
- PCI DSS v4.0 → 800-53 cloud-computing guidance
- HIPAA Security Rule → NIST 800-66 Rev 2
- NIST CSF 2.0 → 800-53 mappings (CSF is outcome-oriented; 800-53 is control-oriented)

## Internal cross-references (other skills in this library)

| Skill | Relationship |
|-------|--------------|
| `isaca-audit-methodology` | ITGC testing underpins many 800-53 controls; COBIT 2019 maps to APO/BAI/DSS/MEA objectives; ISACA's risk-based planning is the engagement shell that wraps 800-53 testing |
| `coso-internal-controls` | COSO Principle 12 (policies & procedures) ↔ 800-53 PM family; deficiency classification parallels PCAOB MW/SD/D |
| `aicpa-soc-reporting` | SOC 2 TSC CC1–CC9 maps to 800-53 AC, AT, AU, CM, IR, RA, etc.; SOC for Service Organizations ↔ FedRAMP SSP narrative style |
| `audit-workpapers` | AS 1215 workpaper standards apply to SAR documentation; AS 1105 evidence hierarchy applies to 800-53A assessment evidence |

## External cross-references

| External | How 800-53 maps |
|----------|-----------------|
| AICPA TSC 2017 (SOC 2) | CC1–CC9 ↔ 800-53 AC, AT, CM, IA, PM, SI; AICPA "Trust Services Criteria to 800-53" mapping |
| ISO 27001:2022 | Annex A controls ↔ 800-53 families; 93 Annex A vs ~1,000+ 800-53 — 800-53 is more granular |
| PCI DSS v4.0 | PCI's 12 requirements ↔ 800-53 families; cloud-computing guidance references 800-53 |
| HIPAA Security Rule | 45 CFR 164.308–164.316 ↔ 800-53 (108 controls incl. AC, AT, AU, CP, IR, MP, PE, PS, RA, SC, SI families); authoritative element-level rows in the NIST CPRT (SP 800-66 Rev 2 OLIR sets) |
| NIST CSF 2.0 | Govern/Identify/Protect/Detect/Respond/Recover ↔ 800-53 families; CSF is outcome-oriented, 800-53 is control-oriented |
| ISO 27701 | Privacy extension ↔ 800-53 PT family (Rev 5) |
| FedRAMP Rev 5 | FedRAMP defines the cloud authorization overlay; uses 800-53 Rev 5 baselines |
| SOC for Cybersecurity | AICPA's cybersecurity examination framework; uses 2017 TSC as criteria |
| CMMC 2.0 | DoD's contractor cybersecurity model; maps to 800-171 (which references 800-53) |
| CJIS Security Policy v6.0 | Criminal Justice Information Services (CJIS) Security Policy maps partially to 800-53 AC, AU, IA, IR, PE, SC families (especially for law enforcement systems). Consult CJIS Security Policy for criminal justice information systems. [CJIS-v6.0] |
| IRS Pub 1075 | IRS Publication 1075 (Tax Information Security Guidelines for Federal, State, and Local Agencies) maps to 800-53 controls for tax information systems receiving, processing, storing, or transmitting FTI (Federal Tax Information). Consult IRS Pub 1075 for tax information systems. [IRS-Pub-1075] |

## SOC 2 → 800-53 Moderate typical mapping

In production use, expect:

- **~8% overlap** (27 of ~325 controls) in the seed crosswalk at `data/crosswalks/soc2-to-800-53-mod.json`, which is a representative curated sample. Production crosswalks using the full AICPA TSC-to-800-53 mapping from authoritative sources may yield different overlap percentages. Always verify against the current AICPA TSC appendix.
- A **representative 93-record gap register** (81 'gap' + 12 'strengthen' dispositions — computed from the shipped seeds, not the complete Moderate gap set). Gap categories:
  - **Privacy controls** (PT family, Rev 5).
  - **Supply chain risk management** (SR family, Rev 5).
  - **Program management** (PM family) — partial overlap.
  - **Specific enhancements** (e.g., AC-2(11) usage conditions, AC-2(13) account disable for high-risk users).
  - **Operational depth** (e.g., SI-4(2) automated tools, IR-4(1) automated IR).

The skill ships crosswalk data at `data/crosswalks/soc2-to-800-53-mod.json` (curated sample), `data/seeds/hipaa-to-800-53.json` (COMPLETE: 68 Security Rule elements -> 279 OLIR informative-reference rows -> 108 unique 800-53 Rev 5.1.1 controls, generated from the NIST CPRT extraction by `data/generators/gen_hipaa_crosswalk.py`; no exact/partial strength ratings — the OLIR source carries none), `data/seeds/iso27001-2022-to-800-53.json`, and `data/seeds/pci-to-800-53.json`.

## Anti-hallucination note

Always verify crosswalks against the current authoritative source. The mappings in `data/crosswalks/` are curated; treat them as starting points, not as definitive. The AICPA "Trust Services Criteria to NIST 800-53" appendix is the authoritative SOC 2 crosswalk; the FedRAMP PMO publishes cloud-specific overlays.

## Citations in this chunk

- `[SOC-2-TSC-2017]` — AICPA TSC to 800-53 mapping (authoritative crosswalk)
- `[NIST-SP-800-66-Rev2]` — HIPAA crosswalk
- `[SOC-2-TSC-2017]` — AICPA TSC

See `## 10. References & Citation Manifest` in SKILL.md.
