#!/usr/bin/env python3
"""Generate ROADMAP.md, board-hierarchy.md, and docs/planning/roadmap.html.

REST-ONLY. Uses `gh api repos/<owner>/<repo>/issues` (REST budget) — never the
GraphQL `gh project` API. This avoids the point-heavy ProjectsV2 GraphQL calls
that previously exhausted the GraphQL budget.

Phase is parsed from the issue title/body convention (`P0`..`P14`), not from the
Project board (board field values are GraphQL-only). Board membership/status is
NOT read here; issue open/closed state is used instead.

`roadmap.html` is published under `/docs` for GitHub Pages embeds (repo-root
ROADMAP.md is not deployed).

Safe by design: single paginated REST call, no loops, hard-fail on error.
"""
import html
import json
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

OWNER = "rbonon"
REPO = "alba-assistant"
ROOT = Path(__file__).resolve().parents[1]
ROADMAP = ROOT / "ROADMAP.md"
HIERARCHY = ROOT / "docs/planning/board-hierarchy.md"
ROADMAP_HTML = ROOT / "docs/planning/roadmap.html"
PHASE_ORDER = [f"P{i}" for i in range(15)] + ["No Phase"]


def fetch_issues() -> list[dict]:
    raw = subprocess.check_output(
        ["gh", "api", f"repos/{OWNER}/{REPO}/issues",
         "--paginate", "-X", "GET", "-f", "state=all", "-f", "per_page=100"],
    )
    return [i for i in json.loads(raw) if "pull_request" not in i]


def phase_of(issue: dict) -> str:
    m = re.search(r"\bP\d+\b", issue["title"])
    if m:
        return m.group(0)
    body = issue.get("body") or ""
    m = re.search(r"\bP\d+\b", body[:400])
    return m.group(0) if m else "No Phase"


def kind(issue: dict) -> str:
    t = issue["title"]
    if "[Epic]" in t:
        return "epic"
    if "[Gate]" in t:
        return "gate"
    return "leaf"


def issues_by_phase(issues: list[dict]) -> dict[str, dict[str, list]]:
    by_phase: dict[str, dict[str, list]] = defaultdict(lambda: {"open": [], "closed": []})
    for i in issues:
        by_phase[phase_of(i)]["open" if i["state"] == "open" else "closed"].append(i)
    return by_phase


def write_roadmap(issues: list[dict]) -> None:
    by_phase = issues_by_phase(issues)

    lines = [
        "# Alba Context Assistant — ROADMAP",
        "",
        "> Generated (REST-only) mirror of GitHub issues. Do not hand-edit.",
        "> Regenerate: `./scripts/refresh-roadmap.sh`",
        "",
    ]
    for ph in PHASE_ORDER:
        d = by_phase.get(ph)
        if not d or (not d["open"] and not d["closed"]):
            continue
        lines.append(f"# {ph}\n")
        for state in ("open", "closed"):
            if not d[state]:
                continue
            lines.append(f"## {state.capitalize()}\n")
            for i in sorted(d[state], key=lambda x: x["number"]):
                lines.append(f"- [#{i['number']}]({i['html_url']}) {i['title']}")
            lines.append("")
    ROADMAP.write_text("\n".join(lines) + "\n")
    print(f"Wrote {ROADMAP}")


def write_hierarchy(issues: list[dict]) -> None:
    by_num = {i["number"]: i for i in issues}
    epics_by_phase: dict[str, list[int]] = defaultdict(list)
    leaves_by_phase: dict[str, list[int]] = defaultdict(list)
    for n, i in by_num.items():
        ph = phase_of(i)
        (epics_by_phase if kind(i) == "epic" else leaves_by_phase)[ph].append(n)

    n_epics = sum(len(v) for v in epics_by_phase.values())
    lines = [
        "# Alba Context Assistant — Board hierarchy",
        "",
        f"> Owner: **{OWNER}** · Repo: **{REPO}** · Project: **{REPO}** (#5)",
        "> **Generated (REST-only)** — do not edit. Regenerate: `./scripts/refresh-board-hierarchy.sh`",
        "",
        f"> {len(issues)} issues · {n_epics} epics · phase from title/body convention",
        "",
    ]
    for ph in PHASE_ORDER:
        if not epics_by_phase.get(ph) and not leaves_by_phase.get(ph):
            continue
        lines.append(f"## {ph}")
        lines.append("")
        for en in sorted(epics_by_phase.get(ph, [])):
            e = by_num[en]
            state = "✅" if e["state"] == "closed" else "🟡 open"
            lines.append(f"### [{en}]({e['html_url']}) — {e['title']} · {state}")
            lines.append("")
        leaves = sorted(leaves_by_phase.get(ph, []))
        if leaves:
            lines.append("| # | Title | State |")
            lines.append("|---|-------|-------|")
            for n in leaves:
                i = by_num[n]
                lines.append(f"| [{n}]({i['html_url']}) | {i['title']} | {i['state']} |")
            lines.append("")
    HIERARCHY.write_text("\n".join(lines) + "\n")
    print(f"Wrote {HIERARCHY}")


def write_roadmap_html(issues: list[dict]) -> None:
    """Portal embed for progress-report.html (published under /docs on GitHub Pages)."""
    by_phase = issues_by_phase(issues)
    sections: list[str] = []
    for ph in PHASE_ORDER:
        d = by_phase.get(ph)
        if not d or (not d["open"] and not d["closed"]):
            continue
        blocks: list[str] = []
        for state in ("open", "closed"):
            items = sorted(d[state], key=lambda x: x["number"])
            if not items:
                continue
            lis = []
            for i in items:
                cls = ' class="closed"' if state == "closed" else ""
                title = html.escape(i["title"])
                lis.append(
                    f'<li{cls}><a href="{html.escape(i["html_url"])}" target="_blank" rel="noopener">'
                    f'#{i["number"]}</a> {title}</li>'
                )
            blocks.append(
                f'<h3>{state.capitalize()}</h3><ul>{"".join(lis)}</ul>'
            )
        sections.append(f'<section class="phase"><h2>{html.escape(ph)}</h2>{"".join(blocks)}</section>')

    body = "\n    ".join(sections) if sections else "<p>No issues.</p>"
    ROADMAP_HTML.write_text(
        f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>ROADMAP mirror</title>
  <link rel="stylesheet" href="../assets/portal.css" />
  <style>
    body {{ padding: 1rem 1.25rem 1.5rem; font-size: 0.88rem; background: #fff; }}
    .phase {{ margin-bottom: 1.25rem; }}
    .phase h2 {{ font-size: 1rem; color: var(--navy); margin: 0 0 0.35rem; border-bottom: 1px solid var(--border); padding-bottom: 0.25rem; }}
    .phase h3 {{ font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.05em; color: var(--muted); margin: 0.65rem 0 0.3rem; font-weight: 600; }}
    ul {{ margin: 0; padding-left: 1.1rem; list-style: disc; }}
    li {{ margin: 0.2rem 0; line-height: 1.45; }}
    li.closed {{ color: var(--muted); }}
    li a {{ font-weight: 600; }}
  </style>
</head>
<body>
  {body}
</body>
</html>
""",
        encoding="utf-8",
    )
    print(f"Wrote {ROADMAP_HTML}")


def main() -> int:
    try:
        issues = fetch_issues()
    except subprocess.CalledProcessError as exc:
        print(f"REST fetch failed: {exc}", file=sys.stderr)
        return 1
    if not issues:
        print("No issues returned; refusing to overwrite docs.", file=sys.stderr)
        return 1
    write_roadmap(issues)
    write_hierarchy(issues)
    write_roadmap_html(issues)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
