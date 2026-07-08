## Why

P1 spec needs locked **MCP client requirements**: which AI clients are MVP-first (Cursor/Claude), which tools Alba exposes, how user identity and workspace RBAC (D-016) are enforced at the client boundary, and how ChatGPT/Claude chat surfaces relate to MCP. D-005 and D-031 name MCP at MVP but not client/tool/auth detail. Grilling on **#21** locks requirements before P2 auth architecture and P7 implementation.

## What Changes

- Grilling session on issue **#21 — [Grill] P1 — MCP client requirements**
- Resolve MVP client priority, MCP tool catalog, auth/session model at client boundary, workspace enforcement, and ChatGPT/Claude vs IDE MCP paths
- Record decisions in `DECISIONS.md` (D-052+), `open-questions.md`, issue **#21**
- Update `features.md` / `modules.md` MCP rows as needed

No runtime code.

## Capabilities

### New Capabilities

- `mcp-client-requirements`: MVP client priority, MCP tools, client-boundary auth, workspace enforcement, chat UI vs IDE MCP (issue #21)

### Modified Capabilities

- _(none — no main spec requirement changes yet)_

## Impact

- **Docs:** `DECISIONS.md`, `docs/planning/open-questions.md`, `features.md`, `modules.md`, input for `#26` requirements
- **Board:** **#21** → In Progress → Done on close
- **Downstream:** informs P2 auth (Q-008), P7 MCP server + client config, spec leaves **#26–#28**
