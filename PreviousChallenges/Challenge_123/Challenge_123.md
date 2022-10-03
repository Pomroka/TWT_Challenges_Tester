# Challenge 123: Conjecture or Proof?

**Difficulty: 2/10**
**Labels: simulation, loops**

There is a weird algorithm in mathematics. For any number `x`, **divide** it by `2` (`x = x/2`) if it is **even**, or **multiply** it by `3` then **add** `1` to it (`x = 3x+1`) if it is **odd**. Repeat that over and over until `x` reaches `1`. It has been shown that for any `x` up to a very, very big number, `x` will eventually end up in a `4-2-1` loop.

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The first line contains a number `x`.

Do the algorithm above, and output all the steps until it reaches `1`, separated by a single **space**.

### Examples

#### Input

```rust
3
8
3
1
```

#### Output

```rust
8 4 2 1
3 10 5 16 8 4 2 1
1
```

#### Note

`1 <= T`
`1 <= x <= 10`<sup>`6`</sup>
It can be shown that all `x` in the above constraint will eventually end up at `1`.

### Extra Challenge

Can you prove that this algorithm will always end up in a `4-2-1` loop? (I am not responsible if you spend your entire life on it with no success :))

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

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/PreviousChallenges/Challenge_123)
