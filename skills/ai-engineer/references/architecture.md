# Architecture selection

Start with the user-visible outcome, authority boundary, latency target, persistence requirements, and expected failure modes. Compare a deterministic workflow with the smallest agent that could meet the same requirements.

| Need | Default option | Escalate when |
| --- | --- | --- |
| Extraction or one bounded generation | Plain Python + Responses API | Tool selection is genuinely model-driven |
| Explicit tool loop with application-owned dispatch | Responses API | Built-in agent lifecycle materially helps |
| Agent loop, function tools, handoffs or built-in tracing | OpenAI Agents SDK | Explicit graph state or custom recovery is required |
| Branches, cycles, checkpoints or interrupt/resume | LangGraph | A managed graph runtime is actually needed |
| RAG without adaptive retrieval | Deterministic retrieve → synthesize | Coverage-based search reformulation demonstrably helps |

Choose one runtime to own the loop; use the other SDKs only for distinct capabilities. Multi-agent only when independently scoped specialists or ownership handoffs improve measured quality or maintainability. Prefer deterministic routing for authorization, billing, persistence, tenant scoping, and side effects. Keep long runs off request threads if they must survive process restarts; set concurrency and cancellation boundaries for async services.

Write a short decision record: alternatives, chosen runtime, state lifetime, storage/checkpoint strategy, user approvals, budget and termination, security boundary, test and eval plan. Check installed package versions and current official documentation before naming APIs. Do not create extra abstractions when an existing repository convention suffices.
