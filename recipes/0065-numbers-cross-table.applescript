-- Experiment 0065: save a Numbers spreadsheet where table 1's E2 refers to B2 of a second table named "Other".
-- Usage: osascript recipes/0065-numbers-cross-table.applescript /absolute/path/doc.numbers
-- The folder must exist. Numbers opens while the recipe runs.

on run argv
	if (count of argv) is not 1 then error "usage: osascript 0065-numbers-cross-table.applescript /absolute/path/doc.numbers"
	set outFile to POSIX file (item 1 of argv)
	tell application "Numbers"
		set theDoc to make new document
		tell sheet 1 of theDoc to make new table with properties {name:"Other"}
		set value of cell "B2" of table "Other" of sheet 1 of theDoc to 9
		set value of cell "E2" of table 1 of sheet 1 of theDoc to "=Other::B2"
		save theDoc in outFile
		close theDoc saving no
	end tell
end run
