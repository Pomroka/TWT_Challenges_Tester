# Challenge 181: Minimum Knight Moves

**Difficulty: 3/10  
Labels: BFS**

A wooden plank is on fire! Snowy, a horse made out of snow, needs to reach the plank as soon as possible to put out the fire. Unfortunately, as a horse, Snowy can only perform horsey moves like a knight on a chessboard in the game of chess. More unfortunately, Snowy is restricted to a square chessboard.
Find the minimum number of moves needed for Snowy to reach the fire-plank.

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The only line contains five integers, `n x`<sub>`1`</sub>` y`<sub>`1`</sub>` x`<sub>`2`</sub>` y`<sub>`2`</sub>. On a `n by n` chessboard, Snowy is at `(x`<sub>`1`</sub>`, y`<sub>`1`</sub>`)` and the fire-plank is at `(x`<sub>`2`</sub>`, y`<sub>`2`</sub>`)`.

If Snowy is subject to knight moves and cannot move outside the board, find the minimum number of moves Snowy needs to reach the fire-plank.

A knight move is to move two squares in one direction (up, down, left, or right), and then moves one square in a direction perpendicular to the 2-square move.

Note that the lower-left corner of the board is `(0, 0)` and the upper-right corner of the board is `(n-1, n-1)`.

### Examples

#### Input

```rust
‌6
5 0 0 4 4
10 9 0 0 9
6 1 1 4 5
10 8 9 2 3
1 0 0 0 0
2023 2022 2022 0 0
```

#### Output

```rust
‌4
6
3
4
0
1348
```

For test case 1, an optimal path would be `(0, 0) -> (2, 1) -> (1, 3) -> (3, 2) -> (4, 4)`.

### Note

- `1 <= T`
- `1 <= n <= 2023`
- `0 <= x`<sub>`1`</sub>`, y`<sub>`1`</sub>`, x`<sub>`2`</sub>`, y`<sub>`2`</sub>` < n`
- **It is guaranteed that a path exists.**
- To math people: I have no idea if this can be solved with number theory but feel free to try (but be aware of not going outside of the board).

### Submissions

Code can be written in any of these languages:

- `Python` 3.11
- `C` (gnu17) / `C++` (c++20) - GCC 12.2
- `Ruby` 3.2
- `Golang` 1.21
- `Java` 19 (Open JDK) - use **"class Main"!!!**
- `Rust` 1.72
- `C#` 11 (.Net 7.0)
- `JavaScript` ES2023 (Node.js 20.6)

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_181)
