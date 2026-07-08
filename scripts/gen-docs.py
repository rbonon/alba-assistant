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
Also generates `phase-map.html` and `progress-report.html` from live issue state.

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
PHASE_MAP_HTML = PLANNING / "phase-map.html"
PROGRESS_HTML = PLANNING / "progress-report.html"
PHASE_ORDER = [f"P{i}" for i in range(15)] + ["No Phase"]
PLANNING_PHASES = [f"P{i}" for i in range(6)]
DELIVERY_PHASES = [f"P{i}" for i in range(6, 15)]
PHASE_LABELS: dict[str, str] = {
    "P0": "Foundation",
    "P1": "Spec",
    "P2": "Architecture",
    "P3": "Environments",
    "P4": "Operations",
    "P5": "Roadmap",
    "P6": "MVP index",
    "P7": "API+MCP",
    "P8": "Writes",
    "P9": "Clinical",
    "P10": "Calendar",
    "P11": "Tasks",
    "P12": "Drive",
    "P13": "Android",
    "P14": "Alexa",
}

# Markdown canon → portal HTML (features.html is hand-maintained separately)
PORTAL_MD_SOURCES: list[tuple[Path, str, str, str]] = [
    # path (from repo root), title, lang, optional preamble HTML
    (Path("docs/planning/open-questions.md"), "Open questions", "en", ""),
    (Path("docs/planning/decisions.md"), "Decisions log", "en", ""),
    (Path("docs/planning/workflow.md"), "Workflow", "en", ""),
    (Path("docs/planning/phases.md"), "Phases & epics", "en", ""),
    (Path("docs/planning/modules.md"), "Modules & tools", "en", ""),
    (Path("docs/planning/architecture.md"), "Architecture", "en", ""),
    (Path("docs/planning/session-handoff.md"), "Session handoff", "en", ""),
    (Path("docs/planning/product-vision.md"), "Product vision", "en", ""),
    (Path("docs/planning/README.md"), "Planning index", "en", ""),
    (
        Path("docs/vision/alba-context-assistant-handoff.md"),
        "Architecture handoff",
        "pt",
        '<p class="notice"><strong>Vision input (Portuguese)</strong> — not final spec. '
        "Canon lives in <code>docs/planning/</code> and <code>DECISIONS.md</code> after grilling.</p>",
    ),
    (Path("docs/vision/README.md"), "Vision index", "en", ""),
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


def state_badge(issue: dict, *, compact: bool = False) -> str:
    closed = issue["state"] == "closed"
    cls = "state-closed" if closed else "state-open"
    if compact:
        icon = "✅" if closed else "🟡"
        label = "closed" if closed else "open"
        return f'<span class="issue-state {cls}" aria-label="{label}">{icon}</span>'
    text = "✅ closed" if closed else "🟡 open"
    return f'<span class="{cls}">{text}</span>'


def issue_link(issue: dict) -> str:
    return (
        f'<a href="{html.escape(issue["html_url"])}" target="_blank" rel="noopener">'
        f'#{issue["number"]}</a>'
    )


def issue_line(issue: dict, *, compact_badge: bool = True) -> str:
    closed = issue["state"] == "closed"
    li_cls = "issue-closed" if closed else "issue-open"
    title = html.escape(issue["title"])
    badge = state_badge(issue, compact=compact_badge)
    return (
        f'<li class="{li_cls}">{issue_link(issue)} '
        f'<span class="issue-title">{title}</span> {badge}</li>'
    )


def compute_phase_states(by_phase: dict[str, dict[str, list]]) -> dict[str, str]:
    states: dict[str, str] = {}
    current_set = False
    for ph in PHASE_ORDER[:-1]:
        d = by_phase.get(ph)
        if not d or (not d["open"] and not d["closed"]):
            states[ph] = "future"
            continue
        if not d["open"]:
            states[ph] = "done"
        elif not current_set:
            states[ph] = "current"
            current_set = True
        else:
            states[ph] = "future"
    return states


def current_phase_label(states: dict[str, str]) -> str:
    for ph in PHASE_ORDER[:-1]:
        if states.get(ph) == "current":
            return f"{ph} — {PHASE_LABELS.get(ph, ph)}"
    for ph in reversed(PHASE_ORDER[:-1]):
        if states.get(ph) == "done":
            nxt = f"P{int(ph[1:]) + 1}" if ph[1:].isdigit() and int(ph[1:]) < 14 else None
            if nxt and nxt in PHASE_LABELS:
                return f"{nxt} — {PHASE_LABELS[nxt]}"
    return "P0 — Foundation"


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
    row_cls = "issue-closed" if closed else "issue-open"
    title = html.escape(i["title"])
    return (
        f'<tr class="{row_cls}"><td>{issue_link(i)}</td><td>{title}</td>'
        f'<td class="col-status">{state_badge(i, compact=True)}</td></tr>'
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
            blocks.append(
                f'<div class="epic-head"><h3>'
                f'<a href="{html.escape(e["html_url"])}" target="_blank" rel="noopener">'
                f"#{en}</a> — {html.escape(e['title'])}</h3>"
                f'{state_badge(e, compact=True)}</div>'
            )
        leaves = sorted(leaves_by_phase.get(ph, []))
        if leaves:
            rows = "".join(_issue_row(by_num[n]) for n in leaves)
            blocks.append(
                "<table><colgroup>"
                '<col class="col-num" /><col /><col class="col-status" />'
                "</colgroup><thead><tr><th>#</th><th>Title</th>"
                '<th class="col-status" aria-label="Status"></th></tr></thead>'
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
            lis = [issue_line(i) for i in items]
            blocks.append(f"<h3>{state.capitalize()}</h3><ul class=\"issue-list\">{''.join(lis)}</ul>")
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


def _phase_track_node(ph: str, states: dict[str, str]) -> str:
    status = states.get(ph, "future")
    label = PHASE_LABELS.get(ph, ph)
    return (
        f'<div class="phase-node {status}"><div class="num">{html.escape(ph)}</div>'
        f'<div class="label">{html.escape(label)}</div></div>'
    )


def _phase_card(ph: str, states: dict[str, str], by_phase: dict[str, dict[str, list]]) -> str:
    status = states.get(ph, "future")
    label = PHASE_LABELS.get(ph, ph)
    d = by_phase.get(ph, {"open": [], "closed": []})
    all_issues = sorted(d["open"] + d["closed"], key=lambda x: x["number"])
    n_open = len(d["open"])
    n_closed = len(d["closed"])
    if all_issues:
        count = f"{n_closed}/{n_closed + n_open} closed"
        items = "".join(issue_line(i) for i in all_issues)
        issue_html = f'<ul class="phase-issue-list">{items}</ul>'
    else:
        count = "no issues"
        issue_html = '<p class="empty">No issues yet</p>'
    return (
        f'<article class="phase-card {status}">'
        f'<div class="phase-card-head">'
        f'<div><span class="num">{html.escape(ph)}</span> '
        f'<span class="label">{html.escape(label)}</span></div>'
        f'<span class="phase-card-count">{count}</span></div>'
        f"{issue_html}</article>"
    )


def write_phase_map_html(issues: list[dict]) -> None:
    by_phase = issues_by_phase(issues)
    states = compute_phase_states(by_phase)
    current = current_phase_label(states)

    planning_track = "".join(_phase_track_node(ph, states) for ph in PLANNING_PHASES)
    delivery_track = "".join(_phase_track_node(ph, states) for ph in DELIVERY_PHASES)
    planning_cards = "".join(_phase_card(ph, states, by_phase) for ph in PLANNING_PHASES)
    delivery_cards = "".join(_phase_card(ph, states, by_phase) for ph in DELIVERY_PHASES)

    body = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Alba — Phase map</title>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../assets/portal.css" />
</head>
<body>
  <div class="toolbar"><div class="brand"><a href="../index.html">← Alba Docs</a></div></div>
  <main class="phase-map-wrap">
    <h1 style="font-size:1.5rem;color:var(--navy)">Phase map</h1>
    <p style="color:var(--muted);margin:0.5rem 0 1rem">
      Generated from GitHub issues. Canon: <a href="./phases.html">phases.html</a>.
      <span class="badge badge-progress">Current: {html.escape(current.split(" — ")[0])}</span>
    </p>

    <h2 class="phase-section-title">Planning (no code)</h2>
    <div class="phase-track">{planning_track}</div>
    <div class="gate-chip">Gate after each phase — human approval required</div>
    <div class="phase-detail-grid">{planning_cards}</div>

    <h2 class="phase-section-title">Delivery (OpenSpec)</h2>
    <div class="phase-track">{delivery_track}</div>
    <p style="margin:0.5rem 0 0.25rem;color:var(--muted);font-size:0.88rem">
      MVP go-live marker at end of <strong>P7</strong> (staging → production).
    </p>
    <div class="phase-detail-grid">{delivery_cards}</div>

    <p style="margin-top:1.5rem;font-size:0.82rem;color:var(--muted)">
      Regenerate: <code>./scripts/refresh-roadmap.sh</code> ·
      <span class="state-open">🟡</span> open · <span class="state-closed">✅</span> closed
    </p>
  </main>
</body>
</html>
"""
    PHASE_MAP_HTML.write_text(body, encoding="utf-8")
    print(f"Wrote {PHASE_MAP_HTML}")


def write_progress_report_html(issues: list[dict]) -> None:
    by_phase = issues_by_phase(issues)
    states = compute_phase_states(by_phase)
    current = current_phase_label(states)

    p1 = by_phase.get("P1", {"open": [], "closed": []})
    grill_closed = [
        i for i in p1["closed"]
        if "[Grill]" in i["title"] and i["number"] >= 14
    ]
    grill_open = [i for i in p1["open"] if "[Grill]" in i["title"]]
    next_open = sorted(p1["open"], key=lambda x: x["number"])
    next_issue = next_open[0] if next_open else None
    next_html = (
        f'<a href="{html.escape(next_issue["html_url"])}">#{next_issue["number"]}</a>'
        if next_issue
        else "—"
    )
    grill_summary = "none closed"
    if grill_closed:
        nums = sorted(i["number"] for i in grill_closed)
        grill_summary = f"#{nums[0]}–#{nums[-1]} closed ({len(nums)})"
    if grill_open:
        grill_summary += f" · {len(grill_open)} open"

    body = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Alba — Progress report</title>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../assets/portal.css" />
  <style>
    .wrap {{ max-width: 960px; margin: 0 auto; padding: 2rem 1.25rem 3rem; }}
    .stats {{ display: flex; flex-wrap: wrap; gap: 0.5rem; margin: 1rem 0; }}
    .stats span {{ background: var(--card); border: 1px solid var(--border); padding: 0.35rem 0.75rem; border-radius: 999px; font-size: 0.8rem; }}
    .view-links {{ display: flex; flex-wrap: wrap; gap: 0.75rem; margin: 1rem 0; }}
    .view-links a {{
      display: inline-flex; align-items: center; gap: 0.35rem;
      background: var(--card); border: 1px solid var(--border); border-radius: var(--radius);
      padding: 0.55rem 0.9rem; font-size: 0.85rem; font-weight: 600; text-decoration: none;
    }}
    .view-links a:hover {{ border-color: var(--blue); }}
    .view-tabs {{ display: flex; gap: 0.5rem; margin: 1rem 0 0.5rem; }}
    .view-tabs button {{
      font-family: inherit; font-size: 0.82rem; font-weight: 600;
      padding: 0.45rem 0.85rem; border-radius: 999px; cursor: pointer;
      border: 1px solid var(--border); background: var(--card); color: var(--navy);
    }}
    .view-tabs button.active {{ background: var(--blue); border-color: var(--blue); color: #fff; }}
    #view-frame {{
      width: 100%; height: 560px; border: 1px solid var(--border);
      border-radius: 8px; background: #fff;
    }}
    .legend {{ font-size: 0.82rem; color: var(--muted); margin: 0.5rem 0 0; }}
    .legend .state-open, .legend .state-closed {{ font-weight: 600; }}
  </style>
</head>
<body>
  <div class="toolbar"><div class="brand"><a href="../index.html">← Alba Docs</a></div></div>
  <main class="wrap">
    <h1 style="font-size:1.5rem;color:var(--navy)">Progress — issue list</h1>
    <p style="color:var(--muted);margin-bottom:1rem">
      Generated views of the GitHub board. Live board:
      <a href="https://github.com/users/rbonon/projects/5">alba-assistant #5</a>
    </p>
    <div class="stats">
      <span><strong>Phase:</strong> {html.escape(current)}</span>
      <span><strong>P1 grilling:</strong> {html.escape(grill_summary)}</span>
      <span><strong>Next:</strong> {next_html}</span>
      <span>Regenerate: <code>./scripts/refresh-roadmap.sh</code></span>
    </div>
    <p class="legend">
      <span class="state-open">🟡 open</span> · <span class="state-closed">✅ closed</span> on every issue line below
    </p>
    <div class="view-links">
      <a href="./board-hierarchy.html">Board hierarchy (HTML)</a>
      <a href="./roadmap.html">ROADMAP (HTML)</a>
      <a href="./phase-map.html">Phase map</a>
      <a href="https://github.com/rbonon/alba-assistant/blob/main/ROADMAP.md" target="_blank" rel="noopener">ROADMAP.md on GitHub</a>
    </div>
    <div class="view-tabs" role="tablist" aria-label="Board views">
      <button type="button" class="active" data-src="./board-hierarchy.html" role="tab" aria-selected="true">Hierarchy</button>
      <button type="button" data-src="./roadmap.html" role="tab" aria-selected="false">ROADMAP</button>
    </div>
    <iframe id="view-frame" title="Board view" src="./board-hierarchy.html"></iframe>
    <p style="margin-top:1rem;font-size:0.85rem;color:var(--muted)">
      Portal HTML is generated by <code>scripts/gen-docs.py</code> — run <code>./scripts/refresh-roadmap.sh</code> after board changes.
    </p>
  </main>
  <script>
    document.querySelectorAll('.view-tabs button').forEach((btn) => {{
      btn.addEventListener('click', () => {{
        document.querySelectorAll('.view-tabs button').forEach((b) => {{
          b.classList.remove('active');
          b.setAttribute('aria-selected', 'false');
        }});
        btn.classList.add('active');
        btn.setAttribute('aria-selected', 'true');
        document.getElementById('view-frame').src = btn.dataset.src;
      }});
    }});
  </script>
</body>
</html>
"""
    PROGRESS_HTML.write_text(body, encoding="utf-8")
    print(f"Wrote {PROGRESS_HTML}")


def write_portal_md_html() -> None:
    for rel_path, title, lang, preamble in PORTAL_MD_SOURCES:
        src = ROOT / rel_path
        if not src.is_file():
            print(f"Skip missing {src}", file=sys.stderr)
            continue
        out = src.with_suffix(".html")
        body = md_to_html(src.read_text(encoding="utf-8"))
        out.write_text(
            portal_page_html(
                title=title,
                body_html=body,
                source_md=rel_path,
                lang=lang,
                preamble_html=preamble,
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
    write_phase_map_html(issues)
    write_progress_report_html(issues)
    write_portal_md_html()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
