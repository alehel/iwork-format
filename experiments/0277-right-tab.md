# 0277: A right-aligned tab with a leader

**Status:** run

[0255](0255-tab-stop.md) found tab stops in paragraph property 25, each with its position in field 1. A left-aligned stop with no leader stored nothing else. This experiment sets a stop's alignment and leader, to find their fields.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0255](0255-tab-stop.md), a left stop at 3 cm |

## Recipe

1. Make a document with the body text `One`:
   ```bash
   osascript -e 'tell application "Pages" to set body text of (make new document) to "One"'
   ```
2. With Pages in front, add a tab stop at 3 cm as in 0255. Set its alignment to Right (*Høyre*) and its leader to dots (`.....`).
3. Save it as `samples/0277/right-tab.pages`.

## Observation

The paragraph style's property 25 is:

```
25: { 1: { 1: 85.03937, 2: 2, 3: "." } }
```

## Conclusion

Each tab stop holds its position in points (field 1), its alignment (field 2) and its leader (field 3). The leader is stored as the character itself, so a reader can repeat it to fill the gap. Right alignment is 2. Following the pop-up's order (left, centre, right, decimal), left is 0 and absent by default, centre is probably 1 and decimal 3.

## Confidence

*Likely*: tab stop field 2 is the alignment (2 right) and field 3 the leader character.

*Unknown*: the values for centre and decimal.
