# Challenge 179: Tim and His Friends

**Difficulty: 2/10 (4/10 for Extra Challenge)  
Labels: Simulation, Brute Force, (Meet in the Middle for Extra Challenge)**

Tim has many friends. Some of them are happy and some of them are unhappy. Tim wants to make all his friends become happy, so he invented the following plan:

There are `n` boys and `m` girls among his friends. Let's number them from `0` to `n - 1` and `0` to `m - 1` separately. In `i`<sup>`th`</sup> day, Tim invites `(i mod n)`<sup>`th`</sup> boy and `(i mod m)`<sup>`th`</sup> girl to have dinner together (as Tim is a programmer, `i` starts from `0`). If one of those two people is happy, the other one will also become happy. Otherwise, those two people remain in their states. Once a person becomes happy (or if he/she was happy originally), he stays happy forever.

Tim wants to know whether he can use this plan to make all his friends become happy at some moment.

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The first line contains two integer `n` and `m`.
- The second line contains integer `b`, denoting the number of happy boys among friends of Tim, and **then follow** `b` distinct integers `x`<sub>`1`</sub>`, x`<sub>`2`</sub>`, ..., x`<sub>`b`</sub>, denoting the list of indices of happy boys.
- The third line contains integer `g`, denoting the number of happy girls among friends of Tim, and then follow `g` distinct integers `y`<sub>`1`</sub>`, y`<sub>`2`</sub>`, ... , y`<sub>`g`</sub>, denoting the list of indices of happy girls.

If Tim can make all his friends become happy by this plan, print `YES`. Otherwise, print `NO`.

### Examples

#### Input

```rust
‌3
2 3
0
1 0
2 4
1 0
1 2
2 3
1 0
1 1
```

#### Output

```rust
‌YES
NO
YES
```

For test case 1:

- On the 0<sup>th</sup> day, Tim invites 0<sup>th</sup> boy and 0<sup>th</sup> girl. Because 0<sup>th</sup> girl is happy at the beginning, 0<sup>th</sup> boy become happy at this day.
- On the 1<sup>st</sup> day, Tim invites 1<sup>st</sup> boy and 1<sup>st</sup> girl. They are both unhappy, so nothing changes at this day.
- On the 2<sup>nd</sup> day, Tim invites 0<sup>th</sup> boy and 2<sup>nd</sup> girl. Because 0<sup>th</sup> boy is already happy he makes 2<sup>nd</sup> girl become happy at this day.
- On the 3<sup>rd</sup> day, Tim invites 1<sup>st</sup> boy and 0<sup>th</sup> girl. 0<sup>th</sup> girl is happy, so she makes 1<sup>st</sup> boy happy.
- On the 4<sup>th</sup> day, Tim invites 0<sup>th</sup> boy and 1<sup>st</sup> girl. 0<sup>th</sup> boy is happy, so he makes the 1<sup>st</sup> girl happy. So, all friends become happy at this moment.

### Note

- `1 <= T`
- `1 <= n, m <= 100`
- `0 <= b, x`<sub>`i`</sub>` < n`
- `0 <= g, y`<sub>`i`</sub>` < m`
- It is guaranteed that there is at least one person that is unhappy among his friends.

Source: Huang I-Wen on Codeforces

## Extra Challenge (won't be tested)

- `O((n + m)(n * m))` and `O(n * m)` solutions will be accepted. But there actually exists an `O(n + m)` solution!
- `1 <= n, m <= 10`<sup>`6`</sup>

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

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_179)
