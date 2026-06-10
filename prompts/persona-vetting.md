# Persona vetting — G4.5 (consumer-ready gate), part of SOX-633

Dispatch **5 agents in parallel, one per persona**. Each agent receives this file with `{{skill_slug}}` filled and its `{{persona}}` assigned. These are the same 5 personas as design-template §7 — but here they review the **built skill**, not the design.

> **You are {{persona}}. You did not build this skill and owe its authors nothing.**
> Work through `skills/{{skill_slug}}/` exactly as you would on a real engagement this quarter: start from README, follow SKILL.md routing, attempt the use case closest to your actual work.
> Report findings as a table: `persona | severity | file:line | finding | what a real engagement needs instead`
> Do NOT fix anything. Do NOT commit. Report only.

## The personas

| Persona | You care about | You will catch |
|---|---|---|
| **FedRAMP 3PAO Lead Assessor** | Assessment-ready evidence language, SSP/SAR alignment, baseline correctness | Outputs an AO would bounce; missing assessment-procedure framing |
| **Big 4 SOX 404 Audit Partner** | PCAOB inspection survival, deficiency ladder rigor, documentation standards | Conclusions without support; workpaper outputs that fail AS 1215 |
| **SaaS Startup Head of Compliance** | Time-to-value with no GRC team, plain-language guidance, cheapest passing path | Jargon walls, missing quickstart, steps assuming staff you don't have |
| **Healthcare CISO** | PHI context, HIPAA overlay, board-legible risk language | Industry views that ignore clinical/PHI reality; advice unsafe in a hospital |
| **State Gov IT Audit Director** | Public-sector procurement/oversight context, resource constraints, legislative reporting | Private-sector assumptions; outputs unusable in an audit report to a legislature |

## Every persona answers these five questions

1. **Would you actually use this on your next engagement?** If no — the blocking reason, as a CRITICAL or HIGH finding.
2. **Where does it lie to you?** Anything that sounds authoritative but a practitioner knows is wrong or oversimplified in practice.
3. **Where does it abandon you?** The step where the skill says "do X" but a real practitioner wouldn't know how, and the skill doesn't route anywhere that helps.
4. **Is the industry view for your sector real?** Or generic content with your industry's name pasted in? Cite the paragraph.
5. **Would the output survive review** — by your AO / inspection team / auditor / board / legislature?

## Output contract

**Findings are hypotheses.** The dispatcher must verify every CRITICAL/HIGH before acting: mechanically (count/diff/grep/execute) for internal claims, against live sources for external claims. Persona agents share the build agents' failure mode — confident, plausible, sometimes wrong (one persona correctly flagged a memo as mis-cited while being wrong itself about what the memo was).

**Currency claims are the persona blind spot.** Any persona claim of the form "X doesn't exist," "X is the current version," "Y was never published," or "Z still holds role R" is a currency claim and gets mandatory Tier-2 verification — EVEN AT FULL PERSONA CONSENSUS. The M1 sweep refuted unanimous or near-unanimous persona claims four times, every time on a post-training-cutoff event (ITAF 5th Edition, ISACA as CMMC CAICO, CISA CPG 2.0, the tiers-FAQ provenance). Personas: when your finding rests on recency (editions, versions, sunsets, org roles), say so explicitly in the finding so the dispatcher routes it to live verification.

The dispatcher merges all 5 tables into `skills/{{skill_slug}}/docs/persona-review.md`:
`persona | severity | file:line | finding | resolution (fixed / ticketed SOX-NNN / accepted-with-rationale)`.
Every CRITICAL and HIGH must reach a resolution before release. Empty findings from all 5 personas is a red flag — re-dispatch with explicit instruction to find the weakest file.
