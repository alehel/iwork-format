-- Experiments 0061-0062: save a Numbers spreadsheet with "abc" in B2 and one alignment setting changed.
-- Usage: osascript recipes/0061-numbers-alignment.applescript /absolute/path/doc.numbers center|top-nowrap
-- center sets B2's alignment to center; top-nowrap sets its vertical alignment to top and text wrap to false.
-- The folder must exist. Numbers opens while the recipe runs.

on run argv
	if (count of argv) is not 2 then error "usage: osascript 0061-numbers-alignment.applescript doc.numbers center|top-nowrap"
	set outFile to POSIX file (item 1 of argv)
	set what to item 2 of argv
	tell application "Numbers"
		set theDoc to make new document
		tell table 1 of sheet 1 of theDoc
			set value of cell "B2" to "abc"
			if what is "center" then
				set alignment of cell "B2" to center
			else
				set vertical alignment of cell "B2" to top
				set text wrap of cell "B2" to false
			end if
		end tell
		save theDoc in outFile
		close theDoc saving no
	end tell
end run
