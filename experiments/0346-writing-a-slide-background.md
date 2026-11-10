# 0346: Writing a slide's background colour

**Status:** run

A slide's background is the fill in its slide style (type 9), property 11.1 ([0271](0271-dynamic-background.md)), with a colour in 11.1.1 laid out as other colours. This experiment writes a colour into a slide's style and samples the slide Keynote exports.

## Setup

| | |
| --- | --- |
| Keynote | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/theme/0025/hello.key`: a slide in the test theme, whose slide field 1 names `slide-0-slidestyle` (record 2651744), with a white fill (1, 1, 1, colour space 1) |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py) |

## Recipe

```bash
mkdir -p samples/0346/img-o samples/0346/img-w
cp samples/theme/0025/hello.key samples/0346/original.key
python3 -I recipes/0302-set-path.py samples/0346/original.key samples/0346/written.key 2651744 \
  11.1.1.3 float 1.0 11.1.1.4 float 0.9 11.1.1.5 float 0.6
```

The style is the theme's named style, shared with the layouts, so every slide using it changes. Keynote opened each file on its own and exported its slides as PNG images; the pixel near each image's corner was read.

## Observation

Keynote exports PNG images with a Display P3 profile.

| File | Corner pixel (Display P3) |
| --- | --- |
| `original.key` | 1.000, 1.000, 1.000 |
| `written.key` | 0.984, 0.902, 0.639 |

1.0, 0.9, 0.6 in sRGB is 0.983, 0.904, 0.638 in Display P3.

## Conclusion

The slide style's 11.1.1 is the slide's background colour, and Keynote draws exactly the sRGB colour written, converted to the image's Display P3 profile on export. Comparing colours from exported images needs that conversion; read raw, they aren't the stored values.

## Confidence

*Confirmed*: slide style 11.1.1 is the background colour, by writing it.
