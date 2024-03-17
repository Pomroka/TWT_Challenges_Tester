# Challenge 192: Field Trip, Part 2

**Difficulty: 4/10  
Labels: DFS, Connected Components, DSU**

The difference between this challenge and last week's is the group going on the field trip.

There are `n` people in a community and there are `m` pairs of friends. **You can choose any subset** of the people (possibly none or all) to go on a field trip.
If you choose `k` people, then:

- The original happiness of the group is `-k`.
- For each pair of friends `(a, b)`, if `a` and `b` are **both** going on the trip, then the happiness increases by one. If only one of the two is going on the trip, then the happiness decreases by one.
- The happiness does not change if neither of them are going.

Notice that if you choose no one to go on the field trip, the happiness is `0`. If you choose everyone, then the happiness is `m-n`.
Calculate the **maximum** happiness that can be obtained over all possible subsets of people going on the field trip.

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The first line contains two integers, `n` and `m`. The people are numbered `1, 2, ..., n`.
- The next `m` lines each contain two integers `a` and `b`. This denotes person `a` and person `b` are friends.

Output a single integer, the maximum total happiness of any group.

### Examples

#### Input

```rust
3
4 5
1 2
1 3
1 4
2 3
3 4
2 1
1 2
20 13
1 2
2 3
3 4
4 1
4 2
1 3
6 7
7 5
8 9
9 10
10 8
11 9
11 8
```

#### Output

```rust
1
0
3
```

- For test case 1, we can choose all four people `{1,2,3,4}` to obtain a happiness of `-4 + 5 = 1`.
- For test case 2, including any person will result in a negative happiness, so the best we can do is do choose nobody.
- For test case 3, it is optimal to select `{1,2,3,4}`, `{8,9,10,11}` to obtain a maximum happiness of `-8 + 6 + 5 = 3`.

### Note

`1 <= T`
`2 <= n <= 5,000`
`1 <= m <= 7,000`

## Submissions

Code can be written in any of these languages:

- `Python` 3.11
- `C` (gnu17) / `C++` (c++20) - GCC 12.2
- `Ruby` 3.2
- `Golang` 1.21
- `Java` 19 (Open JDK) - use **"class Main"!!!**
- `Rust` 1.72
- `C#` 11 (.Net 7.0)
- `JavaScript` ES2023 (Node.js 20.6)

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_192)
