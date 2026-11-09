-- Experiment 0025: save a new Keynote presentation whose first slide's title is the given text.
-- Usage: osascript recipes/0025-keynote-title.applescript /absolute/path/doc.key [text]
-- The text defaults to "hello". The folder must exist. Keynote opens while the recipe runs.

on run argv
	if (count of argv) < 1 or (count of argv) > 2 then error "usage: osascript 0025-keynote-title.applescript /absolute/path/doc.key [text]"
	set outFile to POSIX file (item 1 of argv)
	set theText to "hello"
	if (count of argv) is 2 then set theText to item 2 of argv
	tell application "Keynote"
		set theDoc to make new document
		set object text of default title item of slide 1 of theDoc to theText
		save theDoc in outFile
		close theDoc saving no
	end tell
end run
