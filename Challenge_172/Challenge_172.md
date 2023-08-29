# Challenge 172: Learning Skills

**Difficulty: 3/10  
Labels: Greedy**
Avib wants to learn two skills from Tim's YouTube videos. Unfortunately, Tim has many videos, and they either teach both skills, one of them, or neither of them. The videos vary in lengths. Help Avib determine the minimum amount of time to acquire both skills from Tim's videos.

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The first line contains an integer `n`, the number of videos.
`n` lines follow. Each of them start with an integer `m`, the time it takes to watch the video. Then, two digits 0 or 1 are given, representing each skill. 1 means the video teaches that skill, and 0 means it doesn't.
Considering these `n` videos, if Avib can only watch one video at a time, output the minimum amount of time to acquire both skills. If it is not possible, output `-1`.

### Examples

#### Input

```rust
4
4
2 00
3 10
4 01
4 00
3
16 11
8 10
7 01
3
9 11
8 01
7 10
6
4 01
6 01
7 01
8 00
9 01
1 00
```

#### Output

```rust
7
15
9
-1
```

- For test case 1, Avib can choose skills #2 and #3, taking 3+4=7.
- For test case 2, learning #2 and #3 is faster than learning #1.

### Note

- `1 <= T`
- `1 <= n, m <= 10`<sup>`5`</sup>
- Credit: codeforces

### Submissions

Code can be written in any of these languages:

- `Python` 3.10
- `C` (gnu17) / `C++` (c++20) - GCC 11.2
- `Ruby` 3.1
- `Golang` 1.19
- `Java` 19 (Open JDK) - use **"class Main"!!!**
- `Rust` 1.68.2
- `C#` 10 (.Net 6.0)
- `JavaScript` ES2022 (Node.js 18.10)

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_172)
