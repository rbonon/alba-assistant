# alba-assistant — AI agent context

## What this repo is

**Alba Context Assistant** — a personal/family context platform that indexes Obsidian notes and Git repositories into a regenerable RAG layer, exposed via HTTP API and MCP. Canonical human memory lives in Obsidian; technical truth in Git; RAG is never primary storage.

This repo is the **runtime/engine** repo. Related: `rbonon/alba-docs`. Planned migration to an **Alba GitHub org**.

## Structure

```
alba-assistant/
├── docs/
│   ├── index.html              # GitHub Pages portal (English)
│   ├── vision/                 # Vision handoff (input, not final spec)
│   ├── planning/               # Product canon + generated board-hierarchy
│   ├── spec/                   # Requirements (P1)
│   ├── architecture/           # Architecture detail (P2–P3)
│   └── operations/             # Bootstrap, go-live (P4)
├── openspec/                   # OpenSpec (implementation from P6+)
├── scripts/                    # refresh-roadmap, refresh-board-hierarchy
├── AGENTS.md                   # This file
├── DECISIONS.md                # Append-only decision log
├── STATUS.md                   # Session compass
└── ROADMAP.md                  # Generated from GitHub Project board
```

## Key files

- `docs/vision/alba-context-assistant-handoff.md` — vision input (Portuguese)
- `docs/planning/README.md` — planning index
- `docs/planning/phases.md` — P0–P14 sequencing
- `docs/planning/open-questions.md` — grilling backlog
- `DECISIONS.md` — locked decisions (read before significant work)

## Tech stack

**TBD — lock in P2 grilling.** Proposed: TypeScript/Node.js, SQLite, LanceDB or Chroma, Fastify, MCP server.

## Architecture and design

See `docs/planning/architecture.md` and `DECISIONS.md`. Invariants:

- Obsidian = human memory; Git = technical memory
- RAG = regenerable index
- Workspace-filtered retrieval (`ricardo`, `gisele`, `casa`, `compartilhado`)
- AI writes only to `Inbox/AI Drafts` until human promotes
- Staging before production for every slice
- Never index secrets, `.env`, `node_modules`, clinical/sensitive content

## Important rules

- **No implementation** until `[Gate] P5` (roadmap approved)
- Use **`rbo-create-issue`** → **`rbo-create-change`** → **`rbo-close-change`** for delivery work
- Use **`rbo-grilling`** for spec/arch decisions (one question at a time)
- Never hand-edit `ROADMAP.md` or `docs/planning/board-hierarchy.md` — regenerate via scripts
- Append to `DECISIONS.md` only — never overwrite entries
- GitHub Project board title = **`alba-assistant`**

## Working with this repo as an AI agent

- Read `DECISIONS.md` before significant changes
- Read `STATUS.md` for current phase and next step
- Update planning docs and portal pages as phases complete
- Run refresh scripts after board changes
