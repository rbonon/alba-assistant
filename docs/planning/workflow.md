# Workflow — Board, OpenSpec, GitHub Pages

## Three layers

```text
docs/planning/     →  why, scope, questions, decisions
GitHub board       →  epics + issues (execution)
STATUS.md          →  session compass
ROADMAP.md         →  generated board mirror
OpenSpec           →  spec + tasks per implementable leaf (P6+)
Portal (Pages)     →  human-readable progress + architecture views
```

## Lifecycle skills

```text
rbo-create-issue        →  roadmap entry on board
rbo-create-change       →  branch + explore + propose (approval gate)
openspec-apply-change   →  implement tasks on branch
rbo-close-change        →  archive → merge → push → Closes #N → refresh ROADMAP
rbo-grilling            →  one question at a time before spec/arch decisions
```

## Issue hierarchy & change linkage (Model A)

| Level | GitHub | Branch | OpenSpec change | Closes on merge |
|-------|--------|--------|-----------------|-----------------|
| Phase | **Phase** field | No | No | No |
| Epic | `[Epic] Pn — …` | No | No | No — closes when children Done |
| **Leaf** (Feature / Chore) | Implementable issue | **`feat/<change-name>`** | Yes (propose at minimum) | **`Closes #N`** |
| Gate | `[Gate] Pn — …` | No | No | Human closes after approval |

### Rules

1. **Every leaf issue** → `rbo-create-change` → branch → propose → (apply) → `rbo-close-change` → `Closes #N`.
2. **Epics and gates** never get a branch or OpenSpec change.
3. **Planning docs (P0–P5):** leaf issues still get a branch + change; OpenSpec can be **lightweight** (proposal + tasks only) until P6 code work.
4. **No direct commits to `main`** for leaf deliverables after P0 retro-close.
5. P0 leaf issues #7–#12 were retro-closed against commits already on `main` (one-time exception).

### Lifecycle

```text
rbo-create-issue (leaf)
  → rbo-create-change (branch feat/<name>, In Progress, propose)
  → [approval gate]
  → openspec-apply-change (if implementation)
  → human validation
  → rbo-close-change (archive → merge → push Closes #N → board Done → refresh ROADMAP)
```

Until **Alba org** exists: use `[Epic]` title prefix on personal repo. After org migration: native Epic issue type + sub-issues (like fortegb/platform).

## Refresh scripts

| Script | Output |
|--------|--------|
| `scripts/refresh-roadmap.sh` | `ROADMAP.md` |
| `scripts/refresh-board-hierarchy.sh` | `docs/planning/board-hierarchy.md` |

Run after issue create/close or board status change. Update `docs/assets/build-info.json` date on portal-facing commits.

## Gates

No OpenSpec implementation until **`[Gate] P5`** is closed. Each planning phase (P1–P4) ends with explicit human approval.

## GitHub Pages

- Source: `/docs` on `main`
- URL: https://rbonon.github.io/alba-assistant/
- Language: **English** portal; vision handoff may stay Portuguese
