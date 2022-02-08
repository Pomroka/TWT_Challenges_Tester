# Challenge 88: One Digit Sum

Given a number `x`, find the sum of all the digits and then find the sum of the digits of the sum till the resulting sum is a **one digit number**

## Task

You are given a number `T` and `T` testcases follow, for each testcase you are given a number to calculate the final sum off.

## Examples

### Input

```sh
3
1234
14239087
18
```

### Output

```sh
1
7
9
```

### Explanation

- sum of `1,2,3,4 = 10`; sum of `1,0 =` **1**
- sum of `1,4,2,3,9,0,8,7 = 34`; `sum of 3,4 =` **7**
- sum of `1,8 =` **9**

## Note

- constraint: `1 < len(str(x)) < 1000`

Challenge suggested by @KK1729

## Submissions

Code can be written in any of these languages:

- `Python` 3.9
- `C/C++` (GCC 10.3)
- `Ruby` 3.0
- `Golang` 1.16
- `Java` 18
- `Rust` 1.56

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/PreviousChallenges/Challenge_88)
