# 0300: Writing document settings

**Status:** run

Three settings were read from files earlier: Pages' Facing Pages as field 34 of the type-10012 record ([0017](0017-section-switches.md)), and Keynote's Loop Slideshow and Play Automatically as fields 8 and 18 of the presentation record ([0087](0087-auto-play.md), [0088](0088-auto-loop.md)). AppleScript can read all three back. This experiment writes them into files and asks the apps.

## Setup

| | |
| --- | --- |
| Pages, Keynote | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0002/hello.pages`, and `samples/theme/0025/hello.key` in the test theme ([0292](0292-test-theme-reruns.md)) |
| Writer | [`recipes/0300-set-field.py`](../recipes/0300-set-field.py), using the writer of [0287](0287-rewriting-a-document.md) |

## Recipe

```bash
mkdir -p samples/0300
python3 -I recipes/0300-set-field.py samples/0002/hello.pages samples/0300/facing.pages 10012 34=1
python3 -I recipes/0300-set-field.py samples/theme/0025/hello.key samples/0300/loop-play.key 2 8=1 18=1
```

The script sets top-level varint fields in every record of a type, here one record each. All three fields were 0 before. With no other document open, each app opened the original and the written file through AppleScript and read `facing pages`, or `auto loop` and `auto play`, then saved the written file again.

## Observation

| File | Read by AppleScript |
| --- | --- |
| `hello.pages` | facing pages: false |
| `facing.pages` | facing pages: true |
| `hello.key` | auto loop: false, auto play: false |
| `loop-play.key` | auto loop: true, auto play: true |

Both apps opened the written files without a warning, and the files saved again kept field 34 = 1, and fields 8 = 1 and 18 = 1.

## Conclusion

The three readings hold from the writing side: field 34 of Pages' type-10012 record turns on facing pages, and fields 8 and 18 of Keynote's presentation record make the slideshow loop and play on opening. A writer only needs to set the field; nothing else in the file depends on it.

## Confidence

*Confirmed*: type-10012 field 34 is Facing Pages; presentation fields 8 and 18 are Loop Slideshow and Play Automatically.
