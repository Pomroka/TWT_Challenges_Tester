# Challenge 63.2: Hmmm, Substrings ?

Unfortunately unable to think of a story.

## Task

Given a string `s` and an integer `k`, output the length of the longest substring of `s` such that the frequency of each character in this substring is greater than or equal to `k`. (output `0` if none was found).

## Examples

You are given a number `T` the number of tests cases. `T` cases follow.  
For each case you are given a string `s` and an integer `k`.

### Input
```
5
aaabb 3
ababbc 2
abbacbb 2
abacbb 2
dcdcdc 5
```

### Output
```
3
5
4
2
0
```

### Explanation 

- The longest substring is `"aaa"`, as `'a'` is repeated `3` times.
- The longest substring is `"ababb"`, as `'a'` is repeated `2` times and `'b'` is repeated `3` times.
- The longest substring is `"abba"`, as `'a'` is repeated `2` times and `'b'` is repeated `2` times.
- The longest substring is `"bb"`, as `'b'` is repeated `2` times.
- None was found.


## Submissions and Grading

- code must be written in python
- `eval`, `exec` and `open` functions are not allowed same goes for `import`

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/PreviousChallenges/Challenge_63_2)