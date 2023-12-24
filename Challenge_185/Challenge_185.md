# Challenge 185: What are the chances?

**Difficulty: 2/10  
Labels: Probability**

Tim has `n` friends and is competing with all of them for a plane ticket to TechWithTimia. They have decided that each of them will roll a random integer from 1 to `k` using a random number generator, and whoever gets the highest number wins the ticket.
Since everyone loves Tim, if Tim ever gets the same number as the person with the highest number, Tim will still win the ticket.
Tim's friends rolled first. Compute the probability that Tim wins the ticket.

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The first line contains two integers `n` and `k`.
- The second line contains `n` integers, the numbers his `n` friends rolled.

Output the required probability in the form of irreducible fraction in format `A/B`, where `A` — the numerator, and `B` — the denominator. If the required probability equals to zero, output `0/1`. If the required probability equals to 1, output `1/1`.

### Examples

#### Input

```rust
4
‌2 6
2 4
4 2
1 1 1 1
7 13
1 8 5 7 11 7 7
19 2024
394 228 1103 429 797 1219 1171 466 390 373 147 597 1247 222 1015 1266 512 1047 955
```

#### Output

```rust
‌1/2
1/1
3/13
3/8
```

For test case 1, Tim has to roll a 4, 5, 6 to win, so the answer is 3/6 = 1/2.

### Note

`1 <= T`
`1 <= n <= 10`<sup>`5`</sup>
`1 <= k <= 10`<sup>`9`</sup>

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

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_185)
