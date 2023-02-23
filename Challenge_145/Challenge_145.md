# Challenge 145: Swappity-Swap

**Difficulty: 2/10  
Labels: Arrays**

You are given an array of `n` integers. You have to process `q` queries that either require you to swap two elements with index `x` and `y` in the array, or report the current value at index `x`

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- In first line you are given an integer `n` and an integer `q`
- In the next line, you are given `n` integers denoting the array `a`.
- Then, `q` lines follow denoting the queries

    For each query you are given 3 numbers. First `t` denoting the type of query:

  - If `t` is `1` you are given two integers `x` and `y` denoting the indices of the elements to be swapped
  - If `t` is `2` you are given an integer `x`, and you have to output the element at index `x`. If there is more than one type `2` query, print `x`'s in new line.

### Examples

#### Input

```rust
1
4 3
3 4 1 7
1 2 3
1 3 4
2 4
```

#### Output

```rust
4
```

### Note

After the first query, elements at index `2` and `3` are swapped. The array looks like `[3, 1, 4, 7]`

After the second query, elements at index `3` and `4` are swapped. The array looks like `[3, 1, 7, 4]`

The third query asks for the element at index `4`. The answer is `4`.

The problem statement uses **1 based** indexing

### Constraints:

`1 <= n, q < 10000`
`0 <= a[i] <= 10`<sup>`9`</sup>
`1 <= t <= 2`
`1 <= x, y <= n`

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

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_145)
