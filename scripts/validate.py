#!/usr/bin/env python3
"""Static validation checks for the single-page CyberShield OS demo."""
from __future__ import annotations

import re
import subprocess
import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "index.html"
TMP_JS = ROOT / ".tmp-index-check.js"


class Parser(HTMLParser):
    pass


def main() -> int:
    text = HTML.read_text(encoding="utf-8")
    Parser().feed(text)

    ids = re.findall(r'id="([^"]+)"', text)
    duplicate_ids = [name for name, count in Counter(ids).items() if count > 1]
    if duplicate_ids:
        print(f"Duplicate ids found: {', '.join(sorted(duplicate_ids))}", file=sys.stderr)
        return 1

    referenced_ids = set(re.findall(r"getElementById\(['\"]([^'\"]+)['\"]\)", text))
    missing_ids = sorted(referenced_ids - set(ids))
    if missing_ids:
        print(f"Missing elements referenced by getElementById: {', '.join(missing_ids)}", file=sys.stderr)
        return 1

    match = re.search(r"<script>(.*)</script>", text, re.DOTALL)
    if not match:
        print("No inline script block found", file=sys.stderr)
        return 1

    try:
        TMP_JS.write_text(match.group(1), encoding="utf-8")
        subprocess.run(["node", "--check", str(TMP_JS)], check=True, cwd=ROOT)
    finally:
        TMP_JS.unlink(missing_ok=True)

    print("HTML ids and inline JavaScript syntax validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
