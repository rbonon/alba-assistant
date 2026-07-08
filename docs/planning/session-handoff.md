# Session handoff — 2026-07-08

> **Start here in a new session.** Run `rbo-catch-up` then read this file + [`STATUS.md`](../../STATUS.md).

---

## Where we are

| Item | State |
|------|--------|
| **Phase** | **P1** — Requirements & spec v1 |
| **P0** | **Complete** — gate #13 closed |
| **P1 grilling** | **#14–#21 closed** (D-015–D-057) |
| **Portal** | Live — https://rbonon.github.io/alba-assistant/ |
| **Board** | GitHub Project **`alba-assistant`** [#5](https://github.com/users/rbonon/projects/5) |
| **Branch** | `main` — no open Change |
| **OpenSpec** | Empty — no active change |
| **ROADMAP** | REST-only (`scripts/refresh-roadmap.sh`) |

---

## What recent sessions accomplished

### P1 grilling closed (#14–#21)

| # | Topic | Decisions |
|---|--------|-----------|
| 14–20 | (see prior handoff) | D-015–D-051 |
| 21 | MCP client requirements | D-052–D-057 |

**#21 highlights (D-052–D-057):** All clients at go-live (Cursor → Claude Code → chat); five read-only MCP tools; per-user token auth; server workspace enforcement; IDE MCP + chat API mirror; staging Artur / prod Ricardo+Gisele.

---

## Issue map (current)

### Open — P1

| # | Title | Notes |
|---|--------|-------|
| 2 | [Epic] P1 — Requirements & spec v1 | |
| **22** | [Grill] Google Calendar scope | **NEXT** |
| 23–25 | Remaining grills | |
| 26–28 | Spec docs | After grills |
| 29 | OpenSpec spec v1 (docs only) | |
| **30** | [Gate] Approve spec v1 | → P2 |

See [`board-hierarchy.md`](./board-hierarchy.md) and [`ROADMAP.md`](../../ROADMAP.md).

---

## Next session — exact steps

1. **`rbo-catch-up`** on `alba-assistant`
2. Read **`STATUS.md`** and this handoff
3. **`rbo-create-change`** on **#22 — [Grill] P1 — Google Calendar scope**
4. **`rbo-grilling`** — one question at a time
5. Continue #23–#25, then spec leaves #26–#28
6. Close **#30** only when spec is approved

**Do not:** runtime code, skip gates, direct-to-main leaf commits.

---

## Architecture invariants (do not violate)

```text
Obsidian = optional human memory editor · Drive/Docs + Git = human canon · RAG = regenerable index
Workspaces: ricardo, gisele, casa, compartilhado
MCP: five read-only tools · per-user token · server enforces D-016 (D-052–D-057)
IDE = native MCP · Chat = HTTP API mirror · Staging Artur / prod Ricardo+Gisele
No runtime implementation until [Gate] P5
```

---

**Handoff author:** Cursor session 2026-07-08 (#21 close — MCP client requirements)
