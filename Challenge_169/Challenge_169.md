# Challenge 169: New York Sequence

**Difficulty: 2/10  
Labels: Implementation, Mathematics**

Tim recently discovered an interesting sequence called the **New York Sequence** (the name is fictional for the purpose of this challenge).
The sequence starts with the integer 1. The New York Sequence is obtained by repeatedly adding 1 to the previous term and then doubling it. For example:

```rust
1 -> add 1 -> 2 -> double => 4
4 -> add 1 -> 5 -> double => 10
10 -> add 1 -> 11 -> double => 22
...
```

Thus, the sequence starts with `NYS = 1, 4, 10, 22, 46, 94, ...`. Where 1 is the 1st term, 4 is the 2nd term, etc.
Tim challenges you. He gives you an integer of his choice; let it be `x`.
If `x` is an term of the New York Sequence, output its position in the sequence. For example, if `x = 22`, then you would output `4` as 22 is the 4th term in NYS.
Otherwise (if `x` is not a term in NYS), output `-1`.

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The only line contains an integer `x`.

If `x` is a term of NYS, output its position. Otherwise, output `-1`.

### Examples

#### Input

```rust
7
22
5
1
128
25165822
98302
393215
```

#### Output

```rust
4
-1
1
-1
23
15
-1
```

For testcase 4, 128 is not a term in NYS. The two terms around it are 94 and 190.

### Note

- `1 <= T`
- `1 <= x <= 10`<sup>`18`</sup>
- If you are using a compiled language, you should use an 64-bit integer (such as `long long` in C++) to avoid integer overflow.
- Credit: 1989 NYSML

### Extra Practice

Construct a mathematical formula.

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

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_169)
