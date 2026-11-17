# 0386: Writing left and right pages

**Status:** run

Section field 19 is 1 when left and right pages have different headers and footers. Then the right-hand pages use the set that section field 25 names and the left-hand pages the set in field 24 ([0019](0019-left-and-right-pages.md)). Pages shows that switch only with *Facing pages* on, the document setting in field 34 of the type-10012 record ([0017](0017-section-switches.md)). This experiment turns each off and reads the headers from the exported PDF.

## Setup

| | |
| --- | --- |
| Pages | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-17 |
| Input | `samples/0019/left-right.pages`: two pages, `one` and `Two`, with facing pages on and section 1732296's field 19 = 1. The first page's header reads `Right` and the second's `left` |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py); exported with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) and read with [`recipes/0374-pdf-text.swift`](../recipes/0374-pdf-text.swift) |

## Recipe

```bash
mkdir -p samples/0386
R=recipes/0302-set-path.py
F=samples/0019/left-right.pages
O=samples/0386
cp $F $O/original.pages
python3 -I $R $F $O/same.pages 1732296 19 varint 0
python3 -I $R $F $O/not-facing.pages 1732614 34 varint 0
for f in original same not-facing; do
  sh recipes/0372-in-app.sh Pages $O/$f.pages "export d to POSIX file \"$PWD/$O/$f.pdf\" as PDF
return facing pages of d"
  swift recipes/0374-pdf-text.swift $O/$f.pdf
done
```

## Observation

| File | Written | `facing pages` | Page 1 | Page 2 |
| --- | --- | --- | --- | --- |
| `original.pages` | nothing | true | Right / one | left / Two |
| `same.pages` | section field 19 = 0 | true | Right / one | Right / Two |
| `not-facing.pages` | settings field 34 = 0 | false | Right / one | left / Two |

## Conclusion

Field 19 decides whether left-hand pages get their own headers and footers: with it 0, the second page uses the right-hand set like the first. The left-hand set's text stays in the file but isn't used. Facing pages doesn't gate it: with field 34 at 0, AppleScript reports facing pages off, yet the second page still uses the left-hand set. So *left* and *right* here are even and odd pages whatever the facing-pages setting, and a reader should follow field 19 alone.

## Confidence

*Confirmed*: section field 19 as *left and right pages are different*, by writing it, and that it applies with facing pages off.
