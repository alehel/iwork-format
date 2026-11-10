# 0320: Writing indents, measured on the page

**Status:** run

A paragraph style's indents were read as properties 12.7 (first line), 12.11 (left) and 12.19 (right), in points ([0253](0253-indents.md)). This experiment writes each into the Body style of a paragraph long enough to wrap, and measures the lines on the exported page with [`recipes/0319-measure-pdf.swift`](../recipes/0319-measure-pdf.swift).

## Setup

| | |
| --- | --- |
| Pages | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0002/hello.pages`, with its body text replaced by the word `measure` sixty times, which wraps to several lines |
| Writer | [`recipes/0287-iwa-writer.py`](../recipes/0287-iwa-writer.py) for the text, [`recipes/0302-set-path.py`](../recipes/0302-set-path.py) for the indents |

## Recipe

```bash
mkdir -p samples/0320
python3 -I recipes/0287-iwa-writer.py samples/0002/hello.pages samples/0320/long.pages \
  --text 1732539 "$(python3 -c "print(' '.join(['measure']*60))")"
python3 -I recipes/0302-set-path.py samples/0320/long.pages samples/0320/left72.pages 1731511 12.11 float 72
python3 -I recipes/0302-set-path.py samples/0320/long.pages samples/0320/first36.pages 1731511 12.7 float 36
python3 -I recipes/0302-set-path.py samples/0320/long.pages samples/0320/right72.pages 1731511 12.19 float 72
```

All three indents were 0. Each file was opened in Pages on its own, exported as PDF and measured.

## Observation

Left and right ends of the first three lines, in points; the text area runs from 56.69 to 538.59:

| File | Line 1 | Line 2 | Line 3 |
| --- | --- | --- | --- |
| `long.pages` | 57.5 – 506.0 | 57.5 – 506.0 | 57.5 – 506.0 |
| `left72.pages` (12.11 = 72) | 57.5 – 506.0 | 129.5 – 532.8 | 129.5 – 532.8 |
| `first36.pages` (12.7 = 36) | 93.5 – 496.8 | 57.5 – 506.0 | 57.5 – 506.0 |
| `right72.pages` (12.19 = 72) | 57.5 – 460.8 | 57.5 – 460.8 | 57.5 – 460.8 |

## Conclusion

12.7 indents the first line and 12.11 every other line, each measured from the margin on its own, not one from the other: with only 12.11 set, the first line stays at the margin. So a reader must apply 12.7 to the first line and 12.11 to the rest, and Pages' Left setting presumably writes both. 12.19 moves the right edge in by its value: lines now wrap before 538.59 − 72 = 466.59.

## Confidence

*Confirmed*: 12.7, 12.11 and 12.19, by writing them and measuring; 12.7 and 12.11 are independent, both from the margin.
