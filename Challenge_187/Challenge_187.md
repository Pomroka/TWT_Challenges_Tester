# Challenge 187: Missing Dance Moves

**Difficulty: 3/10  
Labels: Recursion, Memoization, DP**

Tim is on a linear dance machine. By the rules, Tim must move either left or right exactly one square every move. Every square has a bonus value, and his final score is the sum of the bonus values of all the squares he has stepped on. Some squares have a negative bonus value, which means Tim gets a penalty for stepping on there!
Unfortunately, Tim prepared his dance moves last night but forgot some of them. Help Tim figure out the maximum score he could get, if the missing dance moves are replaced by either left or right.

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The first line contains two integers, `N`, the number of squares on the machine, and `k`, the position of Tim's initial position. The leftmost square has position `1` and the rightmost square has position `N`. The initial square **does not** count towards the final score.
- The second line contains `N` integers `a`, the bonus value for each square.
- The third line contains a string `s`, the dance moves Tim will perform. A missing dance move will be denoted as a `?`, a left move will be denoted as a `L`, and a right move will be denoted as a `R`.

If Tim is at an edge (position 1 or `N`), he can still move or choose to move towards the direction of the edge, but instead of falling off he will restep on the edge square again, gaining the bonus on that square.

Tim must follow the moves except when he sees a `?`, for which he may choose left or right. Output a single integer, the maximum score Tim could get. In other words, complete each `?` as `L` or `R` and compute the best score.

### Examples

#### Input

```rust
4
5 3
3 5 8 2 3
LRLLLL
7 5
-7 0 3 15 1 -6 9
?RL??LRRR
4 1
1 -100 -200 800
????L
8 8
1 2 3 9 6 3 2 1
??L?RR????RR?
```

#### Output

```rust
‌27
62
1100
74
```

- For test case 1, Tim didn't forget any dance move, so he starts at 8 (position 3) and goes to 5, 8, 5, 3, 3, 3 in order. His score is `5 + 8 + 5 + 3 + 3 + 3 = 27`.
- For test case 2, Tim starts at 1 (position 5). He can complete the dance moves as `LRLLRLRRR` to achieve a maximum score of `15 + 1 + 15 + 3 + 15 + 3 + 15 + 1 + -6 = 62`.
- The moves for test case 3 and 4 are `RRRRL` and `LLLLRRLLRLRRL`, respectively.

### Note

- `1 <= T`
- `2 <= N <= 10`<sup>`4`</sup>
- `1 <= k <= N`
- `-1000 <= a[i] <= 1000`
- `1 <= |s| <= 1000`

### Submissions

Code can be written in any of these languages:

- `Python` 3.11
- `C` (gnu17) / `C++` (c++20) - GCC 12.2
- `Ruby` 3.2
- `Golang` 1.21
- `Java` 19 (Open JDK) - use **"class Main"!!!**
- `Rust` 1.72
- `C#` 11 (.Net 7.0)
- `JavaScript` ES2023 (Node.js 20.6)

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_187)
