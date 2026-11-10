-- Experiment 0024: save a new, empty document from Keynote, Numbers or Pages.
-- Usage: osascript recipes/0024-empty-iwork-document.applescript Keynote|Numbers|Pages /absolute/path/empty.ext
-- The folder must exist. The app opens while the recipe runs.

on run argv
	if (count of argv) is not 2 then error "usage: osascript 0024-empty-iwork-document.applescript Keynote|Numbers|Pages /absolute/path/empty.ext"
	set appName to item 1 of argv
	set outFile to POSIX file (item 2 of argv)
	using terms from application "Pages"
		tell application appName
			if appName is "Keynote" then
				set theDoc to my newKeynote()
			else
				set theDoc to make new document
			end if
			save theDoc in outFile
			close theDoc saving no
		end tell
	end using terms from
end run

-- A new Keynote presentation in the theme named in IWORK_KEYNOTE_THEME, such as
-- "iwork-format test" (experiment 0291), or in Keynote's default theme when it is unset.
on newKeynote()
	set t to system attribute "IWORK_KEYNOTE_THEME"
	tell application "Keynote"
		if t is "" then return make new document
		return make new document with properties {document theme:theme t}
	end tell
end newKeynote
