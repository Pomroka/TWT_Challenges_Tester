# Challenge 151: SnowballSH and April Fools' Day

**Difficulty: 1/10  
Labels: lol**

You are playing a number game with SnowballSH. SnowballSH picks one integer, `x`. You need to pick an integer, `y`. SnowballSH then rolls a fair n-sided die, labelled `1, 2, ..., n`, and obtains the number `z`.

You win the game if the following statement is true:
`xyz = xz + yz`
Otherwise, SnowballSH wins.

Since the die is annoyingly random, output the integer `y` you should choose to maximize your chance to win. If there are multiple answers, output the string `:)` (colon followed by right parenthesis).

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The only line contains two integers, `x` and `n`, separated by a single space.

Output a single integer that solely maximizes your chance to win, or `:)` if multiple choices of `y` yields the same maximum chance of winning.

### Examples

#### Input

```rust
4
0 6
5 4
2 1
-2023 2023
```

#### Output

```rust
0
:)
2
:)
```

- For test case 1, if you choose `y = 0`, the equation becomes `0 * 0 * z = 0 * z + 0 * z` and is always true, yielding a 100% win rate for you. It can be shown that this is the only choice that yields 100% win rate.
- For test case 2, it can be shown that any choice of `y` maximizes a win rate of 0% for you. SnowballSH will always win.
- For test case 3, a one-sided die always yields `1`. Thus, the equation becomes `2y = 2 + y`, solving it you obtain `y = 2`.

### Note

- Assume a one-sided die always yields `1`.
- `1 <= T`
- `-10`<sup>`8`</sup>` <= x <= 10`<sup>`8`</sup>
- `1 <= n <= 10`<sup>`4`</sup>

### Hint

Read the title and reread the equation.

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

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_151)
