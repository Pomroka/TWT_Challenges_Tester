# Challenge 162: SnowballSH and Parties

**Difficulty: 3/10**  
**Labels: Greedy**

It's party season! SnowballSH has a lot of friends, and they are hosting parties of various durations at various times. Unfortunately, many of them overlap. SnowballSH wants to go to as many parties as possible. To not disappoint his friends, SnowballSH will not leave in the middle of a party. Given the start and end times of all parties, what is the maximum number of parties he can attend?

## Task

You are given a number `T` and `T` testcases follow, for each testcase:

- The first line contains an integer, `N`, the number of parties.
- `N` lines follow. For each line, there are two integers `a` and `b`, separated by a single space. This represents a party starting at time `a` and ending at time `b`, inclusively.

Assuming SnowballSH does not take any time to get from one party to another, output an integer, the maximum number of parties SnowballSH can attend.

### Examples

#### Input

```rust
2
3
4 9
3 5
5 8
3
3 4
5 6
7 8
```

#### Output

```rust
‌2
3
```

- For testcase 1, SnowballSH can attend parties `2` and `3`. If he attends party `1` he would have to miss other parties.

## Note

- `1 <= T`
- `1 <= N <= 5,000`
- `1 <= a <= b <= 10`<sup>`8`</sup>

## Submissions

Code can be written in any of these languages:

- `Python` 3.10
- `C` (gnu17) / `C++` (c++20) - GCC 11.2
- `Ruby` 3.1
- `Golang` 1.19
- `Java` 19 (Open JDK) - use **"class Main"!!!**
- `Rust` 1.68.2
- `C#` 10 (.Net 6.0)
- `JavaScript` ES2022 (Node.js 18.10)

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_162)
