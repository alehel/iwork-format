# 0376: A highlight is a comment without text

**Status:** run

A highlight and a comment are stored the same way: a type-2013 entry in run table 23 pointing at a type-3056 record. The only difference seen was that a highlight's text, field 1, is empty ([0200](0200-highlight.md), [0249](0249-comment.md)). This experiment writes text into a highlight and empties a comment, and lets Pages list the comments when it exports PDF.

## Setup

| | |
| --- | --- |
| Pages | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-17 |
| Input | `samples/0200/highlight.pages`: a highlight on `One`, record 1732718 with an empty field 1. `samples/0249/comment.pages`: the comment `Note` on `One`, record 1732721 |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py); exported with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) and read with [`recipes/0374-pdf-text.swift`](../recipes/0374-pdf-text.swift) |

## Recipe

```bash
mkdir -p samples/0376
R=recipes/0302-set-path.py
cp samples/0200/highlight.pages samples/0249/comment.pages samples/0376/
python3 -I $R samples/0200/highlight.pages samples/0376/highlight-with-text.pages 1732718 1 string "Written note"
python3 -I $R samples/0249/comment.pages samples/0376/comment-emptied.pages 1732721 1 string ""
for f in highlight highlight-with-text comment comment-emptied; do
  sh recipes/0372-in-app.sh Pages samples/0376/$f.pages \
    "export d to POSIX file \"$PWD/samples/0376/$f.pdf\" as PDF with properties {include comments:true}"
done
swift recipes/0374-pdf-text.swift samples/0376/*.pdf
```

## Observation

| File | Written | Comments listed in the margin |
| --- | --- | --- |
| `highlight.pages` | nothing | none |
| `highlight-with-text.pages` | field 1 = `Written note` | 1. (owner's name) / 9. november 2026 kl. 19:47:29 / Written note |
| `comment.pages` | nothing | 1. (owner's name) / 9. november 2026 kl. 20:58:43 / Note |
| `comment-emptied.pages` | field 1 = empty | none |

## Conclusion

Whether an annotation is a comment or a highlight depends only on whether its type-3056 record has text in field 1. With text, Pages treats it as a comment with that author and time; without, as a highlight that isn't listed. A reader can tell them apart the same way.

## Confidence

*Confirmed*: an empty field 1 makes a highlight, and text in it a comment, by writing it both ways.
