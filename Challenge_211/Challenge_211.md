# Challenge 211: Halloween, Part 2

**Difficulty: 4/10  
Labels: Dynamic Programming**

During Halloween, SnowballSH is collecting candies from his `n` neighbors. Each neighbor is offering a box of candy with a certain tastiness. SnowballSH wants to maximize the sum of the tastinesses he ends up with.

Each box of candy that a neighbor offers **has a certain weight**, and SnowballSH’s bag can only carry up to `k` units of weight.

Can you help SnowballSH determine the maximum possible sum of tastinesses he can collect, given the weight limitations of his bag?

## Task

You are given a number `T` and `T` test cases follow, for each test case,

- The first line contains two integers `n` and `k`, where `n` is the number of neighbors, and `k` is the maximum weight SnowballSH's bag can carry.
- The second line contains an array of `n` integers `w`, where `w[i]` is the weight of the box of candy offered by the `i`-th neighbor.
- The third line contains an array of `n` integers `a`, where `a[i]` is the tastiness of the box of candy offered by the `i`-th neighbor.

Output a single integer, the maximum possible sum of the tastinesses of the boxes SnowballSH can choose, without exceeding the weight limit `k` of his bag.

### Examples

#### Input

```rust
7
6 5
3 5 1 4 1 3
4 5 3 4 2 5
8 15
1 3 2 5 5 3 4 2
9 7 2 10 9 5 3 10
3 100
101 101 101
1 2 3
9 30
22 8 13 31 47 19 2 26 39
162 186 24 200 68 192 45 14 113
7 123
46 30 31 1 45 47 39
108 87 79 175 8 142 1
3 97
4 1 39
178 192 18
1 1000000000
1000
10000
```

#### Output

```rust
10
41
0
423
483
388
10000
```

- For the first test case, it is optimal for SnowballSH to pick the boxes with tastiness 2, 3, and 5, which have weights 1, 1, and 3. Since `1+1+3=5`, they all fit into his bag. The answer is therefore `2+3+5=10`.
- For the third test case, it is impossible for SnowballSH to take any box, so the answer is `0`.

### Note

- `1 <= T`
- `1 <= n <= 1,000`
- `1 <= k <= 10`<sup>`9`</sup>
- `1 <= a[i] <= 10,000`
- `1 <= w[i] <= 1,000`
- **It is guaranteed that the sum of all elements of `w` does not exceed 1,000.**
- **Remember that `k` is very large.**

### Submissions

Code can be written in any of these languages:

- `Python` 3.11
- `C` (gnu17) / `C++` (c++20) - GCC 12.2
- `Ruby` 3.3.4
- `Golang` 1.21
- `Java` 19 (Open JDK) - use **"class Main"!!!**
- `Rust` 1.72
- `C#` 11 (.Net 7.0)
- `JavaScript` ES2023 (Node.js 20.6)
- `Zig` 0.13.0

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_211)
