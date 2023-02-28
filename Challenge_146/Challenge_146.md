# Challenge 146: Happy Tiles

**Difficulty: 3/10  
Labels: String**

Tim is walking on a road called the MIT road. This road is special: it consists of N square tiles in a row, where each tile has a letter written on it.
Tim wants to pick a tile to start walking on. The tile he lands on is a happy tile if it is the i<sup>th</sup> tile he walked on and has the same letter as the i<sup>th</sup> tile of the entire road. A tile is unhappy if it is not a happy tile. Tim stops immediately once he steps on an unhappy tile. He wants to pick a tile to start walking, so he can maximum the number of happy tiles he will step on. However, Tim is not a boring person, so he does not wish to start from the first tile of the road. Can you help him?

## Task

The first line contains a single integer `T`, the number of test cases. For each test case:

- The first line contains an integer `N`, the number of tiles on the road.
- The next line contains a string of `N` characters `a-z`, call it `S`, the letter on each tile.

If Tim starts on the j<sup>th</sup> tile, the i<sup>th</sup> tile of the road (where `i >= j`) is happy if `S[i] = S[i-j]`.
Output the maximum number of consecutive happy tiles Tim can step on before he reaches the end of the road. He may start on any tile but the first one.

### Examples

#### Input

```rust
5
5
aaaaa
7
abacaba
7
aaabaab
11
techwithtim
3
xyz
```

#### Output

```rust
4
3
2
1
0
```

For test case 1, Tim can start on the second tile, where the `1-4`<sup>`th`</sup> characters are the same as the `2-5`<sup>`th`</sup> characters.
For test case 2, Tim can start on the `5`<sup>`th`</sup> tile, where the `1-3`<sup>`th`</sup> characters are the same as the `5-7`<sup>`th`</sup> characters.

### Note

`1 <= T`
`2 <= N <= 1000`
`a <= each character <= z`

### Submissions

- `Python` 3.10
- `C` (gnu17) / `C++` (c++20) - GCC 11.2
- `Ruby` 3.1
- `Golang` 1.19
- `Java` 19 (Open JDK) - use **"class Main"!!!**
- `Rust` 1.64
- `C#` 10 (.Net 6.0)
- `JavaScript` ES2022 (Node.js 18.10)

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_146)
