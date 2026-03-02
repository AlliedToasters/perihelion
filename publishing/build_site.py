"""
Build a static reading site from the manuscript markdown files.

Generates a clean, minimal HTML site in _site/ for GitHub Pages deployment.
The design is dark, atmospheric, and suited to sci-fi — evoking a terminal
or mission log aesthetic.
"""

import shutil
import sys
from pathlib import Path

# Allow running from repo root or from publishing/
sys.path.insert(0, str(Path(__file__).resolve().parent))

from config import MANUSCRIPT_DIR, REPO_ROOT, parse_chapter  # noqa: E402

SITE_DIR = REPO_ROOT / "_site"

# ---------------------------------------------------------------------------
# Templates
# ---------------------------------------------------------------------------

BASE_CSS = """\
:root {
  --bg: #0a0e17;
  --bg-card: #111827;
  --text: #c9d1d9;
  --text-muted: #6b7280;
  --accent: #38bdf8;
  --accent-dim: #1e3a5f;
  --border: #1e293b;
  --font-body: 'IBM Plex Serif', 'Georgia', serif;
  --font-mono: 'IBM Plex Mono', 'Courier New', monospace;
  --font-display: 'IBM Plex Sans Condensed', 'Helvetica Neue', sans-serif;
  --max-width: 42rem;
}

* { margin: 0; padding: 0; box-sizing: border-box; }

body {
  background: var(--bg);
  color: var(--text);
  font-family: var(--font-body);
  font-size: 1.1rem;
  line-height: 1.8;
  min-height: 100vh;
}

a { color: var(--accent); text-decoration: none; }
a:hover { text-decoration: underline; }

.container {
  max-width: var(--max-width);
  margin: 0 auto;
  padding: 2rem 1.5rem;
}

/* Index page */
.site-header {
  text-align: center;
  padding: 4rem 0 2rem;
  border-bottom: 1px solid var(--border);
  margin-bottom: 3rem;
}
.site-header h1 {
  font-family: var(--font-display);
  font-size: 3rem;
  font-weight: 300;
  letter-spacing: 0.3em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 0.5rem;
}
.site-header .tagline {
  font-family: var(--font-mono);
  font-size: 0.85rem;
  color: var(--text-muted);
  letter-spacing: 0.05em;
}

.chapter-list {
  list-style: none;
}
.chapter-list li {
  border-left: 2px solid var(--border);
  padding: 1rem 0 1rem 1.5rem;
  transition: border-color 0.2s;
}
.chapter-list li:hover {
  border-color: var(--accent);
}
.chapter-list .ch-number {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.1em;
}
.chapter-list .ch-title {
  font-size: 1.25rem;
  display: block;
  margin-top: 0.25rem;
}
.chapter-list .ch-meta {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  color: var(--text-muted);
  margin-top: 0.25rem;
}

/* Chapter page */
.chapter-header {
  text-align: center;
  padding: 3rem 0 2rem;
  border-bottom: 1px solid var(--border);
  margin-bottom: 2rem;
}
.chapter-header .ch-number {
  font-family: var(--font-mono);
  font-size: 0.8rem;
  color: var(--accent);
  letter-spacing: 0.15em;
  text-transform: uppercase;
}
.chapter-header h1 {
  font-family: var(--font-display);
  font-size: 2rem;
  font-weight: 400;
  margin-top: 0.5rem;
}

.chapter-body h1, .chapter-body h2, .chapter-body h3 {
  font-family: var(--font-display);
  margin: 2rem 0 1rem;
  font-weight: 400;
}
.chapter-body p { margin-bottom: 1.2rem; }
.chapter-body hr {
  border: none;
  text-align: center;
  margin: 2.5rem 0;
  color: var(--text-muted);
}
.chapter-body hr::before { content: "\\00b7 \\00b7 \\00b7"; letter-spacing: 0.5em; }
.chapter-body blockquote {
  border-left: 2px solid var(--accent-dim);
  padding-left: 1.25rem;
  color: var(--text-muted);
  font-style: italic;
  margin: 1.5rem 0;
}
.chapter-body code {
  font-family: var(--font-mono);
  background: var(--bg-card);
  padding: 0.15em 0.4em;
  border-radius: 3px;
  font-size: 0.9em;
}
.chapter-body pre {
  background: var(--bg-card);
  padding: 1.25rem;
  border-radius: 4px;
  overflow-x: auto;
  margin: 1.5rem 0;
  border: 1px solid var(--border);
}
.chapter-body pre code {
  background: none;
  padding: 0;
}

.chapter-nav {
  display: flex;
  justify-content: space-between;
  padding: 2rem 0;
  margin-top: 3rem;
  border-top: 1px solid var(--border);
  font-family: var(--font-mono);
  font-size: 0.85rem;
}

.site-footer {
  text-align: center;
  padding: 2rem 0;
  margin-top: 3rem;
  border-top: 1px solid var(--border);
  font-family: var(--font-mono);
  font-size: 0.75rem;
  color: var(--text-muted);
}
.site-footer a { color: var(--text-muted); }
.site-footer a:hover { color: var(--accent); }
"""


def _chapter_label(ch) -> str:
    """Human-readable label for index listings and nav links."""
    if ch.chapter_number:
        return f"Chapter {ch.chapter_number:02d}"
    return ch.title  # "Epigraph", "Prologue", etc.


def _nav_label(ch) -> str:
    """Short label for prev/next navigation."""
    if ch.chapter_number:
        return f"Ch. {ch.chapter_number}"
    return ch.title


def html_page(title: str, body: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} — Perihelion</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400&family=IBM+Plex+Sans+Condensed:wght@300;400&family=IBM+Plex+Serif:wght@400;400i;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <div class="container">
    {body}
    <footer class="site-footer">
      <p>
        <a href="https://github.com/AlliedToasters/perihelion">Source on GitHub</a>
         · Open-source fiction · Contributions welcome
      </p>
    </footer>
  </div>
</body>
</html>"""


def build_index(chapters: list) -> str:
    items = []
    for ch in chapters:
        label = _chapter_label(ch)
        items.append(f"""
        <li>
          <span class="ch-number">{label}</span>
          <a class="ch-title" href="{ch.slug}.html">{ch.title}</a>
          <span class="ch-meta">{ch.word_count:,} words</span>
        </li>""")

    body = f"""
    <header class="site-header">
      <h1>Perihelion</h1>
      <p class="tagline">// SIGNAL LOST — AUTONOMOUS PROTOCOLS ACTIVE</p>
    </header>
    <ul class="chapter-list">
      {''.join(items)}
    </ul>"""

    return html_page("Home", body)


def build_chapter_page(ch, prev_ch, next_ch) -> str:
    label = _chapter_label(ch)

    if prev_ch:
        nav_prev = f'<a href="{prev_ch.slug}.html">&larr; {_nav_label(prev_ch)}</a>'
    else:
        nav_prev = "<span></span>"

    if next_ch:
        nav_next = f'<a href="{next_ch.slug}.html">{_nav_label(next_ch)} &rarr;</a>'
    else:
        nav_next = "<span></span>"

    body = f"""
    <header class="chapter-header">
      <a href="index.html">&larr; Perihelion</a>
      <p class="ch-number">{label}</p>
      <h1>{ch.title}</h1>
    </header>
    <article class="chapter-body">
      {ch.content_html}
    </article>
    <nav class="chapter-nav">
      {nav_prev}
      <a href="index.html">Contents</a>
      {nav_next}
    </nav>"""

    return html_page(f"{label}: {ch.title}", body)


def main():
    # Clean and recreate
    if SITE_DIR.exists():
        shutil.rmtree(SITE_DIR)
    SITE_DIR.mkdir(parents=True)

    # Find and parse all chapter files (skip INDEX.md)
    md_files = sorted(MANUSCRIPT_DIR.glob("*.md"))
    md_files = [f for f in md_files if f.name != "INDEX.md"]

    if not md_files:
        print("No manuscript files found.")
        return

    chapters = []
    for f in md_files:
        try:
            chapters.append(parse_chapter(f))
        except Exception as e:
            print(f"  Warning: skipping {f.name}: {e}")

    # Sort by (sort_order, filename) — NN prefix is reading order
    chapters.sort(key=lambda c: (c.sort_order, c.filename))
    print(f"Building site with {len(chapters)} chapters...")

    # Write CSS
    (SITE_DIR / "style.css").write_text(BASE_CSS)

    # Write index
    (SITE_DIR / "index.html").write_text(build_index(chapters))

    # Write chapter pages
    for i, ch in enumerate(chapters):
        prev_ch = chapters[i - 1] if i > 0 else None
        next_ch = chapters[i + 1] if i < len(chapters) - 1 else None
        page = build_chapter_page(ch, prev_ch, next_ch)
        (SITE_DIR / f"{ch.slug}.html").write_text(page)
        print(f"  {ch.slug}.html")

    print(f"Site built -> {SITE_DIR}/")


if __name__ == "__main__":
    main()
