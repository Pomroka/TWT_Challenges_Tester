# Challenge 197: Eraser

**Difficulty: 2/10  
Labels: Greedy**

Tim was completing a [Nonogram](https://en.wikipedia.org/wiki/Nonogram) grid on paper when he realized one of his row is completely wrong! The row is an array of `n` squares, where each square is currently either black or white.
Fortunately, Tim has an eraser, but it can only erase `k` consecutive squares at once by changing these squares to white. Help him find the minimum number of times he needs to use his eraser to make the entire row of squares white.

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The first line contains two integers `N` and `k`.
The second line contains `N` letters, each `W` or `B`, denoting that the `i`th square is white if the `i`th letter is `W` or black if it is `B`.

If one operation denotes turning `k` consecutive squares to white, output an integer, the minimum number of operations needed to turn all the squares white.

### Examples

#### Input

```rust
‌8
6 3
WBWWWB
7 3
WWBWBWW
5 4
BWBWB
5 5
BBBBB
8 2
BWBWBBBB
10 2
WBBWBBWBBW
4 1
BBBB
3 2
WWW
```

#### Output

```rust
‌2
1
2
1
4
3
4
0
```

- For test case 1, **WBW**WWB->WWW**WWB**->WWWWWW takes 2 operations. The bolded texts denote the squares we are erasing.
- For test case 2, WW**BWB**WW->WWWWWWW takes 1 operation.
- For test case 8, all squares are already white.

### Note

`1 <= T`
`1 <= k <= N <= 5,000`
It is guaranteed that the string only contains `W` or `B` and contains exactly `N` characters.
`O(N`<sup>`2`</sup>`)` solutions are acceptable. However, the problem can be solved in `O(N)`.

Source: Codeforces

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

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_197)
