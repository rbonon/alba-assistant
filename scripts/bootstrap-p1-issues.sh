#!/usr/bin/env zsh
# Create P1 leaf issues (REST only — board fields when GraphQL available).
set -euo pipefail
OWNER="rbonon"
REPO="alba-assistant"

create_issue() {
  local title="$1" body="$2" type_hint="${3:-Feature}"
  gh api "repos/$OWNER/$REPO/issues" -f title="$title" -f body="$body" \
    --jq '.number' 2>&1 | tail -1
}

P1_ISSUES=(
  "[Grill] P1 — Users, workspaces & personas|## What
Grilling session: MVP users, workspace model, personas (Alba Dev / Texto / Casa).

## Open questions
- Q-001: Ricardo only vs Ricardo + Gisele for MVP go-live

## Phase
P1

## Parent epic
#2

## Acceptance criteria
- [ ] Grilling complete; answers in issue comments
- [ ] Decisions recorded in DECISIONS.md / open-questions.md"

  "[Grill] P1 — Canonical sources vs RAG boundaries|## What
Grilling: what lives in Obsidian vs Git vs Calendar/Tasks/Drive vs RAG index.

## Phase
P1 · Epic #2

## Acceptance criteria
- [ ] Boundaries documented for spec input"

  "[Grill] P1 — Privacy, LGPD & sensitive content|## What
Grilling: Gisele workspace privacy, clinical content exclusion, LGPD posture.

## Phase
P1 · Epic #2

## Acceptance criteria
- [ ] Privacy rules documented for spec"

  "[Grill] P1 — MVP scope vs post-MVP|## What
Grilling: draw MVP line (P6–P7) vs P8+ integrations.

## Phase
P1 · Epic #2

## Acceptance criteria
- [ ] MVP boundary list agreed"

  "[Grill] P1 — Success metrics per persona|## What
Grilling: measurable success for Ricardo MVP; Gisele/Casa deferred metrics.

## Phase
P1 · Epic #2

## Acceptance criteria
- [ ] Metrics documented"

  "[Grill] P1 — Obsidian requirements|## What
Grilling: vault model, folders, templates, inbox/drafts workflow.

## Phase
P1 · Epic #2

## Acceptance criteria
- [ ] Obsidian requirements captured for spec"

  "[Grill] P1 — Git memory requirements|## What
Grilling: repo allowlist, indexed paths, exclusion rules, secret handling.

## Phase
P1 · Epic #2

## Acceptance criteria
- [ ] Git indexing requirements captured"

  "[Grill] P1 — MCP client requirements|## What
Grilling: Cursor/Claude first; tools, auth, workspace enforcement at client boundary.

## Phase
P1 · Epic #2

## Acceptance criteria
- [ ] MCP requirements captured"

  "[Grill] P1 — Google Calendar scope|## What
Grilling: read-only meeting context; post-MVP P10 — spec requirements only.

## Open questions
- Q-009

## Phase
P1 · Epic #2"

  "[Grill] P1 — Tasks integration scope|## What
Grilling: Google Tasks vs Todoist; boundary vs Obsidian checklists. Q-010.

## Phase
P1 · Epic #2"

  "[Grill] P1 — Google Drive index scope|## What
Grilling: metadata vs full-text; privacy limits. Post-MVP P12 — spec input.

## Phase
P1 · Epic #2"

  "[Grill] P1 — Voice interfaces scope|## What
Grilling: Android capture vs Alexa short commands vs alternatives. Q-011.

## Phase
P1 · Epic #2"

  "Write docs/spec/requirements.md|## What
Produce requirements.md from completed P1 grilling sessions.

## Phase
P1 · Epic #2

## Acceptance criteria
- [ ] requirements.md complete
- [ ] Linked from portal"

  "Write docs/spec/user-stories.md|## What
User stories with acceptance criteria per persona/workspace.

## Phase
P1 · Epic #2

## Acceptance criteria
- [ ] user-stories.md complete"

  "Write docs/spec/non-goals.md|## What
Explicit non-goals for MVP and later phases.

## Phase
P1 · Epic #2

## Acceptance criteria
- [ ] non-goals.md complete"

  "OpenSpec proposal — spec v1 (documentation only)|## What
OpenSpec change for P1 spec artifacts only — no implementation tasks.

## Phase
P1 · Epic #2

## Workflow
- [ ] rbo-create-change
- [ ] propose → approval gate
- [ ] apply (docs only)

## Acceptance criteria
- [ ] openspec/changes/<name>/ with proposal + tasks (docs)"

  "[Gate] P1 — Approve spec v1|## What
Human approval gate — spec v1 frozen before P2 architecture grilling.

## Phase
P1 · Epic #2

## Acceptance criteria
- [ ] All P1 grill + spec issues Done
- [ ] Ricardo confirms → begin P2"
)

echo "Creating P1 leaf issues..."
for entry in "${P1_ISSUES[@]}"; do
  title="${entry%%|*}"
  body="${entry#*|}"
  num="$(create_issue "$title" "$body")"
  echo "#$num $title"
done
