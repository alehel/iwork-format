# 0071: A transition

**Status:** run

[0046](0046-slide-layout.md) found the text `Transition` and `none` in a template slide. This experiment gives a slide a dissolve transition of 2 seconds.

## Setup

| | |
| --- | --- |
| Keynote | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0025](0025-keynote-title.md), `empty.key` |

## Recipe

```bash
mkdir -p samples/0071
osascript recipes/0068-keynote-variants.applescript "$PWD/samples/0071/transition.key" transition
```

The recipe sets slide 1's `transition properties` to the effect `dissolve` with a duration of 2 seconds.

## Observation

The slide (type 5) changed in field 4.2.8:

```
2: "none" → "apple:dissolve"
3: 1.0 → 2.0                     (a double)
11: a number that changed too
```

The slide's node (type 4) changed field 7 from 0 to 1.

## Conclusion

A slide's transition is in its field 4.2.8: the effect as a name in field 2 (`none`, `apple:dissolve`), and the duration in seconds in field 3. The default for no transition is 1 second. Slide node field 7 becomes 1 with a transition, so it may mark the slide as having one.

## Confidence

*Likely*: slide field 4.2.8.2 is the transition effect's name, and 4.2.8.3 its duration in seconds.

*Unknown*: field 4.2.8.11 and slide node field 7.
