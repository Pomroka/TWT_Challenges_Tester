# Challenge 137: Ordering

**Difficulty: 3/10
Labels: Sorting**

Alex is a kindergartener, and he was facing a challenge from his teacher. The teacher gave Alex an ordered deck of cards, each with either `A` or `B` written on it. Then, the teacher asked Alex to order the cards so that **All** `A`s occur before `B`s. However, he could only do one operation: swapping any of the two cards.
Can you help him find the most efficient way to order the cards?

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The first line contains a string of characters, each `A` or `B`, representing the deck of cards.

In one move, you may exchange the positions of any two cards.
You must reorder the cards such that all `A`s occur first, then all `B`s.
Output the minimum number of moves required to do this.

### Examples

#### Input

```rust
5
AABA
AAABBB
BB
BBAAB
BAABABBBBBABABB
```

#### Output

```rust
1
0
0
2
2
```

For test case 1, we can swap the last two cards, resulting in `AAAB`.
For test cases 2 & 3, it already satisfies the condition, so no action is needed.
For test case 4, we can swap cards 1 & 3, and cards 2 & 4, resulting in `AABBB`.

### Note

Credit: challenge idea from the Datatähti 2022.

`1 <= T`
`1 <= length of each string <= 100`
Suggested Time Complexity for each test case: `O(N log N)`

#### Hint

Sort the string and see what happens!

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

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_137)
