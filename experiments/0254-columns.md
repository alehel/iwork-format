# 0254: Two columns

**Status:** run

Run table 12 of the body points at records of type 2024, whose meaning has been unknown since 0004. The Layout tab sets the number of columns with a stepper, which needs Pages in front. This experiment sets two columns.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `samples/0236/plain.pages`, a new document with the body text `One` |

## Recipe

1. Make a document with the body text `One`:
   ```bash
   osascript -e 'tell application "Pages" to set body text of (make new document) to "One"'
   ```
2. With Pages in front, click in `One`, then open the Layout tab and click the Columns (*Spalter*) stepper's up arrow once, from 1 to 2.
3. Save it as `samples/0254/two-columns.pages`.

## Observation

The body's run table 12 now points, from position 0, at a new type-2024 record in place of the default one (1732607). The two differ in:

| | Default | Two columns |
| --- | --- | --- |
| 10 | 1 | 2 |
| 11.7.1 | absent | `{ 1: 2, 2: 0.05 }` |

Nothing else changes.

## Conclusion

Type-2024 records are column styles, applied to the body through run table 12. Property 11.7.1 holds the number of columns (field 1) and probably the gap between them as a fraction of the text width (field 2, 0.05). A reader that lays out the body should split it into that many columns.

## Confidence

*Likely*: run table 12 holds column styles (type 2024), with the number of columns in 11.7.1.1.

*Unknown*: the unit of the gap.
