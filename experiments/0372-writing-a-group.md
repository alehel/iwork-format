# 0372: Writing a group's position and a member's offset

**Status:** run

A group is a type-3008 drawable that lists its members in field 2. Each member names the group in its field 1.2 and is positioned relative to the group's top-left corner ([0216](0216-group.md)). AppleScript's `group` class lists a group's items with their positions on the page. This experiment moves the group, then moves one member within it, and reads the positions back from Pages.

## Setup

| | |
| --- | --- |
| Pages | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-17 |
| Input | `samples/0216/group.pages`: two 100 × 100 shapes, grouped. The group (1732829) is at 300, 300 and 250 × 100; the members 1732821 and 1732823 are at 0, 0 and 150, 0 within it |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py); read back with the new [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) |

## Recipe

```bash
mkdir -p samples/0372
R=recipes/0302-set-path.py
G=samples/0216/group.pages
python3 -I $R $G samples/0372/group-moved.pages 1732829 1.1.1.1 float 100 1.1.1.2 float 400
python3 -I $R $G samples/0372/member.pages 1732823 1.1.1.1.1 float 50 1.1.1.1.2 float 60
sh recipes/0372-in-app.sh Pages samples/0372/member.pages 'set out to {}
repeat with g in groups of d
  set end of out to {position of g, width of g, height of g}
  repeat with i in iWork items of g
    set end of out to position of i
  end repeat
end repeat
return out'
```

`recipes/0372-in-app.sh` opens a document through Launch Services, runs the given AppleScript with `d` set to that document, and closes it without saving. The group's geometry is in its payload's field 1.1, but a shape's drawable sits one level deeper, so a member's position is at 1.1.1.1.

## Observation

| File | Written | Group (position, size) | Members on the page |
| --- | --- | --- | --- |
| `group.pages` | nothing | 300, 300; 250 × 100 | 300, 300 and 450, 300 |
| `group-moved.pages` | group 1.1.1 = 100, 400 | 100, 400; 250 × 100 | 100, 400 and 250, 400 |
| `member.pages` | second member 1.1.1 = 50, 60 | 300, 300; 150 × 160 | 300, 300 and 350, 360 |

In both written files Pages still shows one item on the page, the group.

## Conclusion

A member's position is an offset from the group's corner: moving the group moves both members with it, and the member written at 50, 60 is drawn at 300 + 50, 300 + 60. The group's size isn't taken from the file as written: after the member moved, Pages gave the group the box around its members, 150 × 160, though field 1.1.2 still said 250 × 100. A writer should still keep the group's box in step with its members.

## Confidence

*Confirmed*: a group's position, and its members' positions relative to it, by writing them.
