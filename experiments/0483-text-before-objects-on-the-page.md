# 0483: Adding and removing text before objects on the page

**Status:** run

An object placed on the page is listed by page number in type 10010 ([0482](0482-objects-on-later-pages.md)). This experiment changes the amount of body text before two such objects, so that the text moves to other pages, to see whether the objects keep their page or move with the text.

## Setup

| | |
| --- | --- |
| Pages | 16.0 (7052.0.68) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-28 |
| Input | `0482/on-2-and-3.pages`: the body `one`, page break, `two`, page break, `three`, with picture 1732688 on page 2 and picture 1732695 on page 3 |
| Recipe | [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh), with the AppleScript below; checked with [`recipes/0482-red-per-page.swift`](../recipes/0482-red-per-page.swift) |

## Recipe

```bash
mkdir -p samples/0483
S=$PWD/samples/0483
cp samples/0482/on-2-and-3.pages $S/tmp.pages
sh recipes/0372-in-app.sh Pages $S/tmp.pages 'set fillText to ""
repeat 60 times
set fillText to fillText & "line" & return
end repeat
set n0 to count of pages of d
set word 1 of body text of d to fillText & "one"
delay 1
set n1 to count of pages of d
save d in POSIX file "'$S'/text-added.pages"
return {n0, n1}'
cp samples/0482/on-2-and-3.pages $S/tmp.pages
sh recipes/0372-in-app.sh Pages $S/tmp.pages 'set n0 to count of pages of d
set body text of d to "one"
delay 1
set n1 to count of pages of d
save d in POSIX file "'$S'/text-removed.pages"
return {n0, n1, count of images of d}'
rm $S/tmp.pages
sh recipes/0372-in-app.sh Pages $S/text-added.pages "export d to POSIX file \"$S/text-added.pdf\" as PDF"
swift recipes/0482-red-per-page.swift $S/text-added.pdf
```

## Observation

Adding 60 lines before `one` took the document from 3 pages to 5. Pages drew:

| PDF page | Text | Red |
| --- | --- | --- |
| 1 | `line …` | none |
| 2 | `line …` | (286.8, 397.5)–(295.0, 401.8) |
| 3 | `line line one` | (286.8, 397.2)–(295.0, 401.5) |
| 4 | `two` | none |
| 5 | `three` | none |

The pictures stayed on pages 2 and 3, at the same place on the page, while the words `two` and `three` moved on to pages 4 and 5. In the file, type 10010 and the pictures' records are unchanged: page 1 holds 1732688 and page 2 holds 1732695, at (286.8, 397.71) and (286.8, 397.51).

Replacing the body with `one` alone left three pages, where Pages had made one page of text. AppleScript still counted both pictures, and type 10010 is again unchanged.

## Conclusion

An object placed on the page belongs to its page, not to the text around it: when text before it grows or shrinks, it keeps its page number and its position on that page. The text flows past it. Pages doesn't remove pages that still hold such an object, even when the text no longer reaches them.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `text-added.pages` | `0482/on-2-and-3.pages` | `2001#1732539 3: changed`, `2001#1732539 3 ~ "line"`, `10010#1732278 1: ×2 → ×2`, `10010#1732278 1.1 = 1`, `10010#1732278 1.1 = 2`, `3005#1732688 1.1.1.2 = 397.71`, `3005#1732695 1.1.1.2 = 397.51` | *Likely*: text added before the objects moves the text to later pages, not the objects |
| `text-removed.pages` | `0482/on-2-and-3.pages` | `2001#1732539 3: "one\u0005two\u0005three" → "one"`, `10010#1732278 1.1 = 1`, `10010#1732278 1.1 = 2` | *Likely*: pages that hold placed objects stay when the text no longer reaches them |

## Confidence

*Likely*: a placed object keeps its page number and position when the text before it changes, and keeps its page in the document. One experiment each; a second would add text after a section break, or remove a page break by writing.
