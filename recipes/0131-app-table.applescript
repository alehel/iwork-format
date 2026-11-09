-- Experiments 0131-0138: save a Pages or Keynote document with a 5 x 5 table made through AppleScript, changed one way.
-- Usage: osascript recipes/0131-app-table.applescript Pages|Keynote /absolute/path/doc mode
-- Modes: cells (42 in B2, "abc" in C3), formula (4 in B2, 2 in C2, =B2*C2 in E2), merge (B2:C3 merged,
-- 42 in B2), headers (2 header rows), currency (42 in B2, currency format), fill (B2 background red).
-- The folder must exist. The app opens while the recipe runs.

on run argv
	if (count of argv) is not 3 then error "usage: osascript 0131-app-table.applescript Pages|Keynote doc mode"
	set appName to item 1 of argv
	set outFile to POSIX file (item 2 of argv)
	set mode to item 3 of argv
	if appName is "Pages" then
		tell application "Pages"
			set theDoc to make new document
			tell page 1 of theDoc to set t to make new table with properties {row count:5, column count:5}
			my changeTable(t, mode)
			save theDoc in outFile
			close theDoc saving no
		end tell
	else
		tell application "Keynote"
			set theDoc to make new document
			tell slide 1 of theDoc to set t to make new table with properties {row count:5, column count:5}
			my changeTable(t, mode)
			save theDoc in outFile
			close theDoc saving no
		end tell
	end if
end run

on changeTable(t, mode)
	using terms from application "Numbers"
		if mode is "cells" then
			set value of cell "B2" of t to 42
			set value of cell "C3" of t to "abc"
		else if mode is "formula" then
			set value of cell "B2" of t to 4
			set value of cell "C2" of t to 2
			set value of cell "E2" of t to "=B2*C2"
		else if mode is "merge" then
			merge range "B2:C3" of t
			set value of cell "B2" of t to 42
		else if mode is "headers" then
			set header row count of t to 2
		else if mode is "currency" then
			set value of cell "B2" of t to 42
			set format of cell "B2" of t to currency
		else if mode is "fill" then
			set background color of cell "B2" of t to {65535, 0, 0}
		end if
	end using terms from
end changeTable
