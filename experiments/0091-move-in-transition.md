# 0091: The move in transition

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
mkdir -p samples/0091
osascript recipes/0091-keynote-transitions.applescript "$PWD/samples/0091/movein.key" movein
```

## Observation

The recipe sets slide 1's transition to `move in`, 1.5 seconds. The slide's field 4.2.8 changed:

```
2: "none" → "apple:slide"
3: 1.0 → 1.5
```

The slide node's field 7 became 1, as in 0071.

## Conclusion

The stored name of AppleScript's `move in` effect is `apple:slide`. Effect names are Keynote's own identifiers with an `apple:` prefix, not AppleScript's names, so a reader needs a table from one to the other. The duration is in field 3, in seconds.

## Confidence

*Likely*: `move in` is stored as `apple:slide`.
