# Challenge 164: Counting Multiples

**Difficulty: 5/10  
Labels: Permutations, PIE**

Tim's math teacher gave him `K` prime numbers and a positive integer `N`. He then asked Tim to find the number of integers within `1, 2, 3, ..., N` that are divisible by at least one of the prime numbers he provided. Can you help him?

## Task

You are given a number `T` and `T` test cases follow, for each testcase:

- The first line contains two integers, `K` and `N`, separated by a single space.
- The next line contains `K` integers `P`, separated by a single space, the list of prime numbers Tim received.

Output a single integer, the number of positive integers less than or equal to `N` that is divisible by at least one of the prime numbers.

### Examples

#### Input

```rust
4
2 20
2 5
4 2023
17 71 37 11
1 2023
2027
8 123454321
73939133 7393913 739391 73939 7393 739 73 7
```

#### Output

```rust
‌12
364
0
19242785
```

- For testcase 1, the 12 numbers are `2,4,5,6,8,10,12,14,15,16,18,20`.
- For testcase 3, `2027` is larger than `2023`, so there is no multiple of `2027` in the first `2023` positive integers. (Fun fact - we'll have a prime year in just 4 years)

### Note

- `1 <= T`
- `1 <= N <= 10`<sup>`12`</sup>
- `1 <= K <= 17`
- `2 <= P[i] <= N`
- All integers in `P` are positive prime numbers.
- The expected time complexity is $\mathcal{O}(K \cdot 2^K)$.
  $\mathcal{O}(N \cdot K)$ will not pass.

### Challenge Constraints (won't be tested): `1 <= N <= 10`<sup>`18`</sup>`, 1 <= K <= 20`

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

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_164)
