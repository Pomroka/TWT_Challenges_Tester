# Challenge 144: Party

**Difficulty: 5/10  
Labels: Tree**

A company has `n` employees numbered from `1` to `n`. Each employee either has **no** immediate manager or **exactly one** immediate manager, who is another employee with a different number. An employee `A` is said to be the superior of another employee `B` if `A` is the immediate manager of `B`, or if there exists an employee `C` such that `A` is the superior of `C` and `C` is the superior of `B` (transitive).

The company will not have a managerial cycle. That is, there will not exist an employee who is the superior of his/her own immediate manager.

Today the company is going to arrange a party. This involves dividing all `n` employees into several groups: every employee must belong to exactly one group. Furthermore, within any single group, there must not be two employees `A` and `B` such that `A` is the superior of `B`.

What is the minimum number of groups that must be formed?

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The first line contains an integer `N`.
- The next line contains `N` integers `P`, separated by a single space. `P[i]` denotes the immediate manager for the `i-th` employee. If `P[i]` is `-1`, that means that the `i-th` employee does not have an immediate manager.

Print a single integer denoting the minimum number of groups that will be formed in the party.

### Examples

#### Input

```rust
3
5
-1 1 2 1 -1
2
-1 -1
4
-1 1 2 3
```

#### Output

```rust
3
1
4
```

For the first test case, three groups are sufficient, for example:

- Employee 1
- Employees 2 and 4
- Employees 3 and 5

### Note

`1 <= T`
`1 <= N <= 10`<sup>`5`</sup>
`1 <= P[i] <= N or P[i] = -1`
`P[i] != i`

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

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_144)
