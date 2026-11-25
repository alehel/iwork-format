# 0415: Writing a layout's name

**Status:** run

A Keynote layout is a template slide, a type-5 slide whose field 10 is its name in the app's language ([0046](0046-slide-layout.md), [0165](0165-slide-layouts.md)). This experiment writes new names and reads the layouts through AppleScript.

## Setup

| | |
| --- | --- |
| Keynote | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/theme/0160/move.key`, in the test theme: template slide 2651742 is *Tittel* (used by the second slide) and 2652157 *Tom* (blank, used by none) |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py); read back with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) |

## Recipe

```bash
mkdir -p samples/0415
R=recipes/0302-set-path.py
F=samples/theme/0160/move.key
O=samples/0415
cp $F $O/original.key
python3 -I $R $F $O/renamed.key 2651742 10 string "Written layout"
python3 -I $R $F $O/renamed-blank.key 2652157 10 string "Empty page"
for f in original renamed renamed-blank; do
  sh recipes/0372-in-app.sh Keynote $O/$f.key 'set out to {}
repeat with s in slides of d
  set end of out to name of base layout of s
end repeat
set end of out to "|"
repeat with l in slide layouts of d
  set end of out to name of l
end repeat
return out'
done
```

## Observation

| File | Slides' layouts | First layout | Last layout |
| --- | --- | --- | --- |
| `original.key` | Tittel og punkttegn, Tittel, Tittel og punkttegn | Tittel | Tom |
| `renamed.key` | Tittel og punkttegn, Written layout, Tittel og punkttegn | Written layout | Tom |
| `renamed-blank.key` | Tittel og punkttegn, Tittel, Tittel og punkttegn | Tittel | Empty page |

The other 15 layouts' names were the same in all three.

## Conclusion

Field 10 of a template slide is its layout's name, used as written wherever Keynote shows it, for the layout and for the slides based on it. Keynote doesn't translate or replace a name it doesn't know, so the names in a file are those of the language it was made in.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `original.key` | `theme/0160/move.key` | `same bytes` | *Control* |
| `renamed.key` | `original.key` | Only `5#2651742 10: "Tittel" → "Written layout"` | *Confirmed*: field 10 is the layout's name, for the layout and the slide that uses it |
| `renamed-blank.key` | `original.key` | Only `5#2652157 10: "Tom" → "Empty page"` | *Confirmed*: the same for a layout no slide uses |

## Confidence

*Confirmed*: template slide field 10 as the layout's name, by writing it.
