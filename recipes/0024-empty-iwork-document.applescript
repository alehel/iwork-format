-- Experiment 0024: save a new, empty document from Keynote, Numbers or Pages.
-- Usage: osascript recipes/0024-empty-iwork-document.applescript Keynote|Numbers|Pages /absolute/path/empty.ext
-- The folder must exist. The app opens while the recipe runs.

on run argv
	if (count of argv) is not 2 then error "usage: osascript 0024-empty-iwork-document.applescript Keynote|Numbers|Pages /absolute/path/empty.ext"
	set appName to item 1 of argv
	set outFile to POSIX file (item 2 of argv)
	using terms from application "Pages"
		tell application appName
			set theDoc to make new document
			save theDoc in outFile
			close theDoc saving no
		end tell
	end using terms from
end run
