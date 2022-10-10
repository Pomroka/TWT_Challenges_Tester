# Challenge 127: Dice Combinations

**Difficulty: 4/10
Labels: Knapsack DP or Queue or Matrix**

Tim was delivered a magical box containing dices of various kinds. Since the dice sides are uncommon, he is wondering how many ways there are to achieve his favourite numbers using these dices. Can you help him out?

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The first line contains two integers, `N` and `D`, separated by a single space.

Assuming Tim has unlimited amount of fair dices with `D` sides labelled as `1, 2, ... D` (for example, when `D = 5`, Tim has 5-sided dices with sides labelled `1, 2, 3, 4, 5`), and `N` is his favourite number.

Output the number of ways to construct sum `N` by throwing a `D`-sided dice one or more times, modulo (`10`<sup>`9`</sup>` + 7`).

For example, if `N = 3` and `D = 6` (a regular 6-sided dice), there are 4 ways to sum to 3 with numbers within `[1, 6]`:
`1 + 1 + 1`, `1 + 2`, `2 + 1`, `3`

Another example, if `N = 4` and `D = 2`, there are `5` ways to sum to `4` with numbers within `[1, 2]`:
`1 + 1 + 1 + 1`, `1 + 1 + 2`, `1 + 2 + 1`, `2 + 1 + 1`, `2 + 2`

### Examples

#### Input

```rust
5
3 6
6 2
10 7
123 10
1234 31
```

#### Output

```rust
4
13
504
795630471
247902534
```

For test cases `4` and `5`, the actual results are very large, so we print the result modulo by (`10`<sup>`9`</sup>` + 7`).

### Note

`1 <= T`
`1 <= N <= 10`<sup>`5`</sup>
`2 <= D <= 10`<sup>`3`</sup>
`2 <= N * D <= 10`<sup>`6`</sup>
Suggested Time Complexity: `O(N * D)` or `O(N)`

Hint from SnowballSH: Search up "Knapsack DP" if you don't know what it is.

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

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_127)
