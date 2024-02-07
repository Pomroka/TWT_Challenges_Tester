# Challenge 188: Square Root Game

**Difficulty: 2/10  
Labels: Implementation**

Tim is playing a game with a list of positive integers written on a whiteboard. For each move, he picks the largest integer `x` on the whiteboard. If there are multiple instances of `x`, Tim picks the first one. He then does the following operation on `x`:

- If `x` is equal to 1, erase (the first instance of) `x` from the whiteboard.
- Otherwise, replace `x` with `floor(sqrt(x))`, where `floor` is the Greatest Integer Function and `sqrt` is the Square Root Function.

If there are no more numbers on the whiteboard, Tim stops.

After a while, Tim got bored playing the game. He gives you a number `k`. Please compute the numbers on the whiteboard after exactly `k` moves.

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The first line contains two integers, `n` and `k`.
- The second line contains `n` positive integers, the numbers on the whiteboard in order.

Start your output with the character `[`. Immediately after that, output a list of integers separated by a single comma (without space), the numbers on the whiteboard, in order, after `k` moves. Then, finish your line with the character `]`.

### Examples

#### Input

```rust
5
5 4
2 5 3 9 5
10 14
29 28 46 42 13 41 26 23 30 10
2 6
256 81
4 14
137 315 27 95
8 2024
1 20 24 20 24 20 24 1
```

#### Output

```rust
[2,2,1,3,2]
[2,5,2,2,3,2,5,4,5,3]
[2,1]
[1,1,1]
[]
```

For test case 1:

- **Turn 1** Tim chooses the 4th number and replaces it with `floor(sqrt(9)) = 3`.
- **Turn 2** Tim chooses the 2nd number and replaces it with `floor(sqrt(5)) = 2`.
- **Turn 3** Tim chooses the 5th number and replaces it with `floor(sqrt(5)) = 2`.
- **Turn 4** Tim chooses the 3rd number and replaces it with `floor(sqrt(3)) = 1`.

### Note

`1 <= T`
`1 <= n <= 1,000`
`1 <= k <= 10,000`
`1 <= a[i] <= 10`<sup>`9`</sup>

## Extra Challenge

Can you find a $\mathcal{O}(n \log(n))$ solution?

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_188)
