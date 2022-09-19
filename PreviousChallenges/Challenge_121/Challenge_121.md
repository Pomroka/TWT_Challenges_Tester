# Challenge 121: Race to N

**Difficulty: 5/10**  
**Labels: Backward Induction**

Sylte and Tim are playing a number game. The rule is as follows:
Given three numbers `M`, `N`, and `S` for the entire game:
Alternating turns, a player picks a number in the range `[1, M]`. Call the number picked `x`. After the pick, set `S` to `S + x`. If this player made `S` equal to `N`, the player wins.

## Example game:

`M = 6, N = 20, S = 0`
Sylte picks `x = 4 => S = 4`
Tim picks `x = 2 => S = 6`
Sylte picks `x = 6 => S = 12`
Tim picks `x = 1 => S = 13`
Sylte picks `x = 2 => S = 15`
Tim picks `x = 5 => S = 20 = N`, Tim wins the game.

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The first line contains three integers separated by a single space, `M`, `N`, and `S`.

In a game of `M`, `N`, and `S` described above, determine whether the player who moves now has a forced win. Forced win means after player makes the winning move, for any sequence of responses by the opponent, this player always has a way to win.

If the current player has a forced win, print the move he needs to make. Otherwise, print `0`.

It can be proven that at any constrained game state, there exists at most `1` move to force a win, and that if a player doesn't have a forced win, his opponent does.

### Examples

#### Input

```rust
6
6 20 0
6 20 13
1 1 0
1 3 1
9375 8351083625 86697
12345 54321 20000
```

#### Output

```rust
6
0
1
0
0
9629
```

For test case `1`, In the example game, Sylte could have won by picking `x=6` instead.
For test case `2`, no matter which `x` in `[1, 6]` you choose, opponent can match to `20`.

### Constraints

`1 <= T`
`1 <= M <= N <= 10^16`
`0 <= S < N`

### Submissions

Code can be written in any of these languages:

- `Python` 3.10
- `C/C++` (GCC 10.3)
- `Ruby` 3.1
- `Golang` 1.18
- `Java` 18 (Open JDK) - use **"class Main"!!!**
- `Rust` 1.62
- `C#` 10 (.Net 6.0)
- `JavaScript` ES2022 (Node.js 18.2)

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/PreviousChallenges/Challenge_121)
