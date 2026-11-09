# 0247: Checking every sample again

**Status:** run

[0178](0178-regression-check.md) checked that every sample document frames, that every object is reachable from the roots, and that its text extracts. Experiments 0179–0246 added 150 documents with new features: password protection, media, links, tracked changes, highlights, tables of contents, charts in Pages and Numbers, pivot tables, categories, groups, masks and captions. This experiment runs the same checks over all of them.

## Setup

| | |
| --- | --- |
| Tool | `iwork-probe`, unchanged since 0178 |
| Date | 2026-11-09 |
| Baseline | Experiment [0178](0178-regression-check.md) |

## Recipe

The same three checks as in 0178, over every document in `samples/`:

1. **Framing:** every `.iwa` part split into chunks and records.
2. **Reachability:** objects reached from roots 1, 2, 71 and 61 through the IDs listed in record headers.
3. **Text:** every text record extracted.

## Observation

| | |
| --- | --- |
| Documents | 353: 155 Pages, 74 Keynote, 124 Numbers, 3 of them folder packages |
| Failed | 6, the password-protected documents of [0179](0179-password.md) and [0180](0180-password-in-other-apps.md) |
| `.iwa` parts in the other 347 | 8,109, all framed without error |
| Objects | 236,403, all reached from the roots |
| References to missing objects | none other than root 61 in documents without a chart |
| Text extraction | no errors in the other 347 |

The six failures are expected: their parts are encrypted, so none of them frames. Decrypted as described in [container.md](../spec/container.md#password-protection), the same documents framed and were fully reachable in 0180.

## Conclusion

The container findings hold for everything added since 0178: every new record type is framed by the same chunk and record layout and listed in its parent's header references. That includes media, tracked changes, highlights, captions, groups, masks, chart links, pivot tables and category trees. `iwork-probe` doesn't decrypt yet, so a reader built on it must first decrypt password-protected documents.

## Confidence

*Confirmed*: framing and header-reference reachability hold for all 347 unencrypted samples.

Follow-up: add decryption to `iwork-probe`, so the check covers protected documents too.
