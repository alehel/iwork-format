# 0379: Writing a slide's layout

**Status:** run

A slide's field 17 names its layout, a template slide whose field 10 is the layout's name ([0046](0046-slide-layout.md), [0165](0165-slide-layouts.md)). AppleScript reads a slide's layout as its `base layout`. This experiment points a slide at other layouts.

## Setup

| | |
| --- | --- |
| Keynote | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-17 |
| Input | `samples/theme/0160/move.key`: three slides in the test theme. The second, A, is slide 2655467 on the layout *Tittel* (template slide 2651742); the other two use *Tittel og punkttegn* (2651826) |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py); read back with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) |

## Recipe

```bash
mkdir -p samples/0379
R=recipes/0302-set-path.py
F=samples/theme/0160/move.key
cp $F samples/0379/original.key
python3 -I $R $F samples/0379/rewritten.key 2655467 17.1 varint 2651742
python3 -I $R $F samples/0379/same-as-c.key 2655467 17.1 varint 2651826
python3 -I $R $F samples/0379/picture.key 2655467 17.1 varint 2651768
python3 -I $R $F samples/0379/blank.key 2655467 17.1 varint 2652157
for f in rewritten same-as-c picture blank; do
  sh recipes/0372-in-app.sh Keynote samples/0379/$f.key 'set out to {}
repeat with s in slides of d
  set end of out to {name of base layout of s, object text of default title item of s}
end repeat
return out'
done
```

`rewritten.key` writes the value already there, as a check on the writer.

## Observation

| File | Field 17 written | Result |
| --- | --- | --- |
| `rewritten.key` | 2651742, *Tittel* (unchanged) | opens: *Tittel og punkttegn* C, *Tittel* A, *Tittel og punkttegn* B |
| `same-as-c.key` | 2651826, *Tittel og punkttegn* | Keynote quits while opening it |
| `picture.key` | 2651768, *Tittel og bilde* | Keynote quits while opening it |
| `blank.key` | 2652157, *Tom* | Keynote quits while opening it |

Each failure was repeated with Keynote freshly started, with the same result. The slide's other references explain why the layout can't change alone. Besides 17, slide 2655467 refers to a slide style (2651744, type 9), and its title, body and slide-number placeholders (type 7) refer to paragraph styles 2651745, 2651750 and 2651755 (type 2025); all four are in `DocumentStylesheet.iwa` and belong to the *Tittel* layout.

## Conclusion

Field 17 does name the slide's layout: rewriting it with its own value keeps it, and AppleScript reports the template slide's name. But it can't be changed on its own. Keynote expects the slide's style and its placeholders to match the layout's, and a slide pointing at another layout while keeping the old one's placeholders makes Keynote quit. A writer that changes a slide's layout has to rebuild the slide's placeholders from the new layout, as Keynote does; a reader can still take a slide's layout from field 17.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `original.key` | `theme/0160/move.key` | `same bytes`, `5#2655467 17.1 = 2651742` | *Control* |
| `rewritten.key` | `original.key` | `same records`, `same parts` | *Likely*: Keynote opens it and reports the layout field 17 names |
| `same-as-c.key` | `original.key` | Only `5#2655467 17.1: 2651742 → 2651826` | *Likely*: the layout can't be changed alone: Keynote quits while opening it |
| `picture.key` | `original.key` | Only `5#2655467 17.1: 2651742 → 2651768` | *Likely*: as above |
| `blank.key` | `original.key` | Only `5#2655467 17.1: 2651742 → 2652157` | *Likely*: as above |

## Confidence

*Likely*: field 17 as the slide's layout (read back, not changed). *Likely*: a slide's placeholders must belong to its layout. The follow-up is to write a slide whose placeholders and style are taken from the new layout.
