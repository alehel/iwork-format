# 0089: Auto restart

**Status:** run

This experiment turns on *auto restart*, which restarts an idle slideshow, with an idle time of 30, to find both settings.

## Setup

| | |
| --- | --- |
| Keynote | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0025](0025-keynote-title.md), `empty.key` |

## Recipe

```bash
mkdir -p samples/0089
osascript recipes/0087-keynote-document-settings.applescript "$PWD/samples/0089/autorestart.key" autorestart
```

The recipe sets the document's `auto restart` to true and its `maximum idle duration` to 30.

## Observation

The presentation record (type 2) changed two fields:

```
15: 0 → 1
16: 900.0 → 1800.0        (a double)
```

## Conclusion

Field 15 of the presentation is *auto restart*, and field 16 the idle time before a restart, in seconds. AppleScript's `maximum idle duration` of 30 became 1800 seconds, so AppleScript counts that setting in minutes. The default, 900 seconds, is 15 minutes, and is stored even when auto restart is off.

## Confidence

*Likely*: presentation field 15 is auto restart and field 16 the idle time in seconds.
