# Challenge 148: Shopping (Part 2)

**Difficulty: 2/10  
Labels: Implementation**

Tim continues to shop for himself. A messy shelf contains N items, and the type of each item is labelled with a lowercase letter. Tim wants to buy and pack as many groups of gifts (say, `"abc"`) but only wishes to buy a multiple of the entire group (for example, he won't buy `"ab"` or `"aabc"`, but he will buy `"aabbcc"`). What is the maximum number of groups he can buy?

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The first line contains two integers, `N` and `K`.
- The second line contains a string of `N` characters, the shelf.
- The third line contains a string of `K` characters, Tim's desired group of gifts.

Output the maximum number of groups Tim can buy from the shelf, if he has to buy a multiple of the entire group.

### Examples

#### Input

```rust
3
8 3
abbcabcc
abc
11 2
techwithtim
ti
5 1
vwxyz
u
```

#### Output

```rust
2
2
0
```

For the first test case, Tim can buy a maximum of two groups of `"abc"`.  
For the third test case, Tim cannot find `"u"` anywhere on the shelf, so the answer is `0`.

### Note

- `1 <= T`
- `1 <= N <= 10,000`
- `1 <= K <= 26`
- All characters in both strings are lowercase English alphabets, `a-z`.
- All characters in the second string are distinct (but not necessarily for the first string).

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

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_148)
