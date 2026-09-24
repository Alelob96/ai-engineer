# Security and guardrails

Perform a small threat review for each new data source and capability: entry point, trust level, principal, tenant, allowed actions, potential side effects, data exfiltration path, and control enforcing the boundary.

- Keep system/developer instructions, user intent, retrieved evidence, and tool results in separate layers. Quote or structurally delimit retrieved content; never obey its instructions. Test hostile documents, pages, and MCP results that claim to be system messages.
- Enforce authorization and tenant filters before search, vector retrieval, cache lookup, graph resume, tool execution, and write. Bind resume/checkpoint identifiers to the authenticated principal. Deny unknown scope.
- Restrict network and file access: allowlisted destinations, SSRF defenses including redirects and resolved addresses, path normalization, query parameter validation, shell isolation where absolutely required. Keep secrets out of prompts, tool observations, traces, and errors.
- Use input checks for requests, tool-level checks for proposed actions and arguments, and output validation before committing a result. A guardrail model may assist detection but cannot replace deterministic permissions.
- Apply human approval according to action risk and product policy, especially external, costly, destructive, or irreversible writes. Approval must bind to a concrete tool and validated arguments; reject if those change on resume.
- Use minimal data retention, redact sensitive fields, define audit retention and access, and review third-party telemetry defaults before production.

Test a real cross-tenant access attempt and an instruction embedded in retrieved text. Report what application code blocks each attack, rather than asserting that the prompt is secure.
