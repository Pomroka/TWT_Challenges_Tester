# Challenge 93: Traffic Lights

**Difficulty: 6/10 (USACO Silver)**  
In the city of Tekalovania, there are `N` traffic lights (each labeled `1...N`) along one major road. Unfortunately, a recent earthquake damaged several of those traffic lights...

Tekgar, the mayor would like `K` consecutive working traffic lights for the moment, at any position on the road, but he wants to spend as little money as possible. Find the minimum number of traffic lights that needs to be fixed in order to accomplish the mayor's wish.

## Task

You are given a number `T` and `T` testcases follow, for each testcase, you are given `N` (`1 ≤ N ≤ 100,000`), `K` (`1 ≤ K ≤ N`), `B` (`1 ≤ B ≤ N`), separated with a single space.
In the next line, there will be `B` numbers within `[1, N]`, each representing a broken traffic light, separated by a space.
For each test case, output the **minimum number** of traffic lights that needs to be fixed so there are `K` consecutive working traffic lights.

## Examples

### Input

```rs
2
4 3 3
1 4 3
10 6 5
2 10 1 5 9
```

### Output

```rs
2
1
```

### Explanation

#### For example #1

`B W B B` (`W` = working, `B` = broken)  
since `K = 3`, fixing `3rd` and `4th` lights (or `1st` and `3rd`) will result in `3` consecutive `W`s.

#### For example #2

`B B W W B W W W B B`  
since `K = 6`, fixing just the `5th` light will satisfy the requirements.

**Beyond the challenge**  
There is an `O(N)` solution. Can you find it?

Challenge suggested by @SnowballSH

## Submissions

Code can be written in any of these languages:

- `Python` 3.10
- `C/C++` (GCC 10.3)
- `Ruby` 3.1
- `Golang` 1.16
- `Java` 18 (Open JDK)
- `Rust` 1.58
- `C#` 10 (.Net 6.0)

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/PreviousChallenges/Challenge_93)
