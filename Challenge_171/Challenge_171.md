# Challenge 171: Demon Slayer

**Difficulty: 4/10  
Labels: Binary Search**

Tim, the emperor of the Kingdom of Tech With Tim, was just informed that an army of `m` demons is marching toward his kingdom. Fortunately, the demon army is very unorganized - they attack the kingdom one at a time. The demon army will arrive at the kingdom tomorrow.
Tim has `n` brave and powerful heroes. Each of the heroes has a power stat, call it `p`. Each of the demons has an attack stat `a` and a defense stat `d`. Each stat is represented by a positive integer.
The heroes decided that depending on the stats of the demon, one of them will go slay the demon, while others defend the kingdom. This strategy will only work if `p_chosen >= d` (so the chosen hero can slay the demon) **and** `sum of p_rest >= a` (so the sum of the rest can defend against the demon's attacks).
Unfortunately for Tim, his heroes are currently undertrained. However, he has gold coins. Each gold coin can increase a hero's power stat by 1 temporarily. **The stat boost for all is <u>lost</u> after slaying each demon**.
For each demon, compute the **minimum** number of gold coin Tim needs to train his heroes to successfully defend the kingdom.

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The first line contains two integers, `n` and `m`.
- The second line contains `n` integers `p[i]`, the power stat of each hero.
- `m` lines follow. Each line contains two integers `d[i]` and `a[i]`, the defense stat and the attack stat of each demon.

Output the sum of the minimum number of gold coins needed to train the heroes to defend the kingdom, **independently** over all demons.

### Examples

#### Input

```rust
1
4 5
3 6 2 3
3 12
7 9
4 14
1 10
8 7
```

#### Output

```rust
9
```

Due to the input being longer than usual, only one sample is provided, but it provides 5 subcases to check your solution.

The cost for each demon are `1, 2, 4, 0, 2`:

- For the first demon, the first hero is sufficient to slay the demon. You can increase the power stat of one of the rest so the defending sum becomes `12`.
- For the second demon, it is optimal to increase the second hero's stat by `1` so he can slay the demon, and then increase one of the rest by `1` to defend.
- For the third demon, you can increase the first hero's stat by `1`, and one of the rest by `3`.
- For the fourth demon, the current stats are sufficient.
- For the fifth demon, it is optimal to increase the second hero's stat by `2`.
The answer is thus `1 + 2 + 4 + 0 + 2 = 9`.

### Note

- `1 <= T`
- `1 <= n <= 10`<sup>`5`</sup>
- `1 <= m <= 10`<sup>`5`</sup>
- `1 <= p, d, a <= 10`<sup>`9`</sup>
- You should use 64-bit integers to avoid overflow.
- Source: codeforces

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

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_171)
