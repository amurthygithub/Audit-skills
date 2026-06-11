# Persona Review & G4.5 Vetting — sox-302-disclosure-controls

**Date:** 2026-06-11 · **Ticket:** SOX-570 (M5 cycle 2) · **Build:** born-vetted (process v3/v3.1).
Run INSIDE the build PR. Sources are public US federal text — fully machine-verifiable against
live eCFR + statute; verbatim extracts vendored at `docs/builds/sox-570/sec-source-extracts.json`.

## Wave 1 — three parallel passes

- **§5.11 source-of-truth** — machine-verified against live eCFR (Title 17) + 15 U.S.C. 7241.
  **Result: CLEAN — zero findings at any severity.** All three fidelity claims verified
  byte-for-byte: the DC&P definition (13a-15(e), broader than ICFR), the ICFR definition
  (13a-15(f), financial subset), and the 302-vs-404 / 404(b)-EGC-exemption boundary (§229.308(b)
  verbatim; the skill never states the exemption as exempting §302). 6 cert elements =
  7241(a)(1)-(6); disclosure committee/sub-cert labeled practice-not-rule in every occurrence;
  UC↔seed coherence exact. 13 new live-verified rows appended to the acceptance gate (now 36).
- **Persona vetting** (5 personas: SEC-reporting manager, disclosure-committee chair, Big-4 SOX
  advisor, controller, securities lawyer). **PASS** — no CRITICAL/HIGH; 3 MEDIUM + 2 LOW + 1
  INFO, all citation-precision or wording (no substance error). The deliberate
  disclosure-committee-as-practice framing confirmed correct everywhere.
- **Consumer smokes** — 3/3 PASS; 56 tests; **zero cross-file contradictions, zero high-yield
  findings** (no §302-exempt, no cascade-as-rule, no DC&P/ICFR conflation, no §404 re-teaching).

## Findings ledger

| Sev | Finding | Disposition |
|-----|---------|-------------|
| MEDIUM | chunk 03 ¶3 attributes "cash flows" to the statute; 15 U.S.C. 7241(a)(3) says "financial condition and results of operations" only — "cash flows" is a 601(b)(31) exhibit-form addition. | **FIXED** — re-cited to the exhibit form (verified against statute text). |
| MEDIUM | chunk 05 cites the newly-public §404 transition to Item 308(a); the verbatim transition language is in **Instruction 1 to Item 308**. | **FIXED** — re-cited to Instruction 1 (verified: "Instructions to Item 308: 1."). |
| MEDIUM | chunk 05 framed the Item 307 DC&P conclusion as area-scoped ("not effective for that area"); Item 307 is a single **entity-wide** conclusion. | **FIXED** — reworded to the overall not-effective conclusion (the output + chunk 04 template were already correct). |
| LOW | FPI annual evaluation frequency could be read as attaching to a foreign *subsidiary* in a domestic group rather than to an FPI **registrant**. | **FIXED** — scoping note in UC-03 §4. |
| LOW | chunk 04 §4 described Item 308(a) report contents before disclaiming §404 re-teaching. | **FIXED** — contents referenced to coso-internal-controls; only the boundary fact kept. |
| LOW | README "~32 tests" vs 56. | **FIXED** — 56. |
| INFO | "Any SD/MW triggers ¶5" could be read as covering a DC&P-only deficiency; ¶5 is ICFR-scoped. | **FIXED** — scope note in chunk 07 (a missed cyber 8-K is a DC&P matter, not a ¶5 item). |

## Tier-2 adjudications

- All three fidelity claims and the 6 cert elements verified byte-for-byte against live eCFR /
  statute by §5.11 AND re-checked by the dispatcher at the source for the two citation MEDIUMs.
- Currency: 13a-14/13a-15/Items 307-308 current (last amendments 2003-2018); 2023 cyber
  additions (33-11216) noted; no pending change as of 2026-06-11.
- No persona currency refutation entertained from memory.

## Residual (declared by §5.11)

- The exact "4 business days" 8-K Item 1.05 wording was corroborated via Item 106's 2023 bracket
  and cross-file consistency, not read verbatim (Federal Register bot-walled). Well-established;
  re-verify verbatim at a future pass if a client engagement turns on it.
- SEC Releases 33-8124 / 33-11216 cited in prose were not fetched verbatim (sec.gov bot-wall);
  33-11216 corroborated via the eCFR Item 106 bracket.

## Eval lane (process v3.1)

`evals/sox-302-disclosure-controls/cases/` — 3 UC substance cases + 1 idempotence invariant,
oracle-labeled, CI-enforced (stub lane 100%). Calibration sweep (Haiku 4.5, N=2) logged in
`evals/README.md`. Publication sweep (N≥20 × Haiku+Sonnet) before any release/GTM claim.

## Verdict

**G4.5 PASS** — no CRITICAL/HIGH at any pass; §5.11 clean against primary source; all MEDIUM/LOW
citation-precision and wording findings fixed inside the build PR. The skill's two spine
boundaries (DC&P≠ICFR, §302≠§404) and the practice-vs-rule discipline are correct and verified.
