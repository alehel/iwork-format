-- Experiment 0038: save a Keynote presentation with two slides, titled "first" and "second".
-- Usage: osascript recipes/0038-keynote-two-slides.applescript /absolute/path/doc.key
-- The folder must exist. Keynote opens while the recipe runs.

on run argv
	if (count of argv) is not 1 then error "usage: osascript 0038-keynote-two-slides.applescript /absolute/path/doc.key"
	set outFile to POSIX file (item 1 of argv)
	tell application "Keynote"
		set theDoc to make new document
		set object text of default title item of slide 1 of theDoc to "first"
		tell theDoc to make new slide
		set object text of default title item of slide 2 of theDoc to "second"
		save theDoc in outFile
		close theDoc saving no
	end tell
end run
