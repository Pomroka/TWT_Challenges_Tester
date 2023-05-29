# Challenge 159: Alternation

**Difficulty: 2/10**  
**Labels: Implementation, Number Theory**

Tim has an interesting sequence of integers. The `0`<sup>`th`</sup> term is defined to be `0` and the `1`<sup>`st`</sup> term is defined to be `1`. Then, we alternate adding and multiplying the **previous two terms**. For example, the `2`<sup>`nd`</sup> term would be `0 + 1 = 1`, the `3`<sup>`rd`</sup> term would be `1 * 1 = 1`, the `4`<sup>`th`</sup> term would be `1 + 1 = 2`, etc.
Formally, with `A(0) = 0, A(1) = 1`, For all `n >= 2`, `A(n) = (A(n-2) + A(n-1))` if `n` is **even**, otherwise `(A(n-2) * A(n-1))` if `n` is **odd**.

Thus, the sequence starts with: `0, 1, 1, 1, 2, 2, 4, 8, 12, 96, 108, 10368, 10476, 108615168, ...`

Since the answer gets large pretty quickly, Tim asks you to compute the remainder when dividing (modulo) the `n`<sup>`th`</sup> term by `30029`.

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The only line contains an integer `n`.

Output a single integer, the `n`<sup>`th`</sup> term in the alternating sequence, modulo `30029`.

### Examples

#### Input

```rust
‌5
6
13
1
128
2023
```

#### Output

```rust
‌4
275
1
3683
13707
```

For test case 2, as shown above, the `13`<sup>`th`</sup> term is `108615168`, which is `275` when divided by `30029`.

### Note

- `30029` is a prime number.
- `1 <= T`
- `1 <= n <= 10`<sup>`4`</sup>
- All computations fit in a 32-bit integer.

#### Extra Challenges (not tested)

`1 <= n < 2`<sup>`63`</sup>, what happens as `n` gets large?  
Is it still true if you change `30029` to `10`<sup>`9`</sup>` + 7`?

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

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_159)
