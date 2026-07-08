## ADDED Requirements

### Requirement: Canonical sources are defined per domain

The product SHALL document which system is the system of record for human memory, technical memory, scheduling, tasks, and files — separate from the RAG index.

#### Scenario: Source matrix locked

- **WHEN** grilling on issue **#15** completes
- **THEN** planning canon lists canonical source per domain (Obsidian, Git, Calendar, Tasks, Drive, etc.)

### Requirement: RAG index is never primary storage

The RAG index SHALL be a regenerable derivative of canonical sources only; loss of the index MUST NOT lose canonical data.

#### Scenario: Rebuild policy stated

- **WHEN** grilling resolves RAG role
- **THEN** `DECISIONS.md` states index is rebuildable from sources and never sole storage

### Requirement: MVP indexed sources are explicit

The product SHALL list which canonical sources are indexed in MVP vs deferred to post-MVP integrations.

#### Scenario: MVP source list

- **WHEN** grilling completes MVP scope for sources
- **THEN** `features.md` or spec input docs state in-scope sources for MVP read-only memory

### Requirement: Operational systems boundary is preserved

Calendar and Tasks SHALL remain systems of record; Obsidian holds meeting/task *context* only — not duplicate scheduling truth.

#### Scenario: Calendar/Tasks boundary reaffirmed or refined

- **WHEN** grilling covers Calendar/Tasks/Drive
- **THEN** decision records what is indexed vs referenced vs out of scope for MVP
