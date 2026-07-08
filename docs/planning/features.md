# Feature set — Alba Context Assistant

> Business-facing capability map. **MVP boundary locked D-031** (issue #17).

## MVP (P6–P7 go-live) — IN

| Feature | Description | Sources |
|---------|-------------|---------|
| Read-only memory search | Hybrid vector + keyword search, workspace-filtered | Obsidian `.md`, selected Git files |
| Git memory (Ricardo) | Index repos from `rbonon`, `fortegb`, `akamlibehsafe` | Git (per-repo allowlist) |
| Project context | Retrieve notes + repo docs for a named project | Obsidian + Git |
| Decision lookup | Find prior decisions on a topic | Obsidian decisions/research |
| Standards lookup | Coding/writing standards for Ricardo | Obsidian + Git agent docs |
| Casa / shared search | Recipes and family notes in `casa` / `compartilhado` searchable | Obsidian |
| Multi-user production | Ricardo + Gisele day one; workspace isolation | D-015, D-016 |
| HTTP API | `/memory/search` and health | Alba API |
| MCP tools | `search_memory`, `get_decisions`, `get_project_context` | MCP server |
| Staging → production | Controlled promotion from staging | All MVP components |
| Workspace isolation tests | Automated — Ricardo ↔ Gisele private never cross-read (D-033) | Staging gate before prod |

**Non-prod testing (D-034):** Real account **Artur** — staging/dev stand-in for Gisele workspace RBAC; synthetic data only; disabled before production.

**Indexed sources (D-019):** Obsidian + Git only.

## MVP — OUT (post-MVP)

| Category | Examples | Phase (tentative) |
|----------|----------|-------------------|
| Clinical slice | Meet transcripts, Patient-00N, Virtuologia analysis | Post-MVP gated (D-026–D-030) |
| Integrations | Calendar, Tasks, Drive, contacts | P10–P12 |
| Controlled writes | Drafts to Obsidian inbox | P8 |
| Interactive voice | Step-by-step recipe reading, Alexa | P13–P14 |
| Android capture | Voice → API | P13 |

## Post-MVP — Gisele clinical slice (gated)

> Not MVP. Requires D-027–D-030 + professional LGPD review (D-028).

| Feature | Description |
|---------|-------------|
| Meet transcript import | Auto-match or assign Patient-00N; Obsidian canonical chart |
| Clinical RAG search | De-identified Patient-00N only; `gisele` partition; encrypted at rest |
| Virtuologia analysis | Cloud LLM summaries/patterns (D-029) |
| Hard delete | Remove patient/session from Obsidian + clinical index (D-030) |

## Post-MVP — controlled writes (P8)

| Feature | Description |
|---------|-------------|
| Save research draft | Structured note → `00 Inbox/AI Drafts/` |
| Save recipe / decision draft | Template-based drafts for human review |
| Reindex on promote | Index updates after user moves note out of inbox |

## Post-MVP — integrations

| Feature | Phase (tentative) | Tool |
|---------|-------------------|------|
| Meeting context (read-only) | P10 | Google Calendar |
| Task context / create draft | P11 | Google Tasks or Todoist |
| Document metadata search | P12 | Google Drive |
| Voice capture | P13 | Android app → API |
| Short voice commands | P14 | Alexa Skill (or alternative) |

## Explicit non-goals (MVP)

- Clinical / patient content in RAG (clinical slice post-MVP)
- Gmail indexing
- Autonomous writes without human review
- Calendar/Tasks/Drive as indexed sources at MVP
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
