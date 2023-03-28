# Challenge 150: SnowballSH and cows

**Difficulty: 7/10  
Labels: DSU, Greedy**

Don't freak out, this one is not too hard, and next week's challenge will be easy :)

SnowballSH is mad at Farmer John because John's issues made him fail the last USACO contest. Therefore, he summons Farmer Nhoj to kick John out of his farm.
Farmer John and Farmer Nhoj plays a game. There are `N` cows on the farm, labelled `1`, `2`, ... `N`. For each move, a player can tie two cows together. However, the move "fails" if the two cows are already connected. We define cows `A` and `B` are "connected" if cow `A` is tied to cow `B`, or if cow `A` and `B` are both connected to cow `C`. If a move does not fail, the action is taken and the player gets `1` point.
Farmer John and Farmer Nhoj play this game for `M` rounds. Farmer John moves first. Since SnowballSH hates John, he told Nhoj all of John's strategies, so Nhoj knows every move John is going to make.
Compute the maximum difference between the scores of Farmer Nhoj and Farmer John. That is, the maximum value of (Nhoj - John).

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The first line contains two integers, `N` and `M`.
- `M` lines follow. The `i`th line contains two integers `A`<sub>`i`</sub> and `B`<sub>`i`</sub>. This means for John's `i`<sup>th</sup> move, he attempts to connect cows `A`<sub>`i`</sub> and `B`<sub>`i`</sub>, no matter what Nhoj does.

Output a single integer, the maximum value of (Nhoj - John), where Nhoj is Nhoj's score and John is John's score.

### Examples

#### Input

```rust
5
5 3
1 2
2 3
3 4
10 2
1 7
2 8
2 1
1 2
5 3
3 5
1 3
1 5
4 3
1 2
2 3
3 4
```

#### Output

```rust
2
1
-1
2
1
```

For the first test case, there are `4` cows and `3` turns.
First, John ties cows `1` and `2`, obtaining `1` point. There are several optimal moves. For example, Nhoj can connect cows `1` and `3`, obtaining `1` point. John's next move will fail because `1`, `2`, `3` are connected. Then, Nhoj should connect cow `4` with any other cow, obtaining a second point. John's 3rd move also fails. Finally, Nhoj can connect cow `5` with any other cow, obtaining `3 - 1 = 2`.
For the second test case, since Nhoj cannot stop John from succeeding both moves, the answer is 0.
For the third test case, John obtains one point on the first move, but Nhoj cannot obtain a single point, so the answer is `0 - 1 = -1`.
For the fourth test case, the moves `[(1, 3), (2, 4), (4, 5)]` is one example of optimal strategy.

### Note

- `1 <= T`
- `2 <= N <= 1,000`
- `1 <= M <= 500`
- `1 <= A`<sub>`i`</sub>` < B`<sub>`i`</sub>` <= N`
- `(A`<sub>`i`</sub>`, B`<sub>`i`</sub>`) != (A`<sub>`j`</sub>`, B`<sub>`j`</sub>`) for all i != j`

### Submissions

Code can be written in any of these languages:

- `Python` 3.10
- `C` (gnu17) / `C++` (c++20) - GCC 11.2
- `Ruby` 3.1
- `Golang` 1.19
- `Java` 19 (Open JDK) - use **"class Main"!!!**
- `Rust` 1.64
- `C#` 10 (.Net 6.0)
- `JavaScript` ES2022 (Node.js 18.10)

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_150)
