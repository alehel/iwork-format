# 0255: A tab stop

**Status:** run

Tab stops are edited in a table in the Layout tab, which needs Pages in front. This experiment adds one.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `samples/0236/plain.pages`, a new document with the body text `One` |

## Recipe

1. Make a document with the body text `One`:
   ```bash
   osascript -e 'tell application "Pages" to set body text of (make new document) to "One"'
   ```
2. With Pages in front, click in `One`, then open the Layout tab, expand Tabs (*Tabulatorer*), click + to add a stop, and change its position to 3 cm. The stop is left-aligned, with no leader.
3. Save it as `samples/0255/tab-stop.pages`.

## Observation

The paragraph runs point at a new paragraph style whose only property is:

```
25: { 1: { 1: 85.03937 } }   ← 3 cm in points
```

## Conclusion

Paragraph property 25 is the list of tab stops, one entry in 25.1 per stop, with its position in points in field 1. The alignment and leader aren't stored for a left-aligned stop with no leader. They are probably further fields of each entry, absent when they have their default value.

## Confidence

*Likely*: paragraph property 25 lists tab stops with their positions in points.

*Unknown*: the fields for alignment and leader.
