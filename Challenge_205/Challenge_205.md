# Challenge 205: Minimum Number After Removal, Part 2

**Difficulty: 4/10  
Labels: Greedy, Stacks**

Hethat has a large number represented by a sequence of digits. He wants to erase `k` of the digits so that the remaining digits form the smallest possible number in the same order. Can you help find find the smallest possible number after at most `k` digits are erased from the number?

For the purposes of this challenge, if there are no digits left, we interpret the number as 0. If the resulting number has leading zeroes, do not output leading zeroes in your answer.

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The only line contains two integers `n` and `k`.

Output a single integer, the smallest integer that can be obtained by removing **at most** `k` digits from `n`.

**Note that because `n` is very large, you are recommended to view `n` as a string of characters when taking input!**

### Examples

#### Input

```rust
10
1432219 3
10200 1
10 2
1892041 3
1 1
49534552563074878185 5
14540861491327603694 7
12829536814893230746 10
91563934677465826111 14
82129410213673260299 17
```

#### Output

```rust
1219
200
0
1041
0
342563074878185
141327603694
1143230746
126111
2
```

### Note

- `1 <= T`
- `1 <= k <= n <= 10`<sup>`(10`<sup>`4`</sup>`)`</sup>

Challenge idea: hethat

### Submissions

Code can be written in any of these languages:

- `Python` 3.11
- `C` (gnu17) / `C++` (c++20) - GCC 12.2
- `Ruby` 3.2
- `Golang` 1.21
- `Java` 19 (Open JDK) - use **"class Main"!!!**
- `Rust` 1.72
- `C#` 11 (.Net 7.0)
- `JavaScript` ES2023 (Node.js 20.6)

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_205)
