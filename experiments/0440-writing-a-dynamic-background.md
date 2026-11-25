# 0440: Writing a dynamic background

**Status:** run

A Keynote slide with a dynamic background has an image fill showing a pre-rendered still, a `motionBackground-…` data file, and field 200 naming a type-26 motion background style, which holds the generator's name, such as `KNGradientLinearBase`, colour stops as in a gradient fill (11.3.2), and its parameters ([0271](0271-dynamic-background.md)). This experiment replaces the still and changes the stops, and reads the colours of the exported slide.

## Setup

| | |
| --- | --- |
| Keynote | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/theme/0271/dynamic.key`: one slide with the *Rainbow* dynamic background, in the test theme. Its still is `Data/motionBackground-9094.jpeg`, data ID 9094, and its motion style is 2651723, with six colour stops |
| Writer | [`recipes/0395-data-file.py`](../recipes/0395-data-file.py) for the still and [`recipes/0383-set-nth-path.py`](../recipes/0383-set-nth-path.py) for the stops; exported with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) and read with [`recipes/0384-pdf-colours.swift`](../recipes/0384-pdf-colours.swift) |

## Recipe

```bash
mkdir -p samples/0440
O=samples/0440
F=samples/theme/0271/dynamic.key
cp $F $O/original.key
sips -s format jpeg samples/0395/green-8x4.png --out $O/green.jpeg
python3 -I recipes/0395-data-file.py $F $O/still-green.key 9094 --replace $O/green.jpeg
args=(); for i in 1 2 3 4 5 6; do args+=(11.3.2.2:$i.1.3 float 1 11.3.2.2:$i.1.4 float 0 11.3.2.2:$i.1.5 float 0); done
python3 -I recipes/0383-set-nth-path.py $F $O/motion-red.key 2651723 "${args[@]}"
for f in original still-green motion-red; do
  sh recipes/0372-in-app.sh Keynote $O/$f.key "export d to POSIX file \"$PWD/$O/$f.pdf\" as PDF"
  swift recipes/0384-pdf-colours.swift $O/$f.pdf 100,100 960,540 1800,1000
done
```

`motion-red.key` makes all six stops pure red.

## Observation

Colours at the top left, the centre and the bottom right of the 1920 × 1080 slide:

| File | Written | (100, 100) | (960, 540) | (1800, 1000) |
| --- | --- | --- | --- | --- |
| `original.key` | | 0, 1, 0.66 | 0, 0.98, 0.45 | 0.46, 0.95, 0.25 |
| `still-green.key` | the still replaced by plain green | the same | the same | the same |
| `motion-red.key` | all stops red | 1, 0, 0 | 1, 0, 0 | 1, 0, 0 |

## Conclusion

Keynote draws a dynamic background from its motion style, rendering it again when it exports, and doesn't use the still in the image fill: replacing the still changed nothing, while red stops made the whole slide red. The still is there for whatever can't render the motion, such as other readers and previews. So a reader that can't run Keynote's generators should show the still, and a writer that changes a dynamic background should render a new still to go with it.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `original.key` | `theme/0271/dynamic.key` | `same bytes` | *Control* |
| `still-green.key` | `original.key` | Only `part Data/motionBackground-9094.jpeg: changed` | *Confirmed*: Keynote ignores the still; the colours stay the same |
| `motion-red.key` | `original.key` | Only `26#2651723 11.3.2.2.1.3: changed`, `26#2651723 11.3.2.2.1.4: changed`, `26#2651723 11.3.2.2.1.5: changed`, `26#2651723 11.3.2.2.1.3 = 1.0` | *Confirmed*: Keynote draws the background from the motion style's stops; the slide is red |

## Confidence

*Confirmed*: Keynote renders a dynamic background from its motion style's stops and ignores the still, by writing them.
