# Challenge 175: Dense Number (Part 2)

**Difficulty: 4/10  
Labels: Binary, Permutations, Dynamic Programming, Ripple Carry**

Given a positive integer `n`, call `m` a **bit subset** of `n` if, when the binary representations of `n` and `m` are right-aligned, for every unset bit (`0`) in `n`, the corresponding bit in `m` is also unset (`0`). Note that **`0` is a bit subset of any integer**.

In other words, `m` is a bit subset of `n` if you can obtain `m` by changing any combination (possibly none or all) of `1`s in `n` to `0`.

For example, `10=0b1010` is a bit subset of `27=0b11011`, but `4=0b100` is not (the third bit from the right should be `0`).

Given another positive integer `p`, please find the number of bit subsets of `n` that is divisible by `p`. Consider `0` to be divisible by any positive integer.

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The first line contains two integers, `n` and `p`.

Output a single integer, the number of bit subsets of `n` that is a multiple of `p`.

### Examples

#### Input

```rust
6
27 3
1 1
3 2
4 5
2023 13
160842843834660 7
```

#### Output

```rust
6
2
2
1
39
11561
```

For test case 1, all `2^4=16` subsets of `27=0b11011` are `0,1,2,3,8,9,10,11,16,17,18,19,24,25,26,27`. Out of these 16 numbers, 6 of them are multiplies of `3`.
For test case 4, the only two subsets of 4 are 0 and 4. Only 0 is a multiple of `5`.

### Note

`1 <= T`
`1 <= n <= 10`<sup>`18`</sup>
`1 <= p <= 10`<sup>`18`</sup>
It is guaranteed that `n` contains **at most 20 set bits**.

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

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_175)
