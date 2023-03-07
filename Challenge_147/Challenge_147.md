# Challenge 146: Shopping (Part 1)

**Difficulty: 1/10  
Labels: None**

**This is Part 1 of a series of four similar problems. The difficulty will grow in the order of 1-2-4-7.**

Tim is shopping at a grocery store and found Avib's favourite candy. Yesterday, Avib told Tim that he would like Tim to buy him `N` pieces of such candy.
Each piece of candy costs `C` cents. Fortunately for Tim, there is a promotion event going on at the store! It reads: "Buy one, get one free for any item." Help Tim determine how much money he needs to pay to buy the candy for Avib.

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The only line contains two integers, `N` and `C`, separated by a single space.
    `N` is the number of pieces of candy Avib wants, and `C` is the cost of each piece of candy, in cents.

With the promotion "Buy One, Get One Free" event going on, output a single integer, the minimum number of cents Tim needs to pay in total to satisfy Avib's request.

### Examples

#### Input

```rust
6
4 3
33 7
7 33
230306 11
0 100
100 0
```

#### Output

```rust
6
119
132
1266683
0
0
```

- For test case 1, Tim needs to buy `4` candies where each costs `3` cents. Since he can buy one, get one free, he only needs to pay for `2` candies, paying `2 * 3 = 6` cents.
- For test case 2, Tim needs to buy `33` candies where each costs `7` cents. Paying for `16` candies only gives him `32` after the promotion, so he needs to buy one more, paying `17 * 7 = 119` cents.
- For test case 5, since Tim doesn't need to buy any candy, the cost is `0`.
- For test case 6, since candy is free, the cost is also `0`.

### Note

`1 <= T`
`0 <= N <= 10`<sup>`9`</sup>
`0 <= C <= 10`<sup>`9`</sup>
`N * C <= 10`<sup>`9`</sup>

### Submissions

Code can be written in any of these languages:

- `Python` 3.10
- `C` (gnu17) / `C++` (c++20) - GCC 11.2
- `Ruby` 3.1
- `Golang` 1.19
- `Java` 19 (Open JDK) - use **"class Main"!!!**
- `Rust` 1.64
- `C#` 10 (.Net 6.0)
- `JavaScript` ES2022 (Node.js 18.10)

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_147)
