# Challenge 55.1: Vampire numbers

A vampire number is a non-negative number that can be factored into two numbers (fangs) each with half as many digits as the original where the two factors contain all the digits of the original, in any order. Both fangs may not have trailing zeros.

For example `1260` = `21*60`, `1395` = `15*93`, `1435` = `35*41`, `1530` = `30*51`, etc..

## Task

Given `n` and `m` 2 integers output the amount of vampire numbers between `n` and `m` (`n` and `m` are counted)

## Examples

You are given a number `T` the number of tests cases. `T` lines follow each line is a test case which has two numbers separated by a space `n m`

### Input
```
3
0 1259
1000 100000
1260 1260
```

### Output
```
0
7
1
```

## Submissions and Grading

- code must be written in python
- `eval` and `exec` functions are not allowed same goes for `import`

**NOTE:** `0 <= n < 17m` and `0 <= m < 17m`

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/PreviousChallenges/Challenge_55_1)
