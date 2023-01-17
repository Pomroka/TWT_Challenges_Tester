# Challenge 140: Maximize Profit

**Difficulty: 6/10  
Labels: Dynamic Programming**

Tim is visiting the country of Techlovania and entered a tech store. The store sells all kinds of valuable tech accessories. Unfortunately, Tim has a budget for today's trip (he can only spend at most this amount of money). He decides to spend all of this budget inside this store. Can you use your coding knowledge to help him obtain the most value out of the store?

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The first line contains two integers `N` and `B`, separated by a single space. `N` is the total number of items in the store. `B` is Tim's budget.
- The second line contains `N` integers `V`. `V[i]` represents the value of the `i`<sup>`th`</sup> item.
- The third line contains `N` integers `C`. `C[i]` represents the cost of the `i`<sup>`th`</sup> item.

Output the maximum value Tim can obtain with at most `B` dollars.

### Example 1

#### Input

```rust
1
4 10
4 11 8 1
4 8 5 3
```

#### Output

```rust
12
```

#### Explanation:

There are `4` items, and Tim has `10` dollars. The optimal purchase is to buy item `#1` and item `#3`, where the cost is `(4 + 5) <= 10` and the value is `(4 + 8) = 12`. This can be shown to be the most valuable combination with at most `10` dollars.

### Example 2

#### Input

```rust
2
3 1
5 6 7
4 3 4
10 269
55 10 47 5 4 50 8 61 85 87
95 4 60 32 23 72 80 62 65 46
```

#### Output

```rust
0
295
```

### Note

`1 <= T`
`1 <= N <= 100`
`1 <= B <= 5,000`
`1 <= V[i], C[i] <= 500`
Recommended time complexity: `O(N * B)`
You can only buy each item at most once.

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

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_140)
