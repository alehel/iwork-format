-- Experiment 0196: save a Keynote presentation with one slide per transition effect.
-- Usage: osascript recipes/0196-keynote-all-transitions.applescript /absolute/path/doc.key
-- Slide N gets effect N of the list below, and its title is the effect's AppleScript name.
-- The folder must exist. Keynote opens while the recipe runs.

on run argv
	set outFile to POSIX file (item 1 of argv)
	tell application "Keynote"
		set effects to {shimmer, sparkle, swing, object cube, object flip, object pop, object push, object revolve, object zoom, perspective, clothesline, confetti, drop, droplet, fade through color, grid, iris, reveal, switch, wipe, blinds, color planes, doorway, fall, flip, flop, mosaic, page flip, pivot, reflection, revolving door, scale, swap, swoosh, twirl, twist, fade and move, radial wipe}
		set names to {"shimmer", "sparkle", "swing", "object cube", "object flip", "object pop", "object push", "object revolve", "object zoom", "perspective", "clothesline", "confetti", "drop", "droplet", "fade through color", "grid", "iris", "reveal", "switch", "wipe", "blinds", "color planes", "doorway", "fall", "flip", "flop", "mosaic", "page flip", "pivot", "reflection", "revolving door", "scale", "swap", "swoosh", "twirl", "twist", "fade and move", "radial wipe"}
		set theDoc to my newKeynote()
		repeat with i from 1 to count of effects
			if i > 1 then make new slide at end of slides of theDoc
			set s to slide i of theDoc
			set object text of default title item of s to item i of names
			set transition properties of s to {transition effect:item i of effects}
		end repeat
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
