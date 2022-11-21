# Challenge 133: Increasing or Decreasing?

**Difficulty: 1/10
Labels: While loop**

We call an array of numbers strictly increasing if each number is strictly greater than all the numbers before it.
We call an array of numbers strictly decreasing if each number is strictly less than all the numbers before it.
We call an array of numbers **"bad"** if it is neither strictly increasing nor strictly decreasing.

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The first line contains an integer `N`. This is the number of elements in the array.
- The next line contains `N` integers, separated by a single space.

Output `inc` if the array is strictly increasing, `dec` if the array is strictly decreasing, or `bad` if the array is neither of the previous two.

### Examples

#### Input

```rust
4
4
-8 5 6 9
3
1 0 -1
2
7 7
5
1 3 7 4 5
```

#### Output

```rust
inc
dec
bad
bad
```

### Note

`1 <= T`
`2 <= N <= 10`<sup>`5`</sup>

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

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_133)
