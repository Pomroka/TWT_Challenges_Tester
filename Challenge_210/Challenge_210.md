# Challenge 210: Halloween, Part 1

**Difficulty: 1/10  
Labels: Sorting**

During Halloween, SnowballSH is collecting candies from his `n` neighbors. Each neighbor is offering a box of candy with a certain tastiness. SnowballSH wants to maximize the sum of the tastinesses he ends up with, but unfortunately his bag can only store up to `k` boxes of candy.

Can you help him find the maximum possible sum of the tastinesses of the boxes he chooses to put in his bag?

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The first line contains two integers `n` and `k`, the number of neighbors and the maximum number of boxes SnowballSH can take, respectively.
- The second line contains an array of `n` integers `a`, where `a[i]` is the tastiness of the box of candy offered by the `i`th neighbor.

Output a single integer, the maximum possible sum of the tastinesses of the boxes SnowballSH chooses to take.

### Examples

#### Input

```rust
5
5 3
5 1 3 2 4
7 5
1 14 13 13 13 13 13
4 2024
100 500 300 500
1 1
1
6 1
1 2 4 8 16 32
```

#### Output

```rust
12
66
1400
1
32
```

- For the first test case, it is optimal for SnowballSH to pick the boxes with tastiness `3`, `4`, and `5`, giving him a total tastiness of `3+4+5=12`. He cannot take more boxes because he is limited to at most `3` boxes.
- For the third test case, it is optimal for SnowballSH to take all `4` boxes.

### Note

- `1 <= T`
- `1 <= n <= 10`<sup>`5`</sup>
- `1 <= k <= 10`<sup>`9`</sup>
- `1 <= a[i] <= 10,000`

### Extra challenges for experienced programmers

To learn more about data structures and algorithms!

1. Solve this challenge without sorting, but with data structures.
2. Solve this challenge with divide and conquer.
3. Solve this challenge in $\mathcal{O}(n + k)$ on average.
4. Utilizing the low values of `a[i]`, solve this challenge in $\mathcal{O}(n + k)$ in worst case.

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

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_210)
