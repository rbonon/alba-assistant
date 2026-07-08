# Planning — Alba Context Assistant

> Design canon and sequencing. **Phase P1 in progress** — requirements & spec v1.

---

## Start here

| Step | Action | Doc |
|------|--------|-----|
| 1 | `rbo-catch-up` + read **session handoff** | [`session-handoff.md`](./session-handoff.md) |
| 2 | Read **STATUS.md** | [`../../STATUS.md`](../../STATUS.md) |
| 3 | Read vision handoff (input, not spec) | [`../vision/alba-context-assistant-handoff.md`](../vision/alba-context-assistant-handoff.md) |
| 4 | Board **`alba-assistant`** #5 | [GitHub Project](https://github.com/users/rbonon/projects/5) |
| 5 | **`rbo-create-change`** on **#14 — [Grill] P1 — Users, workspaces & personas** → Q-001 | [`open-questions.md`](./open-questions.md) |

**Grilling:** use **`rbo-grilling`** — one question at a time. Resolved items move to [`decisions.md`](./decisions.md) and root [`DECISIONS.md`](../../DECISIONS.md).

---

## Index

| Document | Content |
|----------|---------|
| [session-handoff.md](./session-handoff.md) | **New session start** — full context handoff |
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
- Product suite (ai-skills): **`rbo-product-bootstrap`**, **`rbo-product-test`**, **`rbo-product-release`** — see `ai-skills/docs/rbo-product-skills.md`
