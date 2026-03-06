"""
Publish chapters to Ghost (https://perihelion.ghost.io) via the Admin API.

Reuses parse_chapter() from config.py for chapter discovery and rendering.
Idempotent: creates missing posts, updates changed posts, skips unchanged.

PR preview mode (--draft --slug-prefix pr-42- --pr-tag pr-42):
  Publishes chapters as Ghost drafts with prefixed slugs and a PR tag.
  Drafts are invisible to public readers but previewable in Ghost admin.

Cleanup mode (--cleanup-tag pr-42):
  Deletes all Ghost posts tagged with the given tag, then exits.

Requires env vars:
  GHOST_API_URL       — e.g. https://perihelion.ghost.io
  GHOST_ADMIN_API_KEY — id:secret hex pair from Ghost Admin → Integrations
"""

import argparse
import base64
import hashlib
import hmac
import json
import os
import re
import struct
import sys
import time
from pathlib import Path

import requests

# Allow running from repo root or from publishing/
sys.path.insert(0, str(Path(__file__).resolve().parent))

from config import MANUSCRIPT_DIR, parse_chapter  # noqa: E402

# Base epoch for published_at ordering — chapters get sequential timestamps
# 2037-01-01T00:00:00Z (arbitrary future date in the story's era)
_ORDERING_EPOCH = "2037-01-01T00:00:00.000Z"

# Regex to extract content_hash from codeinjection_foot
_HASH_RE = re.compile(r"<!-- content_hash:(\w+) -->")


# ---------------------------------------------------------------------------
# JWT auth (HMAC-SHA256, no PyJWT needed)
# ---------------------------------------------------------------------------

def _b64url(data: bytes) -> str:
    """Base64url-encode without padding."""
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode()


def make_jwt(api_key: str, api_url: str) -> str:
    """Create a Ghost Admin API JWT token (5-minute expiry)."""
    kid, secret_hex = api_key.split(":")
    secret = bytes.fromhex(secret_hex)

    now = int(time.time())
    header = {"alg": "HS256", "typ": "JWT", "kid": kid}
    payload = {
        "iat": now,
        "exp": now + 300,
        "aud": "/admin/",
    }

    segments = _b64url(json.dumps(header).encode()) + "." + _b64url(json.dumps(payload).encode())
    signature = hmac.new(secret, segments.encode(), hashlib.sha256).digest()
    return segments + "." + _b64url(signature)


# ---------------------------------------------------------------------------
# Ghost API helpers
# ---------------------------------------------------------------------------

_session = requests.Session()
_api_url = ""
_api_key = ""


def _init_client():
    global _api_url, _api_key
    _api_url = os.environ["GHOST_API_URL"].rstrip("/")
    _api_key = os.environ["GHOST_ADMIN_API_KEY"]


def ghost_request(method: str, path: str, **kwargs) -> requests.Response:
    """Make an authenticated request to the Ghost Admin API."""
    token = make_jwt(_api_key, _api_url)
    url = f"{_api_url}/ghost/api/admin/{path}"
    headers = kwargs.pop("headers", {})
    headers["Authorization"] = f"Ghost {token}"
    resp = _session.request(method, url, headers=headers, **kwargs)
    if not resp.ok and resp.status_code != 404:
        print(f"  Ghost API error {resp.status_code}: {resp.text[:500]}")
    resp.raise_for_status()
    return resp


def get_post_by_slug(slug: str, *, include_drafts: bool = False) -> dict | None:
    """Fetch an existing Ghost post by slug, or None if not found."""
    try:
        params = f"posts/slug/{slug}/"
        if include_drafts:
            params += "?filter=status:draft,status:published"
        resp = ghost_request("GET", params)
        data = resp.json()
        posts = data.get("posts", [])
        return posts[0] if posts else None
    except requests.HTTPError as e:
        if e.response.status_code == 404:
            return None
        raise


def get_all_posts(include_drafts: bool = False) -> list:
    """Fetch all Ghost posts (paginated)."""
    posts = []
    page = 1
    status_filter = "status:published,status:draft" if include_drafts else ""
    while True:
        params = f"limit=50&page={page}&include=tags"
        if status_filter:
            params += f"&filter={status_filter}"
        resp = ghost_request("GET", f"posts/?{params}")
        data = resp.json()
        posts.extend(data.get("posts", []))
        meta = data.get("meta", {}).get("pagination", {})
        if page >= meta.get("pages", 1):
            break
        page += 1
    return posts


def delete_post(post_id: str) -> None:
    """Delete a Ghost post by ID."""
    ghost_request("DELETE", f"posts/{post_id}/")


def _hash_marker(content_hash: str) -> str:
    """HTML comment storing content_hash for change detection."""
    return f"<!-- content_hash:{content_hash} -->"


def _extract_hash(post: dict) -> str | None:
    """Extract content_hash from a Ghost post's codeinjection_foot."""
    foot = post.get("codeinjection_foot") or ""
    m = _HASH_RE.search(foot)
    return m.group(1) if m else None


def _published_at(position: int) -> str:
    """Generate a published_at timestamp for ordering.

    Each chapter gets a timestamp 1 minute after the previous one,
    starting from _ORDERING_EPOCH. This keeps Ghost's default sort
    (newest-first) matching our reading order when reversed.
    """
    # Parse the epoch and add position * 60 seconds
    # We'll use a simple approach: just format with minute offsets
    # Ghost wants ISO 8601: 2037-01-01T00:01:00.000Z
    minutes = position
    hours, mins = divmod(minutes, 60)
    return f"2037-01-01T{hours:02d}:{mins:02d}:00.000Z"


# ---------------------------------------------------------------------------
# Create / Update
# ---------------------------------------------------------------------------

def _ghost_tags(chapter) -> list[dict]:
    """Build the Ghost tag list for a chapter.

    The theme expects:
      - Tag 1: "chapter" (used by index.hbs to build the TOC)
      - Tag 2: "Chapter N" (used by chapter-card.hbs for the label)
    The epigraph is fetched by slug, not by tag, so it skips the chapter tag.
    """
    tags = []
    is_epigraph = chapter.slug == "epigraph"

    if not is_epigraph:
        tags.append({"name": "chapter"})
        if chapter.chapter_number:
            tags.append({"name": f"Chapter {chapter.chapter_number}"})

    # Append the default metadata tags
    tags.extend({"name": t} for t in chapter.tags)
    return tags


def create_post(chapter, position: int, *, status: str = "published",
                 slug_prefix: str = "", extra_tags: list[dict] | None = None) -> dict:
    """Create a new Ghost post from a Chapter."""
    slug = slug_prefix + chapter.slug
    tags = _ghost_tags(chapter) + (extra_tags or [])
    post_data = {
        "title": chapter.title,
        "slug": slug,
        "html": chapter.content_html,
        "status": status,
        "codeinjection_foot": _hash_marker(chapter.content_hash),
        "tags": tags,
    }
    if status == "published":
        post_data["published_at"] = _published_at(position)
    body = {"posts": [post_data]}
    resp = ghost_request("POST", "posts/?source=html", json=body)
    return resp.json()["posts"][0]


def update_post(post_id: str, chapter, updated_at: str, *,
                extra_tags: list[dict] | None = None) -> dict:
    """Update an existing Ghost post with new content."""
    tags = _ghost_tags(chapter) + (extra_tags or [])
    body = {
        "posts": [{
            "html": chapter.content_html,
            "title": chapter.title,
            "codeinjection_foot": _hash_marker(chapter.content_hash),
            "updated_at": updated_at,
            "tags": tags,
        }]
    }
    resp = ghost_request("PUT", f"posts/{post_id}/?source=html", json=body)
    return resp.json()["posts"][0]


def _needs_tag_update(existing: dict, chapter) -> bool:
    """Check if the remote post is missing expected tags."""
    remote_tags = {t["name"] for t in existing.get("tags", [])}
    is_epigraph = chapter.slug == "epigraph"
    if not is_epigraph and "chapter" not in remote_tags:
        return True
    if chapter.chapter_number and f"Chapter {chapter.chapter_number}" not in remote_tags:
        return True
    return False


def sync_chapter(chapter, position: int, *, status: str = "published",
                 slug_prefix: str = "", extra_tags: list[dict] | None = None) -> tuple[str, dict | None]:
    """Idempotent sync: create, update, or skip a single chapter.

    Returns: (action, post_data) where action is 'created', 'updated', or 'skipped'.
    """
    slug = slug_prefix + chapter.slug
    is_draft = status == "draft"
    existing = get_post_by_slug(slug, include_drafts=is_draft)

    if existing is None:
        post = create_post(chapter, position, status=status,
                           slug_prefix=slug_prefix, extra_tags=extra_tags)
        return "created", post

    remote_hash = _extract_hash(existing)
    if remote_hash == chapter.content_hash and not _needs_tag_update(existing, chapter):
        return "skipped", existing

    post = update_post(existing["id"], chapter, existing["updated_at"],
                       extra_tags=extra_tags)
    return "updated", post


# ---------------------------------------------------------------------------
# Cleanup by tag
# ---------------------------------------------------------------------------

def cleanup_by_tag(tag_name: str) -> int:
    """Delete all Ghost posts that carry the given tag. Returns count deleted."""
    all_posts = get_all_posts(include_drafts=True)
    deleted = 0
    for post in all_posts:
        post_tags = {t["name"] for t in post.get("tags", [])}
        if tag_name in post_tags:
            try:
                delete_post(post["id"])
                print(f"  {'deleted':8s}  {post['slug']}")
                deleted += 1
            except Exception as e:
                print(f"  ERROR     deleting {post['slug']}: {e}")
    return deleted


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def parse_args(argv=None):
    parser = argparse.ArgumentParser(description="Sync chapters to Ghost CMS")
    parser.add_argument("--draft", action="store_true",
                        help="Publish as drafts instead of published posts")
    parser.add_argument("--slug-prefix", default="",
                        help="Prefix for all post slugs (e.g. 'pr-42-')")
    parser.add_argument("--pr-tag", default="",
                        help="Extra tag added to all posts (e.g. 'pr-42')")
    parser.add_argument("--cleanup-tag", default="",
                        help="Delete all posts with this tag, then exit")
    parser.add_argument("--preview-urls", default="",
                        help="Write JSON manifest of preview URLs to this path")
    parser.add_argument("--files", nargs="*", default=None,
                        help="Only process these manuscript files (paths relative to repo root)")
    return parser.parse_args(argv)


def main():
    args = parse_args()
    _init_client()

    # Cleanup mode: delete all posts with the given tag and exit
    if args.cleanup_tag:
        print(f"Cleaning up Ghost posts tagged '{args.cleanup_tag}'...")
        deleted = cleanup_by_tag(args.cleanup_tag)
        print(f"Done: {deleted} deleted")
        return

    # Discover and parse chapters (same logic as build_site.py)
    if args.files:
        REPO_ROOT = Path(__file__).resolve().parent.parent
        md_files = [REPO_ROOT / f for f in args.files]
    else:
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

    chapters.sort(key=lambda c: (c.sort_order, c.filename))

    status = "draft" if args.draft else "published"
    extra_tags = [{"name": args.pr_tag}] if args.pr_tag else None
    mode_label = f"as drafts (prefix={args.slug_prefix!r})" if args.draft else ""
    print(f"Syncing {len(chapters)} chapters to Ghost {mode_label}...")

    created = updated = skipped = errors = 0
    preview_manifest = []
    for i, ch in enumerate(chapters):
        slug_display = args.slug_prefix + ch.slug
        try:
            result, post_data = sync_chapter(ch, i, status=status,
                                             slug_prefix=args.slug_prefix,
                                             extra_tags=extra_tags)
            print(f"  {result:8s}  {slug_display}")
            if result == "created":
                created += 1
            elif result == "updated":
                updated += 1
            else:
                skipped += 1
            if post_data and post_data.get("uuid"):
                preview_manifest.append({
                    "title": ch.title,
                    "slug": slug_display,
                    "chapter_number": ch.chapter_number,
                    "uuid": post_data["uuid"],
                    "preview_url": f"{_api_url}/p/{post_data['uuid']}/",
                })
        except Exception as e:
            print(f"  ERROR     {slug_display}: {e}")
            errors += 1

    if args.preview_urls and preview_manifest:
        Path(args.preview_urls).write_text(json.dumps(preview_manifest, indent=2))
        print(f"Preview manifest written to {args.preview_urls}")

    # Cleanup stale posts — only in production mode (no slug prefix)
    deleted = 0
    if not args.slug_prefix:
        current_slugs = {ch.slug for ch in chapters}
        all_posts = get_all_posts()
        for post in all_posts:
            post_tags = {t["name"] for t in post.get("tags", [])}
            is_managed = "chapter" in post_tags or post["slug"] == "epigraph"
            if is_managed and post["slug"] not in current_slugs:
                try:
                    delete_post(post["id"])
                    print(f"  {'deleted':8s}  {post['slug']} (stale)")
                    deleted += 1
                except Exception as e:
                    print(f"  ERROR     deleting {post['slug']}: {e}")
                    errors += 1

    print(f"\nDone: {created} created, {updated} updated, {skipped} skipped, {deleted} deleted, {errors} errors")
    if errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
