## Context

- **Prior locks:** D-005 MCP/API access layer; D-015 multi-user; D-016 workspace read boundaries; D-017 persona mapping; D-021 ephemeral chat; D-031 API/MCP IN at MVP; D-033 isolation tests; D-034 Artur staging stand-in; features.md lists `search_memory`, `get_decisions`, `get_project_context`
- **Issue #21 scope:** Cursor/Claude first; tools, auth, workspace enforcement at client boundary
- **Open:** Q-008 auth mechanism (P2/P3) — #21 locks **requirements** at client boundary, not credential implementation

## Goals / Non-Goals

**Goals:**
- Lock **MVP client priority** (Cursor MCP, Claude Code, ChatGPT/Claude API)
- Lock **MCP tool catalog** and read-only MVP scope
- Lock **auth/session model** at client boundary (per-user identity → workspace RBAC)
- Lock **workspace enforcement** — where D-016 is applied (server-side; client hints)
- Lock **chat UI vs IDE MCP** relationship (D-021 ephemeral threads)

**Non-Goals:**
- MCP transport implementation (stdio vs SSE — P2)
- OAuth/token storage mechanism (P2/P3)
- Runtime MCP server code (P7)
- Write tools (P8)

## Decisions

_(Populated during grilling — one question at a time via `rbo-grilling`)_

| ID | Topic | Status |
|----|-------|--------|
| #21-Q-001 | MVP client priority (Cursor vs Claude Code vs ChatGPT/Claude) | **Open** |
| #21-Q-002 | MVP MCP tool catalog and read-only scope | **Open** |
| #21-Q-003 | Auth/session at client boundary (per-user identity) | **Open** |
| #21-Q-004 | Workspace enforcement — server vs client responsibilities | **Open** |
| #21-Q-005 | ChatGPT/Claude chat as client vs IDE-native MCP | **Open** |
| #21-Q-006 | Staging (Artur) vs production client configuration | **Open** |

## Risks / Trade-offs

- [Chat clients lack native MCP] → may need API bridge or connector — define at grilling
- [Workspace leakage] → enforcement must be server-side (D-033); client params are hints only
- [Q-008 overlap] → #21 locks requirements; P2 locks mechanism

## Open Questions

See table above. Grilling starts with **#21-Q-001**.
