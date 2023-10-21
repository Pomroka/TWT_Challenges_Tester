# Challenge 178: Pal

**Difficulty: 2/10  
Labels: Strings**

You have a box of palindromes. A palindrome is a string that reads the same forwards as backwards. Unfortunately, they are lonely and need to find pals.
Given a palindrome, how many palindromes can be created by permuting its characters?

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The first line contains a string `S`. `S` is guaranteed to be a palindrome.

Output a single integer, **modulo 10<sup>9</sup> + 7**, the number of palindromes among all permutations of `S`.

### Examples

#### Input

```rust
6
tacocat
aabccbaa
gg
eeerrreee
bbaaarriereirraaabb
abcdefghijklmnopqrstuvwxyzyxwvutsrqponmlkjihgfedcba
```

#### Output

```rust
‌6
12
1
4
15120
440732388
```

- For test case 1, the six permutations are `tacocat`, `tcaoact`, `ctaoatc`, `catotac`, `atcocta`, `actotca`.
- For test case 4, the four permutations are `eeerrreee`, `eerereree`, `ereereere`, `reeereeer`.

### Note

- `1 <= T`
- `1 <= |S| <= 1000`

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

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_178)
