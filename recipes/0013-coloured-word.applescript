-- Experiment 0013: save "one two three" with the second word in a colour.
-- Usage: osascript recipes/0013-coloured-word.applescript /absolute/path/doc.pages red green blue
-- Each component is 0 to 65535, as Pages' AppleScript colours are. The folder must exist.

on run argv
	if (count of argv) is not 4 then error "usage: osascript 0013-coloured-word.applescript /absolute/path/doc.pages red green blue"
	set outFile to POSIX file (item 1 of argv)
	set theColour to {(item 2 of argv) as integer, (item 3 of argv) as integer, (item 4 of argv) as integer}
	tell application "Pages"
		set theDoc to make new document
		set body text of theDoc to "one two three"
		set color of word 2 of body text of theDoc to theColour
		save theDoc in outFile
		close theDoc saving no
	end tell
end run
