# **Challenge 154: Frequency**

**Difficulty: 2/10  
Labels: Data Structures, Implementation**

SnowballSH has some strings, but they are all corrupted by one (or more) letters that appear very frequently. SnowballSH hates letters that appear frequently, so he asks you to remove the most frequent letters from his strings.

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The only line contains a string `s`.

Output `"#"` followed by a new string, that is `s` with the letter with the highest frequency (occurs the most) removed. If there are multiple letters with the same highest frequency, remove all of them.

### Examples

#### Input

```rust
‌4
apple
techwithtim
aaaabaaabaz
easy
```

#### Output

```rust
‌#ale
#echwihim
#bbz
#
```

- For test case 1, `p` appears twice in "apple", which is the most frequent.
- For test case 4, all 4 letters have the same frequency, so remove all of them.

### Note

- `1 <= T`
- `1 <= |s| <= 1,000`
- `s` only contains lowercase English alphabets.

Extra constraints (won't be tested): `1 <= |s| <= 10`<sup>`6`</sup>

### Submissions

Code can be written in any of these languages:

- `Python` 3.10
- `C` (gnu17) / `C++` (c++20) - GCC 11.2
- `Ruby` 3.1
- `Golang` 1.19
- `Java` 19 (Open JDK) - use "class Main"!!!
- `Rust` 1.68.2
- `C#` 10 (.Net 6.0)
- `JavaScript` ES2022 (Node.js 18.10)

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_154)
