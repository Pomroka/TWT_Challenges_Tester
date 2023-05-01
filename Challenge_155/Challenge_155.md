# Challenge 155: Hamsters and Apples

**Difficulty: 3/10  
Labels: Binary Search**

There are `N` hamsters and `M` apples in the yard. Each hamster eats at a different pace. If all hamsters can eat apples simultaneously and nonstop, and you can freely distribute the apples to hamsters, what is the minimum time for the hamsters to finish eating all the apples?

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The first line contains two integers, `N` and `M`, separated by a single space. `N` is the number of hamsters and `M` is the number of apples.
- The next line contains `A`, a list of `N` integers, separated by a single space.

Let `A[i]` denote the time it takes for hamster `i` to eat **one** apple. Output a single integer, the minimum time for the hamsters to finish eating all the apples.

### Examples

#### Input

```rust
4
3 7
2 5 3
10 10
5 4 10 7 8 4 1 8 9 2
2 2
20 23
2 2
202 3
```

#### Output

```rust
‌8
5
23
6
```

- For test case 1, there are `3` hamsters to eat `7` apples. In `8` minutes, hamster `1` will eat `4` apples, hamster `2` will eat `1` apple, hamster `3` will eat `2` apples, finishing a total of `7`. This can be shown to be the minimum time to finish all `7` apples.
- For test case 4, instead of distributing one apple to each, we should distribute both apples to the faster hamster.

### Note

- `1 <= T`
- `1 <= N <= 5,000`
- `1 <= M <= 10`<sup>`4`</sup>
- `1 <= A[i] <= 10`<sup>`4`</sup>
- (The answer fits in a signed 32-bit integer).

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

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_155)
