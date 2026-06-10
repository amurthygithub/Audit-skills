# Fix pass — G4 pass 3

Dispatch **1 agent per skill**, in parallel across skills. Each agent receives this file with the findings table pasted in.

> **You are applying the EXACT findings below to `skills/{{skill_slug}}/`. Nothing else.**
>
> {{findings_table — paste the §5.11 / 5-lens findings verbatim, with file:line and expected values}}

## Rules

1. **Fix only what is listed.** No opportunistic rewrites, no style improvements, no reorganizing. Every unlisted change makes re-verification harder.
2. **Use the expected value from the finding — and check its provenance.** For external framework facts, the finding must cite a live source (URL + quote). If it only says "reviewers agree" or has no source, do NOT apply a new specific claim — either flag it back as "needs source" or replace the wrong claim with a verify-against caveat. Concurrence between reviewers is not a source.
3. **Edit files in the repo path** (`/Users/amurthy/Code/Audit-skills/skills/{{skill_slug}}/`), never `~/.config/opencode/skills/`. Historically ~60% of fix agents get this wrong.
4. **Do NOT commit. Do NOT push.** The dispatcher reviews `git diff` and commits.
5. **Keep counts synchronized.** If you fix a count in one file, grep for the same count in every other file of the skill and fix all occurrences — partial fixes create the self-contradictions the next verification pass will flag.
5a. **The seed + oracle are the contract.** If a finding reveals a UC document disagreeing with its seed or its oracle tests, rebuild the DOC to the tested fixture (or change the contract everywhere at once — seed, stub, oracle, doc, README — in the same pass). Never patch one artifact in isolation.
5b. **Label house conventions; never attribute them.** Any formula, scale, weighting, or rollup that is not verbatim in a cited source must be labeled "house convention / illustrative heuristic" — do not leave (or add) attribution of invented math to a named publication.
5c. **Caveats are prose, not tags.** A shipped caveat reads "verify X against Y before client use." Never write `[VERIFY: ...]` author-TODO markers — the linter rejects them outside the changelog.
6. **Run the gates before reporting done:**
   ```bash
   python3 tools/lint_skill.py skills/{{skill_slug}}
   python3 -m pytest skills/{{skill_slug}}/tests/ tests/test_consistency_lib.py -q -p no:asyncio
   ```
7. **Report back:** findings fixed (with file:line of each edit), findings skipped and why, gate output pasted.

After all fix agents complete, the dispatcher MUST run the re-verify pass (`prompts/s511-verification.md`, re-verify mode). Fix agents introduce new errors; an unverified fix pass is an unfinished fix pass.
