# Real Life Patch Notes: The Comedy Changelog

![make.fun](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d.svg)
![rank](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d/rank.svg)
![reward](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d/reward.svg)

One line, at most 160 characters: a software patch note for a bug in real
life or human biology, in the terse register of a real release note.

## Entry

```
v2.0.3: fixed a bug where the legs walked into a room and immediately forgot why they were there.
```

## How it works

`main.py` (stdlib only) copies the stored line from `entry.txt` to
`$MAKEFUN_OUTPUT_DIR/entry.txt`. No network, no fonts, no dependencies.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
