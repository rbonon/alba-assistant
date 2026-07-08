# CLAUDE.md — Project Context
# Behavioral rules are in .claude/CLAUDE.md and loaded automatically by Claude Code

@AGENTS.md

## Why

Ricardo and family need a context assistant that preserves research, decisions, code patterns, recipes, and project knowledge across AI sessions — without losing data in chat history or duplicating Git in Obsidian.

## What

Greenfield product repo: **P1** — requirements & spec. Docs portal on GitHub Pages (`/docs`). Engine code starts P6+ after planning gates (Alba board) / after master implementation gate (`rbo-product-*` suite).

Stack TBD in P2. Integrations: Obsidian, Git, MCP (MVP); Calendar, Tasks, Drive, Android, Alexa (later).

## How

- **Planning:** GitHub Project `alba-assistant`, grilling, `docs/planning/`
- **Implementation:** OpenSpec + `feat/<change-name>` branches from P6+
- **Verify:** staging deploy → validation → production go-live checklist
- **Refresh:** `scripts/refresh-roadmap.sh` after board updates

## Milestone

**Current:** P1 — Requirements & spec v1. P0 complete (gate #13 closed).

**Next:** `rbo-create-change` on issue #14 → Q-001 grilling. See [`docs/planning/session-handoff.md`](docs/planning/session-handoff.md).
