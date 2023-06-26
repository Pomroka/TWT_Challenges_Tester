# Challenge 163: Leading Vowels

**Difficulty: 2/10  
Labels: Strings, Sets**

Tim has a strange friend who believes that encrypting messages by adding random vowels at the beginning of the messages is effective. As a result, Tim receives hundreds of messages with random leading vowels from him every day. Can you help him "decipher" the messages?

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The only line contains a string `S`.

A letter is a vowel if it is `a`, `e`, `i`, `o`, or `u`. Output `S` with leading vowels removed.

### Examples

#### Input

```rust
‌4
eeeeeehello
howareyou
ogoodbyeeeee
aeiouy
```

#### Output

```rust
‌hello
howareyou
goodbyeeeee
y
```

### Note

- `1 <= T`
- `1 <= |S| <= 2,000`
- `S` only contains lowercase English alphabets `a-z`.
- `S` contains at least one consonant (non-vowel).

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

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_163)
