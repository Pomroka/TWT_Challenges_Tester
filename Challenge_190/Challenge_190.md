# Challenge 190: Counting Letters

**Difficulty: 1/10  
Labels: Strings**

Tim's custom computer system hates strings, so all characters has to be converted to an integer before one feeds them into the computer. Tim decides to label `A=1`, `B=2`, `C=3`, `...`, `Y=25`, `Z=26`. For example, the string `"APPLE"` would be converted to `{1, 16, 16, 12, 5}`.

Tim's computer system then adds up the distinct numbers representing vowels (`aeiou`) and outputs the sum; it then adds up the distinct numbers representing consonants and outputs the second sum.

Obviously, this kind of computer system was nonexistent over 20 years ago. However, Tim wants to recreate this program. Please help him recreate this computer system.

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The only line contains a string `S` containing uppercase English alphabets A-Z.

Output **two integers**, separated by a single space, **the sum of numbers representing distinct vowels** and **the sum of numbers representing distinct consonants**.

### Examples

#### Input

```rust
‌5
APPLE
TECHWITHTIM
ILOVECOMPUTERSCIENCE
ZZZZZZZZ
THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG
```

#### Output

```rust
6 28
14 67
50 137
0 26
‌51 300
```

- For test case 1, the vowels are `1 + 5 = 6`, and the consonants are `16 + 12 = 28`.
- For test case 5, it is clear that every alphabet is used, so the sum of both should be `1 + 2 + 3 + ... + 26 = (26)(13) = 351``, which is indeed equal to `51 + 300`.

### Note

- `1 <= T`
- `1 <= |S| <= 10,000`

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

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_190)
