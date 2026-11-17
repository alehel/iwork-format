# 0387: Writing *same as previous section*

**Status:** run

Each section (type 10011) names its own header-and-footer sets, in fields 23, 24 and 25. Field 17 is the *Same as previous section* switch, 1 by default ([0017](0017-section-switches.md)). This experiment writes header text into two sections and turns the second section's switch off, then reads the exported PDF.

## Setup

| | |
| --- | --- |
| Pages | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-17 |
| Input | `samples/0361/char-only-resaved.pages`: `first`, a section break, then `second`, so two pages and two sections, 1732660 and 1732682, both with field 17 = 1 and empty headers. The first header box of each section's right-hand set (field 25) is text record 1732676 and 1732698 |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py); exported with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) and read with [`recipes/0374-pdf-text.swift`](../recipes/0374-pdf-text.swift) |

## Recipe

```bash
mkdir -p samples/0387
R=recipes/0302-set-path.py
F=samples/0361/char-only-resaved.pages
O=samples/0387
python3 -I $R $F $O/first-only.pages 1732676 3 string "First header"
python3 -I $R $O/first-only.pages $O/first-only-own.pages 1732682 17 varint 0
python3 -I $R $O/first-only.pages $O/both.pages 1732698 3 string "Second header"
python3 -I $R $O/both.pages $O/both-own.pages 1732682 17 varint 0
for f in first-only first-only-own both both-own; do
  sh recipes/0372-in-app.sh Pages $O/$f.pages "export d to POSIX file \"$PWD/$O/$f.pdf\" as PDF"
  swift recipes/0374-pdf-text.swift $O/$f.pdf
done
```

## Observation

| File | Section 1 header | Section 2 header | Section 2 field 17 | Page 1 | Page 2 |
| --- | --- | --- | --- | --- | --- |
| `first-only.pages` | First header | empty | 1 | First header / first | First header / second |
| `first-only-own.pages` | First header | empty | 0 | First header / first | second |
| `both.pages` | First header | Second header | 1 | First header / first | First header / second |
| `both-own.pages` | First header | Second header | 0 | First header / first | Second header / second |

## Conclusion

With field 17 at 1, a section's pages use the previous section's headers and footers, and its own sets are kept but ignored, even when they hold text. With field 17 at 0, the section uses its own sets. A reader must follow field 17 back to the section whose sets are actually used.

## Confidence

*Confirmed*: section field 17 as *same as previous section*, by writing it.
