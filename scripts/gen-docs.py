#!/usr/bin/env python3
"""Generate ROADMAP.md, board-hierarchy.md, portal HTML mirrors, and planning *.html.

REST-ONLY. Uses `gh api repos/<owner>/<repo>/issues` (REST budget) — never the
GraphQL `gh project` API. This avoids the point-heavy ProjectsV2 GraphQL calls
that previously exhausted the GraphQL budget.

Phase is parsed from the issue title/body convention (`P0`..`P14`), not from the
Project board (board field values are GraphQL-only). Board membership/status is
NOT read here; issue open/closed state is used instead.

Portal HTML under `docs/planning/` is published on GitHub Pages (`/docs` root).
Repo-root `ROADMAP.md` is not deployed — use generated `roadmap.html`.

Safe by design: single paginated REST call, no loops, hard-fail on error.
"""
import html
import json
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

from portal_md import md_to_html, portal_page_html

OWNER = "rbonon"
REPO = "alba-assistant"
ROOT = Path(__file__).resolve().parents[1]
PLANNING = ROOT / "docs/planning"
ROADMAP = ROOT / "ROADMAP.md"
HIERARCHY = PLANNING / "board-hierarchy.md"
ROADMAP_HTML = PLANNING / "roadmap.html"
HIERARCHY_HTML = PLANNING / "board-hierarchy.html"
PHASE_ORDER = [f"P{i}" for i in range(15)] + ["No Phase"]

# Markdown canon → portal HTML (features.html is hand-maintained separately)
PORTAL_MD_PAGES: list[tuple[str, str]] = [
    ("open-questions.md", "Open questions"),
    ("decisions.md", "Decisions log"),
    ("workflow.md", "Workflow"),
    ("phases.md", "Phases & epics"),
    ("modules.md", "Modules & tools"),
    ("architecture.md", "Architecture"),
    ("session-handoff.md", "Session handoff"),
    ("product-vision.md", "Product vision"),
    ("README.md", "Planning index"),
]


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


def _issue_row(i: dict) -> str:
    closed = i["state"] == "closed"
    cls = ' class="closed"' if closed else ""
    title = html.escape(i["title"])
    return (
        f"<tr{cls}><td><a href=\"{html.escape(i['html_url'])}\" target=\"_blank\" "
        f'rel="noopener">#{i["number"]}</a></td><td>{title}</td>'
        f'<td>{html.escape(i["state"])}</td></tr>'
    )


def write_board_hierarchy_html(issues: list[dict]) -> None:
    by_num = {i["number"]: i for i in issues}
    epics_by_phase: dict[str, list[int]] = defaultdict(list)
    leaves_by_phase: dict[str, list[int]] = defaultdict(list)
    for n, i in by_num.items():
        ph = phase_of(i)
        (epics_by_phase if kind(i) == "epic" else leaves_by_phase)[ph].append(n)

    n_epics = sum(len(v) for v in epics_by_phase.values())
    sections: list[str] = [
        "<h1>Board hierarchy</h1>",
        "<blockquote>"
        f"Owner: <strong>{OWNER}</strong> · Repo: <strong>{REPO}</strong> · "
        f"Project: <strong>{REPO}</strong> (#5). "
        f"{len(issues)} issues · {n_epics} epics · generated REST-only."
        "</blockquote>",
    ]
    for ph in PHASE_ORDER:
        if not epics_by_phase.get(ph) and not leaves_by_phase.get(ph):
            continue
        blocks: list[str] = [f"<h2>{html.escape(ph)}</h2>"]
        for en in sorted(epics_by_phase.get(ph, [])):
            e = by_num[en]
            epic_closed = e["state"] == "closed"
            state_cls = "state-closed" if epic_closed else "state-open"
            state_lbl = "✅ closed" if epic_closed else "🟡 open"
            blocks.append(
                f'<div class="epic-head"><h3>'
                f'<a href="{html.escape(e["html_url"])}" target="_blank" rel="noopener">'
                f"#{en}</a> — {html.escape(e["title"])}</h3>"
                f'<span class="{state_cls}">{state_lbl}</span></div>'
            )
        leaves = sorted(leaves_by_phase.get(ph, []))
        if leaves:
            rows = "".join(_issue_row(by_num[n]) for n in leaves)
            blocks.append(
                "<table><thead><tr><th>#</th><th>Title</th><th>State</th></tr></thead>"
                f"<tbody>{rows}</tbody></table>"
            )
        sections.append("".join(blocks))

    body = "\n    ".join(sections)
    HIERARCHY_HTML.write_text(
        portal_page_html(
            title="Board hierarchy",
            body_html=body,
            source_md=HIERARCHY.relative_to(ROOT),
        ),
        encoding="utf-8",
    )
    print(f"Wrote {HIERARCHY_HTML}")


def write_roadmap_html(issues: list[dict]) -> None:
    by_phase = issues_by_phase(issues)
    sections: list[str] = [
        "<h1>ROADMAP</h1>",
        "<blockquote>Generated (REST-only) mirror of GitHub issues by phase.</blockquote>",
    ]
    for ph in PHASE_ORDER:
        d = by_phase.get(ph)
        if not d or (not d["open"] and not d["closed"]):
            continue
        blocks: list[str] = [f"<h2>{html.escape(ph)}</h2>"]
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
            blocks.append(f"<h3>{state.capitalize()}</h3><ul>{''.join(lis)}</ul>")
        sections.append("".join(blocks))

    body = "\n    ".join(sections) if len(sections) > 2 else "<p>No issues.</p>"
    ROADMAP_HTML.write_text(
        portal_page_html(
            title="ROADMAP",
            body_html=body,
            source_md=ROADMAP.relative_to(ROOT),
        ),
        encoding="utf-8",
    )
    print(f"Wrote {ROADMAP_HTML}")


def write_portal_md_html() -> None:
    for md_name, title in PORTAL_MD_PAGES:
        src = PLANNING / md_name
        if not src.is_file():
            print(f"Skip missing {src}", file=sys.stderr)
            continue
        out = PLANNING / (src.stem + ".html")
        body = md_to_html(src.read_text(encoding="utf-8"))
        out.write_text(
            portal_page_html(
                title=title,
                body_html=body,
                source_md=src.relative_to(ROOT),
            ),
            encoding="utf-8",
        )
        print(f"Wrote {out}")


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
    write_board_hierarchy_html(issues)
    write_portal_md_html()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
