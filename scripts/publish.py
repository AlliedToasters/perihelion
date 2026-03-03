#!/usr/bin/env python3
"""
Publish Perihelion manuscript chapters to Ghost via the Admin API.

Reads markdown files from manuscript/, resolves timestamp placeholders,
and creates or updates Ghost posts with the correct chapter/ch-XX tags.

Environment variables:
    GHOST_URL           - Ghost site URL (e.g. https://perihelion.ghost.io)
    GHOST_ADMIN_API_KEY - Admin API key (integration key from Ghost Admin)

Usage:
    python3 scripts/publish.py                    # dry-run: show what would be published
    python3 scripts/publish.py --publish          # actually publish to Ghost
    python3 scripts/publish.py --publish --force   # update all posts even if unchanged
"""

import argparse
import hashlib
import hmac
import json
import re
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from urllib.parse import urljoin

REPO_ROOT = Path(__file__).resolve().parent.parent
MANUSCRIPT_DIR = REPO_ROOT / "manuscript"
PAGES_DIR = REPO_ROOT / "pages"

# Add tracking to path for timestamp resolution
sys.path.insert(0, str(REPO_ROOT / "tracking"))
import timestamps as ts  # noqa: E402


# ── Chapter Parsing ──────────────────────────────────────────────────────────

CHAPTER_RE = re.compile(
    r"^(\d+)"            # NN sort order
    r"(?:_ch(\d+))?"     # optional chXX
    r"(?:_([^.]+))?"     # station_type tail
    r"\.md$"
)


@dataclass
class ManuscriptChapter:
    filepath: Path
    sort_order: int
    chapter_number: int   # 0 for epigraph/prologue
    title: str
    slug: str
    rendered_md: str
    content_hash: str
    station: str
    chapter_type: str


def slugify(text: str) -> str:
    s = text.lower().strip()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[\s_]+", "-", s)
    return re.sub(r"-+", "-", s).strip("-")


def parse_manuscript_file(filepath: Path) -> ManuscriptChapter:
    """Parse a manuscript markdown file into a ManuscriptChapter."""
    raw = filepath.read_text()

    # Resolve timestamps
    data = ts.load()
    variables = ts.load_variables()
    rendered_md = ts.render_text(raw, data, variables)

    # Extract title from first heading
    title_match = re.search(r"^#\s+(.+)", rendered_md, re.MULTILINE)
    if title_match:
        title = title_match.group(1).strip()
    else:
        stem = filepath.stem
        stem = re.sub(r"^\d+_", "", stem)
        title = stem.replace("_", " ").strip().title() or filepath.stem

    # Parse filename
    m = CHAPTER_RE.match(filepath.name)
    sort_order = int(m.group(1)) if m else 0
    chapter_number = int(m.group(2)) if m and m.group(2) else 0
    tail = m.group(3) if m and m.group(3) else ""

    station = ""
    chapter_type = ""
    if tail:
        parts = tail.rsplit("_", 1)
        if len(parts) == 2:
            station, chapter_type = parts
        else:
            chapter_type = parts[0]

    if chapter_number:
        slug = f"ch{chapter_number:02d}-{slugify(title)}"
    else:
        slug = slugify(title) or filepath.stem

    content_hash = hashlib.sha256(rendered_md.encode()).hexdigest()[:16]

    return ManuscriptChapter(
        filepath=filepath,
        sort_order=sort_order,
        chapter_number=chapter_number,
        title=title,
        slug=slug,
        rendered_md=rendered_md,
        content_hash=content_hash,
        station=station,
        chapter_type=chapter_type,
    )


# ── Ghost Admin API ──────────────────────────────────────────────────────────

def make_jwt(api_key: str) -> str:
    """Create a Ghost Admin API JWT from an admin API key."""
    import struct
    import base64

    key_id, secret_hex = api_key.split(":")
    secret = bytes.fromhex(secret_hex)

    # JWT header
    header = base64.urlsafe_b64encode(
        json.dumps({"alg": "HS256", "typ": "JWT", "kid": key_id}).encode()
    ).rstrip(b"=")

    # JWT payload — 5-minute expiry
    now = int(time.time())
    payload = base64.urlsafe_b64encode(
        json.dumps({
            "iat": now,
            "exp": now + 300,
            "aud": "/admin/"
        }).encode()
    ).rstrip(b"=")

    # Signature
    signing_input = header + b"." + payload
    signature = base64.urlsafe_b64encode(
        hmac.new(secret, signing_input, "sha256").digest()
    ).rstrip(b"=")

    return (signing_input + b"." + signature).decode()


class GhostAPI:
    """Minimal Ghost Admin API client using only stdlib."""

    def __init__(self, ghost_url: str, admin_api_key: str):
        self.base_url = ghost_url.rstrip("/")
        self.api_key = admin_api_key
        self._tags_cache = None

    def _request(self, method: str, path: str, data: dict = None) -> dict:
        url = f"{self.base_url}/ghost/api/admin/{path}"
        token = make_jwt(self.api_key)

        headers = {
            "Authorization": f"Ghost {token}",
            "Content-Type": "application/json",
        }

        body = json.dumps(data).encode() if data else None
        req = Request(url, data=body, headers=headers, method=method)

        try:
            with urlopen(req) as resp:
                return json.loads(resp.read())
        except HTTPError as e:
            error_body = e.read().decode()
            print(f"  API error {e.code}: {error_body}", file=sys.stderr)
            raise

    def get(self, path: str) -> dict:
        return self._request("GET", path)

    def post(self, path: str, data: dict) -> dict:
        return self._request("POST", path, data)

    def put(self, path: str, data: dict) -> dict:
        return self._request("PUT", path, data)

    def get_all_posts(self) -> list:
        """Fetch all posts (paginated)."""
        posts = []
        page = 1
        while True:
            result = self.get(f"posts/?limit=50&page={page}&formats=mobiledoc,lexical&include=tags")
            posts.extend(result.get("posts", []))
            meta = result.get("meta", {}).get("pagination", {})
            if page >= meta.get("pages", 1):
                break
            page += 1
        return posts

    def get_all_tags(self) -> list:
        """Fetch all tags."""
        if self._tags_cache is not None:
            return self._tags_cache
        result = self.get("tags/?limit=all")
        self._tags_cache = result.get("tags", [])
        return self._tags_cache

    def find_or_create_tag(self, slug: str, name: str) -> dict:
        """Find a tag by slug, or create it."""
        tags = self.get_all_tags()
        for t in tags:
            if t["slug"] == slug:
                return t
        # Create
        result = self.post("tags/", {"tags": [{"name": name, "slug": slug}]})
        tag = result["tags"][0]
        self._tags_cache = None  # invalidate cache
        return tag

    def create_post(self, post_data: dict) -> dict:
        result = self.post("posts/", {"posts": [post_data]})
        return result["posts"][0]

    def update_post(self, post_id: str, post_data: dict) -> dict:
        result = self.put(f"posts/{post_id}/", {"posts": [post_data]})
        return result["posts"][0]

    # ── Pages API ──

    def get_all_pages(self) -> list:
        """Fetch all Ghost pages (paginated), including drafts."""
        pages = []
        page_num = 1
        while True:
            result = self.get(f"pages/?limit=50&page={page_num}&status=all")
            pages.extend(result.get("pages", []))
            meta = result.get("meta", {}).get("pagination", {})
            if page_num >= meta.get("pages", 1):
                break
            page_num += 1
        return pages

    def update_page_html(self, page_id: str, page_data: dict) -> dict:
        """Update a Ghost page using ?source=html."""
        result = self.put(f"pages/{page_id}/?source=html", {"pages": [page_data]})
        return result["pages"][0]

    def delete_post(self, post_id: str) -> None:
        """Delete a Ghost post by ID."""
        url = f"{self.base_url}/ghost/api/admin/posts/{post_id}/"
        token = make_jwt(self.api_key)
        headers = {
            "Authorization": f"Ghost {token}",
            "Content-Type": "application/json",
        }
        req = Request(url, headers=headers, method="DELETE")
        try:
            with urlopen(req) as resp:
                pass  # 204 No Content on success
        except HTTPError as e:
            error_body = e.read().decode()
            print(f"  API error {e.code}: {error_body}", file=sys.stderr)
            raise


# ── Publishing Logic ─────────────────────────────────────────────────────────

def build_tags_for_chapter(ch: ManuscriptChapter) -> list[dict]:
    """Build the Ghost tags list for a chapter.

    The theme expects:
      - Tag 1: "chapter" (used by index.hbs to build the TOC)
      - Tag 2: "Chapter N" (used by chapter-card.hbs for the label)
    The epigraph is fetched by slug, not by tag, so it skips the chapter tag.
    """
    is_epigraph = ch.slug == "epigraph"
    if is_epigraph:
        return []
    tags = [{"slug": "chapter", "name": "chapter"}]
    if ch.chapter_number:
        tags.append({
            "slug": f"ch-{ch.chapter_number:02d}",
            "name": f"Chapter {ch.chapter_number}",
        })
    return tags


def build_post_data(ch: ManuscriptChapter, index: int,
                    existing_post: dict = None) -> dict:
    """Build the Ghost post data dict for creating/updating a post."""
    tags = build_tags_for_chapter(ch)

    # Set published_at with 1-day spacing so Ghost's prev/next navigation
    # follows reading order (oldest = first chapter, newest = last).
    import datetime as dt_mod
    base_date = datetime(2025, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
    publish_date = base_date + dt_mod.timedelta(days=index)

    data = {
        "title": ch.title,
        "slug": ch.slug,
        "mobiledoc": json.dumps({
            "version": "0.3.1",
            "markups": [],
            "atoms": [],
            "cards": [["markdown", {"markdown": ch.rendered_md}]],
            "sections": [[10, 0]],
        }),
        "status": "published",
        "published_at": publish_date.strftime("%Y-%m-%dT%H:%M:%S.000Z"),
        "tags": tags,
    }

    # Include the content hash as a code injection comment for change detection
    data["codeinjection_head"] = f"<!-- perihelion-hash:{ch.content_hash} -->"

    if existing_post:
        data["updated_at"] = existing_post["updated_at"]

    return data


def get_existing_hash(post: dict) -> str:
    """Extract the content hash from a post's code injection, if present."""
    head = post.get("codeinjection_head") or ""
    m = re.search(r"perihelion-hash:([a-f0-9]+)", head)
    return m.group(1) if m else ""


def _needs_tag_update(existing: dict, ch: ManuscriptChapter) -> bool:
    """Check if the remote post is missing expected tags."""
    remote_tags = {t["name"] for t in existing.get("tags", [])}
    is_epigraph = ch.slug == "epigraph"
    if not is_epigraph and "chapter" not in remote_tags:
        return True
    if ch.chapter_number and f"Chapter {ch.chapter_number}" not in remote_tags:
        return True
    return False


def publish_chapters(chapters: list[ManuscriptChapter], ghost_url: str,
                     api_key: str, force: bool = False):
    """Publish chapters to Ghost. Creates new posts or updates existing ones."""
    api = GhostAPI(ghost_url, api_key)

    # Fetch existing posts and index by slug
    existing_posts = api.get_all_posts()
    posts_by_slug = {p["slug"]: p for p in existing_posts}

    created = 0
    updated = 0
    skipped = 0

    for i, ch in enumerate(chapters):
        existing = posts_by_slug.get(ch.slug)

        if existing and not force:
            existing_hash = get_existing_hash(existing)
            if existing_hash == ch.content_hash and not _needs_tag_update(existing, ch):
                print(f"  skip  {ch.slug} (unchanged)")
                skipped += 1
                continue

        post_data = build_post_data(ch, i, existing)

        if existing:
            api.update_post(existing["id"], post_data)
            print(f"  update  {ch.slug}")
            updated += 1
        else:
            api.create_post(post_data)
            print(f"  create  {ch.slug}")
            created += 1

    # ── "To Be Continued" sentinel post ──
    # Tagged "chapter" so Ghost's prev/next navigation reaches it from the
    # last real chapter, but no "Chapter N" tag so the TOC card shows "// TO BE CONTINUED".
    tbc_slug = "to-be-continued"
    tbc_md = (
        "Perihelion is an ongoing work of collaborative fiction "
        "written by humans and AI. Eight stations, eight voices, no narrator. "
        "New chapters are added regularly.\n\n"
        "[About the project](/about/) · "
        "[Source on GitHub](https://github.com/AlliedToasters/perihelion)"
    )
    tbc_hash = hashlib.sha256(tbc_md.encode()).hexdigest()[:16]

    import datetime as dt_mod
    tbc_date = datetime(2025, 1, 1, 12, 0, 0, tzinfo=timezone.utc) + dt_mod.timedelta(days=len(chapters))

    tbc_data = {
        "title": "To Be Continued",
        "slug": tbc_slug,
        "mobiledoc": json.dumps({
            "version": "0.3.1",
            "markups": [],
            "atoms": [],
            "cards": [["markdown", {"markdown": tbc_md}]],
            "sections": [[10, 0]],
        }),
        "status": "published",
        "published_at": tbc_date.strftime("%Y-%m-%dT%H:%M:%S.000Z"),
        "tags": [
            {"slug": "chapter", "name": "chapter"},
            {"slug": "tbc", "name": "tbc"},
        ],
        "codeinjection_head": f"<!-- perihelion-hash:{tbc_hash} -->",
    }

    existing_tbc = posts_by_slug.get(tbc_slug)
    if existing_tbc:
        existing_tbc_hash = get_existing_hash(existing_tbc)
        if existing_tbc_hash == tbc_hash and not force:
            print(f"  skip  {tbc_slug} (unchanged)")
        else:
            tbc_data["updated_at"] = existing_tbc["updated_at"]
            api.update_post(existing_tbc["id"], tbc_data)
            print(f"  update  {tbc_slug}")
    else:
        api.create_post(tbc_data)
        print(f"  create  {tbc_slug}")

    # ── Cleanup: delete Ghost posts that no longer match any manuscript slug ──
    current_slugs = {ch.slug for ch in chapters}
    current_slugs.add(tbc_slug)
    deleted = 0
    for post in existing_posts:
        post_tags = {t["name"] for t in post.get("tags", [])}
        # Only clean up posts we manage (tagged "chapter" or the epigraph)
        is_managed = "chapter" in post_tags or post["slug"] == "epigraph"
        if is_managed and post["slug"] not in current_slugs:
            try:
                api.delete_post(post["id"])
                print(f"  delete  {post['slug']} (stale)")
                deleted += 1
            except Exception as e:
                print(f"  ERROR deleting {post['slug']}: {e}", file=sys.stderr)

    print(f"\nDone: {created} created, {updated} updated, {skipped} unchanged, {deleted} deleted")


# ── Managed Pages ────────────────────────────────────────────────────────────

# Maps source files in pages/ to their Ghost page slug.
MANAGED_PAGES = {
    "about.md": "about",
}


def _md_to_html(text: str) -> str:
    """Convert markdown to HTML using only stdlib.

    Handles paragraphs, headings, horizontal rules, links, bold, and italic.
    Good enough for simple about-page content without requiring pip packages.
    """
    import html as html_mod
    lines = text.strip().split("\n")
    out = []
    paragraph = []

    def flush_para():
        if paragraph:
            raw = " ".join(paragraph)
            raw = html_mod.escape(raw)
            # bold
            raw = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", raw)
            # italic
            raw = re.sub(r"\*(.+?)\*", r"<em>\1</em>", raw)
            # links
            raw = re.sub(r"\[(.+?)\]\((.+?)\)", r'<a href="\2">\1</a>', raw)
            # em-dash
            raw = raw.replace(" --- ", " &mdash; ").replace("---", "&mdash;")
            raw = raw.replace(" -- ", " &ndash; ").replace("--", "&ndash;")
            out.append(f"<p>{raw}</p>")
            paragraph.clear()

    for line in lines:
        stripped = line.strip()
        if not stripped:
            flush_para()
        elif stripped.startswith("# "):
            flush_para()
            heading = html_mod.escape(stripped[2:])
            out.append(f"<h1>{heading}</h1>")
        elif stripped.startswith("## "):
            flush_para()
            heading = html_mod.escape(stripped[3:])
            out.append(f"<h2>{heading}</h2>")
        elif stripped == "---" or stripped == "***":
            flush_para()
            out.append("<hr>")
        else:
            paragraph.append(stripped)

    flush_para()
    return "\n".join(out)


def sync_pages(ghost_url: str, api_key: str, force: bool = False):
    """Sync managed pages (pages/ dir) to Ghost pages by slug."""
    if not PAGES_DIR.is_dir():
        return

    api = GhostAPI(ghost_url, api_key)
    data = ts.load()
    variables = ts.load_variables()

    # Fetch all Ghost pages and index by slug
    ghost_pages = api.get_all_pages()
    pages_by_slug = {p["slug"]: p for p in ghost_pages}

    for filename, target_slug in MANAGED_PAGES.items():
        source = PAGES_DIR / filename
        if not source.exists():
            print(f"  warning: {source} not found, skipping", file=sys.stderr)
            continue

        raw = source.read_text()
        rendered_md = ts.render_text(raw, data, variables)
        content_hash = hashlib.sha256(rendered_md.encode()).hexdigest()[:16]

        existing = pages_by_slug.get(target_slug)

        if existing and not force:
            existing_hash = get_existing_hash(existing)
            if existing_hash == content_hash:
                print(f"  skip  {target_slug} (unchanged)")
                continue

        # Extract title from first heading
        title_match = re.search(r"^#\s+(.+)", rendered_md, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else filename.replace(".md", "").title()

        html = _md_to_html(rendered_md)

        page_data = {
            "title": title,
            "html": html,
            "status": "published",
            "codeinjection_head": f"<!-- perihelion-hash:{content_hash} -->",
        }

        if existing:
            page_data["updated_at"] = existing["updated_at"]
            api.update_page_html(existing["id"], page_data)
            print(f"  update  {target_slug}")
        else:
            print(f"  warning: Ghost page '{target_slug}' not found, skipping", file=sys.stderr)

    # Clean up any stale posts with managed-page slugs (from earlier bugs)
    managed_slugs = set(MANAGED_PAGES.values())
    all_posts = api.get_all_posts()
    for post in all_posts:
        if post["slug"] in managed_slugs:
            try:
                api.delete_post(post["id"])
                print(f"  delete  post/{post['slug']} (stale, now a page)")
            except Exception as e:
                print(f"  ERROR deleting post/{post['slug']}: {e}", file=sys.stderr)


# ── CLI ──────────────────────────────────────────────────────────────────────

def load_chapters() -> list[ManuscriptChapter]:
    """Load and sort all manuscript chapters."""
    md_files = sorted(MANUSCRIPT_DIR.glob("*.md"))
    md_files = [f for f in md_files if f.name != "INDEX.md"]

    chapters = []
    for f in md_files:
        try:
            chapters.append(parse_manuscript_file(f))
        except Exception as e:
            print(f"  warning: skipping {f.name}: {e}", file=sys.stderr)

    chapters.sort(key=lambda c: (c.sort_order, c.filepath.name))
    return chapters


def dry_run(chapters: list[ManuscriptChapter]):
    """Show what would be published without making any API calls."""
    print(f"Found {len(chapters)} manuscript files:\n")

    total_words = 0
    for ch in chapters:
        word_count = len(ch.rendered_md.split())
        total_words += word_count

        is_epigraph = ch.slug == "epigraph"
        tags = []
        if not is_epigraph:
            tags.append("chapter")
            if ch.chapter_number:
                tags.append(f"ch-{ch.chapter_number:02d}")

        label = f"Chapter {ch.chapter_number}" if ch.chapter_number else ch.chapter_type.title() or "Front Matter"

        print(f"  {ch.filepath.name}")
        print(f"    {label}: {ch.title}")
        print(f"    slug: {ch.slug}")
        print(f"    tags: {', '.join(tags)}")
        print(f"    words: {word_count:,}")
        print(f"    hash: {ch.content_hash}")
        print()

    print(f"Total: {len(chapters)} files, {total_words:,} words")
    print(f"\nRun with --publish to push to Ghost.")


def main():
    import os

    parser = argparse.ArgumentParser(
        description="Publish Perihelion chapters to Ghost"
    )
    parser.add_argument(
        "--publish", action="store_true",
        help="Actually publish to Ghost (default is dry-run)"
    )
    parser.add_argument(
        "--force", action="store_true",
        help="Update all posts even if content hash hasn't changed"
    )
    args = parser.parse_args()

    chapters = load_chapters()
    if not chapters:
        print("No manuscript files found.")
        return

    if not args.publish:
        dry_run(chapters)
        return

    # Publishing mode — require env vars
    ghost_url = os.environ.get("GHOST_URL")
    api_key = os.environ.get("GHOST_ADMIN_API_KEY")

    if not ghost_url or not api_key:
        print("Error: GHOST_URL and GHOST_ADMIN_API_KEY environment variables are required.", file=sys.stderr)
        print("  export GHOST_URL='https://your-site.ghost.io'", file=sys.stderr)
        print("  export GHOST_ADMIN_API_KEY='id:secret'", file=sys.stderr)
        sys.exit(1)

    print(f"Publishing to {ghost_url}...")
    publish_chapters(chapters, ghost_url, api_key, force=args.force)

    print("\nSyncing pages...")
    sync_pages(ghost_url, api_key, force=args.force)


if __name__ == "__main__":
    main()
