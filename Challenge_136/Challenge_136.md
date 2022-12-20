# Challenge 136: Same Line

**Difficulty: 2/10
Labels: Sets**

Hethat received some coordinates from his teacher. All points but one are on the same line in a regular coordinate plane. To test his knowledge of algebra, his teacher asked him to identify the point that is not on the same line as all other points. Can you help him out?

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The first line contains an integer `N`.
- The next `N` lines each contain one pair of coordinates `x y`.

Output the outlier in the form `x y`.

### Examples

#### Input

```rust
2
4
0 0
2 3
6 9
3 5
6
0 1
1 0
1 1
1 -9
1 6
1 2
```

#### Output

```rust
3 5
0 1
```

For test case 1, points `(0,0)`, `(2,3)`, `(6,9)` are all on the line `y=1.5x`, while `(3,5)` is not.

### Note

`1 <= T`
`4 <= N <= 10`<sup>`5`</sup>
`-10`<sup>`6`</sup>` <= x, y <= 10`<sup>`6`</sup>
It is guaranteed that all points but one lie on the same line.
All points are distinct.

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

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_136)
