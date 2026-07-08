# Decisions — planning mirror

> Human-readable summary. **Append-only canonical log:** [`../../DECISIONS.md`](../../DECISIONS.md)

## Locked (from vision handoff — 2026-07-07)

| ID | Decision |
|----|----------|
| D-001 | Alba is a context assistant, not a document dump |
| D-002 | **Human memory** — Google Drive/Docs (workspace roots) + Git; Obsidian optional (#19, amends prior Obsidian-only wording) |
| D-003 | Git = canonical technical/code memory |
| D-004 | RAG = regenerable index, never sole storage |
| D-005 | MCP/API = standard access layer for AI clients |
| D-006 | AI writes to final folders under `Root_*/Alba/`; searchable after TTL — no mandatory inbox promote (#19, amends prior `Inbox/AI Drafts` rule) |
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
| D-019 | **MVP RAG index** — **Drive/Docs + Git** + optional Obsidian; Calendar/Tasks/contacts post-MVP (#19 amends) |
| D-020 | **Ricardo Git indexing** — all three GitHub accounts: `rbonon`, `fortegb`, `akamlibehsafe` (#15 Q-002) |
| D-021 | **AI ideation** — chat ephemeral; final idea `.md` canonical in Obsidian or Git `ideas/` (#20 refines); Git when building (#15 Q-003; **amend at #20**) |
| D-022 | **Idea doc + repo** — idea stays canonical in Obsidian **or** Git `ideas/`; repo holds implementation (#15 Q-004; **amend at #20**) |
| D-023 | **Never-index list** — secrets, build/vendor, clinical until #16, raw chat logs (#15 Q-005) |
| D-024 | **RAG rebuild** — full rebuild from canonical sources on recovery (D-004) (#15 Q-006) |
| D-025 | **Calendar/Tasks model** — personal per user + Casa shared; Obsidian context only; integrate post-MVP (#15 Q-007) |
| D-026 | **Gisele clinical pseudonym** — Patient-00N in RAG; identity in Obsidian; auto-assign on ingest (#16 Q-002) |
| D-027 | **Clinical encryption** — at-rest required (separate key) before clinical slice go-live (#16 Q-003) |
| D-028 | **Clinical slice gates** — post-MVP, gisele-only, no patient consent in Alba, legal review (#16 Q-004) |
| D-029 | **Clinical AI inference** — cloud LLM APIs allowed with Patient-00N text (#16 Q-005) |
| D-030 | **Clinical erasure** — hard delete from Obsidian + clinical RAG (#16 Q-006) |
| D-031 | **MVP scope** — read-only memory + API/MCP IN; integrations/clinical/voice/writes OUT (#17 Q-001) |
| D-032 | **P9 reframe** — Gisele clinical slice (post-MVP); multi-user Gisele at MVP P6–P7 (#17 Q-002) |
| D-033 | **Isolation tests** — automated cross-workspace tests MVP blocker before prod (#17 Q-003) |
| D-034 | **Artur** — real non-prod stand-in for Gisele workspace testing; removed at prod (#17 Q-004) |
| D-035 | **MVP success metrics structure** — core + Ricardo/Gisele non-clinical/Casa; clinical/integrations/voice deferred (#18 Q-001) |
| D-036 | **Search quality bar** — fixture suite, top-3, 100% pass on staging (#18 Q-002) |
| D-037 | **Staging fixture corpus** — synthetic only; AI/app-generated, not hand-maintained (#18 Q-003) |
| D-038 | **Production validation** — manual smoke checklist after promote; no prod fixtures (#18 Q-004) |
| D-039 | **Human memory sources** — Drive/Docs + Git; Obsidian optional per user (#19) |
| D-040 | **MVP Drive indexing** — Google Drive/Docs at MVP (amends D-019) (#19) |
| D-041 | **Drive roots** — `Root_Gisele`, `Root_Ricardo`, `Root_Casa` + `Alba/` namespace; per-user auth (#19 Q-002) |
| D-042 | **Ingest** — poll ~15 min, TTL/subfolder searchable, DB audit + admin UI; no Drive Validar folder (#19 Q-003) |
| D-043 | **Habilidades da Alba** — `…/Alba/Habilidades/`; gdoc + md; skills template (#19 Q-004) |
| D-044 | **Obsidian optional** — Ricardo mirror `Alba/`; no Sync required (#19 Q-005) |
| D-045 | **Meet transcripts** — manual placement in session tree (#19 Q-006) |

## Session (2026-07-08)

- **Q-001 closed (#14):** MVP = Ricardo + Gisele from day one; extensible for more users
- **#15 Q-007 closed:** Calendar/Tasks personal + Casa shared (D-025)
- **#15 grilling complete** — ready for validation → `rbo-close-change`
- **#16 Q-006 closed:** hard delete erasure (D-030)
- **#16 grilling complete** — ready for validation → `rbo-close-change`
- **#17 Q-004 closed:** Artur non-prod stand-in (D-034)
- **#17 closed** on main — D-031–D-034
- **#18 Q-001 closed:** MVP metrics structure locked (D-035); Calendar/Tasks in deferred integrations bucket
- **#18 Q-002 closed:** search fixtures, top-3, 100% pass on staging (D-036)
- **#18 Q-003 closed:** synthetic staging corpus, AI/app-generated (D-037)
- **#18 Q-004 closed:** prod manual smoke checklist (D-038)
- **#18 closed** on main (`feede3e`) — D-035–D-038
- **#19 grilling applied** — D-039–D-045; Drive at MVP; human validation → `rbo-close-change`

## Session (2026-07-07)

- P0 complete: portal live, board #5, issues #7–#12 retro-closed
- Repo public for GitHub Pages
- Global rules persisted in `AGENTS.md`
