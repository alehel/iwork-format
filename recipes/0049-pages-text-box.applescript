-- Experiment 0049: save a Pages document with body text "one" and a text box reading "box" on page 1.
-- Usage: osascript recipes/0049-pages-text-box.applescript /absolute/path/doc.pages
-- The folder must exist. Pages opens while the recipe runs.

on run argv
	if (count of argv) is not 1 then error "usage: osascript 0049-pages-text-box.applescript /absolute/path/doc.pages"
	set outFile to POSIX file (item 1 of argv)
	tell application "Pages"
		set theDoc to make new document
		set body text of theDoc to "one"
		tell page 1 of theDoc to make new text item with properties {object text:"box"}
		save theDoc in outFile
		close theDoc saving no
	end tell
end run
