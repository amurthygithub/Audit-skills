# §5.11 source-of-truth verification — G4 pass 2 (and pass 4, re-verify)

Dispatch **1 agent per skill** (or N in parallel for a library sweep). The agent **must have webfetch access** — this pass is meaningless without live sources. This is the ONLY gate that catches factual errors; the linter, tests, and 5-lens review do not.

> **You are verifying every factual claim in `skills/{{skill_slug}}/` against live authoritative sources.**
> The skill's fact-sheet is at `docs/{{skill_slug}}-fact-sheet.md` — verify the skill against the fact-sheet first, then spot-check the fact-sheet itself against live sources (fact-sheets rot too).
> Report findings as a table: `severity | file:line | claim as written | correct value | source URL | retrieval date`
> Do NOT fix anything. Do NOT commit. Report only.

## Check every category — none are optional

1. **Framework identifiers** — every Category/Subcategory/control/criteria code exists in the real spec, with that exact ID format. LLM builds fabricate plausible codes (`GV.SR`, `PR.AC` as CSF 2.0); assume fabrication until verified.
2. **Counts** — every count stated anywhere (function counts, subcategory counts, criteria counts, PoF counts). Count them yourself in the source document. Builds are reliably wrong by ±2.
3. **Versions** — every version reference is the current published version. If a newer version/revision exists, or the cited one was withdrawn (e.g. SP 800-61 Rev 2, withdrawn Apr 2025), flag it. Watch for fabricated versions (`Rev 5.1.1`).
4. **URLs** — every §10 manifest URL returns 200 right now (not 404/410/redirect-to-homepage). Known rot zones: AICPA `/resources/`, COSO guidance pages, ISACA ITAF paths, NIST revision-specific URLs, FedRAMP `/resources/`.
5. **Crosswalk rows** — every mapping row matches the authoritative cross-reference (e.g. NIST IR informative references). Spot-check at minimum 20 rows or 100%, whichever is smaller.
6. **Terminology** — framework-specific terms match the source's exact wording (Tier 1 = "Partial", not "Initial").
7. **Cross-chunk consistency** — any fact stated in more than one file says the same thing everywhere (grep for the fact; list every location).
8. **Supersession claims** — "X supersedes Y" claims match the publisher's own supersession notice.

## Output contract

- Findings table (format above), ordered CRITICAL → LOW.
- A verification summary appended to (or creating) `skills/{{skill_slug}}/docs/acceptance-gate.md`: `fact | source | retrieval date | verifier | status` — one row per category checked, minimum 20 rows for a new skill.
- Explicit statement of what you did NOT check, so the next pass knows the residual risk.

## Re-verify mode (pass 4)

After a fix pass, rerun this prompt scoped to: (a) every finding from the previous run — confirm fixed; (b) every file the fix agent touched — fix agents introduce new errors. Same output contract.
