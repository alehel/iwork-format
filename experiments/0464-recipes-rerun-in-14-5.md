# 0464: The recipes rerun in 14.5

**Status:** run

The simplest new documents from Pages and Numbers 14.5 have the same structure as from 15.4 ([0461](0461-new-documents-in-14-5.md)). This experiment reruns, unchanged, every AppleScript recipe of the early experiments that makes one document from nothing but an output path, and compares each 14.5 document with the one 15.4 made.

## Setup

| | |
| --- | --- |
| Pages | 14.5, in Norwegian |
| Numbers | 14.5 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-23 |
| Recipes | 0030, 0031, 0035, 0036, 0037, 0043, 0044, 0045, 0047, 0059, 0060, 0063, 0064, 0065, 0066 and 0078 for Numbers (cells, formulas, formats, sheets, styles, merges, sizes, tables, headers, sparse rows, functions, cross-table references, errors); 0049, 0050, 0051, 0052, 0053, 0054, 0058 and 0198 for Pages (a text box, a shape, a line, a floating table, a font, sizes, a tab, a book template) |
| Compared with | Each experiment's own 15.4 sample, with [`recipes/0461-compare-structure.py`](../recipes/0461-compare-structure.py) |

## Recipe

```bash
mkdir -p samples/0464
for e in 0030 0031 0035 0036 0037 0043 0044 0045 0047 0049 0050 0051 0052 0053 0054 0058 0059 0060 0063 0064 0065 0066 0078 0198; do
  r=$(ls recipes/$e-*.applescript | head -1)
  old=$(ls samples/$e/*.pages samples/$e/*.numbers 2>/dev/null | head -1)
  osascript $r "$PWD/samples/0464/$e-$(basename $old)"
  python3 -I recipes/0461-compare-structure.py $old samples/0464/$e-$(basename $old)
done
```

A first run timed out on every recipe, because two password-protected documents left open by [0462](0462-opening-15-4-documents-in-14-5.md) were blocking Pages, and each recipe left an untitled document behind; those were closed unsaved and the run repeated.

## Observation

All 24 recipes ran and made their documents. Besides the differences 0461 found in every document (the format version, the build, the type-4011 record), the comparison found only this:

| Documents | 15.4 | 14.5 |
| --- | --- | --- |
| All 16 Numbers documents | one more paragraph style (type 2022) in the stylesheet: `text-12-paragraphstyle-Table Title 1` | without it |
| All 8 Pages documents | | the same parts, record types, versions and fields |

The same ZIP entries, the same parts, the same number of records of each other type, and the same top-level fields for every type were found in all 24 pairs.

## Conclusion

Pages and Numbers 14.5 write text boxes, shapes, lines, tables, cells of every kind, formulas, formats, styles, merges, sizes and sheets with the same records as 15.4. The one difference in content is a paragraph style that the 15.4 Numbers template adds, *Table Title 1*, for tables' titles; a reader finds styles by reference, so it needs nothing for it. What the spec says about these structures holds for 14.5 as written.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `*-*.numbers` | `*/*.numbers` | `11006#2 7: x"1a0400" → x"0e0401"`, `records 4011: 1 → 0`, `2022 1.2 ≠ "text-12-paragraphstyle-Table Title 1"` | *Confirmed*: 14.5 writes spreadsheets with 15.4's structure, without the *Table Title 1* style |
| `*-*.pages` | `*/*.pages` | `11006#2 7: x"1a0400" → x"0e0401"`, `records 4011: 1 → 0` | *Confirmed*: 14.5 writes Pages documents with 15.4's structure |

## Confidence

*Confirmed*: for the 24 documents of these recipes, 14.5 writes the same structure as 15.4, apart from Numbers' *Table Title 1* style.
