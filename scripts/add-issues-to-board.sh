#!/usr/bin/env zsh
# Add issues to Project board #5, set Phase + Status. Idempotent-ish.
# Usage: ./scripts/add-issues-to-board.sh <phase> <issue-number...>
#   e.g. ./scripts/add-issues-to-board.sh P1 14 15 16 ... 30
set -euo pipefail

OWNER="rbonon"
REPO="alba-assistant"
PROJECT_NUM="${ALBA_PROJECT_NUM:-5}"

PHASE_VALUE="$1"; shift
ISSUES=("$@")

PROJECT_ID="$(gh project list --owner "$OWNER" --format json \
  | jq -r --arg t "$REPO" '.projects[] | select(.title == $t) | .id')"

FIELDS="$(gh project field-list "$PROJECT_NUM" --owner "$OWNER" --format json)"
STATUS_FIELD="$(echo "$FIELDS" | jq -r '.fields[] | select(.name=="Status") | .id')"
PHASE_FIELD="$(echo "$FIELDS"  | jq -r '.fields[] | select(.name=="Phase")  | .id')"
TODO_ID="$(echo "$FIELDS"   | jq -r '.fields[] | select(.name=="Status") | .options[] | select(.name=="Todo") | .id')"
PHASE_ID="$(echo "$FIELDS"  | jq -r --arg p "$PHASE_VALUE" '.fields[] | select(.name=="Phase") | .options[] | select(.name==$p) | .id')"

for n in "${ISSUES[@]}"; do
  url="https://github.com/$OWNER/$REPO/issues/$n"
  item_id="$(gh project item-add "$PROJECT_NUM" --owner "$OWNER" --url "$url" --format json | jq -r '.id')"
  gh project item-edit --id "$item_id" --project-id "$PROJECT_ID" \
    --field-id "$STATUS_FIELD" --single-select-option-id "$TODO_ID"
  gh project item-edit --id "$item_id" --project-id "$PROJECT_ID" \
    --field-id "$PHASE_FIELD" --single-select-option-id "$PHASE_ID"
  echo "added #$n → $PROJECT_NUM (Phase=$PHASE_VALUE, Status=Todo)"
done
