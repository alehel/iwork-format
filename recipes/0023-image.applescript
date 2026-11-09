-- Experiment 0023: save a document with body text "one" and an image placed on the page.
-- Usage: osascript recipes/0023-image.applescript /absolute/path/doc.pages /absolute/path/image.png
-- The folder must exist. Pages opens while the recipe runs.

on run argv
	if (count of argv) is not 2 then error "usage: osascript 0023-image.applescript /absolute/path/doc.pages /absolute/path/image.png"
	set outFile to POSIX file (item 1 of argv)
	set imageFile to POSIX file (item 2 of argv)
	tell application "Pages"
		set theDoc to make new document
		set body text of theDoc to "one"
		tell page 1 of theDoc to make new image with properties {file:imageFile}
		save theDoc in outFile
		close theDoc saving no
	end tell
end run
