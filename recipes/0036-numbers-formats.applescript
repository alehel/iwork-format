-- Experiment 0036: save a Numbers spreadsheet with one cell in each of six more formats.
-- Usage: osascript recipes/0036-numbers-formats.applescript /absolute/path/doc.numbers
-- B2 checkbox (true), C2 rating (3), D2 fraction (0.5), E2 scientific (1234.5),
-- F2 text ("042"), G2 duration (90). The folder must exist. Numbers opens while it runs.

on run argv
	if (count of argv) is not 1 then error "usage: osascript 0036-numbers-formats.applescript /absolute/path/doc.numbers"
	set outFile to POSIX file (item 1 of argv)
	tell application "Numbers"
		set theDoc to make new document
		tell table 1 of sheet 1 of theDoc
			set format of cell "B2" to checkbox
			set value of cell "B2" to true
			set format of cell "C2" to rating
			set value of cell "C2" to 3
			set format of cell "D2" to fraction
			set value of cell "D2" to 0.5
			set format of cell "E2" to scientific
			set value of cell "E2" to 1234.5
			set format of cell "F2" to text
			set value of cell "F2" to "042"
			set format of cell "G2" to duration
			set value of cell "G2" to 90
		end tell
		save theDoc in outFile
		close theDoc saving no
	end tell
end run
