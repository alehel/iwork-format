# 0303: Writing an object's position, size, rotation and lock

**Status:** run

A drawable's field 1.1 was read as its geometry: 1.1.1 the position and 1.1.2 the size of the unrotated box in points, 1.1.4 the rotation in degrees ([0055](0055-image-size.md), [0056](0056-image-rotation.md), [0097](0097-keynote-shape-rotation.md)); and field 1.5 as the lock ([0100](0100-locked-object.md)). AppleScript can read an object's position, width, height, rotation and lock. This experiment writes new values and asks Keynote.

## Setup

| | |
| --- | --- |
| Keynote | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/theme/0069/image.key`: the 8 × 4 red PNG of [0023](0023-an-image.md) on a slide, in the test theme |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py) |

## Recipe

```bash
mkdir -p samples/0303
cp samples/theme/0069/image.key samples/0303/original.key
python3 -I recipes/0302-set-path.py samples/0303/original.key samples/0303/written.key 2655552 \
  1.1.1.1 float 100 1.1.1.2 float 200 1.1.2.1 float 320 1.1.2.2 float 160 1.1.4 float 30 1.5 varint 1
```

Record 2655552 is the image (type 3005), at (956, 538), 8 × 4, unrotated and unlocked. Keynote opened each file on its own through Launch Services ([0302](0302-writing-a-transition.md)), read the image's properties through AppleScript, and saved the written file again.

## Observation

| File | Position | Size | Rotation | Locked |
| --- | --- | --- | --- | --- |
| `original.key` | 956, 538 | 8 × 4 | 0 | false |
| `written.key` | 81, 131 | 320 × 160 | 30 | true |

The written box is 320 × 160 at (100, 200). Turned 30° about its centre, its bounding box starts at (81.4, 130.7), which is what AppleScript reports as the position. The resaved file holds the values as written.

## Conclusion

The geometry fields are as read. 1.1.1 is the top-left corner of the unrotated box, 1.1.2 its size and 1.1.4 its rotation, all floats. AppleScript's `position` is the corner of the rotated object's bounding box instead, so it matches 1.1.1 only for unrotated objects. Field 1.5 = 1 locks the object.

## Confidence

*Confirmed*: drawable fields 1.1.1, 1.1.2, 1.1.4 and 1.5, by writing them.
