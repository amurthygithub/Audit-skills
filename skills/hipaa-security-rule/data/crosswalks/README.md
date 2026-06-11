# Crosswalks — hipaa-security-rule

`hipaa-to-800-53-r511.json` — the COMPLETE Security Rule -> SP 800-53 Rev 5.1.1 mapping
(68 Security Rule elements, 279 rows, 108 unique controls), vendored from the same
generated artifact as `skills/nist-800-53-rmf/data/seeds/hipaa-to-800-53.json`.
Source: NIST CPRT, SP 800-66 Rev 2 framework, OLIR set
SP-800-66-Rev-2-to-SP-800-53-Rev-5.1.1 (extraction archived at
`docs/builds/sox-638/cprt-extraction.json`, retrieved 2026-06-10; regenerate with
`skills/nist-800-53-rmf/data/generators/gen_hipaa_crosswalk.py`). Rows are OLIR
informative references — no exact/partial strength ratings exist in the source.
The companion CSF mapping in the same CPRT data targets CSF v1.1 only ("intentionally
broad" per SP 800-66r2 Appendix D) and is deliberately NOT encoded here.
