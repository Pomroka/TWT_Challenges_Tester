# Challenge 152: Lazy Spelling

**Difficulty: 1/10  
Labels: Implementation**

Tim recently realized some words like `"localization"` or `"internationalization"` are so long that writing them many times in one text is quite tiresome.

Let's consider a word too long, if its length is strictly more than 10 characters. All too long words should be replaced with a special abbreviation.

This abbreviation is made like this: we write down the first and the last letter of a word and between them, we write the number of letters between the first and the last letters. That number is in decimal system and doesn't contain any leading zeroes.

Thus, `"localization"` will be spelled as `"l10n"`, and `"internationalization"` will be spelled as `"i18n"`.

At that all too long words should be replaced by the abbreviation and the words that are not too long should not undergo any changes.

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The only line contains a string `S`.

Output the abbreviated version of `S`, as described above.

### Examples

#### Input

```rust
6
word
localization
internationalization
pneumonoultramicroscopicsilicovolcanoconiosis
techandtim
techwithtim
```

#### Output

```rust
‌word
l10n
i18n
p43s
techandtim
t9m
```

### Note

`1 <= T`
`1 <= |S| <= 500`
all letters are lowercase english alphabets (`a-z`).

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

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_152)
