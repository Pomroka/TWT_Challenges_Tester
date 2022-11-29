# Challenge 134: Diagonals

**Difficulty: 1/10
Labels: Brute-force or Binary Search**

Alex loved counting diagonals in a polygon. However, this time he wanted to do the inverse. He chose a random integer, and tried to find the polygon with the least sides that has at least that many diagonals. Can you help him out?

**Hint:** it can be shown (via simple combinatorics) that **for any polygon with `x` sides `(x >= 3)`, it has exactly `x * (x - 3) / 2` diagonals**. For example, a Hexagon (6 sides) has `6 * (6 - 3) / 2 = 9` diagonals.

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The first line contains an integer `N`.

Output the minimum number of sides a polygon must have, so it has at least `N` diagonals.

### Examples

#### Input

```rust
5
1
2
4
2022
124250
```

#### Output

```rust
4
4
5
66
500
```

For test case `1`, a triangle (`3` sides) has `0` diagonals. A rectangle (`4` sides) has `2` diagonals `>= 1`, so output `4` for rectangle.
For test case `3`, a rectangle has `2` diagonals, but a pentagon (`5` sides) has `5` diagonals. A pentagon is the first polygon to have at least `4` diagonals.
For test case `4`, a polygon with `65` sides has only `2015` diagonals, while a polygon with `66` sides has `2079` diagonals, the minimum to have is at least `2022`.

### Note

`1 <= T`
`1 <= N <= 10`<sup>`6`</sup>

Recommended Time complexity is `O(log N)` for educational purposes. However, correct `O(N)` and **math** solutions will also be accepted and will pass.
Want extra challenge? Write solutions for each of the above time complexities.

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

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_134)
