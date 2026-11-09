# 0257: A build

**Status:** run

Keynote can animate an object onto a slide (a build). Builds are added in the Animate sidebar, which needs Keynote in front. This experiment adds a Dissolve build-in to a slide's title.

## Setup

| | |
| --- | --- |
| Keynote | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `samples/0257/plain.key`, the same slide without a build |

## Recipe

1. Make a presentation whose first slide's title is `One`:
   ```bash
   osascript -e 'tell application "Keynote"' -e 'set d to make new document' \
     -e 'set object text of default title item of slide 1 of d to "One"' -e 'end tell'
   ```
2. With Keynote in front, click the title once to select its box, open the Animate sidebar, and choose Add an Effect → Dissolve (*Legg til en effekt → Overtoning*) on the Build In tab. The sidebar shows a duration of 1 s and delivery All at Once (*Alt samtidig*).
3. Save it as `samples/0257/build.key`. For the baseline, make the same presentation and save it without a build.

## Observation

The slide's part gains a type-8 record and a type-153 record. The slide record (type 5) gains field 2, naming the type-8 record, and field 43, naming the type-153 record.

The type-8 record:

```
1: { 1: 2652199 }                 ← the title placeholder
2: "All at Once"
3: 0.0
4: { 4: 1, 17: 60.0,
     18: { 1: "In", 2: "apple:dissolve character", 3: 1.0, 5: 0.0, … },
     20: 1, 21: 1 }
5: 1
```

The type-153 record names the type-8 record in field 1, and holds 1.0 in field 4 and a 128-bit ID.

## Conclusion

A build is a type-8 record listed by the slide in field 2:

- **Field 1:** the object it animates.
- **Field 2:** its delivery, as an English name.
- **Field 4.18:** the effect. Field 1 is `In` for a build-in, field 2 the effect's identifier, and field 3 its duration in seconds.

Effect identifiers use the `apple:` form of transition names ([0196](0196-every-transition.md)). Here it is `apple:dissolve character`, not `apple:dissolve`. Slide field 43 lists type-153 records, probably the build order shown in the Build Order window, each naming a build. A reader that only shows slides can ignore builds and draw every object.

## Confidence

*Likely*: builds are type-8 records in slide field 2, with their target in field 1 and their effect in 4.18.

*Unknown*:

- The type-153 records beyond naming a build.
- Fields 3, 4.4, 4.17, 4.20, 4.21 and 5.
