# human-memory-requirements Specification

## Purpose
TBD - created by archiving change grill-p1-human-memory-requirements. Update Purpose after archive.
## Requirements
### Requirement: Human memory sources are defined for MVP

The product SHALL document MVP canonical human memory as **Google Drive/Docs (per workspace roots) + Git**, with **Obsidian supported but optional** per user.

#### Scenario: Multi-source canon locked

- **WHEN** grilling on issue **#19** completes
- **THEN** `DECISIONS.md` records Drive, Git, and optional Obsidian roles per workspace (D-039, D-040)

### Requirement: Drive folder layout and workspace mapping are defined

The product SHALL document `Root_Gisele/`, `Root_Ricardo/`, `Root_Casa/` each containing an **`Alba/`** namespace with subfolders mapped to workspaces `gisele`, `ricardo`, `casa`, and `compartilhado` (D-041).

#### Scenario: Path conventions documented

- **WHEN** grilling completes Drive layout
- **THEN** each workspace has documented Drive root paths and per-user auth requirements for ingest

### Requirement: Ingest trigger, searchability, and audit are defined

The product SHALL document poller-based ingest (~15 min), **TTL-per-subfolder** before documents are searchable, replace-by-stable-id indexing, central ingest log in Alba metadata DB (staging + production), and admin UI/CLI for Ricardo (D-042).

#### Scenario: No mandatory human approval queue

- **WHEN** grilling completes ingest rules
- **THEN** `DECISIONS.md` states writes go to final folders directly; no Drive `Validar/` approval folder; searchability follows TTL policy

### Requirement: Habilidades da Alba pattern is defined

The product SHALL document **`…/Alba/Habilidades/`** with one file per skill (Google Doc and/or `.md` on Git/Obsidian), shared template sections, and `doc_type=habilidade` indexing (D-043).

#### Scenario: Skills catalogue pattern

- **WHEN** grilling completes Habilidades scope
- **THEN** spec records folder pattern, formats per user, and defers advanced skill automations post-MVP

### Requirement: Obsidian optional path is defined

The product SHALL document optional Obsidian use (primarily Ricardo): mirror `Alba/` tree, local path ingest, Habilidades `.md` allowed; no Obsidian Sync requirement; Gisele/Casa not required to use Obsidian (D-044).

#### Scenario: Obsidian optional documented

- **WHEN** grilling completes Obsidian rules
- **THEN** optional vault paths and alignment with Drive `Alba/` namespace are recorded

### Requirement: Meet transcript placement is defined

The product SHALL document **manual** placement of Meet transcript Docs into the Gisele session tree; Alba poll + TTL only at MVP (D-045).

#### Scenario: Meet manual placement

- **WHEN** grilling completes Meet workflow
- **THEN** example path and deferred auto-routing are documented

