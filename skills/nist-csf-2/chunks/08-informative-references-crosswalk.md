---
chunk_id: 08-informative-references-crosswalk
parent_skill: nist-csf-2
topic: "CSF subcategory → 800-53, 800-171, ISO 27001, HIPAA Security Rule mappings"
load_when: "user asks for a crosswalk, mapping, or how CSF relates to 800-53"
---

# Chunk 08 — Informative References Crosswalk

NIST publishes an "Informative References" spreadsheet alongside CSF 2.0 that maps each of the **106** Subcategories to ~50 other frameworks and control catalogs (800-53 Rev 5.1.1, 800-53 Rev 5.2.0, 800-171 Rev 3, ISO 27001:2022 Annex A + mandatory clauses, COBIT 2019, CIS Controls v8, SOC 2 TSC 2017, PCI DSS v4.0.1, and others) [NIST-CSF-2.0 Informative References]. The mapping is **informative, not normative**: it is NIST's published view of the relationship, but an org is not required to follow any specific mapping.

## 1. What informative references are (and what they are not)

An **informative reference** in NIST parlance is a citation in the framework text that points to a related authoritative source. For CSF 2.0, NIST publishes a spreadsheet that lists, for each Subcategory, the corresponding controls in ~50 other frameworks. The published spreadsheet is the **primary source** for all CSF crosswalks.

What informative references **are**: a NIST-curated view of how a CSF Subcategory outcome relates to controls in other frameworks; a starting point for orgs that need to demonstrate coverage of multiple frameworks with one evidence base; a bridge between outcome-oriented frameworks (CSF, COBIT) and control-oriented frameworks (800-53, ISO 27001 Annex A).

What informative references **are not**: **normative** (an org can deviate with a documented rationale); **1:1** (most Subcategories map to 2-15 controls in 800-53, the 1-to-many pattern is dominant); **exhaustive** (the 50 frameworks are not all the frameworks an org might face); **authoritative for the target framework** (the CSF ↔ 800-53 mapping tells you how a Subcategory relates to 800-53; for the authoritative 800-53 control, you read 800-53 itself).

## 2. The CSF ↔ 800-53 crosswalk (representative samples)

The CSF ↔ 800-53 mapping is the most-used crosswalk in federal-adjacent engagements. The representative samples below are taken verbatim from the NIST CSF 2.0 Informative References spreadsheet (Rev 5.1.1 column), which is the authoritative source. Each Subcategory's `to_controls` list includes the complete set of 800-53 Rev 5.1.1 controls that the spreadsheet maps to it (the dominant pattern is 1-to-many, not 1-to-1).

| CSF Subcategory | 800-53 Rev 5.1.1 controls (per NIST IR spreadsheet) |
|-----------------|---------------------------------------------------|
| `GV.OC-01` (mission understood) | PM-11 |
| `GV.OC-02` (stakeholders) | PM-9, PM-18, PM-30, SR-3, SR-5, SR-6, SR-8 |
| `GV.OC-03` (legal/regulatory) | AC-01, AT-01, AU-01, CA-01, CM-01, CP-01, IA-01, IR-01, MA-01, MP-01, PE-01, PL-01, PM-01, PM-28, PS-01, PT-01, RA-01, SA-01, SC-01, SI-01, SR-01 |
| `GV.OC-04` (critical objectives) | PM-8, PM-11, PM-30(01), CP-2(8), RA-9 |
| `GV.OC-05` (outcomes org depends on) | PM-11, PM-30, RA-7, SA-9, SR-5 |
| `GV.RM-01` (objectives) | PM-9, RA-7, SR-2 |
| `GV.RM-02` (risk appetite) | PM-9 |
| `GV.RM-03` (ERM integration) | PM-3, PM-9, PM-30, RA-7, SR-2 |
| `GV.RM-04` (strategic direction) | PM-9, PM-28, PM-30, SR-2 |
| `GV.RM-05` (lines of communication) | PM-9, PM-30 |
| `GV.RM-06` (standardized method) | PM-9, PM-18, PM-28, PM-30, RA-3 |
| `GV.RM-07` (opportunities) | PM-9, PM-18, PM-28, PM-30, RA-3 |
| `GV.RR-01` (leadership accountable) | PM-2, PM-19, PM-23, PM-24, PM-29 |
| `GV.RR-02` (roles communicated) | PM-2, PM-13, PM-19, PM-23, PM-24, PM-29 |
| `GV.RR-03` (resources allocated) | PM-3 |
| `GV.RR-04` (cyber in HR practices) | PM-13, PS-1, PS-7, PS-9 |
| `GV.PO-01` (policy) | AC-01, AT-01, AU-01, CA-01, CM-01, CP-01, IA-01, IR-01, MA-01, MP-01, PE-01, PL-01, PM-01, PS-01, PT-01, RA-01, SA-01, SC-01, SI-01, SR-01 |
| `GV.PO-02` (policy reviewed) | (same as GV.PO-01) |
| `GV.OV-01` (performance reviewed) | AC-01, AT-01, AU-01, CA-01, CM-01, CP-01, IA-01, IR-01, MA-01, MP-01, PE-01, PL-01, PM-01, PM-9, PM-18, PM-30, PM-31, PS-01, PT-01, RA-01, RA-7, SA-01, SC-01, SI-01, SR-01, SR-6 |
| `GV.OV-02` (strategy reviewed) | PM-9, PM-19, PM-30, PM-31, RA-7, SR-6 |
| `GV.OV-03` (performance evaluated) | PM-4, PM-6, RA-7, SR-6 |
| `GV.SC-01` (TPRM program) | PM-30, SR-2, SR-3 |
| `GV.SC-02` (supplier roles) | SR-2, SR-3, SR-5 |
| `GV.SC-03` (C-SCRM integrated) | AC-01..SR-01, PM-9, PM-18, PM-30, PM-31, RA-3, RA-7, SR-2, SR-3 |
| `GV.SC-04` (suppliers prioritized) | RA-9, SA-9, SR-6 |
| `GV.SC-05` (contracts) | SA-4, SA-9, SR-3, SR-5, SR-6, SR-10 |
| `GV.SC-06` (planning & due diligence) | SA-4, SA-9, SR-5, SR-6 |
| `GV.SC-07` (risks through relationship) | RA-9, SA-4, SA-9, SR-3, SR-6 |
| `GV.SC-08` (suppliers in IR) | CP-1, IR-1, SA-4, SA-9, SR-2, SR-3, SR-8 |
| `GV.SC-09` (life cycle practices) | PM-9, PM-19, PM-28, PM-30, PM-31, RA-3, RA-7, SA-4, SA-9, SR-2, SR-3, SR-5, SR-6 |
| `GV.SC-10` (post-relationship) | PM-31, RA-3, RA-5, RA-7, SA-4, SA-9, SR-2, SR-3, SR-5, SR-6 |
| `ID.AM-01` (HW inventory) | CM-8, PM-5 |
| `ID.AM-08` (system life cycle) | CM-9, CM-13, MA-2, MA-6, PL-2, PM-22, PM-23, SA-3, SA-4, SA-8, SA-22, SI-12, SI-18, SR-5, SR-12 |
| `ID.RA-01` (vulnerabilities) | CA-2, CA-7, CA-8, RA-3, RA-5, SA-11(2), SA-15(7), SA-15(8), SI-4, SI-5 |
| `PR.AA-01` (identity mgmt) | AC-1, AC-2, AC-14, IA-1, IA-2, IA-3, IA-4, IA-5, IA-6, IA-7, IA-8, IA-9, IA-10, IA-11 |
| `PR.AA-03` (MFA / authenticator mgmt) | AC-7, AC-12, IA-2, IA-3, IA-5, IA-7, IA-8, IA-9, IA-10, IA-11 |
| `PR.AA-05` (access permissions) | AC-1, AC-2, AC-3, AC-5, AC-6, AC-10, AC-16, AC-17, AC-18, AC-19, AC-24, IA-13 |
| `PR.DS-01` (data-at-rest) | CA-3, CP-9, MP-8, SC-4, SC-7, SC-12, SC-13, SC-28, SC-32, SC-39, SC-43, SI-3, SI-4, SI-7 |
| `PR.PS-01` (configuration mgmt) | CM-1, CM-2, CM-3, CM-4, CM-5, CM-6, CM-7, CM-8, CM-9, CM-10, CM-11 |
| `PR.IR-01` (network segmentation) | AC-3, AC-4, SC-4, SC-5, SC-7 |
| `DE.CM-01` (network monitoring) | AC-2, AU-12, CA-7, CM-3, SC-5, SC-7, SI-4 |
| `DE.CM-09` (compute monitoring) | AC-4, AC-9, AU-12, CA-7, CM-3, CM-6, CM-10, CM-11, SC-34, SC-35, SI-4, SI-7 |
| `DE.AE-02` (event correlation) | AU-6, CA-7, IR-4, SI-4 |
| `RS.MA-01` (IR plan executed) | IR-6, IR-7, IR-8, SR-3, SR-8 |
| `RS.AN-03` (analysis performed) | AU-7, IR-4 |
| `RS.CO-02` (regulator notification) | IR-4, IR-6, IR-7, SR-3, SR-8 |
| `RS.CO-03` (info shared) | IR-4, IR-6, IR-7, SR-3, SR-8 |
| `RC.RP-01` (recovery executed) | CP-10, IR-4, IR-8 |
| `RC.CO-03` (recovery comms) | IR-4, IR-6, SR-8 |
| `RC.CO-04` (public comms) | CP-2, IR-4 |

The full mapping is many-to-many: a single 800-53 control (e.g., `AC-2`) can be referenced by multiple CSF Subcategories, and a single CSF Subcategory (e.g., `PR.AA-01`) maps to 14+ 800-53 controls per the IR spreadsheet.

## 3. The CSF ↔ 800-171 crosswalk (moderate baseline, federal-adjacent)

NIST SP 800-171 Rev 3 [NIST-SP-800-171] is the moderate-baseline control set for protecting Controlled Unclassified Information (CUI) in nonfederal systems. The CSF ↔ 800-171 mapping is similar in shape to CSF ↔ 800-53 Moderate but with 800-171's 14 control families (3xx series). 800-171 maps to CMMC 2.0 Level 2; orgs pursuing CMMC L2 use the CSF ↔ 800-171 crosswalk as the bridge.

Representative samples (the full mapping ships in `data/crosswalks/csf-to-800-171-r3.json`):

| CSF Subcategory | 800-171 Rev 3 controls (per NIST IR spreadsheet) |
|-----------------|------------------------------------------------|
| `PR.AA-01` (identity mgmt) | 03.01.01, 03.05.01, 03.05.02, 03.05.03, 03.05.04, 03.05.05, 03.05.07, 03.05.11, 03.05.12, 03.15.01 |
| `PR.AA-03` (MFA) | 03.01.11, 03.05.01, 03.05.02, 03.05.03, 03.05.04, 03.05.07, 03.05.12 |
| `PR.DS-01` (data-at-rest) | 03.08.09, 03.12.05, 03.13.01, 03.13.04, 03.13.06, 03.13.08, 03.13.10, 03.13.11, 03.14.02, 03.14.06 |
| `DE.CM-01` (network monitoring) | 03.01.01, 03.03.03, 03.04.03, 03.12.03, 03.13.01, 03.13.06, 03.14.06 |
| `RS.MA-01` (IR plan executed) | 03.06.02, 03.06.05, 03.17.03 |
| `RC.RP-01` (recovery executed) | 03.06.01, 03.06.05 |
| `GV.SC-03` (C-SCRM integrated) | 03.11.01, 03.11.04, 03.15.01, 03.17.01, 03.17.03 |

800-171 is a strict subset of 800-53 Moderate (~110 controls vs 800-53's ~325); the CSF → 800-171 mapping is therefore a strict subset of the CSF → 800-53 mapping. For orgs pursuing CMMC L2, the practical workflow is: CSF Current Profile → identify lagging Subcategories → map to 800-171 → produce the System Security Plan (SSP) for the CMMC assessment.

## 4. The CSF ↔ ISO 27001:2022 crosswalk (Annex A controls)

ISO 27001:2022 [ISO-27001-2022] introduced a new Annex A with 93 controls organized in 4 themes (Organizational, People, Physical, Technological). The CSF ↔ ISO 27001 mapping is outcome-to-control: a CSF Subcategory typically maps to 1-3 Annex A controls, and an Annex A control typically supports 1-3 CSF Subcategories.

Representative samples (the full mapping ships in `data/crosswalks/csf-to-iso27001-2022.json`):

| CSF Subcategory | ISO 27001:2022 Annex A controls (per NIST IR spreadsheet) | Notes |
|-----------------|----------------------------------------------------------|-------|
| `GV.OC-01` (mission) | Mandatory Clauses: 4.1, 6.1, 8.1, 8.2, 8.3 (no Annex A controls) | Clause-level |
| `GV.SC-04` (suppliers prioritized) | Annex A: 5.19, 5.22; Mandatory: 6.1.1, 6.1.2, 6.1.3 | Supplier relationships theme |
| `GV.PO-01` (policy) | Annex A: 5.1; Mandatory: 5.2 | Policy theme |
| `PR.AA-01` (identity mgmt) | Annex A: 5.15, 5.18, 8.2, 8.5 | Access control theme |
| `PR.AA-03` (MFA / authenticator mgmt) | Annex A: 5.15, 5.16, 5.17, 5.18, 8.5 | Authentication theme |
| `PR.DS-01` (data-at-rest) | Annex A: 5.1, 5.3, 5.10, 5.13, 5.14, 5.15, 6.1, 6.2, 6.5, 7.7, 7.10, 8.2, 8.3, 8.4, 8.7, 8.8, 8.17, 8.19, 8.22, 8.26; Mandatory: 4.2(b), 5.2 | Cryptography + information transfer |
| `PR.PS-01` (configuration mgmt) | Annex A: 8.9; Mandatory: 9.3 | Configuration mgmt |
| `DE.CM-01` (network monitoring) | Annex A: 8.16 | Monitoring activities |
| `RS.MA-01` (IR plan) | Annex A: 5.26, 5.27, 5.28 | Incident management planning |
| `RC.RP-01` (recovery executed) | Annex A: 5.26 | ICT readiness for business continuity |

ISO 27001:2022's 93 Annex A controls are far fewer than 800-53's ~325 Moderate controls. The mapping is therefore *denser* on the ISO side (each ISO control supports more CSF Subcategories on average) and *less granular* on the ISO side (ISO 27001 specifies the control outcome, not the enhancement-level implementation).

## 5. The CSF ↔ HIPAA Security Rule crosswalk (§164.308/310/312 safeguards)

**Important caveat:** The official NIST CSF 2.0 Informative References spreadsheet (the authoritative CSF crosswalk source) does **not** include the HIPAA Security Rule as a row. HIPAA mappings must therefore be **derived** rather than cited as authoritative CSF 2.0 IR. The authoritative HIPAA → 800-53 mapping is NIST SP 800-66 Rev 2, and the CSF → HIPAA mapping below is derived by chaining CSF → 800-53 (from the IR spreadsheet) and 800-53 → HIPAA (from SP 800-66 Rev 2). The rows below should be treated as a **practitioner heuristic**, not as a NIST-published crosswalk.

The HIPAA Security Rule [HIPAA-Security-Rule] specifies administrative, physical, and technical safeguards at 45 CFR §164.308, §164.310, and §164.312.

Representative samples (derived, not NIST CSF 2.0 IR):

| CSF Subcategory | HIPAA Security Rule reference (derived) | Safeguard type |
|-----------------|------------------------------------------|----------------|
| `ID.AM-01` (asset inventory) | §164.308(a)(1)(ii)(A) | Administrative (risk analysis) |
| `ID.RA-01` (vulnerabilities) | §164.308(a)(1)(ii)(A), §164.308(a)(8) | Administrative (evaluation) |
| `PR.AA-01` (identity mgmt) | §164.308(a)(4), §164.312(a)(1), §164.312(d) | Admin + Technical (personnel, access control, authentication) |
| `PR.AA-03` (MFA) | §164.312(d) | Technical (person or entity authentication) |
| `PR.DS-01` (data-at-rest) | §164.312(a)(2)(iv) | Technical (encryption/decryption) |
| `PR.IR-01` (network segmentation) | §164.312(e)(1) | Technical (transmission security) |
| `DE.CM-01` (network monitoring) | §164.308(a)(1)(ii)(D) | Administrative (information system activity review) |
| `RS.MA-01` (IR plan) | §164.308(a)(6) | Administrative (security incident procedures) |
| `RS.CO-02` (regulator notification) | §164.404 (Breach Notification Rule) | Cross-reference to BNR |
| `RC.RP-01` (recovery) | §164.308(a)(7) | Administrative (contingency plan) |
| `GV.SC-04` (supplier assessment) | §164.308(b)(1) | Administrative (business associate contracts) |

**Source caveat (repeated for emphasis):** these HIPAA rows are derived, not authoritative NIST CSF 2.0 IR. Verify each row against the source regulations (45 CFR §164.308, §164.310, §164.312) and against NIST SP 800-66 Rev 2 before relying on it for a covered-entity engagement.

The HIPAA Security Rule is healthcare-specific; the CSF mapping is meaningful for covered entities and business associates. The mapping is also useful for orgs in healthcare-adjacent industries (e.g., health tech, digital health) that handle PHI but are not strictly covered entities.

## 6. The 1-to-many nature of CSF-to-control mappings

The single most important property of the CSF-to-control crosswalks: **a single Subcategory can map to 2-15 controls in the target framework.** This is because CSF Subcategories are **outcomes** (e.g., "Identities and credentials are managed" — `PR.AA-01`) and 800-53 / ISO / HIPAA controls are **mechanisms** (specific safeguards that produce the outcome). A single outcome can require several mechanisms.

Examples of 1-to-many (per NIST IR spreadsheet, 800-53 Rev 5.1.1): `PR.AA-01` → AC-1, AC-2, AC-14, IA-1..IA-11 (14 controls, 2 families); `DE.CM-01` → AC-2, AU-12, CA-7, CM-3, SC-5, SC-7, SI-4 (7 controls, 4 families); `GV.SC-01` → PM-30, SR-2, SR-3 (3 controls, 2 families); `RC.RP-01` → CP-10, IR-4, IR-8 (3 controls, 2 families).

The reverse (1-to-1) is the exception, not the rule. When producing a crosswalk for an org, expect to see 1-to-2 to 1-to-5 mappings as the norm; flag any 1-to-1 mapping for verification (it usually means the mapping is incomplete).

**Practical consequence for the crosswalk JSON**: the curated `data/crosswalks/csf-to-*.json` files use the format `{"from_subcategory": "GV.OC-01", "to_framework": "800-53", "to_controls": ["PM-11", "PM-15"], "rationale": "..."}` — the `to_controls` is an **array**, not a scalar. The 800-53 RMF skill's `soc2-to-800-53-mod.json` uses a different format (1-to-1 control-to-control) because the SOC 2 ↔ 800-53 mapping is dominantly 1-to-1; the CSF → 800-53 mapping is dominantly 1-to-many. Any cross-skill parser consuming both formats must support both shapes.

## 7. Where the authoritative crosswalk lives

The **authoritative source** for CSF 2.0 crosswalks is the NIST CSF 2.0 Informative References spreadsheet, downloaded from `https://csrc.nist.gov/extensions/nudp/services/json/csf/download?olirids=all`. The spreadsheet is the source of truth and is updated periodically by NIST.

The JSON-format sample below is a **suggested schema** for an org that wants to import the IR spreadsheet into a tooling pipeline. It is not a NIST-published schema.

```json
{
  "from_subcategory": "GV.OC-01",
  "to_framework": "800-53-rev5.1.1",
  "to_controls": ["PM-11"],
  "rationale": "Mission and business process definition (PM-11) is the sole 800-53 control mapped to GV.OC-01 in the NIST IR spreadsheet.",
  "mapping_source": "https://csrc.nist.gov/extensions/nudp/services/json/csf/download?olirids=all (2026-06-07)"
}
```

Required fields per row (suggested):

- `from_subcategory` — the CSF Subcategory ID (`GV.OC-01`).
- `to_framework` — the target framework identifier (`800-53-rev5.1.1`, `800-53-rev5.2.0`, `800-171-r3`, `iso27001-2022`, `hipaa-security-rule`, `soc2-tsc-2017`, `pci-dss-4.0.1`, `cobit-2019`).
- `to_controls` — an **array** of control IDs in the target framework. The array is the dominant shape (1-to-many).
- `rationale` — a 1-2 sentence explanation of why the mapping exists.
- `mapping_source` — a URL or citation pointing to the authoritative source (the NIST Informative References spreadsheet, the AICPA TSC mapping, NIST SP 800-66 Rev 2 for HIPAA, etc.).

**Authoritative source URLs** (the canonical list lives in these NIST artifacts; this skill does not ship derivative JSON files because the IR spreadsheet is updated periodically and a snapshot would be stale):

- CSF 2.0 Informative References (XLSX, ~50 frameworks including 800-53 Rev 5.1.1, 800-53 Rev 5.2.0, 800-171 Rev 3, ISO 27001:2022, COBIT 2019, CIS Controls v8, PCI DSS v4.0.1, SOC 2 TSC 2017): `https://csrc.nist.gov/extensions/nudp/services/json/csf/download?olirids=all`
- NIST SP 800-66 Rev 2 (HIPAA Security Rule → 800-53, the authoritative HIPAA mapping): `https://csrc.nist.gov/pubs/sp/800/66/r2/final`
- NIST SP 800-53 Rev 5.1.1 (the 800-53 control catalog the IR spreadsheet maps to): `https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final`

## Cross-references

- `chunks/01-functions-categories.md` — the 106 Subcategory IDs referenced in every crosswalk row; the source of truth for the `from_subcategory` field.
- `chunks/05-govern-function.md` — the GOVERN Subcategories are the most-mapped-to-800-53-PM-family; the GV.SC Subcategories are the most operationally significant in 2.0 and have the most-developed crosswalk to 800-53 SR family.
- `nist-800-53-rmf/chunks/09-crosswalk.md` — the reverse direction (800-53 → CSF); the curated JSON in `nist-800-53-rmf/data/crosswalks/soc2-to-800-53-mod.json` uses a different format (1-to-1) than the CSF-side 1-to-many format used here.
- `aicpa-soc-reporting` — SOC 2 Common Criteria to CSF Subcategory mapping (the reverse direction of `csf-to-soc2-tsc-2017.json`); SOC 2 evidence is the natural precursor to a CSF profile for a SaaS.
- `coso-internal-controls` — the crosswalk to COSO Principles 1, 4, 12 (board oversight, risk appetite, policies) is meaningful for the GOVERN Function.

## Anti-hallucination

- **Authoritative source**: the primary source is the NIST CSF 2.0 **Informative References** spreadsheet, downloaded from `https://csrc.nist.gov/extensions/nudp/services/json/csf/download?olirids=all` (retrieved 2026-06-07). Always verify a curated mapping against the current NIST spreadsheet before publishing.
- **The mapping is informative, not normative.** An org can deviate from the published mapping with a documented rationale. Do not present the curated JSON as a "you must implement these controls" list; present it as a starting point for evidence reuse.
- **The 1-to-many nature is the dominant pattern, not the exception.** A statement like "PR.AA-01 maps to IA-2" is incomplete (it ignores IA-5, AC-2, AC-3, etc.). When the crosswalk JSON shows 1-to-1 for a Subcategory that the NIST spreadsheet shows 1-to-many, the curated JSON is incomplete — flag and update.
- **CSF Subcategories are outcomes, not controls.** The crosswalk is outcome-to-control, not control-to-control. Treating the crosswalk as a 1-to-1 control substitution ("replace IA-2 with PR.AA-01") is wrong; the CSF Subcategory is what you want to achieve, and the target-framework control is one of several mechanisms that produce it.
- **The 800-171 mapping is a subset of the 800-53 mapping**, not a parallel mapping. 800-171's 14 control families are a strict subset of 800-53's 20+ families. Do not invent mappings that exist in 800-171 but not in 800-53.
- **The ISO 27001:2022 mapping is to Annex A controls, not to the 93 clauses of the main standard.** Annex A is the control catalog; clauses 4-10 of ISO 27001 are the ISMS requirements (context, leadership, planning, support, operation, performance evaluation, improvement). The crosswalk ships Annex A mappings; clause-level mappings are a separate exercise.
- **The HIPAA mapping is to the Security Rule, not to the Privacy Rule or the Breach Notification Rule** — and the rows in §5 are **derived, not authoritative NIST CSF 2.0 IR** (the IR spreadsheet does not include HIPAA). The Privacy Rule (§164.500-§164.534) and the Breach Notification Rule (§164.400-§164.414) are separate; the CSF-to-HIPAA crosswalk covers the Security Rule only. The one exception is `RS.CO-02` (regulator notification), which cross-references the Breach Notification Rule §164.404. Verify each row against NIST SP 800-66 Rev 2 and the source regulations before relying on it.
