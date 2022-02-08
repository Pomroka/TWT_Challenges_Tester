# Challenge 73: Tekgar's late | Amogus #3

Alex: "We just started out on our journey, what the hell happened!?"  
Espiobest: "lynx is dead"  
ArKane: "lynx?!"  
Espiobest: "Why are you acting so surprised? You passed right by his body."  
Sarzz: "I met ArKane at the end of the hallway and he appeared to have dozed off."  
Espiobest: "The killer always goes back to the place of the crime."  
Sylte: "When you're dozed off, you don't notice anything that happens around you. Btw where's Tekgar?"  
Tekgar unfortunately has the longest path to take to get to the lobby, hence him being late. On his way there he needs to throw away some trash. In the area of the spaceship where he is currently standing there are a couple parallel hallways with some trashcans at seemingly randomly chosen doors. Help Tekgar figure out how to get rid of his trash the quickest so he can finally get to the meeting.

## Task

You are given a number `T` the number of tests cases. `T` cases follow. For each case you are given a number `D` for the total amount of doors, and on the next line a letter representing which way the lobby is (`L` for left, `R` for right, `U` for up, and `D` for down) and the next two lines arrays of digits representing Tekgar's and the cans' locations (`0` for nothing at the door, `1` for a trashcan, and `2` for Tekgar).  
There will always be two arrays of digits of the exact same length. Figure out the minimum amount of steps (one step is movement from one door to one next to it) needed for Tekgar to get to a trashcan which is preferably on his way to the lobby. To move from one hallway to the other (from one line of digits to the other) Tekgar must first get to the end of the current hallway (line of digits).

### Schematic how this looks (`x` can be `0`, `1` or `2`)
```
  U     U
  ↑     ↑
L←XX...XX→R
  ↕     ↕
L←XX...XX→R
  ↓     ↓
  D     D
```

## Examples

### Input
```
2
6
R
012
000
8
D
1021
0010
```

### Output
```
1
1
```

Challenge suggested by @SnowballSH, changes made based on a suggestion from @class DockerAddict and to better fit the story

## Submissions and grading

- code must be written in python
- `eval`, `exec` and `open` functions are not allowed same goes for `import`

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/PreviousChallenges/Challenge_73)