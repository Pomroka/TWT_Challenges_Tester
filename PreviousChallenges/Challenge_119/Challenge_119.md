# Challenge 119: Lazy Rock Paper Scissors

**Difficulty: 3/10**  
Tim just asked you if you wanted to play `N` rounds of Rock-Paper-Scissors with him, and you agreed. However, you are busy doing your math homework. You decided that you will just play the same move in all `N` rounds, so you don't have to think about the game.
You know a lot about Tim, so much that you can predict all of his `N` moves before the game even started.

You still want to beat Tim, so you need to pick the move that wins the most games based on your predictions.
For the purpose of this challenge, you **don't need to care about minimizing the #[^1] of losses**. Only wins matter to you.

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The first line contains a number `N`, the # of rounds you will play with Tim.
- The next line contains `N` letters, `R`, `P`, or `S`, each representing your prediction of Tim's move for each round.

Output `M`, where `M` is the best move to make.
If multiple best moves exist, output the first one in the order `RPS`. For example, the paper and scissors are equally good and rock is worse, output P.

### Examples

#### Input

```rust
4
3
PPR
5
RPSRP
7
SPSPSPS
21
PRPPSRPRSPRRSSPSSSSPR
```

#### Output

```rust
S
P
R
R
```

- For test case `1`, Tim will play two papers and one rock. If you play scissors all the time, you will win twice, which is the best you can get.
- For test case `2`, although playing Paper and Scissors are equally good, `P` is before `S` in the order `RPS`, therefore output `P`.

#### Note

`R` beats `S`, `S` beats `P`, `P` beats `R`.
`1 <= T`
`1 <= N <= 10^6`
The second line of each test case only contains `R`, `P`, or `S`.

### Submissions

Code can be written in any of these languages:

- `Python` 3.10
- `C/C++` (GCC 10.3)
- `Ruby` 3.1
- `Golang` 1.18
- `Java` 18 (Open JDK) - use "class Main"!!!
- `Rust` 1.62
- `C#` 10 (.Net 6.0)
- `JavaScript` ES2022 (Node.js 18.2)

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/PreviousChallenges/Challenge_119)

[^1] number
