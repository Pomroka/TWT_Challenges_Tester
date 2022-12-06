# Challenge 135: Word Cube

**Difficulty: 2/10
Labels: Sets**

Alex just received an anonymous, mysterious package that consists of unlimited identical wooden cubes. The cube has `6` sides, each has a letter written on it. What words can Alex spell with those `6` letters?

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The first line contains a string of `6` uppercase English alphabets, the letters written on the wooden blocks.
- The second line contains an integer `Q`.
- The next `Q` lines each contain one word.

Output the total length of all words that can be spelled with the given wooden block (`6` alphabets).

### Examples

#### Input

```rust
2
EGAXYZ
4
EGG
AGE
PEA
AEGEAEE
TWSUAL
4
TWTWTWTWT
USAUSA
ALTERS
L
```

#### Output

```rust
13
16
```

For test case **1**, `EGG`, `AGE`, and `AEGEAEE` can be spelled. The lengths are respectively `3`, `3`, and `7`, output the sum which is `13`.

### Note

`1 <= T`
`1 <= Q <= 1000`
`1 <= length of each word <= 100`
All letters will be within `A-Z`. The first line of each test case always contains `6` of those letters, each **unique**.

### Submissions

Code can be written in any of these languages:

- `Python` 3.10
- `C` (gnu17) / `C++` (c++20) - GCC 11.2
- `Ruby` 3.1
- `Golang` 1.19
- `Java` 19 (Open JDK) - use "class Main"!!!
- `Rust` 1.64
- `C#` 10 (.Net 6.0)
- `JavaScript` ES2022 (Node.js 18.10)

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_135)
