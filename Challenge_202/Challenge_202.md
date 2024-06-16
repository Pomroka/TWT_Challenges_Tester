# Challenge 202: Sibling Numbers

**Difficulty: 4/10  
Labels: Bits**

Define the "older sibling" of an integer `n` as the first integer greater than `n` that has the same number of `1` digits as `n` when written in binary. For example, the older sibling of `3=0b11` is `5=0b101` because 5 is the first integer after 3 that also has two `1` digits. Can you find the older sibling of any given number?

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The only line contains an integer `n`.

Output a single integer, the older sibling of `n`. If `n` has no older siblings, output `-1`.

### Examples

#### Input

```rust
12
0
1
2
3
4
5
23
63
128
2024
2028
4398046511103
```

#### Output

```rust
-1
2
4
5
8
6
27
95
256
2032
2033
6597069766655
```

### Note

- `1 <= T`
- `0 <= n <= 10`<sup>`16`</sup>
- You should use a 64-bit integer.

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

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_202)
