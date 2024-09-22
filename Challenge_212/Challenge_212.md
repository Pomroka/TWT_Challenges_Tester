# Challenge 212: Coding

**Difficulty: 3/10  
Labels: Implementation, Greedy**

SnowballSH really enjoys coding. He has a string `s` of lowercase Latin alphabets. SnowballSH wants to calculate the *beauty score* of this string.

He scans `s` from left to right. He searches for the letter `c`, followed by `o`, `d`, `i`, `n`, and `g`. When he finds all six letters `coding`, these six letters are all **crossed off.** Note that he only crosses them off when all six letters are found. Then, he resumes searching for `c` again. SnowballSH never looks back and only continues where he left off.

Then, `score_used` is the number of **crossed off** letters in `s`. `score_unused` is the number of letters that is one of `c`, `o`, `d`, `i`, `n`, or `g`, in `s` that **are not crossed off**.

The *beauty score* of `s` is `score_used - score_unused`.

Given a string `s`, can you help SnowballSH find its *beauty score*?

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The only line contains a string `s`.

Output a single integer, the *beauty score* of `s`.

### Examples

#### Input

```rust
7
ccooddiinngg
codincodincodinggcod
ilovecodingalot
techwithtim
actofdangeringaragecomputerspudding
oding
letters
```

#### Output

```rust
0
-8
3
-3
8
-5
0
```

- For the first test case, the bolded letters are crossed off: **c**c**o**o**d**d**i**i**n**n**g**g, so the answer is 6 - 6 = 0.
- For the third test case, the underlined letters are not one of `coding` (so not counted): i~~l~~o~~ve~~**coding**~~al~~o~~t~~, so the answer is 6 - 3 = 3.

### Note

`1 <= T`
`1 <= |s| <= 10`<sup>`5`</sup>
All characters in `s` are lowercase Latin alphabets.

### Submissions

Code can be written in any of these languages:

- `Python` 3.11
- `C` (gnu17) / `C++` (c++20) - GCC 12.2
- `Ruby` 3.3.4
- `Golang` 1.21
- `Java` 19 (Open JDK) - use **"class Main"!!!**
- `Rust` 1.72
- `C#` 11 (.Net 7.0)
- `JavaScript` ES2023 (Node.js 20.6)
- `Zig` 0.13.0

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_212)
