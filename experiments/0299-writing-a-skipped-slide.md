# 0299: Writing a skipped slide

**Status:** run

[0070](0070-skipped-slide.md) read a slide node's field 4 as the flag that skips a slide in a slideshow. This experiment tests the reading by writing: it sets the flag in a file and asks Keynote, through AppleScript, which slides are skipped.

## Setup

| | |
| --- | --- |
| Keynote | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/theme/0038/two-slides.key`, two slides in the test theme ([0292](0292-test-theme-reruns.md)) |
| Writer | [`recipes/0299-skip-slide.py`](../recipes/0299-skip-slide.py), using the writer of [0287](0287-rewriting-a-document.md) |

## Recipe

```bash
mkdir -p samples/0299
cp samples/theme/0038/two-slides.key samples/0299/two-slides.key
python3 -I recipes/0299-skip-slide.py samples/0299/two-slides.key samples/0299/second-skipped.key 2655609
```

Record 2655609 is the second slide's node (type 4), whose field 4 is 0. The script sets it to 1. Keynote then opened the original and the written file through AppleScript, read each slide's `slide number` and `skipped`, and saved the written one again as `resaved.key`.

Keynote at first refused to open the plain copy `two-slides.key`, saying it couldn't be opened at the moment because the operation wasn't permitted, while another document was still open. With all documents closed, the written file opened. Pages behaved the same way with some copies in an earlier attempt that wasn't written up, so this looks like a limit of the apps, not of the files.

## Observation

| File | Slide 1 | Slide 2 |
| --- | --- | --- |
| Original | number 1, not skipped | number 2, not skipped |
| `second-skipped.key` | number 1, not skipped | number −1, skipped |

In `resaved.key`, the second slide node still has field 4 = 1 and the first 0.

## Conclusion

Field 4 of a slide node is the slide's skipped flag: written as 1, it makes Keynote treat the slide as skipped, which AppleScript reports with the slide number −1, and Keynote keeps it when saving. A slide that isn't skipped has the field as 0, not absent.

## Confidence

*Confirmed*: slide node field 4 = 1 skips the slide.
