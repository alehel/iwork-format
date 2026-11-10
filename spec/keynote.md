# Keynote

What is specific to Keynote documents. The container is the same as Pages' ([container.md](container.md)), and text is stored as in [text.md](text.md). Every finding links to the experiments that support it, with a confidence level as defined in [CONTRIBUTING.md](../CONTRIBUTING.md#confidence).

Observed with Keynote 15.4 on macOS 26.5.2.

## Parts

A new presentation has the seven `.iwa` parts that Pages documents have, without numbers in their names, plus one `Index/Slide-N.iwa` per slide and one `Index/TemplateSlide-N.iwa` per template slide of the theme. N is usually the ID of the slide record inside, but a part may be named `Slide.iwa` or end in `-2`, and names move between slides when slides are deleted; find slides by their IDs ([0161](../experiments/0161-deleted-slide.md), [0162](../experiments/0162-ten-slides.md)). The theme's images, including slide thumbnails, are stored under `Data/`. *Likely* ([0024](../experiments/0024-keynote-and-numbers.md), [0027](../experiments/0027-document-roots.md)). Each master slide has a 356 × 200 thumbnail named `mt-UUID-N.jpg`, where the UUID is the master's and stays the same in every presentation made from the theme; slides have `st-UUID-N.jpg`. A master's thumbnail is redrawn only once the master is shown, so a changed master can keep an old thumbnail until then ([0291](../experiments/0291-test-theme.md)).

A theme file (`.kth`) is a Keynote document in the same container, with a different extension. Its name isn't stored in it: Keynote takes the name from the presentation it was saved from. *Likely* ([0291](../experiments/0291-test-theme.md))

## From the root to a slide's text

| Type | Holds | Part |
| --- | --- | --- |
| 1 | The document root, with the shared document-properties block in field 3 (see [container.md](container.md#following-references)) | `Document.iwa` |
| 2 | The presentation: field 3.2 lists the slide nodes in show order, field 4 is the slide size in points (such as 1920 × 1080, *confirmed* by [0075](../experiments/0075-slide-size.md)), field 5 names the stylesheet ([0038](../experiments/0038-second-slide.md)); slideshow settings are field 8 (auto loop), 9 (presentation type: 0 normal, 1 self-playing), 10 and 11 (self-playing delays before transitions and builds, in seconds, [0272](../experiments/0272-self-playing.md)), 15 (auto restart), 16 (idle time in seconds, *confirmed* by [0197](../experiments/0197-idle-time.md)) and 18 (auto play) ([0087](../experiments/0087-auto-play.md)–[0089](../experiments/0089-auto-restart.md)) | `Document.iwa` |
| 4 | A slide node: field 2 names the slide; fields 10 (thumbnail size) and 16.1 (data ID of the thumbnail image) are optional; field 4 is 1 for a skipped slide ([0070](../experiments/0070-skipped-slide.md)) and field 18 is 1 when the slide's number is shown ([0074](../experiments/0074-slide-numbers.md)) | `Document.iwa` |
| 5 | A slide; fields 5 and 6 name its title and body placeholders, and the repeated fields 7 and 42 list the objects shown, so a hidden placeholder is left out of them ([0101](../experiments/0101-hidden-title.md), [0243](../experiments/0243-hidden-body.md)); field 17 names its layout, a template slide that is itself a type-5 slide named in its field 10 ([0046](../experiments/0046-slide-layout.md)); field 27 names its presenter notes (type 15) | `Slide-N.iwa`, `Slide.iwa`, or `TemplateSlide-N.iwa` for layouts |
| 15 | Presenter notes: field 1 names the notes text, a type-2001 record with field 1 = 4. Every slide has one, empty or not ([0039](../experiments/0039-presenter-notes.md)). | `Slide-N.iwa` |
| 7 | A shape on the slide, such as the title box; fields 2 and 4 name its text record | `Slide-N.iwa` |
| 2001 | The shape's text, as in [text.md](text.md) | `Slide-N.iwa` |

*Likely* ([0025](../experiments/0025-keynote-title.md), [0027](../experiments/0027-document-roots.md))

## Slides

Show order is the order of field 3.2 alone: moving a slide changes only that list ([0160](../experiments/0160-moved-slide.md)). A duplicated slide is a full copy with new IDs ([0159](../experiments/0159-duplicated-slide.md)), and a deleted slide leaves nothing behind ([0161](../experiments/0161-deleted-slide.md)). A template slide's field 10 is its layout name in the app's language ([0165](../experiments/0165-slide-layouts.md)). An empty title placeholder is an empty text record; its prompt is only in the layout ([0168](../experiments/0168-untouched-title.md)). Line feeds in titles and presenter notes are paragraph breaks ([0163](../experiments/0163-multi-paragraph-notes.md), [0164](../experiments/0164-two-line-title.md)). *Likely*

## Slide contents

Shapes added to a slide (text boxes) are type 2011, images type 3005 and tables types 6000 and 6001, as in Pages and Numbers. Each drawable's field 1.2 names the slide it is on. Placeholders from the layout, such as the title, are type 7. Lines and shapes have the same geometry and style identifiers as in Pages ([0166](../experiments/0166-keynote-line.md), [0167](../experiments/0167-keynote-shape-text.md)). *Likely* ([0068](../experiments/0068-keynote-text-box.md), [0069](../experiments/0069-keynote-image.md), [0073](../experiments/0073-keynote-table.md))

A slide's transition is in its field 4.2.8: the effect's name in field 2, its duration in seconds in field 3, the delay before an automatic transition in field 5 (default 0.5) and whether it starts automatically in field 6. *Likely* ([0071](../experiments/0071-transition.md), [0094](../experiments/0094-automatic-transition.md))

Effect names are Keynote's own identifiers: `none`, `apple:dissolve` (AppleScript `dissolve`), `apple:slide` (`move in`), `apple:push` (`push`), `apple:3D-cube` (`cube`) and `apple:magic-move-implied-motion-path` (`magic move`). *Likely* ([0091](../experiments/0091-move-in-transition.md)–[0095](../experiments/0095-magic-move.md)). The identifiers of the other 38 effects AppleScript offers are listed in [0196](../experiments/0196-every-transition.md). Some use the `apple:` form, and others a class name such as `com.apple.iWork.Keynote.BLTBlinds`. *Likely*

Sounds and movies are type 3007. Field 14 names the media file by data ID, field 15 a poster image for a movie, field 7 the volume (0–1) and field 24 the repetition (0 none, 1 loop). Field 23 is 1 when the media has pictures and field 9 is 1 when it has only sound; fields 20 and 21 are a movie's natural size. Field 29 describes the first track: its kind (`soun` or `vide`) and time scale. A sound's drawable has a size of 0 × 0. *Likely* ([0185](../experiments/0185-keynote-audio.md)–[0187](../experiments/0187-keynote-movie.md)). Pages and Numbers store media in the same record: that sounds and movies are type 3007 with their file in field 14 is *confirmed* ([0188](../experiments/0188-media-in-pages-and-numbers.md)).

A build is a type-8 record listed in slide field 2: field 1 names the object, field 2 the delivery (such as `All at Once`), and field 4.18 the effect, with `In`, `Out` or `Action` in 4.18.1 for a build-in, build-out or action, *confirmed* ([0263](../experiments/0263-build-out.md), [0264](../experiments/0264-action-build.md)); an action's settings, such as a rotation's angle in 4.9, sit beside the effect in field 4, an identifier such as `apple:dissolve character` in 4.18.2 and the duration in 4.18.3. Slide field 43 lists type-153 records, probably the build order. *Likely* ([0257](../experiments/0257-build.md))

A slide's background is the fill in its slide style (type 9, property 11.1). A dynamic background is an image fill (field 3) showing a pre-rendered still, a `motionBackground-…` data file, plus field 200 naming a type-26 motion background style. That style holds the generator's name, such as `KNGradientLinearBase`, colour stops as in a gradient fill, and parameters such as the scale (64) and speed (70). *Likely* ([0271](../experiments/0271-dynamic-background.md))

Bulleted body text uses the same text records and list styles as Pages; the theme's default body list style is a bullet (`•` in field 16). *Likely* ([0072](../experiments/0072-keynote-bullets.md))

## Charts

A chart is a drawable of type 5021 on the slide. Its field 10000.7 holds its data: row names in 7.1, column names in 7.2, and one 7.3 per row listing its values as doubles. *Confirmed*: Pages stores charts the same way ([0067](../experiments/0067-chart.md), [0222](../experiments/0222-pages-chart.md)). A Numbers chart also links to its table: field 10000.8 names a type-12006 record whose field 3 holds formulas, in the cell-formula node form, for the series values (3.1), category labels (3.3) and series names (3.4); 10000.7 keeps a copy of the values. *Likely* ([0225](../experiments/0225-numbers-chart.md))

Field 10000.1 is the chart type and 10000.5 the grouping into series (1 by row, 2 by column); the data grid in 10000.7 is the same whatever the type or grouping. *Likely* ([0079](../experiments/0079-pie-chart.md)–[0086](../experiments/0086-chart-grouped-by-column.md))

| 10000.1 | Type |
| --- | --- |
| 1 | Vertical bar |
| 2 | Horizontal bar |
| 3 | Line |
| 4 | Area |
| 5 | Pie |
| 6 | Stacked vertical bar |
| 7 | Stacked horizontal bar ([0195](../experiments/0195-remaining-chart-types.md)) |
| 8 | Stacked area ([0195](../experiments/0195-remaining-chart-types.md)) |
| 9 | Scatter |
| 10 | Mixed ([0224](../experiments/0224-menu-chart-types.md)) |
| 11 | Two-axis ([0224](../experiments/0224-menu-chart-types.md)) |
| 12 | 3D vertical bar |
| 13 | 3D horizontal bar ([0195](../experiments/0195-remaining-chart-types.md)) |
| 14 | 3D line ([0195](../experiments/0195-remaining-chart-types.md)) |
| 15 | 3D area ([0195](../experiments/0195-remaining-chart-types.md)) |
| 16 | 3D pie ([0195](../experiments/0195-remaining-chart-types.md)) |
| 17 | 3D stacked vertical bar ([0195](../experiments/0195-remaining-chart-types.md)) |
| 18 | 3D stacked horizontal bar ([0195](../experiments/0195-remaining-chart-types.md)) |
| 19 | 3D stacked area ([0195](../experiments/0195-remaining-chart-types.md)) |
| 20 | Interactive column ([0224](../experiments/0224-menu-chart-types.md)) |
| 21 | Interactive bar ([0224](../experiments/0224-menu-chart-types.md)) |
| 22 | Bubble ([0224](../experiments/0224-menu-chart-types.md)) |
| 23 | Interactive scatter ([0224](../experiments/0224-menu-chart-types.md)) |
| 24 | Interactive bubble ([0224](../experiments/0224-menu-chart-types.md)) |
| 25 | Donut ([0224](../experiments/0224-menu-chart-types.md)) |
| 27 | Radar ([0224](../experiments/0224-menu-chart-types.md)) |
