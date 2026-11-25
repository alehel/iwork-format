# 0422: Writing the header and footer switches

**Status:** run

Fields 2 and 3 of the type-10012 document settings are *Show headers* and *Show footers*, 1 for on ([0238](0238-no-header.md), [0239](0239-no-footer.md)). Writing field 2 = 0 alone turned the sidebar's checkbox off but didn't hide a header that had text; Pages itself hides headers by also emptying their texts ([0327](0327-writing-headers-and-footers.md)). This experiment writes text into a header and a footer and then each switch, alone and together.

## Setup

| | |
| --- | --- |
| Pages | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/0002/hello.pages`: the body `hello`; section 1732296's header-and-footer set 1732544 has first header box 1732234 and first footer box 1732501, both empty; settings record 1732614 has fields 2 and 3 = 1 |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py); exported with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh), read with [`recipes/0374-pdf-text.swift`](../recipes/0374-pdf-text.swift) and measured with [`recipes/0319-measure-pdf.swift`](../recipes/0319-measure-pdf.swift) |

## Recipe

```bash
mkdir -p samples/0422
R=recipes/0302-set-path.py
O=samples/0422
python3 -I $R samples/0002/hello.pages $O/footer.pages 1732501 3 string "Footer text"
python3 -I $R $O/footer.pages $O/footer-hidden.pages 1732614 3 varint 0
python3 -I $R $O/footer.pages $O/texts.pages 1732234 3 string "Header text"
python3 -I $R $O/texts.pages $O/headers-off.pages 1732614 2 varint 0
python3 -I $R $O/texts.pages $O/footers-off.pages 1732614 3 varint 0
python3 -I $R $O/texts.pages $O/both-off.pages 1732614 2 varint 0 3 varint 0
for f in footer footer-hidden texts headers-off footers-off both-off; do
  sh recipes/0372-in-app.sh Pages $O/$f.pages "export d to POSIX file \"$PWD/$O/$f.pdf\" as PDF"
  swift recipes/0374-pdf-text.swift $O/$f.pdf
done
```

## Observation

| File | Field 2 | Field 3 | Text of the page |
| --- | --- | --- | --- |
| `footer.pages` | 1 | 1 | hello, Footer text |
| `footer-hidden.pages` | 1 | 0 | hello, Footer text |
| `texts.pages` | 1 | 1 | Header text, hello, Footer text |
| `headers-off.pages` | 0 | 1 | Header text, hello, Footer text |
| `footers-off.pages` | 1 | 0 | Header text, hello, Footer text |
| `both-off.pages` | 0 | 0 | hello |

In `texts.pdf` the header is at the top of the page (38–47 points down) and the footer at the bottom (788–797); in `both-off.pdf` only the body's line is left. The body doesn't move.

## Conclusion

Either switch alone leaves headers and footers with text on the page, for headers as found in 0327 and for footers alike. With both at 0, Pages draws neither, even though both still hold text. So whether Pages draws a header or footer that has text depends on the two switches together, not one each, at least when they are written without the texts being emptied as Pages does. A reader of a document Pages saved can still go by the texts: Pages empties those it hides.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `footer.pages` | `0002/hello.pages` | Only `2001#1732501 3: absent → "Footer text"` | *Control*: the footer is drawn |
| `footer-hidden.pages` | `footer.pages` | Only `10012#1732614 3: 1 → 0` | *Confirmed*: the footer switch alone doesn't hide the footer |
| `texts.pages` | `footer.pages` | Only `2001#1732234 3: absent → "Header text"` | *Control*: the header and footer are drawn |
| `headers-off.pages` | `texts.pages` | Only `10012#1732614 2: 1 → 0` | *Confirmed*: the header switch alone hides neither |
| `footers-off.pages` | `texts.pages` | Only `10012#1732614 3: 1 → 0` | *Confirmed*: the footer switch alone hides neither |
| `both-off.pages` | `texts.pages` | Only `10012#1732614 2: 1 → 0`, `10012#1732614 3: 1 → 0` | *Confirmed*: with both at 0 neither is drawn, though both hold text |

## Confidence

*Confirmed*: by writing them, either switch alone doesn't hide a header or footer with text, and both at 0 hide them all. Why the switches act together is *unknown*.
