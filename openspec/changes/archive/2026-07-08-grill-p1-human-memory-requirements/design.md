## Context

- **Prior locks (may amend at close):** D-006 drafts; D-016 workspaces; D-019 Git at MVP; D-021 ephemeral chat; D-026–D-030 clinical gates
- **Grill pivot:** human memory is **multi-source** — not Obsidian-only (amends D-002 / D-019 scope at close)
- **Explored:** Gisele/Casa on Google Docs; Ricardo on Drive + Git `ideas/*.md` + optional Obsidian; ChatGPT/Claude as UI via Alba API/MCP; methodology Docs ≈ skills
- Issue **#19** scope expanded: human memory sources (Drive, Git, optional Obsidian); change `grill-p1-human-memory-requirements`

## Goals / Non-Goals

**Goals:**
- Lock MVP **human memory sources**: Drive/Docs (workspace roots) + Git; Obsidian **supported, optional per user**
- Drive folder conventions (`Root_Gisele/`, `Root_Ricardo/`, `Root_Casa/`, …) and workspace mapping
- Optional Obsidian path rules for Ricardo (if used)
- Drive tree under `Root_*/Alba/`; ingest poll + TTL; ingest audit log + admin UI
- Methodology / template Docs as first-class (Gisele)

**Non-Goals:**
- Runtime ingest implementation (P6)
- P8 write endpoints
- Obsidian Sync as requirement
- Clinical slice production index (post-MVP; folder shape may be defined now)

## Decisions

### Human memory sources — MVP principle (#19, 2026-07-08)

**Decision:** MVP human memory = **Google Drive/Docs by workspace roots** + **Git** (code + Ricardo `ideas/*.md` etc.). **Obsidian supported but optional** per user (primarily Ricardo if he chooses the app).

| Workspace / user | Primary human canon | Optional |
|----------------|---------------------|----------|
| Gisele | Drive/Docs (`Root_Gisele/…`) | — |
| Casa | Drive/Docs (`Root_Casa/…`) | — |
| Ricardo | Drive/Docs + Git | Obsidian vault |
| Code | Git | — |

**UI:** ChatGPT/Claude (and later thin Alba UI) talk to **Alba API/MCP**; chat threads ephemeral (D-021); canon stays in Drive/Git/Obsidian files.

**Implications at close:** amend D-002, D-019; add Drive ingest to MVP scope; Obsidian ingest remains for optional vault paths.

### Drive roots layout — hybrid C (#19-Q-002, 2026-07-08)

**Decision:** **Hybrid C** — per-user Drive roots + shared Casa root:

| Root | Location | Visible to |
|------|----------|------------|
| `Root_Gisele/` | Gisele’s My Drive | Gisele (+ Alba ingest creds scoped to her account) |
| `Root_Ricardo/` | Ricardo’s My Drive | Ricardo |
| `Root_Casa/` | Shared (both users) | Ricardo + Gisele |

**Auth:** Alba API/MCP uses **per-user authentication** — each user’s session maps to their workspace RBAC (D-016). Drive ingest uses **scoped credentials per account** (service account or OAuth per user — mechanism P2/P3; requirement locked here).

**Staging — Artur (D-034):** **Artur** = non-prod stand-in with **same RBAC as Gisele** (`gisele`, `casa`, `compartilhado`); synthetic fixture Drive tree only; **disabled before prod**; Gisele uses real credentials at go-live.

### Drive tree — `Root_*/Alba/` namespace (#19, 2026-07-08)

**Decision:** Each user root contains a single **`Alba/`** namespace; human + Alba content lives under it (not a sibling `Alba/` next to canon):

```text
Root_Gisele/Alba/
  Sessões de Terapia/
  Metodologia/
  Anotações Gerais/
  Nova Funcionalidade Alba/
  …
```

Same pattern for `Root_Ricardo/Alba/`, `Root_Casa/Alba/`. **No `Alba/Validar/` folder on Drive** — ingest QA is not a content queue.

### Ingest, searchability, audit — no human approval (#19-Q-003, 2026-07-08)

**Decision:**

| Rule | Value |
|------|--------|
| Human / Alba writes | **Direct to final folder** under `Root_*/Alba/…` — **no** human approval step |
| Index trigger | **Poller** (~15 min) + change detection per source (`modifiedTime`, git push, optional file watcher for Obsidian) |
| Searchability | **`searchable` after TTL** without edit, **per subfolder** (one policy table — not per-user flows) |
| Index update | **Replace by stable id** (`drive_file_id`, git path+commit) — not additive duplicates |
| Ingest audit | **Central log in Alba metadata DB** — **staging and production** |
| Admin visibility | **HTTP admin UI + CLI** (auth: Ricardo; Artur in staging); metadata + optional snippet / drill-down — **not** a Drive folder |
| `Alba/Validar/` on Drive | **Rejected** — was conflated with ingest QA; QA = DB + admin only |

**Amends at close:** D-006 (no mandatory human promote from inbox); optional Obsidian `Inbox/` only if Ricardo uses vault — same TTL policy or align at #19-Q-005.

### Habilidades da Alba (#19-Q-004, 2026-07-08)

**Decision:** Skills analogue — folder **`Root_*/Alba/Habilidades/`** (multiple skills expected over time). Each skill = **one file** describing inputs, steps, and deliverables.

| User / area | Skill format | Location |
|-------------|--------------|----------|
| Gisele | Google Doc (`.gdoc`) | `Root_Gisele/Alba/Habilidades/` |
| Casa | Google Doc | `Root_Casa/Alba/Habilidades/` |
| Ricardo | **Drive and/or Git** | `Root_Ricardo/Alba/Habilidades/` and/or `habilidades/*.md` in a Git repo |

**Template (all formats):** `Quando usar` · `Workspace(s)` · `Entradas` · `Passos` · `Entregáveis` · `O que não fazer`.

**Index:** `doc_type=habilidade`; same TTL/search rules as sibling subfolders. Advanced automations (Virtuologia clínica, conciliação recibos/cartão, etc.) = **post-MVP** skills in catalog; P1 spec lists pattern + initial examples only.

### Obsidian optional — Ricardo (#19-Q-005, 2026-07-08)

**Decision:** Obsidian **supported, optional** (primarily Ricardo). If used, mirror the **`Alba/`** tree under the vault (e.g. `Alba/Habilidades/*.md`, session folders as needed) — same namespace as Drive; **no Obsidian Sync required**; ingest via local paths on the Alba host.

**Habilidades on Obsidian:** allowed — `.md` with the **same template** as Git; `doc_type=habilidade`, `source=obsidian`. **One skill = one file = one canonical source** (no duplicate across Drive, Git, and vault).

Gisele/Casa: **no Obsidian requirement**.

### Meet transcripts (#19-Q-006, 2026-07-08)

**Decision:** **Manual (A)** — Gisele saves or moves the Meet transcript Google Doc into the patient session tree (e.g. `Root_Gisele/Alba/Sessões de Terapia/Paciente N/YYYY MM DD Sessão NN Transcrição.gdoc`). Alba **poll + TTL** only; no auto-routing from Meet in MVP. Semi-auto / auto placement deferred post-MVP.

## Risks / Trade-offs

- [Drive API ingest] → more engineering than filesystem md — acceptable at family scale
- [Multi-source duplication] → same note in Obsidian + Git + Drive — mitigate with source priority / dedup by hash
- [ACL mapping Drive] → workspace isolation tests must include Drive folders (D-033)
- [Amending locked decisions] → explicit DECISIONS.md entries on #19 close

## Open Questions

| ID | Question | Status |
|----|----------|--------|
| #19-Q-001 | ~~Obsidian vault topology~~ → **Human canon source map** (locked above) | **Closed** |
| #19-Q-002 | Drive layout: hybrid C + per-user auth + Artur staging (D-034) | **Closed** |
| #19-Q-003 | Ingest: no human approval; poll + TTL/subfolder; audit log in DB + admin UI (staging + prod) | **Closed** |
| #19-Q-004 | Habilidades: `…/Alba/Habilidades/`; gdoc (Gisele/Casa); Ricardo **Drive + Git** md; shared template | **Closed** |
| #19-Q-005 | Obsidian optional (Ricardo); `Alba/` mirror incl. `Habilidades/*.md`; same template; no Sync required | **Closed** |
| #19-Q-006 | Meet transcript: manual placement in session tree; Alba poll + TTL | **Closed** |
