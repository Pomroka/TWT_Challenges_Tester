# Challenge 102: Tic-Tac-Toe

**Difficulty: 4/10**  
***Demon Slayer: Encountering a Demon, Part 1***  
If I were 5 years old I would scream, instead my mouth stays shut, slightly lump. The creature, no the human, or is it a human, is standing about seven feet tall and feels like it weighs about twice as much as a bodybuilder. Its teeth are showing through a crooked smile in a zigzag pattern, each tooth probably the equivalent of a dagger blade. Its lips have a green-ish mold like look to them in random spots. The hair looks like it hasn’t had a shower in over a month. The eyes are white balls with slit like openings concealing an endless void behind them.

“Never seen a demon before have you?” The creature asked in a shaky croaked voice.
“A- a demon?” The absurdity of the question made me let out a quick laugh that was louder than it needed to be.
“Yes… Yes, this is your first time encountering a demon, I can tell. But then most people never see demons, only when they're about to die.” The monster let out a high pitched amused laughter.
“When they’re about to die?” I asked, perplexed
“Mmm… well… well, enough of this, time to get some breakfast.” The monster didn’t seem to hear my question.

----------

Here we assume you know the rules and winning conditions of Tic-tac-toe (a.k.a. Crosses & Noughts, 3-in-a-row, Xs & Os, etc.). If not, please [read](https://en.wikipedia.org/wiki/Tic-tac-toe) and learn to play it before you try this challenge.

## Task

You are given a number `T` and `T` testcases follow, for each testcase,
You are given three lines, each consisting of three characters, one of `O`, `X`, `#`, as the current `3x3` Tic-Tac-Toe board. Each `O` means an `O` piece is placed at this location and each `X` means an `X` piece is at this location, while a `#` means this location is empty.
For each testcase (each contains a board), if player `X` moves now, output `O` if player `O` has a forced win, `X` if player `X` has a forced win, and `D` if the game is a draw (tie) with perfect play.

### Examples

#### Input

```rs
4
XX#
#OO
OXO
OO#
XOX
#X#
#OX
#X#
OXO
###
###
###
```

#### Output

```rs
X
O
D
D
```

#### Explanation

Test case 1 is a win for `X` because `X` plays top right, 3-in-a-row.
Test case 2 is a win for `O` because no matter which square `X` plays, `O` can win by playing top right or bottom left, whichever is empty.
Test case 3 is a draw with perfect play.
Test case 4 is the starting position, and is proven to be a draw with perfect play.

### Notes

`1 ≤ T`
`O` is the English alphabet `O`, not zero (`0`).
It is not guaranteed that the board can be created by only playing legal moves from an empty board.
The board will not contain 3-in-a-row already (a.k.a. the game is guaranteed to be ongoing).
The board will not be full.

### Submissions

Code can be written in any of these languages:

- `Python` 3.10
- `C/C++` (GCC 10.3)
- `Ruby` 3.1
- `Golang` 1.18
- `Java` 18 (Open JDK) - use **"class Main"**!!!
- `Rust` 1.60
- `C#` 10 (.Net 6.0)

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/PreviousChallenges/Challenge_102)
