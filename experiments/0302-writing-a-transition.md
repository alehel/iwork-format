# 0302: Writing a slide transition

**Status:** run

[0071](0071-transition.md) and [0094](0094-automatic-transition.md) read a slide's transition from its field 4.2.8: the effect's identifier in field 2, the duration in seconds in field 3, the delay before an automatic transition in field 5 and whether it starts automatically in field 6. AppleScript can read all four. This experiment writes new values into a file and asks Keynote.

## Setup

| | |
| --- | --- |
| Keynote | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/theme/0071/transition.key`: one slide with a Dissolve transition, in the test theme ([0292](0292-test-theme-reruns.md)) |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py), which sets a value at a field path in one record, using the writer of [0287](0287-rewriting-a-document.md) |

## Recipe

```bash
mkdir -p samples/0302
cp samples/theme/0071/transition.key samples/0302/original.key
python3 -I recipes/0302-set-path.py samples/0302/original.key samples/0302/written.key 2655467 \
  4.2.8.2 string apple:push 4.2.8.3 double 3.25 4.2.8.5 double 1.5 4.2.8.6 varint 1
```

Record 2655467 is the slide (type 5). Its transition was `apple:dissolve`, 2.0 s, a delay of 0.5 s and not automatic; the script writes `apple:push`, 3.25 s, 1.5 s and automatic. Each file was then opened on its own and its slide's `transition properties` read through AppleScript; the written file was saved again as `resaved.key`.

Opening the files with AppleScript's `open` command failed, Keynote saying the file couldn't be opened at the moment because the operation wasn't permitted, even with no other document open. Opening them through Launch Services (`open -a "Keynote Creator Studio" FILE`) and then reading the front document worked every time. So the refusals in [0299](0299-writing-a-skipped-slide.md) and [0301](0301-writing-header-rows.md) depend on how the file is opened, not on its contents or on another open document.

## Observation

| File | Effect | Duration | Delay | Automatic |
| --- | --- | --- | --- | --- |
| `original.key` | dissolve | 2.0 | 0.5 | false |
| `written.key` | push | 3.25 | 1.5 | true |

In `resaved.key`, field 4.2.8 holds `apple:push`, 3.25, 1.5 and 1, as written. Fields 3 and 5 are doubles.

## Conclusion

The reading of field 4.2.8 holds when writing: field 2 names the effect, by the identifier AppleScript calls `push`; field 3 is its duration and field 5 its delay, both doubles in seconds; field 6 = 1 starts it automatically. Nothing else in the slide needs to change.

## Confidence

*Confirmed*: transition fields 4.2.8.2, 3, 5 and 6.
