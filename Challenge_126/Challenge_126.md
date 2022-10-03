# Challenge 126: Pokémon Adventure, Part 2

**Difficulty: 2/10  
Labels: Sets**

Ash successfully picked his Pokémon, thanks to your help! However, as the journey began, the Pokémon became hungry.
Each of Ash's Pokémon only likes to eat one kind of fruit, and no two Pokémon like the same fruit. All fruits are labelled with a unique integer ID.
Ash has a basket of fruits, but not all the Pokémon will be satisfied with the fruits in the basket. Some of the Pokémon's favorite fruits are missing!
Help Ash compute the number of fruits his Pokémon like, but he does not have in his basket.

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The first line contains two integers, `M` and `N`, separated by a single space.
- The second line contains `M` distinct integers, separated by a single space, call them `A`. This is the set of fruits Ash's Pokémon like.
- The third line contains `N` distinct integers, separated by a single space, call them `B`. This is the set of fruits Ash has in his basket.

Output the number of fruits the Pokémon like but not in the basket. Formally, output the number of elements that are in set `A` but not in set `B`.

### Examples

#### Input

```rust
3
4 3
1 2 3 5
2 3 4
6 7
10 12 5 7 9 8
12 10 7 8 6 4 9
2 3
30 100
100 45 30
```

#### Output

```rust
2
1
0
```

For test case `1`, `A = {1, 2, 3, 5}` and `B = {2, 3, 4}`. `1` and `5` are in `A` but not in `B`.
For test case `3`, all elements in `A` are included in `B`.

### Note

`1 <= T`
`1 <= M, N <= 10`<sup>`6`</sup>
`1 <= A[i], B[i] <= 10`<sup>`9`</sup>
All `A[i]` are distinct, and all `B[i]` are distinct.

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

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_126)
