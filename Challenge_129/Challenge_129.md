# Challenge 129: ACGT, Part 2

**Difficulty: 2/10
Labels: Basic String Operations**

Banik's professor gave him a sequence of DNA. Since the professor loves palindromes, he asks Banik if he can add ONE letter to the end of the sequence to make it a palindrome. Can you help him out?

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The first line contains a string `S`.

We call a string `P` a palindrome if and only if `P` reads the same forward as it is read backwards. For example, `ACGTGCA`, `CGGC`, and `T` are palindromes, while `ACGT` and `GTA` are not.

Determine whether it is possible to make `S` a palindrome by adding a character at the end of `S`. If it is possible, print the character added. If it is not possible, print `!`.

### Examples

#### Input

```rust
5
AGCG
TGC
TT
C
CTC
```

#### Output

```rust
A
!
T
C
!
```

For test case `1`, adding `A` to the end would make the string `AGCGA`, a palindrome.
For test case `2`, it is impossible to make `TGC`? A palindrome with any choice of ?.
For test case `4`, adding `C` to the end makes the string `CC`, a palindrome.
For test case `5`, although `CTC` is already a palindrome, we are forced to add a new character which makes a palindrome impossible here.

#### Note

`1 <= T`
`1 <= |S| < 10`<sup>`5`</sup> (where `|S|` means the length of string `S`)
All characters in `S` will be one of the following: `A`, `C`, `G`, or `T`.
It can be shown that the answer for each test case will always be one of the following `5` characters: `A`, `C`, `G`, `T`, `!`.

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

Recommended Time Complexity for each test case: `O(|S|)`

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_129)
