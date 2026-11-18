# 0452: Writing a hidden title

**Status:** run

A slide's fields 5 and 6 name its title and body placeholders, and its repeated fields 7 and 42 list the objects shown, so a hidden placeholder is left out of them; that was confirmed by writing it for a body ([0101](0101-hidden-title.md), [0243](0243-hidden-body.md), [0312](0312-writing-a-hidden-body.md)). This experiment does the same for a title, and reads the slide through AppleScript and its exported text.

## Setup

| | |
| --- | --- |
| Keynote | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/theme/0025/hello.key`: one slide, 2655467, titled `hello`, whose field 5 names title placeholder 2655477, listed in fields 7 and 42 |
| Writer | [`recipes/0312-hide-object.py`](../recipes/0312-hide-object.py); read back with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) and [`recipes/0374-pdf-text.swift`](../recipes/0374-pdf-text.swift) |

## Recipe

```bash
mkdir -p samples/0452
O=samples/0452
cp samples/theme/0025/hello.key $O/original.key
python3 -I recipes/0312-hide-object.py $O/original.key $O/title-hidden.key 2655467 2655477
for f in original title-hidden; do
  sh recipes/0372-in-app.sh Keynote $O/$f.key "export d to POSIX file \"$PWD/$O/$f.pdf\" as PDF
set s to slide 1 of d
return {title showing of s, body showing of s}"
  swift recipes/0374-pdf-text.swift $O/$f.pdf
done
```

## Observation

| File | `title showing` | `body showing` | Text of the slide |
| --- | --- | --- | --- |
| `original.key` | true | true | hello |
| `title-hidden.key` | false | true | none |

## Conclusion

A title placeholder left out of fields 7 and 42 is hidden, as a body is: AppleScript reports the title as not showing and its text isn't drawn, though field 5 still names it and its text is still in the file.

## Confidence

*Confirmed*: hiding a title by leaving it out of slide fields 7 and 42, by writing it.
