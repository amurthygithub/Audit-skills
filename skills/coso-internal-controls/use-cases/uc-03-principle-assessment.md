---
uc_id: UC-03
title: "COSO 2013 ICIF principle-by-principle assessment with template output"
industries: [financial-services]
frameworks: [COSO-ICIF-2013]
inputs:
  entity_description: "Public company evaluating all 17 COSO principles for ICFR effectiveness"
  assessment_date: "2026-06-30"
procedure:
  - "chunks/01-coso-icif.md: Evaluate each principle (P1-P17) for presence and functioning"
  - "chunks/01-coso-icif.md: Assess each Point of Focus as Yes/No/Partially"
  - "chunks/06-rcm-and-reports.md: Complete the COSO Principle Assessment template"
  - "chunks/01-coso-icif.md: Evaluate integrated operation across all 5 components"
expected_outputs:
  principle_assessments:
    - {principle: P1, component: "Control Environment", present_and_functioning: true, pofs_assessed: 4, deficiencies: 0}
    - {principle: P2, component: "Control Environment", present_and_functioning: true, pofs_assessed: 4, deficiencies: 0}
    - {principle: P8, component: "Risk Assessment", present_and_functioning: true, pofs_assessed: 4, deficiencies: 0}
  overall: "All 17 principles present and functioning; components operating in integrated manner"
oracle:
  type: schema_match
  assertion: "All 17 principle assessments completed with PoF-by-PoF evaluation"
data_refs: []
tests: ["tests/test_coso_internal_controls_oracle.py::test_uc_03_oracle"]
status: stub
---

# UC-03: Principle-by-Principle COSO Assessment

## Scenario

Public company performing a comprehensive COSO 2013 ICIF assessment. All 17 principles must be evaluated for presence and functioning, and the 5 components must be assessed for integrated operation. The entity uses the COSO Principle Assessment template from chunk 06.

## Walk-through

### Phase 1: Control Environment (P1-P5)
Evaluate each principle against its Points of Focus. For each PoF, assess Yes/No/Partially with supporting evidence. Document findings in the Principle Assessment template.

### Phase 2: Risk Assessment (P6-P9)
Evaluate objectives clarity, risk identification, fraud risk assessment, and change assessment. Link each risk to relevant controls.

### Phase 3: Control Activities (P10-P12)
Evaluate control design and deployment. Map key controls to risks and assertions. Assess technology controls (P11).

### Phase 4: Information and Communication (P13-P15)
Evaluate information quality, internal communication channels, and external communication. Verify board/audit committee reporting.

### Phase 5: Monitoring Activities (P16-P17)
Evaluate mix of ongoing and separate evaluations. Assess deficiency communication timeliness.

### Phase 6: Integrated Operation
Confirm that all 5 components collectively reduce risk to an acceptable level. If any component is not functioning, identify the impact on other components.
