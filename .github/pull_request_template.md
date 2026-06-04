<!--
Welcome! Audit-skills is a content library - most PRs are content edits.
A maintainer will review within ~3 days. The two commands below catch
the structural issues; you don't need to learn git terminology.
-->

## What changed
<!-- One or two sentences. Example: "Added healthcare industry view to coso-internal-controls." -->

## Why
<!-- One sentence. Example: "Closes #42 - healthcare was the most-requested missing industry." -->

## Skill affected
<!-- Tick one or more, or write in a new skill's slug. -->
- [ ] nist-800-53-rmf
- [ ] isaca-audit-methodology
- [ ] coso-internal-controls
- [ ] aicpa-soc-reporting
- [ ] audit-workpapers
- [ ] new skill (slug: `__________`)
- [ ] repo-wide (CI, linter, README, no specific skill)

## Test evidence
<!-- Paste the output of these two commands run from the repo root:
     python tools/lint_skill.py skills/nist-800-53-rmf skills/isaca-audit-methodology skills/coso-internal-controls skills/aicpa-soc-reporting skills/audit-workpapers
     pytest skills/ tests/ -q
     "OK" / "X passed" is enough; we trust the green light. -->

```
<paste terminal output here>
```

## Breaking change?
<!-- A breaking change means an existing LLM agent loading this skill
     by manifest URL would need to update. Rare for content edits;
     common only for renames, slug changes, or manifest schema bumps. -->
- [ ] No
- [ ] Yes - describe below

## Related issue
<!-- "Closes #42" or "None". -->
