-- Experiment 0043: save a Numbers spreadsheet with 42 in B2 to F2, formatted differently.
-- Usage: osascript recipes/0043-numbers-cell-style.applescript /absolute/path/doc.numbers
-- B2 plain; C2 font size 20; D2 font Helvetica-Bold; E2 text colour red; F2 background red.
-- The folder must exist. Numbers opens while the recipe runs.

on run argv
	if (count of argv) is not 1 then error "usage: osascript 0043-numbers-cell-style.applescript /absolute/path/doc.numbers"
	set outFile to POSIX file (item 1 of argv)
	tell application "Numbers"
		set theDoc to make new document
		tell table 1 of sheet 1 of theDoc
			repeat with c in {"B2", "C2", "D2", "E2", "F2"}
				set value of cell c to 42
			end repeat
			set font size of cell "C2" to 20
			set font name of cell "D2" to "Helvetica-Bold"
			set text color of cell "E2" to {65535, 0, 0}
			set background color of cell "F2" to {65535, 0, 0}
		end tell
		save theDoc in outFile
		close theDoc saving no
	end tell
end run
