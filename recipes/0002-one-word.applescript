-- Experiment 0002: save a new Pages document whose body text is one word.
-- Usage: osascript recipes/0002-one-word.applescript /absolute/path/word.pages [word]
-- The word defaults to "hello". The folder must exist. Pages opens while the recipe runs.

on run argv
	if (count of argv) < 1 or (count of argv) > 2 then error "usage: osascript 0002-one-word.applescript /absolute/path/word.pages [word]"
	set outFile to POSIX file (item 1 of argv)
	set theWord to "hello"
	if (count of argv) is 2 then set theWord to item 2 of argv
	tell application "Pages"
		set theDoc to make new document
		set body text of theDoc to theWord
		save theDoc in outFile
		close theDoc saving no
	end tell
end run
