# 0327: Writing header and footer text

**Status:** run

Header and footer text is in type-2001 records reached through the section's header-and-footer sets: in a set (type 10143), field 1 lists the header's left, centre and right texts and field 2 the footer's ([0016](0016-header-and-footer.md)). [0238](0238-no-header.md) read field 2 of the document settings (type 10012) as the switch that shows headers. This experiment writes header and footer text, and turns that switch off, and measures the exported page with [`recipes/0319-measure-pdf.swift`](../recipes/0319-measure-pdf.swift).

## Setup

| | |
| --- | --- |
| Pages | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0002/hello.pages`: the section (record 1732296) names set 1732544 in field 25, whose header texts are 1732234, 1732385 and 1732428 and footer texts 1732501, 1732440 and 1732492, all empty; settings record 1732614 has fields 1, 2 and 3 = 1 |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py) |

## Recipe

```bash
mkdir -p samples/0327
R=recipes/0302-set-path.py
python3 -I $R samples/0002/hello.pages samples/0327/a.pages 1732234 3 string LEFT
python3 -I $R samples/0327/a.pages samples/0327/b.pages 1732428 3 string RIGHT
python3 -I $R samples/0327/b.pages samples/0327/header.pages 1732492 3 string FOOT
rm samples/0327/a.pages samples/0327/b.pages
python3 -I $R samples/0327/header.pages samples/0327/header-off.pages 1732614 2 varint 0
```

An empty text storage has no field 3, so the text is added as a new field. A first attempt with the writer of [0287](0287-rewriting-a-document.md), whose `--text` option only replaces an existing field 3, wrote nothing. Each file was opened in Pages on its own, exported as PDF and measured.

## Observation

`header.pages` and `header-off.pages` print the same:

| Text | Top – bottom | Left – right |
| --- | --- | --- |
| `LEFT` and `RIGHT` | 37.8 – 46.8 | 57.8 – 84.5 and 503.5 – 538.8 |
| `hello` (body) | 58.2 – 66.2 | 57.5 – 79.5 |
| `FOOT` | 788.0 – 797.0 | 507.5 – 538.8 |

## Conclusion

The header-and-footer set works as read: field 1's first and third texts are the left and right header boxes, aligned to the left and right margins, and field 2's third the right footer box. They are placed in the margins, 1.25 cm from the top and about 1.5 cm from the bottom, the Blank template's distances. Setting document settings field 2 to 0 alone doesn't hide headers that have text. When Pages turns headers off itself, it also replaces the header text records ([0238](0238-no-header.md)), so field 2 is not the whole switch. How Pages decides to hide them isn't settled.

## Confidence

*Confirmed*: header and footer texts and their order in a set, by writing them.

*Unknown*: what hides headers; field 2 = 0 alone doesn't.
