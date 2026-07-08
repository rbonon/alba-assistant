#!/usr/bin/env python3
"""Generate ROADMAP.md and docs/planning/board-hierarchy.md.

REST-ONLY. Uses `gh api repos/<owner>/<repo>/issues` (REST budget) — never the
GraphQL `gh project` API. This avoids the point-heavy ProjectsV2 GraphQL calls
that previously exhausted the GraphQL budget.

Phase is parsed from the issue title/body convention (`P0`..`P14`), not from the
Project board (board field values are GraphQL-only). Board membership/status is
NOT read here; issue open/closed state is used instead.

Safe by design: single paginated REST call, no loops, hard-fail on error.
"""
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


def write_roadmap(issues: list[dict]) -> None:
    by_phase: dict[str, dict[str, list]] = defaultdict(lambda: {"open": [], "closed": []})
    for i in issues:
        by_phase[phase_of(i)]["open" if i["state"] == "open" else "closed"].append(i)

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
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
