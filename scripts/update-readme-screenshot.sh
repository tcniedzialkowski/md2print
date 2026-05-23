#!/usr/bin/env bash
set -euo pipefail

# Regenerate the README screenshot from md2print's current README-rendered HTML.
# This captures self-contained HTML opened in Chrome; it does not create PDF output.

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PYTHON_BIN="${PYTHON:-python}"
OUTPUT_PATH="$ROOT_DIR/docs/readme-output-screenshot.png"

# Use a temporary directory so generated HTML does not pollute the repository.
TMP_DIR="$(mktemp -d)"
cleanup() {
  rm -rf "$TMP_DIR"
}
trap cleanup EXIT

SOURCE_PATH="$TMP_DIR/readme-source.md"
HTML_PATH="$TMP_DIR/readme.html"

# Strip this screenshot's own README block before rendering so regeneration does not recurse.
"$PYTHON_BIN" - <<'PY' "$ROOT_DIR/README.md" "$SOURCE_PATH"
from pathlib import Path
import re
import sys

source = Path(sys.argv[1]).read_text(encoding="utf-8")
source = re.sub(
    r"<!-- README_SCREENSHOT_START -->.*?<!-- README_SCREENSHOT_END -->\n?",
    "",
    source,
    flags=re.DOTALL,
)
Path(sys.argv[2]).write_text(source, encoding="utf-8")
PY

# Render the current README-derived source through the local md2print package with default settings.
# No --meta flag is passed, so the metadata banner remains off.
cd "$ROOT_DIR"
"$PYTHON_BIN" -m md2print "$SOURCE_PATH" --output "$HTML_PATH" --force

# Find Chrome/Chromium. CHROME_BIN can be set by CI or a developer shell.
CHROME_BIN="${CHROME_BIN:-}"
if [[ -z "$CHROME_BIN" ]]; then
  if command -v google-chrome >/dev/null 2>&1; then
    CHROME_BIN="$(command -v google-chrome)"
  elif command -v chromium >/dev/null 2>&1; then
    CHROME_BIN="$(command -v chromium)"
  elif command -v chromium-browser >/dev/null 2>&1; then
    CHROME_BIN="$(command -v chromium-browser)"
  elif [[ -x "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" ]]; then
    CHROME_BIN="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
  elif [[ -x "/Applications/Chromium.app/Contents/MacOS/Chromium" ]]; then
    CHROME_BIN="/Applications/Chromium.app/Contents/MacOS/Chromium"
  else
    echo "Could not find Chrome or Chromium. Set CHROME_BIN to the browser executable." >&2
    exit 1
  fi
fi

# Convert the generated HTML path to a file:// URL that Chrome can open reliably.
FILE_URL="$($PYTHON_BIN -c 'from pathlib import Path; import sys; print(Path(sys.argv[1]).resolve().as_uri())' "$HTML_PATH")"

# Capture the top of the generated HTML at a stable browser viewport.
# The viewport is intentionally wider than Letter paper so the CSS page shadow is visible.
"$CHROME_BIN" \
  --headless=new \
  --disable-gpu \
  --disable-dev-shm-usage \
  --no-sandbox \
  --hide-scrollbars \
  --window-size=1100,1400 \
  --screenshot="$OUTPUT_PATH" \
  "$FILE_URL"

echo "Updated $OUTPUT_PATH"
