# 0291: A test theme with our own images

**Status:** run

Every new Keynote presentation carries the images of its theme in `Data/`. With Basic White, the default theme, that is six stock photos and 17 thumbnails drawn from Apple's master slides, some showing those photos. Those images are Apple's, so the project's Keynote samples can't be published. This experiment builds a theme whose masters are Basic White's, with every photo replaced by a test card the project drew itself, and records what Keynote stores when it does.

## Setup

| | |
| --- | --- |
| Keynote | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Theme | Basic White (*Enkel, hvit*), Keynote's default |
| Cards | [`recipes/0291-test-cards.swift`](../recipes/0291-test-cards.swift), released under CC0 |

## Recipe

```bash
swift recipes/0291-test-cards.swift theme/cards
mkdir -p samples/0291
osascript recipes/0291-test-theme.applescript "$PWD/theme/cards" "$PWD/samples/0291/test-theme.key"
```

The Swift script draws nine test cards. The photo cards are at most 1024 pixels on the longer side, to keep presentations small; a first version drew them at the photos' full size, which made the theme 2.5 MB rather than 0.9 MB. The cards are: six with the proportions of Basic White's six photos (`photo-a` to `photo-f`), a 1920 × 1080 background, a transparent PNG and a 64 × 48 image. Each card prints its own name, role, size and format, with a grid, diagonals, a centre circle and corner tags (TL, TR, BL, BR) to show scaling, cropping and flips.

AppleScript lists the images on each master slide of a new presentation. Basic White has seven, on five masters:

| Master | Image | Size on the slide | Card |
| --- | --- | --- | --- |
| 2, Title & Photo | `666699290_02_crop_3159x1892.jpg` | 1920 × 1080 | `photo-f` |
| 3, Title & Photo Alt | `910457886_1434x1669.jpg` | 860 × 880 | `photo-a` |
| 6, Title, Bullets & Photo | `660384004_1290x1720.jpg` | 860 × 881 | `photo-b` |
| 15, Photo – 3 Up | `886640052_1858x1486.jpg` | 585 × 426 | `photo-d` |
| 15, Photo – 3 Up | `910457886_1434x1669.jpg` | 585 × 426 | `photo-a` |
| 15, Photo – 3 Up | `660384004_rotate_1964x1473.jpg` | 1116 × 885 | `photo-c` |
| 16, Photo | `886640052_3195x2556.jpg` | 1920 × 1080 | `photo-e` |

The recipe sets each image's `file name` to its card, which AppleScript allows on a master's image, and saves. The result's thumbnails were then checked, and the document saved as a theme with File → Save Theme → Add to Theme Chooser (*Arkiv → Lagre tema → Legg til i Temavelger*), which isn't scriptable.

## Observation

**Replacing the images.** After `set file name`, each image names its card. The photos are gone from `Data/`. Each card is stored once under its own name (`photo-a-9080.jpg`), even though `photo-a` fills two placeholders. Keynote adds a reduced copy of each, at most 256 pixels on the longer side, named `photo-a-small-9081.jpeg`. Apple's photos were stored only in that reduced form, `…-small-N.jpeg`, at 256 pixels.

**Thumbnails.** `Data/` also holds one `mt-UUID-N.jpg` per master slide, 356 × 200 pixels, and one `st-UUID-N.jpg` for the slide. The master thumbnails keep their UUID from the theme: the same 17 names appear in every Basic White presentation. Saving after the replacement redrew most of them, but not the Photo and Photo – 3 Up masters, whose thumbnails still showed Apple's photos. Adding one slide per master and saving again redrew those two as well. Four thumbnails were never redrawn, and show only Apple's placeholder text (*Statement*, *“Notable Quote”*, *100% Fact information*) or an empty slide.

**The theme file.** The saved theme is a `.kth` file in `~/Library/Containers/com.apple.Keynote/Data/Library/Application Support/User Templates/`, named by a UUID. It is a ZIP laid out like a `.key`: the same `Index/`, `Metadata/` and `Data/` parts and previews. Its 30 data files are the six cards, their reduced copies, 17 master thumbnails and one slide thumbnail. None of its parts contains the theme's name. Keynote took the name from the presentation's file name. It probably keeps the names with its themes in iCloud: a theme added and then removed from that folder stayed in Keynote's theme list.

## Conclusion

A theme with the project's own images can be built from Basic White by script, except for the final Save Theme. A master's image can be swapped with AppleScript's `file name`. Its master thumbnail, though, is redrawn only once the master is shown, so a builder must use every master on a slide before saving.

A `.kth` theme is a Keynote document in the same container format, with a different extension. Two data findings from Pages carry over to Keynote: identical files are stored once ([0142](0142-same-image-twice.md)), and large images get a reduced `-small` copy ([0148](0148-large-image.md)), here at most 256 pixels on the longer side.

The theme is in the repository as `theme/iwork-format test.kth`, with its cards in `theme/cards/`. How best to install it on another Mac isn't tested yet.

## Confidence

*Likely*:

- A theme file is a Keynote document.
- A master thumbnail is redrawn only when its master is shown.
- Keynote stores a reduced copy of an image at most 256 pixels on the longer side.
- The theme name comes from the file name and isn't stored in the file.
