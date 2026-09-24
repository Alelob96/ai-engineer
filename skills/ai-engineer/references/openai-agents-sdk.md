# OpenAI Agents SDK

Use when a managed runtime for a bounded agent loop, function tools, guardrails, handoffs, MCP, and traces has concrete value. Check the installed `openai-agents` package and current Python SDK documentation; API signatures and defaults can change.

Set maximum turns and external tool budgets at the application boundary, and understand what an SDK turn counts. Derive authority from application context for each tool invocation. Choose handoffs only when the receiving specialist should own the answer; choose an agent-as-tool when the parent should retain control. Guardrails can inspect inputs, outputs, or tool calls but are not a replacement for app-side authorization. Check how approval pauses and resumption bind to the specific proposed write.

Review tracing defaults before processing sensitive text; add correlation IDs without leaking credentials or personal data. Aggregate usage from the actual run/model calls, including specialists, without double-counting aggregate and per-call values. Cover handoff termination, tool failure, approval denial, and max-turn behavior with tests.

Official entry point: https://developers.openai.com/api/docs/guides/agents/sdk .
