# Challenge 191: Field Trip, Part 1

**Difficulty: 2/10  
Labels: Sets**

There are `n` people in a community and there are `m` pairs of friends. The community chooses `k` people to go on a trip.
The original happiness of the group is `-k`.
For each pair of friends `(a, b)`, if `a` and `b` are **both** going on the trip, then the happiness increases by one. If only one of the two is going on the trip, then the happiness decreases by one. The happiness does not change if neither of them are going.
Calculate the happiness of the chosen group that will be going on the trip.

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The first line contains three integers, `n`, `m`, `k`. The people are numbered 1, 2, ..., `n`.
- The next `m` lines each contain two integers `a` and `b`, `a != b`. All `m` pairs are unique. This denotes person `a` and person `b` are friends.
- The final line contains `k` integers, the list of people who will be going on the trip as a group.

Output a single integer, the total happiness of the group.

### Examples

#### Input

```rust
2
5 5 4
1 2
2 3
3 4
4 1
4 2
1 2 3 4
6 3 3
1 2
3 4
5 6
5 4 3
```

#### Output

```rust
1
-3
```

- For test case 1, all five friend pairs have both people going, so the happiness value is `(-4)+5 = 1`.
- For test case 2, neither of `(1,2)` are going, both of `(3,4)` are going, and only one of `(5,6)` are going. The answer is `(-3)+0+1-1 = -3`.

### Note

- `1 <= T`
- `2 <= n <= 10,000`
- `1 <= m <= 10,000`
- `1 <= k <= n`

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

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_191)
