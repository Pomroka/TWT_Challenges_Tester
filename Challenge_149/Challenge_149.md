# Challenge 149: Shopping (Part 3)

**Difficulty: 6/10  
Labels: 2D DP**

I decided to surprise you with a harder one this week. Have fun!

Tim is walking in a supermarket shaped like a `N` by `N` grid. He is standing at the entrance, the top left corner. The exit is in the bottom right corner, however, because Tim is feeling happy today, he will buy every item in his path!

Each cell in the grid contains a nonnegative integer, the price of the item in that cell. Tim must buy the item if he steps on the cell. If Tim is at location `(x, y)`, he can move to `(x + 1, y)` or `(x, y + 1)` in a single movement (and then he will step on that cell).

Compute the minimum amount of money Tim needs to spend to get to the bottom right cell.

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The first line contains a single integer, `N`.
- `N` lines follow. Each line contains `N` nonnegative integers. This is the `N` by `N` grid.

Output a single integer, the minimum sum of costs out of all paths from top left to bottom right, if Tim can move one cell right or one cell down each time.

### Examples

#### Input

```rust
4
3
1 2 3
4 5 6
7 8 9
4
1 2 7 9
8 1 0 1
6 7 8 1
9 9 9 9
3
4 0 0
4 9 9
4 0 0
1
2023
```

#### Output

```rust
21
15
12
2023
```

- For test case 1, the optimal path is `1-2-3-6-9`.
- For test case 2, the optimal path is `1-2-1-0-1-1-9`.
- For test case 3, the optimal path is `4-4-4-0-0`.

#### Note

- `1 <= T`
- `1 <= N <= 100`
- `0 <= each integer in the grid <= 10`<sup>`6`</sup>
- It is guaranteed that sum of all integers in the grid fits in a signed 32-bit integer.

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
- `Python` 3.10

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_149)
