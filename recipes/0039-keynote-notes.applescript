-- Experiment 0039: save a Keynote presentation whose first slide has presenter notes "notes here".
-- Usage: osascript recipes/0039-keynote-notes.applescript /absolute/path/doc.key
-- The folder must exist. Keynote opens while the recipe runs.

on run argv
	if (count of argv) is not 1 then error "usage: osascript 0039-keynote-notes.applescript /absolute/path/doc.key"
	set outFile to POSIX file (item 1 of argv)
	tell application "Keynote"
		set theDoc to make new document
		set presenter notes of slide 1 of theDoc to "notes here"
		save theDoc in outFile
		close theDoc saving no
	end tell
end run
