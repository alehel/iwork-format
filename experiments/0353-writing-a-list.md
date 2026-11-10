# 0353: Writing a list

**Status:** run

A list is a list style (type 2023) applied to a range of paragraphs through run table 7, with the level in run table 6; the marker isn't in the text ([0014](0014-lists.md), [0015](0015-list-levels.md)). This experiment turns two plain paragraphs into a dash list by writing table 7 alone.

## Setup

| | |
| --- | --- |
| Pages | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0005/two-lf.pages`: `one` and `two`, with no list; the template's `text-7-liststyle-Dash` is record 1731488 |
| Writer | [`recipes/0351-add-run.py`](../recipes/0351-add-run.py) |

## Recipe

```bash
mkdir -p samples/0353
cp samples/0005/two-lf.pages samples/0353/original.pages
python3 -I recipes/0351-add-run.py samples/0353/original.pages samples/0353/list.pages 1732539 7 0 1731488 4 1731488
```

Table 7 gets the Dash list style at both paragraph starts; table 6 is left as it was. Each file was opened in Pages on its own, exported as PDF and measured with [`recipes/0319-measure-pdf.swift`](../recipes/0319-measure-pdf.swift), and the written one saved again.

## Observation

| File | Line 1 | Line 2 |
| --- | --- | --- |
| `original.pages` | 57.2 – 74.8 | 57.0 – 74.5 |
| `list.pages` | 57.5 – 86.8 | 57.5 – 86.5 |

In `list.pages`, each line starts with the marker at the margin and the word follows about 12 points further right, as in the dash list of [0334](0334-writing-list-markers.md).

## Conclusion

Run table 7 is enough to make paragraphs into a list: with no level entry in table 6, they take the first level. The marker and the indent come from the list style.

## Confidence

*Confirmed*: list runs (table 7), by writing them.
