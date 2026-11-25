# 0374: Writing a caption's and a title's text

**Status:** run

An object's caption and title are type-633 text shapes named in its drawable's fields 1.11 and 1.10, each with a text record of its own ([0228](0228-caption.md), [0229](0229-title.md)). When they are shown but empty, Pages draws a prompt. AppleScript can't read captions, so this experiment writes text into both and reads the PDF Pages exports.

## Setup

| | |
| --- | --- |
| Pages | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-17 |
| Input | `samples/0229/title-and-caption.pages`: an image with both a caption and a title shown and empty. The caption's text record is 1732703 and the title's 1732733. Neither has a field 3 |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py); exported with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) and read with the new [`recipes/0374-pdf-text.swift`](../recipes/0374-pdf-text.swift) |

## Recipe

```bash
mkdir -p samples/0374
R=recipes/0302-set-path.py
F=samples/0229/title-and-caption.pages
cp $F samples/0374/original.pages
python3 -I $R $F samples/0374/caption.pages 1732703 3 string "Written caption"
python3 -I $R $F samples/0374/title.pages 1732733 3 string "Written title"
python3 -I $R samples/0374/caption.pages samples/0374/both.pages 1732733 3 string "Written title"
for f in original caption title both; do
  sh recipes/0372-in-app.sh Pages samples/0374/$f.pages \
    "export d to POSIX file \"$PWD/samples/0374/$f.pdf\" as PDF"
done
swift recipes/0374-pdf-text.swift samples/0374/*.pdf
```

An empty text record has no field 3 at all, so the writer adds it.

## Observation

| File | Text of the exported page |
| --- | --- |
| `original.pages` | One / Tittel / Infotekst |
| `caption.pages` | One / Tittel / Written caption |
| `title.pages` | One / Written title / Infotekst |
| `both.pages` | One / Written title / Written caption |

*Tittel* and *Infotekst* are the Norwegian prompts for an empty title and caption.

## Conclusion

The caption's and the title's text are the text records their type-633 shapes name, and Pages draws whatever is written there in place of the prompt. An empty one is drawn as the prompt in the app's language. A reader that wants the document's own words should treat an empty caption or title as having no text, not print a prompt.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `original.pages` | `0229/title-and-caption.pages` | `same bytes` | *Control*: an empty caption and title are drawn as prompts |
| `caption.pages` | `original.pages` | Only `2001#1732703 3: absent → "Written caption"` | *Confirmed*: record 1732703 is the caption's text |
| `title.pages` | `original.pages` | Only `2001#1732733 3: absent → "Written title"` | *Confirmed*: record 1732733 is the title's text |
| `both.pages` | `caption.pages` | Only `2001#1732733 3: absent → "Written title"` | *Confirmed*: Pages draws both texts |

## Confidence

*Confirmed*: the text records of a caption and a title, by writing them.
