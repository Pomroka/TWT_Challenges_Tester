# Challenge 184: Trib3

**Difficulty: 2/10  
Labels: Implementation**

Let `T(n)` denote the `n`<sup>`th`</sup> tribonacci number, defined by `T(0) = 0, T(1) = T(2) = 1` and `T(n) = T(n-3) + T(n-2) + T(n-1) for all n >= 3`. (In other words, each term is the sum of the previous three terms)
For example, the first few tribonacci numbers are 0, 1, 1, 2, 4, 7, 13, 24, 44, 81, ...

Let `S(n)` denote the sum of the **cubes** of the first n tribonacci numbers. In other words, `S(n) = T(1)^3 + T(2)^3 + T(3)^3 + ... + T(n)^3`.
For example, `S(5) = 1^3 + 1^3 + 2^3 + 4^3 + 7^3 = 417`.

Given `n`, please compute `S(n)`. Since `S(n)` grows quickly, output the remainder when `S(n)` is divided by `10^9 + 7`.

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The only line contains an integer `n`.

Output `S(n) mod 10`<sup>`9`</sup>` + 7`.

### Examples

#### Input

```rust
8
1
2
3
5
8
1000
2023
12716
```

#### Output

```rust
‌1
2
10
417
101622
372248459
579756235
206575602
```

### Note

- `1 <= T`
- `1 <= n <= 10`<sup>`6`</sup>
- For test case 6, the answer is more than 1500 digits long, so we take its remainder when divided by 10<sup>9</sup> + 7.
- Fun fact: Only 130 of the answers in the given constraints are palindromes. Test case 8 is one of them.

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

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/PreviousChallenges/tree/main/Challenge_184)
