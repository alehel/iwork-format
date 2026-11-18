# 0448: Writing a build's stages

**Status:** run

A build is a type-8 record listed in slide field 2, and slide field 43 lists type-153 records, probably the build order; a build's stages are probably its type-153 records, one per stage ([0257](0257-build.md), [0368](0368-writing-a-build-delivery.md)). Keynote exports a slide's build stages as separate images. This experiment removes each list and repeats the stage, and compares the images with the slide without a build.

## Setup

| | |
| --- | --- |
| Keynote | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/theme/0257/build.key`: a slide (2655467) whose title builds in, with build 2655727 in field 2 and stage record 2655732 (type 153) in field 43. `samples/theme/0257/plain.key`: the same slide without a build |
| Writer | [`recipes/0381-show-object.py`](../recipes/0381-show-object.py) to add an entry and [`recipes/0412-drop-field.py`](../recipes/0412-drop-field.py) to remove a list; exported with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) |

## Recipe

```bash
mkdir -p samples/0448
O=samples/0448
F=samples/theme/0257/build.key
cp $F $O/build.key
cp samples/theme/0257/plain.key $O/plain.key
python3 -I recipes/0381-show-object.py $F $O/stage-twice.key 2655467 2655732 43
python3 -I recipes/0412-drop-field.py $F $O/no-stages.key 2655467 43
python3 -I recipes/0412-drop-field.py $F $O/no-builds.key 2655467 2
for f in plain build stage-twice no-stages no-builds; do
  mkdir -p $O/img-$f
  sh recipes/0372-in-app.sh Keynote $O/$f.key \
    "export d to POSIX file \"$PWD/$O/img-$f\" as slide images with properties {image format:PNG, all stages:true}"
done
```

Each image was compared with `plain.key`'s with [`recipes/0449-image-diff.swift`](../recipes/0449-image-diff.swift), added in the next experiment, which counts differing pixels over every second pixel.

## Observation

| File | Written | Images | Image 1 | Image 2 |
| --- | --- | --- | --- | --- |
| `plain.key` | (no build) | 1 | | |
| `build.key` | (as made) | 2 | 2,253 sampled pixels differ: no title | same as plain |
| `stage-twice.key` | 2655732 twice in field 43 | 2 | as `build.key` | same as plain |
| `no-stages.key` | field 43 removed | 1 | same as plain | |
| `no-builds.key` | field 2 removed | 1 | same as plain | |

## Conclusion

A build plays only when both lists are there: without its stage record in slide field 43, the build in field 2 is ignored and the title is shown from the start, and without field 2 the stage record does nothing either. Listing the same stage twice doesn't add a stage. So field 43 lists the stages to play, each naming its build, and a writer adding a build must add both the build and its stage. How a delivery in several steps is stored is still open, since Keynote doesn't let its delivery be set from a script.

## Confidence

*Confirmed*: a build needs both its entry in slide field 2 and a type-153 stage in field 43, and a stage listed twice plays once, by writing them.
