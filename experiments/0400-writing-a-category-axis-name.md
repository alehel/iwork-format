# 0400: Writing a category axis name

**Status:** run

A chart's category axis shows its name when its settings record (type 5027, named by chart field 10000.16) has 10000.13 = 1. The value axis uses 10000.14 for the same switch ([0297](0297-chart-category-axis.md), [0399](0399-writing-chart-border-and-axes.md)). This experiment writes each field into the category axis's settings and compares the slide with Keynote's own.

## Setup

| | |
| --- | --- |
| Keynote | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/0297/baseline.key`: a bar chart in the test theme whose category axis settings, record 2655561, are empty. Keynote's own version with the name shown: `samples/0297/x-axis-name.key` |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py); exported with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) and compared with [`recipes/0399-pdf-diff.swift`](../recipes/0399-pdf-diff.swift) |

## Recipe

```bash
mkdir -p samples/0400
R=recipes/0302-set-path.py
B=samples/0297/baseline.key
O=samples/0400
cp $B $O/baseline.key
cp samples/0297/x-axis-name.key $O/keynote-x-axis-name.key
python3 -I $R $B $O/category-name.key 2655561 10000.13 varint 1
python3 -I $R $B $O/category-14.key 2655561 10000.14 varint 1
for f in $O/*.key; do
  sh recipes/0372-in-app.sh Keynote $f "export d to POSIX file \"$PWD/${f%.key}.pdf\" as PDF"
done
swift recipes/0399-pdf-diff.swift $O/baseline.pdf $O/keynote-x-axis-name.pdf $O/category-name.pdf $O/category-14.pdf
swift recipes/0374-pdf-text.swift $O/*.pdf
```

## Observation

| File | Written | Pixels differing from the baseline | Text added |
| --- | --- | --- | --- |
| `keynote-x-axis-name.pdf` | (Keynote's own) | 8,167, in 899.5, 891.5 – 1095.5, 923.5 | `Kategoriakse` |
| `category-name.pdf` | 10000.13 = 1 | the same 8,167, identical to Keynote's | `Kategoriakse` |
| `category-14.pdf` | 10000.14 = 1 | none | |

## Conclusion

Field 10000.13 of the category axis's settings shows its name, *Kategoriakse* (category axis) in a Norwegian Keynote, below the chart, exactly as Keynote draws it. The value axis's field, 10000.14, does nothing in the category axis's settings: each kind of axis reads its own field, even though both live in type-5027 records.

## Confidence

*Confirmed*: category axis setting 10000.13 as showing its name, by writing it, and that 10000.14 doesn't do so there.
