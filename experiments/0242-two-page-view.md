# 0242: Two-page view

**Status:** run

[0241](0241-zoom.md) found the zoom in the type-10133 view state record. Pages can also show two pages side by side. This experiment turns that on, to find its field.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `samples/0236/plain.pages` |

## Recipe

1. Make a document with the body text `One`:
   ```bash
   osascript -e 'tell application "Pages" to set body text of (make new document) to "One"'
   ```
2. Choose View → Zoom → Two Pages (*Vis → Zoom → To sider*).
3. Save it as `samples/0242/two-pages.pages`.

## Observation

In the type-10133 record:

- **Field 33:** changes from 0 to 1.
- **Field 2, a point:** moves from (0, 0) to (−272.4, 0).
- **Fields 7 and 17:** the first value of each grows, 7.1 from 582.4 to 1140 and 17.1 from 1031 to 1728.
- **Field 16:** its first value drops from 342 to 0.
- **Field 15, the zoom:** stays 1.25.

## Conclusion

Field 33 of the view state is the page layout of the view: 1 for two pages side by side. The other fields that move are sizes and offsets of the visible area, which grows wider to fit two pages, consistent with field 7 being the visible area's size in document points ([0241](0241-zoom.md)). Like the zoom, this is a view preference that a reader can ignore.

## Confidence

*Likely*: view state field 33 is 1 for two-page view.
