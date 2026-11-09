-- Experiment 0064: save a Numbers spreadsheet with formulas using operators and functions.
-- Usage: osascript recipes/0064-numbers-functions.applescript /absolute/path/doc.numbers
-- B2 = 4, C2 = 2; E2..E10 hold, in order: =B2-C2, =B2/C2, =B2^2, =B2&C2, =AVERAGE(B2:C2),
-- =MIN(B2:C2), =MAX(B2:C2), =IF(B2>1,1,0), =COUNT(B2:C2). The folder must exist.

on run argv
	if (count of argv) is not 1 then error "usage: osascript 0064-numbers-functions.applescript /absolute/path/doc.numbers"
	set outFile to POSIX file (item 1 of argv)
	set formulas to {"=B2-C2", "=B2/C2", "=B2^2", "=B2&C2", "=AVERAGE(B2:C2)", "=MIN(B2:C2)", "=MAX(B2:C2)", "=IF(B2>1,1,0)", "=COUNT(B2:C2)"}
	tell application "Numbers"
		set theDoc to make new document
		tell table 1 of sheet 1 of theDoc
			set value of cell "B2" to 4
			set value of cell "C2" to 2
			repeat with i from 1 to count of formulas
				set value of cell ("E" & (i + 1)) to item i of formulas
			end repeat
		end tell
		save theDoc in outFile
		close theDoc saving no
	end tell
end run
