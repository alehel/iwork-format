# 0362: Writing first-page headers

**Status:** run

Section field 28 is the switch "Hide header and footer on the section's first page" ([0017](0017-section-switches.md)). A section names three header-and-footer sets, in fields 23, 24 and 25. A plain document uses 25, and left-hand pages use 24 when field 19 is on; what 23 is for was unknown ([0016](0016-header-and-footer.md), [0019](0019-left-and-right-pages.md)). This experiment writes field 28, then puts text into set 23 and turns on, one at a time, the section's other unexplained switches, 18, 20 and 21, to see which one shows set 23.

## Setup

| | |
| --- | --- |
| Pages | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0327/header.pages`, whose set 25 has the header texts LEFT and RIGHT and the footer FOOT. Its section, 1732296, has 17 = 1, 22 = 1 and 18–21, 28 = 0. Set 23's left header is text storage 1732494 |
| Writer | The writer of [0287](0287-rewriting-a-document.md) and [`recipes/0302-set-path.py`](../recipes/0302-set-path.py) |

## Recipe

```bash
mkdir -p samples/0362
R=recipes/0302-set-path.py
python3 -I recipes/0287-iwa-writer.py samples/0327/header.pages samples/0362/x.pages \
  --text 1732539 "$(printf 'page one\x05page two')"
python3 -I $R samples/0362/x.pages samples/0362/both.pages 1732494 3 string FIRSTSET
rm samples/0362/x.pages
python3 -I $R samples/0362/both.pages samples/0362/hide-first.pages 1732296 28 varint 1
for n in 18 20 21; do
  python3 -I $R samples/0362/both.pages samples/0362/field-$n.pages 1732296 $n varint 1
done
```

Pages opened each file on its own and exported it as PDF. The text of each page was read with PDFKit.

## Observation

| File | Page 1 | Page 2 |
| --- | --- | --- |
| `both.pages` | LEFT RIGHT / page one / FOOT | LEFT RIGHT / page two / FOOT |
| `hide-first.pages` (28 = 1) | page one | LEFT RIGHT / page two / FOOT |
| `field-18.pages` (18 = 1) | FIRSTSET / page one | LEFT RIGHT / page two / FOOT |
| `field-20.pages` (20 = 1) | as `both` | as `both` |
| `field-21.pages` (21 = 1) | as `both` | as `both` |

Set 23's footer is empty, so page 1 of `field-18.pages` has no footer.

## Conclusion

Field 28 = 1 hides the header and footer on the section's first page. Field 18 = 1 makes the section's first page use its own set, the one in field 23, in place of set 25. Fields 20 and 21 change nothing that shows on these two pages.

## Confidence

*Confirmed*: field 28 hides the first page's header and footer. Field 18 switches the first page to set 23. Which control in Pages sets field 18 wasn't checked.
