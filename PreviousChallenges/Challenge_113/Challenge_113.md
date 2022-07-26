# Challenge 113: Morning Walk

**Difficulty: 7/10**  
John, a senior citizen, likes to go for a walk every morning. But he hates dogs when they stand at the gate of their owner's house. In some houses, there might be more than one dog at the gate! John always tries to avoid them when he goes for a walk. John can tolerate encountering at most `x` dogs during his walk.

He can travel any sub-segment of the street. John would like to know the maximum length of his walk while encountering at most `x` dogs.

The street a has `n` houses and the number of dogs in the `i`<sup>`th`</sup> house is represented by `a[i]`.

## Task

### Input

You are given a number `T` and `T` test cases follow, for each test case:
You are given two integers `n` and `x`, `n` representing the number of houses in the street and `x` the maximum number of dogs John can encounter.
The next line contains space separated array of integers `a` of length `n`

### Output

The maximum length John can walk while encountering at most `x` dogs.

### Constraints

`1 <= n <= 2*10`<sup>`5`</sup>
`1 <= x <= 10`<sup>`9`</sup>
`1 <= a[i] <= 10`<sup>`9`</sup>

### Examples

#### Input

```rs
2
4 5
1 4 5 3
5 10
4 5 4 4 1
```

#### Output

```rs
2
3
```

#### Explanation:

The below explanations follow `1` based indexing not `0`

1. He can cover the sub-segment [1:2]. It can be proved that this is the maximum length (1+4)
2. He can cover the sub-segment [3:5]. (4+4+1)

### Note:

A subsegment is any contiguous part of the array that can be obtained by deleting several(possibly 0) elements from the beginning and deleting several(possibly 0) elements from the end.

An O(n^2) or worse time complexities might not pass in the time limit

Challenge written by @KK1729

### Submissions

Code can be written in any of these languages:

- `Python` 3.10
- `C/C++` (GCC 10.3)
- `Ruby` 3.1
- `Golang` 1.18
- `Java` 18 (Open JDK) - use "class Main"!!!
- `Rust` 1.61
- `C#` 10 (.Net 6.0)
- `JavaScript` ES2022 (Node.js 18.2)

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/PreviousChallenges/Challenge_113)
