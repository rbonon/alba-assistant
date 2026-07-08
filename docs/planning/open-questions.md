# Open questions — grilling backlog

> One grilling session resolves one question (or a tight group). Move closed items to [decisions.md](./decisions.md) and root [DECISIONS.md](../../DECISIONS.md).

| ID | Topic | Phase | Status |
|----|-------|-------|--------|
| Q-001 | MVP primary user — Ricardo only vs Ricardo + Gisele day one | P1 | **Closed** — D-015 |
| #14-Q-002 | MVP workspace read boundaries per user | P1 (#14) | **Closed** — D-016 |
| #14-Q-003 | MVP persona mapping | P1 (#14) | **Closed** — D-017 |
| #14-Q-004 | Post-launch user onboarding model | P1 (#14) | **Closed** — D-018 |
| #15-Q-001 | MVP RAG indexed sources | P1 (#15) | **Closed** — D-019 |
| #15-Q-002 | Ricardo GitHub accounts for Git indexing | P1 (#15) | **Closed** — D-020 |
| #15-Q-003 | AI ideation → canonical storage | P1 (#15) | **Closed** — D-021 |
| #15-Q-004 | Idea doc when Git repo exists | P1 (#15) | **Closed** — D-022 |
| #15-Q-005 | Never-index list | P1 (#15) | **Closed** — D-023 |
| #15-Q-006 | RAG rebuild policy | P1 (#15) | **Closed** — D-024 |
| #15-Q-007 | Calendar/Tasks personal + Casa shared model | P1 (#15) | **Closed** — D-025 |
| #16-Q-002 | Gisele clinical pseudonym + auto-assign | P1 (#16) | **Closed** — D-026 |
| #16-Q-003 | Clinical partition encryption at rest | P1 (#16) | **Closed** — D-027 |
| #16-Q-004 | Clinical slice admission gates | P1 (#16) | **Closed** — D-028 |
| #16-Q-005 | Clinical AI inference (cloud) | P1 (#16) | **Closed** — D-029 |
| #16-Q-006 | Clinical retention & erasure | P1 (#16) | **Closed** — D-030 |
| #17-Q-001 | MVP IN / MVP OUT capability bundle | P1 (#17) | **Closed** — D-031 |
| #17-Q-002 | Reframe P9 → Gisele clinical slice | P1 (#17) | **Closed** — D-032 |
| #17-Q-003 | Cross-workspace isolation tests MVP blocker | P1 (#17) | **Closed** — D-033 |
| #17-Q-004 | Non-prod stand-in user Artur (Gisele testing) | P1 (#17) | **Closed** — D-034 |
| #18-Q-001 | MVP success metrics structure (core + personas + deferred) | P1 (#18) | **Closed** — D-035 |
| #18-Q-002 | Search quality bar — fixture set + relevance threshold | P1 (#18) | **Closed** — D-036 |
| #18-Q-003 | Staging fixture corpus — synthetic only vs real notes | P1 (#18) | **Closed** — D-037 |
| #18-Q-004 | Production post-promote validation — manual smoke only? | P1 (#18) | **Closed** — D-038 |
| #19-Q-001 | Human memory source map (Drive + Git + optional Obsidian) | P1 (#19) | **Closed** — D-039 |
| #19-Q-002 | Drive roots hybrid C + per-user auth | P1 (#19) | **Closed** — D-041 |
| #19-Q-003 | Ingest poll + TTL; audit log in DB + admin UI | P1 (#19) | **Closed** — D-042 |
| #19-Q-004 | Habilidades da Alba (`…/Alba/Habilidades/`) | P1 (#19) | **Closed** — D-043 |
| #19-Q-005 | Obsidian optional (Ricardo); `Alba/` mirror | P1 (#19) | **Closed** — D-044 |
| #19-Q-006 | Meet transcript manual placement | P1 (#19) | **Closed** — D-045 |
| #20-Q-001 | Git repo allowlist (explicit opt-in; staging subset) | P1 (#20) | **Closed** — D-046 |
| #20-Q-002 | Git indexed paths (canon / canon+code profiles) | P1 (#20) | **Closed** — D-047 |
| #20-Q-003 | Git ref scope (default branch only) | P1 (#20) | **Closed** — D-048 |
| #20-Q-004 | Git-specific exclusions (extend D-023) | P1 (#20) | **Closed** — D-049 |
| #20-Q-005 | Git secret handling (HEAD scan; skip file) | P1 (#20) | **Closed** — D-050 |
| #20-Q-006 | Amend D-021/D-022 — ideas + habilidades in Git | P1 (#20) | **Closed** — D-051 |
| Q-002 | Obsidian vault topology | P1 (#19) | **Closed** — optional Obsidian mirror (D-044); not family canon driver |
| Q-007 | Ingestion trigger — poll vs watch vs manual | P1 (#19) | **Partial** — poll ~15 min locked (D-042); file watcher optional Obsidian (P2) |
| Q-003 | Hosting model — local Mac, homelab, cloud VM | P3 | Open |
| Q-004 | Metadata store — SQLite MVP path to Postgres? | P2 | Open |
| Q-005 | Vector store — LanceDB vs Chroma vs Qdrant | P2 | Open |
| Q-006 | Embedding provider & model | P2 | Open |
| Q-007 | Ingestion trigger — file watch vs cron vs manual | P2 | **Partial** — see D-042 |
| #21-Q-001 | MVP MCP client priority (validate Cursor → Claude Code → chat) | P1 (#21) | **Closed** — D-052 |
| #21-Q-002 | MVP MCP tool catalog (five read-only tools) | P1 (#21) | **Closed** — D-053 |
| #21-Q-003 | Auth at client boundary (per-user token) | P1 (#21) | **Closed** — D-054 |
| #21-Q-004 | Workspace enforcement (server authority) | P1 (#21) | **Closed** — D-055 |
| #21-Q-005 | Chat vs IDE (MCP + API mirror) | P1 (#21) | **Closed** — D-056 |
| #21-Q-006 | Staging vs production client config | P1 (#21) | **Closed** — D-057 |
| Q-008 | Auth model for API/MCP — token format, storage, rotation (mechanism) | P2/P3 | Open — requirements locked D-054 (#21) |
| Q-009 | Google Calendar scope (read-only MVP of integration) | P1 | Open |
| Q-010 | Tasks provider — Google Tasks vs Todoist | P1 | Open |
| Q-011 | Alexa vs alternative voice assistant | P1 | Open |
| Q-012 | Alba GitHub org timing and repo migration | P0/P1 | Open — repo public on rbonon; org TBD |

**Next grilling:** issue **#22 — [Grill] P1 — Google Calendar scope**
