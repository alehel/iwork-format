-- Experiment 0030: save a Numbers spreadsheet whose first table has 300 rows, with 42 in B2 and 7 in B300.
-- Usage: osascript recipes/0030-numbers-row-300.applescript /absolute/path/doc.numbers
-- The folder must exist. Numbers opens while the recipe runs.

on run argv
	if (count of argv) is not 1 then error "usage: osascript 0030-numbers-row-300.applescript /absolute/path/doc.numbers"
	set outFile to POSIX file (item 1 of argv)
	tell application "Numbers"
		set theDoc to make new document
		tell table 1 of sheet 1 of theDoc
			set row count to 300
			set value of cell "B2" to 42
			set value of cell "B300" to 7
		end tell
		save theDoc in outFile
		close theDoc saving no
	end tell
end run
