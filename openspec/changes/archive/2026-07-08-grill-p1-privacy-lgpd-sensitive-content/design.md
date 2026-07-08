## Context

- **D-016:** workspace read isolation — Ricardo ↔ Gisele private workspaces never cross-read
- **D-019 / D-023:** Meet transcriptions **not indexed at MVP**; clinical on never-index until #16
- Gisele use case: Meet transcriptions + session notes → insights, Virtuologia pattern analysis
- Brazil LGPD applies to personal and sensitive health-related data

## Goals / Non-Goals

**Goals:**

- Decide clinical content in Alba vs separate stack
- If in Alba: define gated phase, controls (encryption, audit, consent)
- Lock Gisele workspace privacy for production spec
- LGPD principles for spec writers

**Non-Goals:**

- Legal review (recommend professional review before clinical go-live)
- Technical implementation (P2/P6+)
- Encryption vendor selection

## Decisions

| Topic | Approach |
|-------|----------|
| Interview | `rbo-grilling` — one question at a time |
| Baseline | D-023 never-index clinical until this grill approves exception |

## Open Questions

| ID | Question | Status |
|----|----------|--------|
| #16-Q-001 | Patient Meet transcriptions — ever in Alba? If yes, when and how isolated? | **Open — start here** |
