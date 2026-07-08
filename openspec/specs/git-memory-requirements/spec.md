# git-memory-requirements Specification

## Purpose
TBD - created by archiving change grill-p1-git-memory-requirements. Update Purpose after archive.
## Requirements
### Requirement: Git repo allowlist is explicit per account

The product SHALL index Git repositories only when listed on an explicit per-GitHub-account allowlist; auto-discovery of all repos MUST NOT be the default.

#### Scenario: Allowlist locked at grilling

- **WHEN** grilling on issue **#20** completes
- **THEN** `DECISIONS.md` documents allowlist rules for `rbonon`, `fortegb`, and `akamlibehsafe` including staging subset vs production full list

### Requirement: Indexed paths within repos are defined

The product SHALL document default path include/exclude patterns for Git indexing and whether per-repo overrides are allowed.

#### Scenario: Path rules captured

- **WHEN** grilling resolves indexed paths
- **THEN** planning canon states default globs (e.g. docs, README, agent context, `ideas/`, `habilidades/`, source) and exclusion interaction with D-023

### Requirement: Branch and ref scope is explicit

The product SHALL document which Git refs are indexed (e.g. default branch only vs all branches vs tags).

#### Scenario: Ref scope locked

- **WHEN** grilling completes branch scope
- **THEN** `DECISIONS.md` states MVP ref policy for Git ingest

### Requirement: Git-specific exclusions extend the never-index list

The product SHALL extend D-023 with Git-specific path and content exclusions (build artifacts, vendored deps, large binaries, tool caches, etc.).

#### Scenario: Git exclusions documented

- **WHEN** grilling completes exclusion rules
- **THEN** `DECISIONS.md` lists Git-specific never-index patterns in addition to D-023

### Requirement: Secret handling for Git is defined

The product SHALL document how secrets in working tree and Git history are detected, blocked from indexing, and audited.

#### Scenario: Secret policy locked

- **WHEN** grilling completes secret handling
- **THEN** `DECISIONS.md` states rules for `.env*`, credential files, API keys, and whether historical commits are scanned or only HEAD

### Requirement: Git canonical folders for ideas and skills are defined

The product SHALL amend D-021/D-022 to state when `ideas/` and `habilidades/` in Git repos are canonical human/technical memory vs Obsidian/Drive.

#### Scenario: ideas and habilidades paths locked

- **WHEN** grilling completes D-021/D-022 amendments
- **THEN** `DECISIONS.md` records canonical location rules for idea docs and Habilidades `.md` in Git

