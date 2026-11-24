# 3. Styles

How text is formatted: character, paragraph and list styles, the properties they set, and how they combine. The text refers to them through its run tables ([2. Text](text.md#runs)). Every finding links to the experiments that support it, with a confidence level as defined in [CONTRIBUTING.md](../CONTRIBUTING.md#confidence). Records, object IDs and types are as described in [1. Container](container.md).

## Styles made by formatting

Changing the size of part of the text, or making it bold or italic, creates a new, unnamed character style (type 2021) in `DocumentStylesheet.iwa`. It inherits (field 1.3) from a character style whose identifier is `character-style-null`. *Confirmed* ([0004](../experiments/0004-larger-word.md), [0007](../experiments/0007-bold-and-italic.md), [0008](../experiments/0008-runs-and-shared-styles.md))

Formatting a whole paragraph instead creates an unnamed paragraph style (type 2022) that inherits from the paragraph's style and carries the change. *Likely* ([0008](../experiments/0008-runs-and-shared-styles.md), [0149](../experiments/0149-family-emoji.md))

Several properties set on one range go into one style ([0152](../experiments/0152-size-and-colour.md)). Setting a property to the value it already has makes no style ([0153](../experiments/0153-same-size-again.md)), and styles nothing uses are dropped on save ([0154](../experiments/0154-replaced-text.md)). A template's styles are copied into the document with their own values, such as white text in the black template ([0157](../experiments/0157-black-template.md)). *Likely*

## Character properties

Field 11 of a character style or a paragraph style holds the character properties it sets. A property that is left out is inherited, and one set to 0 is turned off (*confirmed* by writing both into a character style over a paragraph style, [0392](../experiments/0392-writing-inherited-properties.md)). *Likely* ([0004](../experiments/0004-larger-word.md), [0007](../experiments/0007-bold-and-italic.md), [0008](../experiments/0008-runs-and-shared-styles.md))

| Field 11.n | Property | Encoding |
| --- | --- | --- |
| 1 | Bold | varint: 1 bold, 0 not bold |
| 2 | Italic | varint: 1 italic |
| 3 | Size in points | float |
| 5 | Font name, such as `HelveticaNeue` | text |
| 7 | Text colour | message: red, green and blue in fields 3, 4 and 5 and alpha in field 6, as floats from 0 to 1, in the colour space named by field 12: 1 (or absent) sRGB, 2 Display P3 ([0329](../experiments/0329-the-colour-space-field.md)); field 1 = 1 is RGB. The apps write 1, and five such colours matched sRGB, through AppleScript and on the drawn page ([0328](../experiments/0328-writing-a-page-background.md)); AppleScript reports colours converted to Generic RGB ([0309](../experiments/0309-writing-a-cell-colour.md)). In cell text styles, at least, the colour drawn is 46.1 and this field a copy that the app rewrites from it on saving ([0310](../experiments/0310-writing-a-cell-text-style.md)) |
| 46 | Text fill | message: field 1 is the text colour as in 7; this is the one drawn, and the app keeps 7 in step with it when saving ([0310](../experiments/0310-writing-a-cell-text-style.md)). With 1, 2, 3 and 5, *confirmed* by writing a paragraph style in Pages ([0311](../experiments/0311-writing-a-paragraph-style.md)) |
| 10 | Baseline position | varint: 1 superscript, 2 subscript ([0203](../experiments/0203-superscript.md), [0204](../experiments/0204-subscript.md)) *Confirmed* by writing and measuring ([0322](../experiments/0322-writing-character-properties.md)). |
| 11 | Underline | varint: 1 underlined, 0 not |
| 12 | Strikethrough | varint: 1 struck through, 0 not |
| 13 | Capitalisation | varint: 1 all caps, 2 small caps; the stored text keeps its case ([0205](../experiments/0205-small-caps.md), [0206](../experiments/0206-all-caps.md)) *Confirmed* by writing and measuring ([0322](../experiments/0322-writing-character-properties.md)). |
| 14 | Baseline shift | float, in points, up from the baseline ([0209](../experiments/0209-raised-baseline.md)) *Confirmed* by writing and measuring ([0322](../experiments/0322-writing-character-properties.md)). |
| 16 | Ligatures | varint: 0 none; absent means the default ([0208](../experiments/0208-no-ligatures.md)) |
| 27 | Letter spacing | float, as a fraction of the font size: 0.01 is 1% ([0207](../experiments/0207-looser-letter-spacing.md)) *Confirmed* by writing and measuring ([0322](../experiments/0322-writing-character-properties.md)). |

Field 11.5 is *confirmed* ([0010](../experiments/0010-alignment.md), [0053](../experiments/0053-font.md)), and so is 11.7 ([0013](../experiments/0013-text-colour.md)); 11.11 and 11.12 are *likely* ([0012](../experiments/0012-underline-and-strikethrough.md)); the rest as above.

## Paragraph properties

A paragraph style also has a field 12 for paragraph properties. *Likely* ([0008](../experiments/0008-runs-and-shared-styles.md), [0010](../experiments/0010-alignment.md))

| Field 12.n | Property | Encoding |
| --- | --- | --- |
| 1 | Alignment | varint: 0 left, 1 right, 2 centred, 3 justified, 4 probably natural (the Body style's value, shown as left); 1 and 2 *confirmed* by writing them and measuring the page ([0319](../experiments/0319-writing-paragraph-alignment.md)) |
| 7 | First-line indent | float, in points from the margin, for the first line only ([0253](../experiments/0253-indents.md); *confirmed* by writing and measuring, [0320](../experiments/0320-writing-indents.md)) |
| 11 | Left indent | float, in points from the margin, for every line but the first, independent of 7 ([0253](../experiments/0253-indents.md); *confirmed*, [0320](../experiments/0320-writing-indents.md)) |
| 13 | Line spacing | message: field 1 is the kind (absent for a multiple of lines; 1 at least, 2 exactly and 4 between, in points, [0281](../experiments/0281-other-line-spacing-kinds.md)) and field 2 the amount, such as 2.0 for double ([0252](../experiments/0252-line-spacing.md), [0276](../experiments/0276-exact-line-spacing.md)). A multiple of lines and exact spacing (kind 2) are *confirmed* by writing and measuring ([0321](../experiments/0321-writing-spacing.md)); kinds 1 and 4 are *likely* ([0281](../experiments/0281-other-line-spacing-kinds.md)). |
| 19 | Right indent | float, in points from the right margin ([0253](../experiments/0253-indents.md); *confirmed*, [0320](../experiments/0320-writing-indents.md)) |
| 20 | Space after the paragraph | float, in points ([0256](../experiments/0256-paragraph-spacing.md)) *Confirmed* by writing and measuring ([0321](../experiments/0321-writing-spacing.md)). |
| 21 | Space before the paragraph | float, in points ([0256](../experiments/0256-paragraph-spacing.md)) *Confirmed* by writing and measuring ([0321](../experiments/0321-writing-spacing.md)). |
| 25 | Tab stops | message: one 25.1 per stop, with its position in points from the left margin in field 1 (*confirmed* with left and right stops by writing and measuring, [0325](../experiments/0325-writing-tab-stops.md); without stops, Pages uses one every 36 points), its alignment in field 2 (absent for left, 1 centre, 2 right, 3 decimal, [0282](../experiments/0282-centre-and-decimal-tabs.md)) and its leader character in field 3 (a space draws nothing) ([0255](../experiments/0255-tab-stop.md), [0277](../experiments/0277-right-tab.md)) |
| 32 | Border | message: a stroke in the layout of a shape's (colour, width, pattern); property 45 gives its edges as bits (1 top, 2 bottom, 15 all), and property 15 an older single value (1 top, 2 bottom, 4 all). Pages draws from 15; changing 45 alone changes nothing drawn (*confirmed* by writing and measuring, [0336](../experiments/0336-writing-paragraph-borders.md)) ([0262](../experiments/0262-paragraph-border.md), [0273](../experiments/0273-border-edges.md)) |

Values 0 to 3 are *confirmed* ([0010](../experiments/0010-alignment.md), [0011](../experiments/0011-left-alignment.md)); 4 as natural alignment is *likely*.

## Named and unnamed styles

Named styles such as Body set every property; unnamed ones set only what differs from their parent (field 1.3). *Likely* ([0010](../experiments/0010-alignment.md)). That an unnamed style takes what it leaves out from the style in its field 1.3 is *confirmed* by writing another parent there ([0393](../experiments/0393-writing-a-style-parent.md)).

Field 10 has equalled the number of properties set in every unnamed style so far, and is 57 in the named paragraph styles, which set 59. It doesn't count edits. *Unknown* ([0010](../experiments/0010-alignment.md), [0011](../experiments/0011-left-alignment.md), [0152](../experiments/0152-size-and-colour.md))

## List styles

A list style (type 2023) stores most properties as nine repeated values, one per list level. Field 11 is the kind of marker (0 none, 2 a text character, 3 a number), field 16 the marker text for kind 2, and field 13 an indent in points that grows by a fixed step per level, moving the marker and text together. *Likely* ([0014](../experiments/0014-lists.md)); fields 11, 13 and 16 *confirmed* by writing them and measuring ([0334](../experiments/0334-writing-list-markers.md))

## Finding a character's formatting

To find a character's formatting, take each property from the first style that sets it. Look first in its character style (from the field-8 runs), then that style's parent (field 1.3), and so on. Then look in its paragraph style (from the field-5 runs) and that style's parents. A property set to 0 counts as set. A font name in 11.5 may already include a weight, such as `HelveticaNeue-Bold`; Pages takes only the family from it, and the face from the bold and italic flags (*confirmed* by writing them: `HelveticaNeue-Bold` with bold 0 is drawn regular, [0428](../experiments/0428-writing-a-font-name-with-a-weight.md)). *Likely* for bold, italic, size and font: the rule predicted Pages' own reading of all 19 words of 8 documents ([0033](../experiments/0033-style-resolution.md), [0034](../experiments/0034-mixed-paragraph-styles.md)). It also holds for text colour ([0042](../experiments/0042-colour-resolution.md)).
