# Challenge 166: SnowballSH and Cute Arrays

**Difficulty: 3/10  
Labels: Prefix Sum**

SnowballSH loves arrays. He calls an array "cute" if and only if the sum of the elements in the array is equal to the length of the array. For example, the array `[0, 2, 1]` is cute, because 0 + 2 + 1 is the length of the array. `[3, 1]` is not cute, because 3 + 1 is not equal to 2.
SnowballSH has a large array. He wants to know how many **non-empty** subarrays in that array are "cute." Can you help him?

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The first line contains an integer `N`. This is the number of elements in the array.
- The next line contains `N` integers, separated by a single space. Call this array `A`. Output a single integer, the number of "cute" **non-empty** subarrays in `A`.

Formally, output the number of ordered pairs `(i, j)` where `i <= j` and `A[i] + A[i+1] + ... + A[j] = length(A)`.

### Examples

#### Input

```rust
‌3
3
0 2 1
6
1 0 0 1 3 1
4
1 1 1 1
```

#### Output

```rust
‌3
7
10
```

- For testcase 1, the cute subarrays are `[0, 2]`, `[0, 2, 1]`, and `[1]`.
- For testcase 2, the cute subarrays are `[1]`, `[1]`, `[1]`, `[0, 0, 1, 3]`, `[0, 0, 1, 3, 1]`, `[1, 0, 0, 1, 3]`, and `[1, 0, 0, 1, 3, 1]`.

### Note

- `1 <= T`
- `1 <= N <= 1,000`
- `0 <= A[i] <= 1,500`

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

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_166)
