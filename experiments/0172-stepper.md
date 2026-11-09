# 0172: A stepper

**Status:** run

This experiment gives a cell the stepper format.

## Setup

| | |
| --- | --- |
| Numbers | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0171](0171-slider.md) |

## Recipe

```bash
mkdir -p samples/0172
osascript recipes/0169-numbers-controls.applescript stepper "$PWD/samples/0172/stepper.numbers"
```

Cell B2 of table 1 is decoded from `Index/Tables/Tile.iwa` as in [0036](0036-more-cell-formats.md).

## Observation

B2 has the same flags as the slider in [0171](0171-slider.md), holding 5. The cell-control entry is `{ 1: 4, 3: 1.0, 4: 100.0, 5: 1.0 }`, the same as the slider's apart from field 1, and the format list's entry is the same.

## Conclusion

A stepper is control kind 4. Sliders and steppers have the same range defaults and number format, so a reader that can't draw either control can show the number.

| 12.1 | Control |
| --- | --- |
| 4 | Stepper |
| 5 | Slider |
| 6 | Rating |
| 8 | Checkbox |

## Confidence

*Likely*: cell-control kinds 4 stepper, 5 slider, 6 rating and 8 checkbox ([0169](0169-unchecked-checkbox.md)–this experiment).
