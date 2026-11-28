# 0487: A picture set to Move with Text

**Status:** run

An object in the text is a U+FFFC with an entry in the body's attachment runs (field 9), pointing at a type-2003 record, which points at the object; so far that was seen for tables ([0020](0020-a-table.md)). An object placed on the page has no parent (drawable field 1.2) and is listed by types 10015 and 10010 ([0482](0482-objects-on-later-pages.md)). This experiment switches a picture from Stay on Page to Move with Text in the Arrange sidebar, to see whether it becomes an attachment, and where its offset is kept.

## Setup

| | |
| --- | --- |
| Pages | 16.0 (7052.0.68), with a Norwegian (nb) user interface |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-28 |
| Input | `samples/0002/hello.pages` with the body written as one paragraph of two lines, `first paragraph of text here. … at least once.` |
| Recipe | Below: the writer of [0287](0287-rewriting-a-document.md), AppleScript, and one click in the Pages window. Exported with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) and measured with [`recipes/0482-red-per-page.swift`](../recipes/0482-red-per-page.swift) and [`recipes/0319-measure-pdf.swift`](../recipes/0319-measure-pdf.swift) |

## Recipe

1. Write the input and open it in Pages:
   ```bash
   mkdir -p samples/0487
   S=$PWD/samples/0487
   python3 -I recipes/0287-iwa-writer.py samples/0002/hello.pages $S/gui-base.pages --text 1732539 \
     "first paragraph of text here. second sentence of the paragraph runs on so the line wraps across the page width at least once."
   open -a "Pages Creator Studio" $S/gui-base.pages
   ```
2. AppleScript places the red picture of [0023](0023-an-image.md) on page 1 at 80 × 40 points (`tell page 1 of front document to make new image with properties {file: …, width: 80, height: 40}`), and saves the front document as `stay.pages`.
3. In the Arrange (*Ordne*) tab of the Format sidebar, with the picture selected, click *Move with Text* (*Flytt med tekst*). Pages moved the anchor mark to the end of the paragraph. AppleScript saves the front document as `move.pages`.
4. AppleScript replaces the body's first word, `first`, with `added`, a return and `first`, so that the paragraph starts one line lower, and saves the front document as `move-line-added.pages`. `gui-base.pages` was then deleted.
5. Then:
   ```bash
   python3 -I recipes/0383-set-nth-path.py $S/move.pages $S/move-type-5.pages 1732688 1.3.1 varint 5
   for f in move move-line-added move-type-5; do
     cp $S/$f.pages $S/tmp.pages
     sh recipes/0372-in-app.sh Pages $S/tmp.pages "export d to POSIX file \"$S/$f.pdf\" as PDF"
     swift recipes/0482-red-per-page.swift $S/$f.pdf
     swift recipes/0319-measure-pdf.swift $S/$f.pdf
   done
   rm $S/tmp.pages
   ```

## Observation

### Stay on Page to Move with Text

Comparing `move.pages` with `stay.pages`:

```
body 1732539, field 3:   … at least once.  →  … at least once.￼        a U+FFFC at 125, the end
body 1732539, field 9:   absent → { 1: { 1: 125, 2: { 1: 1732732 } } }
new record 1732732, type 2003:
  1: { 1: 1732688 }      the picture
  2: 0
  3: 230.10709           float
  4: 0
  5: 316.90707           float
picture 1732688, field 1.2:  absent → { 1: 1732539 }    the body's text
type 10010, field 1:     { 1: 0, 4: { 1: { 1: 1732688 } } }  →  absent
type 10015, field 1:     unchanged: the body's text, then the picture
```

The picture's own position, 1.1.1 = (286.8, 397.6), didn't change, and neither did its wrap settings (1.3).

### The offset

The page's left margin is 56.69 points, and 286.8 − 56.69 = 230.11, field 3. The paragraph's two lines are 12 points high, the first from 56.69: in `move.pdf` the text bands are 58.2–68.2 and 70.2–80.2. The line holding the U+FFFC is the second, ending at 80.69, and 397.6 − 80.69 = 316.91, field 5.

In `move-line-added.pages` the paragraph starts a line lower. The 2003 record and the picture's 1.1.1 = (286.8, 397.6) are unchanged in the file, but Pages drew the picture 12 points lower, at (286.8, 409.2)–(367.0, 449.5), against (286.8, 397.2)–(367.0, 437.5) in `move.pdf`. The anchor's line now ends at 92.69, and 92.69 + 316.91 = 409.6.

### Wrap type 5

`move-type-5.pages`, with the wrap type (1.3.1) written as 5, drew the same as `move.pages`: the picture stays where it was and the text above it unchanged. Pages kept the 5 when it saved.

## Conclusion

Move with Text makes the picture an attachment, as a table in the text is: a U+FFFC in the body, an entry in the body's attachment runs (field 9) at its position, a type-2003 record that names the picture in field 1, and the body's text as the picture's parent in drawable field 1.2. It is still a floating object: it stays in the page's stacking list (type 10015), keeps its own position and wrap, and leaves the page list (type 10010), since its page now follows the text.

The 2003 record holds the picture's offset from its anchor, in points: field 3 from the left edge of the body's text column, and field 5 from the bottom of the line that holds the U+FFFC (here also the paragraph's last line, so the two can't be told apart). Pages places the picture from this offset when it lays out the text, and doesn't update the picture's 1.1.1 in the file when the text before it moves. A reader should take the position of a Move with Text object from the anchor and the 2003 offset, not from 1.1.1.

Wrap type 5 is not Inline with Text: written into a floating picture it changed nothing drawn.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `stay.pages` | `0002/hello.pages` | `2001#1732539 3 ~ "first paragraph"`, `3005#1732688 1.1.2.1 = 80.0`, `10010#1732278 1.1 = 0`, `10015#1732364 1.1 = 1732688` | *Control*: a picture on page 1, Stay on Page |
| `move.pages` | `stay.pages` | `2001#1732539 3: changed`, `2001#1732539 9.1.1 = 125`, `records 2003: 0 → 1`, `2003 1.1 = 1732688`, `2003 3 = 230.10709`, `2003 5 = 316.90707`, `3005#1732688 1.2.1: absent → 1732539`, `10010#1732278 1: ×1 → ×0`, `10015#1732364 1.1 = 1732688` | *Likely*: Move with Text makes an attachment with its offset in a 2003 record, outside the page list |
| `move-line-added.pages` | `move.pages` | `2001#1732539 3: changed`, `2003 5 = 316.90707`, `3005#1732688 1.1.1.2 = 397.6` | *Likely*: the picture is drawn from the anchor and the offset, and 1.1.1 isn't updated |
| `move-type-5.pages` | `move.pages` | Only `3005#1732688 1.3.1: 4 → 5` | *Unknown*: wrap type 5 written into a floating picture changes nothing drawn |
| `move-type-5-resaved.pages` | `move-type-5.pages` | `3005#1732688 1.3.1 = 5` | *Not used*: a saved copy |

## Confidence

*Confirmed*: the attachment chain U+FFFC → field 9 entry → type 2003 → object holds for a picture as for a table ([0020](0020-a-table.md)), and a Move with Text object names the body's text in its field 1.2.

*Likely*: the 2003 record's fields 3 and 5 are the offset from the text column's left edge and from the bottom of the anchor's line, and Move with Text objects leave type 10010 but stay in 10015. One experiment; a second would drag the picture to another offset and anchor it in a paragraph's first line.

*Unknown*: 2003 fields 2 and 4 (both 0), and how Inline with Text is stored. AppleScript can't put a picture in the text (Pages refuses `make new image` in the body text), and the wrap pop-up that offers Inline with Text can't be used in the background; a follow-up needs the Pages window in front.
