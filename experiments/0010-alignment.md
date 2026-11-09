# 0010: Alignment

**Status:** run

[0008](0008-runs-and-shared-styles.md) found that formatting a whole paragraph creates an unnamed paragraph style, and that paragraph styles have a field 12 which was empty there. This experiment changes a paragraph property, its alignment, to see what goes into field 12.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), with a Norwegian (nb) user interface |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0004](0004-larger-word.md), `plain.pages` (left-aligned, the default) |

## Recipe

As in 0007: AppleScript makes a new document and sets its body text to `one two three`. In the Pages window, click in the paragraph, then click one alignment button in the Style tab of the Format sidebar. AppleScript then saves the document.

| File | Button |
| --- | --- |
| `center.pages` | Centred (*sentrert*) |
| `right.pages` | Right (*høyre*) |
| `justify.pages` | Justified (*rette marger*) |

After the click, the sidebar showed the paragraph style as `Brødtekst*` and offered to update the style. That is how it marks a paragraph whose formatting differs from its style.

## Observation

In each file the stylesheet has one new record, an unnamed type-2022 paragraph style. The paragraph-style runs (field 5 of the body's type-2001 record) point the whole paragraph at it. Its parent (field 1.3) is the Body style 1731511, as in 0008. Its other fields:

```
center.pages    10: varint 1   11: bytes (0)   12: { 1: varint 2 }
right.pages     10: varint 1   11: bytes (0)   12: { 1: varint 1 }
justify.pages   10: varint 1   11: bytes (0)   12: { 1: varint 3 }
```

The bold paragraph in 0008 was the reverse: field 11 held `{ 1: 1 }` and field 12 was empty.

### The Body style

The Body paragraph style itself (object 1731511) sets many properties. In field 11:

```
11:
  1: varint 0                       ← not bold
  2: varint 0                       ← not italic
  3: fixed32 (as float 11)          ← 11 pt, as the sidebar shows
  5: text "HelveticaNeue"           ← the font the sidebar shows
  … 27 more fields
```

and in field 12:

```
12:
  1: varint 4                       ← alignment
  3: text ","
  4: fixed32 (as float 36)
  … 25 more fields
```

The sidebar showed Body text as left-aligned, but Body's 12.1 is 4, not 0.

Field 10 is 57 in Body, in the Heading style and in the header-and-footer style. Each of those sets 31 fields in field 11 and 28 in field 12, 59 in all. In the unnamed styles that set one property, field 10 is 1. In the one from 0007 that set two, it was 2.

## Conclusion

Field 12 of a paragraph style holds paragraph properties. Field 12.1 is the alignment:

| 12.1 | Alignment |
| --- | --- |
| 1 | Right |
| 2 | Centred |
| 3 | Justified |
| 4 | Body's value, which Pages shows as left |

Pages' default value for left is probably 4 or 0, and this experiment can't tell which, because no paragraph was set to left explicitly. A value of 4 for left could mean "natural": left for left-to-right text.

Body confirms the readings of 0007: 11.1 bold, 11.2 italic, 11.3 size, plus 11.5 as the font name. So a named style is a full set of properties, and an unnamed one sets only what differs from its parent.

Field 10 isn't simply the number of properties set (57 against 59 for the full styles). It is still unknown.

## Confidence

*Likely*:

- Field 12 of a paragraph style holds paragraph properties.
- Field 12.1 is the alignment, with the values above.
- Field 11.5 is the font name.

*Unknown*:

- What value means left when set explicitly. Follow-up: centre a paragraph, then set it back to left, and save.
- The meaning of field 10, and of the other fields of 11 and 12.
