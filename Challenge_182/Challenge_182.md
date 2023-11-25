# Challenge 182: Simple Game

**Difficulty: 2/10  
Labels: Game Theory, Greedy**

Yan and Tim are playing a game on a sequence `a`<sub>`1`</sub>`, a`<sub>`2`</sub>`, …, a`<sub>`n`</sub> of length `n`. They move in turns and Yan moves first.

In the turn of each player, he or she should select an integer and remove it from the sequence. The game ends when there is no integer left in the sequence.

Yan wins if the sum of her selected integers is **even**; otherwise, Tim wins.

Determine who will win the game, if both players play optimally.

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The first line contains an integer `n`.
- The second line contains `n` integers, separated by single spaces, the sequence `a`.

Output `Yan` or `Tim`, whoever will win the game, if both players play optimally.

### Examples

#### Input

```rust
‌4
3
1 3 5
4
1 3 5 7
4
1 2 3 4
4
10 -20 -30 40
```

#### Output

```rust
‌Yan
Yan
Tim
Yan
```

- For testcase 1, any legal sequence of moves results in a win for Yan.
- For testcase 3, if Yan picks an even number, then Tim will pick the other even number, and Yan cannot get an even sum. If Yan picks an odd number, then Tim will pick the other odd number, and Yan still cannot get an even sum. Therefore, Tim wins.

### Note

`1 <= T`
`1 <= n <= 10`<sup>`5`</sup>
`-10`<sup>`9`</sup>` <= a`<sub>`i`</sub>` <= 10`<sup>`9`</sup>
Source: Codeforces

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

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_182)
