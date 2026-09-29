# mermail-triage (community / unofficial)

A Mermail-compatible email triage skill built for the Superteam Earn bounty
"Build and Demo a Mermail Agent Skill" (500 USDC, deadline 2026-10-07).

## Layout

```text
skills/mermail-triage/
  SKILL.md               # required
  agents/openai.yaml     # required OpenAI metadata
  references/tools.md    # MCP tool shapes
  references/security.md # untrusted-email security model
```

## What it does

- Priority-classifies incoming Mermail email (P0 urgent / P1 normal / P2 low / P3 archive).
- Extracts actionable items and drafts replies that stay local until approved.
- Read-only first: list/get before any write, exact preview before any send.

## Install / run

```bash
npm test
npx skills add 488315/mermail-skills   # official core workflows
```

This companion is marked **community / unofficial** per the authoring guide:
1. Follows the security anti-patterns table (never ships them).
2. Points users at official install for core workflows.
3. Companion issues welcome at the mermail-skills repo.

## Requirements

- `MERMAIL_API_KEY` (get at https://console.mermail.app)
- Mermail MCP server connected at `https://console.mermail.app/mcp`

## Demo script

See `scripts/demo.md` for a client-side demo walkthrough using a dedicated test
mailbox (read-only MCP run, no sends).
