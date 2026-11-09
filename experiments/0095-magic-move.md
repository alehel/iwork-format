# 0095: Magic Move

**Status:** run

This experiment tries the *Magic Move* transition, which animates objects from one slide to the next, to see what more it stores than a simple effect.

## Setup

| | |
| --- | --- |
| Keynote | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0025](0025-keynote-title.md), `empty.key` (no transition), and experiment [0071](0071-transition.md) (dissolve) |

## Recipe

```bash
mkdir -p samples/0095
osascript recipes/0091-keynote-transitions.applescript "$PWD/samples/0095/magicmove.key" magicmove
```

## Observation

The recipe sets slide 1's transition to `magic move`, 1 second. The slide's field 4.2.8 changed:

```
2: "none" → "apple:magic-move-implied-motion-path"
13: (absent) → 1
15: (absent) → 4
16: (absent) → 1
```

## Conclusion

Magic Move is stored as `apple:magic-move-implied-motion-path`, with three more fields (13, 15 and 16) that the simple effects don't set. They probably hold its options, such as how objects are matched and how text moves. They aren't decoded here.

## Confidence

*Likely*: Magic Move's stored name.

*Unknown*: transition fields 13, 15 and 16.
