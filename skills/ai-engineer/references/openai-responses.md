# OpenAI Responses API

Use when application code should own state, tool dispatch, retries and loop limits. Read current official OpenAI docs for the installed `openai` Python package before using specific methods or schemas.

Preserve the model's tool call identifier when returning each tool result. Validate JSON arguments against a strict schema, then apply server-side permission and budget checks. Handle multiple tool calls in a response if supported. Return sanitized observations and continue only while the enclosing application loop permits. Follow current model-specific instructions for passing reasoning items and response continuation; never expose private reasoning or assume a plain text message is the entire response.

Use documented response usage fields to record token counts per call. Treat missing usage as unknown. Distinguish built-in tools executed by OpenAI from application-executed function calls for authorization, accounting and logging. Test the completed response, the correctable bad-argument path, a blocked write, a timeout, and budget exhaustion.

Official entry points: https://developers.openai.com/api/docs/guides/function-calling and https://developers.openai.com/api/docs/guides/reasoning .
