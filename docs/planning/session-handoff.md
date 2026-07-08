# Session handoff — 2026-07-08

> **Start here in a new session.** Run `rbo-catch-up` then read this file + [`STATUS.md`](../../STATUS.md).
>
> **Repo convention:** this file is the canonical session handoff (not `/tmp`).

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
| **OpenSpec** | No active change; main specs: `git-memory-requirements`, `mcp-client-requirements` |
| **ROADMAP** | REST-only (`scripts/refresh-roadmap.sh`) |

---

## What this session accomplished

Closed **#20 Git memory** (D-046–D-051) and **#21 MCP client** (D-052–D-057). Portal synced after each close. No runtime code.

| # | Topic | Highlights |
|---|--------|------------|
| 20 | Git memory | Explicit allowlist; `canon`/`canon+code` profiles; default branch only; exclusions + HEAD secret scan; amend D-021/D-022 |
| 21 | MCP client | All clients at go-live (validate Cursor → Claude Code → chat); 5 read-only tools; per-user token; server workspace enforcement; IDE MCP + chat API mirror; staging Artur / prod Ricardo+Gisele |

Prior grilling #14–#19: D-015–D-045 (see `DECISIONS.md`).

---

## Artifacts

| Item | Reference |
|------|-----------|
| Latest `main` | `0b7d55c` — portal sync after #21 |
| Merge #21 | `c33621f` — `Closes #21` |
| Archive #20 | `openspec/changes/archive/2026-07-08-grill-p1-git-memory-requirements/` |
| Archive #21 | `openspec/changes/archive/2026-07-08-grill-p1-mcp-client-requirements/` |
| Next issue | [#22 — Google Calendar scope](https://github.com/rbonon/alba-assistant/issues/22) |

---

## Control doc paths

| Role | Path |
|------|------|
| Decisions (canonical) | [`DECISIONS.md`](../../DECISIONS.md) · mirror [`decisions.md`](./decisions.md) |
| Session compass | [`STATUS.md`](../../STATUS.md) |
| Planning | [`docs/planning/`](./) |
| Agent context | [`AGENTS.md`](../../AGENTS.md), [`CLAUDE.md`](../../CLAUDE.md) |
| Portal home (hand-edit) | [`docs/index.html`](../index.html) |

---

## Issue map (open P1)

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

**On close-out:** `./scripts/refresh-roadmap.sh` + update `docs/index.html` + `docs/assets/build-info.json` — commit push.

**Do not:** runtime code, skip gates, direct-to-main leaf commits, hand-edit `ROADMAP.md`.

---

## Architecture invariants (do not violate)

```text
Obsidian = optional human memory editor · Drive/Docs + Git = human canon · RAG = regenerable index
Workspaces: ricardo, gisele, casa, compartilhado
Git: explicit repo allowlist · canon/canon+code · default branch only (D-046–D-051)
MCP: five read-only tools · per-user token · server enforces D-016 (D-052–D-057)
IDE = native MCP · Chat = HTTP API mirror · Staging Artur / prod Ricardo+Gisele
No runtime implementation until [Gate] P5
```

---

## Suggested skills

`rbo-catch-up` · `rbo-create-change` · `rbo-grilling` · `rbo-close-change`

---

**Handoff author:** Cursor session 2026-07-08 (#20–#21 close + portal sync)
