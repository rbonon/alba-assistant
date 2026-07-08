# Session handoff — 2026-07-08

> **Start here in a new session.** Run `rbo-catch-up` then read this file + [`STATUS.md`](../../STATUS.md).

---

## Where we are

| Item | State |
|------|--------|
| **Phase** | **P1** — Requirements & spec v1 |
| **P0** | **Complete** — gate #13 closed |
| **P1 grilling** | **#14–#20 closed** (D-015–D-051) |
| **Portal** | Live — https://rbonon.github.io/alba-assistant/ |
| **Board** | GitHub Project **`alba-assistant`** [#5](https://github.com/users/rbonon/projects/5) |
| **Branch** | `main` — no open Change |
| **OpenSpec** | Empty — no active change |
| **ROADMAP** | REST-only (`scripts/refresh-roadmap.sh`) |

---

## What recent sessions accomplished

### P1 grilling closed (#14–#20)

| # | Topic | Decisions |
|---|--------|-----------|
| 14 | Users, workspaces & personas | D-015–D-018 |
| 15 | Canonical sources vs RAG | D-019–D-025 |
| 16 | Privacy, LGPD & sensitive content | D-026–D-030 |
| 17 | MVP scope vs post-MVP | D-031–D-034 |
| 18 | Success metrics per persona | D-035–D-038 |
| 19 | Human memory requirements | D-039–D-045 |
| 20 | Git memory requirements | D-046–D-051 |

**#20 highlights (D-046–D-051):** Explicit per-account repo allowlist (staging subset); `canon` / `canon+code` index profiles; default branch only; Git exclusions extend D-023; HEAD secret scan; amends D-021/D-022 for `ideas/` / `habilidades/` in Git.

**#19 highlights (D-039–D-045):** Human memory = Drive/Docs + Git + optional Obsidian; `Root_*/Alba/` tree; poll + TTL searchability; Habilidades; ingest audit in DB + admin UI; Meet manual placement.

### Earlier (portal + canon sync)

- Closed **#19** — `grill-p1-human-memory-requirements` merged
- Portal: phase-map + progress-report; open/closed cues on issue lines
- Canon sync after #19 — Drive-first MVP

---

## Issue map (current)

### Closed — P1 grilling (#14–#20)

| # | Title |
|---|--------|
| 14–19 | (see above) |
| 20 | [Grill] Git memory requirements |

### Open — P1

| # | Title | Notes |
|---|--------|-------|
| 2 | [Epic] P1 — Requirements & spec v1 | |
| **21** | [Grill] MCP client requirements | **NEXT** |
| 22–25 | Remaining grills | |
| 26–28 | Spec docs | After grills |
| 29 | OpenSpec spec v1 (docs only) | |
| **30** | [Gate] Approve spec v1 | → P2 |

See [`board-hierarchy.md`](./board-hierarchy.md) and [`ROADMAP.md`](../../ROADMAP.md).

---

## Next session — exact steps

1. **`rbo-catch-up`** on `alba-assistant`
2. Read **`STATUS.md`** and this handoff
3. **`rbo-create-change`** on **#21 — [Grill] P1 — MCP client requirements**
4. **`rbo-grilling`** — one question at a time
5. Continue #22–#25, then spec leaves #26–#28
6. Close **#30** only when spec is approved
7. After **#30**: run [`reminder-after-p1-gate.md`](./reminder-after-p1-gate.md)
8. Then **leaf out P2** under epic **#3**

**Do not:** runtime code, skip gates, direct-to-main leaf commits.

---

## Architecture invariants (do not violate)

```text
Obsidian = optional human memory editor · Drive/Docs + Git = human canon · RAG = regenerable index
Workspaces: ricardo, gisele, casa, compartilhado
AI writes → `Root_*/Alba/…` · searchable after TTL · Staging before prod per slice
Never index secrets, .env, node_modules, clinical/sensitive content
No runtime implementation until [Gate] P5
Git: explicit repo allowlist · canon/canon+code profiles · default branch only (D-046–D-050)
```

---

## Doc index for agents

| File | Role |
|------|------|
| [`AGENTS.md`](../../AGENTS.md) | Global + repo rules |
| [`STATUS.md`](../../STATUS.md) | Session compass |
| [`DECISIONS.md`](../../DECISIONS.md) | Append-only decision log |
| [`docs/planning/open-questions.md`](./open-questions.md) | Grilling backlog |

---

**Handoff author:** Cursor session 2026-07-08 (#20 close — Git memory requirements)
