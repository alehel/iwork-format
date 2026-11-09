# 0094: An automatic transition

**Status:** run

[0071](0071-transition.md) found the transition's effect and duration. This experiment makes a transition start by itself after a delay, instead of on a click.

## Setup

| | |
| --- | --- |
| Keynote | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0025](0025-keynote-title.md), `empty.key` (no transition), and experiment [0071](0071-transition.md) (dissolve) |

## Recipe

```bash
mkdir -p samples/0094
osascript recipes/0091-keynote-transitions.applescript "$PWD/samples/0094/auto.key" auto
```

## Observation

The recipe sets slide 1's transition to `dissolve`, 1 second, `automatic transition` true and `transition delay` 3 seconds. The slide's field 4.2.8 changed:

```
2: "none" → "apple:dissolve"
5: 0.5 → 3.0
6: 0 → 1
```

## Conclusion

Field 4.2.8.6 is 1 when the transition starts automatically, and 4.2.8.5 is the delay before it, in seconds. The default delay is 0.5 seconds, stored even when the transition waits for a click.

## Confidence

*Likely*: transition field 6 is the automatic switch and field 5 the delay in seconds.
