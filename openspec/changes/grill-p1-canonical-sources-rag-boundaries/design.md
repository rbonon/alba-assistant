## Context

- **D-002–D-004** already assert: Obsidian = human memory, Git = technical memory, RAG = regenerable index.
- Issue **#15** grills the **operational detail**: MVP indexing scope, Calendar/Tasks/Drive boundaries, rebuild rules, what must never be indexed.
- Builds on **D-015–D-018** (multi-user, workspace filters apply to indexed content).

## Goals / Non-Goals

**Goals:**

- Lock source-of-truth matrix for P1 spec
- Define MVP vs post-MVP indexed sources
- State RAG rebuild/regeneration expectations
- Clarify Calendar/Tasks/Drive vs Obsidian context split

**Non-Goals:**

- Vault topology on disk (global Q-002, P2)
- Vector DB / embedding choices (P2)
- Ingestion implementation (P6+)

## Decisions

| Topic | Approach |
|-------|----------|
| Interview | `rbo-grilling` — one question at a time |
| Storage | `DECISIONS.md` + issue **#15** + `open-questions.md` |
| Baseline | Treat D-002–D-004 as starting points, not skip grilling |

## Risks / Trade-offs

| Risk | Mitigation |
|------|------------|
| Indexing Calendar/Tasks duplicates systems of record | Default: context in Obsidian only; integrations read-only later |
| Indexing secrets or build artifacts | Explicit never-index list in this grill |
| RAG treated as writable store | Reaffirm rebuild-only; AI writes go to Obsidian inbox only (D-006) |

## Open Questions

| ID | Question | Status |
|----|----------|--------|
| #15-Q-001 | MVP indexed canonical sources — Obsidian + Git only, or include more at launch? | **Open — start here** |
