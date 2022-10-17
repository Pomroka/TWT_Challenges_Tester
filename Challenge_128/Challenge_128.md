# Challenge 128: ACGT, Part 1

**Difficulty: 2/10
Labels: While Loop**

Banik is studying DNA in his biology class. He learned that there are four types of bases in DNA, `A`, `C`, `G`, and `T`. Banik loves the letter `A`, therefore he wants to find out the longest sequence of `A`'s in a DNA. Can you help him out?

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The first line contains a string `S`. We say a substring is a "sequence of `A`'s" if and only if all characters in the string are the character `A`.

    For example, `AAAAA` and `A` are sequences of `A`'s, while `AAAAT`, `AGAA`, and `C` are not.

Output the length of the longest sequence of `A`'s among all substrings of `S`. That is, in other words, the maximum length of repeating `A`'s in `S`.
If there is no `A` in `S`, output `0`.

### Examples

#### Input

```rust
4
A
AAGAGCCT
GAACAAAAGTACGAAA
TTCGTCGT
```

#### Output

```rust
1
2
4
0
```

For test case 1, there is only `1` `A`.
For test case 2, the longest sequence is `AA`, `2` As.
For test case 3, the longest sequence is `AAAA`, `4` As.
For test case 4, there is no character `A` in the string, therefore output `0`.

#### Note

`1 <= T`
`1 <= |S| <= 10`<sup>`6`</sup> (where `|S|` means the length of string `S`)
`S` only contains characters `A`, `C`, `T`, and `G`

### Submissions

Code can be written in any of these languages:

- `Python` 3.10
- `C` (gnu17) / `C++` (c++20) - GCC 11.2
- `Ruby` 3.1
- `Golang` 1.19
- `Java` 19 (Open JDK) - use **"class Main"!!!**
- `Rust` 1.64
- `C#` 10 (.Net 6.0)
- `JavaScript` ES2022 (Node.js 18.10)

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_128)
