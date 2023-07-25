# Challenge 167: Baby Palindromes

**Difficulty: 3/10  
Labels: Implementation**

A **Palindromic Integer** is a positive integer without leading zeroes in base 10 that reads the same forwards as backwards. For example, `0`, `121`, and `88` are Palindromic Integers, while `10` and `1231` are not.

Given an integer `m > 1`, a Palindromic Integer `p` is said to have a **Baby Palindrome** for `m` if `floor(p / m)` is also a Palindromic Integer. For example, if `m = 7`, the Palindromic Integer 63836 has a Baby Palindrome because `floor(63836 / 7) = 9119` is also a Palindromic Integer. (Note that `floor(x)` outputs the largest integer less than or equal to x.)

You are given a range `[a, b]` and an integer `m`. Output the number of Palindromic Integers `p` where `a <= p <= b` such that `p` has a Baby Palindrome for `m`.

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The only line contains three integers, `a`, `b`, and `m`, separated by single spaces.

Output a single integer, the number of Palindromic Integers in `[a, b]` that have a Baby Palindrome for `m`.

### Examples

#### Input

```rust
5
1 20 3
106 595 6
23 724 11
535 535 3
2023 54321 19
```

#### Output

```rust
‌10
4
17
0
25
```

- For test case 1, the valid integers are all palindromes in the range, `1, 2, ..., 9, 11`, since dividing them by 3 always yields a single digit.
- For test case 2, the 4 valid pairs are `202->33, 333->55, 464->77, 595->99`.
- For test case 4, although 535 is a palindromic integer, floor(535/3)=178 is not.

### Note

`1 <= T`
`1 <= a <= b <= 10`<sup>`5`</sup>
`2 <= m <= max(2, b)`

#### Extra challenge (won't be tested)

`1 <= a <= b <= 10`<sup>`9`</sup>

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

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_167)
