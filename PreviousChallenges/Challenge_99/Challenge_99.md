# Challenge 99: Challenge Testing

**Difficulty: 1/10**  
It's near the 100th challenge, and we would like you to try being a challenge tester too!

## Task

You are given a number `T` and `T` testcases follow, for each testcase,  
You are given two positive integers, `N` and `P`. The next line will contain `N` characters, consisting only `"Y"` and `"N"` characters, in which `"Y"` means the participant got the test case right, `"N"` means the participant got it wrong.  
If the participant has an accuracy above or equal to `P%`, then the participant passes. For each test case, print `PASS` if the participant passes, and `FAIL` if the participant doesn't.

### Examples

#### Input

```rs
4
4 50
YNYY
5 100
YYYYN
1 100
Y
9 33
YNNYNNNYN
```

#### Output

```rs
PASS
FAIL
PASS
PASS
```

- For test case `1`, the participant passed `3` out of `4` test cases, `3/4 = 75% > 50%`.  
- For test case `2`, the participant passed `4/5 = 80% < 100%`.  
- For test case `4`, the participant passed `3/9 = 33.33% > 33%`

#### Note

- `1 ≤ T`  
- `1 ≤ N ≤ 40,000`  
- `0 ≤ P ≤ 100`  

### Submissions

Code can be written in any of these languages:

- `Python` 3.10
- `C/C++` (GCC 10.3)
- `Ruby` 3.1
- `Golang` 1.18
- `Java` 18 (Open JDK)
- `Rust` 1.59
- `C#` 10 (.Net 6.0)

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/PreviousChallenges/Challenge_99)
