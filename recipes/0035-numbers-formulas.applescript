-- Experiment 0035: save a Numbers spreadsheet with formulas that refer to other cells.
-- Usage: osascript recipes/0035-numbers-formulas.applescript /absolute/path/doc.numbers
-- B2 = 1 and C3 = 2; then E2 "=B2", E3 "=C3", E4 "=$B$2", E5 "=B2+C3", E6 "=SUM(B2:C3)".
-- The folder must exist. Numbers opens while the recipe runs.

on run argv
	if (count of argv) is not 1 then error "usage: osascript 0035-numbers-formulas.applescript /absolute/path/doc.numbers"
	set outFile to POSIX file (item 1 of argv)
	tell application "Numbers"
		set theDoc to make new document
		tell table 1 of sheet 1 of theDoc
			set value of cell "B2" to 1
			set value of cell "C3" to 2
			set value of cell "E2" to "=B2"
			set value of cell "E3" to "=C3"
			set value of cell "E4" to "=$B$2"
			set value of cell "E5" to "=B2+C3"
			set value of cell "E6" to "=SUM(B2:C3)"
		end tell
		save theDoc in outFile
		close theDoc saving no
	end tell
end run
