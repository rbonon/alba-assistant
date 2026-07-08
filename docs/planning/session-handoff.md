# Session handoff — 2026-07-07

> **Start here in a new session.** Run `rbo-catch-up` then read this file + [`STATUS.md`](../../STATUS.md).

---

## Where we are

| Item | State |
|------|--------|
| **Phase** | **P1** — Requirements & spec v1 (started) |
| **P0** | **Complete** — gate #13 closed, epic #1 closed |
| **Portal** | Live — https://rbonon.github.io/alba-assistant/ (English, public repo) |
| **Board** | GitHub Project **`alba-assistant`** [#5](https://github.com/users/rbonon/projects/5) |
| **Branch** | `main` — no open Change |
| **OpenSpec** | Empty — no active change |

---

## What this session accomplished

### Product foundation (P0)

- English GitHub Pages portal under `docs/` (mirrors fortegb/platform pattern)
- Planning canon: `docs/planning/*`, vision handoff in `docs/vision/`
- GitHub Project board created with **Phase** field (P0–P14)
- Epics P0–P5 shell issues (#1–#6)
- P0 leaf issues #7–#12 delivered and retro-closed (Model A exception — work landed on `main` before strict branch rule)
- Repo made **public** for Pages
- Refresh scripts: `scripts/refresh-roadmap.sh`, `scripts/refresh-board-hierarchy.sh` (+ REST fallback when GraphQL rate-limited)

### Process decisions locked

- **Model A:** every **leaf** issue → `rbo-create-change` → `feat/<name>` → OpenSpec → `rbo-close-change` with `Closes #N`. Epics and gates excluded.
- **Phase gates:** P0→P5 planning, then P6+ implementation only after `[Gate] P5`
- **Grilling:** one question at a time (`rbo-grilling`); Q-001 is first
- **Global behavioural rules** persisted in root `AGENTS.md` (also in Cursor User Rules)
- **Planned Alba GitHub org** for `alba-assistant`, `alba-docs` (Q-012 — timing TBD)

### P1 breakdown (this session end)

17 leaf issues created under epic **#2** — issues **#14–#30** (see table below).

---

## Issue map (as of session end)

### Closed — P0

| # | Title |
|---|--------|
| 1 | [Epic] P0 — Product foundation |
| 7–12 | P0 leaf features (portal, handoff, canon, agent docs, DECISIONS, scripts) |
| 13 | [Gate] P0 — Product foundation complete |

### Open — P1 epic

| # | Title |
|---|--------|
| 2 | [Epic] P1 — Requirements & spec v1 |

### Open — P1 leaves (do in order)

| # | Title | Notes |
|---|--------|-------|
| **14** | [Grill] P1 — Users, workspaces & personas | **START HERE** — Q-001 |
| 15 | [Grill] P1 — Canonical sources vs RAG boundaries | |
| 16 | [Grill] P1 — Privacy, LGPD & sensitive content | |
| 17 | [Grill] P1 — MVP scope vs post-MVP | |
| 18 | [Grill] P1 — Success metrics per persona | |
| 19 | [Grill] P1 — Obsidian requirements | |
| 20 | [Grill] P1 — Git memory requirements | |
| 21 | [Grill] P1 — MCP client requirements | |
| 22 | [Grill] P1 — Google Calendar scope | Q-009 |
| 23 | [Grill] P1 — Tasks integration scope | Q-010 |
| 24 | [Grill] P1 — Google Drive index scope | |
| 25 | [Grill] P1 — Voice interfaces scope | Q-011 |
| 26 | Write docs/spec/requirements.md | After grills |
| 27 | Write docs/spec/user-stories.md | |
| 28 | Write docs/spec/non-goals.md | |
| 29 | OpenSpec proposal — spec v1 (documentation only) | `rbo-create-change` |
| **30** | [Gate] P1 — Approve spec v1 | Human gate → P2 |

### Open — future epics (shells only)

#3 P2 Architecture · #4 P3 Environments · #5 P4 Operations · #6 P5 Roadmap

---

## Next session — exact steps

1. **`rbo-catch-up`** on `alba-assistant`
2. Read **`STATUS.md`** and this handoff
3. **`rbo-create-change`** on issue **#14** (Grill — users/workspaces/personas)
4. Run **`rbo-grilling`** — first question:

   > **Q-001:** MVP primary user — Ricardo only for production go-live, or Ricardo + Gisele from day one?
   >
   > **Recommended:** Ricardo only (`ricardo` + `compartilhado` read paths). Gisele spec'd in P1, production in P9.

5. Record answer in issue #14 comment + `DECISIONS.md` + `open-questions.md`
6. Continue grilling issues #15–#25 one at a time (or batch only if user asks)
7. Spec write issues #26–#28 via `rbo-create-change` each
8. Issue #29 — OpenSpec spec-only change
9. Close **#30** only when Ricardo approves spec v1

**Do not:** write runtime code, skip gates, commit leaf work directly to `main`.

---

## Key commits on main (P0)

| Commit | Summary |
|--------|---------|
| `066a5d9` | P0 bootstrap — portal, planning canon, board script |
| `40453b0` | Pages live (public repo) |
| `7468516` | Model A workflow |
| `f9d1d7d` | Refresh scripts REST fallback |
| `3a7760a` | Global rules in AGENTS.md |

---

## Architecture invariants (do not violate)

```text
Obsidian = human memory · Git = technical memory · RAG = regenerable index
Workspaces: ricardo, gisele, casa, compartilhado
AI writes → Inbox/AI Drafts only · Staging before prod per slice
Never index secrets, .env, node_modules, clinical/sensitive content
No runtime implementation until [Gate] P5
```

---

## Known gaps / housekeeping

| Gap | Action |
|-----|--------|
| P1 issues #14–#30 may not be on Project board yet | When GraphQL resets: add to board #5, set Phase=P1, Status=Todo; or re-run board field script |
| `ROADMAP.md` / `board-hierarchy.md` | Run `./scripts/refresh-board-hierarchy.sh` after board sync |
| Spec files empty | Expected — P1 deliverables #26–28 |
| Alba org | Q-012 open — migrate `alba-assistant` + `alba-docs` when ready |

---

## Doc index for agents

| File | Role |
|------|------|
| [`AGENTS.md`](../../AGENTS.md) | Global rules + repo rules |
| [`STATUS.md`](../../STATUS.md) | Session compass (update each session) |
| [`DECISIONS.md`](../../DECISIONS.md) | Append-only decision log |
| [`docs/planning/workflow.md`](./workflow.md) | Model A + lifecycle |
| [`docs/planning/phases.md`](./phases.md) | P0–P14 map |
| [`docs/planning/open-questions.md`](./open-questions.md) | Grilling backlog |
| [`docs/vision/alba-context-assistant-handoff.md`](../vision/alba-context-assistant-handoff.md) | Vision input (PT) — not final spec |

---

## Session closed

**Handoff author:** Cursor session 2026-07-07  
**User approval:** P0 gate closed; P1 leaves created; Model A confirmed.
