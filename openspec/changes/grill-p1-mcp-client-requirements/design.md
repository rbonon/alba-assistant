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

### MVP client priority — validate Cursor → Claude Code → chat (#21-Q-001, 2026-07-08)

**Decision:** All three client paths are **required at MVP go-live** (D-015, D-031). **Build/validation order:**

| Order | Client | Primary user / persona |
|-------|--------|------------------------|
| 1 | **Cursor MCP** | Ricardo — Alba Dev |
| 2 | **Claude Code MCP** | Ricardo — Alba Dev (parity with Cursor) |
| 3 | **ChatGPT / Claude chat** | Ricardo + Gisele — Alba Texto / Casa |

Chat path may use **HTTP API** if native MCP unavailable in chat UI (#21-Q-005) — still required at go-live. Staging must prove all three before prod promote (D-035, D-038).

**Rationale:** “Cursor/Claude first” = sequencing for implementation/QA, not deferring Gisele’s chat surface.

### MVP MCP tool catalog — read-only, five tools (#21-Q-002, 2026-07-08)

**Decision:** MVP MCP (and API mirror for chat clients) exposes **five read-only tools**:

| Tool | Purpose |
|------|---------|
| `search_memory` | Hybrid workspace-filtered search |
| `get_decisions` | Decision lookup on a topic |
| `get_project_context` | Notes + repo docs for a named project |
| `list_workspaces` | Returns workspaces the authenticated user may query (D-016) |
| `get_habilidade` | Fetch one Habilidades skill doc by name (D-043) |

**OUT at MVP:** `write_*`, `promote_*`, `admin_*`, raw file-dump tools. Ingest audit via admin UI/CLI only (D-042). Write tools deferred to P8.

**Rationale:** Core trio from features.md + workspace discovery + Habilidades fetch; same surface for IDE MCP and chat API mirror.

### Auth at client boundary — per-user token at MVP (#21-Q-003, 2026-07-08)

**Decision:** **Per-user API token** at MVP (D-054; mechanism in P2 Q-008). Each client configured with the authenticated user’s token. Server derives **user identity, default persona (D-017), and allowed workspaces (D-016)** from the token — **never trust a client-supplied `user_id`**.

| User | Token maps to | Workspaces (D-016) |
|------|---------------|---------------------|
| Ricardo | `ricardo` / Alba Dev | `ricardo`, `compartilhado`, `casa` |
| Gisele | `gisele` / Alba Texto | `gisele`, `compartilhado`, `casa` |
| Artur (staging only, D-034) | Gisele-equivalent RBAC | `gisele`, `compartilhado`, `casa` — synthetic data only |

Tokens are **revocable per user**. **Post-MVP upgrade path:** OAuth interactive session (same server-side trust model). Persona switching remains post-MVP (D-017).

### Workspace enforcement — server authority (#21-Q-004, 2026-07-08)

**Decision:** **Server-only enforcement** of D-016 on every MCP and API path. Clients never bypass workspace RBAC.

| Rule | Value |
|------|--------|
| Authority | Alba server filters all retrieval by token-derived allowed workspaces |
| Optional `workspace` param | Narrows query **within** allowed set; invalid/overreach → **error** (not silent clamp) |
| Param omitted | Search across **all** workspaces the user may access (merged ranking) |
| Client hints | UX only — `list_workspaces` informs valid values |
| Tests | D-033 isolation tests cover **every MCP tool** + chat API mirror |

### Chat vs IDE — MCP + API mirror (#21-Q-005, 2026-07-08)

**Decision:**

| Surface | Transport | Notes |
|---------|-----------|--------|
| **IDE** (Cursor, Claude Code) | Native **MCP** server | Five read-only tools (#21-Q-002); transport stdio/SSE — P2 |
| **Chat** (ChatGPT, Claude web/app) | **HTTP API mirror** of same tool contract | Per-user token; Custom GPT Actions / Claude connectors |
| **Post-MVP** | Optional native MCP in chat clients where supported | Same server — no second tool surface |

**D-021:** chat threads ephemeral; tools read canon only — no indexing raw threads. One tool schema, two transports.

### Staging vs production client config (#21-Q-006, 2026-07-08)

**Decision:**

| | Staging | Production |
|---|---------|------------|
| **Alba URL** | Separate staging deployment (D-011) | Production deployment |
| **Tokens** | Ricardo staging + **Artur** (Gisele-equivalent RBAC, D-034); synthetic index (D-037) | **Ricardo + Gisele only**; Artur revoked/disabled at go-live |
| **Client paths** | All three (#21-Q-001) — Cursor MCP, Claude Code MCP, chat API mirror — validated before promote | Same client types; prod URL + real user tokens |
| **Gisele in non-prod** | Artur stands in — no Gisele credentials in staging | Gisele real token |

IDE configs point at staging URL during P6–P7 validation; switched to prod at promote.

| ID | Topic | Status |
|----|-------|--------|
| #21-Q-001 | MVP client priority (Cursor vs Claude Code vs ChatGPT/Claude) | **Closed** |
| #21-Q-002 | MVP MCP tool catalog and read-only scope | **Closed** |
| #21-Q-003 | Auth/session at client boundary (per-user identity) | **Closed** |
| #21-Q-004 | Workspace enforcement — server vs client responsibilities | **Closed** |
| #21-Q-005 | ChatGPT/Claude chat as client vs IDE-native MCP | **Closed** |
| #21-Q-006 | Staging (Artur) vs production client configuration | **Closed** |

## Risks / Trade-offs

- [Chat clients lack native MCP] → may need API bridge or connector — define at grilling
- [Workspace leakage] → enforcement must be server-side (D-033); client params are hints only
- [Q-008 overlap] → #21 locks requirements; P2 locks mechanism

## Open Questions

See table above. Grilling starts with **#21-Q-001**.
