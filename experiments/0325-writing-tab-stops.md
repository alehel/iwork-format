# 0325: Writing tab stops, measured on the page

**Status:** run

A paragraph style's tab stops were read as property 12.25, one 25.1 per stop with its position in points in field 1 and its alignment in field 2: absent for left, 2 right ([0255](0255-tab-stop.md), [0277](0277-right-tab.md)). This experiment writes a tab into a paragraph, then left and right stops into the Body style, and measures where the text after the tab lands.

## Setup

| | |
| --- | --- |
| Pages | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0002/hello.pages`, with its body text replaced by `a`, a tab and `b`; the Body style has no tab stops; margins are 56.69 points |
| Writer | [`recipes/0287-iwa-writer.py`](../recipes/0287-iwa-writer.py) for the text, [`recipes/0302-set-path.py`](../recipes/0302-set-path.py) for the stops |
| Measuring | [`recipes/0319-measure-pdf.swift`](../recipes/0319-measure-pdf.swift) |

## Recipe

```bash
mkdir -p samples/0325
python3 -I recipes/0287-iwa-writer.py samples/0002/hello.pages samples/0325/tab.pages --text 1732539 "$(printf 'a\tb')"
python3 -I recipes/0302-set-path.py samples/0325/tab.pages samples/0325/left200.pages 1731511 12.25.1.1 float 200
python3 -I recipes/0302-set-path.py samples/0325/tab.pages samples/0325/right200.pages 1731511 12.25.1.1 float 200 12.25.1.2 varint 2
```

Each file was opened in Pages on its own, exported as PDF and measured.

## Observation

| File | `a` | `b` |
| --- | --- | --- |
| `tab.pages` (no stops) | 57.2 – 62.5 | 93.8 – 99.0 |
| `left200.pages` | 57.2 – 62.5 | 257.8 – 263.0 |
| `right200.pages` | 57.2 – 62.5 | 251.2 – 256.5 |

56.69 + 200 = 256.69.

## Conclusion

A stop's position is in points from the left margin. A left stop puts the start of the text after the tab there, apart from the letter's own side bearing, and a right stop (field 2 = 2) its end. Without stops, Pages uses a default stop every 36 points: `b` starts at 56.69 + 36 plus its side bearing.

## Confidence

*Confirmed*: tab stop position and the left and right alignments, by writing them and measuring.
