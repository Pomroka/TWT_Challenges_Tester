# Challenge 78: The jokester | The scandal #1

The story is rather big, so I had to type it elsewhere, here's the link:
https://code-sharing.herokuapp.com/xDc31Y-P88E

## Task

You are given a number `T` the number of tests cases. `T` cases follow.  
For each case you are given the `width` and `height` of a two-dimensional array (`matrix`), and the `matrix` of potentially unequal height and width containing only `0s` and `1s`. All rows will be of the same length, and all columns be of the same length. Each `0` represents land, and each `1` represents part of a river. A river consists of any number of `1s` that are either horizontally or vertically adjacent (but not diagonally adjacent).  
The number of adjacent `1s` forming a river determine its size. Write code that outputs an array of the sizes of all rivers represented in the input matrix. Note that these sizes need to be in an ascending order.

## Sample Input:
```
1
5 5
1 0 0 1 0
1 0 1 0 0
0 0 1 0 1
1 0 1 0 1
1 0 1 1 0
```

## Output:
```
1 2 2 2 5
```

Challenge suggested by @KK1729

## Submissions and grading

Code can be written in either of these languages:

- `Python 3.9` - Fully supported by my tester
- `Ruby 3.0` - May or may not work in my tester
- `C++ - G++ 10.3` - Should work with my tester same other compiled languages
- Other languages not officially supported - May or may not work in my tester

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/PreviousChallenges/Challenge_78)