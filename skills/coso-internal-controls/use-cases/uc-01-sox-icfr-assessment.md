---
uc_id: UC-01
title: "Full SOX 404 ICFR assessment with walkthrough, RcM, and deficiency classification"
industries: [financial-services]
frameworks: [COSO-ICIF-2013, SOX-404, PCAOB-AS-2201, SEC-Reg-S-K-Item-308]
inputs:
  entity_description: "Mid-cap public bank, accelerated filer, $12B assets, 3 significant processes"
  processes: ["Loan Origination", "Deposit Operations", "Investment Securities"]
procedure:
  - "chunks/03-sox-pcaob.md: Scope significant accounts and relevant assertions"
  - "chunks/04-walkthrough-controls.md: Perform walkthrough for each process"
  - "chunks/01-coso-icif.md: Evaluate entity-level controls (P1-P5)"
  - "chunks/06-rcm-and-reports.md: Complete RcM for each process"
  - "chunks/05-deficiency-classification.md: Classify any identified deficiencies"
  - "chunks/07-compensating-updates-cross.md: Evaluate compensating controls"
  - "chunks/06-rcm-and-reports.md: Produce Management ICFR Report"
expected_outputs:
  rcm: {processes: 3, total_controls_identified: 45, key_controls: 28, deficiencies_identified: 3}
  management_icfr_report: {conclusion: "Effective, subject to remediation"}
oracle:
  type: schema_match
  assertion: "RcM template 17 columns, deficiency classification 3-step decision tree, Management ICFR Report per SEC Reg S-K Item 308"
data_refs: []
tests: ["tests/test_lint.py"]
status: stub
---

# UC-01: Full SOX 404 ICFR Assessment

## Scenario

Mid-cap public regional bank ($12B assets, accelerated filer) performing annual SOX 404 ICFR assessment. Three processes: loan origination, deposit operations, investment securities. COSO 2013 ICIF framework.

## Walk-through

Phase 1: Scope significant accounts and relevant assertions per AS 2201.
Phase 2: Perform walkthroughs (Inquiry/Observation/Inspection/Re-performance).
Phase 3: Complete 17-column RcM, identify key vs non-key controls, evaluate effectiveness.
Phase 4: Apply 3-step deficiency decision tree, evaluate compensating controls. Final: 1 SD, 2 D.
Phase 5: Produce Management ICFR Report per SEC Reg S-K Item 308.
