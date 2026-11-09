# 0263: A build-out

**Status:** run

[0257](0257-build.md) found that a build-in is a type-8 record whose effect, in field 4.18, starts with `In`. This experiment adds the same effect as a build-out instead, which removes the object from the slide.

## Setup

| | |
| --- | --- |
| Keynote | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0257](0257-build.md), `build.key` |

## Recipe

As in 0257, but on the Animate sidebar's Build Out tab (*Bygg ut*): choose Add an Effect → Dissolve (*Overtoning*), then save as `samples/0263/build-out.key`.

## Observation

The slide again gains one type-8 build and one type-153 record. The build differs from 0257's only in its random-looking field 4.18.11 and in:

```
4.18.1: "In" → "Out"
```

The effect identifier is the same, `apple:dissolve character`.

## Conclusion

Build-ins and build-outs are the same type-8 record. Field 4.18.1 says which, as the English word `In` or `Out`, and the effect identifier is shared. A reader showing the end state of a slide should hide objects with a build-out. One showing the start state should hide objects with a build-in.

## Confidence

*Confirmed*, with 0257: builds are type-8 records with their effect in field 4.18.

*Likely*: field 4.18.1 is `In` or `Out`. Actions, Keynote's third kind of build, probably use a third value.
