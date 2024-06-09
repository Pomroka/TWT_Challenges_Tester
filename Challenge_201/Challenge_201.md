# Challenge 201: Bit-reversed Integers

**Difficulty: 2/10  
Labels: Binary, Strings**

Let `f(n)` denote the bit-reversed 8-bit binary number of `n`. This sequence is found in computer programs that need to reverse the bits in a byte, typically during data compression or other bit-level encoding. `f(n)` is computed by taking the 8-bit binary representation of the base 10 integer `n`, reversing the eight digits, and then converting it back to base 10 representation.
For example, `f(29) = 184` because `29=00011101` would turn into `10111000=184`.

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The only line contains an integer `n`.

Output a single integer, the base-10 representation of `f(n)`, the bit-reversed 8-bit binary number of `n`.

### Examples

#### Input

```rust
11
0
1
2
3
4
5
29
184
200
128
255
```

#### Output

```rust
0
‌128
64
192
32
160
184
29
19
1
255
```

### Note

- `1 <= T`
- `0 <= n <= 255`

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

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_201)
