# Challenge 130: Array Division

**Difficulty: 4/10
Labels: Binary Search**

This is a classic problem that uses binary search (and some greedy thinking).
If you need help, I suggest you learning the binary search algorithm (on monotonic functions) before attempting this challenge.

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The first line contains two integers, `N` and `D`, separated by a single space.
- The second line contains `N` integers, separated by a single space. Call this array `A`.

Your job is to divide the array `A` into `D` subarrays so that the **maximum** sum in any of the subarrays is **as small as possible**.
Output the **maximum sum** of any subarray when `A` is divided into `D` subarrays optimally.

### Examples

#### Input

```rust
4
5 3
2 4 7 3 5
7 4
6 9 3 5 2 9 6
2 1
13 12
3 3
3 3 3
```

#### Output

```rust
8
15
25
3
```

For test case 1, `A = [2, 4, 7, 3, 5]` and `D = 3`. When `A` is divided into `[2, 4]`, `[7]`, `[3, 5]`, the sums are `6`, `7`, `8`, so we output the maximum sum, `8`. This can be shown to be the minimum answer one can obtain.
For example, if you divide `A` into `[2, 4]`, `[7, 3]`, `[5]`, the maximum sum becomes `7 + 3 = 10`, which is higher than the optimal answer `8`.

For test case 3, the only subarray is `[13, 12]` (as you divide an array into one part), so the answer is `13 + 12 = 25`.
For test case 4, you have no choice but to have subarrays `[3]`, `[3]`, and `[3]`. The maximum sum of those is `3`.

#### Note

`1 <= T`
`1 <= D <= N <= 10`<sup>`5`</sup>
`1 <= A[i] <= 10`<sup>`6`</sup> where `A[i]` is any element in array `A`.

### Submissions

Code can be written in any of these languages:

- `Python` 3.10
- `C` (gnu17) / `C++` (c++20) - GCC 11.2
- `Ruby` 3.1
- `Golang` 1.19
- `Java` 19 (Open JDK) - use **"class Main"!!!**
- `Rust` 1.64
- `C#` 10 (.Net 6.0)
- `JavaScript` ES2022 (Node.js 18.10)

Suggested Time Complexity for each test case: `O(N * log N)`

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_130)
