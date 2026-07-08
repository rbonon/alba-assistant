# Decisions — planning mirror

> Human-readable summary. **Append-only canonical log:** [`../../DECISIONS.md`](../../DECISIONS.md)

## Locked (from vision handoff — 2026-07-07)

| ID | Decision |
|----|----------|
| D-001 | Alba is a context assistant, not a document dump |
| D-002 | Obsidian = canonical human memory |
| D-003 | Git = canonical technical/code memory |
| D-004 | RAG = regenerable index, never sole storage |
| D-005 | MCP/API = standard access layer for AI clients |
| D-006 | AI writes start as drafts in `Inbox/AI Drafts` |
| D-007 | Multi-workspace from day one: ricardo, gisele, casa, compartilhado |
| D-008 | Personas: Alba Dev, Alba Texto, Alba Casa |
| D-009 | Clinical/sensitive content out of MVP |
| D-010 | Calendar/Tasks = operational systems; Obsidian holds context only |
| D-011 | Start read-only; staging before production |
| D-012 | GitHub Pages portal in **English** for project docs |
| D-013 | Planned **Alba GitHub org** for alba-assistant, alba-docs, etc. (timing TBD) |
| D-014 | P0 gate closed; P1 leaf issues #14–#30 created; Model A enforced from P1 |
| D-015 | **MVP multi-user from day one** — Ricardo + Gisele at production go-live; user model extensible for more users post-launch (Q-001, #14) |
| D-016 | **MVP workspace read boundaries** — each user: own + `compartilhado` + `casa`; never other’s private workspace (#14 Q-002) |
| D-017 | **MVP persona mapping** — fixed per user (Dev/Texto); `casa`→Alba Casa; persona switching deferred post-MVP (#14 Q-003) |
| D-018 | **Post-launch users** — dedicated workspace + D-016 read rules + assigned persona at onboarding (#14 Q-004) |

## Session (2026-07-08)

- **Q-001 closed (#14):** MVP = Ricardo + Gisele from day one; extensible for more users
- **#14 Q-004 closed:** post-launch user model (D-018)
- **#14 grilling complete** — ready for human validation → `rbo-close-change`

## Session (2026-07-07)

- P0 complete: portal live, board #5, issues #7–#12 retro-closed
- Repo public for GitHub Pages
- Global rules persisted in `AGENTS.md`
- **Next:** issue #14 → Q-002 grilling

- Tech stack details (P2)
- Vault paths on disk (P2/P3)
- Staging vs production hosting (P3)
- MVP workspace read boundaries (#14 Q-002 — closed D-016)
