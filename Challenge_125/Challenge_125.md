# Challenge 125: Pokémon Adventure, Part 1

**Difficulty: 5/10
Labels: Two Pointers(2P)**

Professor Oak has `N` Pokémon in this garden. Each Pokémon has a different strength value `S[i]`.
One day, a young boy named Ash Ketchum came to the Professor's house and asked to borrow a team of Pokémon for an adventure. Professor Oak made his Pokémon line up in a single file.
Ash wants to pick out a **consecutive** section in the file of Pokémon such that the sum of strength values of these Pokémon is **exactly** `X`.
Help Ash find the number of different subsections of Pokémon he can pick.

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The first line contains two integers, `N` and `X`, separated by a single space.
- The second line contains array of `N` integers, separated by a single space, call the array `S`.

Output the number of distinct subarrays of `S` such as the sum of the subarray is exactly `X`.

### Examples

#### Input

```rust
4
5 7
2 4 1 2 7
10 7
1 1 1 1 1 1 1 1 3 4
5 1
1 1 1 1 1
4 2
3 1 5 1
```

#### Output

```rust
3
4
5
0
```

For test case `1`, we want to pick subarrays of `[2, 4, 1, 2, 7]` such that the sum is exactly `7`. The possible subarrays are: `[2, 4, 1]`, `[4, 1, 2]`, and `[7]`.
For test case `4`, it is impossible to obtain `2` from any subarray.

#### Note

`1 <= T`
`1 <= N <= 400,000`
`1 <= X, S[i] <= 10`<sup>`9`</sup>
**`O(N`<sup>`3`</sup>`)` or `O(N`<sup>`2`</sup>`)` solutions will likely fail the testing. Try to find an `O(N)` solution.**

### Submissions

Code can be written in any of these languages:

- `Python` 3.10
- `C/C++` (GCC 10.3)
- `Ruby` 3.1
- `Golang` 1.18
- `Java` 18 (Open JDK) - use **"class Main"!!!**
- `Rust` 1.62
- `C#` 10 (.Net 6.0)
- `JavaScript` ES2022 (Node.js 18.2)

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_125)
