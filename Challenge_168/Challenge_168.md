# Challenge 168: Sandwich Strings

**Difficulty: 2/10 (4/10 for extra challenge)  
Labels: String Searching, Brute-force**

Tim recently realizes that a lot of strings look like a sandwich, where two of the same sequence of letters (the **bread**) contains another sequence of letters in the middle (the meat). For example, the word `eraser` can be seen as a sandwich of `as` in the middle of two pieces of `er`. The word `educated` can be seen as a sandwich of `ucat` in the middle of two pieces of `ed`.
Note that breads cannot overlap - for example, the longest bread for `asasa` would be `a`.

Given a list of strings, help Tim find the maximum possible length of a **bread** in each of them.

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The only line contains a string `S`.

Output a single integer, the maximum length of a **bread** in `S`. In other words, output the maximum value of `n` **<= |S| / 2** such that the sequence of the first `n` letters in `S` is the same as the sequence of the last `n` letters in `S`.
If no such value is possible, output `0`.
Note from above that the answer should be less than or equal to half the length of the string.

### Examples

#### Input

```rust
5
eraser
abcababcab
apple
asasa
sssssss
```

#### Output

```rust
2
5
0
1
3
```

### Note

- `1 <= T`
- `1 <= |S| <= 10`<sup>`3`</sup>
- All characters in `S` are lowercase English alphabets `a-z`.

#### Extra Challenge (not tested)

- `1 <= |S| <= 10`<sup>`6`</sup>

### Submissions

Code can be written in any of these languages:

- `Python` 3.10
- `C` (gnu17) / `C++` (c++20) - GCC 11.2
- `Ruby` 3.1
- `Golang` 1.19
- `Java` 19 (Open JDK) - use **"class Main"!!!**
- `Rust` 1.68.2
- `C#` 10 (.Net 6.0)
- `JavaScript` ES2022 (Node.js 18.10)

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_168)
