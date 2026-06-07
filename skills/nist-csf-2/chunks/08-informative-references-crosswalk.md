---
chunk_id: 08-informative-references-crosswalk
parent_skill: nist-csf-2
topic: "CSF subcategory → 800-53, 800-171, ISO 27001, HIPAA Security Rule mappings"
load_when: "user asks for a crosswalk, mapping, or how CSF relates to 800-53"
---

# Chunk 08 — Informative References Crosswalk

NIST publishes an "Informative References" spreadsheet alongside CSF 2.0 that maps each of the ~108 Subcategories to ~50 other frameworks and control catalogs (800-53, 800-171, ISO 27001:2022 Annex A, COBIT 2019, CIS Controls v8, HIPAA Security Rule, SOC 2 TSC 2017, PCI DSS v4.0.1, and others) [NIST-CSF-2.0 Informative References]. The mapping is **informative, not normative**: it is NIST's published view of the relationship, but an org is not required to follow any specific mapping. The curated JSON version of these mappings lives in `data/crosswalks/` and is the input to the cross-framework use cases (UC-03 in particular).

## 1. What informative references are (and what they are not)

An **informative reference** in NIST parlance is a citation in the framework text that points to a related authoritative source. For CSF 2.0, NIST publishes a spreadsheet that lists, for each Subcategory, the corresponding controls in ~50 other frameworks. The published mapping is the **primary source**; the curated JSON in `data/crosswalks/` is a derived, project-specific snapshot.

What informative references **are**:

- A NIST-curated view of how a CSF Subcategory outcome relates to controls in other frameworks.
- A starting point for orgs that need to demonstrate coverage of multiple frameworks with one evidence base.
- A bridge between outcome-oriented frameworks (CSF, COBIT goals cascade) and control-oriented frameworks (800-53, ISO 27001 Annex A).

What informative references **are not**:

- **Not normative.** An org can deviate from the published mapping with a documented rationale. The mapping is NIST's view, not a rule.
- **Not 1:1.** Most Subcategories map to 2-5 controls in 800-53; some map to 10+. The 1-to-many pattern is the dominant one.
- **Not exhaustive.** The 50 frameworks in the spreadsheet are not all the frameworks an org might face (e.g., state-level RMF variants, sector-specific overlays like CISA ICS CPG, regional privacy laws like GDPR).
- **Not authoritative for the target framework.** The CSF ↔ 800-53 mapping tells you how a CSF Subcategory relates to 800-53; for the authoritative 800-53 control, you read 800-53 itself. Same for ISO 27001, HIPAA, SOC 2.

## 2. The CSF ↔ 800-53 crosswalk (representative samples)

The CSF ↔ 800-53 mapping is the most-used crosswalk in federal-adjacent engagements. The representative samples below cover the 6 Functions; the full curated mapping is in `data/crosswalks/csf-to-800-53-mod.json` (the moderate baseline; high-baseline mappings are in `data/crosswalks/csf-to-800-53-high.json`).

| CSF Subcategory | Representative 800-53 Rev 5 controls | Notes |
|-----------------|--------------------------------------|-------|
| `GV.OC-01` (mission understood) | `PM-11`, `PM-15` | Program Management family |
| `GV.OC-03` (legal/regulatory) | `PM-9`, `RA-1` | Cross-family (PM + RA) |
| `GV.RM-02` (risk appetite) | `PM-9`, `PM-8` | Program Management family |
| `GV.SC-01` (TPRM program) | `SR-1`, `SR-3` | Supply Chain family |
| `GV.SC-04` (supplier assessment) | `SR-6` | Supply Chain family |
| `GV.SC-05` (supplier IR coord.) | `SR-8`, `IR-4` | Cross-family (SR + IR) |
| `GV.PO-01` (policy) | `PM-1`, all "XX-1" controls | PM family + per-family policy controls |
| `GV.OV-01` (performance reviewed) | `CA-7`, `PM-6` | Continuous Monitoring + PM |
| `GV.RR-01` (leadership accountable) | `PM-2`, `PM-3` | Program Management family |
| `ID.AM-01` (asset inventory HW) | `ID-1` (old) or `PM-5` (Rev 5) | 800-53 Rev 5 retired ID-1 in favor of PM-5 |
| `ID.AM-08` (system SDLC) | `SA-3`, `SA-8`, `SA-15` | System and Services Acquisition family |
| `ID.RA-01` (vulnerabilities) | `RA-3`, `RA-5`, `SI-2` | Risk Assessment + System Integrity |
| `PR.AA-01` (identity mgmt) | `IA-2`, `IA-5`, `AC-2` | Identification & Authentication + Access Control |
| `PR.AA-03` (MFA) | `IA-2(1)`, `IA-2(2)`, `AC-6(9)` | IA + AC with enhancements |
| `PR.AA-05` (access permissions) | `AC-2`, `AC-3`, `AC-5`, `AC-6` | Access Control family |
| `PR.DS-01` (data-at-rest) | `SC-28`, `SC-28(1)` | System and Communications Protection |
| `PR.PS-01` (configuration mgmt) | `CM-2`, `CM-6`, `CM-7` | Configuration Management family |
| `PR.IR-01` (network segmentation) | `SC-7`, `SC-32` | System and Communications Protection |
| `DE.CM-01` (network monitoring) | `SI-4`, `AU-2` | System Integrity + Audit |
| `DE.CM-09` (compute monitoring) | `SI-4`, `SI-4(2)` | System Integrity + enhancement |
| `DE.AE-02` (event correlation) | `AU-6`, `SI-4(2)` | Audit + System Integrity |
| `RS.MA-01` (IR plan executed) | `IR-4`, `IR-5`, `IR-6` | Incident Response family |
| `RS.CO-02` (regulator notification) | `IR-6` | Incident Response |
| `RC.RP-01` (recovery executed) | `CP-2`, `CP-10`, `IR-4` | Contingency Planning + IR |

The full mapping is many-to-many: a single 800-53 control (e.g., `AC-2`) can be referenced by multiple CSF Subcategories (PR.AA-01, PR.AA-05, etc.), and a single CSF Subcategory (e.g., `PR.AA-01`) can be referenced by 4-5 800-53 controls.

## 3. The CSF ↔ 800-171 crosswalk (moderate baseline, federal-adjacent)

NIST SP 800-171 Rev 3 [NIST-SP-800-171] is the moderate-baseline control set for protecting Controlled Unclassified Information (CUI) in nonfederal systems. The CSF ↔ 800-171 mapping is similar in shape to CSF ↔ 800-53 Moderate but with 800-171's 14 control families (3xx series). 800-171 maps to CMMC 2.0 Level 2; orgs pursuing CMMC L2 use the CSF ↔ 800-171 crosswalk as the bridge.

Representative samples (the full mapping ships in `data/crosswalks/csf-to-800-171-r3.json`):

| CSF Subcategory | 800-171 Rev 3 control | CMMC L2 practice |
|-----------------|------------------------|------------------|
| `PR.AA-01` (identity mgmt) | 03.01.01 (AC-2 family) | AC.L2-3.1.1 |
| `PR.AA-03` (MFA) | 03.01.02 (AC-2 + IA-2 enhancements) | AC.L2-3.1.12 |
| `PR.DS-01` (data-at-rest) | 03.13.16 (SC-28) | SC.L2-3.13.16 |
| `DE.CM-01` (network monitoring) | 03.13.06 (SI-4) | SI.L2-3.13.06 |
| `RS.MA-01` (IR plan executed) | 03.06.01 (IR-4) | IR.L2-3.6.1 |
| `RC.RP-01` (recovery executed) | 03.07.01 (CP-2) | CP.L2-3.7.1 |
| `GV.SC-03` (contracts) | 03.12.01 (SR-3) | SR.L2-3.12.1 |

800-171 is a strict subset of 800-53 Moderate (~110 controls vs 800-53's ~325); the CSF → 800-171 mapping is therefore a strict subset of the CSF → 800-53 mapping. For orgs pursuing CMMC L2, the practical workflow is: CSF Current Profile → identify lagging Subcategories → map to 800-171 → produce the System Security Plan (SSP) for the CMMC assessment.

## 4. The CSF ↔ ISO 27001:2022 crosswalk (Annex A controls)

ISO 27001:2022 [ISO-27001-2022] introduced a new Annex A with 93 controls organized in 4 themes (Organizational, People, Physical, Technological). The CSF ↔ ISO 27001 mapping is outcome-to-control: a CSF Subcategory typically maps to 1-3 Annex A controls, and an Annex A control typically supports 1-3 CSF Subcategories.

Representative samples (the full mapping ships in `data/crosswalks/csf-to-iso27001-2022.json`):

| CSF Subcategory | ISO 27001:2022 Annex A control | Notes |
|-----------------|--------------------------------|-------|
| `GV.OC-01` (mission) | A.5.1 (Policies), A.5.2 (Information security roles) | Organizational theme |
| `GV.SC-04` (supplier assessment) | A.5.19-A.5.23 (Supplier relationships) | Organizational theme |
| `GV.PO-01` (policy) | A.5.1 (Policies for information security) | Organizational |
| `PR.AA-01` (identity mgmt) | A.5.16 (Identity management), A.5.17 (Authentication info) | Organizational + Technological |
| `PR.AA-03` (MFA) | A.8.5 (Secure authentication) | Technological theme (renamed in 2022) |
| `PR.DS-01` (data-at-rest) | A.8.24 (Use of cryptography) | Technological |
| `PR.PS-01` (configuration mgmt) | A.8.9 (Configuration management) | Technological |
| `DE.CM-01` (network monitoring) | A.8.16 (Monitoring activities) | Technological |
| `RS.MA-01` (IR plan) | A.5.24-A.5.27 (Incident management planning) | Organizational |
| `RC.RP-01` (recovery executed) | A.8.14 (Backup), A.5.30 (ICT readiness) | Technological + Organizational |

ISO 27001:2022's 93 Annex A controls are far fewer than 800-53's ~325 Moderate controls. The mapping is therefore *denser* on the ISO side (each ISO control supports more CSF Subcategories on average) and *less granular* on the ISO side (ISO 27001 specifies the control outcome, not the enhancement-level implementation).

## 5. The CSF ↔ HIPAA Security Rule crosswalk (§164.308/310/312 safeguards)

The HIPAA Security Rule [HIPAA-Security-Rule] specifies administrative, physical, and technical safeguards at 45 CFR §164.308, §164.310, and §164.312. The CSF ↔ HIPAA mapping is outcome-to-safeguard; a single CSF Subcategory typically maps to 1-2 Security Rule safeguard references. NIST 800-66 Rev 2 is the authoritative HIPAA → 800-53 mapping; the CSF → HIPAA mapping in this skill is derived from 800-66's reverse direction.

Representative samples (the full mapping ships in `data/crosswalks/csf-to-hipaa.json`):

| CSF Subcategory | HIPAA Security Rule reference | Safeguard type |
|-----------------|-------------------------------|----------------|
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

The HIPAA Security Rule is healthcare-specific; the CSF mapping is meaningful for covered entities and business associates. The mapping is also useful for orgs in healthcare-adjacent industries (e.g., health tech, digital health) that handle PHI but are not strictly covered entities.

## 6. The 1-to-many nature of CSF-to-control mappings

The single most important property of the CSF-to-control crosswalks: **a single Subcategory can map to 2-5 controls in the target framework; some map to 10+.** This is because CSF Subcategories are **outcomes** (e.g., "Identities and credentials are managed" — `PR.AA-01`) and 800-53 / ISO / HIPAA controls are **mechanisms** (specific safeguards that produce the outcome). A single outcome can require several mechanisms.

Examples of 1-to-many:

- **`PR.AA-01` (identity mgmt) → 800-53**: `IA-2`, `IA-5`, `AC-2`, `AC-3`, `IA-4`, `IA-8`. Six controls across two families.
- **`DE.CM-01` (network monitoring) → 800-53**: `SI-4`, `AU-2`, `AU-6`, `CA-7`. Four controls across three families.
- **`GV.SC-01` (TPRM program) → 800-53**: `SR-1`, `SR-3`, `SR-6`, `PM-30`. Four controls across two families.
- **`RC.RP-01` (recovery executed) → 800-53**: `CP-2`, `CP-10`, `IR-4`, `IR-8`. Four controls across two families.

The reverse (1-to-1) is the exception, not the rule. When producing a crosswalk for an org, expect to see 1-to-2 to 1-to-5 mappings as the norm; flag any 1-to-1 mapping for verification (it usually means the mapping is incomplete).

**Practical consequence for the crosswalk JSON**: the curated `data/crosswalks/csf-to-*.json` files use the format `{"from_subcategory": "GV.OC-01", "to_framework": "800-53", "to_controls": ["PM-11", "PM-15"], "rationale": "..."}` — the `to_controls` is an **array**, not a scalar. The 800-53 RMF skill's `soc2-to-800-53-mod.json` uses a different format (1-to-1 control-to-control) because the SOC 2 ↔ 800-53 mapping is dominantly 1-to-1; the CSF → 800-53 mapping is dominantly 1-to-many. Any cross-skill parser consuming both formats must support both shapes.

## 7. The `data/crosswalks/` JSON format

The curated crosswalks ship as JSON files in `data/crosswalks/`. The format is the **CSF-side** format (one row per CSF Subcategory, with an array of target-framework controls):

```json
{
  "from_subcategory": "GV.OC-01",
  "to_framework": "800-53-rev5",
  "to_controls": ["PM-11", "PM-15"],
  "rationale": "Mission and business process definition (PM-11) and security/privacy groups (PM-15) produce the organizational context Subcategory outcome.",
  "mapping_source": "https://www.nist.gov/cyberframework (Informative References spreadsheet, Feb 2024)"
}
```

Required fields per row:

- `from_subcategory` — the CSF Subcategory ID (`GV.OC-01`).
- `to_framework` — the target framework identifier (`800-53-rev5`, `800-171-r3`, `iso27001-2022`, `hipaa-security-rule`, `soc2-tsc-2017`, `pci-dss-4.0.1`, `cobit-2019`).
- `to_controls` — an **array** of control IDs in the target framework. The array is the dominant shape (1-to-many).
- `rationale` — a 1-2 sentence explanation of why the mapping exists. The rationale is what differentiates the curated JSON from a bare mapping table.
- `mapping_source` — a URL or citation pointing to the authoritative source (the NIST Informative References spreadsheet, the AICPA TSC mapping, the 800-66 Rev 2 HIPAA mapping, etc.).

Files in `data/crosswalks/` (the current set, expand over time):

- `csf-to-800-53-mod.json` — CSF Subcategories → 800-53 Rev 5 Moderate baseline controls.
- `csf-to-800-53-high.json` — CSF Subcategories → 800-53 Rev 5 High baseline controls.
- `csf-to-800-171-r3.json` — CSF Subcategories → 800-171 Rev 3 controls (CMMC L2 readiness).
- `csf-to-iso27001-2022.json` — CSF Subcategories → ISO 27001:2022 Annex A controls.
- `csf-to-hipaa.json` — CSF Subcategories → HIPAA Security Rule §164.308/310/312 safeguards.
- `csf-to-soc2-tsc-2017.json` — CSF Subcategories → SOC 2 Trust Services Criteria 2017.
- `csf-to-pci-dss-4.0.1.json` — CSF Subcategories → PCI DSS v4.0.1 requirements.
- `csf-to-cobit-2019.json` — CSF Subcategories → COBIT 2019 management objectives.
- `csf-2-0-subcategories.json` — the canonical list of all ~108 CSF 2.0 Subcategories (referenced by `chunks/01-functions-categories.md`).

## Cross-references

- `chunks/01-functions-categories.md` — the ~108 Subcategory IDs referenced in every crosswalk row; the source of truth for the `from_subcategory` field.
- `chunks/05-govern-function.md` — the GOVERN Subcategories are the most-mapped-to-800-53-PM-family; the GV.SC Subcategories are the most operationally significant in 2.0 and have the most-developed crosswalk to 800-53 SR family.
- `nist-800-53-rmf/chunks/09-crosswalk.md` — the reverse direction (800-53 → CSF); the curated JSON in `nist-800-53-rmf/data/crosswalks/soc2-to-800-53-mod.json` uses a different format (1-to-1) than the CSF-side 1-to-many format used here.
- `nist-800-53-rmf/data/crosswalks/soc2-to-800-53-mod.json` — the existing 1-to-1 crosswalk JSON in the sibling skill; the format difference (1-to-1 vs 1-to-many) is the reason the two skills ship distinct shapes.
- `data/crosswalks/csf-to-800-53-mod.json` — the primary curated crosswalk for federal/DoD engagements; the source for UC-03's "Current/Target gap mapped to 800-53" deliverable.
- `aicpa-soc-reporting` — SOC 2 Common Criteria to CSF Subcategory mapping (the reverse direction of `csf-to-soc2-tsc-2017.json`); SOC 2 evidence is the natural precursor to a CSF profile for a SaaS.
- `coso-internal-controls` — the crosswalk to COSO Principles 1, 4, 12 (board oversight, risk appetite, policies) is meaningful for the GOVERN Function.

## Anti-hallucination

- **Authoritative source**: the primary source is the NIST CSF 2.0 **Informative References** spreadsheet [NIST-CSF-2.0 Informative References], published at https://www.nist.gov/cyberframework (Feb 2024). Always verify a curated mapping against the current NIST spreadsheet before publishing. The spreadsheet is updated periodically; check the version date.
- **The mapping is informative, not normative.** An org can deviate from the published mapping with a documented rationale. Do not present the curated JSON as a "you must implement these controls" list; present it as a starting point for evidence reuse.
- **The 1-to-many nature is the dominant pattern, not the exception.** A statement like "PR.AA-01 maps to IA-2" is incomplete (it ignores IA-5, AC-2, AC-3, etc.). When the crosswalk JSON shows 1-to-1 for a Subcategory that the NIST spreadsheet shows 1-to-many, the curated JSON is incomplete — flag and update.
- **CSF Subcategories are outcomes, not controls.** The crosswalk is outcome-to-control, not control-to-control. Treating the crosswalk as a 1-to-1 control substitution ("replace IA-2 with PR.AA-01") is wrong; the CSF Subcategory is what you want to achieve, and the target-framework control is one of several mechanisms that produce it.
- **The 800-171 mapping is a subset of the 800-53 mapping**, not a parallel mapping. 800-171's 14 control families are a strict subset of 800-53's 20+ families. Do not invent mappings that exist in 800-171 but not in 800-53.
- **The ISO 27001:2022 mapping is to Annex A controls, not to the 93 clauses of the main standard.** Annex A is the control catalog; clauses 4-10 of ISO 27001 are the ISMS requirements (context, leadership, planning, support, operation, performance evaluation, improvement). The crosswalk ships Annex A mappings; clause-level mappings are a separate exercise.
- **The HIPAA mapping is to the Security Rule, not to the Privacy Rule or the Breach Notification Rule.** The Privacy Rule (§164.500-§164.534) and the Breach Notification Rule (§164.400-§164.414) are separate; the CSF-to-HIPAA crosswalk covers the Security Rule only. The one exception is `RS.CO-02` (regulator notification), which cross-references the Breach Notification Rule §164.404.
- **The curated JSON in `data/crosswalks/` is a project-specific snapshot.** The published NIST spreadsheet is the primary source; the JSON files are derived, versioned, and may lag. Always check the `mapping_source` field for the date and version of the source the curated row was derived from.
