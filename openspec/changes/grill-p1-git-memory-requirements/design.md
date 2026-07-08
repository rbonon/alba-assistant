## Context

- **Prior locks (may amend at close):** D-003 Git = technical canon; D-016 workspaces; D-020 three GitHub accounts; D-021/D-022 ideation + idea doc (Obsidian-centric — **amend at #20**); D-023 never-index; D-039–D-045 human memory (Git + `habilidades/` in repos); D-042 poll + TTL ingest
- **Issue #20 scope:** repo allowlist, indexed paths, exclusion rules, secret handling
- **Explored:** Ricardo spans `rbonon`, `fortegb`, `akamlibehsafe`; repos mix product code, docs, agent context (`AGENTS.md`, `CLAUDE.md`); `ideas/` and `habilidades/` may live in Git per #19; staging uses subset + synthetic repos (D-034, D-037)

## Goals / Non-Goals

**Goals:**
- Lock **repo allowlist** model per GitHub account (explicit list; staging subset)
- Lock **indexed path patterns** within allowed repos (defaults + per-repo overrides)
- Lock **branch/ref scope** for indexing
- Extend **Git-specific exclusions** beyond D-023
- Lock **secret detection / never-index** handling for Git content and history
- Amend **D-021/D-022** for Git `ideas/` and `habilidades/` as canonical paths

**Non-Goals:**
- Git auth mechanism (P2/P3)
- Runtime ingest implementation (P6)
- Gisele Git repos (no Git canon for Gisele/Casa human memory — Drive per D-039)
- Indexing private third-party forks without explicit allowlist entry

## Decisions

### Repo allowlist — explicit opt-in (#20-Q-001, 2026-07-08)

**Decision:** Git indexing uses an **explicit per-account repo allowlist** in version-controlled config. **No auto-discovery** — a repo is indexed only when listed.

| Environment | Rule |
|-------------|------|
| **Staging** | Named **subset** of repos (fixture corpus for D-036/D-037); e.g. start with `rbonon/alba-assistant` (+ optional `rbonon/ai-skills`) |
| **Production** | **Full curated allowlist** per account (`rbonon`, `fortegb`, `akamlibehsafe`); each entry maps to workspace `ricardo` |

**Operational model:** add repo → edit allowlist config → deploy/restart ingest → poller picks up on next cycle (D-042). Repos not on the list are never touched (e.g. `medban-*` stay off unless explicitly added later). Config format and credentials deferred to P2/P3; admin UI shows list + ingest status (D-042).

**Rationale:** Matches D-023 privacy posture; staging stays small/synthetic; no surprise indexing of new or sensitive repos.

### Indexed paths — dual profile per allowlist entry (#20-Q-002, 2026-07-08)

**Decision:** Each allowlist entry declares an **`index_profile`**. Global exclusions (D-023 + #20-Q-004) apply on top. Optional `path_add` / `path_remove` per repo.

| Profile | Includes |
|---------|----------|
| **`canon`** | Root agent files (`AGENTS.md`, `CLAUDE.md`, `DECISIONS.md`, `README.md`, `STATUS.md`); `**/*.{md,mdx,txt}`; `docs/**`; `openspec/**` (including `archive/`); `ideas/**`; `habilidades/**` |
| **`canon+code`** | Everything in **`canon`** plus `src/**`, `app/**`, `lib/**`, `packages/**` (whichever exist in the repo) |

**Examples:** `alba-assistant`, `ai-skills` → `canon`; `fortegb/platform`, `shutterzilla-app` → `canon+code`.

**Rationale:** Docs/skills repos need canon + specs without indexing full build trees; app repos need code patterns (D-003). Profiles declared on the allowlist row — not inferred from repo name.

### Branch / ref scope — default branch only (#20-Q-003, 2026-07-08)

**Decision:** Git ingest indexes the **default branch only** (`main` / `master` / repo default). No tags, no all-branches scan, no PR head refs in MVP.

**Post-MVP (deferred):** optional per-repo branch allowlist (e.g. active `feat/*`) if needed.

**Rationale:** Canon = merged truth (D-003); simpler poller; feature-branch WIP indexed after merge.

### Git-specific exclusions — extend D-023 (#20-Q-004, 2026-07-08)

**Decision:** Git ingest applies D-023 **plus** the following path/content rules. **`*.example` config files remain indexed** (documentation, not secrets).

| Category | Patterns / rule |
|----------|-----------------|
| Secrets (extend) | `**/.env*`, `**/*.{pem,key,p12,crt,cer}` |
| Build/vendor (extend) | `**/.next/**`, `**/.turbo/**`, `**/__pycache__/**`, `**/.cache/**`, `**/coverage/**` |
| Lockfiles | `**/package-lock.json`, `**/yarn.lock`, `**/pnpm-lock.yaml` |
| Agent tool noise | `**/.cursor/**`, `**/.claude/**` (root `AGENTS.md` / `CLAUDE.md` still indexed via canon profile) |
| Asset folders | `**/_Branding/**` |
| Binaries | `**/*.{png,jpg,jpeg,gif,webp,ico,pdf,zip,tar,gz,woff,woff2,ttf,mp3,mp4,webm}` |
| Size cap | Skip any blob **> 1 MB** regardless of path |

**Force-include:** `.github/workflows/**` and other CI/config YAML under indexed paths — not excluded.

**Rationale:** Reduces index noise and cost; lockfiles and duplicated skill trees add little retrieval value; size cap catches unlisted binaries.

### Secret handling — HEAD scan, skip file (#20-Q-005, 2026-07-08)

**Decision:** At ingest time, scan **HEAD snapshot only** (default branch tree per #20-Q-003). **No Git history walk** in MVP.

| Rule | Value |
|------|--------|
| Content scan | Pattern matchers: GitHub PAT (`ghp_`, `github_pat_`), AWS key patterns, PEM blocks, `API_KEY=` / `SECRET=` in non-example files |
| `*.example` exemption | Exempt from secret patterns — indexed as documentation |
| On match | **Skip offending file only** (not whole repo); log `ingest_events` with `reason=secret_detected`; never index that blob |
| Admin | Visible in ingest audit log + admin UI (D-042) |

**Deferred post-MVP:** full history scan on first ingest; repo-level quarantine.

**Rationale:** Safety net on top of path exclusions; per-file skip avoids punishing entire repo for one bad file; history scan cost/risk trade-off acceptable for family scale at MVP.

### Ideas and habilidades in Git — amend D-021/D-022 (#20-Q-006, 2026-07-08)

**Decision:** **Amends D-021 and D-022.** D-043 unchanged.

| Topic | Rule |
|-------|------|
| **Ideation (D-021)** | Chat (ChatGPT/Claude) remains **ephemeral**. Final idea `.md` is canonical in **Obsidian `ideas/`** *or* **Git** (`ideas/<slug>.md` or `docs/vision/` in a repo). |
| **Idea + repo (D-022)** | Once a product repo exists, **Git in that repo is canonical** for the idea/vision doc; Obsidian may mirror but **Git wins on conflict**. |
| **Habilidades (D-043)** | Unchanged — `habilidades/*.md` in Git is canonical when that is where the skill file lives; one skill = one file = one source. |

**Rationale:** Matches Ricardo's product-repo workflow (`docs/vision/`, repo-local ideas); Obsidian optional (D-044); Git indexed via `canon` profile (#20-Q-002).

| ID | Topic | Status |
|----|-------|--------|
| #20-Q-001 | Repo allowlist model (per account; staging vs production) | **Closed** |
| #20-Q-002 | Indexed paths within repos (default globs + overrides) | **Closed** |
| #20-Q-003 | Branch / ref scope (default branch, tags, all branches) | **Closed** |
| #20-Q-004 | Git-specific exclusions (extend D-023) | **Closed** |
| #20-Q-005 | Secret handling (content + history; example env files) | **Closed** |
| #20-Q-006 | Amend D-021/D-022 — `ideas/` and `habilidades/` in Git | **Closed** |

## Risks / Trade-offs

- [Large monorepos] → path exclusions and size caps needed — define at grilling
- [Multi-account auth] → allowlist locked in P1; credential flow deferred P2/P3
- [Secret leakage via history] → must decide scan depth vs trust boundary
- [Amending D-021/D-022] → explicit DECISIONS.md entries on #20 close

## Open Questions

See table above. Grilling starts with **#20-Q-001**.
