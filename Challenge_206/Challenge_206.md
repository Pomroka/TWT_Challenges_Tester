# Challenge 206: Finding Triangles

**Difficulty: 3/10  
Labels: Geometry, Permutations, Sets**

A triangle is a plane figure with three straight sides. A nondegenerate triangle is a triangle with a non-zero area.

SnowballSH has many sticks of various lengths. Using only one stick for each side, how many **distinct** nondegenerate triangles can he piece together?

Note that two nondegenerate triangles are considered the same if they have the same set of three side lengths. Also note that SnowballSH cannot break any stick or use the same stick for multiple sides.

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The first line contains an integer `N`.
The second line contains `N` positive integers, separated by a single space, the lengths of the sticks SnowballSH can use.

Ouput a single integer, the number of distinct nondegenerate triangles SnowballSH can put together using only the given sticks.

### Examples

#### Input

```rust
8
4
1 2 3 4
5
2 3 6 8 10
6
5 5 5 2 4 4
5
10 10 10 10 10
8
1 1 2 3 5 8 13 21
9
2024 293967 12048 128374 3298 1 100 3298 99
3
8 3 4
15
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
```

#### Output

```rust
1
3
6
1
0
4
0
203
```

For test case 1, the only possible nondegenerate triangle is using sticks of lengths `2`, `3`, `4`.
For test case 3, the possible nondegenerate triangles are `(2,4,4)`, `(2,4,5)`, `(2,5,5)`, `(4,4,5)`, `(4,5,5)`, and `(5,5,5)`.

### Note

`1 <= T`
`3 <= N <= 100`
`1 <= stick length <= 10`<sup>`7`</sup>

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

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_206)
