# Challenge 106: Reverse Index

**Difficulty: 1/10**  
_**Demon Slayer Story Part 5**_
It’s been a week or so since my encounter with the demon and the demon slayer. I’m heading home from another taekwondo class. The sky is rather cloudy, very similar to that day. I’m approaching the front door which I notice is slightly open. I wonder if my brother has left it open again like he does sometimes. As I come in I notice a large muscular person standing inside. “Can I help you?” I ask. “You can help me kill them but it’s my dinner.” It said in a deep croaky voice.

On a paper, you see a upside-down triangle, with numbers on each cell, like this for size of 3:

```rs
1 2 3
0 4 5
0 0 6
```

For size `s`, a square of dimension `s`x`s` is drawn. For row `r`, a padding of `r-1` 0s are added to the front of that row. Then, numbers are labelled starting with 1 from left-to-right, top-to-bottom, to the empty squares. A number is also written on the paper.

Find the row and column in which this number is located. If there are multiple or no answer, output `BAD INPUT`.

## Task

You are given a number `T` and `T` testcases follow, for each testcase:
You are given an integer `s`, representing the size of the upside-down triangle, and an integer `v`, representing the number written on the paper.
Let `r` be the row `v` is in, and `c` be the column `v` is in (1-indexed).
If there is exactly **ONE** answer, output `r v` (separated by a single space). Otherwise, output `BAD INPUT`.

### Examples

#### Input

```rs
6
2 2
3 5
3 7
3 0
9 32
2 0
```

#### Output

```rs
1 2
2 3
BAD INPUT
BAD INPUT
5 6
2 1
```

#### Explanation

- For test case 1, the paper looks like this:

```rs
1 2
0 3
```

2 is on the 1st row and 2nd column.

- For test case 3, 7 is not on the triangle.
- For test case 4, 0 occurs multiple times on the triangle.
- For test case 6, 0 occurs exactly once on the triangle, 2nd row, 1st column.

### Note

- 1 <= `T`
- 1 <= `s` <= 10^8
- 0 <= `v` <= 10^9

Challenge suggested by @Pièrre (old: WaterSteen/Sjourd)

### Submissions

Code can be written in any of these languages:

- `Python` 3.10
- `C/C++` (GCC 10.3)
- `Ruby` 3.1
- `Golang` 1.18
- `Java` 18 (Open JDK) - use "class Main"!!!
- `Rust` 1.60
- `C#` 10 (.Net 6.0)

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/PreviousChallenges/Challenge_106)
