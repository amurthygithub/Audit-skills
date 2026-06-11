# Persona Review & G4.5 Vetting — pci-dss-assessment

**Date:** 2026-06-11 · **Ticket:** SOX-568 (M5 cycle 1) · **Build:** born-vetted (process v3/v3.1).
Run INSIDE the build PR. PCI DSS is licensed (Read-and-Copy) — verification was machine-checked
against the local licensed copy; this doc cites IDs/section refs, never verbatim standard text.

## Wave 1 — three parallel passes

- **§5.11 source-of-truth** — machine-verified against `~/Standards-licensed/PCI/` (the licensed
  PDF). Result: **1 CRITICAL** (below), the rest VERIFIED. Inventory recount was a perfect
  bijection (zero IDs in the text absent from the inventory and vice versa); 33 future-dated
  markers confirmed (column-wrap; naive grep undercounts); 6.4.3/11.6.1 confirmed as the
  payment-page-script requirements; currency re-checked live (v4.0.1 only active, no successor
  2026-06-11); no PAN and no bulk verbatim leakage anywhere.
- **Persona vetting** — 5 personas (QSA lead, e-comm SaaS lead, retail security manager, solo
  consultant, acquirer/brand analyst). Result: **1 HIGH** + 2 LOW. Brand/SSC boundary, currency
  posture, PAN-handling, and the customized-vs-compensating distinction all verified correct.
- **Consumer smokes** — 3/3 UCs PASS (one with notes); 62 tests stable; the entire counting
  layer byte-consistent across files; independently re-found the chunk-02 defect + 1 LOW.

## Findings ledger

| Sev | Finding | Disposition |
|-----|---------|-------------|
| **CRITICAL** | Compensating Controls Worksheet stated as **four** elements; PCI DSS v4.0.1 Appendix C has **six** Information-Required rows (Constraints; Definition of Compensating Controls; Objective; Identified Risk; Validation of Compensating Controls; Maintenance). The skill dropped Validation and Maintenance and mislabeled "Definition of Compensating Controls" as "controls-in-place". The error was hardcoded into the oracle (`assert len == 4`) and the acceptance gate cited that assertion as its own proof — a self-referential trust-anchor fabrication CI structurally could not catch. **Found only by machine-verification against the licensed PDF.** | **FIXED** full-stack: stub WORKSHEET_ELEMENTS (6 keys), seed (all six), oracle (`len == 6`), adversarial test, and ~11 docs/chunks; acceptance-gate row 12 re-evidenced to the licensed Appendix C. Re-verified against the PDF. |
| **HIGH** | chunks/02 worked illustration printed "4 connected → 9 in-scope / 5 out-of-scope" (internally inconsistent, didn't foot to 14) while seed/oracle/every other file say 5 connected → 10/4. | **FIXED** to 10/4 (lone divergent copy). |
| LOW | SKILL.md UC-02 persona labeled "assessor" vs "auditee" in the index. | **FIXED** to auditee/retail security manager. |
| LOW | chunk-06 ROC finding-status set incomplete for a working ROC. | **FIXED** — one-line note that the assessor ROC template governs the exact status set. |
| LOW | A-vs-A-EP model collapses iframe-server-delivery nuance into the JS flag. | **ACCEPTED** — labeled house convention with a refuse-on-missing-fact escape hatch; boundary table sound (24 ROC / 6 A-EP / 2 A). |

## Tier-2 adjudications

- **Worksheet = six rows** — verified verbatim-structure against the licensed Appendix C (six
  "Information Required" rows, in order). The "four" was the build's fabrication, not the source.
- **Currency** — v4.0.1 only active, future-dated all in force since 2025-03-31, no successor
  as of 2026-06-11 (document-library level). No persona refutation entertained from memory.

## Eval lane (process v3.1)

`evals/pci-dss-assessment/cases/` — 3 UC substance cases + 1 idempotence invariant, oracle-
labeled, CI-enforced (stub lane 100%). Calibration sweep (Haiku 4.5, N=2) logged in
`evals/README.md`. Publication sweep (N≥20 × Haiku+Sonnet) before any release/GTM claim.

## Verdict

**G4.5 PASS** — 1 CRITICAL + 1 HIGH found and fixed inside the build PR, re-verified against
the licensed primary source; remaining findings ACCEPTED with rationale. The CRITICAL is the
headline lesson of M5 cycle 1: **a licensed local copy turns the deepest fabrication class —
the self-referential trust-anchor error CI cannot catch — into a catchable one.**
