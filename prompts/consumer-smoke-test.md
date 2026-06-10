# Consumer smoke test — G4.5 (consumer-ready gate), part of SOX-633

Run **1 clean agent session per use case**. "Clean" means: a fresh agent with NO repo context, no AGENTS.md, no design docs — only what a real consumer has: the skill folder contents and this UC's input. This is the difference between "the markdown lints" and "the skill works as a prompt."

When the Epic 6 harness lands (SOX-600), this becomes automated (N runs per golden case, pass-rate ≥95%, cross-model matrix per SOX-604). Until then it is manual and mandatory for every new skill.

## Procedure (per use case)

1. **Setup:** new agent session. Provide only `skills/{{skill_slug}}/` (as the consumer's installed skill) — nothing else from the repo.
2. **Input:** paste the UC's input verbatim from `use-cases/uc-{{NN}}-*.md` (the input block only — not the procedure or expected output).
3. **Ask** the agent to perform the UC's task using the skill.
4. **Observe, don't steer.** No hints, no corrections, no "try section 7." If the agent asks a clarifying question a real consumer couldn't answer, that is itself a finding.
5. **Grade** the output against the UC's oracle assertions:
   - every oracle assertion: PASS / FAIL
   - routing: did the agent reach the right chunk(s) via SKILL.md §11, or wander?
   - citations: does the output cite real manifest entries (§10), or invent sources?
   - fabrication: any identifier/count/claim not present in the skill or its sources?

## Grading

| Result | Criteria |
|---|---|
| **PASS** | All oracle assertions hold; no fabricated identifiers; routing reached the intended content |
| **PASS-WITH-NOTES** | Oracle holds but routing wandered or output needed cosmetic cleanup — file MEDIUM findings |
| **FAIL** | Any oracle assertion fails, any fabricated identifier, or the agent could not complete the task from the skill alone |

## Output contract

Append one row per UC to `skills/{{skill_slug}}/docs/acceptance-gate.md`:
`smoke-test uc-NN | model used | result | failed assertions (if any) | date | verifier`

Any FAIL blocks release. A FAIL is a defect in the **skill** (routing, templates, missing guidance) until proven otherwise — not in the consumer. Fix the skill, re-run the failing UC in another clean session.
