# Challenge 176: Differentiation or Ternary Search?

**Difficulty: 4/10  
Labels: Ternary Search (No math)**

Tired of reading long problem statements from the last few challenges? We understand, so:
Given three integers `a`, `b`, and `c`,
Let `f(x) = ax^2 + bx + c`, a standard quadratic function. Let `g(x) = f(x) / sin(x)` **where 0 < x < π/2**.
Find the minimum value of `g(x)` over its domain, **rounded to five decimal places** (for example, 5.8834963 is rounded to 5.88350). Please output trailing zeroes, so there are exactly 5 digits after the decimal point.

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The only line contains three integers, `a`, `b`, and `c`, separated by single spaces.

Output a number with exactly 5 decimal places, the minimum of `g(x)` where `0 < x < π/2` rounded to 5 decimal places.

### Examples

#### Input

```rust
6
1 1 1
2 3 4
1 10 2
7 4 9
20 13 23
25 25 17
```

#### Output

```rust
3.39251
10.62136
14.72983
23.23014
64.40302
72.39490
```

Explanation: <https://www.desmos.com/calculator/llanicyi5q>

### Note

`1 <= T`
`1 <= a, b, c <= 25`
It can be shown that for the given constraints, there exists a unique answer, and `3 < answer < 85`.
Please, do not ruin your day by finding the derivative and solving `dg/dx = 0`.

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

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_176)
