# 0096: Formatting a whole text box

**Status:** run

[0008](0008-runs-and-shared-styles.md) found that formatting a whole paragraph in Pages makes an unnamed paragraph style. This experiment formats all the text of a Keynote text box through AppleScript.

## Setup

| | |
| --- | --- |
| Keynote | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0068](0068-keynote-text-box.md), `textbox.key` |

## Recipe

```bash
mkdir -p samples/0096
osascript recipes/0096-keynote-objects.applescript "$PWD/samples/0096/textstyle.key" textstyle
```

## Observation

The recipe makes a text item `box` on slide 1 and sets the `font` of its text to Georgia, the `size` to 40 and the `color` to red. `DocumentStylesheet.iwa` gained one record, an unnamed type-2022 paragraph style:

```
1: { 3: { 1: 2651133 }, 4: 1, 5: { 1: 2652414 } }     ← parent: Body
10: 3
11: { 3: 40.0, 5: "Georgia", 7: (1.0, 0.149, 0.0, alpha 1.0) }
```

## Conclusion

Formatting all of a text box's text gives its paragraph an unnamed paragraph style that sets the changed character properties, as in Pages. A character style isn't used. Field 10 is 3 for three properties, which again fits it counting the properties a style sets. Red is stored as in Pages and Numbers, (1.0, 0.149, 0.0).

## Confidence

*Likely*: whole-text formatting in Keynote makes an unnamed paragraph style, as in Pages.
