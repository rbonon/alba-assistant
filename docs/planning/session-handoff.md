# Session handoff — 2026-07-08

> **Start here in a new session.** Run `rbo-catch-up` then read this file + [`STATUS.md`](../../STATUS.md).

---

## Where we are

| Item | State |
|------|--------|
| **Phase** | **P1** — Requirements & spec v1 |
| **P0** | **Complete** — gate #13 closed |
| **P1 grilling** | **#14–#19 closed** (D-015–D-045) |
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

**#19 highlights (D-039–D-045):** Human memory = Drive/Docs + Git + optional Obsidian; `Root_*/Alba/` tree; poll + TTL searchability; Habilidades; ingest audit in DB + admin UI; Meet manual placement. Amends D-002, D-006, D-019.

### This session (2026-07-08, portal + canon sync)

- Closed **#19** — `grill-p1-human-memory-requirements` merged (`f294cdc`)
- Portal: generated **phase-map** + **progress-report** from live issues; open/closed cues on issue lines
- Canon sync: `features.md`, `phases.md`, `product-vision.md`, `index.html` — Drive-first MVP (D-039–D-045); `features.html` now generated from `features.md`
- Confirmed: **P2 leaves** created after **[Gate] P1** (#30); **`rbo-product-bootstrap` Step 1** (inventory only) runs per [`reminder-after-p1-gate.md`](./reminder-after-p1-gate.md)

### Platform & agent onboarding (earlier)

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

### Closed — P1 grilling (#14–#19)

| # | Title |
|---|--------|
| 14 | [Grill] Users, workspaces & personas |
| 15 | [Grill] Canonical sources vs RAG boundaries |
| 16 | [Grill] Privacy, LGPD & sensitive content |
| 17 | [Grill] MVP scope vs post-MVP |
| 18 | [Grill] Success metrics per persona |
| 19 | [Grill] Human memory requirements (was Obsidian requirements) |

### Open — P1

| # | Title | Notes |
|---|--------|-------|
| 2 | [Epic] P1 — Requirements & spec v1 | |
| **20** | [Grill] Git memory requirements | **NEXT** |
| 21–25 | Remaining grills | |
| 26–28 | Spec docs | After grills |
| 29 | OpenSpec spec v1 (docs only) | |
| **30** | [Gate] Approve spec v1 | → P2 |

See [`board-hierarchy.md`](./board-hierarchy.md) and [`ROADMAP.md`](../../ROADMAP.md).

---

## Next session — exact steps

1. **`rbo-catch-up`** on `alba-assistant`
2. Read **`STATUS.md`** and this handoff
3. **`rbo-create-change`** on **#20 — [Grill] P1 — Git memory requirements**
4. **`rbo-grilling`** — one question at a time
5. Continue #21–#25, then spec leaves #26–#28
6. Close **#30** only when spec is approved
7. After **#30**: run [`reminder-after-p1-gate.md`](./reminder-after-p1-gate.md) (`rbo-product-bootstrap` Step 1 — inventory only)
8. Then **leaf out P2** (propose leaves → OK → create issues) under epic **#3**

**Do not:** runtime code, skip gates, direct-to-main leaf commits.

---

## Key commits on main (recent)

| Commit | Summary |
|--------|---------|
| `6ffa75e` | Canon sync after #19 — features, phases, product-vision, portal home |
| `769953c` | Portal — status marks right column, icon-only |
| `af49518` | Portal — phase map + progress issue cues |
| `f294cdc` | merge #19 — human memory requirements (D-039–D-045) |

---

## Architecture invariants (do not violate)

```text
Obsidian = optional human memory editor · Drive/Docs + Git = human canon · RAG = regenerable index
Workspaces: ricardo, gisele, casa, compartilhado
Vision docs = input only · Canon = spec/arch/plan/decisions after grilling
AI writes → `Root_*/Alba/…` · searchable after TTL · Staging before prod per slice
Never index secrets, .env, node_modules, clinical/sensitive content
No runtime implementation until [Gate] P5
```

---

## Doc index for agents

| File | Role |
|------|------|
| [`AGENTS.md`](../../AGENTS.md) | Global + repo rules — **mandates reading this handoff at session start** |
| [`CLAUDE.md`](../../CLAUDE.md) | Claude context — same session-start rule |
| [`STATUS.md`](../../STATUS.md) | Session compass |
| [`DECISIONS.md`](../../DECISIONS.md) | Append-only decision log |
| [`docs/planning/features.md`](./features.md) | MVP scope + success metrics |
| [`docs/planning/open-questions.md`](./open-questions.md) | Grilling backlog |
| [`docs/planning/decisions.md`](./decisions.md) | Planning mirror of decisions |

---

**Handoff author:** Cursor session 2026-07-08 (#19 close + portal/canon sync)
