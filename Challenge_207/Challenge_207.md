# Challenge 207: Cyclic Traffic Light

**Difficulty: 3/10  
Labels: Two Pointers, Binary Search**

SnowballSH finds himself stuck in front of a strange traffic light. The light signal cycles every `n` seconds, and on each second the signal is either `R` (Red), `Y` (Yellow), or `G` (Green). For example, if the signal cycle is `RGGRY`, then the light would turn `Red-Green-Green-Red-Yellow-Red-Green-Green-Red-Yellow-Red-...`. He can only cross the road if the light turns green. Wanting to get to his destination as soon as possible, SnowballSH will cross immediately when the signal turns green.

SnowballSH knows the cycle of the signal and the signal he is currently seeing. Help him compute the **minimum number of seconds** he has to wait until he is **guaranteed** to be able to cross the road.

For example, if the signal cycle is `RGGRY` and SnowballSH currently sees Red, he would either cross after 1 second (he would see `RG`) or after 3 seconds (he would see `RYRG`). Since he does not know which `R` he is at right now, the minimum number of seconds he has to wait to **guarantee** a green light, or in other words the maximum number of seconds he could be waiting for a green light, would be `3`.

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The first line contains an integer `n`, the length of the cycle, and a character `c`, a character `R`, `Y`, or `G`, the signal SnowballSH currently sees, separated by a single space.
- The second line contains a string of `n` characters `s`, each `R`, `Y`, or `G`, the cyclic signal sequence of this traffic light. Each signal in `s` appears for one second. It is guaranteed that at least one of these characters will be `G`.

Output a single integer, the **minimum number of seconds** SnowballSH has to wait until he is **guaranteed** to be able to cross the road.

### Examples

#### Input

```rust
7
5 R
RGGRY
1 G
G
3 R
RRG
5 Y
YRRGY
7 R
RGRGYRG
9 Y
RRRGYYYGY
10 G
GRRRRRRRRG
```

#### Output

```rust
3
0
2
4
1
4
0
```

## Note

- `1 <= T`
- `1 <= n <= 10`<sup>`5`</sup>
- `c` and all `s[i]` is one of `R`, `Y`, or `G`
- For at least one `1 <= i <= n`, `s[i] = G`.
- Credit: codeforces

## Submissions

Code can be written in any of these languages:

- `Python` 3.11
- `C` (gnu17) / `C++` (c++20) - GCC 12.2
- `Ruby` 3.3.4
- `Golang` 1.21
- `Java` 19 (Open JDK) - use "class Main"!!!
- `Rust` 1.72
- `C#` 11 (.Net 7.0)
- `JavaScript` ES2023 (Node.js 20.6)
- `Zig` 0.13.0

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_207)
