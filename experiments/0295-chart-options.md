# 0295: A chart's title, legend, border and caption

**Status:** run

[0067](0067-chart.md) to [0086](0086-chart-grouped-by-column.md) found where a chart's data, type and grouping are kept. This experiment turns on each of the four Chart Options in Keynote's Format sidebar in turn, to find where a chart's own title, legend, border and caption are stored.

## Setup

| | |
| --- | --- |
| Keynote | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Theme | The test theme ([0291](0291-test-theme.md)) |
| Chart | A 2D vertical bar chart from the [0067](0067-chart.md) recipe: rows `r1` and `r2`, columns `a`, `b` and `c` |

## Recipe

```bash
mkdir -p samples/0295
IWORK_KEYNOTE_THEME='iwork-format test' osascript recipes/0067-keynote-chart.applescript "$PWD/samples/0295/baseline.key"
```

A copy of the same presentation was opened and the chart clicked to select it. On the Format sidebar's Chart tab, under Chart Options (*Diagramvalg*), one option at a time was turned on: Title (*Tittel*), Legend (*Forklaring*), Border (*Kantlinje*) and Caption (*Infotekst*). After each, the presentation was saved under a new name through AppleScript (`save front document in`) and the option turned off again, giving `title.key`, `legend.key`, `border.key` and `caption.key`.

Keynote autosaved the open file while the options were being changed. The first baseline, taken from that file, picked up the border and was set aside, so each version is compared with `baseline.key`, made separately by the recipe.

## Observation

A chart drawable (type 5021) names two records besides its data: field 10000.9 a chart style (type 5022) and field 10000.10 a type-5023 record of chart settings. In the baseline, 10000.9 names the theme's chart style, `chart-0-chart`, directly, and the type-5023 record has 10000.21 = 0.

| Option | What changes |
| --- | --- |
| Title | The type-5023 record gains 10000.21 = 1 |
| Legend | The type-5023 record gains 10000.20 = 1 |
| Border | Field 10000.9 names a new, unnamed chart style whose parent (1.3) is `chart-0-chart`. It holds one property, 10000.18 = 1, and field 10001 = 1 |
| Caption | Drawable field 1.11 names a type-633 caption instead of a type-3097 placeholder, as for other objects ([0228](0228-caption.md)) |

Each version shows the chart as set, and Keynote shows the title text as `Tittel` and the legend entries as the row names. Turning an option off again left 0 in the type-5023 record (10000.20 = 0 after the legend was turned off), not an absent field.

## Conclusion

A chart's title and legend switches are chart settings in its type-5023 record: 10000.21 for the title and 10000.20 for the legend, 1 when shown. The border is a chart style property, 10000.18, which Keynote sets by giving the chart an unnamed style that inherits from the theme's chart style, as it does for paragraph and character styles. The caption works as for any drawable. The title's own text wasn't found in these records; the default text may come from the app.

## Confidence

*Likely*: type 5023 field 10000.21 is the title switch and 10000.20 the legend switch; chart style property 10000.18 is the border.

*Unknown*: where an edited chart title's text is stored.
