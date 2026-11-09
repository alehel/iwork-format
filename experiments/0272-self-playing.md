# 0272: A self-playing presentation

**Status:** run

The Keynote Document sidebar sets the presentation type: normal, links only or self-playing. It is a pop-up that needs Keynote in front. [0087](0087-auto-play.md)–[0089](0089-auto-restart.md) mapped the other slideshow settings in the presentation record (type 2). This experiment makes a presentation self-playing.

## Setup

| | |
| --- | --- |
| Keynote | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `samples/0271/plain.key`, a new presentation |

## Recipe

1. Make a new presentation:
   ```bash
   osascript -e 'tell application "Keynote" to make new document'
   ```
2. With Keynote in front, open the Document sidebar and choose Self-Playing (*Selvspillende*) from Presentation Type. The sidebar shows delays of 5.0 s between transitions and 2.0 s between builds.
3. Save it as `samples/0272/self-playing.key`.

## Observation

Apart from IDs, the only change is in the presentation record (type 2):

```
9: 0 → 1
```

Fields 10 (5.0) and 11 (2.0) are present in both documents.

## Conclusion

Presentation field 9 is the presentation type: 0 for normal and 1 for self-playing. Links only is probably 2. Fields 10 and 11 are the self-playing delays in seconds, before each transition and each build. They are stored with their defaults even when the presentation isn't self-playing.

## Confidence

*Likely*: presentation field 9 is the type, and fields 10 and 11 the self-playing delays.

*Unknown*: the value for links only.
