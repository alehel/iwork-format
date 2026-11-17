# 0427: Writing paragraph runs without a style

**Status:** run

Run table 5 attaches paragraph styles: one entry per paragraph, at its first character, even when the style doesn't change, and each entry's style was confirmed by writing it ([0151](0151-thousand-paragraphs.md), [0352](0352-writing-paragraph-style-runs.md)). An entry with no field 2 seemed to keep the previous paragraph's style ([0034](0034-mixed-paragraph-styles.md)). This experiment writes such entries, and a table with fewer entries than paragraphs.

## Setup

| | |
| --- | --- |
| Pages | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/0002/hello.pages`, with its body (1732539) replaced by three paragraphs, `one`, `two` and `three`, which start at 0, 4 and 8. The template's *Tittel* (1731491) is 30-point bold and *Brødtekst* (1731511) 11-point |
| Writer | The writer of [0287](0287-rewriting-a-document.md) for the text and [`recipes/0351-add-run.py`](../recipes/0351-add-run.py) for the run table; read back with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) |

## Recipe

```bash
mkdir -p samples/0427
A=recipes/0351-add-run.py
O=samples/0427
python3 -I recipes/0287-iwa-writer.py samples/0002/hello.pages $O/text.pages --text 1732539 "$(printf 'one\ntwo\nthree')"
python3 -I $A $O/text.pages $O/title-none-body.pages 1732539 5 0 1731491 4 0 8 1731511
python3 -I $A $O/text.pages $O/title-body-none.pages 1732539 5 0 1731491 4 1731511 8 0
python3 -I $A $O/text.pages $O/title-only.pages 1732539 5 0 1731491
for f in text title-none-body title-body-none title-only; do
  sh recipes/0372-in-app.sh Pages $O/$f.pages 'set out to {}
repeat with p in paragraphs of body text of d
  set end of out to {(p as text), font of p, size of p}
end repeat
return out'
done
```

A style of 0 in `recipes/0351-add-run.py` writes an entry with no field 2. `text.pages` keeps `hello`'s single entry, at 0, for three paragraphs.

## Observation

| File | Table 5 | `one` | `two` | `three` |
| --- | --- | --- | --- | --- |
| `text.pages` | 0 *Brødtekst* (as in `hello.pages`) | 12-point regular | 12-point regular | 12-point regular |
| `title-only.pages` | 0 *Tittel* | 12-point regular | 12-point regular | 12-point regular |
| `title-none-body.pages` | 0 *Tittel*, 4 none, 8 *Brødtekst* | 30-point bold | 30-point bold | 11-point regular |
| `title-body-none.pages` | 0 *Tittel*, 4 *Brødtekst*, 8 none | 30-point bold | 11-point regular | 11-point regular |

The font is Helvetica Neue throughout.

## Conclusion

An entry with no style gives its paragraph the previous paragraph's style, whichever that is. A table with fewer entries than the text has paragraphs is ignored altogether: with one entry for three paragraphs, every paragraph took 12-point text, which is neither the entry's style nor *Brødtekst*, and is probably the document's default paragraph style. So a writer must give every paragraph its own entry, as Pages does, and a reader meeting a short table can't trust its entries.

## Confidence

*Confirmed*: a table-5 entry without a style keeps the previous paragraph's style, and a table with fewer entries than paragraphs isn't used, by writing them. *Likely*: the 12-point fallback is the document's default paragraph style.
