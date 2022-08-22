# Challenge 117: Diamond Showcase, Part II

**Difficulty: 1/10**  
Alex received a case containing a diamond from a friend. However, to prevent it being stolen by anyone else, his friend put a random string of letters on the case, and a lock. The password to the lock is the number of times Alex's favorite letter appears in the string (only Alex and his friend know what this letter is!).

However, Alex is too lazy to count. Help Alex find the password to the lock.

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The first line contains a string of lowercase English Alphabets, call it `S`.
- The second line contains a single lowercase English Alphabet, call it `A`.

Output the number of times `A` appears in `S`.

### Examples

#### Input

```rust
5
aabcdd
a
abcd
c
zazazaz
z
asdfowrgihdsnoqerfoeuwthpassieh
f
abcdefghijklmnpqrstuvwxyz
o
```

#### Output

```rust
2
1
4
2
0
```

#### Note

`'a' <= S[i] <= 'z'`
`'a' <= A <= 'z'`
`1 <= |S| <= 10`<sup>`5`</sup>

### Submissions

Code can be written in any of these languages:

- `Python` 3.10
- `C/C++` (GCC 10.3)
- `Ruby` 3.1
- `Golang` 1.18
- `Java` 18 (Open JDK) - use "class Main"!!!
- `Rust` 1.62
- `C#` 10 (.Net 6.0)
- `JavaScript` ES2022 (Node.js 18.2)

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/PreviousChallenges/Challenge_117)
