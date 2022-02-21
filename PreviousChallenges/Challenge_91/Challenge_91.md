# Challenge 91: More water

## Difficulty: 5/10

You're playing a 2d sandbox video game. You've drawn up vertical lines of different lengths next to each other on the ground. Now you want to figure out between which two lines you need to pour water to get the maximum volume of water possible.

## Task

You are given a number `T` and `T` test cases follow, for each test case, output (to stdout) the maximum amount of water that can be stored with the available lines.
Each test case has the `number of lines` given, then a `list of heights` of those lines in order.
The space between each `2` adjacent lines is `1` unit.

## Examples

### Input

```sh
1
9
1 8 6 2 5 4 8 3 7
```

### Output

```sh
49
```

### Explanation

Imagine when you pour water between each two lines you're trying out, all the other lines disappear. Now going through all of them, when you pour water between the `2nd` and the `last` line the water goes up to `7` units in height and the distance between the two lines is `7`, making the area the water occupies `7x7=49` units. That is the largest possible area the water can occupy with this example.

```rust
  v             v
  |         |     8
  |x x x x x|x x| 7
  |x|x x x x|x x| 6
  |x|x x|x x|x x| 5
  |x|x x|x|x|x x| 4
  |x|x x|x|x|x|x| 3
  |x|x|x|x|x|x|x| 2
| |x|x|x|x|x|x|x| 1
1 2 3 4 5 6 7 8 9
```

(Note that choosing the two `8`s result in an area of `8x5=40 < 49`, so `49` is optimal.)

Challenge suggested by @V G#3307

## Submissions

Code can be written in any of these languages:

- `Python` 3.10
- `C/C++` (GCC 10.3)
- `Ruby` 3.1
- `Golang` 1.16
- `Java 18` (Open JDK)
- `Rust` 1.58
- `C# 10` (.Net 6.0)

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/PreviousChallenges/Challenge_91)
