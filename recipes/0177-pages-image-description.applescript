-- Experiment 0177: save a Pages document with an image whose description is "a red box".
-- Usage: osascript recipes/0177-pages-image-description.applescript /absolute/path/out.pages /absolute/path/image.png
-- The folder must exist. Pages opens while the recipe runs.

on run argv
	set outFile to POSIX file (item 1 of argv)
	set img to POSIX file (item 2 of argv)
	tell application "Pages"
		set theDoc to make new document
		set body text of theDoc to "one"
		tell page 1 of theDoc to set i1 to make new image with properties {file:img}
		set description of i1 to "a red box"
		save theDoc in outFile
		close theDoc saving no
	end tell
end run
