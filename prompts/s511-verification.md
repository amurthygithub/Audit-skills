# §5.11 source-of-truth verification — G4 pass 2 (and pass 4, re-verify)

Dispatch **1 agent per skill** (or N in parallel for a library sweep). The agent **must have webfetch access** — this pass is meaningless without live sources. This is the ONLY gate that catches factual errors; the linter, tests, and 5-lens review do not.

> **You are verifying every factual claim in `skills/{{skill_slug}}/` against live authoritative sources.**
> The skill's fact-sheet is at `docs/{{skill_slug}}-fact-sheet.md` — verify the skill against the fact-sheet first, then spot-check the fact-sheet itself against live sources (fact-sheets rot too).
> Report findings as a table: `severity | file:line | claim as written | correct value | source URL | retrieval date`
> Do NOT fix anything. Do NOT commit. Report only.

## Check every category — none are optional

1. **Framework identifiers — existence AND semantics** — every code exists in the real spec, with that exact ID format, **and means what the skill says it means**. Existence checks are not enough: SC-8(1) existed but the skill called it a wireless control and taught users to scope it out (caught by persona vetting after 3 §5.11 rounds missed it). For every identifier, verify the official NAME and verify the skill's usage matches the control's actual scope. LLM builds fabricate plausible codes; assume fabrication until verified.
2. **Counts** — every count stated anywhere (function counts, subcategory counts, criteria counts, PoF counts). Count them yourself in the source document. Builds are reliably wrong by ±2.
3. **Versions** — every version reference is the current published version. If a newer version/revision exists, or the cited one was withdrawn (e.g. SP 800-61 Rev 2, withdrawn Apr 2025), flag it. Watch for fabricated versions (`Rev 5.1.1`).
4. **URLs** — every §10 manifest URL returns 200 right now (not 404/410/redirect-to-homepage). Known rot zones: AICPA `/resources/`, COSO guidance pages, ISACA ITAF paths, NIST revision-specific URLs, FedRAMP `/resources/`.
5. **Crosswalk rows** — every mapping row matches the authoritative cross-reference (e.g. NIST IR informative references). Spot-check at minimum 20 rows or 100%, whichever is smaller.
6. **Terminology** — framework-specific terms match the source's exact wording (Tier 1 = "Partial", not "Initial").
7. **Cross-chunk consistency** — any fact stated in more than one file says the same thing everywhere (grep for the fact; list every location).
8. **Supersession claims** — "X supersedes Y" claims match the publisher's own supersession notice.
9. **Process/SLA/duration claims** — remediation windows, reporting timelines, authorization durations, review cadences: verify against the governing program document (e.g., FedRAMP ConMon guide, OMB A-130). The skill once shipped fabricated "48h/24h FedRAMP SLAs" that sounded authoritative.
10. **Cited-document identity** — for every memo/standard cited by number, fetch it and confirm the TITLE matches the number (the manifest once cited M-22-15 with two different wrong titles; the real document was M-24-15).
11. **Currency & negative existence** — any claim that something "is current," "is the latest edition," "was sunset/superseded," "was never published," or "does not exist" MUST be settled by a live fetch, never by your knowledge or reviewer consensus. The M1 sweep refuted persona consensus 4 times, always on post-cutoff events (ITAF 5th Ed launched 2026; CISA CPG 2.0 published Dec 2025; ISACA became the CMMC CAICO; the FFIEC CAT was sunset). Also check each cited TOOL/BODY still exists in the stated role (JAB→FedRAMP Board class of staleness).
12. **Catalog inventory-diff** — when the skill encodes a framework catalog (criteria/objectives/subcategories/requirements), obtain the FULL official inventory (PDF text-extraction or official JSON/export) and diff the skill's IDs, names, and counts against it. Spot checks miss offsetting errors (an invented BAI12 masked a missing MEA04; the total still summed correctly).
13. **Anti-hallucination & limits sections FIRST** — verify every specific claim in the skill's anti-hallucination, limits-and-disclaimers, and acceptance-gate content as the highest priority: in 4 of 6 M1 skills, fabrications (invented statutes, fake SLAs, wrong editions) lived inside the trust-anchor sections themselves. A gate row marked ✓ without a verbatim quote is invalid — re-derive it; flag any unresolved author markers (`[VERIFY:`, "need recount") as CRITICAL.
14. **UC-doc ↔ seed/oracle coherence (Tier 1)** — every use-case document's stated facts (org name/size, gap lists, counts, expected values, control-ID formats, file pointers) must match its `data_refs` seed and its `tests` assertions. The tested fixture is the contract; flag every divergence (M1: one skill shipped ALL THREE UC docs describing different companies than their seeds).
15a. **Licensed-source rows (the ONE exception to the verbatim-quote rule)** — facts sourced from licence-restricted text (ISO/COSO) must carry a clause pointer + `verified_by: human (licensed copy, <edition>)` + date and NO verbatim quote. Verify the sign-off exists and is current for the cited edition; flag any verbatim standard text beyond a short attributed excerpt as a licence violation (CRITICAL). Never fetch, request, or reconstruct licensed text yourself.
15b. **House-convention attribution** — every formula, scale, weighting, threshold, or rollup must either carry a verbatim source quote or be explicitly labeled a house convention/illustrative heuristic. Invented math attributed to a named publication is CRITICAL (e.g., "L×I×CRF per the CISA CRM", "%-gap per NIST").

## Output contract

- Findings table (format above), ordered CRITICAL → LOW.
- **Every VERIFIED claim must carry a verbatim quote from the fetched source** (one sentence is enough). A verification row without a quote is Tier-3 concurrence, not verification — it does not count.
- A verification summary appended to (or creating) `skills/{{skill_slug}}/docs/acceptance-gate.md`: `fact | source | retrieval date | verifier | status` — one row per category checked, minimum 20 rows for a new skill.
- Explicit statement of what you did NOT check, so the next pass knows the residual risk.

## Re-verify mode (pass 4)

After a fix pass, rerun this prompt scoped to: (a) every finding from the previous run — confirm fixed; (b) every file the fix agent touched — fix agents introduce new errors. Same output contract.
