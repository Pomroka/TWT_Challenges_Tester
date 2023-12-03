# Challenge 183: Fourier's Swappy Strings

**Difficulty: 6/10  
Labels: Strings, DFS**

Your physics professor, Prof. Fourier, loves to perform an operation on two strings `a` and `b` of equal length. He calls this **operation** "swappy." First, he chooses two characters `c1` and `c2`. Then, he replaces every instance of `c1` in `a` with `c2`, and replaces every instance of `c1` in `b` with `c2` as well.

Let's denote the **distance** between strings `a` and `b` as the **minimum number of "swappy" operations** required to make these strings equal.
For example, if the two strings are `abcd` and `ddcb`, the distance between the two strings is 2 — we may replace every occurrence of `a` with `b`, so `abcd` becomes `bbcd`, and then we may replace every occurrence of `b` with `d`, so both strings become `ddcd`.

Prof. Fourier received two strings `A` and `B` from each of his students. For every substring of `A` consisting of `|B|` characters, determine the distance between this substring and `B`.

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The first line contains the string `A`,
- the second contains the string `B`.

Both strings consist of only lowercase Latin letters from `a` to `f`.

Print `|A| - |B| + 1` integers, separated by single spaces. The `i`<sup>`th`</sup> of these integers must be equal to the distance between the substring of `S` beginning at `i`<sup>`th`</sup> index with length `|B|` and the string `B`.

### Examples

#### Input

```rust
4
abcdefa
ddcb
abccba
bcc
abcfedcfaebcadfe
cafe
fff
eee
```

#### Output

```rust
‌2 3 3 3
2 0 1 2
4 2 3 4 3 3 1 3 3 4 4 2 2
1
```

### Note

`|S|` denotes the length of string `S`.
`1 <= T`
`1 <= |B| <= |A| <= 10`<sup>`5`</sup>
`(|A| - |B|)(|B|) <= 10`<sup>`7`</sup>
`A` and `B` only contain characters from `abcdef`.
This challenge is hard - let us know if you need more time!

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

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_183)
