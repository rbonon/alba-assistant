# DECISIONS — architectural decision history

This file is **append-only**. New sessions add entries at the bottom under a dated heading.

---

## 2026-07-07 — Product foundation & vision validation

### Alba as context assistant (not document repository)

**Decision:** Build Alba as a multi-workspace context assistant with personas and permission filters — not a passive document store.

**Rationale:** Primary use is retrieve, synthesize, and reuse context across Obsidian, Git, and future integrations.

**Implications:**
- API/MCP exposes tools, not raw file dumps only
- Workspace + user filters on every retrieval path

### Canonical sources vs RAG index

**Decision:** Obsidian and Git are canonical stores; RAG is a regenerable index only.

**Rationale:** Index must be rebuildable; canonical data must survive index loss.

**Implications:**
- Never treat vector DB as sole copy of important knowledge
- Support full reindex from sources

### Multi-workspace model

**Decision:** Day-one workspaces: `ricardo`, `gisele`, `casa`, `compartilhado` with explicit access rules.

**Rationale:** Prevent cross-context leakage between family members.

**Implications:**
- Metadata on every indexed document/chunk includes workspace + owner
- Permission matrix enforced at search time

### Controlled AI writes

**Decision:** AI-generated notes land in `00 Inbox/AI Drafts/` until human review and promotion.

**Rationale:** Quality and privacy gate before canonical Obsidian folders.

### MVP privacy boundary

**Decision:** Clinical/sensitive mental-health content stays out of MVP index.

**Rationale:** LGPD and trust; Gisele workspace needs explicit privacy design before production.

### Read-only first; staging before production

**Decision:** First implementation is read-only indexing and search; prove in staging before production for each slice.

**Rationale:** Reduce risk of bad writes and secret leakage; align with handoff mitigation for complexity.

### Operational systems boundary

**Decision:** Calendar and Tasks remain systems of record; Obsidian holds meeting/task *context* only.

**Rationale:** Avoid duplicating scheduling truth in notes.

### GitHub Pages project docs (English)

**Decision:** Publish project documentation from `/docs` on GitHub Pages in English.

**Rationale:** Readable portal for progress, features, architecture — mirroring fortegb/platform pattern.

### Planned Alba GitHub organization

**Decision:** Plan migration to an **Alba** GitHub org holding `alba-assistant`, `alba-docs`, and future repos. Timing TBD (Q-012).

**Rationale:** Native Epic issue types, shared conventions, product separation from personal account.

**Implications:**
- Until migration: use `[Epic]` issue title prefix on `rbonon/alba-assistant`
- Revisit board + Pages URLs after org move

### Model A — leaf issue change linkage

**Decision:** Every **leaf** issue (Feature/Chore) flows through `rbo-create-change` → branch → propose → close with `Closes #N`. Epics and gates never get a branch or change.

**Rationale:** Traceability between board, branch, OpenSpec, and commits without OpenSpec on epics.

**Implications:**
- Planning docs (P1–P5) use lightweight OpenSpec (proposal + tasks)
- P0 leaf issues #7–#12 retro-closed against commits already on `main` (one-time exception)
- No more direct-to-main leaf work

### P0 gate closed — P1 started (2026-07-07)

**Decision:** P0 foundation approved. Gate #13 and epic #1 closed. P1 broken into leaf issues #14–#30.

**Implications:**
- Next work: `rbo-create-change` on #14 (grilling Q-001)
- Spec implementation blocked until `[Gate] P1` (#30)

### REST-only ROADMAP refresh (2026-07-08)

**Decision:** `scripts/gen-docs.py` regenerates `ROADMAP.md` and `board-hierarchy.md` via REST only (`gh api repos/.../issues`). No `gh project` GraphQL in refresh paths.

**Rationale:** GraphQL runaway from chained refresh scripts exhausted API budget.

**Implications:**
- `./scripts/refresh-roadmap.sh` and `refresh-board-hierarchy.sh` are thin wrappers
- Board item-add remains bounded GraphQL (`add-issues-to-board.sh`) — one-shot, `set -euo pipefail`

### Product management skills (ai-skills, 2026-07-08)

**Decision:** Ship **`rbo-product-bootstrap`**, **`rbo-product-test`**, **`rbo-product-release`** in `ai-skills` as the canonical product SDLC suite.

**Rationale:** Repeatable greenfield/brownfield bootstrap without retyping instructions; integration testing and release ceremony separated from bootstrap.

**Implications:**
- Alba board still uses P0–P14 map; realign to suite phase template is **future work**
- Guide: `ai-skills/docs/rbo-product-bootstrap-guide.md` · Suite: `ai-skills/docs/rbo-product-skills.md`
- Prod promote stays manual (Vercel/GitHub); `rbo-product-release` does not deploy

---

## TBD (resolve in grilling — do not implement assumptions)

- Tech stack: SQLite vs Postgres path, vector DB, embedding model (P2)
- Obsidian vault topology: single vault vs multiple (P2)
- Hosting: local vs homelab vs cloud (P3)
- MVP primary user scope: Ricardo-only vs Ricardo+Gisele day one (P1 — Q-001)
