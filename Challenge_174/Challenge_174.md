# Challenge 174: Dense Number (Part 1)

**Difficulty: 2/10  
Labels: Binary**

Given a positive integer `n`, call a sequence of bits `s` its **normal binary representation** if and only if `s` is the binary representation of `n` and `s` starts with a set bit (1). Basically, no leading zeroes.
Define the density of `s` to be `(# of 1 in s)/(length of s)`. For example, `6 = 0b110` has density 2/3.

You can do the following two operations to `s`:

1. Remove the leading bit of `s`. (`0b110 -> 0b10`)
2. Remove the trailing bit of `s`. (`0b110 -> 0b11`)

For this challenge, determine the minimum number of such operations on `s` needed so that `s` has a density of 1.

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The only line contains an integer `n`.
Output a single integer, the minimum number of such operations needed on the normal binary representation of `n` so that it has a density of 1.

### Examples

#### Input

```rust
6
6
7
29
632
1
81919
```

#### Output

```rust
1
0
2
6
0
3
```

- For test case 4, `632=0b1001111000`. We remove the first 3 and last 3 bits.
- For test case 6, `81919=0b10011111111111111`. We remove the first 3 bits.

### Note

`1 <= T`
`1 <= n <= 10`<sup>`18`</sup>
You should use a 64-bit integer.

### Submissions

Code can be written in any of these languages:

- `Python` 3.11
- `C` (gnu17) / `C++` (c++20) - GCC 12.2
- `Ruby` 3.2
- `Golang` 1.21
- `Java` 19 (Open JDK) - use ****"class Main"!!!****
- `Rust` 1.72
- `C#` 11 (.Net 7.0)
- `JavaScript` ES2023 (Node.js 20.6)

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_174)
