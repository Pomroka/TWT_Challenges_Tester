# Challenge 141: Illegal number

**Difficulty: 2/10  
Labels: For loop**

SnowballSH is studying algebra, but he is struggling with number bases. Can you help him out?

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The first line contains a number `B`.
- The second line contains a string `S` consisting of characters `0-9`.

Is `S` a valid number in base `B`? If it is, output `YES`. Otherwise, output `NO`.

### Examples

#### Input

```rust
5
10
123210
6
0033250144
6
4256
1
00
3
8
```

#### Output

```rust
YES
YES
NO
YES
NO
```

For test case 1, `123210` is a valid number in base `10`, as all digits are less than `10`.
For test case 3, `4256` is not a valid number in base `6`, as it contains the digit `6`.
For test case 5, `8` is not a valid number in base `3`, as it contains the digit `8`.

### Note

`1 <= T`
`1 <= B <= 10`
`1 <= length of S <= 10`<sup>`5`</sup>
Each character in `S` is one of the digits `0-9`.
Leading **zeroes** are **valid**

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

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_141)
