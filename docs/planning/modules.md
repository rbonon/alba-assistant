# Modules & integrations

> Map for grilling and environment parity (P1 requirements → P3 environments).

## Canonical sources

| Module | Role | MVP | Staging | Production |
|--------|------|-----|---------|------------|
| **Obsidian** | Human memory — notes, templates, inbox/drafts | Index + templates | Staging vault paths | Live vault paths |
| **Git** | Technical memory — code, README, agent docs | Allowlist + exclusions | Test repos subset | Full allowlist |

## Alba runtime (to be built)

| Module | Role | MVP |
|--------|------|-----|
| **Ingestion** | Discover, chunk, embed, index | Obsidian + Git |
| **Retrieval** | Hybrid search + rerank | Yes |
| **API** | HTTP endpoints | `/memory/search`, health |
| **MCP** | Cursor / Claude tools | Read-only tools first |
| **Metadata store** | Document/chunk registry | SQLite (TBD) |
| **Vector store** | Embeddings index | LanceDB or Chroma (TBD) |

## Client integrations

| Module | Role | MVP | Later |
|--------|------|-----|-------|
| **Cursor MCP** | Dev assistant access | P7 | — |
| **Claude Code MCP** | Dev assistant access | P7 | — |
| **ChatGPT / other MCP** | Additional clients | — | Post-MVP |

## External integrations (post-MVP)

| Module | Role | Spec (P1) | Arch (P2) | Env (P3) | Build |
|--------|------|-----------|-----------|----------|-------|
| **Google Calendar** | Read event context | ✓ | ✓ | ✓ | P10 |
| **Tasks** (Google Tasks / Todoist) | Task boundaries | ✓ | ✓ | ✓ | P11 |
| **Google Drive** | Document index | ✓ | ✓ | ✓ | P12 |
| **Android voice** | Capture → API → inbox draft | ✓ | ✓ | ✓ | P13 |
| **Alexa / voice assistant** | Short commands | ✓ | ✓ | ✓ | P14 |

## Environments

Every module above must have a **staging** and **production** row in [`../architecture/environments.md`](../architecture/environments.md) (created in P3).
