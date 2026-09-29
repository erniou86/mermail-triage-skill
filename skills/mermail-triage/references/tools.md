# Mermail MCP tools

Host-qualified tool names exposed by the `mermail` MCP server
(`https://console.mermail.app/mcp`, streamable HTTP).

## Read tools (safe, use first)

- `Mermail:list_workspaces` — list workspaces the API key can see.
- `Mermail:list_mailboxes` — list mailboxes in a workspace; params include
  `workspaceId` (optional, else default workspace).
- `Mermail:list_emails` — list messages in a mailbox; params include `mailboxId`
  (prefer `public_id`), `limit`, `before`/`after` (ISO timestamps).
- `Mermail:get_email` — single message by id; returns full headers and body.
- `Mermail:get_thread` — full thread by thread id (read-only).

## Write / external-effect tools (require approval)

- `Mermail:create_draft` — compose a draft; **query must be a native JSON object**,
  never a stringified JSON blob.
- `Mermail:update_draft` — edit an existing draft by id.
- `Mermail:send_email` — external effect; requires exact preview + user approval.
- `Mermail:archive_email` / `Mermail:mark_read` — state changes, non-destructive.

## Destructive / wallet tools

- `Mermail:prepare_destructive_action` — obtain a short-lived token bound to the
  exact tool + arguments before any destructive call.
- `Mermail:paybox_*` / wallet tools — OAuth-only, full-profile required; never
  claim the API key can call wallet tools.

## Conventions

- `query` arguments are native JSON objects, never stringified.
- Prefer `public_id` over internal ids for `mailboxId`.
- Credit / plan caveats: list/get calls consume plan quota; cap `limit` to what is
  needed (default 10, hard cap 50).
