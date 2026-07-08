"""Minimal Markdown → HTML for GitHub Pages portal (no third-party deps)."""
from __future__ import annotations

import html
import re
from pathlib import Path

RE_LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
RE_CODE = re.compile(r"`([^`]+)`")
RE_BOLD = re.compile(r"\*\*([^*]+)\*\*")
RE_INLINE = re.compile(
    r"\[([^\]]+)\]\(([^)]+)\)|`([^`]+)`|\*\*([^*]+)\*\*"
)


def inline_format(text: str) -> str:
    out: list[str] = []
    pos = 0
    for m in RE_INLINE.finditer(text):
        out.append(html.escape(text[pos : m.start()]))
        if m.group(1) is not None:
            href = html.escape(m.group(2), quote=True)
            out.append(f'<a href="{href}">{html.escape(m.group(1))}</a>')
        elif m.group(3) is not None:
            out.append(f"<code>{html.escape(m.group(3))}</code>")
        elif m.group(4) is not None:
            out.append(f"<strong>{html.escape(m.group(4))}</strong>")
        pos = m.end()
    out.append(html.escape(text[pos:]))
    return "".join(out)


def _parse_table(lines: list[str], start: int) -> tuple[str | None, int]:
    rows: list[list[str]] = []
    i = start
    while i < len(lines) and lines[i].strip().startswith("|"):
        row = [c.strip() for c in lines[i].strip().strip("|").split("|")]
        rows.append(row)
        i += 1
    if len(rows) < 2:
        return None, start
    header = rows[0]
    body_rows = [r for r in rows[2:] if not all(set(c) <= {"-", ":", " "} for c in r)]
    thead = "".join(f"<th>{inline_format(c)}</th>" for c in header)
    tbody_parts: list[str] = []
    for row in body_rows:
        cells = row + [""] * (len(header) - len(row))
        tds = []
        for cell in cells[: len(header)]:
            cls = ""
            low = cell.lower()
            if low in ("closed", "done", "✅"):
                cls = ' class="closed"'
            tds.append(f"<td{cls}>{inline_format(cell)}</td>")
        tbody_parts.append(f"<tr>{''.join(tds)}</tr>")
    table = f"<table><thead><tr>{thead}</tr></thead><tbody>{''.join(tbody_parts)}</tbody></table>"
    return table, i


def md_to_html(md: str) -> str:
    lines = md.splitlines()
    out: list[str] = []
    i = 0
    in_code = False
    list_buf: list[str] = []
    list_ordered = False

    def flush_list() -> None:
        nonlocal list_buf, list_ordered
        if not list_buf:
            return
        tag = "ol" if list_ordered else "ul"
        items = "".join(f"<li>{inline_format(item)}</li>" for item in list_buf)
        out.append(f"<{tag}>{items}</{tag}>")
        list_buf = []

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if stripped.startswith("```"):
            flush_list()
            if in_code:
                out.append("</code></pre>")
                in_code = False
            else:
                out.append("<pre><code>")
                in_code = True
            i += 1
            continue

        if in_code:
            out.append(html.escape(line))
            i += 1
            continue

        if not stripped:
            flush_list()
            i += 1
            continue

        if stripped == "---":
            flush_list()
            out.append("<hr />")
            i += 1
            continue

        if stripped.startswith("|"):
            flush_list()
            table, ni = _parse_table(lines, i)
            if table:
                out.append(table)
                i = ni
                continue

        if stripped.startswith("### "):
            flush_list()
            out.append(f"<h3>{inline_format(stripped[4:])}</h3>")
            i += 1
            continue
        if stripped.startswith("## "):
            flush_list()
            out.append(f"<h2>{inline_format(stripped[3:])}</h2>")
            i += 1
            continue
        if stripped.startswith("# "):
            flush_list()
            out.append(f"<h1>{inline_format(stripped[2:])}</h1>")
            i += 1
            continue

        if stripped.startswith("> "):
            flush_list()
            quotes = []
            while i < len(lines) and lines[i].strip().startswith("> "):
                quotes.append(lines[i].strip()[2:])
                i += 1
            out.append(f"<blockquote>{inline_format(' '.join(quotes))}</blockquote>")
            continue

        m = re.match(r"- \[( |x|X)\] (.*)", stripped)
        if m:
            if list_buf and list_ordered:
                flush_list()
            list_ordered = False
            checked = m.group(1).lower() == "x"
            mark = "☑" if checked else "☐"
            list_buf.append(f"{mark} {m.group(2)}")
            i += 1
            continue

        m = re.match(r"(\d+)\.\s+(.*)", stripped)
        if m:
            if list_buf and not list_ordered:
                flush_list()
            list_ordered = True
            list_buf.append(m.group(2))
            i += 1
            continue

        if stripped.startswith("- ") or stripped.startswith("* "):
            if list_buf and list_ordered:
                flush_list()
            list_ordered = False
            list_buf.append(stripped[2:])
            i += 1
            continue

        flush_list()
        out.append(f"<p>{inline_format(stripped)}</p>")
        i += 1

    flush_list()
    if in_code:
        out.append("</code></pre>")
    return "\n    ".join(out)


def portal_page_html(
    *,
    title: str,
    body_html: str,
    back_href: str = "../index.html",
    source_md: Path | str | None = None,
    embed_friendly: bool = True,
    lang: str = "en",
    preamble_html: str = "",
) -> str:
    source_line = ""
    if source_md is not None:
        md_name = source_md.as_posix() if isinstance(source_md, Path) else source_md
        gh = f"https://github.com/rbonon/alba-assistant/blob/main/{md_name}"
        source_line = (
            f'<p class="source-note doc-footer">Markdown source: '
            f'<a href="{html.escape(gh)}">{html.escape(Path(md_name).name)}</a></p>'
        )
    embed_script = ""
    if embed_friendly:
        embed_script = """<script>
if (window.self !== window.top) document.body.classList.add('embed');
</script>"""
    return f"""<!DOCTYPE html>
<html lang="{html.escape(lang)}">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Alba — {html.escape(title)}</title>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../assets/portal.css" />
  <link rel="stylesheet" href="../assets/portal-doc.css" />
</head>
<body>
  <div class="toolbar"><div class="brand"><a href="{html.escape(back_href)}">← Alba Docs</a></div></div>
  <main class="doc-body doc-body--wide">
    {preamble_html}
    {body_html}
    {source_line}
  </main>
  {embed_script}
</body>
</html>
"""
