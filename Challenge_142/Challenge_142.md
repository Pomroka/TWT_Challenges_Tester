# Challenge 142: Bridges

**Difficulty: 3/10  
Labels: Graph Theory, Connected Components**

The king wants to build bridges to connect his `N` villages. Bridges are both-way. The king, however, wants to spend as little money as possible, but also making sure that even if any `K` bridges break, one can still travel from any village to any other village. Find the minimum number of bridges the king needs to build.

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The first line contains two integers, `N` and `K`.

Output one integer, the minimum number of bridges needed to connect `N` villages such that the villages are connected after any choice of `K` bridges break. That is, no matter which `K` bridges are removed, one can still travel from one village to any other village.

### Examples

#### Input

```rust
6
4 0
4 1
6 2
520 0
2023 2
2023 12
```

#### Output

```rust
3
4
9
519
3035
13150
```

For test case 1, `3` **bridges** are required to connected `4` **villages**.
For test case 3, we can build a connected village network such that each **village** is connected to `3` **bridges**. This way no matter which `2` **bridges** are broken, each **village** is still connected to the main network in at least `1` way. This can be done with minimum `9` **bridges**.

### Note

`1 <= T`
`1 <= N <= 10`<sup>`6`</sup>
`0 <= K <= N`
`N * K <= 10`<sup>`9`</sup>
Problem inspired by the 2023 Chicago Area All Star Math Team Tryouts (#7, N=2023 K=2)

### Submissions

Code can be written in any of these languages:

- `Python` 3.10
- `C` (gnu17) / `C++` (c++20) - GCC 11.2
- `Ruby` 3.1
- `Golang` 1.19
- `Java` 19 (Open JDK) - use "class Main"!!!
- `Rust` 1.64
- `C#` 10 (.Net 6.0)
- `JavaScript` ES2022 (Node.js 18.10)

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_142)
