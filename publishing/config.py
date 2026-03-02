"""
Shared configuration and chapter-parsing logic for the publishing pipeline.

Imports timestamp rendering directly from tracking/timestamps.py so there
is a single source of truth for placeholder resolution.
"""

import hashlib
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

# Let Python find the tracking module
REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "tracking"))

import timestamps as ts  # noqa: E402

MANUSCRIPT_DIR = REPO_ROOT / "manuscript"

# Filename pattern: NN_chXX_station_type.md  (epigraph/prologue lack chXX)
_CHAPTER_RE = re.compile(
    r"^(\d+)"            # NN sort order
    r"(?:_ch(\d+))?"     # optional chXX
    r"(?:_([^.]+))?"     # station_type tail (e.g. p8_imr)
    r"\.md$"
)


@dataclass
class Chapter:
    title: str
    chapter_number: int          # 0 for epigraph/prologue
    slug: str
    word_count: int
    content_html: str
    content_md: str
    content_hash: str
    tags: list[str] = field(default_factory=lambda: ["sci-fi", "ai-safety", "fiction", "space"])
    subtitle: str = ""
    filepath: str = ""           # relative to repo root
    filename: str = ""
    sort_order: int = 0
    station: str = ""
    chapter_type: str = ""


def _slugify(text: str) -> str:
    s = text.lower().strip()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[\s_]+", "-", s)
    return re.sub(r"-+", "-", s).strip("-")


def parse_chapter(filepath: Path) -> Chapter:
    """Read a manuscript markdown file and return a populated Chapter."""
    filepath = Path(filepath)
    raw = filepath.read_text()

    # Resolve timestamps / variables
    data = ts.load()
    variables = ts.load_variables()
    rendered_md = ts.render_text(raw, data, variables)

    # Convert to HTML — import markdown lazily so the rest of the module
    # works even if the package isn't installed (useful for tracking-only ops)
    import markdown
    html = markdown.markdown(rendered_md, extensions=["extra", "smarty"])

    # Extract title from first heading, or derive from filename
    title_match = re.search(r"^#\s+(.+)", rendered_md, re.MULTILINE)
    if title_match:
        title = title_match.group(1).strip()
    else:
        # Derive readable title from filename: "00_epigraph" → "Epigraph"
        stem = filepath.stem
        # Strip leading NN_ sort prefix
        stem = re.sub(r"^\d+_", "", stem)
        title = stem.replace("_", " ").strip().title() or filepath.stem

    # Parse filename
    m = _CHAPTER_RE.match(filepath.name)
    sort_order = int(m.group(1)) if m else 0
    chapter_number = int(m.group(2)) if m and m.group(2) else 0
    tail = m.group(3) if m and m.group(3) else ""

    # Split tail into station + type (e.g. "p8_imr" → "p8", "imr")
    station = ""
    chapter_type = ""
    if tail:
        parts = tail.rsplit("_", 1)
        if len(parts) == 2:
            station, chapter_type = parts
        else:
            chapter_type = parts[0]

    # Build a readable label for non-chapter entries
    if chapter_number:
        label = f"ch{chapter_number:02d}-{_slugify(title)}"
    else:
        label = _slugify(title) or filepath.stem

    word_count = len(rendered_md.split())
    content_hash = hashlib.sha256(rendered_md.encode()).hexdigest()[:16]

    return Chapter(
        title=title,
        chapter_number=chapter_number,
        slug=label,
        word_count=word_count,
        content_html=html,
        content_md=rendered_md,
        content_hash=content_hash,
        filepath=str(filepath.relative_to(REPO_ROOT)),
        filename=filepath.name,
        sort_order=sort_order,
        station=station,
        chapter_type=chapter_type,
    )
