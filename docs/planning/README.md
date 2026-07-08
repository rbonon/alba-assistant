# Planning — Alba Context Assistant

> Design canon and sequencing. **Phase P0 in progress** — foundation, board, and portal.

---

## Start here

| Step | Action | Doc |
|------|--------|-----|
| 1 | `rbo-catch-up` + read **STATUS.md** | [`../../STATUS.md`](../../STATUS.md) |
| 2 | Read vision handoff (input, not spec) | [`../vision/alba-context-assistant-handoff.md`](../vision/alba-context-assistant-handoff.md) |
| 3 | GitHub Project board | Board title **`alba-assistant`** |
| 4 | Next: close **P0 gate**, then **P1 grilling** | [`open-questions.md`](./open-questions.md) |

**Grilling:** use **`rbo-grilling`** — one question at a time. Resolved items move to [`decisions.md`](./decisions.md) and root [`DECISIONS.md`](../../DECISIONS.md).

---

## Index

| Document | Content |
|----------|---------|
| [product-vision.md](./product-vision.md) | English vision summary |
| [features.md](./features.md) | Feature set — MVP vs later |
| [modules.md](./modules.md) | Tools & integrations map |
| [phases.md](./phases.md) | P0–P14 epics and gates |
| [architecture.md](./architecture.md) | Architecture summary (P2 gate) |
| [open-questions.md](./open-questions.md) | Grilling backlog |
| [decisions.md](./decisions.md) | Human-readable decisions |
| [workflow.md](./workflow.md) | Board, OpenSpec, Pages, skills |
| [board-hierarchy.md](./board-hierarchy.md) | **Generated** — epic/issue tree |

## Portal (GitHub Pages)

| Page | URL path |
|------|----------|
| Home | `/docs/index.html` |
| Progress — issues | `/docs/planning/progress-report.html` |
| Progress — phases | `/docs/planning/phase-map.html` |
| Features | `/docs/planning/features.html` |
| Architecture | `/docs/planning/architecture-overview.html` |

Published at: **https://rbonon.github.io/alba-assistant/** (after Pages enable + push)

---

## Rules

- **Board** = execution · **`docs/planning/`** = thinking · **OpenSpec** = 1:1 implementable leaf issues (from P6+)
- **`ROADMAP.md`** = generated from board; never hand-edit
- **`STATUS.md`** = session compass — update when focus changes
- Lifecycle skills: **`rbo-create-issue`** → **`rbo-create-change`** → **`rbo-close-change`**
