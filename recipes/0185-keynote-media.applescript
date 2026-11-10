-- Experiments 0185-0187: save a Keynote presentation with a sound or movie on slide 1.
-- Usage: osascript recipes/0185-keynote-media.applescript mode /absolute/path/out.key /absolute/path/media
-- Modes:
--   audio  an audio clip from the media file
--   loop   the same, with repetition method loop and volume 50
--   movie  a movie from the media file
-- The folder must exist. Keynote opens while the recipe runs.

on run argv
	set mode to item 1 of argv
	set outFile to POSIX file (item 2 of argv)
	set media to POSIX file (item 3 of argv)
	tell application "Keynote"
		set theDoc to my newKeynote()
		tell slide 1 of theDoc
			-- "make new audio clip" and "make new movie" add nothing. "make new image" with a
			-- sound or movie file makes an audio clip or movie instead.
			set a to make new image with properties {file:media}
			if mode is "loop" then
				set a to audio clip 1
				set repetition method of a to loop
				set clip volume of a to 50
			end if
		end tell
		save theDoc in outFile
		close theDoc saving no
	end tell
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
