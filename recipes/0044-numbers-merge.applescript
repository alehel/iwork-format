-- Experiment 0044: save a Numbers spreadsheet with cells B2:C3 merged and 42 in the merged cell.
-- Usage: osascript recipes/0044-numbers-merge.applescript /absolute/path/doc.numbers
-- The folder must exist. Numbers opens while the recipe runs.

on run argv
	if (count of argv) is not 1 then error "usage: osascript 0044-numbers-merge.applescript /absolute/path/doc.numbers"
	set outFile to POSIX file (item 1 of argv)
	tell application "Numbers"
		set theDoc to make new document
		tell table 1 of sheet 1 of theDoc
			merge range "B2:C3"
			set value of cell "B2" to 42
		end tell
		save theDoc in outFile
		close theDoc saving no
	end tell
end run
