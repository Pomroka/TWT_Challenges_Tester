# Challenge 139: Maximum Negation

**Difficulty: 3/10  
Labels: Simple Searching**

The first semester of university is finally over! Avib received a list of all the grades he has gotten throughout the semester. Interestingly, his teacher grades on a scale of real numbers. Seeing Avib unhappy with his total grade (sum of all the grades he got), his teacher gave him a final chance:

Avib can perform the following operation to his grades:

- Pick any grade and flip its sign (`f(x) = -x`)

However, the teacher only allows him to perform the operation at most once. Can you help Avib make the best operation?

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The first line contains an integer `N`.
- The next line contains `N` integers, separated by a single space. This is Avib's grades.

Output the maximum total grade score Avib can obtain after at most one of the operation above.

### Examples

#### Input

```rust
4
4
2 -3 -9 10
3
4 9 7
1
-123
6
-17 0 -15 -17 6 1
```

#### Output

```rust
18
20
123
-8
```

For test case 1, the best way is to pick `-9`, resulting in `2 + (-3) + 9 + 10 = 18`.
For test case 2, doing the operation on any number would decrease the total score, so we do nothing, resulting in `4 + 9 + 7 = 20`.

### Note

`1 <= T`
`1 <= N <= 10`<sup>`5`</sup>
`-10`<sup>`9`</sup>` <= each grade <= 10`<sup>`9`</sup>

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

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_139)
