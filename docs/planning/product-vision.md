# Alba Context Assistant — product vision

> English summary. Full vision input: [`../vision/alba-context-assistant-handoff.md`](../vision/alba-context-assistant-handoff.md)

## What

Alba is a **personal/family context assistant** that remembers, retrieves, and reuses knowledge from:

- **Obsidian** — human memory (notes, research, recipes, decisions)
- **Git** — technical truth (code, docs, agent context files)
- **Calendar / Tasks / Drive** — operational systems (later integrations)
- **RAG index** — regenerable search layer (not primary storage)
- **MCP/API** — standard access for Cursor, Claude Code, ChatGPT, mobile, voice

## Who

| Workspace | Primary users | Persona |
|-----------|---------------|---------|
| `ricardo` | Ricardo | Alba Dev — technical, implementation-focused |
| `gisele` | Gisele | Alba Texto — writing, clarity, preserves voice |
| `casa` | Family | Alba Casa — practical daily use |
| `compartilhado` | Shared | Cross-family context |

## Architectural invariants

```text
Canonical sources ≠ RAG index
AI writes → Inbox/AI Drafts only (human promotes)
All search filtered by user + allowed workspaces
Never index secrets, .env, node_modules, build output, clinical/sensitive content
Start read-only; prove in staging before production
```

## Proposed stack (TBD — lock in P2)

TypeScript/Node.js, SQLite metadata, LanceDB or Chroma vectors, HTTP API + MCP server. Details in grilling P2.

## GitHub org (planned)

Repos today: **`rbonon/alba-assistant`**, **`rbonon/alba-docs`**. Planned **`Alba` GitHub org** for all Alba projects; migrate when ready (native Epic issue types, shared board conventions).

## Milestone

**MVP:** Ricardo can query his context (Obsidian + Git) via hybrid search in **staging**, then **production** — read-only, workspace-filtered, MCP-enabled.
