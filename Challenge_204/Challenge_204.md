# Challenge 204: Minimum Number After Removal, Part 1

**Difficulty: 2/10  
Labels: Greedy**

Hethat has a large number represented by a sequence of digits. He wants to erase one of the digits so that the remaining digits form the smallest possible number in the same order. Can you help find the smallest possible number after at most one digit are erased from the number?

For the purposes of this challenge, if there are no digits left, we interpret the number as 0. If the resulting number has leading zeroes, do not output leading zeroes in your answer.

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The only line contains an integer `n`.

Output a single integer, the smallest integer that can be obtained by removing **at most one** digit from `n`.

**Note that because `n` is very large, you are recommended to view `n` as a string of characters when taking input!**

### Examples

#### Input

```rust
8
1
31415
1357924680
1110111
1111111
987654321
100000001
23345566641349569492452457602452
```

#### Output

```rust
0
1415
135724680
110111
111111
87654321
1
2334556641349569492452457602452
```

### Note

- `1 <= T`
- `1 <= n <= 10`<sup>`(10`<sup>`4`</sup>`)`</sup>

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

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_204)
