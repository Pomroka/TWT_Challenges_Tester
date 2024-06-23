# Challenge 203: Frequency Sort

**Difficulty: 3/10  
Labels: Implementation**

SnowballSH wants to sort his array in the following order:
For any two elements `x` and `y`,

- If `x` appears more often than `y` in the array, `x` comes before `y`.
- If `x` and `y` appear equally often in the array, the one whose value (first instance) appears earlier comes first.

Can you help him sort his array in this order?

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The first line contains an integer `n`.

The second line contains `n` integers, separated by a single space, SnowballSH's array.

Output `n` integers, separated by a single space, the array after the "frequency sort" described above.

### Examples

#### Input

```rust
6
5
2 1 2 1 2
9
1 3 3 3 2 2 2 1 1
9
11 33 11 77 54 11 25 25 33
1
2024
15
3 1 4 1 5 9 2 6 5 3 5 8 9 7 9
8
27 18 28 18 28 459045235360 28 74713527
```

#### Output

```rust
2 2 2 1 1
1 1 1 3 3 3 2 2 2
11 11 11 33 33 25 25 77 54
2024
5 5 5 9 9 9 3 3 1 1 4 2 6 8 7
28 28 28 18 18 27 459045235360 74713527
```

### Note

`1 <= T`
`1 <= n <= 10,000`
`1 <= a[i] <= 10`<sup>`8`</sup>

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

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_203)
