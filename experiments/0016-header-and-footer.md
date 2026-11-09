# 0016: Header and footer

**Status:** run

[0003](0003-non-ascii-word.md) found 18 type-2001 records besides the body, and [0004](0004-larger-word.md) found that they use the paragraph style for headers and footers. This experiment types into a header and a footer to see which records the text goes to, and how those records are tied to the page.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), with a Norwegian (nb) user interface and default autocorrection |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0002](0002-one-word.md) |

## Recipe

1. AppleScript makes a new document and sets its body text to `body`.
2. In the Pages window, choose View → Show Layout (*Vis → Vis layout*). The header and footer then appear as three boxes each, left, centre and right. Without it, clicks in the header area did nothing.
3. Click the left header box and type `head`. Click the right footer box and type `foot`.
4. Pages capitalised `head`, and offered `Foot` in a suggestion that blocked AppleScript until it was dismissed with its close button (as in [0014](0014-lists.md)).
5. AppleScript saves the document as `header.pages`.

The Document tab of the sidebar showed the header and footer turned on, 1.25 cm and 1.5 cm from the edges. These are the defaults of the Blank template.

## Observation

### Where the text went

Of the 19 type-2001 records in `Document.iwa`, three have a field 3:

```
1732539  "body"    (the body, as since 0002)
1732234  "Head"
1732492  "foot"
```

Both header and footer records use the header-and-footer paragraph style (1731520), as all 18 did in 0004.

### Header and footer sets

One record refers to both: object 1732544, type 10143.

```
1: { 1: 1732234 }      ← "Head"
1: { 1: 1732385 }
1: { 1: 1732428 }
2: { 1: 1732501 }
2: { 1: 1732440 }
2: { 1: 1732492 }      ← "foot"
```

`Document.iwa` has three records of type 10143: 1732380, 1732482 and 1732544. Each lists three type-2001 records in field 1 and three in field 2, which together are the 18 non-body records.

### The section

All three type-10143 records are named by object 1732296, type 10011. That's the object that the body's field 17 has pointed at since 0002:

```
17: varint 1
18: varint 0
19: varint 0
20: varint 0
21: varint 0
22: varint 1
23: { 1: 1732380 }
24: { 1: 1732482 }
25: { 1: 1732544 }     ← the set the text went into
26: text "Blank"
28: varint 0
29: { 1: 1732233 }
```

## Conclusion

A header or footer is a text record of type 2001, like the body. The page links to it through two levels:

- A type-10011 record is probably a section. The body's field-17 run table points ranges of the body at it.
- The section's fields 23, 24 and 25 each name a set of headers and footers (type 10143). Field 1 of a set is the header and field 2 the footer, each as three text records in the order left, centre, right.

The set that a plain document uses is the one in field 25. The other two are probably the variants Pages offers for a different first page and for left and right pages. Fields 18 to 21 of the section, all 0 here, are candidates for the switches that turn those variants on. Field 26 is the name of the template the section came from.

A reader that wants the visible header of a simple document follows the body's field 17 to the section, then field 25 to a set, then field 1 to the three text records.

## Confidence

*Likely*:

- Headers and footers are type-2001 records listed by type-10143 sets, with field 1 for the header and field 2 for the footer, each in left, centre, right order.
- The section (type 10011) names three such sets, and a plain document uses the one in field 25.
- Body field 17 holds section runs.

*Unknown*:

- Which pages the sets in fields 23 and 24 belong to, and what fields 17–22, 28 and 29 of the section mean. Follow-up: turn on a different first page (Document tab → Section → *Ulik første side*, "different first page"), type in the first page's header, and see whether field 23 or 24 is used and which flag changes.
