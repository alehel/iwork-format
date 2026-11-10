# 0334: Writing a list's marker and indent, measured on the page

**Status:** run

A list style (type 2023) keeps its properties as nine repeated values, one per level: field 11 the kind of marker (0 none, 2 a text character, 3 a number), field 16 the marker text, and field 13 an indent in points ([0014](0014-lists.md), [0015](0015-list-levels.md)). This experiment writes each into a dash list's style and looks at the exported page.

## Setup

| | |
| --- | --- |
| Pages | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0014/dash-list.pages`: the paragraphs `One`, `Two` and `Three` in the Dash list style (record 1731488, `text-7-liststyle-Dash`), whose marker kind is 2 and text `-` at every level, and whose first indent is 0 |
| Writer | [`recipes/0334-set-repeated.py`](../recipes/0334-set-repeated.py), which sets every occurrence of a repeated field, or only the first |

## Recipe

```bash
mkdir -p samples/0334
cp samples/0014/dash-list.pages samples/0334/dash.pages
R=recipes/0334-set-repeated.py
python3 -I $R samples/0334/dash.pages samples/0334/none.pages 1731488 11 varint 0
python3 -I $R samples/0334/dash.pages samples/0334/guillemet.pages 1731488 16 string "»"
python3 -I $R samples/0334/dash.pages samples/0334/indent72.pages 1731488 13 float 72 1
```

Each file was opened in Pages on its own, exported as PDF and measured with [`recipes/0319-measure-pdf.swift`](../recipes/0319-measure-pdf.swift); the guillemet version's first lines were also drawn as an image.

## Observation

The first line's ink, marker and word together:

| File | Ink |
| --- | --- |
| `dash.pages` | 57.5 – 89.0 |
| `none.pages` (11 = 0) | 69.2 – 89.0 |
| `guillemet.pages` (16 = `»`) | 57.8 – 89.0, drawn as `» One` |
| `indent72.pages` (first 13 = 72) | 129.5 – 161.0 |

## Conclusion

Field 11 = 0 removes the marker and leaves the text where it was; field 16 is the character drawn as the marker; and the first occurrence of field 13 indents the first level's marker and text together by its value in points. The text itself never changes: list markers aren't in it.

## Confidence

*Confirmed*: list style fields 11, 13 and 16, by writing them and measuring.
