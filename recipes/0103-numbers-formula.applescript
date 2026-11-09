-- Experiments 0103-0112: save a Numbers spreadsheet with B2 = 4, C2 = 2 and one formula in E2.
-- Usage: osascript recipes/0103-numbers-formula.applescript /absolute/path/doc.numbers formula [second-sheet]
-- If a third argument is given, a second sheet with that name is added first, with 9 in B2 of its table.
-- The formula is typed as in a Norwegian Numbers, with ";" between arguments. The folder must exist.

on run argv
	if (count of argv) < 2 then error "usage: osascript 0103-numbers-formula.applescript doc.numbers formula [second-sheet]"
	set outFile to POSIX file (item 1 of argv)
	set theFormula to item 2 of argv
	tell application "Numbers"
		set theDoc to make new document
		if (count of argv) is 3 then
			tell theDoc to set s2 to make new sheet with properties {name:(item 3 of argv)}
			set value of cell "B2" of table 1 of s2 to 9
		end if
		tell table 1 of sheet 1 of theDoc
			set value of cell "B2" to 4
			set value of cell "C2" to 2
			set value of cell "E2" to theFormula
		end tell
		save theDoc in outFile
		close theDoc saving no
	end tell
end run
