# Perihelion Ghost Theme

A dark, reading-focused Ghost theme for the Perihelion serial novel. Designed for distraction-free long-form prose with a warm solar accent on a deep dark background.

## Installation

1. In the `perihelion-theme/` directory, create a zip file:
   ```bash
   cd perihelion-theme
   zip -r perihelion-theme.zip . -x "README.md" -x "*.zip"
   ```
2. In Ghost Admin, go to **Settings > Design > Change theme > Upload theme**
3. Upload `perihelion-theme.zip` and activate it

## Ghost Configuration

### Site Settings

- **Title**: "Perihelion" (or your preferred title)
- **Description**: Used as the tagline on the landing page (e.g., "// SIGNAL LOST -- AUTONOMOUS PROTOCOLS ACTIVE")

### Navigation

In Ghost Admin > Settings > Navigation, add links as needed:

| Label   | URL    |
|---------|--------|
| About   | /about |

The home link is built into the theme header.

## Chapter Tagging Convention

The theme uses Ghost tags to identify and order chapters:

### Required Tags

- **`chapter`** — Applied to every chapter post. The home page queries for posts with this tag and displays them in ascending chronological order (oldest first = chapter 1 at top).
- **`ch-XX`** — A secondary tag indicating the chapter number (e.g., `ch-01`, `ch-02`, ..., `ch-20`). The theme displays the tag's **name** (not slug), so create these tags with display names like "Chapter 1", "Chapter 2", etc.

### How It Works

1. A post tagged `chapter` + `ch-03` (name: "Chapter 3") appears in the table of contents
2. The chapter number label is pulled from the `ch-XX` tag's display name
3. Posts **without** the `chapter` tag do not appear in the chapter list — they show in a separate "Updates" section on the home page

### Previous/Next Navigation

Ghost's `{{prev_post}}` and `{{next_post}}` helpers navigate by `published_at` date within posts tagged `chapter`. To maintain correct reading order, **publish chapters in chronological order** (chapter 1 first, chapter 2 second, etc.).

## Publishing Script

The `scripts/publish.py` script automates publishing from manuscript source files to Ghost.

### Setup

The script uses only Python stdlib — no additional dependencies needed.

Set environment variables:
```bash
export GHOST_URL='https://your-site.ghost.io'
export GHOST_ADMIN_API_KEY='your-key-id:your-secret'
```

To get an Admin API key:
1. Ghost Admin > Settings > Integrations > Add custom integration
2. Copy the **Admin API Key** (format: `id:secret`)

### Usage

```bash
# Dry run — see what would be published
python3 scripts/publish.py

# Publish to Ghost (creates new posts, updates changed ones)
python3 scripts/publish.py --publish

# Force update all posts (even if content hasn't changed)
python3 scripts/publish.py --publish --force
```

### How It Works

1. Reads all `*.md` files from `manuscript/` (excluding `INDEX.md`)
2. Resolves `{event_id}` timestamp placeholders using `tracking/timestamps.json`
3. Parses filenames to extract chapter numbers, stations, and types
4. Generates slugs matching the pattern `ch01-title`, `ch02-title`, etc.
5. Creates Ghost posts with:
   - The `chapter` tag for filtering
   - A `ch-XX` tag (with name "Chapter X") for display
   - Content as mobiledoc/markdown
   - A content hash in `codeinjection_head` for change detection
6. On subsequent runs, only posts with changed content are updated (idempotent by slug)

## Theme Structure

```
perihelion-theme/
├── package.json         # Ghost theme manifest
├── default.hbs          # Base layout (head, fonts, body wrapper)
├── index.hbs            # Home page with TOC and updates
├── post.hbs             # Chapter reading view
├── page.hbs             # Static pages (About, etc.)
├── tag.hbs              # Tag archive
├── author.hbs           # Author page
├── partials/
│   ├── header.hbs       # Sticky navigation header
│   ├── footer.hbs       # Site footer
│   ├── chapter-nav.hbs  # Prev / Contents / Next navigation
│   └── chapter-card.hbs # Single chapter entry in TOC
└── assets/
    ├── css/
    │   └── style.css    # All theme styles (dark mode, typography)
    └── js/
        └── progress.js  # Reading progress bar
```

## Design Notes

- **Dark mode only** — background `#0d1117`, text `#c9d1d9`
- **Accent color** — warm solar orange/amber `#e8913a`
- **Body font** — Lora (serif) for reading comfort
- **UI font** — Inter (sans-serif) for navigation and metadata
- **Mono font** — JetBrains Mono for code blocks and labels
- **Max reading width** — 680px with 1.75 line height
- **Progress bar** — subtle amber bar at the top of chapter pages showing scroll progress
