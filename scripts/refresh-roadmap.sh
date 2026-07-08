#!/usr/bin/env zsh
# Regenerate ROADMAP.md from GitHub Project board.
set -euo pipefail

ROOT="$(git -C "$(dirname "$0")/.." rev-parse --show-toplevel)"
cd "$ROOT"

OWNER="${GITHUB_OWNER:-rbonon}"
REPO="$(basename "$ROOT")"
PROJECT_NUM="${ALBA_PROJECT_NUM:-}"

if [[ -z "$PROJECT_NUM" ]]; then
  PROJECT_NUM="$(gh project list --owner "$OWNER" --format json \
    | jq -r --arg t "$REPO" '.projects[] | select(.title == $t) | .number' | head -1)"
fi

if [[ -z "$PROJECT_NUM" || "$PROJECT_NUM" == "null" ]]; then
  echo "No project board titled '$REPO' for owner $OWNER" >&2
  exit 1
fi

gh project item-list "$PROJECT_NUM" --owner "$OWNER" --limit 500 --format json \
  | jq -r '
      ["P0","P1","P2","P3","P4","P5","P6","P7","P8","P9","P10","P11","P12","P13","P14","No Phase"] as $porder
    | ["Todo","In Progress","Done"] as $sorder
    | .items
    | map(.phase //= "No Phase")
    | group_by(.phase)
    | sort_by(.[0].phase as $p | ($porder | index($p)) // 99)[]
    | "# \(.[0].phase)\n\n" +
      ( [ group_by(.status)
          | sort_by(.[0].status as $s | ($sorder | index($s)) // 99)[]
          | "## \(.[0].status // "No Status")\n" +
            (map("- [#\(.content.number)](\(.content.url)) \(.content.title)") | join("\n"))
        ] | join("\n\n") ) + "\n"' \
  > ROADMAP.md

echo "Wrote ROADMAP.md from board $REPO (#$PROJECT_NUM)"
