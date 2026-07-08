# Modules & integrations

> Map for grilling and environment parity (P1 requirements → P3 environments).

## Canonical sources

| Module | Role | MVP | Staging | Production |
|--------|------|-----|---------|------------|
| **Google Drive/Docs** | Human memory — Gisele, Casa, Ricardo docs; `Root_*/Alba/` tree | Index workspace roots | Synthetic fixture Drive trees (D-037, D-034) | Live per-user + shared Casa roots |
| **Git** | Technical memory — code, README, agent docs; Ricardo `ideas/`, `habilidades/` | Explicit allowlist + `canon`/`canon+code` profiles + exclusions (D-046–D-050) | Subset (e.g. `alba-assistant`) | Full curated allowlist per account |
| **Obsidian** | Optional human memory editor (primarily Ricardo); mirror `Alba/` | Optional path ingest | Optional staging paths | Optional live vault paths |

## Alba runtime (to be built)

| Module | Role | MVP |
|--------|------|-----|
| **Ingestion** | Discover, chunk, embed, index | Drive + Git + optional Obsidian |
| **Ingest audit** | Central log in metadata DB; admin UI + CLI (Ricardo) | Staging + production |
| **Retrieval** | Hybrid search + rerank; TTL-gated `searchable` flag | Yes |
| **API** | HTTP endpoints | `/memory/search`, health, `/admin/ingest` |
| **MCP** | Cursor / Claude / ChatGPT tools | Read-only tools first |
| **Metadata store** | Document/chunk registry + ingest_events | SQLite (TBD) |
| **Vector store** | Embeddings index | LanceDB or Chroma (TBD) |

## Client integrations

| Module | Role | MVP | Later |
|--------|------|-----|-------|
| **Cursor MCP** | Dev assistant access | P7 | — |
| **Claude Code MCP** | Dev assistant access | P7 | — |
| **ChatGPT / Claude** | Assistant UI via Alba API/MCP | P7 | — |

## External integrations (post-MVP)

| Module | Role | Spec (P1) | Arch (P2) | Env (P3) | Build |
|--------|------|-----------|-----------|----------|-------|
| **Google Calendar** | Read event context | ✓ | ✓ | ✓ | P10 |
| **Tasks** (Google Tasks / Todoist) | Task boundaries | ✓ | ✓ | ✓ | P11 |
| **Android voice** | Capture → API → draft | ✓ | ✓ | ✓ | P13 |
| **Alexa / voice assistant** | Short commands | ✓ | ✓ | ✓ | P14 |

## Environments

Every module above must have a **staging** and **production** row in [`../architecture/environments.md`](../architecture/environments.md) (created in P3).
