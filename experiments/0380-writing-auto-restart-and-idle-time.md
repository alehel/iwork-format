# 0380: Writing auto restart and the idle time

**Status:** run

A presentation's type-2 record holds its slideshow settings. Field 15 was read as *restart show if idle* and field 16 as the idle time in seconds, 900 by default ([0089](0089-auto-restart.md), [0197](0197-idle-time.md)). Keynote's AppleScript has `auto restart` and `maximum idle duration`. This experiment writes both fields and reads them back.

## Setup

| | |
| --- | --- |
| Keynote | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-17 |
| Input | `samples/theme/0160/move.key`: presentation 2652410, with field 15 = 0 and field 16 = 900 |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py); read back with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) |

## Recipe

```bash
mkdir -p samples/0380
R=recipes/0302-set-path.py
F=samples/theme/0160/move.key
cp $F samples/0380/original.key
python3 -I $R $F samples/0380/restart.key 2652410 15 varint 1
python3 -I $R $F samples/0380/both.key 2652410 15 varint 1 16 double 42.5
for s in 60 150 179 300; do
  python3 -I $R $F samples/0380/idle-$s.key 2652410 16 double $s
done
for f in samples/0380/*.key; do
  sh recipes/0372-in-app.sh Keynote $f 'return {auto restart of d, maximum idle duration of d}'
done
```

## Observation

| File | Field 15 | Field 16 | `auto restart` | `maximum idle duration` |
| --- | --- | --- | --- | --- |
| `original.key` | 0 | 900 | false | 15 |
| `restart.key` | 1 | 900 | true | 15 |
| `idle-60.key` | 0 | 60 | false | 1 |
| `idle-150.key` | 0 | 150 | false | 2 |
| `idle-179.key` | 0 | 179 | false | 2 |
| `idle-300.key` | 0 | 300 | false | 5 |
| `both.key` | 1 | 42.5 | true | 0 |

`auto loop` and `auto play` stayed false in every file.

## Conclusion

Field 15 is auto restart, 1 for on. Field 16 is the idle time in seconds, a double; AppleScript reports it in whole minutes, rounding down (179 seconds is 2, 42.5 is 0). Keynote keeps a time that isn't a whole number of minutes, so a reader should take the seconds from the file.

## Confidence

*Confirmed*: field 15 as auto restart and field 16 as the idle time in seconds, by writing them.
