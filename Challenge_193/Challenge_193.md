# Challenge 193: Number Formatting

**Difficulty: 2/10  
Labels: String Searching, Regex**

Tim noticed that when a number is too long, it is impossible to read. For example, Tim found it difficult to compare `1000000000000` and `5358523495841`.

We can solve this issue by splitting the number with a comma every three digits from the right. For example, the above numbers would be written as `1,000,000,000,000` and `5,358,523,495,841`. Now it is clear that the latter is larger.

Tim requests you to write a program to automatically convert all numbers in a sentence to this form.

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The only line contains a string `S`. `S` contains words separated by a single space. Each word is either all lowercase English alphabets (`a-z`) or all digits (`0-9`). The first digit of any number will **not** be `0`.

Output a string, where each all-digit word is converted to the more readable form described above.

### Examples

#### Input

```rust
4
china has a population of 1425316371 people
101 the product of 1234 and 987654321 is equal to 1218765432114
this sentence has no numbers
1 12 123 1234 12345 1234 123 12 1
```

#### Output

```rust
china has a population of 1,425,316,371 people
101 the product of 1,234 and 987,654,321 is equal to 1,218,765,432,114
this sentence has no numbers
1 12 123 1,234 12,345 1,234 123 12 1
```

### Note

`1 <= T`
`1 <= |S| <= 1,000`

### Submissions

Code can be written in any of these languages:

- `Python` 3.11
- `C` (gnu17) / `C++` (c++20) - GCC 12.2
- `Ruby` 3.2
- `Golang` 1.21
- `Java` 19 (Open JDK) - use **"class Main"!!!**
- `Rust` 1.72
- `C#` 11 (.Net 7.0)
- `JavaScript` ES2023 (Node.js 20.6)This challenge will have a duration of 1.5 weeks, due Mar 31st.

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_193)
