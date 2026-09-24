# Bounded loop and error handling

Define stop reasons before coding: completed, insufficient evidence, user input needed, approval required, policy denied, budget exhausted, cancelled, timeout, and unrecoverable error. Each iteration checks remaining wall time, model calls, tool calls, token budget and cost cap **before** work starts; verify limits again after a call. Stop on repeated identical tool calls without new evidence. A budget breach yields a controlled partial answer or escalation, not an unbounded extra model call.

Typical sequence: model response → validate all requested calls → authorize → apply side-effect approval policy → execute bounded tools → normalize observations → update state/usage → evaluate stop condition → call model again if permitted. Where parallel calls are supported, count and authorize each separately; avoid assuming only one call per model turn. Preserve provider-required reasoning/context items when returning tool outputs; do not expose private reasoning to users.

| Error class | Owner | Handling |
| --- | --- | --- |
| Transient network, rate limit, service failure | Infrastructure | Bounded retries with jitter/backoff, timeout, idempotency; honor retry hints |
| Invalid tool arguments or retriable domain choice | Agent | Structured, sanitized actionable observation; cap correction attempts |
| Missing user information or approval | User | Pause/interrupt with a specific request; persist state before resuming |
| Permission, tenant, policy or secret exposure | Application | Deny and audit; never ask the model to work around denial |
| Unexpected bug or exhausted recovery | Developer | Preserve restricted diagnostics; fail predictably |

Do not let a model retry an HTTP 503 by repeatedly selecting the same tool. Separate provider SDK retries, tool transport retries, graph retries, and semantic replanning; otherwise their attempt counts multiply. Cancel child tasks and release resources when a run is cancelled. For long-running graphs, design writes and node boundaries for replay after a crash.
