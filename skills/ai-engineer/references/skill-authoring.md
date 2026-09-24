# Authoring an AI engineering skill

Give each skill one coherent job and a precise `name` plus trigger-oriented `description` in YAML frontmatter. Keep `SKILL.md` short and imperative: operating sequence, invariants, and direct links to optional references. Load only the needed reference for a particular task. Put stable procedures in references; do not copy fast-changing API signatures or pricing into the core. Include scripts only when deterministic computation is needed repeatedly, and test executable scripts.

For a public repository, use `skills/<name>/SKILL.md`, supporting `references/` and optional `agents/openai.yaml` next to it. Keep repository-level README, license and CI outside the skill directory. Review instructions for prompt injection and for conflict with explicit user directions. Validate frontmatter and every local link. Test realistic requests for architecture, review, tool failure and security; adjust the skill when its advice causes the wrong level of abstraction or omits a real constraint.

Confirm current `npx skills` install flags in the maintained CLI documentation before publishing installation commands. For the `ai-engineer` repo, the documented form is `npx skills add OWNER/ai-engineer --skill ai-engineer` after publishing to GitHub. Installation from a local directory uses `npx skills add ./ai-engineer`.
