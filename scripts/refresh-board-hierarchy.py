#!/usr/bin/env python3
"""Regenerate docs/planning/board-hierarchy.md from GitHub Project."""
import json
import os
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

OWNER = "rbonon"
REPO = "alba-assistant"
DEFAULT_PROJECT_NUM = "5"
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs/planning/board-hierarchy.md"


def gh(*args: str) -> dict:
    return json.loads(subprocess.check_output(["gh", *args]))


def main() -> int:
    project_num = os.environ.get("ALBA_PROJECT_NUM", DEFAULT_PROJECT_NUM)

    try:
        return write_from_board(project_num)
    except subprocess.CalledProcessError as exc:
        print(f"GraphQL board fetch failed ({exc}); falling back to REST issues", file=sys.stderr)
        return write_from_rest_issues()


def write_from_board(project_num: str) -> int:
    board = gh(
        "project", "item-list", str(project_num),
        "--owner", OWNER, "--limit", "500", "--format", "json",
    )
    items_by_num: dict[int, dict] = {}
    for it in board.get("items", []):
        content = it.get("content") or {}
        num = content.get("number")
        if not num:
            continue
        items_by_num[num] = {
            "title": it.get("title") or content.get("title", ""),
            "url": content.get("url", f"https://github.com/{OWNER}/{REPO}/issues/{num}"),
            "phase": it.get("phase") or "—",
            "status": it.get("status") or "—",
        }

    issues = gh(
        "issue", "list", "--repo", f"{OWNER}/{REPO}",
        "--state", "all", "--limit", "500", "--json", "number,title,state",
    )
    for issue in issues:
        num = issue["number"]
        if num in items_by_num:
            items_by_num[num]["state"] = issue["state"]

    epics = sorted(n for n, m in items_by_num.items() if "[Epic]" in m.get("title", ""))
    by_phase: dict[str, list[int]] = defaultdict(list)
    for num in epics:
        by_phase[items_by_num[num]["phase"]].append(num)

    phase_order = [f"P{i}" for i in range(15)] + ["—"]
    lines = [
        "# Alba Context Assistant — Board hierarchy",
        "",
        f"> Owner: **{OWNER}** · Repo: **{REPO}** · Project: **{REPO}** (#{project_num})",
        "> **Generated** — do not edit. Regenerate: `scripts/refresh-board-hierarchy.sh`",
        "",
        f"> {len(items_by_num)} items on board · {len(epics)} epics",
        "",
    ]

    for phase in phase_order:
        epic_nums = sorted(by_phase.get(phase, []))
        if not epic_nums:
            continue
        lines.append(f"## {phase}")
        lines.append("")
        for num in epic_nums:
            e = items_by_num[num]
            lines.extend([
                f"### [{num}]({e['url']}) — {e['title']}",
                "",
                "| Field | Value |",
                "|-------|-------|",
                f"| Phase | `{e['phase']}` |",
                f"| Board status | {e['status']} |",
                f"| GitHub state | {e.get('state', '—')} |",
                "",
            ])

    lines.append("## All issues by phase")
    lines.append("")
    for phase in phase_order:
        nums = sorted(
            n for n, m in items_by_num.items()
            if m.get("phase") == phase and n not in epics
        )
        if not nums:
            continue
        lines.append(f"### {phase}")
        lines.append("")
        lines.append("| # | Title | Status |")
        lines.append("|---|-------|--------|")
        for num in nums:
            m = items_by_num[num]
            lines.append(f"| [{num}]({m['url']}) | {m['title']} | {m['status']} |")
        lines.append("")

    OUT.write_text("\n".join(lines) + "\n")
    print(f"Wrote {OUT}")
    return 0


def write_from_rest_issues() -> int:
    """Fallback when GraphQL project API is rate-limited."""
    raw = subprocess.check_output(
        ["gh", "api", f"repos/{OWNER}/{REPO}/issues", "--paginate"],
    )
    issues = json.loads(raw)

    items_by_num: dict[int, dict] = {}
    for issue in issues:
        if "pull_request" in issue:
            continue
        num = issue["number"]
        body = issue.get("body") or ""
        phase = "—"
        for line in body.splitlines():
            if line.strip().startswith("Phase:"):
                phase = line.split(":", 1)[1].strip()
                break
        if "[Epic]" in issue["title"] and "P" in issue["title"]:
            for token in issue["title"].split():
                if token.startswith("P") and token[1:].isdigit():
                    phase = token
                    break
        items_by_num[num] = {
            "title": issue["title"],
            "url": issue["html_url"],
            "phase": phase,
            "status": "—",
            "state": issue["state"].upper(),
        }

    epics = sorted(n for n, m in items_by_num.items() if "[Epic]" in m.get("title", ""))
    by_phase: dict[str, list[int]] = defaultdict(list)
    for num in epics:
        by_phase[items_by_num[num]["phase"]].append(num)

    phase_order = [f"P{i}" for i in range(15)] + ["—"]
    lines = [
        "# Alba Context Assistant — Board hierarchy",
        "",
        f"> Owner: **{OWNER}** · Repo: **{REPO}** · Project: **{REPO}** (#{DEFAULT_PROJECT_NUM})",
        "> **Generated (REST fallback)** — board status omitted while GraphQL rate-limited.",
        "> Regenerate: `ALBA_PROJECT_NUM=5 ./scripts/refresh-board-hierarchy.sh`",
        "",
        f"> {len(items_by_num)} issues · {len(epics)} epics",
        "",
    ]

    for phase in phase_order:
        epic_nums = sorted(by_phase.get(phase, []))
        if not epic_nums:
            continue
        lines.append(f"## {phase}")
        lines.append("")
        for num in epic_nums:
            e = items_by_num[num]
            lines.extend([
                f"### [{num}]({e['url']}) — {e['title']}",
                "",
                f"GitHub state: **{e.get('state', '—')}**",
                "",
            ])

    lines.append("## All issues by phase")
    lines.append("")
    for phase in phase_order:
        nums = sorted(
            n for n, m in items_by_num.items()
            if m.get("phase") == phase and n not in epics
        )
        if not nums:
            continue
        lines.append(f"### {phase}")
        lines.append("")
        for num in nums:
            m = items_by_num[num]
            lines.append(f"- [#{num}]({m['url']}) {m['title']}")
        lines.append("")

    OUT.write_text("\n".join(lines) + "\n")
    print(f"Wrote {OUT} (REST fallback)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
