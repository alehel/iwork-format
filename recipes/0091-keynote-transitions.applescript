-- Experiments 0091-0095: save a Keynote presentation whose first slide has a given transition.
-- Usage: osascript recipes/0091-keynote-transitions.applescript /absolute/path/doc.key mode
-- Modes: movein, push, cube (each 1.5 seconds), auto (dissolve, starting automatically after a
-- delay of 3 seconds), magicmove. The folder must exist. Keynote opens while the recipe runs.

on run argv
	if (count of argv) is not 2 then error "usage: osascript 0091-keynote-transitions.applescript doc.key mode"
	set outFile to POSIX file (item 1 of argv)
	set mode to item 2 of argv
	tell application "Keynote"
		set theDoc to make new document
		set s to slide 1 of theDoc
		if mode is "movein" then
			set transition properties of s to {transition effect:move in, transition duration:1.5}
		else if mode is "push" then
			set transition properties of s to {transition effect:push, transition duration:1.5}
		else if mode is "cube" then
			set transition properties of s to {transition effect:cube, transition duration:1.5}
		else if mode is "auto" then
			set transition properties of s to {transition effect:dissolve, transition duration:1.0, automatic transition:true, transition delay:3.0}
		else if mode is "magicmove" then
			set transition properties of s to {transition effect:magic move, transition duration:1.0}
		end if
		save theDoc in outFile
		close theDoc saving no
	end tell
end run
