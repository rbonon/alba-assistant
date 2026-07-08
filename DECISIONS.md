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

### Deferred — post-P1 bootstrap inventory (2026-07-08)

**Decision:** After P1 leaves **#14–#30** close and **[Gate] P1** (#30) is approved, run
`rbo-product-bootstrap` **brownfield Step 1 only** (inventory + gap report; no mutations
until explicit OK). Checklist: `docs/planning/reminder-after-p1-gate.md`.

**Rationale:** Compare Alba compressed phase map vs suite template without derailing
in-flight P1 grilling.

**Implications:**
- Do not invoke full bootstrap during P1
- Realignment (if any) is a separate approved change — not automatic

---

### MVP multi-user from day one (2026-07-08 — Q-001, issue #14)

**Decision:** MVP production targets **multiple users from day one** — Ricardo and Gisele at launch, with the user model designed to add more users post-launch without rework.

**Rationale:** Family product intent; both primary users should benefit from go-live. Extensibility avoids a false "single-user MVP" that blocks Gisele.

**Implications:**
- P1 spec must cover two production users, workspace isolation, and persona mapping (Alba Dev / Alba Texto)
- Privacy/LGPD grilling (#16) is required before production — not optional
- Alba board P9 "Gisele workspace" may need reframing: multi-user is day one; P9 becomes capability depth or polish, not first Gisele access
- Revisit `features.md` and phase map when Q-002+ on #14 are resolved

---

### MVP workspace read boundaries (2026-07-08 — #14 Q-002)

**Decision:** At MVP production go-live, each user reads **own workspace + `compartilhado` + `casa`**. Users MUST NOT read the other’s private workspace (`ricardo` ↔ `gisele`).

| User | Read workspaces |
|------|-----------------|
| Ricardo | `ricardo`, `compartilhado`, `casa` |
| Gisele | `gisele`, `compartilhado`, `casa` |

**Rationale:** Family shared context via `casa` and `compartilhado`; strict isolation on personal workspaces for privacy/LGPD.

**Implications:**
- Retrieval and auth must enforce workspace filter per user
- Indexing must tag content by workspace; `casa` and `compartilhado` are shared read paths
- Privacy grilling (#16) builds on this baseline

---

### MVP persona mapping (2026-07-08 — #14 Q-003)

**Decision:** At MVP, personas are **fixed per user** (Option A):

| User / context | Persona |
|----------------|---------|
| Ricardo | Alba Dev — technical, implementation-focused |
| Gisele | Alba Texto — writing, clarity, preserves voice |
| `casa` workspace (either user) | Alba Casa — practical family tone |

**Post-MVP:** Persona switching, multi-persona per user, or richer persona customization MAY be added after go-live as new functionality (new issues/features — not MVP scope).

**Rationale:** Keeps MVP simple; matches primary use cases. Expansion path preserved without blocking launch.

**Implications:**
- API/MCP can default persona from authenticated user + workspace context
- Post-launch persona features → `rbo-create-issue` when prioritized

---

### Post-launch user model (2026-07-08 — #14 Q-004)

**Decision:** Each **new user added post-launch** gets a **dedicated workspace**, D-016 read rules (own + `compartilhado` + `casa`), and an **assigned persona** at onboarding — same pattern as Ricardo/Gisele.

**Rationale:** Consistent extensibility model; avoids one-off exceptions as the family grows.

**Implications:**
- User provisioning is a first-class concept in P1 spec (even if automation comes later)
- Persona catalog may grow; assignment at onboarding, switching still post-MVP (D-017)

---

## TBD (resolve in grilling — do not implement assumptions)

- Tech stack: SQLite vs Postgres path, vector DB, embedding model (P2)
- Obsidian vault topology: single vault vs multiple (P2)
- Hosting: local vs homelab vs cloud (P3)
