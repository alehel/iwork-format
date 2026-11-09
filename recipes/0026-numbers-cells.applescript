-- Experiment 0026: save a new Numbers spreadsheet with 42 in cell B2 and "abc" in cell C3.
-- Usage: osascript recipes/0026-numbers-cells.applescript /absolute/path/doc.numbers
-- The folder must exist. Numbers opens while the recipe runs.

on run argv
	if (count of argv) is not 1 then error "usage: osascript 0026-numbers-cells.applescript /absolute/path/doc.numbers"
	set outFile to POSIX file (item 1 of argv)
	tell application "Numbers"
		set theDoc to make new document
		tell table 1 of sheet 1 of theDoc
			set value of cell "B2" to 42
			set value of cell "C3" to "abc"
		end tell
		save theDoc in outFile
		close theDoc saving no
	end tell
end run
