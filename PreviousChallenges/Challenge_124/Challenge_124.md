# Challenge 124: Expensive Trip

**Difficulty: 3/10
Labels: Binary operations, Loops, Math**

Bob is on a trip. On the trip, he needs to go from city `a` to city `b`, where `a` and `b` are integer labels of two cities. However, the only way he can travel from `a` to `b` is by going through every single city in the range [a, b]. The cost of visiting city `x` is `x`<sup>`2`</sup>. Help Bob find the total cost of the trip, modulo (`10`<sup>`9`</sup>` + 7`).

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The first line contains two numbers, separated by a single space, `a` and `b`.

Output the cost of the trip from `a` to `b` -- which is the sum of all squares of the range `[a, b]` -- **modulo by (`10`<sup>`9`</sup>` + 7`)**.

### Examples

#### Input

```rust
4
1 4
3 6
9 9
1234 4321
```

#### Output

```rust
30
86
81
276259650
```

For test case `1`, Bob needs to travel from city `1` to city `4`. The total cost is `1`<sup>`2`</sup>` + 2`<sup>`2`</sup>` + 3`<sup>`2`</sup>` + 4`<sup>`2`</sup>` = 30`.
For test case `3`, Bob only needs to stay at city `9`, so the cost is just `9`<sup>`2`</sup>` = 81`.
For test case `4`, although the actual result is really big, we modulo it by `10`<sup>`9`</sup>` + 7`.

#### Note

`1 <= T`
`1 <= a <= b <= 10`<sup>`5`</sup>
The range is inclusive.
Modulo means the remainder (`%`) operator. Output the remainder of the actual result divided by `10`<sup>`9`</sup>` + 7`.
An `O(N)` time complexity is enough to pass.

#### Extra Challenge

This constraint will NOT be tested against your submission. This is only for an extra challenge to find a more efficient solution.
`-10`<sup>`9`</sup>` <= a <= b <= 10`<sup>`9`</sup>

Challenge suggested by @KK1729

### Submissions

Code can be written in any of these languages:

- `Python` 3.10
- `C/C++` (GCC 10.3)
- `Ruby` 3.1
- `Golang` 1.18
- `Java` 18 (Open JDK) - use "class Main"!!!
- `Rust` 1.62
- `C#` 10 (.Net 6.0)
- `JavaScript` ES2022 (Node.js 18.2)

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/PreviousChallenges/Challenge_124)
