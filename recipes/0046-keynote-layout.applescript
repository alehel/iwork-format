-- Experiment 0046: save a Keynote presentation whose first slide uses the layout (master slide) given by name.
-- Usage: osascript recipes/0046-keynote-layout.applescript /absolute/path/doc.key layout-name
-- The folder must exist. Keynote opens while the recipe runs.

on run argv
	if (count of argv) is not 2 then error "usage: osascript 0046-keynote-layout.applescript /absolute/path/doc.key layout-name"
	set outFile to POSIX file (item 1 of argv)
	set layoutName to item 2 of argv
	tell application "Keynote"
		set theDoc to my newKeynote()
		set base slide of slide 1 of theDoc to master slide layoutName of theDoc
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
