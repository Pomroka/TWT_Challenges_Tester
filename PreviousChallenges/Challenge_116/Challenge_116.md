# Challenge 116: Diamond Showcase (Part I)

**Difficulty: 3/10**  
Alex likes to collect diamonds, and he enjoys putting them in a case and showing it to his friends.

Alex just obtained a lot of diamonds from his friend as birthday gift, and they are in different sizes. However, Alex only wishes to display a case of diamonds if all the diamonds in the case are of the exact same size. Alex also prefers larger diamonds over smaller ones, but quantity comes before it.

Help Alex determine the maximum number of diamonds he can put in a case and the size of each diamond.

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The first line contains `N`, the number of diamonds Alex has.
- The next line contains `N` integers (call them `D`) separated by a single space, where each `D[i]` represents the size of diamond `i`.

Output `x y` where `x` is the maximum number of diamonds Alex can put in a case and `y` is the size of each diamond in it. If multiple different cases of the maximum size exist, output `y` with the maximum value. _(Formally, Alex can only put the set of diamonds `K` in a case if every `K[i]` is equal to every `K[j]`)_

### Examples

#### Input

```rust
5
3
1 2 2
4
3 8 8 3
8
3 9 5 9 9 3 77 77
1
123454321
5
9 9 9 9 9
```

#### Output

```rust
2 2
2 8
3 9
1 123454321
5 9
```

For the second test case, `3 3` and `8 8` are two valid cases both with size `2`, however since Alex prefers larger diamonds, we output `8 `instead of `3`.
For the third test case, `3 3`, `5`, `9 9 9`, `77 77` are four valid cases, but `9 9 9` has the maximum number of items (`3`) so we output `3 9`.

### Note

`1 ≤ T`
`1 ≤ N ≤ 10`<sup>`6`</sup>
`1 ≤ D[i] ≤ 10`<sup>`16`</sup>

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

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/PreviousChallenges/Challenge_116)
