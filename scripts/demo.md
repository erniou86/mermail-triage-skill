# Demo walkthrough: mermail-triage (read-only, no sends)

Client-side demo using a dedicated test mailbox.

## Prereqs

1. `MERMAIL_API_KEY` exported in env (never paste into chat).
2. Mermail MCP server connected: `https://console.mermail.app/mcp`.
3. A dedicated test mailbox with 3–5 known messages (mixed: urgent invoice, product
   newsletter, spam-like marketing, a question thread).

## Steps

```text
1. Mermail:list_workspaces
   -> pick workspace id W

2. Mermail:list_mailboxes (workspaceId: W)
   -> pick test mailbox public_id M

3. Mermail:list_emails (mailboxId: M, limit: 10)
   -> capture message ids

4. For each id: Mermail:get_email
   -> classify per SKILL.md table (priority/category/action)

5. Produce triage table:

   | sender | subject | priority | category | one-line summary |
   | --- | --- | --- | --- | --- |

6. For P0: surface to user immediately.
   For P1 with a draft request: compose Mermail:create_draft, show exact preview
   with recipients, await approval. Do NOT send without approval.
7. Summarize: completed reads, classifications, drafts pending approval, skips.
```

## Acceptance criteria

- 37+ deterministic tests pass (see repo test suite).
- Real read-only MCP run processed at least 3 explicitly approved demo messages.
- No send/invite/wallet tool invoked during demo.
