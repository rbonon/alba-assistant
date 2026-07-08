#!/usr/bin/env python3
"""Regenerate docs/planning/board-hierarchy.md from GitHub Project."""
import json
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

OWNER = "rbonon"
REPO = "alba-assistant"
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs/planning/board-hierarchy.md"


def gh(*args: str) -> dict:
    return json.loads(subprocess.check_output(["gh", *args]))


def main() -> int:
    projects = gh("project", "list", "--owner", OWNER, "--format", "json")
    project_num = next(
        (p["number"] for p in projects["projects"] if p["title"] == REPO),
        None,
    )
    if not project_num:
        print(f"No project board titled {REPO}", file=sys.stderr)
        return 1

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


if __name__ == "__main__":
    raise SystemExit(main())
