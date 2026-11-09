# 0197: The idle time without auto restart

**Status:** run

[0089](0089-auto-restart.md) found that presentation field 16 is the idle time before a slideshow restarts, in seconds, with AppleScript counting it in minutes. That was seen together with auto restart turned on. This experiment changes the idle time alone, with a different value, to confirm the reading.

## Setup

| | |
| --- | --- |
| Keynote | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `default.key`, a new presentation from the same recipe |

## Recipe

```bash
mkdir -p samples/0197
osascript recipes/0197-keynote-idle.applescript "$PWD/samples/0197"
```

The recipe saves a new presentation as `default.key`, reporting its `maximum idle duration` (15). It then saves a second one, with the duration set to 123, as `idle.key`.

## Observation

Pairing the records of the two documents, the only difference other than IDs is in the presentation (type 2):

```
16: 900.0 → 7380.0   (a double)
```

Field 15 (auto restart) is 0 in both.

## Conclusion

Field 16 is the idle time in seconds, set independently of auto restart. 123 minutes is 7,380 seconds, so AppleScript counts in minutes, as in 0089.

## Confidence

*Confirmed*, with 0089: presentation field 16 is the idle time in seconds.
