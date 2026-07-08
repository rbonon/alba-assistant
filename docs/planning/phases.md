# Phases & epics

> High-level sequencing. Each epic = GitHub issue `[Epic] Pn — …` on the board (Phase field = `Pn`).

## Planning phases (no application code)

| Phase | Epic | Gate | Status |
|-------|------|------|--------|
| **P0** | Product foundation | `[Gate] P0` #13 | ✅ Done |
| **P1** | Requirements & spec v1 | `[Gate] P1` #30 | **In progress** |
| **P2** | Architecture v1 | `[Gate] P2` | Todo |
| **P3** | Environments & deployment | `[Gate] P3` | Todo |
| **P4** | Operations & go-live | `[Gate] P4` | Todo |
| **P5** | Product roadmap | `[Gate] P5` | Todo |

## Delivery phases (OpenSpec + rbo-create-change)

| Phase | Epic | Capability |
|-------|------|------------|
| **P6** | MVP read-only memory | Index Obsidian + Git, hybrid search, staging |
| **P7** | MVP API + MCP + prod v0 | HTTP + MCP, production go-live |
| **P8** | Controlled writes | Drafts to Obsidian inbox |
| **P9** | Gisele clinical slice | Meet transcripts, Patient-00N, Virtuologia (post-MVP gated, D-026–D-030) |
| **P10** | Google Calendar | Read-only meeting context |
| **P11** | Tasks integration | TBD provider |
| **P12** | Google Drive | Metadata/content index |
| **P13** | Android voice capture | Speech → API → draft |
| **P14** | Alexa / voice assistant | Short commands |

## P0 — complete ✅

- [x] Bootstrap GitHub Pages portal (English) — #7
- [x] Normalize vision handoff → `docs/vision/` — #8
- [x] Seed planning canon — #9
- [x] Populate AGENTS.md, CLAUDE.md, DECISIONS.md — #10, #11
- [x] Board + Phase field + refresh scripts — #12
- [x] Epic shells P1–P5 — #2–#6
- [x] `[Gate] P0` — #13 closed 2026-07-07
- [x] Epic P0 — #1 closed

## P1 — leaf issues (#14–#30)

### Grilling (sequential recommended)

| # | Issue |
|---|--------|
| 14 | [Grill] Users, workspaces & personas — **Q-001 start here** |
| 15 | [Grill] Canonical sources vs RAG boundaries |
| 16 | [Grill] Privacy, LGPD & sensitive content |
| 17 | [Grill] MVP scope vs post-MVP |
| 18 | [Grill] Success metrics per persona |
| 19 | [Grill] Obsidian requirements |
| 20 | [Grill] Git memory requirements |
| 21 | [Grill] MCP client requirements |
| 22 | [Grill] Google Calendar scope |
| 23 | [Grill] Tasks integration scope |
| 24 | [Grill] Google Drive index scope |
| 25 | [Grill] Voice interfaces scope |

### Spec deliverables

| # | Issue |
|---|--------|
| 26 | Write docs/spec/requirements.md |
| 27 | Write docs/spec/user-stories.md |
| 28 | Write docs/spec/non-goals.md |
| 29 | OpenSpec proposal — spec v1 (docs only) |
| 30 | **[Gate] P1 — Approve spec v1** |

## Dependency spine

```text
P0 ✅ → P1 (grill + spec) → [Gate P1] → [REALIGN CHECK] → P2 → … → P5 → P6+ implementation
```

### After P1 gate — deferred realignment check

When **#14–#30** are done and **[Gate] P1** (#30) is closed, run the checklist in
[`reminder-after-p1-gate.md`](./reminder-after-p1-gate.md) (`rbo-product-bootstrap`
brownfield inventory only — compare Alba map vs suite template; stop for OK before
any board changes).
