# CLAUDE.md — Project Context
# Behavioral rules are in .claude/CLAUDE.md and loaded automatically by Claude Code

@AGENTS.md

## Why

Ricardo and family need a context assistant that preserves research, decisions, code patterns, recipes, and project knowledge across AI sessions — without losing data in chat history or duplicating Git in Obsidian.

## What

Greenfield product repo: planning phase (P0). Docs portal on GitHub Pages (`/docs`). Engine code starts P6+ after spec, architecture, environments, ops, and roadmap gates.

Stack TBD in P2. Integrations: Obsidian, Git, MCP (MVP); Calendar, Tasks, Drive, Android, Alexa (later).

## How

- **Planning:** GitHub Project `alba-assistant`, grilling, `docs/planning/`
- **Implementation:** OpenSpec + `feat/<change-name>` branches from P6+
- **Verify:** staging deploy → validation → production go-live checklist
- **Refresh:** `scripts/refresh-roadmap.sh` after board updates

## Milestone

**Current:** P0 — Product foundation (portal, board, agent context).

**Next gate:** `[Gate] P0` → begin P1 requirements grilling.
