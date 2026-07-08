#!/usr/bin/env zsh
set -euo pipefail
ROOT="$(git -C "$(dirname "$0")/.." rev-parse --show-toplevel)"
python3 "$ROOT/scripts/refresh-board-hierarchy.py"
"$ROOT/scripts/refresh-roadmap.sh"
