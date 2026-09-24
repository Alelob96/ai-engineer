# LangGraph

Use when explicit typed state, conditional routing, checkpointing, pause/resume, or custom recovery paths materially simplify a workflow. Verify the installed `langgraph` version and current Python docs before naming graph APIs.

Design a state schema with immutable request/principal context, evidence and provenance, budgets, attempts, stop reason and output. Nodes should return minimal updates rather than silently mutate shared state. Keep routing explicit and bounded; avoid loops without measurable progress. Compile with an appropriate production checkpointer when durability or interrupts are required. Bind thread/checkpoint IDs to authenticated tenant and principal.

An interrupted or failed node may execute again when resumed. Keep side effects idempotent, place approvals before writes, and isolate non-idempotent work in carefully designed tasks/nodes. Use node-level retry for transient failures, structured state feedback for model-correctable errors, interrupt for missing user decisions, and surfaced exceptions for unknown bugs. Configure attempt timeouts and total run limits separately. Verify checkpointer schema migrations, cleanup, and retention.

Test checkpoint/resume with a write, cancellation, retry exhaustion, loop bound, and a cross-tenant resume attempt. Official entry points: https://docs.langchain.com/oss/python/langgraph/thinking-in-langgraph and https://docs.langchain.com/oss/python/langgraph/interrupts .
