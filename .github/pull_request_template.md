<!--
Welcome! Audit-skills is a content library - most PRs are content edits.
A maintainer will review within ~3 days. The commands below catch the
structural issues; you don't need to learn git terminology.
Maintainers: every PR follows the G0-G6 pipeline in AGENTS.md.
-->

## What changed
<!-- One or two sentences. Example: "Added healthcare industry view to coso-internal-controls." -->

## Why
<!-- One sentence. -->

## Work type
<!-- Tick one (see AGENTS.md §1). External contributors: B is the common one. -->
- [ ] A — new skill (design doc + fact-sheet required; gates G1-G4 evidence below)
- [ ] B — edit to an existing skill
- [ ] C — tooling / CI / repo-wide
- [ ] D — docs only

## Skill affected
<!-- Tick one or more, or write in a new skill's slug. -->
- [ ] nist-800-53-rmf
- [ ] isaca-audit-methodology
- [ ] coso-internal-controls
- [ ] aicpa-soc-reporting
- [ ] audit-workpapers
- [ ] nist-csf-2
- [ ] new skill (slug: `__________`) — **design doc + fact-sheet required per [CONTRIBUTING.md](../CONTRIBUTING.md)**
- [ ] repo-wide (CI, linter, README, no specific skill)

## Test evidence
<!-- Paste the output of these commands run from the repo root:
     python tools/lint_skill.py skills/nist-800-53-rmf skills/isaca-audit-methodology skills/coso-internal-controls skills/aicpa-soc-reporting skills/audit-workpapers skills/nist-csf-2
     pytest skills/ tests/ -q
     New skills additionally paste:
     python tools/check_fact_sheet.py docs/<slug>-fact-sheet.md
     python tools/check_design_doc.py docs/<slug>-design.md
     "OK" / "X passed" is enough; we trust the green light. -->

```
<paste terminal output here>
```

## Gate evidence (new skills only — work type A)
<!-- Per AGENTS.md §2-3. Delete this section for other work types. -->
- [ ] G1: fact-sheet passes `check_fact_sheet.py` (output pasted above)
- [ ] G2: design doc passes `check_design_doc.py` (output pasted above)
- [ ] G4: §5.11 verification + re-verify done — `skills/<slug>/docs/acceptance-gate.md` has ≥20 rows, no FAIL
- [ ] G4.5: persona vetting done — `skills/<slug>/docs/persona-review.md`, all CRITICAL/HIGH resolved
- [ ] G4.5: consumer smoke test PASS for every UC (rows in acceptance-gate.md)

## Facts changed?
<!-- If this PR changes any factual claim (identifier, count, URL, version,
     crosswalk row), it must be verified against a live source. Cite it: -->
- [ ] No factual claims changed
- [ ] Yes — verified against: `<source URL, retrieval date>`

## Breaking change?
<!-- A breaking change means an existing LLM agent loading this skill
     by manifest URL would need to update. Rare for content edits;
     common only for renames, slug changes, or manifest schema bumps. -->
- [ ] No
- [ ] Yes - describe below

## Related issue
<!-- Linear: "Closes SOX-NNN" (auto-transitions the ticket on merge).
     GitHub: "Closes #42". External contributors: "None" is fine. -->
