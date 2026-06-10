# prompts/ — version-controlled agent prompts for the G4 verify stage

Every review pass in the G0–G6 pipeline uses the prompt file in this directory **verbatim** — fill in the `{{placeholders}}`, dispatch, done. Do not improvise review instructions: improvised prompts drift, skip checks, and make runs non-comparable.

If a prompt is inadequate, improve the file in a PR. That is the ratchet — the prompt gets better for every future run, not just yours.

| File | G4 pass | Dispatched as |
|---|---|---|
| [five-lens-review.md](five-lens-review.md) | 1. Structure/convention review | 5 agents in parallel, one per lens |
| [s511-verification.md](s511-verification.md) | 2. Source-of-truth verification + 4. Re-verify | 1+ agent per skill, **webfetch required** |
| [fix-pass.md](fix-pass.md) | 3. Apply findings | 1 agent per skill, parallel across skills |
| [persona-vetting.md](persona-vetting.md) | 5a. Practitioner + industry vetting (G4.5) | 5 agents in parallel, one per persona |
| [consumer-smoke-test.md](consumer-smoke-test.md) | 5b. Fresh-agent usability test (G4.5) | 1 clean agent session per use case |

Findings from every pass use the shared severity scale:

- **CRITICAL** — factually wrong, fabricated, or broken; blocks release
- **HIGH** — misleading or convention-breaking; fix before merge
- **MEDIUM** — quality gap; fix or ticket
- **LOW** — nice-to-have
