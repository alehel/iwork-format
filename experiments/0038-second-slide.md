# 0038: A second slide

**Status:** run

[0027](0027-document-roots.md) followed Keynote's root through a presentation (type 2) and a slide node (type 4) to a slide (type 5) in its own part. With one slide, it couldn't show how slides are listed. This experiment adds a second slide.

## Setup

| | |
| --- | --- |
| Keynote | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0025](0025-keynote-title.md), `hello.key` |

## Recipe

```bash
mkdir -p samples/0038
osascript recipes/0038-keynote-two-slides.applescript "$PWD/samples/0038/two-slides.key"
```

The recipe sets slide 1's title to `first`, adds a slide with `make new slide`, and sets its title to `second`. Opening the saved file in Keynote through AppleScript reports 2 slides, the second titled `second`.

## Observation

The presentation (object 2652410, type 2):

```
2: { 1: 2651112 }
3: { 2: { 1: 2652174 }, 2: { 1: 2652533 } }     ← two slide nodes
4: { 1: 1920.0, 2: 1080.0 }
5: { 1: 2652414 }                               ← the stylesheet (type 401)
```

| | Slide 1 | Slide 2 |
| --- | --- | --- |
| Slide node (type 4) | 2652174 | 2652533 |
| Node field 2: the slide | 2652175 | 2652493 |
| Node fields 10 and 16: thumbnail size and data ID | 356 × 200, 9058 | absent |
| Part holding the slide | `Index/Slide-2652175.iwa` | `Index/Slide.iwa` |
| Title text record | 2652192, `first` | 2652492, `second` |

`Document.iwa` also holds 17 more slide nodes (type 4), one for each template slide. Each has a thumbnail size and data ID like slide 1's, and points at a slide in a `TemplateSlide-N.iwa` part.

## Conclusion

The presentation's field 3 lists the slide nodes in show order, in its repeated field 2. Its field 4 is the slide size in points: 1920 × 1080 for this Wide theme. To list a presentation's slides, a reader goes:

- root → presentation
- field 3.2 → slide nodes
- each node's field 2 → a slide

Slides live in parts named like other one-record parts ([container.md](../spec/container.md)): `Slide-N.iwa`, or `Slide.iwa` without a number. A reader should find a slide by its ID, not by the part name.

A slide added through AppleScript had no thumbnail when saved: its node has no fields 10 and 16. A reader can't rely on every slide having a thumbnail.

The template slides' nodes aren't listed in field 3.2. Whatever lists them is still to be found.

## Confidence

*Likely*:

- Presentation field 3.2 is the ordered list of slide nodes, and field 4 is the slide size.
- Slide parts may be named without a number.
- A slide node's thumbnail is optional.

*Unknown*:

- Where the template slides are listed.
- Presentation field 2 (object 2651112).
