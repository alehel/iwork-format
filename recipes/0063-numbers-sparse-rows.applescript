-- Experiment 0063: save a Numbers spreadsheet whose first table has 1000 rows, with 1 in B2, 2 in B600 and 3 in B1000.
-- Usage: osascript recipes/0063-numbers-sparse-rows.applescript /absolute/path/doc.numbers
-- The folder must exist. Numbers opens while the recipe runs.

on run argv
	if (count of argv) is not 1 then error "usage: osascript 0063-numbers-sparse-rows.applescript /absolute/path/doc.numbers"
	set outFile to POSIX file (item 1 of argv)
	tell application "Numbers"
		set theDoc to make new document
		tell table 1 of sheet 1 of theDoc
			set row count to 1000
			set value of cell "B2" to 1
			set value of cell "B600" to 2
			set value of cell "B1000" to 3
		end tell
		save theDoc in outFile
		close theDoc saving no
	end tell
end run
