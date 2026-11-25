# 0375: Writing a comment's text, time and author

**Status:** run

A comment is an entry in run table 23 pointing at a type-2013 record, which points at a type-3056 record: the text in field 1, a time in field 2.1 (seconds since 2001), the author in field 3 and an ID in field 5. Authors are type-212 records in `AnnotationAuthorStorage`, with their name in field 1 ([0249](0249-comment.md), [0193](0193-tracked-insertion.md)). AppleScript can't read comments, but Pages can export them to PDF, where it lists them in the margin. This experiment writes each value and reads the exported page.

## Setup

| | |
| --- | --- |
| Pages | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84), time zone Europe/Oslo |
| Date | 2026-11-17 |
| Input | `samples/0249/comment.pages`: the comment `Note` on the word `One`, in record 1732721, by author 1732718 (the project owner) |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py); exported with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) and read with [`recipes/0374-pdf-text.swift`](../recipes/0374-pdf-text.swift) |

## Recipe

```bash
mkdir -p samples/0375
R=recipes/0302-set-path.py
F=samples/0249/comment.pages
python3 -I $R $F samples/0375/text.pages 1732721 1 string "Written comment"
python3 -I $R $F samples/0375/time.pages 1732721 2.1 double 771681600
python3 -I $R $F samples/0375/author.pages 1732718 1 string "Test Author"
for f in text time author; do
  sh recipes/0372-in-app.sh Pages samples/0375/$f.pages \
    "export d to POSIX file \"$PWD/samples/0375/$f.pdf\" as PDF with properties {include comments:true}"
done
swift recipes/0374-pdf-text.swift samples/0375/*.pdf
```

771,681,600 seconds after the start of 2001 (UTC) is 15 June 2025, 12:00 UTC.

## Observation

Each page lists the comment in its margin as a number, the author, the time and the text. The PDF has no annotations: the comments are drawn as text.

| File | Written | Margin |
| --- | --- | --- |
| `comment.pages` | nothing | 1. (owner's name) / 9. november 2026 kl. 20:58:43 / Note |
| `text.pages` | 3056 field 1 = `Written comment` | 1. (owner's name) / 9. november 2026 kl. 20:58:43 / Written comment |
| `time.pages` | 3056 field 2.1 = 771681600 | 1. (owner's name) / 15. juni 2025 kl. 14:00:00 / Note |
| `author.pages` | 212 field 1 = `Test Author` | 1. Test Author / 9. november 2026 kl. 20:58:43 / Note |

## Conclusion

Field 1 of the type-3056 record is the comment's text, field 2.1 its time in seconds since 1 January 2001 UTC (shown in local time, two hours ahead in June in Oslo), and field 1 of the author's type-212 record the name shown. The name lives only in the author record, so renaming that record renames every comment that points at it.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `text.pages` | `0249/comment.pages` | Only `3056#1732721 1: "Note" → "Written comment"` | *Confirmed*: field 1 of type 3056 is the comment's text |
| `time.pages` | `0249/comment.pages` | Only `3056#1732721 2.1: 815947123.8006 → 771681600.0` | *Confirmed*: field 2.1 is the time in seconds since 2001, UTC: 15 June 2025, 14:00 in Oslo |
| `author.pages` | `0249/comment.pages` | Only `212#1732718 1: changed`, `212#1732718 1 = "Test Author"` | *Confirmed*: field 1 of type 212 is the author's name |

## Confidence

*Confirmed*: a comment's text and time, and an author's name, by writing them.
