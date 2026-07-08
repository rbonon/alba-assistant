# Feature set — Alba Context Assistant

> Business-facing capability map. Technical choices stay open until P2 grilling.

## MVP (target: P6–P7)

| Feature | Description | Sources |
|---------|-------------|---------|
| Read-only memory search | Hybrid vector + keyword search, workspace-filtered | Obsidian `.md`, selected Git files |
| Project context | Retrieve notes + repo docs for a named project | Obsidian + Git |
| Decision lookup | Find prior decisions on a topic | Obsidian decisions/research |
| Standards lookup | Coding/writing standards for Ricardo | Obsidian + Git agent docs |
| HTTP API | `/memory/search` and health | Alba API |
| MCP tools | `search_memory`, `get_decisions`, `get_project_context` | MCP server |
| Staging environment | Full stack parity skeleton | All MVP components |
| Production go-live v0 | Controlled promotion from staging | All MVP components |

**MVP users:** Ricardo and Gisele from production go-live (multi-user day one). User model must support adding more users post-launch — each gets dedicated workspace, D-016 read rules, and assigned persona (D-018).

**Workspace read (D-016):** each user — own workspace + `compartilhado` + `casa`; never the other’s private workspace.

## Post-MVP — controlled writes (P8)

| Feature | Description |
|---------|-------------|
| Save research draft | Structured note → `00 Inbox/AI Drafts/` |
| Save recipe / decision draft | Template-based drafts for human review |
| Reindex on promote | Index updates after user moves note out of inbox |

## Post-MVP — multi-user (P9)

| Feature | Description |
|---------|-------------|
| Gisele workspace production | Persona Alba Texto, privacy-enforced filters |
| Cross-workspace isolation tests | Ricardo cannot read Gisele private content |

## Post-MVP — integrations

| Feature | Phase (tentative) | Tool |
|---------|-------------------|------|
| Meeting context (read-only) | P10 | Google Calendar |
| Task context / create draft | P11 | Google Tasks or Todoist |
| Document metadata search | P12 | Google Drive |
| Voice capture | P13 | Android app → API |
| Short voice commands | P14 | Alexa Skill (or alternative) |

## Explicit non-goals (MVP)

- Clinical / sensitive mental-health content in index
- Gmail indexing
- Autonomous writes without human review
- Replacing Calendar or Tasks as systems of record
- Full Alexa/ChatGPT long conversation replacement

See [`non-goals.md`](../spec/non-goals.md) after P1 spec gate.
