# Session handoff — 2026-07-08

> **Start here in a new session.** Run `rbo-catch-up` then read this file + [`STATUS.md`](../../STATUS.md).

---

## Where we are

| Item | State |
|------|--------|
| **Phase** | **P1** — Requirements & spec v1 |
| **P0** | **Complete** — gate #13 closed |
| **P1 grilling** | **#14–#18 closed** (D-015–D-038) |
| **Portal** | Live — https://rbonon.github.io/alba-assistant/ |
| **Board** | GitHub Project **`alba-assistant`** [#5](https://github.com/users/rbonon/projects/5) |
| **Branch** | `main` — no open Change |
| **OpenSpec** | Empty — no active change |
| **ROADMAP** | REST-only (`scripts/refresh-roadmap.sh`) |

---

## What recent sessions accomplished

### P1 grilling closed (#14–#18)

| # | Topic | Decisions |
|---|--------|-----------|
| 14 | Users, workspaces & personas | D-015–D-018 |
| 15 | Canonical sources vs RAG | D-019–D-025 |
| 16 | Privacy, LGPD & sensitive content | D-026–D-030 |
| 17 | MVP scope vs post-MVP | D-031–D-034 |
| 18 | Success metrics per persona | D-035–D-038 |

**#18 highlights (D-035–D-038):** MVP metrics = core + Ricardo + Gisele non-clinical + Casa search; staging fixture gate (top-3, 100%); synthetic AI/app-generated corpus; prod manual smoke. Calendar/Tasks/clinical/voice metrics **deferred**.

### Platform

- REST-only doc refresh (`scripts/gen-docs.py`)
- Portal pages synced with canon (`features.md`, phase map, progress)

---

## Issue map (current)

### Closed — P0

| # | Title |
|---|--------|
| 1 | [Epic] P0 — Product foundation |
| 7–12 | P0 leaf features |
| 13 | [Gate] P0 — Product foundation complete |

### Closed — P1 grilling (#14–#18)

| # | Title |
|---|--------|
| 14 | [Grill] Users, workspaces & personas |
| 15 | [Grill] Canonical sources vs RAG boundaries |
| 16 | [Grill] Privacy, LGPD & sensitive content |
| 17 | [Grill] MVP scope vs post-MVP |
| 18 | [Grill] Success metrics per persona |

### Open — P1

| # | Title | Notes |
|---|--------|-------|
| 2 | [Epic] P1 — Requirements & spec v1 | |
| **19** | [Grill] Obsidian requirements | **NEXT** |
| 20–25 | Remaining grills | |
| 26–28 | Spec docs | After grills |
| 29 | OpenSpec spec v1 (docs only) | |
| **30** | [Gate] Approve spec v1 | → P2 |

See [`board-hierarchy.md`](./board-hierarchy.md) and [`ROADMAP.md`](../../ROADMAP.md).

---

## Next session — exact steps

1. **`rbo-catch-up`** on `alba-assistant`
2. Read **`STATUS.md`** and this handoff
3. **`rbo-create-change`** on **#19 — [Grill] P1 — Obsidian requirements**
4. **`rbo-grilling`** — one question at a time
5. Continue #20–#25, then spec leaves #26–#28
6. Close **#30** only when spec is approved

**Do not:** runtime code, skip gates, direct-to-main leaf commits.

---

## Key commits on main (recent)

| Commit | Summary |
|--------|---------|
| `7e0882f` | ROADMAP refresh after #18 |
| `feede3e` | merge #18 — success metrics (D-035–D-038) |
| `17bd5c2` | merge #17 — MVP scope (D-031–D-034) |

---

## Architecture invariants (do not violate)

```text
Obsidian = human memory · Git = technical memory · RAG = regenerable index
Workspaces: ricardo, gisele, casa, compartilhado
Vision docs = input only · Canon = spec/arch/plan/decisions after grilling
AI writes → Inbox/AI Drafts only · Staging before prod per slice
Never index secrets, .env, node_modules, clinical/sensitive content
No runtime implementation until [Gate] P5
```

---

## Doc index for agents

| File | Role |
|------|------|
| [`AGENTS.md`](../../AGENTS.md) | Global + repo rules |
| [`STATUS.md`](../../STATUS.md) | Session compass |
| [`DECISIONS.md`](../../DECISIONS.md) | Append-only decision log |
| [`docs/planning/features.md`](./features.md) | MVP scope + success metrics |
| [`docs/planning/open-questions.md`](./open-questions.md) | Grilling backlog |
| [`docs/planning/decisions.md`](./decisions.md) | Planning mirror of decisions |

---

**Handoff author:** Cursor session 2026-07-08 (post #18 close)
