# 0449: Writing a build's direction

**Status:** run

A build's effect is in its field 4.18, with `In`, `Out` or `Action` in 4.18.1 for a build-in, build-out or action ([0263](0263-build-out.md), [0264](0264-action-build.md)). This experiment turns a build-in into a build-out by writing that text, and compares the exported stages with the slide without a build.

## Setup

| | |
| --- | --- |
| Keynote | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/theme/0257/build.key`: a slide whose title builds in, build 2655727 with 4.18.1 = `In` and the effect `apple:dissolve character`. `samples/theme/0257/plain.key`: the same slide without a build |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py); exported with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) and compared with the new [`recipes/0449-image-diff.swift`](../recipes/0449-image-diff.swift) |

## Recipe

```bash
mkdir -p samples/0449
O=samples/0449
cp samples/theme/0257/plain.key $O/plain.key
python3 -I recipes/0302-set-path.py samples/theme/0257/build.key $O/out.key 2655727 4.18.1 string Out
for f in plain out; do
  mkdir -p $O/img-$f
  sh recipes/0372-in-app.sh Keynote $O/$f.key \
    "export d to POSIX file \"$PWD/$O/img-$f\" as slide images with properties {image format:PNG, all stages:true}"
done
swift recipes/0449-image-diff.swift $O/img-plain/*.png $O/img-out/*.png
```

## Observation

| Images | Compared with the plain slide |
| --- | --- |
| `img-out.001.png` | the same: the title is shown |
| `img-out.002.png` | 2,253 sampled pixels differ: the title is gone |

As a build-in ([0448](0448-writing-a-build-s-stages.md)), the same build gave the opposite: no title in the first image, the title in the second.

## Conclusion

Field 4.18.1 decides the build's direction: written `Out`, the title is on the slide at first and the build takes it away, where `In` brings it on. The effect, its identifier in 4.18.2, stays the same, so the same dissolve plays either way. A reader showing a slide's starting or final state must apply builds by their direction.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `plain.key` | `theme/0257/plain.key` | `same bytes` | *Control*: the title is shown |
| `out.key` | `theme/0257/build.key` | Only `8#2655727 4.18.1: "In" → "Out"` | *Confirmed*: field 4.18.1 is the build's direction; the title is there at first, then gone |

## Confidence

*Confirmed*: field 4.18.1 as the build's direction, by writing `Out` into a build-in.
