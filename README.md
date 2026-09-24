# ai-engineer

An English-language Agent Skill for designing, implementing and reviewing secure, bounded, observable Python AI agents and RAG systems. It covers OpenAI Responses API, OpenAI Agents SDK, LangGraph, tool/MCP design, failure handling, multi-tenant security, token and cost tracking, and evaluations.

## Layout

```text
ai-engineer/
├── skills/ai-engineer/
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   └── references/*.md
├── scripts/validate_skill.py
└── .github/workflows/validate.yml
```

The `SKILL.md` is the entry point. References are read only when relevant. This repository provides instructions and design checks, not an application framework or version-pinned copy/paste SDK templates.

## Install

From the published GitHub repository:

```bash
npx skills add OWNER/ai-engineer --skill ai-engineer
```

Replace `OWNER` with the GitHub account or organization that publishes this repository. To install locally from the parent directory:

```bash
npx skills add ./ai-engineer --skill ai-engineer
```

Use `-g` for a global installation, or add `-a codex` / `-a claude-code` to select an agent, according to your installed `skills` CLI version. Verify the CLI flags against its current documentation when publishing.

## Validate

```bash
python scripts/validate_skill.py
```

This checks the skill frontmatter, file naming, local links, and repository layout without requiring an API key. Use realistic agent tasks and code reviews to evaluate the skill's behavior before a public release.

## License

MIT. See [LICENSE](LICENSE).
