# Testing, evaluations, and reviews

Choose checks that could expose real defects. Use deterministic tests for tool schemas, authn/authz, tenant filters, budget stops, retry count, idempotency, and state transitions. Use mocked model/tool traces to exercise branching, then a small representative end-to-end run if credentials and environment allow. Do not require paid live calls just to validate a skill or conceptual design.

Create a small eval set from real task categories and hard cases: normal success, no evidence, contradictory evidence, malformed tool arguments, timeouts/429s, repeated calls, prompt injection in source text, cross-tenant retrieval, denied write, resume after crash, and citation mismatch. Measure task correctness, groundedness, tool choice, latency, usage and cost against a simpler baseline. Keep failures and regression cases for future runs.

For a code review, inspect executable call paths and report severity, precise location, observed or plausible impact, and a concrete fix. Prioritize exploitable access errors and unbounded costs ahead of formatting or speculative refactors. For implementation, report commands actually run and their outcome. Distinguish verified behavior from assumptions and unknowns.
