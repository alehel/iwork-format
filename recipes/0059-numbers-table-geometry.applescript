-- Experiment 0059: save a Numbers spreadsheet whose first table is at (50, 60) and 300 x 150 points.
-- Usage: osascript recipes/0059-numbers-table-geometry.applescript /absolute/path/doc.numbers
-- The folder must exist. Numbers opens while the recipe runs.

on run argv
	if (count of argv) is not 1 then error "usage: osascript 0059-numbers-table-geometry.applescript /absolute/path/doc.numbers"
	set outFile to POSIX file (item 1 of argv)
	tell application "Numbers"
		set theDoc to make new document
		tell table 1 of sheet 1 of theDoc
			set position to {50, 60}
			set width to 300
			set height to 150
		end tell
		save theDoc in outFile
		close theDoc saving no
	end tell
end run
