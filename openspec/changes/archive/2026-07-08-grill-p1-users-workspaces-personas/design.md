## Context

- Vision handoff (`docs/vision/alba-context-assistant-handoff.md`) and `docs/planning/product-vision.md` suggest four workspaces and three personas.
- `open-questions.md` lists **Q-001** as the first open item for issue **#14**.
- Model A: this leaf uses branch `feat/grill-p1-users-workspaces-personas` and lightweight OpenSpec (docs-only apply).

## Goals / Non-Goals

**Goals:**

- Resolve Q-001 and tightly related workspace/persona questions via `rbo-grilling` (one question at a time)
- Persist decisions in append-only `DECISIONS.md` and close Q-001 in `open-questions.md`
- Keep vision labeled as input; canon only after user approval

**Non-Goals:**

- Tech stack, auth implementation, or indexing design (P2+)
- Gisele production rollout unless explicitly chosen at Q-001
- Board phase-map realignment (`reminder-after-p1-gate.md` — deferred until **#30**)

## Decisions

| Topic | Approach | Rationale |
|-------|----------|-----------|
| Interview style | `rbo-grilling` — one question, wait for answer | Reduces bewilderment; matches repo rules |
| Decision storage | `DECISIONS.md` + issue **#14** comment + `open-questions.md` status | Traceability for Model A close |
| Suggested default | Ricardo-only MVP (`ricardo` + `compartilhado` read) | Reduces LGPD/privacy scope for first production slice |
| Canon updates | Edit `product-vision.md` / `features.md` only where grilling overrides suggestions | Vision ≠ canon |

## Risks / Trade-offs

| Risk | Mitigation |
|------|------------|
| Ricardo + Gisele day one expands privacy/LGPD scope | Default recommend Ricardo-only; explicit user OK required |
| Vision doc treated as decided | Label changes as post-grill canon; reference decision IDs |
| Scope creep into Q-002+ (vault topology, hosting) | Defer to issues **#15–#25**; stay on users/workspaces/personas |

## Open Questions

| ID | Question | Status |
|----|----------|--------|
| Q-001 | MVP primary user — Ricardo only vs Ricardo + Gisele day one | **Open — start here** |
