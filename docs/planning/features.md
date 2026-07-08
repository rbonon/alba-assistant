# Feature set — Alba Context Assistant

> Business-facing capability map. **MVP boundary locked D-031** (issue #17).

## MVP (P6–P7 go-live) — IN

| Feature | Description | Sources |
|---------|-------------|---------|
| Read-only memory search | Hybrid vector + keyword search, workspace-filtered | **Google Drive/Docs**, Git, optional Obsidian |
| Gisele / Casa memory | Notes, sessions, recipes, Habilidades in `Root_*/Alba/` | Drive (D-039, D-041) |
| Git memory (Ricardo) | Index repos from `rbonon`, `fortegb`, `akamlibehsafe`; `ideas/`, `habilidades/` | Git (D-020) |
| Project context | Retrieve notes + repo docs for a named project | Drive + Git |
| Decision lookup | Find prior decisions on a topic | Drive + Git |
| Standards lookup | Coding/writing standards for Ricardo | Drive + Git agent docs |
| Habilidades da Alba | Skill docs (inputs, steps, deliverables) in `…/Alba/Habilidades/` | Drive gdoc + Git/Obsidian md (D-043) |
| Casa / shared search | Recipes and family notes in `casa` / `compartilhado` searchable | Drive `Root_Casa/Alba/` |
| Multi-user production | Ricardo + Gisele day one; workspace isolation | D-015, D-016 |
| HTTP API | `/memory/search`, health, admin ingest log | Alba API |
| MCP tools | `search_memory`, `get_decisions`, `get_project_context` | MCP server |
| Chat UI | ChatGPT/Claude as client surface (ephemeral threads D-021) | API/MCP |
| Ingest audit | DB log + admin UI/CLI for Ricardo (staging + prod) | D-042 |
| Staging → production | Controlled promotion from staging | All MVP components |
| Workspace isolation tests | Automated — Ricardo ↔ Gisele private never cross-read (D-033) | Staging gate before prod |

**Non-prod testing (D-034):** Real account **Artur** — staging/dev stand-in for Gisele workspace RBAC; synthetic data only; disabled before production.

**Indexed sources (D-019, D-040):** **Google Drive/Docs (workspace roots) + Git** + optional Obsidian paths.

## MVP — OUT (post-MVP)

| Category | Examples | Phase (tentative) |
|----------|----------|-------------------|
| Clinical slice | Meet transcripts, Patient-00N, Virtuologia analysis | Post-MVP gated (D-026–D-030) |
| Integrations | Calendar, Tasks, contacts | P10–P11 |
| Controlled writes | Alba writes to `Root_*/Alba/…` (P8); searchable after TTL (D-042) | P8 |
| Interactive voice | Step-by-step recipe reading, Alexa | P13–P14 |
| Android capture | Voice → API | P13 |

## Post-MVP — Gisele clinical slice (gated)

> Not MVP. Requires D-027–D-030 + professional LGPD review (D-028).

| Feature | Description |
|---------|-------------|
| Meet transcript import | Manual placement in Drive session tree at MVP (D-045); auto-routing post-MVP | Post-MVP gated |
| Clinical RAG search | De-identified Patient-00N only; `gisele` partition; encrypted at rest |
| Virtuologia analysis | Cloud LLM summaries/patterns (D-029) |
| Hard delete | Remove patient/session from Obsidian + clinical index (D-030) |

## Post-MVP — controlled writes (P8)

| Feature | Description |
|---------|-------------|
| Save draft to Drive | Alba writes Google Doc under `Root_*/Alba/…`; searchable after TTL (D-042) |
| Save idea to Git | Structured `.md` → `ideas/` or `habilidades/` |
| Optional Obsidian | Mirror `Alba/` if Ricardo uses vault |

## Post-MVP — integrations

| Feature | Phase (tentative) | Tool |
|---------|-------------------|------|
| Meeting context (read-only) | P10 | Google Calendar |
| Task context / create draft | P11 | Google Tasks or Todoist |
| Voice capture | P13 | Android app → API |
| Short voice commands | P14 | Alexa Skill (or alternative) |

## Explicit non-goals (MVP)

- Clinical / patient content in RAG (clinical slice post-MVP)
- Gmail indexing
- Autonomous writes without TTL/searchability rules (D-042)
- Calendar/Tasks as indexed sources at MVP
- Replacing Calendar or Tasks as systems of record
- Interactive voice / Alexa at MVP
- Full Alexa/ChatGPT long conversation replacement

See [`non-goals.md`](../spec/non-goals.md) after P1 spec gate.

## MVP success metrics (D-035)

> P6–P7 go-live validation. Integrations/clinical/voice excluded — see deferred below.

### Core (all users)

- Isolation tests pass on staging (D-033)
- Hybrid search: **fixture suite, top-3, 100% pass on staging** (D-036)
- Staging corpus: **synthetic only, AI/app-generated** (D-037)
- Production: **manual smoke checklist** per persona after promote (D-038)
- API + MCP healthy on staging
- Staging sign-off before prod (D-011)

### Per persona

| Persona | MVP metric |
|---------|------------|
| Alba Dev (Ricardo) | Project context, decision lookup, coding standards from Git index |
| Alba Texto (Gisele) | Non-clinical `gisele` search; no Ricardo workspace leakage |
| Alba Casa | `casa` recipes/notes searchable |

### Deferred (post-MVP metrics)

- Clinical (Virtuologia, Meet, Patient-00N) — P9
- Calendar, Tasks, Drive, contacts — P10–P12 (D-025 model; not MVP index)
- Voice, writes — P8, P13–P14
