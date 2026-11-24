#!/bin/bash
# Experiment 0469: rerun, unchanged, the AppleScript recipes of experiments 0461, 0464 and 0466 in
# whichever release of the apps is installed, and compare each document with the 15.4 one.
#
# Usage: bash recipes/0469-rerun-in-16-0.sh [OUT]
#
# OUT defaults to samples/0469. Run from the repository root, with the 15.4 samples in samples/.
# Each pair is compared with recipes/0461-compare-structure.py; UUIDs, the build history, the
# format version and record counts that agree are left out of what it prints.
set -u
out=${1:-samples/0469}
mkdir -p "$out/0197" "$out/0243"
P=$(cd "$out" && pwd -P)
pairs=()

# Pages and Numbers: the recipes of 0461 and 0464, each taking only an output path.
osascript recipes/0001-empty-document.applescript "$P/empty.pages";      pairs+=("0001/empty-a.pages empty.pages")
osascript recipes/0002-one-word.applescript "$P/hello.pages";            pairs+=("0002/hello.pages hello.pages")
osascript recipes/0026-numbers-cells.applescript "$P/cells.numbers";     pairs+=("0026/cells.numbers cells.numbers")
for e in 0030 0031 0035 0036 0037 0043 0044 0045 0047 0049 0050 0051 0052 0053 0054 0058 \
         0059 0060 0063 0064 0065 0066 0078 0198; do
  r=$(ls recipes/$e-*.applescript | head -1)
  old=$(ls samples/$e/*.pages samples/$e/*.numbers 2>/dev/null | head -1)
  osascript "$r" "$P/$e-$(basename "$old")" || echo "FAILED $e"
  pairs+=("${old#samples/} $e-$(basename "$old")")
done

# Keynote: the recipes of 0466, Basic White, including 0196's radial wipe.
osascript recipes/0024-empty-iwork-document.applescript Keynote "$P/0024-empty-a.key"
osascript recipes/0025-keynote-title.applescript "$P/0025-hello.key"
osascript recipes/0038-keynote-two-slides.applescript "$P/0038-two-slides.key"
osascript recipes/0039-keynote-notes.applescript "$P/0039-notes.key"
osascript recipes/0046-keynote-layout.applescript "$P/0046-blank-layout.key" Tom
osascript recipes/0067-keynote-chart.applescript "$P/0067-chart.key"
osascript recipes/0068-keynote-variants.applescript "$P/0068-textbox.key" textbox
osascript recipes/0087-keynote-document-settings.applescript "$P/0087-autoplay.key" autoplay
osascript recipes/0091-keynote-transitions.applescript "$P/0091-movein.key" movein
osascript recipes/0096-keynote-objects.applescript "$P/0096-textstyle.key" textstyle
osascript recipes/0159-keynote-slides.applescript dup "$P/0159-dup.key"
osascript recipes/0196-keynote-all-transitions.applescript "$P/0196-all.key" || echo "FAILED 0196"
osascript recipes/0197-keynote-idle.applescript "$P/0197"
osascript recipes/0243-keynote-body-showing.applescript "$P/0243"
pairs+=("0024/empty-a.key 0024-empty-a.key" "0025/hello.key 0025-hello.key"
  "0038/two-slides.key 0038-two-slides.key" "0039/notes.key 0039-notes.key"
  "0046/blank-layout.key 0046-blank-layout.key" "0067/chart.key 0067-chart.key"
  "0068/textbox.key 0068-textbox.key" "0087/autoplay.key 0087-autoplay.key"
  "0091/movein.key 0091-movein.key" "0096/textstyle.key 0096-textstyle.key"
  "0159/dup.key 0159-dup.key" "0196/all.key 0196-all.key"
  "0197/default.key 0197/default.key" "0197/idle.key 0197/idle.key"
  "0243/body.key 0243/body.key" "0243/no-body.key 0243/no-body.key")

for pair in "${pairs[@]}"; do
  set -- $pair
  echo "=== $1"
  python3 -I recipes/0461-compare-structure.py "samples/$1" "$P/$2" \
    | grep -vE "UUID|revision|BuildVersionHistory|fileFormatVersion|-> [0-9]+ records$"
done
