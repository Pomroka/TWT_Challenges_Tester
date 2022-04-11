# Challenge 98: So Close!

**Difficulty: 3/10**  
A friend of Avib showed him that for almost every pair of positive integers, he can multiply each by an integer to make their sum exactly `1`.
Avib doesn't believe him, so he gives his friend a list of integer pairs for him to solve. Unfortunately, Avib's friend is not very good at math, so it is taking a long time for him to manually compute the answers. Can you help him?

## Task

You are given a number `T` and `T` testcases follow, for each testcase,  
You are given two positive integers `X` and `Y`, separated by one single space.  
Let `A` and `B` be integers (not necessarily distinct or positive), and `A * X + B * Y = 1`.  
If such `A` and `B` exist, output the ordered pair `A,B` . If multiple solutions exist, output the one with the least value of `A^2 + B^2`. If no such `A` and `B` exist, output `IMPOSSIBLE`.
It is guaranteed that there is only one ordered pair with the least value of `A^2 + B^2`, if there is any solution.

### Examples

#### Input

```rs
5
3 5
16 7
76 19
25 98
2022 337
```

#### Output

```rs
2,-1
-3,7
IMPOSSIBLE
-47,12
IMPOSSIBLE
```

For case `1`, `2 * 3 + -1 * 5 = 1`, and it has the least value of `A^2 + B^2`, `5`.  
For case `3`, It is not possible to construct `1` with `76 * A` and `19 * B`.  
For case `4`, `25 * -47 + 98 * 12 = 1`.

#### Note

`1 ≤ T`
`1 ≤ X, Y ≤ 30,000`

### Submissions

Code can be written in any of these languages:

- `Python` 3.10
- `C/C++` (GCC 10.3)
- `Ruby` 3.1
- `Golang` 1.16
- `Java` 18 (Open JDK)
- `Rust` 1.59
- `C#` 10 (.Net 6.0)

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/PreviousChallenges/Challenge_98)
