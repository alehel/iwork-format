-- Experiment 0054: save "one two three" with words 1 and 3 at 14 points and word 2 at 20 points.
-- Usage: osascript recipes/0054-pages-sizes.applescript /absolute/path/doc.pages
-- The folder must exist. Pages opens while the recipe runs.

on run argv
	if (count of argv) is not 1 then error "usage: osascript 0054-pages-sizes.applescript /absolute/path/doc.pages"
	set outFile to POSIX file (item 1 of argv)
	tell application "Pages"
		set theDoc to make new document
		set body text of theDoc to "one two three"
		set size of word 1 of body text of theDoc to 14
		set size of word 2 of body text of theDoc to 20
		set size of word 3 of body text of theDoc to 14
		save theDoc in outFile
		close theDoc saving no
	end tell
end run
