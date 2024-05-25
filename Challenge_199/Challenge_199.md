# Challenge 199: Friendly Password

**Difficulty: 3/10  
Labels: Strings**

Three friends, Tim, Avib, and Sylte meet together to create a strong password for the admin account on their ongoing project.

Three of them have many common hobbies, each denoted by a string of characters. To remember their friendship forever, they want to include the name of a hobby, denoted as the string `h`, in the password.

Avib proposes that `h` should occur at the beginning of the password `s` as a prefix. Sylte proposes that `h` should occur at the end of `s` as a suffix. Tim proposes that `h` should occur neither in the beginning nor at the end of `s` so that it occurs as a substring in the middle of the string `s`.

After a week of brainstorming, they come up with a password `s` that hopefully satisfies all three of their proposals. Can you find the longest possible name of their hobby?

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The only line contains a string `s`.

Output a string, the **longest** string `h` such that

- `h` is a prefix of `s`,
- `h` is a suffix of `s`, and
- `h` is a substring of `s` neither as a prefix nor as a suffix.

If no string `h` exists, output the sad face `:(`

### Examples

#### Input

```rust
9
fixprefixsuffix
abcdabc
girafarig
ghghghgxghghghg
twtwt
twtwtwt
xx
yyy
zzzz
```

#### Output

```rust
‌fix
:(
:(
ghghg
t
twt
:(
y
zz
```

- For test case 1, the string `fix` occurs at the beginning, end, and middle.
- For test case 2, there is no string `h` that satisfies all three proposals.

### Note

- `1 <= T`
- `1 <= |s| <= 500`
- O(N<sup>3</sup>) solutions will be accepted.

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

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_199)
