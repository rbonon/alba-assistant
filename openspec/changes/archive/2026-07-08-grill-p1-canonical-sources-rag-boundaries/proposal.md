## Why

P1 spec writing needs locked boundaries for **canonical sources** (systems of record) vs the **RAG index** (regenerable derivative). Vision asserts Obsidian + Git + operational systems, but MVP indexing scope and non-negotiable rules need grilling before `docs/spec/requirements.md`.

## What Changes

- Grilling session on issue **#15 — [Grill] P1 — Canonical sources vs RAG boundaries**
- Resolve source-of-truth map: Obsidian, Git, Calendar/Tasks/Drive (MVP vs later), RAG index role
- Record decisions in `DECISIONS.md`, `open-questions.md`, issue **#15** comments
- Update planning canon where grilling overrides vision suggestions

No runtime code. Documentation and decision capture only.

## Capabilities

### New Capabilities

- `canonical-sources-rag`: Source-of-truth matrix, RAG indexing rules, rebuild/regeneration policy, MVP vs post-MVP sources

### Modified Capabilities

- _(none — no main specs exist yet)_

## Impact

- **Docs:** `DECISIONS.md`, `docs/planning/open-questions.md`, `docs/planning/architecture.md` (stub pointers), `features.md`
- **Board:** **#15** → In Progress → Done on close
- **Downstream:** informs **#16** (privacy), **#17** (MVP scope), spec leaves **#26–#28**
