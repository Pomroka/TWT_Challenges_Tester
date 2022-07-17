# Challenge 112: Race

**Difficulty: 4/10**  
Mark has reached the required height to be eligible for the championship, thanks to you!

Now he has set a target to run at least `x` miles in the race.
However, this is no ordinary race, the initial length of the track is **one** mile and the length of the track increases by `1` mile after every lap completed by Mark.

Find the number of laps he should start to cover at least `x` miles.

## Task

You are given a number `T` and `T` test cases follow, for each test case,
you are given an integer `x`, which represents the number of miles to complete.

### Constraints

`1 <= x <= 10`<sup>`14`</sup>

### Examples

#### Input

```rs
4
3
5
7
10
```

#### Output

```rs
2
3
4
4
```

### Note

1. He covers `1` mile in the first lap, `2` miles in the second lap `(1+2) >= 3`

2. He covers `1` mile in the first lap, `2` miles in the second lap, `3` miles in the third lap `(1+2+3) >= 5`

3. He covers `1` mile in the first lap, `2` miles in the second lap, `3` miles in the third lap and `4` miles in the 4th lap `(1+2+3+4) >= 7`

4. He covers `1` mile in the first lap, `2` miles in the second lap, 3 miles in the third lap and `4` miles in the 4th lap `(1+2+3+4) >= 10`

Challenge written by @KK1729

Try to find a `O(1)` solution or a `O(log(n))` solution

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

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/PreviousChallenges/Challenge_112)
