# 0304: Writing an image's opacity and reflection

**Status:** run

An image's style (type 3016) was read as holding its opacity in field 11.2, from 0 to 1 ([0057](0057-image-opacity.md)), and its reflection in 11.4, with the strength in 11.4.1 ([0099](0099-image-reflection.md)). AppleScript reads an image's `opacity`, `reflection showing` and `reflection value`. This experiment writes both properties and asks Keynote.

## Setup

| | |
| --- | --- |
| Keynote | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/theme/0099/reflection.key`: an image with a 40 % reflection, in the test theme |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py) |

## Recipe

```bash
mkdir -p samples/0304
cp samples/theme/0099/reflection.key samples/0304/original.key
python3 -I recipes/0302-set-path.py samples/0304/original.key samples/0304/written.key 2655570 \
  11.2 float 0.4 11.4.1 float 0.75
```

Record 2655570 is the image's own style, an unnamed child of the theme's image style. It holds only the reflection, 11.4.1 = 0.4; the opacity comes from the parent. The script adds 11.2 = 0.4 and sets the reflection to 0.75. Keynote opened each file on its own through Launch Services and read the image's properties, and the written file was saved again.

## Observation

| File | opacity | reflection showing | reflection value |
| --- | --- | --- | --- |
| `original.key` | 100 | true | 40 |
| `written.key` | 40 | true | 75 |

## Conclusion

Image style field 11.2 is the opacity and 11.4.1 the reflection's strength, both fractions from 0 to 1 that AppleScript shows as percentages. A property can be set in an object's own child style without touching the theme's style it inherits from.

## Confidence

*Confirmed*: image style fields 11.2 and 11.4.1, by writing them.
