-- Experiment 0066: save a Numbers spreadsheet with comparison and IF formulas written with semicolons.
-- Usage: osascript recipes/0066-numbers-if.applescript /absolute/path/doc.numbers
-- B2 = 4; E2 "=IF(B2>1;1;0)", E3 "=B2<1", E4 "=B2=4", E5 "=B2>=4", E6 "=B2<=4", E7 "=B2<>4".
-- The folder must exist. Numbers opens while the recipe runs.

on run argv
	if (count of argv) is not 1 then error "usage: osascript 0066-numbers-if.applescript /absolute/path/doc.numbers"
	set outFile to POSIX file (item 1 of argv)
	set formulas to {"=IF(B2>1;1;0)", "=B2<1", "=B2=4", "=B2>=4", "=B2<=4", "=B2<>4"}
	tell application "Numbers"
		set theDoc to make new document
		tell table 1 of sheet 1 of theDoc
			set value of cell "B2" to 4
			repeat with i from 1 to count of formulas
				set value of cell ("E" & (i + 1)) to item i of formulas
			end repeat
		end tell
		save theDoc in outFile
		close theDoc saving no
	end tell
end run
