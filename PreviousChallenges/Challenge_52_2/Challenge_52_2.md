# Challenge 52.2: Differences

## Task:

You are given 2 strings, you need to show the differences between them:
- `[]` for deleted part
- `(before/after)` for changed part 
- `{}` for added part

You should check in the same order stated above so `(h/H)ello` is not equal to `[h]{H}ello`. There will be only one change per case

## Example:

First input `n` is the number of cases.

For each case you are given two lines the first contains the old string the second contains the new string.

### Input
```
1
hello World.
ello World.
```

### Output: 
```
[h]ello World.
```

## Submissions and Grading 

- code must be written in python
- `eval` and `exec` functions are not allowed same goes for `import`

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/PreviousChallenges/Challenge_52_2)
