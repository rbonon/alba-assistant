# Alba Context Assistant — product vision

> English summary. Full vision input: [`../vision/alba-context-assistant-handoff.html`](../vision/alba-context-assistant-handoff.html)

## What

Alba is a **personal/family context assistant** that remembers, retrieves, and reuses knowledge from:

- **Google Drive/Docs** — primary human memory (`Root_*/Alba/` per workspace; D-039, D-041)
- **Git** — technical truth (code, docs, agent context files; Ricardo `ideas/`, `habilidades/`)
- **Obsidian** — optional human memory editor (primarily Ricardo); mirrors `Alba/` if used (D-044)
- **Calendar / Tasks** — operational systems (post-MVP integrations)
- **RAG index** — regenerable search layer (not primary storage)
- **MCP/API** — standard access for Cursor, Claude Code, ChatGPT, mobile, voice

## Who

| Workspace | Primary users | Persona (MVP) |
|-----------|---------------|---------------|
| `ricardo` | Ricardo | Alba Dev — technical, implementation-focused |
| `gisele` | Gisele | Alba Texto — writing, clarity, preserves voice |
| `casa` | Family | Alba Casa — practical daily use (either user in `casa` context) |
| `compartilhado` | Shared | Cross-family context |

Personas are fixed per user at MVP (D-017). Switching/custom personas may be added post-go-live.

## Architectural invariants

```text
Canonical sources ≠ RAG index
Human memory canon: Drive/Docs + Git (+ optional Obsidian for Ricardo)
AI writes → `Root_*/Alba/…`; searchable after TTL — no mandatory inbox promote (D-042)
All search filtered by user + allowed workspaces (see D-016: own + `compartilhado` + `casa`; never peer private workspace)
Never index secrets, .env, node_modules, build output, clinical/sensitive content
Start read-only; prove in staging before production
```

## Proposed stack (TBD — lock in P2)

TypeScript/Node.js, SQLite metadata, LanceDB or Chroma vectors, HTTP API + MCP server. Details in grilling P2.

## GitHub org (planned)

Repos today: **`rbonon/alba-assistant`**, **`rbonon/alba-docs`**. Planned **`Alba` GitHub org** for all Alba projects; migrate when ready (native Epic issue types, shared board conventions).

## Milestone

**MVP:** Ricardo and Gisele can query their context (**Drive/Docs + Git** + optional Obsidian) via hybrid search in **staging**, then **production** — read-only, workspace-filtered, MCP-enabled. User model extensible for more users after launch.
