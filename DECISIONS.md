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

### MVP RAG indexed sources (2026-07-08 — #15 Q-001)

**Decision:** **MVP RAG indexes Obsidian + Git only.**

| Source | Canonical | MVP index? |
|--------|-----------|------------|
| Obsidian | Human memory | **Yes** |
| Git (selected repos) | Technical memory | **Yes** |
| Google Calendar | Operational | **No** — post-MVP |
| Google Tasks | Operational | **No** — post-MVP |
| Google Drive / Meet exports | Operational / files | **No** — post-MVP |
| Google Contacts | Operational | **No** — post-MVP |
| Gisele Meet transcriptions (clinical) | Meet/Drive | **No** — gated by privacy grilling **#16** before any indexing |

**Rationale:** Shippable MVP (P6–P7); Calendar/Tasks/Drive/contacts added in later phases. Clinical content requires LGPD design first.

**Implications:**
- Ricardo: repos + Obsidian at MVP; calendar/contacts via integration later
- Gisele: Obsidian notes indexable at MVP; Meet transcripts blocked until #16
- Casa recipes in Obsidian are covered (Obsidian index)
- Q-009–Q-011 reframed: integration scope for post-MVP, not MVP index

---

### Ricardo GitHub accounts for Git indexing (2026-07-08 — #15 Q-002)

**Decision:** MVP Git memory indexes repos across **all three GitHub identities**: `rbonon`, `fortegb`, and `akamlibehsafe`.

**Rationale:** Ricardo's technical knowledge spans personal, fortegb, and akamlibehsafe repos; MVP should cover the full set he named.

**Implications:**
- Index config is per-account + per-repo allowlist (paths, secrets exclusions)
- Auth/credentials for multi-account Git access deferred to P2/P3 (#15 Q-002 does not lock mechanism)
- Repos remain canonical in Git; RAG is derivative only (D-004)

---

### AI ideation workflow — canonical storage (#15 Q-003)

**Decision:** ChatGPT/Claude sessions (voice or text) are **ephemeral ideation** — not canonical, not indexed as primary storage. The **final markdown** describing the idea is canonical in **Obsidian** (promoted note or `Inbox/AI Drafts` → human promotes).

| Stage | Role |
|-------|------|
| Chat (ChatGPT/Claude) | Bounce ideas until refined — **discard or don't index raw threads** |
| Final idea `.md` | **Obsidian** — system of record for the idea |
| New product/code | **Git repo** when building — technical canon (D-003); idea doc stays in Obsidian with link to repo |

**Rationale:** Matches D-002 (human memory) and user practice; Obsidian is better than a fresh repo for idea docs that may never become code. Cursor/Claude access via indexed Obsidian + Git when a repo exists.

**Implications:**
- No RAG indexing of raw chat exports as canon
- Optional: index promoted Obsidian idea notes at MVP
- Spawning a Git repo is a **later step** when implementing — not the default home for idea MDs

---

### Idea doc when Git repo exists (#15 Q-004)

**Decision:** When an idea spawns a Git repo, the **canonical idea document stays in Obsidian** (Option A). The repo holds code and technical docs; README or links point back to Obsidian. Obsidian is not replaced by repo `docs/vision/`.

**Rationale:** Single source of truth for the idea; avoids duplicate canon (D-002 vs D-003 split stays clean).

**Implications:**
- Alba indexes Obsidian idea notes + Git code/docs with distinct roles
- Repo bootstrap may copy excerpts but Obsidian remains authoritative for product intent

---

### Never-index list (#15 Q-005)

**Decision:** Hard **never-index** exclusions (all phases unless explicitly reopened in grilling + `DECISIONS.md`):

| Category | Examples |
|----------|----------|
| Secrets | `.env`, credentials, API keys, tokens |
| Build/vendor | `node_modules`, `dist`, build output, `.git` internals |
| Clinical / patient | Meet transcriptions, patient identifiers — **no indexing until #16** approves gated path |
| Raw chat logs | ChatGPT/Claude thread exports (D-021) |

**Rationale:** Security, LGPD, and canon hygiene; aligns with architecture invariants.

**Implications:**
- Ingestion pipelines must enforce path/content blocklists
- #16 privacy grilling defines any future clinical indexing exception

---

### RAG rebuild policy (#15 Q-006)

**Decision:** On corrupt, stale, or schema-change recovery, Alba SHALL support **full rebuild from canonical sources** (Option A) — discard the index and re-ingest Obsidian + Git from scratch.

**Rationale:** Reinforces D-004; canonical sources are always truth; index is disposable.

**Implications:**
- No requirement to preserve vector DB across rebuilds
- Scheduled periodic rebuilds may be added later in platform ops (P7) — not MVP requirement

---

### Calendar/Tasks access model (#15 Q-007)

**Decision:** Lock this operational model for spec (integration/indexing **post-MVP** per D-019):

| Layer | Rule |
|-------|------|
| **Personal** | Ricardo and Gisele each have **own** Calendar + Tasks (systems of record) |
| **Casa shared** | **Shared family** Calendar + Tasks — both users can access |
| **Obsidian** | **Context notes only** — never duplicate scheduling/task truth (D-010) |
| **MVP** | Model documented in P1 spec; API integration and RAG indexing deferred |

**Rationale:** Matches multi-user day one (D-015), workspace isolation (D-016), and casa shared use cases (schedules, recipes separate — recipes in Obsidian `casa`).

**Implications:**
- Post-MVP integrations must respect per-user + casa shared calendar/task IDs
- Alba retrieval filters by authenticated user and shared casa resources
- Provider choice (Google Calendar/Tasks vs alternatives) remains Q-009/Q-010

---

### Gisele clinical content — pseudonym model (#16 Q-002)

**Decision:** Gated **post-MVP** clinical path in Alba with this obfuscation model:

| Layer | Content |
|-------|---------|
| **RAG (gisele clinical partition)** | **Patient-001, Patient-002, …** only — de-identified session text |
| **Obsidian (`gisele`)** | Full identity mapping (name, email, etc.) + full transcripts + Gisele's notes — canonical |
| **Assignment** | **Auto on ingest** — match existing patient (Meet series, email, prior session) or assign next Patient-00N; Gisele does **not** pick numbers in normal flow |
| **Corrections** | Gisele may split/merge patients or fix mapping in Obsidian when match is wrong |

**Rationale:** Stronger than first-name-only; preserves Virtuologia analysis; mapping outside search index; low friction for Gisele.

**Implications:**
- Ingest pipeline transforms clinical paths before embed; raw PII never in RAG
- Return consults match to existing Patient-00N automatically
- Encryption and legal review — #16 Q-003+
- No Alba patient-consent workflow (Q-001 direction)

---

### Clinical partition encryption (#16 Q-003)

**Decision:** **Encryption at rest is required** before the Gisele **clinical slice** goes live (Option A). Clinical vectors + metadata use a **separate encryption key** from the family index; host disk encryption (FileVault/LUKS) alone is **not** sufficient.

**Rationale:** Pseudonymization (D-026) and encryption address different threats; LGPD Art. 46 expects appropriate technical measures for sensitive health data.

**Implications:**
- Clinical slice blocked until app-level at-rest encryption is implemented and validated
- TLS required in transit (baseline)

---

### Clinical slice admission gates (#16 Q-004)

**Decision:** Lock all admission gates before Gisele clinical slice goes live:

| Gate | Rule |
|------|------|
| **Timing** | **Post-MVP only** — not in MVP RAG (D-019) |
| **Scope** | **`gisele` clinical partition only** — never `compartilhado`, `casa`, or Ricardo |
| **Consent** | **No Alba patient-consent workflow** — Gisele imports her own Meet data under her accounts |
| **Legal** | **Professional LGPD review required** before clinical slice go-live |

**Rationale:** Clear go/no-go checklist; separates family MVP from sensitive health path.

**Implications:**
- Clinical slice is a distinct delivery increment with its own gate checklist
- D-023 never-index exception for clinical only after these gates + D-027 encryption

---

### Clinical AI inference (#16 Q-005)

**Decision:** Clinical slice AI (summaries, Virtuologia analysis) **may use cloud LLM APIs** (Option B — Claude/OpenAI etc.) with **de-identified Patient-00N text**.

**Rationale:** User priority is maximum model quality and simplest path to AI benefits; pseudonymization (D-026) reduces but does not eliminate sensitive-data exposure to providers.

**Implications:**
- Prefer API terms with **no training** on customer data; document provider choice in P2/P3
- Encryption at rest (D-027) and partition isolation still required
- Legal review (D-028) must cover subprocessors / international transfer
- Local-only inference may be added later as optional hardening — not default

---

### Clinical data retention & erasure (#16 Q-006)

**Decision:** **Hard delete** (Option A) — when Gisele deletes a patient or session, remove from **Obsidian (canonical) and clinical RAG index**; index rebuild confirms removal. No soft-delete retention of clinical content by default.

**Rationale:** LGPD erasure (right to deletion); provable removal for sensitive health data.

**Implications:**
- Delete API/workflow must cascade Obsidian notes + clinical vectors + metadata
- Audit log may record *that* deletion occurred (not retained content)

---

### MVP scope boundary (2026-07-08 — #17 Q-001)

**Decision:** Lock P6–P7 production go-live capability bundle:

**MVP IN:**
- Read-only hybrid search — Obsidian + Git (D-019)
- Ricardo + Gisele multi-user; workspace isolation (D-015, D-016)
- HTTP API + MCP: `search_memory`, `get_decisions`, `get_project_context`
- Casa / `compartilhado` Obsidian content searchable (e.g. recipes as notes)
- Ricardo Git indexing: `rbonon`, `fortegb`, `akamlibehsafe` (D-020)
- Staging → controlled production promotion (D-011)

**MVP OUT (post-MVP):**
- Gisele clinical slice / Meet transcripts (D-026–D-030)
- Calendar, Tasks, Drive, contacts integration (D-019, D-025)
- Controlled writes to Obsidian inbox (P8)
- Interactive voice recipes (“read ingredients step by step”)
- Android voice capture, Alexa (P13–P14)

**Rationale:** Read-only memory platform first; prior grills aligned; avoids scope creep into integrations and clinical before core works.

**Implications:**
- P6–P7 deliverables trace to this list
- Spec leaves #26–#28 use this boundary
- Success metrics (#18) measure MVP IN only

---

### Board P9 reframe — Gisele clinical slice (#17 Q-002)

**Decision:** Reframe delivery phase **P9** from *"Gisele workspace"* to **Gisele clinical slice** (Option A). P9 delivers post-MVP gated clinical capabilities (D-026–D-030), not first Gisele access — that is **MVP P6–P7** (D-015).

**Rationale:** D-015 made multi-user day one; old P9 label was stale and misleading.

**Implications:**
- Update `docs/planning/phases.md` and portal phase map when refreshed
- P6–P7 MVP includes Gisele non-clinical Obsidian + shared workspaces only

---

### Cross-workspace isolation tests at MVP (#17 Q-003)

**Decision:** **Automated cross-workspace isolation tests are an MVP blocker** (Option A). Ricardo MUST NOT retrieve Gisele private content (and vice versa) — tests must pass on **staging** before production promote.

**Rationale:** Multi-user day one (D-015) without provable isolation (D-016) is unacceptable for privacy/LGPD trust.

**Implications:**
- P6–P7 delivery includes isolation test suite (integration level; harness timing P2/P16 TBD)
- Manual validation alone is insufficient for prod go-live

---

### Non-prod stand-in user Artur (#17 Q-004)

**Decision:** **Artur** = real third account, **dev/staging only**, stand-in for **Gisele workspace testing** so Gisele does not need credentials during dev/test. Artur receives **same workspace RBAC as Gisele** (`gisele` + `compartilhado` + `casa`, D-016) in non-prod. **Synthetic/fixture data only** — no real patient content in staging. **Artur disabled or removed before production go-live**; Gisele uses real credentials at prod. Artur is **not** a permanent production family user (no ongoing `artur` workspace in prod).

**Rationale:** Reduces burden on Gisele during development; isolation tests (D-033) still validate Ricardo ↔ gisele-workspace boundaries using Artur as stand-in.

**Implications:**
- P3 environments: document Artur in staging auth config; prod provisioning excludes Artur
- Clinical slice staging tests use synthetic Patient-00N fixtures only

---

### MVP success metrics structure (#18 Q-001)

**Decision:** Lock P6–P7 go-live success metrics in four layers. Metrics measure **MVP IN only** (D-031); integrations, clinical, and voice are explicitly deferred.

**Core (all MVP users — D-015, D-031, D-033):**

| Metric | Criterion |
|--------|-----------|
| Workspace isolation | Automated cross-workspace isolation tests **pass on staging** before production promote (D-033) |
| Search quality | Hybrid search fixture suite — top-3, 100% pass on staging (D-036) |
| API + MCP | HTTP health + MCP `search_memory` succeed on staging |
| Promotion gate | Staging sign-off before production promotion (D-011) |

**Ricardo — Alba Dev:**

| Metric | Criterion |
|--------|-----------|
| Project context | Retrieves project context (Obsidian + Git) for a named project |
| Decision lookup | Finds a prior decision on a known indexed topic |
| Standards lookup | Finds coding standards from indexed repos (`rbonon`, `fortegb`, `akamlibehsafe`) |

**Gisele — Alba Texto (non-clinical only):**

| Metric | Criterion |
|--------|-----------|
| Non-clinical search | Searches non-clinical Obsidian notes in `gisele` workspace |
| Isolation | Zero leakage from Ricardo private workspace |

**Casa — Alba Casa:**

| Metric | Criterion |
|--------|-----------|
| Casa search | Recipes/notes in `casa` workspace searchable via Obsidian index |

**Deferred post-MVP (not MVP success metrics):**

| Category | Examples | Track |
|----------|----------|-------|
| Clinical | Virtuologia, Meet transcripts, Patient-00N | P9 clinical slice (D-026–D-030) |
| Integrations | Ricardo/Gisele personal Calendar & Tasks; Casa shared Calendar/Tasks; Drive, contacts | P10–P12 (#22–#24); model D-025 |
| Voice | Interactive recipe reading, Alexa | P13–P14 |
| Writes | Obsidian inbox drafts | P8 |

**Rationale:** Aligns metrics with D-031 MVP boundary; Ricardo Calendar/Tasks are operational systems (D-010, D-025) — not indexed or validated at MVP go-live.

**Implications:**
- P6–P7 acceptance tests trace to this structure
- `#18-Q-002` locks pass rule (top-3, 100% fixtures on staging)
- `#18-Q-003`/`D-037` synthetic AI/app-generated staging corpus
- `#18-Q-004`/`D-038` prod manual smoke checklist
- Spec leaves #26–#28 inherit this as requirements input

---

### MVP search quality bar (#18 Q-002)

**Decision:** Hybrid search validation on **staging** uses a **curated fixture suite** (Option A):

| Rule | Value |
|------|-------|
| Fixture size | ~10–20 queries per layer (core search + Ricardo + Gisele + Casa) |
| Pass criterion | Expected document appears in **top 3** results |
| Gate | **100% pass** required before production promote |
| Isolation | Separate fixture suite for cross-workspace isolation (D-033) — not mixed with relevance fixtures |

**Rationale:** Binary, reproducible gate without embedding-score calibration debate at go-live. Persona scenario metrics (D-035) map to fixture queries in each layer.

**Implications:**
- Fixture definitions live in repo (test harness — implementation P6/P7)
- Staging index uses fixture corpus; data policy → D-037
- No percentage threshold (Option B rejected); no manual-only gate (Option C rejected)

---

### Staging fixture corpus (#18 Q-003)

**Decision:** Staging search/isolation tests use **synthetic data only** (Option A) — **no real family content** in the staging test index (aligns with D-034 Artur/synthetic staging policy).

**Generation:** Synthetic corpus is **generated by the Alba app/tooling** (AI-assisted or templated seed), **not** hand-maintained markdown fixtures checked into the repo as canonical test data.

| Layer | Rule |
|-------|------|
| Staging index | App-generated synthetic Obsidian + Git-shaped fixtures matching workspace tags (`ricardo`, `gisele`, `casa`, `compartilhado`) |
| Fixture queries | Curated expected query → document pairs (D-036); validated against generated corpus |
| Production | No automated fixture suite on real user data; **manual smoke test** after promote |

**Rationale:** Privacy-safe and reproducible staging; avoids maintaining brittle hand-written fixture files; generation can evolve with schema/index changes.

**Implications:**
- P6/P7 delivery includes staging **seed/generate** step (bootstrap or test harness)
- Fixture query definitions may live in repo; indexed **content** is generated at staging setup
- Prod validation is human spot-check, not fixture automation on live vaults

---

### Production post-promote validation (#18 Q-004)

**Decision:** After staging gate passes and production is promoted, validation is a **manual smoke checklist** (Option A) — **not** re-running the automated fixture suite on production.

| Check | Who | Example |
|-------|-----|---------|
| Alba Dev search | Ricardo | One real project-context or decision search on live index |
| Alba Texto search | Gisele | One non-clinical note search in `gisele` |
| Alba Casa search | Either user | One `casa` recipe/note search |
| Isolation spot-check | Ricardo or Gisele | Confirm no cross-private-workspace results in smoke queries |

**Rationale:** Staging owns reproducible automation (D-036, D-037); production validates against real vaults without automated queries touching live family data at scale.

**Implications:**
- P4 go-live checklist includes this smoke script (human sign-off)
- Automated fixtures remain staging-only forever unless explicitly reopened
- API/MCP health checks may still be automated on prod (infra); search acceptance is manual smoke

---

## TBD (resolve in grilling — do not implement assumptions)

- Tech stack: SQLite vs Postgres path, vector DB, embedding model (P2)
- Obsidian vault topology: single vault vs multiple (P2)
- Hosting: local vs homelab vs cloud (P3)
