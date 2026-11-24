#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog.

Writes the entry (one patch-note line, at most 160 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt. Standard library only, no network,
no files besides the entry text shipped next to this script.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.txt")


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.txt")
    shutil.copyfile(SOURCE, dest)
    with open(dest, "r", encoding="utf-8") as f:
        text = f.read()
    stripped = text.strip()
    if not 1 <= len(stripped) <= 160:
        print("entry must be 1-160 characters, got %d" % len(stripped),
              file=sys.stderr)
        return 1
    if "\n" in stripped:
        print("entry must be a single line", file=sys.stderr)
        return 1
    print("wrote %d characters to %s" % (len(stripped), dest))
    return 0


if __name__ == "__main__":
    sys.exit(main())
