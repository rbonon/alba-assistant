## Why

P1 spec needs locked **Git memory requirements**: which repos and paths Ricardo's three GitHub accounts expose to the RAG index, how exclusions and secrets are handled, and how Git canonical folders (`ideas/`, `habilidades/`) relate to prior D-021/D-022. D-020 names the accounts but not repo/path rules. Grilling on **#20** refines D-020–D-023 and D-021/D-022.

## What Changes

- Grilling session on issue **#20 — [Grill] P1 — Git memory requirements**
- Resolve repo allowlist (per-account, staging vs production), indexed path patterns, branch scope, Git-specific exclusions, secret handling, and `ideas/` / `habilidades/` canon (amend D-021/D-022)
- Record decisions in `DECISIONS.md` (D-046+), `open-questions.md`, issue **#20**
- Update `modules.md` / `features.md` Git indexing rows

No runtime code.

## Capabilities

### New Capabilities

- `git-memory-requirements`: Git repo allowlist, indexed paths, branch scope, exclusion rules, secret handling, canonical `ideas/` / `habilidades/` paths (issue #20)

### Modified Capabilities

- _(none — no main specs exist yet)_

## Impact

- **Docs:** `DECISIONS.md`, `docs/planning/open-questions.md`, `modules.md`, input for `#26` requirements
- **Board:** **#20** → In Progress → Done on close
- **Downstream:** informs P6 Git ingest adapter, P2 auth/credentials for multi-account Git, spec leaves **#26–#28**
