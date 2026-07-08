# mcp-client-requirements Specification

## Purpose
TBD - created by archiving change grill-p1-mcp-client-requirements. Update Purpose after archive.
## Requirements
### Requirement: MVP MCP client priority is explicit

The product SHALL document which AI clients are supported at MVP and their priority order (IDE MCP vs chat API clients).

#### Scenario: Client priority locked

- **WHEN** grilling on issue **#21** completes
- **THEN** `DECISIONS.md` lists MVP-first clients (e.g. Cursor, Claude Code, ChatGPT/Claude) and any deferred clients

### Requirement: MVP MCP tool catalog is defined

The product SHALL document the read-only MCP tools exposed at MVP and their parameters.

#### Scenario: Tool catalog locked

- **WHEN** grilling resolves MCP tools
- **THEN** planning canon lists MVP tools (e.g. `search_memory`, `get_decisions`, `get_project_context`) and confirms read-only scope

### Requirement: Client-boundary auth requirements are defined

The product SHALL document how authenticated user identity flows from each client type to Alba API/MCP for workspace RBAC (D-016).

#### Scenario: Auth requirements captured

- **WHEN** grilling completes auth at client boundary
- **THEN** `DECISIONS.md` states per-user session requirements; mechanism deferred to P2 (Q-008) with requirements locked here

### Requirement: Workspace enforcement responsibilities are defined

The product SHALL document where workspace filtering is enforced (server-side mandatory; client-provided workspace hints optional).

#### Scenario: Enforcement model locked

- **WHEN** grilling completes workspace enforcement
- **THEN** decision records server as authority for D-016; isolation tests (D-033) apply to MCP paths

### Requirement: Chat UI vs IDE MCP relationship is defined

The product SHALL document how ChatGPT/Claude chat surfaces use Alba (MCP, API, or both) alongside IDE-native MCP, respecting D-021 ephemeral threads.

#### Scenario: Chat vs IDE paths locked

- **WHEN** grilling completes client surfaces
- **THEN** `DECISIONS.md` states chat vs IDE MCP requirements at MVP

### Requirement: Staging vs production client configuration is defined

The product SHALL document how Artur (D-034) and staging clients differ from production Ricardo/Gisele client setup.

#### Scenario: Staging client rules locked

- **WHEN** grilling completes staging vs prod
- **THEN** decision records non-prod stand-in account rules for MCP client testing

