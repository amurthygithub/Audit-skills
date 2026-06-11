# Telemetry Baseline (TEMPLATE)

> This file is the **shell** every skill copies. Populate it after the first instrumented run on each use case.

## Methodology

- **Environment**: model + version (e.g., `gpt-4o-2024-08-06`), region.
- **Run size**: N invocations per use case (target: N ≥ 30 for stable p90).
- **Seed strategy**: pinned seeds; same input across runs.
- **Cache**: cache disabled for baseline measurement; re-run with cache on to estimate hit-rate impact.
- **Redaction**: redaction ON; events stripped of free-form PII.

## Per-Use-Case Table

| UC | Industry | Model | input_p50 | input_p90 | output_p50 | output_p90 | total_p90 | latency_p90_ms | cache_hit_rate |
|----|----------|-------|-----------|-----------|------------|------------|-----------|----------------|----------------|
| UC-01 | — | — | — | — | — | — | — | — | — |
| UC-02 | — | — | — | — | — | — | — | — | — |
| UC-03 | — | — | — | — | — | — | — | — | — |

## Cross-Use-Case Aggregates

| Metric | p50 | p90 | p99 |
|--------|-----|-----|-----|
| input_tokens | — | — | — |
| output_tokens | — | — | — |
| total_tokens | — | — | — |
| latency_ms | — | — | — |

## Revisions

| Date | Skill version | Model | Notes |
|------|---------------|-------|-------|
| YYYY-MM-DD | 0.1.0 | — | Initial baseline. |
