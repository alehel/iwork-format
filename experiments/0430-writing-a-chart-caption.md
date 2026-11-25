# 0430: Writing a chart's caption

**Status:** run

A chart's caption is drawable field 1.11, a type-633 text shape, as for other objects ([0295](0295-chart-options.md)). In Pages, writing a caption's text record changed the caption drawn ([0374](0374-writing-a-caption-and-title.md)). This experiment writes the caption of a Keynote chart.

## Setup

| | |
| --- | --- |
| Keynote | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/0295/caption.key`: a bar chart in the test theme with its caption shown and empty. The caption is type-633 record 2655884 (field 3 = 1, a caption), which refers to text record 2655885, without a field 3, and to a type-634 record |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py); exported with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh), read with [`recipes/0374-pdf-text.swift`](../recipes/0374-pdf-text.swift) and compared with [`recipes/0399-pdf-diff.swift`](../recipes/0399-pdf-diff.swift) |

## Recipe

```bash
mkdir -p samples/0430
O=samples/0430
cp samples/0295/caption.key $O/original.key
python3 -I recipes/0302-set-path.py $O/original.key $O/caption-text.key 2655885 3 string "Written chart caption"
for f in original caption-text; do
  sh recipes/0372-in-app.sh Keynote $O/$f.key "export d to POSIX file \"$PWD/$O/$f.pdf\" as PDF"
  swift recipes/0374-pdf-text.swift $O/$f.pdf
done
swift recipes/0399-pdf-diff.swift $O/original.pdf $O/caption-text.pdf
```

## Observation

| File | Caption's text | Text of the slide | Pixels differing from `original.pdf` |
| --- | --- | --- | --- |
| `original.key` | none | 6 4,5 3 1,5 0 a b c | |
| `caption-text.key` | `Written chart caption` | the same, then `Written chart caption` | 6,001, in 884, 883 – 1107, 905.5 |

The changed area is centred under the chart, near the bottom of the 1920 × 1080 slide.

## Conclusion

A chart's caption works as in Pages: the type-633 shape that the chart's drawable names holds the caption's text in its own text record, and Keynote draws what is written there, centred below the chart. An empty caption isn't drawn in an exported slide at all; Keynote shows its prompt only while editing.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `original.key` | `0295/caption.key` | `same bytes`, `2001#2655885 3 = absent` | *Control*: an empty caption isn't drawn |
| `caption-text.key` | `original.key` | Only `2001#2655885 3: absent → "Written chart caption"` | *Confirmed*: the text record holds the chart's caption, drawn below the chart |

## Confidence

*Confirmed*: a chart's caption as the text record of the type-633 shape it names, by writing it.
