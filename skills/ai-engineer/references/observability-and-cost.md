# Observability, usage, and cost

Emit structured application events, not raw conversation dumps. Useful INFO events: `run_started`, `model_completed`, `tool_completed`, `run_completed`, `run_failed`, `approval_requested`. Include run/trace IDs, stage, tool/model identifier, outcome, stop reason, latency, retry count, call count, and usage where available. DEBUG may include sanitized routing decisions, retrieval scores, and state transitions. Use allowlisted logger names for noisy clients at WARNING by default; do not globally suppress warnings and errors. Keep audit records distinct from development logs.

Measure model usage **per actual billable call**, including failed/retried calls when reported. Aggregate across graph nodes and agents without double-counting the same response. When the provider exposes them, record input tokens, cached input tokens, output tokens, reasoning tokens, total tokens, model identifier, and whether each value is observed or unknown. Cached input is a subset of input; reasoning is a subset of output. Do not add either twice. A count of reasoning tokens is not the content of private reasoning.

For a known, current model price, estimate:

`uncached_input = input_tokens - cached_input_tokens`

`estimate = (uncached_input * input_rate + cached_input_tokens * cached_rate + output_tokens * output_rate) / 1_000_000`

Store rates with currency, source URL, observed date, model/version, units and applicable tiers; include cache-write, tool, storage, or provider charges separately when relevant. If pricing or usage is missing, report cost as unavailable or partial, never zero by default. Do not hard-code time-sensitive prices in the skill. Validate cache pricing and any special billing rules against the official price page at implementation time. Distinguish estimates from invoiced amounts and enforce cost caps on best available usage plus conservative reservations for in-flight calls.

Restrict traces and logs to needed operators; redact secrets and personal information; sample high-volume DEBUG traces; keep trace correlation even when content is omitted. Check framework auto-tracing defaults for sensitive fields.
