# 0314: Writing the slide size

**Status:** run

[0075](0075-slide-size.md) confirmed that field 4 of the presentation record (type 2) is the slide size in points. AppleScript reads a presentation's `width` and `height`. This experiment writes a new size and asks Keynote, and looks at what happens to the slides' objects.

## Setup

| | |
| --- | --- |
| Keynote | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/theme/0025/hello.key`: 1920 × 1080, in the test theme; its presentation record is 2652410 |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py) |

## Recipe

```bash
mkdir -p samples/0314
cp samples/theme/0025/hello.key samples/0314/original.key
python3 -I recipes/0302-set-path.py samples/0314/original.key samples/0314/written.key 2652410 4.1 float 1024 4.2 float 768
```

Keynote opened each file on its own and read the presentation's size and the first slide's title placeholder through AppleScript; the written file was saved again.

## Observation

| File | Slide size | Title position | Title width |
| --- | --- | --- | --- |
| `original.key` | 1920 × 1080 | 95, 203 | 1730 |
| `written.key` | 1024 × 768 | 95, 203 | 1730 |

## Conclusion

Field 4.1 is the slide width and 4.2 the height, floats in points, and Keynote uses them as written. The objects keep their geometry, so in the written file the title runs past the slide's right edge. Keynote's own Slide Size setting also moves and scales the objects; a writer that changes the size has to do that itself.

## Confidence

*Confirmed*: presentation fields 4.1 and 4.2, by writing them. *Likely*: writing them doesn't rescale anything.
