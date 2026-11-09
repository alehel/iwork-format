# 0019: Left and right pages

**Status:** run

In [0018](0018-page-break-and-left-page.md), facing pages alone left both pages using the header-and-footer set in section field 25. With facing pages on, the Section tab of the Document sidebar shows a switch it didn't show before: *Venstre og høyre side er ulike* (Left and right pages are different). This experiment turns it on and types a different header on each page.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), with a Norwegian (nb) user interface and default autocorrection |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0018](0018-page-break-and-left-page.md), `left-page-header.pages` (the same steps without the switch) |

## Recipe

As in 0018, with one more switch:

1. AppleScript makes a new document and sets its body text to `one`.
2. Document tab of the sidebar: turn on *Motstående sider* (Facing pages). Section tab: turn on *Venstre og høyre side er ulike*.
3. View → Show Layout. Click the left box of the first page's header and type `right`, which Pages capitalised to `Right`. The first page is a right-hand page.
4. Click at the end of `one`, choose Insert → Page Break, and type `two`.
5. Click the left box of the second page's header, which was empty, and type `left`.
6. Dismiss the `Left` suggestion that blocks AppleScript, as in 0018. Save with AppleScript as `left-right.pages`.

## Observation

The header texts went into two different records:

```
1732234: "Right"   (first page, a right-hand page)
1732221: "left"    (second page, a left-hand page)
```

Record 1732234 is the first header record of the set that section field 25 names (1732544), as in 0016 and 0018. Record 1732221 is the first header record of the set that section field 24 names (1732482):

```
set 1732482: header 1732221 ("left"), 1732237, 1732235; footer 1732445, 1732280, 1732481
```

In the section, field 19 changed from 0 to 1. The section's other fields, and the sets it names, are as in 0018.

## Conclusion

Section field 19 is *Left and right pages are different*. When it is on, left-hand pages take their headers and footers from the set in section field 24, and right-hand pages from the set in field 25. When it is off, every page uses field 25.

That leaves field 23. It is probably the set for the first page of a section, but Pages 15.4 offers only *Hide on first page*, which uses field 28 and no set (0017). So field 23 may be used by documents from other versions of Pages, or by a feature this experiment hasn't found.

To show the right header on a page, a reader has to:

1. Find the page's section through the body's field-17 runs.
2. If section field 28 is 1 and this is the section's first page, show no header or footer.
3. Otherwise, if section field 19 is 1 and this is a left-hand page, use the set in field 24.
4. Otherwise use the set in field 25.

Whether a page is left or right depends on the document's facing-pages setting (field 34 of type 10012) and the page number. The first page of a document is a right-hand page.

## Confidence

*Likely*:

- Section field 19 is *Left and right pages are different*.
- Field 24 is the left-page set.
- Field 25 is the set for right-hand pages, and for every page when field 19 is 0.

*Unknown*: what the set in field 23 is for, and section fields 18, 20, 21, 22 and 29.
