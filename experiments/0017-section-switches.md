# 0017: Section switches

**Status:** run

[0016](0016-header-and-footer.md) found that a section (type 10011) names three header-and-footer sets. A plain document uses the one in field 25, and fields 17 to 22 and 28 of the section were unexplained. This experiment turns on, one at a time, the header and footer switches Pages offers. The aim is to see which fields they set, and whether they bring the other two sets into use.

Pages 15.4 doesn't offer a "different first page" switch for headers. The Section tab of the Document sidebar has *Skjul på første side i inndelingen* (Hide on first page of section) and *Som forrige inndeling* (Same as previous section). The Document tab has *Motstående sider* (Facing pages).

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), with a Norwegian (nb) user interface |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0002](0002-one-word.md), `hello.pages` (a plain document, with all switches at their defaults) |

## Recipe

AppleScript makes a new document and sets its body text to `body`. One checkbox is clicked in the Document sidebar, and AppleScript saves the document. Nothing is typed into a header.

| File | Change |
| --- | --- |
| `hide-first.pages` | Section tab: turn on *Hide on first page of section* |
| `not-same-as-previous.pages` | Section tab: turn off *Same as previous section* (on by default) |
| `facing-pages.pages` | Document tab: turn on *Facing pages* |

## Observation

Compared with `hello.pages`, each file has one field changed, apart from the body text and the save-to-save changes:

| File | Record | Field | Before → after |
| --- | --- | --- | --- |
| `hide-first.pages` | 1732296, the section (type 10011) | 28 | 0 → 1 |
| `not-same-as-previous.pages` | 1732296, the section (type 10011) | 17 | 1 → 0 |
| `facing-pages.pages` | 1732614 (type 10012) | 34 | 0 → 1 |

Record 1732614 is the one that holds the document's creation time, language and template name (see [0001](0001-empty-document.md), [0002](0002-one-word.md)).

No other record changed. In particular, the three header-and-footer sets of the section, and which set is in field 25, stayed the same.

## Conclusion

The two section-level switches map to fields of the section:

| Field | Switch | Values |
| --- | --- | --- |
| 17 | Same as previous section | 1 on (default), 0 off |
| 28 | Hide header and footer on the section's first page | 0 off (default), 1 on |

*Facing pages* is a document-wide setting stored in field 34 of the type-10012 record, so type 10012 is probably the document's settings. With it on, a reader should expect left and right pages to differ, for example in their headers.

None of these switches put the sets in fields 23 and 24 to use, so their purpose is still open. With facing pages on, the left page and right page may each use their own set. That would need a two-page document with header text on the second page.

## Confidence

*Likely*:

- Section field 17 is *Same as previous section*, and field 28 is *Hide on first page of section*.
- Field 34 of the type-10012 record is *Facing pages*.

*Unknown*:

- What the sets in section fields 23 and 24 are for. Follow-up: with facing pages on, add a page break, type into the second page's header, and save.
- Section fields 18–22 and 29.
