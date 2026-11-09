# 0093: The cube transition

**Status:** run

[0071](0071-transition.md) found a slide's transition in its field 4.2.8: the effect's name in field 2 and its duration in field 3. This experiment, one of five (0091–0095), tries a different effect, to see how AppleScript's names map to the stored ones.

## Setup

| | |
| --- | --- |
| Keynote | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0025](0025-keynote-title.md), `empty.key` (no transition), and experiment [0071](0071-transition.md) (dissolve) |

## Recipe

```bash
mkdir -p samples/0093
osascript recipes/0091-keynote-transitions.applescript "$PWD/samples/0093/cube.key" cube
```

## Observation

The recipe sets slide 1's transition to `cube`, 1.5 seconds. The slide's field 4.2.8 changed:

```
2: "none" → "apple:3D-cube"
3: 1.0 → 1.5
12: (absent) → 1
```

The slide node's field 7 became 1, as in 0071.

## Conclusion

The stored name of AppleScript's `cube` effect is `apple:3D-cube`. Effect names are Keynote's own identifiers with an `apple:` prefix, not AppleScript's names, so a reader needs a table from one to the other. The duration is in field 3, in seconds.

## Confidence

*Likely*: `cube` is stored as `apple:3D-cube`.
