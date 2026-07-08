# Session handoff — 2026-07-08

> **Start here in a new session.** Run `rbo-catch-up` then read this file + [`STATUS.md`](../../STATUS.md).

---

## Where we are

| Item | State |
|------|--------|
| **Phase** | **P1** — Requirements & spec v1 |
| **P0** | **Complete** — gate #13 closed, epic #1 closed |
| **Portal** | Live — https://rbonon.github.io/alba-assistant/ (English, public repo) |
| **Board** | GitHub Project **`alba-assistant`** [#5](https://github.com/users/rbonon/projects/5) |
| **Branch** | `main` — no open Change |
| **OpenSpec** | Empty — no active change |
| **ROADMAP** | Regenerated REST-only (`scripts/gen-docs.py`) |

---

## What this session accomplished

### alba-assistant repo

- **REST-only doc refresh** — `scripts/gen-docs.py`; no GraphQL in refresh paths (`bd81444`)
- **P1 issues #14–#30** on board #5 (Phase=P1, Status=Todo)
- **ROADMAP.md** + **board-hierarchy.md** regenerated

### ai-skills repo (separate — product management suite)

Shipped and pushed to `ai-skills` `main`:

| Skill | Purpose |
|-------|---------|
| **`rbo-product-bootstrap`** | Vision → spec/arch/plan → gates → portal → bootstrap → delivery |
| **`rbo-product-test`** | Integration/E2E — runtime scope, AI-driven, user-approved |
| **`rbo-product-release`** | Go-live checklist + semver/CHANGELOG/GitHub Release — **not** prod promote |

- **Human guide:** `ai-skills/docs/rbo-product-bootstrap-guide.md`
- **Suite guide:** `ai-skills/docs/rbo-product-skills.md`
- Symlinks active via `setup_ai` / `dotfiles_update`

### Process / tooling

- Dotfiles session-playbook WIP discarded (was blocking `git pull --rebase`)
- **`dotfiles_update`** completed; product skills symlinked

### Note — Alba phase map vs product suite

Alba board still uses **P0–P14** (planning P0–P5 + delivery P6+). The new **`rbo-product-*`** suite defines a **richer default phase map** (whole-product arch, bootstrap, test phases, master gate P10). **Realign Alba to that model is future work** — not blocking P1 grilling on current board.

---

## Issue map (current)

### Closed — P0

| # | Title |
|---|--------|
| 1 | [Epic] P0 — Product foundation |
| 7–12 | P0 leaf features |
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
| 22 | [Grill] P1 — Google Calendar scope | |
| 23 | [Grill] P1 — Tasks integration scope | |
| 24 | [Grill] P1 — Google Drive index scope | |
| 25 | [Grill] P1 — Voice interfaces scope | |
| 26 | Write docs/spec/requirements.md | After grills |
| 27 | Write docs/spec/user-stories.md | |
| 28 | Write docs/spec/non-goals.md | |
| 29 | OpenSpec proposal — spec v1 (documentation only) | `rbo-create-change` |
| **30** | [Gate] P1 — Approve spec v1 | Human gate → P2 |

See [`board-hierarchy.md`](./board-hierarchy.md) and [`ROADMAP.md`](../../ROADMAP.md).

---

## Next session — exact steps

1. **`rbo-catch-up`** on `alba-assistant`
2. Read **`STATUS.md`** and this handoff
3. **`rbo-create-change`** on **#14 — [Grill] P1 — Users, workspaces & personas**
4. **`rbo-grilling`** — Q-001 (one question, wait for answer):

   > MVP primary user — Ricardo only for production go-live, or Ricardo + Gisele from day one?
   >
   > **Recommended:** Ricardo only (`ricardo` + `compartilhado` read paths).

5. Record answer in issue #14 comment + `DECISIONS.md` + `open-questions.md`
6. Continue #15–#25 one at a time
7. Spec leaves #26–#28 via `rbo-create-change` each
8. #29 — OpenSpec spec-only change
9. Close **#30 — [Gate] P1 — Approve spec v1** only when spec is approved

**Do not:** runtime code, skip gates, direct-to-main leaf commits.

**Communication:** one question at a time; always `#N — Title`.

---

## Key commits on main (recent)

| Commit | Summary |
|--------|---------|
| `bd81444` | REST-only doc refresh (`gen-docs.py`) |
| `59498d9` | P1 leaves + session handoff |
| `3a7760a` | Global rules in AGENTS.md |

---

## Architecture invariants (do not violate)

```text
Obsidian = human memory · Git = technical memory · RAG = regenerable index
Workspaces: ricardo, gisele, casa, compartilhado
Vision docs = input only · Canon = spec/arch/plan/decisions after grilling
AI writes → Inbox/AI Drafts only · Staging before prod per slice
Never index secrets, .env, node_modules, clinical/sensitive content
No runtime implementation until [Gate] P5 (Alba board; P10 in rbo-product-* suite)
```

---

## Doc index for agents

| File | Role |
|------|------|
| [`AGENTS.md`](../../AGENTS.md) | Global + repo rules |
| [`STATUS.md`](../../STATUS.md) | Session compass |
| [`DECISIONS.md`](../../DECISIONS.md) | Append-only decision log |
| [`docs/planning/workflow.md`](./workflow.md) | Model A + lifecycle |
| [`docs/planning/phases.md`](./phases.md) | P0–P14 map (Alba board) |
| [`docs/planning/open-questions.md`](./open-questions.md) | Grilling backlog |
| [`docs/vision/alba-context-assistant-handoff.md`](../vision/alba-context-assistant-handoff.md) | Vision input (PT) |

**External (ai-skills):** `docs/rbo-product-skills.md`, `docs/rbo-product-bootstrap-guide.md`

---

## Session closed

**Handoff author:** Cursor session 2026-07-08  
**User:** closing session; docs persisted for next start.
