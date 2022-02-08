# Challenge 81: permutations

Tekgar is relaxing on a bench in a park. He hears footsteps, first quite far away, then closer and closer. He looks up. "What are you doing?" Lynx says.  
"I'm on my break"  
"I figured, anyway, this stupid machine doesn't wanna work, you wanna look into it?"  
"Sure"

## Task

You are given a number `T` and `T` testcases follow. For each testcase, you are given a number `n`. Print the number of permutations (not compulsory to use all digits of `n` in a permutation) which are `even`.

## Examples

### Input
```
2
223
458
```

### Output
```
4
6
```

### 1st case explanation:

The different [non repeating] permutations of `N`, where the permutation could even be only one digit (this digit `d` has to be a part of `n`) are :=
```
2
22
223
232
322
```
Only `4` of these values are even i.e.: `2`, `22`, `232`, `322`

### 2nd case explanation:

The different [non repeating] permutations of `N`, where the permutation could even be only one digit (this digit `d` has to be a part of `n`) are :=
```
4
45
54
458
485
548
584
845
854
```
Out of these only `6` values are even i.e.: `4`, `54`, `458`, `548`, `584`, `854`

formally, a permutation will be all combinations of
```
arr[0:1]
arr[0:2]
arr[0:3]
......
arr[0:len(arr)]
```
**Valid permutation cant start with `0`**

example
```
202

2
20
02  <- invalid, dont count
022 <- invalid, dont count
202
220
```

Challenge suggested by @OneMegaByte 

## Submissions and grading

Code can be written in either of these languages:

- Python 3.9
- C 10.3
- C++ (G++ 10.3)
- Ruby 3.0
- Golang 1.16

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/PreviousChallenges/Challenge_81)