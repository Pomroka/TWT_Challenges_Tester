# Challenge 186: 2024

**Difficulty: 4/10  
Labels: Prime Factorization, Bitmasking, Number Theory**

Happy New Year 🎆 ! It's finally 2024! We wish everyone best of luck in the new year. Since it is holiday season, you will have two weeks to complete this challenge.

The number 2024 has several interesting properties. One of them is that all positive integers `1 <= k <= 2024` can be written as the sum of **distinct** positive integer divisors of 2024, which are `S = {1 2 4 8 11 22 23 44 46 88 92 184 253 506 1012 2024}`. In other words, for all `1 <= k <= 2024`, there is a subset `U` of `S` such that the sum of all elements of `U` is equal to `k`.

For example: `61 = 1 + 2 + 4 + 8 + 46`, `564 = 4 + 8 + 46 + 506`, `1024 = 1 + 11 + 1012`, etc. It can be shown that for any `1 <= k <= 2024`, we can rewrite `k` in this form.

Call an integer `n` "2024-like" if `n` also has this property. For example, `n = 4` is 2024-like because `1=1`, `2=2`, `3=1+2`, `4=4`. `n = 10` is not 2024-like because we cannot rewrite the number 4 as the sum of distinct divisors of 10 (1, 2, 5, 10). `n = 2023` is also not 2024-like because we cannot write the number 2 as the sum of distinct divisors of 2023.

What properties of a number gives it this special property? Given an integer `n`, find whether it is 2024-like.

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The only line contains an integer `n`.
Output `2024` if `n` is 2024-like; otherwise, output `-1`.

### Examples

#### Input

```rust
9
2023
2024
1
3
6
10
252
87648
87654
```

#### Output

```rust
-1
‌2024
2024
-1
2024
-1
2024
2024
-1
```

### Note

1 <= `T`
1 <= `n` <= 10^5

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

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/PreviousChallenges/tree/main/Challenge_186)
