#!/usr/bin/env python3
"""Write the coined-word entry to entry.txt.

The entry is a single deterministic line. It is validated to be
1-140 characters and not only whitespace before anything is written.
"""

import os
import sys
from pathlib import Path

ENTRY_TEXT = "pocketpat — the panicked patting of your pockets for a phone already in your hand"


def main() -> int:
    text = ENTRY_TEXT
    if not text.strip() or not 1 <= len(text) <= 140:
        print("entry text must be 1-140 non-whitespace characters", file=sys.stderr)
        return 1

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
