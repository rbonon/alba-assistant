#!/usr/bin/env zsh
# Regenerate docs/planning/board-hierarchy.md (and ROADMAP.md) from GitHub issues.
# REST-ONLY — never touches the GraphQL `gh project` API. Hard-fails, no retries.
set -euo pipefail
ROOT="$(git -C "$(dirname "$0")/.." rev-parse --show-toplevel)"
exec python3 "$ROOT/scripts/gen-docs.py"
