# Challenge 115: Infinite Array

**Difficulty: 3/10**  
Assume you have an array `A` of infinite size. Initially, all elements are set to `0`. You have to perform `Q` queries (tasks).

Queries are in one of the three following types where `i` and `v` are integers:

1. `P i` This means you need to print `A[i]`.
2. `S i v` This means you need to set `A[i]` to `v`.
3. `A i` This means you need to increment the value of `A[i]` by `1`.

## Task

You are given a number `T` and `T` test cases follow, for each test case:  
You are given a number `Q`. This is the number of queries you need to perform.  
The next `Q` lines each contain a type of query, described above. Perform the queries.

### Examples

#### Input

```rs
2
3
P 50
S 115 88
P 115
8
A 73
S 90281830235 927
S 0 3
P 90281830235
A 0
P 73
P 0
P 90281830234
```

#### Output

```rs
0
88
927
1
4
0
```

### Note

`1 <= T`
`1 <= Q <= 10`<sup>`6`</sup>
`0 <= i, v <= 10`<sup>`18`</sup>

### Reminder

Since `i` and `v` can be very big, it is not a good idea to actually create an array of size `10`<sup>`18`</sup>, which will fail due to Memory Limit Exceeded.

### Submissions

Code can be written in any of these languages:

- `Python` 3.10
- `C/C++` (GCC 10.3)
- `Ruby` 3.1
- `Golang` 1.18
- `Java` 18 (Open JDK) - use **"class Main"!!!**
- `Rust` 1.62
- `C#` 10 (.Net 6.0)
- `JavaScript` ES2022 (Node.js 18.2)

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/PreviousChallenges/Challenge_115)
