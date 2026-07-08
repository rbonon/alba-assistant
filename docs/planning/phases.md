# Phases & epics

> High-level sequencing. Each epic = GitHub issue `[Epic] Pn — …` on the board (Phase field = `Pn`).

## Planning phases (no application code)

| Phase | Epic | Gate |
|-------|------|------|
| **P0** | Product foundation | `[Gate] P0` — portal, board, vision docs |
| **P1** | Requirements & spec v1 | `[Gate] P1` — approve spec |
| **P2** | Architecture v1 | `[Gate] P2` — tech stack, system, integrations |
| **P3** | Environments & deployment | `[Gate] P3` — staging/prod matrix |
| **P4** | Operations & go-live | `[Gate] P4` — bootstrap, data feeding, checklists |
| **P5** | Product roadmap | `[Gate] P5` — MVP + P6+ issue tree |

## Delivery phases (OpenSpec + rbo-create-change)

| Phase | Epic | Capability |
|-------|------|------------|
| **P6** | MVP read-only memory | Index Obsidian + Git, hybrid search, staging |
| **P7** | MVP API + MCP + prod v0 | HTTP + MCP, production go-live |
| **P8** | Controlled writes | Drafts to Obsidian inbox |
| **P9** | Gisele workspace | Multi-user production |
| **P10** | Google Calendar | Read-only meeting context |
| **P11** | Tasks integration | TBD provider |
| **P12** | Google Drive | Metadata/content index |
| **P13** | Android voice capture | Speech → API → draft |
| **P14** | Alexa / voice assistant | Short commands |

## P0 sub-tasks (current)

1. [ ] Bootstrap GitHub Pages portal (English)
2. [ ] Normalize vision handoff → `docs/vision/`
3. [ ] Seed planning canon
4. [ ] Populate AGENTS.md, CLAUDE.md, DECISIONS.md
5. [ ] Create GitHub Project + Phase field
6. [ ] Create epic shells P1–P5
7. [ ] `[Gate] P0` — human approval

## Dependency spine

```text
P0 → P1 (grill + spec) → P2 (grill + arch) → P3 (env) → P4 (ops) → P5 (roadmap)
  → P6… (implementation via OpenSpec, staging → prod each slice)
```
