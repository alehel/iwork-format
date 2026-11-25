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

*Corrected 2026-11-25:* fields 13, 15 and 16 are next to 4.2.8, not inside it: they are 4.2.13, 4.2.15 and 4.2.16.

## Conclusion

Magic Move is stored as `apple:magic-move-implied-motion-path`, with three more fields (13, 15 and 16) that the simple effects don't set. They probably hold its options, such as how objects are matched and how text moves. They aren't decoded here.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `magicmove.key` | `0025/empty.key` | `5 4.2.8.2: "none" → "apple:magic-move-implied-motion-path"` | *Likely*: the stored name of Magic Move |

## Confidence

*Likely*: Magic Move's stored name.

*Unknown*: transition fields 13, 15 and 16.
