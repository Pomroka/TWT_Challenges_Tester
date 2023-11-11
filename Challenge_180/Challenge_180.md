# Challenge 180: Lucky Numbers

**Difficulty: 2/10  
Labels: None**

TechWithTimia recently launched the production of personal starships. Now everyone on Mars can buy one and fly to other planets inexpensively.

Each starship has a number — some positive integer `𝑥`. Let's define the luckiness of a number `𝑥` as the difference between the largest and smallest digits of that number. For example, `142857` has `8` as its largest digit and `1` as its smallest digit, so its luckiness is `8−1=7`. And the number `111` has all digits equal to `1`, so its luckiness is zero.

Tim is a famous Martian blogger who often flies to different corners of the solar system. To release interesting videos even faster, he decided to buy himself a starship. When he came to the store, he saw starships with numbers from `𝑙` to `𝑟` inclusively. While in the store, Tim wanted to find a starship with the luckiest number.

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The only line contains two integers, `𝑙` and `𝑟`, separated by a single space.

Output a single integer, the luckiest number between `𝑙` and `𝑟`. If there are multiple answers, output the smallest one.

### Examples

#### Input

```rust
7
59 63
42 49
15 15
53 57
1 100
1000 2023
188 881
```

#### Output

```rust
‌60
49
15
53
90
1009
190
```

### Note

- `1 ≤ T`
- `1 ≤ l ≤ r ≤ 10`<sup>`6`</sup>

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

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_180)
