# Challenge 195: Quasi-multiples, Part 1

**Difficulty: 1/10  
Labels: Implementation**

This is the first problem in our exploration of simple modular arithmetic.

Call a positive integer `N` a **quasi-multiple** of positive integer `m` if the remainder when `N` is divided by `m` is either 1 or `m-1`. For example, `28` is a quasi-multiple of `9` and `23` is a quasi-multiple of `8`, but `30` is not a quasi-multiple of `5`.

Given positive integers `N` and `m`, determine if `N` is a quasi-multiple of `m`.

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The only line contains two integers `N` and `m`, separated by a single space.

Output `YES` if `N` is a quasi-multiple of `m`, or `NO` otherwise.

### Examples

#### Input

```rust
6
1 2024
6071 2024
37 13
113 7
10 100
12345 823
```

#### Output

```rust
‌YES
YES
NO
YES
NO
NO
```

- For test case 1, the remainder when `1` is divided by `2024` is `1`.
- For test case 2, the remainder when `6071` is divided by `2024` is `2023`.
- For test case 3, the remainder when `37` is divided by `13` is `11`, not equal to 1 or 12.

### Note

`1 <= T`
`1 <= N <= 10`<sup>`9`</sup>
`2 <= m <= 10`<sup>`9`</sup>

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

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_195)
