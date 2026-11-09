-- Experiment 0004: save a document of two words, the second set in a larger size.
-- Usage: osascript recipes/0004-larger-word.applescript /absolute/path/doc.pages text [size]
-- The size defaults to 24 points; the text's second word gets it. Pass size 0 to leave
-- the text unchanged, for a baseline with the same words. The folder must exist.

on run argv
	if (count of argv) < 2 or (count of argv) > 3 then error "usage: osascript 0004-larger-word.applescript /absolute/path/doc.pages text [size]"
	set outFile to POSIX file (item 1 of argv)
	set theText to item 2 of argv
	set theSize to 24
	if (count of argv) is 3 then set theSize to (item 3 of argv) as number
	tell application "Pages"
		set theDoc to make new document
		set body text of theDoc to theText
		if theSize > 0 then set size of word 2 of body text of theDoc to theSize
		save theDoc in outFile
		close theDoc saving no
	end tell
end run
