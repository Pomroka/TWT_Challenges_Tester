# Challenge 107: Math Evaluator, Part I

> This challenge and the next few challenges will focus on evaluating math expressions. The task will get progressively harder throughout this series of challenges, but code from the previous challenge may be used for the base of the next challenge.
>
> In these challenges, you may **NOT** use existing tools or functions to evaluate the expressions. That said, functions such as `exec` and `eval` in Python and `eval` in Ruby, and any other functions that uses a built-in parser or evaluator are banned (they will be manually checked). This is for fair competition purposes.

**Difficulty: 3/10**  
_**Demon Slayer Story Part 5**_  

I think I forgot how to breathe. Is that a demon too? And this thing is in my home?! If what happened that day when I fought that demon applies to all of them I should be able to finish it quickly. There is just enough space between that demon and the wall. Backflip onto the wall to use it as a jump ramp, onto that demon’s head and a push kick rapidly extending my leg into the demon’s head. The head… Stayed intact. I’m flying backwards onto my back just out the front door. The demon chuckled.

## Task

You are given a number `T` and `T` testcases follow, for each testcase,
You are given one line of math expression.
Numbers will be separated by an operator (`+`, `-`, or `*`) with one space on each side. All operators in one expression will always be the same, so you don't need to worry about operator precedence's.
Numbers may be positive or negative.
Zero will always be `0`, never `-0`.

Let the result of the expression be `r`. Output `r mod (10^9 + 7)` if `r >= 0`, or `-(|r| mod (10^9 + 7))` if `r < 0`.

### Examples

#### Input

```rs
7
1 + 1
1 + 3 + 9
-7 + 7 + 0
3 - -2 - 9
2 * 5 * 3
2308723 * 2093810 * -1238
66
```

#### Output

```rs
2
13
0
-4
30
-761240265
66
```

For test case 1, `1 + 1 = 2`.
For test case 4, `3 - -2 - 9 = 3 + 2 - 9 = -4`.
For test case 6, although the actual result is `-5984525803131940`, we output `-(|-5984525803131940| mod (10^9 + 7)) = -761240265`.

#### Note

The operator will always be the same in each test cases.
Each operator will be either `+`, `-`, or `*`.
`1 ≤ T`
`-10`<sup>`8`</sup>` ≤ each number ≤ 10`<sup>`8`</sup>

### Submissions

Code can be written in any of these languages:

- `Python` 3.10
- `C/C++` (GCC 10.3)
- `Ruby` 3.1
- `Golang` 1.18
- `Java` 18 (Open JDK) - use **"class Main"**!!!
- `Rust` 1.60
- `C#` 10 (.Net 6.0)

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_107)
