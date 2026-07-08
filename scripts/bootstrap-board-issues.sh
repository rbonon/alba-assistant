#!/usr/bin/env zsh
# Bootstrap GitHub Project board and P0–P5 issues for alba-assistant.
set -euo pipefail

ROOT="$(git -C "$(dirname "$0")/.." rev-parse --show-toplevel)"
cd "$ROOT"

OWNER="rbonon"
REPO="alba-assistant"
PHASES="P0,P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12,P13,P14"

# --- Board ---
EXISTING="$(gh project list --owner "$OWNER" --format json | jq -r --arg t "$REPO" '.projects[] | select(.title == $t) | .number' | head -1 || true)"

if [[ -n "$EXISTING" ]]; then
  PROJECT_NUM="$EXISTING"
  echo "Board exists: $REPO (#$PROJECT_NUM)"
else
  echo "Creating board $REPO..."
  CREATED="$(gh project create --owner "$OWNER" --title "$REPO" --format json)"
  PROJECT_NUM="$(echo "$CREATED" | jq -r '.number')"
  PROJECT_ID="$(echo "$CREATED" | jq -r '.id')"
  gh project field-create "$PROJECT_NUM" --owner "$OWNER" \
    --name "Type" --data-type SINGLE_SELECT \
    --single-select-options "Feature,Bug,Chore" 2>/dev/null || true
  gh project link "$PROJECT_NUM" --owner "$OWNER" --repo "$OWNER/$REPO" 2>/dev/null || true
  echo "Created board #$PROJECT_NUM"
fi

PROJECT_ID="$(gh project list --owner "$OWNER" --format json | jq -r --arg t "$REPO" '.projects[] | select(.title == $t) | .id')"
PROJECT_NUM="$(gh project list --owner "$OWNER" --format json | jq -r --arg t "$REPO" '.projects[] | select(.title == $t) | .number')"

# Phase field
if ! gh project field-list "$PROJECT_NUM" --owner "$OWNER" --format json | jq -e '.fields[] | select(.name=="Phase")' >/dev/null; then
  gh project field-create "$PROJECT_NUM" --owner "$OWNER" \
    --name "Phase" --data-type SINGLE_SELECT \
    --single-select-options "$PHASES"
  echo "Created Phase field"
fi

FIELDS="$(gh project field-list "$PROJECT_NUM" --owner "$OWNER" --format json)"
STATUS_FIELD="$(echo "$FIELDS" | jq -r '.fields[] | select(.name=="Status") | .id')"
TYPE_FIELD="$(echo "$FIELDS" | jq -r '.fields[] | select(.name=="Type") | .id')"
PHASE_FIELD="$(echo "$FIELDS" | jq -r '.fields[] | select(.name=="Phase") | .id')"
TODO_ID="$(echo "$FIELDS" | jq -r '.fields[] | select(.name=="Status") | .options[] | select(.name=="Todo") | .id')"
FEATURE_ID="$(echo "$FIELDS" | jq -r '.fields[] | select(.name=="Type") | .options[] | select(.name=="Feature") | .id')"
CHORE_ID="$(echo "$FIELDS" | jq -r '.fields[] | select(.name=="Type") | .options[] | select(.name=="Chore") | .id')"

phase_option_id() {
  local phase="$1"
  echo "$FIELDS" | jq -r --arg p "$phase" '.fields[] | select(.name=="Phase") | .options[] | select(.name==$p) | .id'
}

add_issue() {
  local title="$1" body="$2" phase="$3" type_opt="$4"
  local url num item_id phase_id

  url="$(gh issue create --repo "$OWNER/$REPO" --title "$title" --body "$body")"
  num="${url##*/}"
  item_id="$(gh project item-add "$PROJECT_NUM" --owner "$OWNER" --url "$url" --format json | jq -r '.id')"
  phase_id="$(phase_option_id "$phase")"

  gh project item-edit --id "$item_id" --project-id "$PROJECT_ID" \
    --field-id "$STATUS_FIELD" --single-select-option-id "$TODO_ID"
  gh project item-edit --id "$item_id" --project-id "$PROJECT_ID" \
    --field-id "$TYPE_FIELD" --single-select-option-id "$type_opt"
  gh project item-edit --id "$item_id" --project-id "$PROJECT_ID" \
    --field-id "$PHASE_FIELD" --single-select-option-id "$phase_id"

  echo "#$num $title"
}

# Refresh fields after Phase create
FIELDS="$(gh project field-list "$PROJECT_NUM" --owner "$OWNER" --format json)"

# --- Epics P0–P5 ---
for n in 0 1 2 3 4 5; do
  case $n in
    0) title="[Epic] P0 — Product foundation"; desc="Portal, board, vision docs, agent context. Gate: P0 before P1." ;;
    1) title="[Epic] P1 — Requirements & spec v1"; desc="Grilling + requirements, user stories, non-goals. Gate: P1." ;;
    2) title="[Epic] P2 — Architecture v1"; desc="Tech stack, system design, integrations architecture. Gate: P2." ;;
    3) title="[Epic] P3 — Environments & deployment"; desc="Staging vs production parity for all components. Gate: P3." ;;
    4) title="[Epic] P4 — Operations & go-live"; desc="Bootstrap, data feeding, reindex, backup, go-live. Gate: P4." ;;
    5) title="[Epic] P5 — Product roadmap"; desc="MVP + P6+ issue tree. Gate: P5 before implementation." ;;
  esac
  body="## What
$desc

## Epic
Phase: P$n

## Acceptance criteria
- [ ] All phase sub-issues Done
- [ ] [Gate] P$n closed by human approval"
  add_issue "$title" "$body" "P$n" "$FEATURE_ID"
done

# --- P0 features ---
P0_ISSUES=(
  "Bootstrap GitHub Pages portal (English)|docs/index.html, assets, planning HTML stubs, Pages enabled"
  "Normalize vision handoff into docs/vision/|Move handoff; fix alba-assistant naming; docs/vision/README.md"
  "Seed planning canon|README, workflow, features, modules, phases, open-questions, decisions templates"
  "Populate AGENTS.md and CLAUDE.md|Remove template placeholders; link planning docs"
  "Seed DECISIONS.md with validated vision decisions|Append-only; TBD items marked"
  "Add board refresh scripts|refresh-roadmap.sh, refresh-board-hierarchy.sh"
)

for entry in "${P0_ISSUES[@]}"; do
  title="${entry%%|*}"
  scope="${entry##*|}"
  body="## What
$title

## Scope
$scope

## Phase
P0

## Acceptance criteria
- [ ] Deliverable complete
- [ ] Docs/portal updated if applicable"
  add_issue "$title" "$body" "P0" "$FEATURE_ID"
done

add_issue "[Gate] P0 — Product foundation complete" "## What
Human approval gate — P0 complete.

## Acceptance criteria
- [ ] All P0 features Done
- [ ] Portal live on GitHub Pages
- [ ] Board populated
- [ ] Ricardo confirms → begin P1 grilling (Q-001)" "P0" "$CHORE_ID"

echo ""
echo "Board: https://github.com/users/$OWNER/projects/$PROJECT_NUM"
export ALBA_PROJECT_NUM="$PROJECT_NUM"
"$ROOT/scripts/refresh-board-hierarchy.sh"
