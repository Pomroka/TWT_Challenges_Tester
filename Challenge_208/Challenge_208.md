# Challenge 208: Range XOR Queries

**Difficulty: 5/10  
Labels: Implementation, Prefix Arrays, Bitwise Operations**

SnowballSH has a list of positive integers `a`<sub>`1`</sub>`, a`<sub>`2`</sub>`, ..., a`<sub>`n`</sub>. His Computer Science professor gave him many intervals `[l, r]` and asked him to find `a`<sub>`l`</sub>` ^ a`<sub>`(l+1)`</sub>` ^ ... ^ a`<sub>`r`</sub>, where `^` denotes the [XOR](https://en.wikipedia.org/wiki/Bitwise_operation#XOR) operator. In other words, the professor asked SnowballSH to find the XOR of every number within each given interval.

SnowballSH is too lazy to do this by hand. Can you help him?

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The first line contains two integers `n` and `q`, separated by a single space. `n` is the length of the list, and `q` is the number of queries SnowballSH has to answer.

- The second line contains `n` integers `a`<sub>`1`</sub>`, a`<sub>`2`</sub>`, ..., a`<sub>`n`</sub>`, separated by a single space, SnowballSH's list of integers.

- The next `q` lines each contain two integers `l` and `r`, denoting the 1-based indices of the left and right sides of the interval, requesting the XOR of all integers in the interval `[l, r]` from `a`.

Output a list of `q` integers, separated by a single space, the answer to the `q` queries in order.

### Examples

#### Input

```rust
3
8 4
3 2 4 5 1 1 5 3
2 4
5 6
1 8
3 3
2 3
20 24
1 1
1 2
2 2
14 5
2 1 7 1 8 2 8 1 8 2 8 4 5 9
1 13
2 14
4 11
6 8
7 7
```

#### Output

```rust
3 0 6 4
20 12 24
5 14 0 11 8
```

For the first test case, the first query asks for the XOR of numbers in the list `[2,4,5]`, or `2^4^5`, which is equal to 3; the 4th query asks for the XOR of numbers in the list `[4]`, which is just 4.

### Note

- `1 <= T`
- `1 <= n <= 10`<sup>`5`</sup>
- `1 <= q <= 10`<sup>`5`</sup>
- `1 <= a`<sub>`i`</sub>` <= 10`<sup>`8`</sup>
- `1 <= l <= r <= n`

### Submissions

Code can be written in any of these languages:

- `Python` 3.11
- `C` (gnu17) / `C++` (c++20) - GCC 12.2
- `Ruby` 3.3.4
- `Golang` 1.21
- `Java` 19 (Open JDK) - use **"class Main"!!!**
- `Rust` 1.72
- `C#` 11 (.Net 7.0)
- `JavaScript` ES2023 (Node.js 20.6)
- `Zig` 0.13.0

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_208)
