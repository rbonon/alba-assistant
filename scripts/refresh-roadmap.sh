#!/usr/bin/env zsh
# Regenerate ROADMAP.md, board-hierarchy.md, and portal HTML mirrors.
# REST-ONLY — never touches the GraphQL `gh project` API. Hard-fails, no retries.
set -euo pipefail
ROOT="$(git -C "$(dirname "$0")/.." rev-parse --show-toplevel)"
exec python3 "$ROOT/scripts/gen-docs.py"
