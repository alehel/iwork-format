# 0264: An action build

**Status:** run

[0257](0257-build.md) and [0263](0263-build-out.md) found that build-ins and build-outs are type-8 records, told apart by `In` or `Out` in field 4.18.1. Keynote's third kind of build, an action, moves or changes an object that stays on the slide. This experiment adds a rotation.

## Setup

| | |
| --- | --- |
| Keynote | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiments [0257](0257-build.md) and [0263](0263-build-out.md) |

## Recipe

As in 0257, but on the Animate sidebar's Action tab (*Hendelse*): choose Add an Effect → Rotate (*Roter*), then save as `samples/0264/action.key`. The sidebar shows 1 s, counter-clockwise, an angle of 45° and ease in and out.

## Observation

The slide gains a type-8 build. Its field 4 differs from the build-in's:

```
4.9:  45.0                       ← the angle
4.10: 32
4.13: 3
4.18: { 1: "Action", 2: "apple:action-rotation", 3: 1.0, … }
```

Fields 4.20 and 4.21, set to 1 in the build-in and build-out, are absent.

## Conclusion

Actions are type-8 builds too, with `Action` in field 4.18.1 and an `apple:action-…` identifier in 4.18.2. Their settings sit in field 4 beside the effect: the rotation angle in degrees is 4.9. Fields 4.10 and 4.13 probably hold the direction and the easing, which the sidebar showed as counter-clockwise and ease in and out. A reader showing a slide's end state would have to apply the action, here turning the title 45°.

## Confidence

*Confirmed*, with 0257 and 0263: every build is a type-8 record, its kind given by field 4.18.1.

*Likely*: field 4.9 is a rotation action's angle.

*Unknown*: fields 4.10 and 4.13.
