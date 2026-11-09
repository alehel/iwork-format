-- Experiments 0079-0086: save a Keynote presentation with a 2 x 3 chart of a given type and grouping.
-- Usage: osascript recipes/0079-keynote-chart-type.applescript /absolute/path/doc.key type row|column
-- type is one of Keynote's legacy chart types, such as pie_2d or line_2d. The data is as in 0067:
-- rows "r1", "r2"; columns "a", "b", "c"; values {1, 2, 3} and {4, 5, 6}. The folder must exist.

on run argv
	if (count of argv) is not 3 then error "usage: osascript 0079-keynote-chart-type.applescript doc.key type row|column"
	set outFile to POSIX file (item 1 of argv)
	set chartType to item 2 of argv
	set grouping to item 3 of argv
	set rn to {"r1", "r2"}
	set cn to {"a", "b", "c"}
	set dt to {{1, 2, 3}, {4, 5, 6}}
	tell application "Keynote"
		set theDoc to make new document
		set s to slide 1 of theDoc
		if chartType is "pie_2d" then
			if grouping is "row" then
				add chart s row names rn column names cn data dt type pie_2d group by chart row
			else
				add chart s row names rn column names cn data dt type pie_2d group by chart column
			end if
		else if chartType is "vertical_bar_2d" then
			if grouping is "row" then
				add chart s row names rn column names cn data dt type vertical_bar_2d group by chart row
			else
				add chart s row names rn column names cn data dt type vertical_bar_2d group by chart column
			end if
		else if chartType is "stacked_vertical_bar_2d" then
			if grouping is "row" then
				add chart s row names rn column names cn data dt type stacked_vertical_bar_2d group by chart row
			else
				add chart s row names rn column names cn data dt type stacked_vertical_bar_2d group by chart column
			end if
		else if chartType is "horizontal_bar_2d" then
			if grouping is "row" then
				add chart s row names rn column names cn data dt type horizontal_bar_2d group by chart row
			else
				add chart s row names rn column names cn data dt type horizontal_bar_2d group by chart column
			end if
		else if chartType is "stacked_horizontal_bar_2d" then
			if grouping is "row" then
				add chart s row names rn column names cn data dt type stacked_horizontal_bar_2d group by chart row
			else
				add chart s row names rn column names cn data dt type stacked_horizontal_bar_2d group by chart column
			end if
		else if chartType is "pie_3d" then
			if grouping is "row" then
				add chart s row names rn column names cn data dt type pie_3d group by chart row
			else
				add chart s row names rn column names cn data dt type pie_3d group by chart column
			end if
		else if chartType is "vertical_bar_3d" then
			if grouping is "row" then
				add chart s row names rn column names cn data dt type vertical_bar_3d group by chart row
			else
				add chart s row names rn column names cn data dt type vertical_bar_3d group by chart column
			end if
		else if chartType is "stacked_vertical_bar_3d" then
			if grouping is "row" then
				add chart s row names rn column names cn data dt type stacked_vertical_bar_3d group by chart row
			else
				add chart s row names rn column names cn data dt type stacked_vertical_bar_3d group by chart column
			end if
		else if chartType is "horizontal_bar_3d" then
			if grouping is "row" then
				add chart s row names rn column names cn data dt type horizontal_bar_3d group by chart row
			else
				add chart s row names rn column names cn data dt type horizontal_bar_3d group by chart column
			end if
		else if chartType is "stacked_horizontal_bar_3d" then
			if grouping is "row" then
				add chart s row names rn column names cn data dt type stacked_horizontal_bar_3d group by chart row
			else
				add chart s row names rn column names cn data dt type stacked_horizontal_bar_3d group by chart column
			end if
		else if chartType is "area_2d" then
			if grouping is "row" then
				add chart s row names rn column names cn data dt type area_2d group by chart row
			else
				add chart s row names rn column names cn data dt type area_2d group by chart column
			end if
		else if chartType is "stacked_area_2d" then
			if grouping is "row" then
				add chart s row names rn column names cn data dt type stacked_area_2d group by chart row
			else
				add chart s row names rn column names cn data dt type stacked_area_2d group by chart column
			end if
		else if chartType is "line_2d" then
			if grouping is "row" then
				add chart s row names rn column names cn data dt type line_2d group by chart row
			else
				add chart s row names rn column names cn data dt type line_2d group by chart column
			end if
		else if chartType is "line_3d" then
			if grouping is "row" then
				add chart s row names rn column names cn data dt type line_3d group by chart row
			else
				add chart s row names rn column names cn data dt type line_3d group by chart column
			end if
		else if chartType is "area_3d" then
			if grouping is "row" then
				add chart s row names rn column names cn data dt type area_3d group by chart row
			else
				add chart s row names rn column names cn data dt type area_3d group by chart column
			end if
		else if chartType is "stacked_area_3d" then
			if grouping is "row" then
				add chart s row names rn column names cn data dt type stacked_area_3d group by chart row
			else
				add chart s row names rn column names cn data dt type stacked_area_3d group by chart column
			end if
		else if chartType is "scatterplot_2d" then
			if grouping is "row" then
				add chart s row names rn column names cn data dt type scatterplot_2d group by chart row
			else
				add chart s row names rn column names cn data dt type scatterplot_2d group by chart column
			end if
		else
			error "unknown chart type " & chartType
		end if
		save theDoc in outFile
		close theDoc saving no
	end tell
end run
