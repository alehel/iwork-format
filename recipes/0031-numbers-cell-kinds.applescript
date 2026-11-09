-- Experiment 0031: save a Numbers spreadsheet with one cell of each kind in row 2 of the first table.
-- Usage: osascript recipes/0031-numbers-cell-kinds.applescript /absolute/path/doc.numbers
-- B2: 42 as currency; C2: 0.25 as percent; D2: true; E2: the date 2026-01-02 12:00;
-- F2: the formula =B2*2; G2: 42 with the default format. The folder must exist.

on run argv
	if (count of argv) is not 1 then error "usage: osascript 0031-numbers-cell-kinds.applescript /absolute/path/doc.numbers"
	set outFile to POSIX file (item 1 of argv)
	set theDate to current date
	set year of theDate to 2026
	set month of theDate to 1
	set day of theDate to 2
	set time of theDate to 12 * hours
	tell application "Numbers"
		set theDoc to make new document
		tell table 1 of sheet 1 of theDoc
			set value of cell "B2" to 42
			set format of cell "B2" to currency
			set value of cell "C2" to 0.25
			set format of cell "C2" to percent
			set value of cell "D2" to true
			set value of cell "E2" to theDate
			set value of cell "F2" to "=B2*2"
			set value of cell "G2" to 42
		end tell
		save theDoc in outFile
		close theDoc saving no
	end tell
end run
