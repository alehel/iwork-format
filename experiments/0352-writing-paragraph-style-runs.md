# 0352: Writing paragraph style runs

**Status:** run

A text's run table 5 gives each paragraph its style (type 2022), with an entry at every paragraph's first character ([0005](0005-paragraphs.md), [0289](0289-writing-two-paragraphs.md)). This experiment points the first of two paragraphs at another named style and asks Pages.

## Setup

| | |
| --- | --- |
| Pages | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0005/two-lf.pages`: `one` and `two`, with paragraph runs at 0 (Body, record 1731511) and 4 (no style) |
| Writer | [`recipes/0351-add-run.py`](../recipes/0351-add-run.py) |

## Recipe

```bash
mkdir -p samples/0352
cp samples/0005/two-lf.pages samples/0352/original.pages
python3 -I recipes/0351-add-run.py samples/0352/original.pages samples/0352/title.pages 1732539 5 0 1731491 4 1731511
```

The new table has the template's Title style (record 1731491) at 0 and Body at 4. Pages opened each file on its own, read each paragraph's size and font through AppleScript, and exported it as PDF, measured with [`recipes/0319-measure-pdf.swift`](../recipes/0319-measure-pdf.swift).

## Observation

| File | Paragraph 1 | Paragraph 2 | Lines: top – bottom, left – right |
| --- | --- | --- | --- |
| `original.pages` | 11 pt HelveticaNeue | 11 pt HelveticaNeue | 60.2 – 66.2, 57.2 – 74.8; 70.8 – 78.2, 57.0 – 74.5 |
| `title.pages` | 30 pt HelveticaNeue-Bold | 11 pt HelveticaNeue | 70.5 – 86.8, 58.0 – 109.2; 95.8 – 103.2, 57.0 – 74.5 |

## Conclusion

Each paragraph run entry sets its paragraph's style, and Pages lays the paragraphs out with them: the first in the Title style's 30-point bold, the second in Body, moved down to make room. In the original, the second entry has no style and continues Body; here it names Body explicitly, which works the same way.

## Confidence

*Confirmed*: paragraph style runs (table 5), by writing them.
