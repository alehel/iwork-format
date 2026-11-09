-- Experiments 0087-0091: save a new Keynote presentation with one document setting changed.
-- Usage: osascript recipes/0087-keynote-document-settings.applescript /absolute/path/doc.key setting
-- Settings: autoplay, autoloop, autorestart (with a maximum idle duration of 30 seconds), theme
-- (the second theme Keynote lists). The folder must exist. Keynote opens while the recipe runs.

on run argv
	if (count of argv) is not 2 then error "usage: osascript 0087-keynote-document-settings.applescript doc.key setting"
	set outFile to POSIX file (item 1 of argv)
	set what to item 2 of argv
	tell application "Keynote"
		if what is "theme" then
			set theDoc to make new document with properties {document theme:theme 2}
		else
			set theDoc to make new document
		end if
		if what is "autoplay" then set auto play of theDoc to true
		if what is "autoloop" then set auto loop of theDoc to true
		if what is "autorestart" then
			set auto restart of theDoc to true
			set maximum idle duration of theDoc to 30
		end if
		save theDoc in outFile
		close theDoc saving no
	end tell
end run
