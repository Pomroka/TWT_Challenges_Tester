# Challenge 111: Height

**Difficulty: 2/10**  
Mark's current height is `x`. But in order to be eligible for the upcoming National Athletics Championship, his height should be strictly greater than `y`.

His doctor recommended a drink that would increase his height by `z` everyday.
Mark starts consuming the drink from today. He wants to know how many days it would take for his height to become strictly greater than `y` including today.

It is guaranteed that the answer is less than `10`<sup>`14`</sup>

## Task

You are given a number `T` and `T` testcases follow, for each testcase
you are given three integers `x y z` in a single line

Output the number of days it will take for his height to become strictly greater than `y`

### Examples

#### Input

```rs
2
1 10 3
3 8 2
```

#### Output

```rs
4
3
```

Explanation for testcase 1:
On the first day his height becomes `4` `(1+3)`, `7` on the second day, `10` on the third, and `13` on the `4` the day. `(13 > 10)`

### Constraints

`1 <= x, y, z <= 10`<sup>`12`</sup>
`x < y`

Challenge written by @KK1729

### Submissions

Code can be written in any of these languages:

- `Python` 3.10
- `C/C++` (GCC 10.3)
- `Ruby` 3.1
- `Golang` 1.18
- `Java` 18 (Open JDK) - use **"class Main"!!!**
- `Rust` 1.61
- `C#` 10 (.Net 6.0)
- `JavaScript` ES2022 (Node.js 18.2)

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/PreviousChallenges/Challenge_111)
