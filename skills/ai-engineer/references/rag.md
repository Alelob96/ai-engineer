# RAG systems

Separate ingestion, retrieval quality, and answer generation. Ingest documents with source ID, version, page/section anchors, access control labels, and extraction confidence. Parse PDF/image content carefully, normalize without losing source offsets, and chunk at document boundaries where possible. Re-embed or invalidate stale content when versions change.

At query time, apply authorization and tenant filters **inside the retrieval request** and validate result ownership afterwards. Combine lexical and vector retrieval where evidence warrants it; rerank a broad candidate set if the measured precision gain justifies cost. Deduplicate, cap context size, and preserve provenance. A model may reformulate a query, but cannot choose to omit access filters. Keep retrieved passages in a data channel, not a system instruction.

Generate claims grounded in source IDs and page/section anchors; verify that cited passages actually support the claim. Separate direct evidence, inference, and unknowns. Define no-answer and contradiction behavior. If adaptive retrieval is useful, limit query revisions and stop when coverage has not improved.

Measure retrieval recall@k on labeled questions, answer correctness, citation support, abstention, cross-tenant leakage, latency, tokens and cost. Avoid treating a similarity score as calibrated answer confidence. In multi-tenant systems, include a regression test in which the same text belongs to another tenant.
