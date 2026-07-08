# CLAUDE.md — Project Context
# Behavioral rules are in .claude/CLAUDE.md and loaded automatically by Claude Code

@AGENTS.md

## Session start (read first)

**At the start of any session — and whenever `rbo-catch-up` runs — read
[`docs/planning/session-handoff.md`](docs/planning/session-handoff.md) before
recommending or doing anything.** It is the session baton: current state, issue
map, and the exact next step. Do not wait to be told; open it automatically.

## Why

Ricardo and family need a context assistant that preserves research, decisions, code patterns, recipes, and project knowledge across AI sessions — without losing data in chat history or duplicating Git in Obsidian.

## What

Greenfield product repo: **P1** — requirements & spec. Docs portal on GitHub Pages (`/docs`). Engine code starts P6+ after planning gates (Alba board) / after master implementation gate (`rbo-product-*` suite).

Stack TBD in P2. Integrations: Drive/Docs, Git, optional Obsidian, MCP (MVP); Calendar, Tasks, Android, Alexa (later).

## How

- **Planning:** GitHub Project `alba-assistant`, grilling, `docs/planning/`
- **Implementation:** OpenSpec + `feat/<change-name>` branches from P6+
- **Verify:** staging deploy → validation → production go-live checklist
- **Refresh:** `scripts/refresh-roadmap.sh` after board updates

## Milestone

**Current:** P1 — Requirements & spec v1. P0 complete (gate #13 closed).

**Next:** `rbo-create-change` on **#22 — [Grill] P1 — Google Calendar scope**. #14–#21 closed (D-015–D-057).
