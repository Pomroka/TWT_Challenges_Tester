# Challenge 120: Nth Fibonacci Number

**Difficulty: 3.5/10**  
The Fibonacci Numbers are extremely useful in mathematics. It is defined by:

```rust
F[0] = 0
F[1] = 1
F[n] = F[n-2] + F[n-1]
```

For example, `F[4] = F[2] + F[3] = (F[0] + F[1]) + (F[1] + F[2]) = (0 + 1) + (1 +  (0 + 1)) = 1 + (1 + 1) = 3`
The first few Fibonacci numbers are `0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...`
Given an integer `n`, output `F[n]`, the nth Fibonacci number, modulo `(10`<sup>`9`</sup>` + 7)`.

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The first line contains an integer `n`.

Output `F[n] mod (10^9 + 7)`.

### Examples

#### Input

```rust
5
0
1
10
30
1234567
```

#### Output

```rust
0
1
55
832040
571739961
```

### Note

`1 <= T`
`0 <= n <= 2 * 10`<sup>`6`</sup>

1. Modulo operation: The result of `a mod b` is `r` such as `a = bk + r` where `k` and `r` are integers and `0 <= r < b`. This is simply the `%` operator in most programming languages.
2. You might not want to actually compute the result of `F[n]` then mod it by (`10`<sup>`9`</sup>` + 7`). The result will be too big. Your solution will fail due to Time or Memory Limit Exceeded if you're using Python or any language with BigInt, or due to integer overflow.

### Extra Challenge

Find a `O(log n)` solution that will solve quickly for even larger inputs such as:
`0 <= n <= 10`<sup>`18`</sup>
This extra constraint will not be tested against your submission

### Submissions

Code can be written in any of these languages:

- `Python` 3.10
- `C/C++` (GCC 10.3)
- `Ruby` 3.1
- `Golang` 1.18
- `Java` 18 (Open JDK) - use "class Main"!!!
- `Rust` 1.62
- `C#` 10 (.Net 6.0)
- `JavaScript` ES2022 (Node.js 18.2)

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/PreviousChallenges/Challenge_120)
