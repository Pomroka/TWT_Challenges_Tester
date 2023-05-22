# Challenge 158: Palindrome Test

**Difficulty: 2/10**  
**Labels: Implementation**

Tim loves palindromes. He has a whole list of words, and wonders whether he can change at most one letter to make them palindromes. Can you help him?
A palindrome is a string that reads the same forwards as backwards.

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The only line contains a string `S`.

If it is possible to change **at most one letter** to make it a palindrome, output `YES`. Otherwise, output `NO`.  
**Note** that you can choose to not change anything at all.

### Examples

#### Input

```rust
‌4
tacobat
techwithtim
abra
reviver
```

#### Output

```rust
‌YES
NO
YES
YES
```

- For test case 1, we can change `c` to `b` or `b` to `c`, resulting in `tabobat` or `tacocat`.
- For test case 2, it is impossible to obtain a palindrome by changing at most one letter.

### Note

- `1 <= T`
- `1 <= |S| <= 2,000` where `|S|` denotes the length of `S`.
- `S` only contains lowercase English alphabets `a-z`.

<details>
<summary><b>Hint</b></summary>
Count the number of different letters when reading forward and backward.
</details>

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

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_158)
