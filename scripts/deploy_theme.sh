#!/usr/bin/env bash
#
# Deploy the perihelion-theme to Ghost via the Admin API.
#
# Zips the theme, uploads it, and activates it — works on both
# Ghost Cloud (ghost.io) and self-hosted instances.
#
# Required environment variables:
#   GHOST_URL             - e.g. https://perihelion.ghost.io
#   GHOST_ADMIN_API_KEY   - format: key_id:secret_hex
#
# Usage:
#   ./scripts/deploy_theme.sh              # upload + activate
#   ./scripts/deploy_theme.sh --zip-only   # just create the zip

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
THEME_DIR="$REPO_ROOT/perihelion-theme"
ZIP_PATH="/tmp/perihelion-theme.zip"

# ── Build zip ────────────────────────────────────────────────────────────────

echo "Zipping theme..."
rm -f "$ZIP_PATH"
(cd "$THEME_DIR" && zip -r "$ZIP_PATH" . -x "README.md" -x "*.zip" -x ".DS_Store") > /dev/null
echo "  Created $ZIP_PATH ($(du -h "$ZIP_PATH" | cut -f1))"

if [[ "${1:-}" == "--zip-only" ]]; then
    echo "Done (zip only)."
    exit 0
fi

# ── Validate env ─────────────────────────────────────────────────────────────

if [[ -z "${GHOST_URL:-}" || -z "${GHOST_ADMIN_API_KEY:-}" ]]; then
    echo "Error: GHOST_URL and GHOST_ADMIN_API_KEY must be set." >&2
    echo "  export GHOST_URL='https://your-site.ghost.io'" >&2
    echo "  export GHOST_ADMIN_API_KEY='id:secret'" >&2
    exit 1
fi

GHOST_URL="${GHOST_URL%/}"

# ── Generate JWT ─────────────────────────────────────────────────────────────

TOKEN=$(python3 -c "
import hmac, json, time, base64, sys

api_key = '$GHOST_ADMIN_API_KEY'
key_id, secret_hex = api_key.split(':')
secret = bytes.fromhex(secret_hex)

header = base64.urlsafe_b64encode(
    json.dumps({'alg': 'HS256', 'typ': 'JWT', 'kid': key_id}).encode()
).rstrip(b'=')

now = int(time.time())
payload = base64.urlsafe_b64encode(
    json.dumps({'iat': now, 'exp': now + 300, 'aud': '/admin/'}).encode()
).rstrip(b'=')

signing_input = header + b'.' + payload
signature = base64.urlsafe_b64encode(
    hmac.new(secret, signing_input, 'sha256').digest()
).rstrip(b'=')

print((signing_input + b'.' + signature).decode())
")

# ── Upload theme ─────────────────────────────────────────────────────────────

echo "Uploading theme to $GHOST_URL..."
UPLOAD_RESPONSE=$(curl -s -w "\n%{http_code}" \
    -X POST "$GHOST_URL/ghost/api/admin/themes/upload/" \
    -H "Authorization: Ghost $TOKEN" \
    -F "file=@$ZIP_PATH;type=application/zip")

HTTP_CODE=$(echo "$UPLOAD_RESPONSE" | tail -1)
BODY=$(echo "$UPLOAD_RESPONSE" | sed '$d')

if [[ "$HTTP_CODE" -ge 200 && "$HTTP_CODE" -lt 300 ]]; then
    THEME_NAME=$(echo "$BODY" | python3 -c "import sys,json; print(json.load(sys.stdin)['themes'][0]['name'])" 2>/dev/null || echo "perihelion-theme")
    echo "  Uploaded: $THEME_NAME (HTTP $HTTP_CODE)"
else
    echo "  Upload failed (HTTP $HTTP_CODE):" >&2
    echo "$BODY" | python3 -m json.tool 2>/dev/null || echo "$BODY" >&2
    exit 1
fi

# ── Activate theme ───────────────────────────────────────────────────────────

# Regenerate token (upload may have taken a moment)
TOKEN=$(python3 -c "
import hmac, json, time, base64
api_key = '$GHOST_ADMIN_API_KEY'
key_id, secret_hex = api_key.split(':')
secret = bytes.fromhex(secret_hex)
header = base64.urlsafe_b64encode(json.dumps({'alg': 'HS256', 'typ': 'JWT', 'kid': key_id}).encode()).rstrip(b'=')
now = int(time.time())
payload = base64.urlsafe_b64encode(json.dumps({'iat': now, 'exp': now + 300, 'aud': '/admin/'}).encode()).rstrip(b'=')
signing_input = header + b'.' + payload
signature = base64.urlsafe_b64encode(hmac.new(secret, signing_input, 'sha256').digest()).rstrip(b'=')
print((signing_input + b'.' + signature).decode())
")

echo "Activating theme..."
ACTIVATE_RESPONSE=$(curl -s -w "\n%{http_code}" \
    -X PUT "$GHOST_URL/ghost/api/admin/themes/$THEME_NAME/activate/" \
    -H "Authorization: Ghost $TOKEN" \
    -H "Content-Type: application/json")

HTTP_CODE=$(echo "$ACTIVATE_RESPONSE" | tail -1)
BODY=$(echo "$ACTIVATE_RESPONSE" | sed '$d')

if [[ "$HTTP_CODE" -ge 200 && "$HTTP_CODE" -lt 300 ]]; then
    echo "  Theme '$THEME_NAME' is now active."
else
    echo "  Activation failed (HTTP $HTTP_CODE):" >&2
    echo "$BODY" | python3 -m json.tool 2>/dev/null || echo "$BODY" >&2
    exit 1
fi

echo "Done. Theme deployed to $GHOST_URL"
