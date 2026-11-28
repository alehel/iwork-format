#!/bin/sh
# Experiment 0482 onward: open a Pages document, place an image on each named page, save a copy.
#
# Usage: sh recipes/0482-place-on-pages.sh IN OUT IMAGE PAGE [PAGE ...]
#
# IN is opened through Launch Services (CONTRIBUTING.md). For each PAGE, AppleScript makes an
# image from IMAGE on that page (`tell page N of d to make new image`), which Pages places on the
# page, not in the text. The document is saved as OUT, a new file, and closed. Prints the page
# count and, for each image, its page number as Pages reports it.
set -eu
in=$(cd "$(dirname "$1")" && pwd -P)/$(basename "$1")
out=$(cd "$(dirname "$2")" && pwd -P)/$(basename "$2")
img=$(cd "$(dirname "$3")" && pwd -P)/$(basename "$3")
shift 3
pages="$*"
if [ -d "/Applications/Pages Creator Studio.app" ]; then app="Pages Creator Studio"; else app="Pages"; fi
open -a "$app" "$in"
sed "s/APPNAME/$app/" <<'OSA' | osascript - "$in" "$out" "$img" "$pages"
on run argv
  set target to item 1 of argv
  set outFile to POSIX file (item 2 of argv)
  set imageFile to POSIX file (item 3 of argv)
  set AppleScript's text item delimiters to " "
  set pageList to text items of (item 4 of argv)
  tell application "APPNAME"
    set d to missing value
    repeat 60 times
      repeat with x in documents
        try
          set p to POSIX path of (file of x as alias)
          if p ends with "/" then set p to text 1 thru -2 of p
          if p is target then set d to contents of x
        end try
      end repeat
      if d is not missing value then exit repeat
      delay 0.5
    end repeat
    if d is missing value then error "document did not open: " & target
    set n to count of pages of d
    repeat with i from 1 to count of pageList
      set pageNumber to (item i of pageList) as integer
      tell page pageNumber of d to make new image with properties {file:imageFile}
    end repeat
    save d in outFile
    set r to "pages: " & n
    close d saving no
  end tell
  return r
end run
OSA
