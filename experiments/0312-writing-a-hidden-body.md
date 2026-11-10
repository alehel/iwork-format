# 0312: Writing a hidden body placeholder

**Status:** run

[0243](0243-hidden-body.md) found that hiding a slide's body placeholder leaves it named in slide field 6 but drops it from the slide's repeated fields 7 and 42, which list what is shown ([0101](0101-hidden-title.md) found the same for titles). AppleScript reads a slide's `body showing`. This experiment hides a body by removing it from the two lists and asks Keynote.

## Setup

| | |
| --- | --- |
| Keynote | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/theme/0243/body.key`: two slides; slide 2 (record 2655565) names its body placeholder 2655586 in fields 6, 7 and 42 |
| Writer | [`recipes/0312-hide-object.py`](../recipes/0312-hide-object.py), using the writer of [0287](0287-rewriting-a-document.md) |

## Recipe

```bash
mkdir -p samples/0312
cp samples/theme/0243/body.key samples/0312/original.key
python3 -I recipes/0312-hide-object.py samples/0312/original.key samples/0312/written.key 2655565 2655586
```

The script removes the entries naming 2655586 from fields 7 and 42 of slide 2, and leaves field 6 and the placeholder itself. Keynote opened each file on its own and read `title showing` and `body showing` through AppleScript, and the written file was saved again.

## Observation

| File | Slide 2 title | Slide 2 body | Slide 1 body |
| --- | --- | --- | --- |
| `original.key` | true | true | true |
| `written.key` | true | false | true |

Saved again, slide 2 still names 2655586 in field 6 and lists only the other two objects in 7 and 42, and the placeholder record is still in the slide's part.

## Conclusion

Whether a placeholder shows is decided by fields 7 and 42 alone: an object named in field 6 but missing from those lists is hidden, and Keynote keeps it, so it can come back with its text.

## Confidence

*Confirmed*: a placeholder left out of slide fields 7 and 42 is hidden.
