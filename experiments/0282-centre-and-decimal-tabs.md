# 0282: Centre and decimal tabs

**Status:** run

[0277](0277-right-tab.md) found that a tab stop's alignment is field 2, with 2 for right. This experiment sets the other two alignments, centre and decimal, on two stops in one paragraph.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0277](0277-right-tab.md) |

## Recipe

1. Make a document with the body text `One`:
   ```bash
   osascript -e 'tell application "Pages" to set body text of (make new document) to "One"'
   ```
2. With Pages in front, add a tab stop at 3 cm with Centred (*Sentrert*) alignment, as in 0255.
3. Click + again. Pages adds a second stop at 4.27 cm. Set its alignment to Decimal (*Desimal*). Both stops show no leader (*Ingen*).
4. Save it as `samples/0282/centre-decimal.pages`.

## Observation

```
25: { 1: { 1: 85.03937, 2: 1 },
      1: { 1: 121.03937, 2: 3, 3: " " } }
```

## Conclusion

Tab alignment codes are 0 (absent) left, 1 centre, 2 right and 3 decimal. The second stop was placed 36 points (1.27 cm, the default tab spacing) after the first. It stores a space as its leader, although the sidebar shows none. So a leader of a space is equivalent to no leader, and a reader should draw nothing for it.

## Confidence

*Likely*:

- Tab alignments are 1 centre and 3 decimal.
- A space leader draws nothing.
