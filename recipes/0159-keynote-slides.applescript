-- Experiments 0159-0168: save Keynote presentations that test slides.
-- Usage: osascript recipes/0159-keynote-slides.applescript mode /absolute/path/out.key
-- Modes:
--   dup          slide 1 titled "A", then duplicated
--   move         three slides titled "A", "B", "C"; slide 3 then moved to the front
--   delete       three slides titled "A", "B", "C"; slide 2 then deleted
--   ten          ten slides titled "1" to "10"
--   notes        one slide with the presenter notes "one", "two" and "three" as three paragraphs
--   titlebreak   one slide titled "one", a linefeed, "two"
--   layouts      one slide for each of the first six slide layouts, in the order Keynote lists them
--   line         one slide with a line from (100, 100) to (300, 200)
--   shapetext    one slide with a shape holding the text "shape"
--   untouched    one slide whose title was never set
-- The folder must exist. Keynote opens while the recipe runs.

on run argv
	set mode to item 1 of argv
	set outFile to POSIX file (item 2 of argv)
	tell application "Keynote"
		set theDoc to my newKeynote()
		tell theDoc
			if mode is "dup" then
				set object text of default title item of slide 1 to "A"
				duplicate slide 1
			else if mode is "move" or mode is "delete" then
				set object text of default title item of slide 1 to "A"
				make new slide
				set object text of default title item of slide 2 to "B"
				make new slide
				set object text of default title item of slide 3 to "C"
				if mode is "move" then move slide 3 to before slide 1
				if mode is "delete" then delete slide 2
			else if mode is "ten" then
				set object text of default title item of slide 1 to "1"
				repeat with i from 2 to 10
					make new slide
					set object text of default title item of slide i to (i as text)
				end repeat
			else if mode is "notes" then
				set presenter notes of slide 1 to "one" & linefeed & "two" & linefeed & "three"
			else if mode is "titlebreak" then
				set object text of default title item of slide 1 to "one" & linefeed & "two"
			else if mode is "layouts" then
				repeat with i from 1 to 6
					if i > 1 then make new slide
					set base slide of slide i to slide layout i
				end repeat
			else if mode is "line" then
				tell slide 1 to make new line with properties {start point:{100, 100}, end point:{300, 200}}
			else if mode is "shapetext" then
				tell slide 1 to make new shape with properties {object text:"shape"}
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
