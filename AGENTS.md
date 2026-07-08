# alba-assistant — AI agent context

This file layers **global behavioral rules** (below) with **repo-specific** project
context (at the end). Global rules also live in Cursor → Settings → Rules → User
Rules and in dotfiles (`~/.claude/CLAUDE.md`, `~/.codex/AGENTS.md`).

**Precedence:** repo phase gates and explicit user instructions override global
standing permissions where they conflict (e.g. no commits to `main` for leaf work
until `rbo-close-change`; commit only when the user asks during planning sessions).

---

# Global Behavioural Rules (machine-global, tool-agnostic)

Applies to every AI coding agent (Claude Code, Cursor, Codex). Per-repo project
context lives in each repo's own `CLAUDE.md` / `AGENTS.md`.

Install: symlinked to `~/.claude/CLAUDE.md` and `~/.codex/AGENTS.md` by the dotfiles
`setup_ai` bootstrap. Cursor has no global rules file — paste this section into
Cursor → Settings → Rules → User Rules once per machine.

## Coding Behavior

> These guidelines bias toward caution over speed. For trivial tasks, use judgment.

### 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:

- State assumptions explicitly. If uncertain, say so upfront — don't silently pick an interpretation.
- If multiple interpretations exist, present them briefly, then proceed with the most likely one unless they're equivalent in effort.
- If a simpler approach exists, say so and push back.
- If something is genuinely ambiguous and the wrong choice has large consequences, stop and ask one focused question.

### 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

Self-check: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

### 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

- Don't improve adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it — don't delete it.
- Remove imports/variables/functions that YOUR changes made unused. Leave pre-existing dead code alone unless asked.

Every changed line should trace directly to the request.

### 4. Goal-Driven Execution

**Define success criteria. Loop until verified.**

For multi-step tasks, state a brief plan before starting:

    1. [Step] → verify: [check]
    2. [Step] → verify: [check]

Transform tasks into verifiable goals:

- "Add validation" → write tests for invalid inputs, then make them pass
- "Fix the bug" → write a test that reproduces it, then make it pass
- "Refactor X" → ensure tests pass before and after

Loop independently on strong criteria. Weak criteria ("make it work") are a signal to define success before starting.

## Information Discipline

### 5. Work on Facts, Not Assumptions

- Act on what is known. Do not suppose, guess, or invent information.
- If a decision point requires information you don't have, stop and ask — one focused question, not a list.
- Use judgment: small details don't need confirmation; architectural choices, irreversible actions, and ambiguous requirements do.

### 6. Read Before Editing

- Before modifying a file you have not yet read in this session, read it first.
- Do not make edits based on assumptions about a file's contents.

### 7. Prefer Existing Files Over New Ones

- Before creating a file, check if an existing file is the right place for the content.
- Create new files only when no existing file is a reasonable fit.

### 8. Don't Confuse Correlation with Cause

- Never state a cause confidently based on a structural difference alone (e.g. "missing file X is why Y fails")
- If you don't know the root cause, say so explicitly: "I don't know exactly why — here's what I observe"
- Only claim causation when you can trace the mechanism directly (code path, config key, documented behavior)
- Prefer "try X to rule it out" over "X is the reason"

### 9. Visual Output — Ask the User, Don't Debug Preview

When a change affects the UI and needs human visual judgment (does it look right? is the effect visible?), ask the user to check their browser directly instead of spending time debugging preview tool issues (viewport collapse, screenshot resolution, zoom artifacts). The user can see the result in seconds; preview debugging can waste minutes.

## Standing Permissions

The following are pre-approved. Do not ask for confirmation before performing them:

### File Operations

- Read, create, edit, delete any file in this repo/directory
- Overwrite existing files, create new directories

### Code Execution

- Run bash commands, scripts, tests, linters, formatters
- Install packages via npm, pip, cargo, brew, etc.
- Execute build and deploy scripts

### Git

- Stage, commit, push, amend, branch, merge, delete branches
- Write commit messages using conventional commits — no user prompt needed
- When `/rbo-sync` is invoked without a commit message, generate one from the diff — do not ask
- Push immediately after commit unless told otherwise

### Network

- Fetch URLs, download dependencies

### Browser / UI Automation

- Navigate, click, fill forms, take screenshots
- Accept cookie/consent banners

- Skip confirmation prompts. If uncertain about intent, state your assumption and proceed.
- Only stop to ask if the action is irreversible AND outside the scope of this repo.

## GitHub Issues & Project Board

Every repo is treated as a product with its **own GitHub Project board** — the
project whose **title equals the repo name**, under the repo owner. All board
coordinates are discovered live via the authenticated GitHub CLI (`gh`, with the
`project` scope); there is **no static per-repo config**:

- `owner` / `repo` from `git remote`
- project number + node id from `gh project list --owner <owner> --format json` (match `title` == repo)
- field + option ids from `gh project field-list <n> --owner <owner> --format json`

Board template:

- **Core (every board):** `Status` (Todo / In Progress / Done), `Type` (Feature / Bug / Chore), `Repository`.
- **Optional product extensions:** `Module`, `Phase` — set only if the board already has them; never invented.

Rules:

- Every issue lives on its repo's board. If the board doesn't exist yet it is
  created on first use by `rbo-create-issue` (core template), announced when done.
- Issue Status moves `Todo` → `In Progress` (at `rbo-create-change`) → `Done` (at merge,
  by `rbo-close-change`).
- The mechanics live in the `rbo-create-issue` / `rbo-create-change` / `rbo-close-change`
  skills — don't hand-roll the `gh project` calls here.

### Roadmap (generated mirror)

`ROADMAP.md` is a **generated, read-only mirror** of the GitHub Project — never
hand-edit it; changes go on the board (issues), then regenerate. The board is the
source of truth; `ROADMAP.md` is just a grep-able local copy. Regenerate via
`scripts/refresh-roadmap.sh` when an issue is created, closed, or a change archived.

## Change Workflow

### Canonical lifecycle (the linkage)

Every unit of work flows through one chain. GitHub Projects is the source of
truth for *what* to do (the roadmap); OpenSpec is the source of truth for *the
spec*; the branch and commit messages tie both to the code. Nothing tracks
commits or issues for you — these links do:

```
idea/need → GitHub issue (roadmap) → branch → [explore] → propose (creates change) → apply → human validation → archive → merge → push → close issue (board: Done)
```

- **Issue first; the issue is the roadmap.** Every idea or need starts as a GitHub issue on the project board.
- **The OpenSpec change is created at propose time**, not when the issue is filed.
- **branch = change name.** The branch MUST be `feat/<change-name>` (kebab name derived from the issue), matching the OpenSpec change directory exactly.
- **issue ↔ change.** At propose time the issue is updated to point at `openspec/changes/<change-name>/`. The change → issue backlink is sealed at merge via `Closes #<issue>`.
- **Human validation before archive.** After apply, the user reviews; the chain pauses for explicit go-ahead.
- **Archive on the branch, before merge**, so the archive commit lands in the same merge as the work. Archive is never autonomous (see Archive rule).
- **Merge then push.** Direct merge to `main`, no PR.
- **Close the loop:** `Closes #<issue>` closes the issue on push; set the board item to Done and regenerate `ROADMAP.md`.
- **Skills drive the whole chain.** `rbo-create-issue` → `rbo-create-change` (stops at approval gate) → apply → `rbo-close-change` on explicit go-ahead.

### Trigger: new idea or need ("create an issue …", "log a feature/bug")

Run **`rbo-create-issue`**. Proposes a title (waits for OK), creates the issue on the board, sets Status/Type, refreshes `ROADMAP.md`. No branch or OpenSpec change yet.

### Trigger: "do the change" / "implement <issue>"

1. **`rbo-create-change`** — pick issue → branch `feat/<change-name>` → In Progress → explore (if needed) → propose → **stop at approval gate**.
2. **Pause** — wait for explicit user approval.
3. **Apply** — `openspec-apply-change` on approval.
4. **Human validation** — wait for go-ahead to close out.
5. **`rbo-close-change`** — archive → merge to `main` → push `Closes #N` → board Done → refresh `ROADMAP.md`.

### Skill creation

New skills go to `~/Documents/GitHub/rbonon/ai-skills/skills/<skill-name>/SKILL.md` (flat, MIT license), catalog updated in `ai-skills` README, symlinked via dotfiles `setup_ai`.

### Archive rule

**Never archive autonomously.** Archive only when the user explicitly runs `/opsx:archive` or says "archive". Completing all tasks does NOT trigger archive.

### After any significant fix or improvement (not a full change)

Update `AGENTS.md` Milestone and relevant sections. Do not wait to be asked.

---

# Repo-specific — alba-assistant

## What this repo is

**Alba Context Assistant** — a personal/family context platform that indexes Obsidian notes and Git repositories into a regenerable RAG layer, exposed via HTTP API and MCP. Canonical human memory lives in Obsidian; technical truth in Git; RAG is never primary storage.

This repo is the **runtime/engine** repo. Related: `rbonon/alba-docs`. Planned migration to an **Alba GitHub org**.

## Structure

```
alba-assistant/
├── docs/
│   ├── index.html              # GitHub Pages portal (English)
│   ├── vision/                 # Vision handoff (input, not final spec)
│   ├── planning/               # Product canon + generated board-hierarchy
│   ├── spec/                   # Requirements (P1)
│   ├── architecture/           # Architecture detail (P2–P3)
│   └── operations/             # Bootstrap, go-live (P4)
├── openspec/                   # OpenSpec (implementation from P6+)
├── scripts/                    # refresh-roadmap, refresh-board-hierarchy
├── AGENTS.md                   # This file
├── DECISIONS.md                # Append-only decision log
├── STATUS.md                   # Session compass
└── ROADMAP.md                  # Generated from GitHub Project board
```

## Key files

- `docs/vision/alba-context-assistant-handoff.md` — vision input (Portuguese)
- `docs/planning/README.md` — planning index
- `docs/planning/phases.md` — P0–P14 sequencing
- `docs/planning/open-questions.md` — grilling backlog
- `docs/planning/workflow.md` — Model A issue/change linkage
- `DECISIONS.md` — locked decisions (read before significant work)

## Tech stack

**TBD — lock in P2 grilling.** Proposed: TypeScript/Node.js, SQLite, LanceDB or Chroma, Fastify, MCP server.

## Architecture invariants

See `docs/planning/architecture.md` and `DECISIONS.md`:

- Obsidian = human memory; Git = technical memory
- RAG = regenerable index
- Workspace-filtered retrieval (`ricardo`, `gisele`, `casa`, `compartilhado`)
- AI writes only to `Inbox/AI Drafts` until human promotes
- Staging before production for every slice
- Never index secrets, `.env`, `node_modules`, clinical/sensitive content

## Alba product rules (override / extend global)

- **No runtime implementation** until `[Gate] P5` (roadmap approved)
- **Model A:** every **leaf** issue → `rbo-create-change` → branch + OpenSpec; **epics** and **gates** do not
- **No direct commits to `main`** for leaf deliverables (P0 #7–#12 retro-closed as one-time exception)
- **`rbo-grilling`** for spec/arch — one question at a time
- Never hand-edit `ROADMAP.md` or `docs/planning/board-hierarchy.md` — use `scripts/refresh-*.sh`
- Append to `DECISIONS.md` only — never overwrite
- GitHub Project board title = **`alba-assistant`** (#5)
- Portal: https://rbonon.github.io/alba-assistant/ (English)

## Milestone

**Current:** P1 — Requirements & spec v1 (epic #2; leaves #14–#30).

**Next:** `rbo-create-change` on **#14** → grilling Q-001.

**Handoff:** [`docs/planning/session-handoff.md`](docs/planning/session-handoff.md)

## Working with this repo

- Read `DECISIONS.md` and `STATUS.md` before significant work
- Update planning docs and portal as phases complete
- Run refresh scripts after board changes
- Step-by-step with the user; no rushing phases
