#!/usr/bin/env python3
"""Real Life Patch Notes: The Comedy Changelog.

Writes the single-line patch note stored in entry.txt to
$MAKEFUN_OUTPUT_DIR/entry.txt. Stdlib only, no network, no I/O
outside the output directory.
"""

import os
import sys

ENTRY_FILE = "entry.txt"
MAX_CHARS = 160


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, ENTRY_FILE), "r", encoding="utf-8") as f:
        raw = f.read()

    # Gate: exactly one line. Any embedded newline/CR means the stored
    # entry is not a single line, even if strip() would hide it.
    body = raw.strip()
    if "\n" in body or "\r" in body:
        print(
            "error: entry must be exactly one line, found embedded newline",
            file=sys.stderr,
        )
        return 1
    if not body:
        print("error: entry is empty or only whitespace", file=sys.stderr)
        return 1
    if len(body) > MAX_CHARS:
        print(
            "error: entry is %d characters, over the 160 limit" % len(body),
            file=sys.stderr,
        )
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print(
            "error: MAKEFUN_OUTPUT_DIR is not set; refusing to write anywhere",
            file=sys.stderr,
        )
        return 1
    if not os.path.isdir(out_dir):
        print(
            "error: MAKEFUN_OUTPUT_DIR %r does not exist or is not a directory"
            % out_dir,
            file=sys.stderr,
        )
        return 1

    out_path = os.path.join(out_dir, "entry.txt")
    payload = (body + "\n").encode("utf-8")
    with open(out_path, "wb") as f:
        f.write(payload)

    # Verify the write round-trips byte for byte before reporting success.
    with open(out_path, "rb") as f:
        written = f.read()
    if written != payload:
        print("error: wrote %d bytes but read back %d" % (len(payload), len(written)),
              file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
