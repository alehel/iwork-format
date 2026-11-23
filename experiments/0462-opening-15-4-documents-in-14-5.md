# 0462: Opening 15.4 documents in 14.5

**Status:** run

Pages and Numbers 14.5 write the same format as 15.4 ([0461](0461-new-documents-in-14-5.md)). This experiment opens every Pages and Numbers sample of experiments 0001 to 0371, made or written with the 15.4 apps, in 14.5, and checks what it reads.

## Setup

| | |
| --- | --- |
| Pages | 14.5, in Norwegian |
| Numbers | 14.5 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-23 |
| Input | Every `.pages` and `.numbers` under `samples/0001` to `samples/0371`: 594 documents, from the apps themselves and from the writing experiments 0287 to 0371 |
| Script | The new [`recipes/0462-open-in-app.py`](../recipes/0462-open-in-app.py), which opens each with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh): for Pages it compares the body text 14.5 reports with the body's text record read by `iwork-probe`, and for Numbers it reads the number of sheets and the first table's name |

## Recipe

```bash
python3 -I recipes/0462-open-in-app.py samples 1 371
```

The comparison leaves out spaces, control characters (breaks and footnote marks, which AppleScript returns but `iwork-probe text` shows as markers) and U+FFFC on both sides, and counts a document without a body, for which AppleScript returns `missing value`, as empty. That rule was added after a first run showed that every other difference came from those characters; the files involved were then checked again.

## Observation

| Result | Documents |
| --- | --- |
| Opened, and the body text agrees with the file (Pages) or the sheets and table were read (Numbers) | 590 |
| Opened, and read through the password prompt, with the test password typed by hand | 2 (`0180/accent.pages`, `0180/image.pages`, body `one`) |
| Not opened: the password prompt was cancelled | 2 (`0179/locked.pages`, `0179/locked2.pages`) |

No alert other than the password prompts was shown, and no document failed to open.

## Conclusion

Pages and Numbers 14.5 open every document the 15.4 apps saved in these experiments, and every one written from this spec in experiments 0287 to 0371, and read the same text and tables from them. Nothing 15.4 writes stops the older release reading it, including the type-4011 record 14.5 doesn't write. Whether 14.5 also draws them the same is the next experiment's question.

## Confidence

*Confirmed*: 14.5 opens 594 documents from 15.4 and from the spec's writer, and reads the same body text and tables, apart from the two password-protected documents not opened.
