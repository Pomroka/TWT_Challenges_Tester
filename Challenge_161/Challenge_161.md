# # Challenge 161: SnowballSH and Triangles

**Difficulty: 2/10**  
**Labels: Geometry**

SnowballSH has two sticks of known lengths and an infinitely long piece of stick that he can cut to whatever length he desires. How many different triangles of integer side lengths can SnowballSH make, using the two known sticks and another piece of stick cut off from the infinite stick?

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The first line contains two integers, `a` and `b`, separated by a single space. These are the lengths of the first two sticks.

Output a single integer, the number of different triangles that exist with integer side lengths where `a` and `b` are two of them.

### Examples

#### Input

```rust
‌3
5 2
4 4
1943 2023
```

#### Output

```rust
‌3
7
3885
```

- For test case 1, all possible 3rd side lengths are `4`, `5`, `6`. Any other integer would not make a triangle.
- For test case 2, all possible 3rd side lengths are `1`, `2`, ..., `6`, `7`.

### Note

A degenerate triangle does not count as a triangle.

```rust
1 <= T
1 <= a, b <= 10^8
```

### Submissions

Code can be written in any of these languages:

- `Python` 3.10
- `C` (gnu17) / `C++` (c++20) - GCC 11.2
- `Ruby` 3.1
- `Golang` 1.19
- `Java` 19 (Open JDK) - use **"class Main"!!!**
- `Rust` 1.68.2
- `C#` 10 (.Net 6.0)
- `JavaScript` ES2022 (Node.js 18.10)

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_161)
