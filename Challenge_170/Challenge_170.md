# Challenge 170: Rectangle Area

**Difficulty: 2/10  
Labels: Analysis**

Tim is talking with his good friend, Avib. Avib claims that he has two rectangles with areas A and B. He says that both the width and height of the rectangle with area B are exactly 1 unit more than those of the rectangle with area A. He adds that the widths and lengths of his rectangles are real numbers.
Tim suspects Avib is lying. Can you help Tim determine whether Avib's claim is possible?

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- You are given two integers, `A` and `B`, separated by a single space.

If Avib's claim can never be true, output `LIE`. Otherwise, output `OK`.
Formally, output `OK` if and only if there exists two real numbers `l` and `w` such that $l, w > 0$ and $l \times w = A$ and $(l+1) \times (w+1) = B$.

### Examples

#### Input

```rust
7
20 30
30 20
9 9
9 27
1 2023
1 3
1 4
```

#### Output

```rust
OK
LIE
LIE
OK
OK
LIE
OK
```

- For testcase 1, the rectangles can be $4 \times 5$ and $5 \times 6$.
- For testcase 4, the rectangle with area $A$ can be $\Large{(\frac{17} {2}-\frac{253^{0.5}}{2}) \times (\frac{17}{2}+\frac{253^{0.5}}{2})}$.

### Note

- `1 <= T`
- `1 <= A, B <= 10`<sup>`6`</sup>
- Problem credit: Datatähti 2023 loppu

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

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_170)
