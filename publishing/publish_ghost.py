"""
Publish chapters to Ghost (https://perihelion.ghost.io) via the Admin API.

Reuses parse_chapter() from config.py for chapter discovery and rendering.
Idempotent: creates missing posts, updates changed posts, skips unchanged.

Requires env vars:
  GHOST_API_URL       — e.g. https://perihelion.ghost.io
  GHOST_ADMIN_API_KEY — id:secret hex pair from Ghost Admin → Integrations
"""

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
    if not resp.ok:
        print(f"  Ghost API error {resp.status_code}: {resp.text[:500]}")
    resp.raise_for_status()
    return resp


def get_post_by_slug(slug: str) -> dict | None:
    """Fetch an existing Ghost post by slug, or None if not found."""
    try:
        resp = ghost_request("GET", f"posts/slug/{slug}/")
        data = resp.json()
        posts = data.get("posts", [])
        return posts[0] if posts else None
    except requests.HTTPError as e:
        if e.response.status_code == 404:
            return None
        raise


def get_all_posts() -> list:
    """Fetch all Ghost posts (paginated)."""
    posts = []
    page = 1
    while True:
        resp = ghost_request("GET", f"posts/?limit=50&page={page}&include=tags")
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


def create_post(chapter, position: int) -> dict:
    """Create a new Ghost post from a Chapter."""
    body = {
        "posts": [{
            "title": chapter.title,
            "slug": chapter.slug,
            "html": chapter.content_html,
            "status": "published",
            "published_at": _published_at(position),
            "codeinjection_foot": _hash_marker(chapter.content_hash),
            "tags": _ghost_tags(chapter),
        }]
    }
    resp = ghost_request("POST", "posts/?source=html", json=body)
    return resp.json()["posts"][0]


def update_post(post_id: str, chapter, updated_at: str) -> dict:
    """Update an existing Ghost post with new content."""
    body = {
        "posts": [{
            "html": chapter.content_html,
            "title": chapter.title,
            "codeinjection_foot": _hash_marker(chapter.content_hash),
            "updated_at": updated_at,
            "tags": _ghost_tags(chapter),
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


def sync_chapter(chapter, position: int) -> str:
    """Idempotent sync: create, update, or skip a single chapter.

    Returns: 'created', 'updated', or 'skipped'.
    """
    existing = get_post_by_slug(chapter.slug)

    if existing is None:
        create_post(chapter, position)
        return "created"

    remote_hash = _extract_hash(existing)
    if remote_hash == chapter.content_hash and not _needs_tag_update(existing, chapter):
        return "skipped"

    update_post(existing["id"], chapter, existing["updated_at"])
    return "updated"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    _init_client()

    # Discover and parse chapters (same logic as build_site.py)
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
    print(f"Syncing {len(chapters)} chapters to Ghost...")

    created = updated = skipped = errors = 0
    for i, ch in enumerate(chapters):
        try:
            result = sync_chapter(ch, i)
            print(f"  {result:8s}  {ch.slug}")
            if result == "created":
                created += 1
            elif result == "updated":
                updated += 1
            else:
                skipped += 1
        except Exception as e:
            print(f"  ERROR     {ch.slug}: {e}")
            errors += 1

    # Cleanup: delete Ghost posts that no longer match any manuscript slug
    current_slugs = {ch.slug for ch in chapters}
    all_posts = get_all_posts()
    deleted = 0
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
