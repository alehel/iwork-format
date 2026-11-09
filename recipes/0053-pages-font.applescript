-- Experiment 0053: save "one two three" with the font of word 2 set to Georgia.
-- Usage: osascript recipes/0053-pages-font.applescript /absolute/path/doc.pages
-- The folder must exist. Pages opens while the recipe runs.

on run argv
	if (count of argv) is not 1 then error "usage: osascript 0053-pages-font.applescript /absolute/path/doc.pages"
	set outFile to POSIX file (item 1 of argv)
	tell application "Pages"
		set theDoc to make new document
		set body text of theDoc to "one two three"
		set font of word 2 of body text of theDoc to "Georgia"
		save theDoc in outFile
		close theDoc saving no
	end tell
end run
