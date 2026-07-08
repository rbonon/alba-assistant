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

## Issue hierarchy

| Level | GitHub | OpenSpec? | Code? |
|-------|--------|-----------|-------|
| Phase | **Phase** field (`P0`…`P14`) | No | No |
| Epic | Issue `[Epic] Pn — …` | No | No |
| Feature / task | Child issue or linked issue | Leaf only | P6+ |
| Gate | `[Gate] Pn — …` | No | No |

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
