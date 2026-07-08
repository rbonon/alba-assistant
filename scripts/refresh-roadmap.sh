#!/usr/bin/env zsh
# Regenerate ROADMAP.md from GitHub Project board (GraphQL) or REST fallback.
set -euo pipefail

ROOT="$(git -C "$(dirname "$0")/.." rev-parse --show-toplevel)"
cd "$ROOT"

OWNER="${GITHUB_OWNER:-rbonon}"
REPO="$(basename "$ROOT")"
PROJECT_NUM="${ALBA_PROJECT_NUM:-5}"

write_from_board() {
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
}

write_from_rest() {
  python3 - "$OWNER" "$REPO" "$ROOT/ROADMAP.md" <<'PY'
import json, re, subprocess, sys
from collections import defaultdict

owner, repo, out_path = sys.argv[1:4]
raw = subprocess.check_output(["gh", "api", f"repos/{owner}/{repo}/issues", "--paginate"])
issues = [i for i in json.loads(raw) if "pull_request" not in i]

def phase_for(issue):
    body = issue.get("body") or ""
    for line in body.splitlines():
        if line.strip().startswith("Phase:"):
            return line.split(":", 1)[1].strip()
    m = re.search(r"\bP\d+\b", issue["title"])
    return m.group(0) if m else "No Phase"

by_phase = defaultdict(list)
for i in issues:
    by_phase[phase_for(i)].append(i)

order = [f"P{n}" for n in range(15)] + ["No Phase"]
lines = []
for ph in order:
    group = by_phase.get(ph, [])
    if not group:
        continue
    lines.append(f"# {ph}\n")
    lines.append("## Todo\n")
    for i in sorted(group, key=lambda x: x["number"]):
        lines.append(f"- [#{i['number']}]({i['html_url']}) {i['title']}")
    lines.append("")

header = "> REST fallback — board Status omitted while GraphQL rate-limited.\n\n"
Path = __import__("pathlib").Path
Path(out_path).write_text(header + "\n".join(lines) + "\n")
print(f"Wrote {out_path} (REST fallback)")
PY
}

if write_from_board 2>/dev/null; then
  :
else
  echo "GraphQL board fetch failed; using REST fallback" >&2
  write_from_rest
fi
