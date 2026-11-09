# 0015: List levels

**Status:** run

[0014](0014-lists.md) found that a list style stores nine per-level values, but its one-level lists didn't show where a paragraph's level is kept. Field 6 of the body's type-2001 record has held a single entry of three zeros in every document so far. This experiment indents list items to see whether that changes.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), with a Norwegian (nb) user interface and default autocorrection |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0014](0014-lists.md), `dash-list.pages` |

## Recipe

As in 0014. AppleScript made an empty document, the keys were typed in the Pages window, and AppleScript saved the document as `nested-list.pages`:

`- one`, Return, Tab, `two`, Return, `three`

Tab indented the second item one level. The third item kept that level, so the list was `One` at the first level, then `Two` and `three` at the second.

Pages again showed an autocorrection suggestion under the last word, which blocked AppleScript until it was dismissed with its close button (see 0014).

## Observation

The text and the list-style runs are the same as in `dash-list.pages`: one entry pointing all paragraphs at the Dash list style 1731488. No style was added.

Field 6 gained a second entry:

```
dash-list.pages (0014)
6: { 1: { 1: 0, 2: 0, 3: 0 } }

nested-list.pages
6: { 1: { 1: 0, 2: 0, 3: 0 },
     1: { 1: 4, 2: 1, 3: 0 } }
```

Position 4 is the start of the second paragraph.

## Conclusion

Field 6 of record 2001 is a run table of list levels, with entries starting at paragraph boundaries. In each entry, field 1 is the position, field 2 is the level (0 for the first level), and field 3 is 0 in every case so far. A paragraph's marker and indent come from its list style's values at that level, as in 0014.

Unlike the other run tables, field 6's entries carry a number in field 2, not a reference to an object.

## Confidence

*Likely*: field 6 holds list-level runs, with the level in field 2.

*Unknown*: field 6.3. Follow-up: restart the numbering in the middle of a numbered list.
