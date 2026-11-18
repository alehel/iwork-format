# 0450: Writing which object a build moves

**Status:** run

A build's field 1 names the object it animates ([0257](0257-build.md)). This experiment points a build at another object on the slide and compares the exported stages with the slide without a build.

## Setup

| | |
| --- | --- |
| Keynote | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/theme/0257/build.key`: slide 2655467 with the title `One` (placeholder 2655477) building in through build 2655727, and an empty body placeholder (2655492), whose text record is 2655491 |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py) and [`recipes/0412-drop-field.py`](../recipes/0412-drop-field.py); exported with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) and compared with [`recipes/0449-image-diff.swift`](../recipes/0449-image-diff.swift), which now also gives the box of the differing pixels |

## Recipe

```bash
mkdir -p samples/0450
O=samples/0450
R=recipes/0302-set-path.py
python3 -I $R samples/theme/0257/build.key $O/body-text.key 2655491 3 string "Body words"
python3 -I $R $O/body-text.key $O/build-body.key 2655727 1.1 varint 2655492
python3 -I recipes/0412-drop-field.py $O/body-text.key $O/no-build.key 2655467 2 43
for f in no-build body-text build-body; do
  mkdir -p $O/img-$f
  sh recipes/0372-in-app.sh Keynote $O/$f.key \
    "export d to POSIX file \"$PWD/$O/img-$f\" as slide images with properties {image format:PNG, all stages:true}"
done
swift recipes/0449-image-diff.swift $O/img-no-build/*.png $O/img-body-text/*.png $O/img-build-body/*.png
```

The body is given text so that its build shows. `no-build.key` drops the slide's builds and stages ([0448](0448-writing-a-build-s-stages.md)), so it shows the title and the body at once.

## Observation

| Stage | Differs from the slide without a build | Where, in pixels |
| --- | --- | --- |
| `body-text`, 1 | 2,253 sampled pixels | x 104–316, y 454–540: the title |
| `body-text`, 2 | none | |
| `build-body`, 1 | 1,556 sampled pixels | x 102–408, y 588–636: the body's line |
| `build-body`, 2 | none | |

## Conclusion

Field 1.1 of a build names the object it moves: pointed at the body, the build hides the body until its stage and leaves the title in place from the start. Everything else about the build, its effect and its stage, stayed the same.

## Confidence

*Confirmed*: build field 1 as the object it animates, by writing it.
