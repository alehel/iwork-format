-- Experiment 0067: save a Keynote presentation whose first slide has a vertical bar chart.
-- Usage: osascript recipes/0067-keynote-chart.applescript /absolute/path/doc.key
-- Rows "r1" and "r2", columns "a", "b" and "c"; data {1, 2, 3} and {4, 5, 6}.
-- The folder must exist. Keynote opens while the recipe runs.

on run argv
	if (count of argv) is not 1 then error "usage: osascript 0067-keynote-chart.applescript /absolute/path/doc.key"
	set outFile to POSIX file (item 1 of argv)
	tell application "Keynote"
		set theDoc to my newKeynote()
		add chart slide 1 of theDoc row names {"r1", "r2"} column names {"a", "b", "c"} data {{1, 2, 3}, {4, 5, 6}} type vertical_bar_2d group by chart row
		save theDoc in outFile
		close theDoc saving no
	end tell
end run

-- A new Keynote presentation in the theme named in IWORK_KEYNOTE_THEME, such as
-- "iwork-format test" (experiment 0291), or in Keynote's default theme when it is unset.
on newKeynote()
	set t to system attribute "IWORK_KEYNOTE_THEME"
	tell application "Keynote"
		if t is "" then return make new document
		return make new document with properties {document theme:theme t}
	end tell
end newKeynote
