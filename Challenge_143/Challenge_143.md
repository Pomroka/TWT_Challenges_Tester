# Challenge 143: Big and Small

**Difficulty: 2/10  
Labels: Sorting**

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The first line contains two integers `N` and `K`, separated by a single space.
- The next line contains `N` integers, separated by a single space. Call this array `A`.

Output one integer, the positive difference between the sum of the `K` largest elements in `A` and the sum of the `K` smallest elements in `A`.

### Examples

#### Input

```rust
4
5 2
7 3 9 2 6
6 4
-1 -1 0 -2 1 1
1 1
5
10 9
5 -5 4 -4 3 -3 2 -2 1 -1
```

#### Output

```rust
11
5
0
10
```

For test case 1, the two smallest elements are `2`, `3`, sums to `5`, and the two largest elements are `7`, `9`, sums to `16`. Therefore, the answer is `16 - 5 = 11`.
For test case 3, the smallest and largest element are the same, so output `0`.

### Note

`1 <= T`
`1 <= K <= N <= 10`<sup>`5`</sup>
`-10`<sup>`9`</sup>` <= A[i] <= 10`<sup>`9`</sup>
It is guaranteed that `-10`<sup>`9`</sup>` <= the sum of A <= 10`<sup>`9`</sup> (so don’t worry about integer overflow)

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

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_143)
