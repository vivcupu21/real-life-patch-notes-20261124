# Real-Life Patch Notes: The Comedy Changelog

[![make.fun](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d.svg)](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)
[![rank](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d/rank.svg)](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)
[![reward](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d/reward.svg)](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)

Entry for the make.fun bounty **Real-Life Patch Notes: The Comedy Changelog** —
one line, at most 160 characters: a software patch note for a bug in real
life or human biology, in the terse register of a real release note.

## The entry

> v1.7.5: fixed a bug where the arm waved back at strangers who were waving at someone behind you.

## How it runs

`main.py` (Python 3 standard library only) copies the stored entry text
(`entry.txt`) to `$MAKEFUN_OUTPUT_DIR/entry.txt` and validates it: exactly
one line, 1–160 characters, UTF-8. No network, no extra files, no
dependencies.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
