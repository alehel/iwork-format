# 0381: Writing a slide number

**Status:** run

Turning on slide numbers set field 18 of every slide node (type 4) from 0 to 1 ([0074](0074-slide-numbers.md)). Hidden placeholders are left out of a slide's lists of shown objects, fields 7 and 42 ([0243](0243-hidden-body.md), [0312](0312-writing-a-hidden-body.md)). This experiment writes field 18 and reads Keynote's exported PDF, where a shown slide number is text on the page.

## Setup

| | |
| --- | --- |
| Keynote | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-17 |
| Input | `samples/theme/0160/move.key`: three slides, C, A and B, without numbers. Slide A is node 2655505 and slide 2655467, which refers to a slide-number placeholder, 2655501 (type 7), not in its lists 7 and 42 |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py) and the new [`recipes/0381-show-object.py`](../recipes/0381-show-object.py); exported with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) and read with [`recipes/0374-pdf-text.swift`](../recipes/0374-pdf-text.swift) |

## Recipe

```bash
mkdir -p samples/0381
R=recipes/0302-set-path.py
O=samples/0381
cp samples/theme/0160/move.key $O/original.key
python3 -I $R $O/original.key $O/a-numbered.key 2655505 18 varint 1
python3 -I $R $O/a-numbered.key $O/a-and-b-numbered.key 2655616 18 varint 1
python3 -I $R $O/a-and-b-numbered.key $O/all-numbered.key 2655739 18 varint 1
python3 -I recipes/0381-show-object.py $O/original.key $O/a-placeholder.key 2655467 2655501
python3 -I recipes/0381-show-object.py $O/a-numbered.key $O/a-numbered-placeholder.key 2655467 2655501
for f in original a-numbered a-and-b-numbered all-numbered a-placeholder a-numbered-placeholder; do
  sh recipes/0372-in-app.sh Keynote $O/$f.key \
    "export d to POSIX file \"$PWD/$O/$f.pdf\" as PDF
return slide numbers showing of d"
  swift recipes/0374-pdf-text.swift $O/$f.pdf
done
```

Comparing the records of [0074](0074-slide-numbers.md)'s `slidenumbers.key` with its baseline found what that experiment missed: besides field 18 of every node, the slide record gained its slide-number placeholder in fields 7 and 42. `recipes/0381-show-object.py` adds an object to those lists, the reverse of 0312.

## Observation

| File | Written | `slide numbers showing` | Text of pages 1–3 |
| --- | --- | --- | --- |
| `original.key` | nothing | false | C / A / B |
| `a-numbered.key` | node of A: 18 = 1 | false | C / A / B |
| `a-and-b-numbered.key` | nodes of A and B: 18 = 1 | false | C / A / B |
| `all-numbered.key` | all three nodes: 18 = 1 | false | C / A / B |
| `a-placeholder.key` | slide A: placeholder in 7 and 42 | false | C / A 2 / B |
| `a-numbered-placeholder.key` | both | false | C / A 2 / B |

`slidenumbers.key` from 0074, exported the same way, reports true and shows `1`.

## Conclusion

A slide shows its number when its slide-number placeholder is in its lists of shown objects, fields 7 and 42, like any other placeholder; Keynote fills it with the slide's position, here 2. Field 18 of the slide node doesn't show or hide the number: it was set on its own on every slide without any number appearing. AppleScript's document-wide `slide numbers showing` stayed false even with all three slide nodes set, though it is true in 0074, where the template slides' nodes were set too; it may require every node, layouts included. So a reader should draw a number where the placeholder is listed, and a writer should list the placeholder and set field 18 on every node, as Keynote does.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `original.key` | `theme/0160/move.key` | `same bytes`, `5#2655467 7.1 ≠ 2655501` | *Control*: no numbers shown |
| `a-numbered.key` | `original.key` | Only `4#2655505 18: 0 → 1` | *Likely*: field 18 alone doesn't show the number |
| `a-and-b-numbered.key` | `a-numbered.key` | Only `4#2655616 18: 0 → 1` | *Likely*: as above |
| `all-numbered.key` | `a-and-b-numbered.key` | Only `4#2655739 18: 0 → 1` | *Likely*: as above, on all three slides |
| `a-placeholder.key` | `original.key` | Only `5#2655467 7: ×3 → ×4`, `5#2655467 42: ×3 → ×4`, `5#2655467 7.1 = 2655501`, `5#2655467 42.1 = 2655501` | *Confirmed*: the placeholder in fields 7 and 42 shows the slide's number, 2 |
| `a-numbered-placeholder.key` | `a-numbered.key` | Only `5#2655467 7: ×3 → ×4`, `5#2655467 42: ×3 → ×4`, `5#2655467 7.1 = 2655501`, `5#2655467 42.1 = 2655501` | *Confirmed*: the same with field 18 set |

## Confidence

*Confirmed*: a slide shows its number when its slide-number placeholder is in fields 7 and 42, by writing it. *Likely*: field 18 alone doesn't show it. What field 18 is for is *unknown*.
