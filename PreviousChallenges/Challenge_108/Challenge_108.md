# Challenge 108: Math Evaluator, Part II

> You may NOT use existing tools or functions to evaluate the expressions. That said, functions including but not limited to: `exec` and `eval` in Python and `eval` in Ruby and JS, `Function(...)()` in JS, and any other functions that uses a built-in parser or evaluator are banned (they will be manually checked). This is for fair competition purposes.

**Difficulty: 6/10**  
_**Demon Slayer Story Part 6**_

“You thought I was just another weak demon didn’t you?” Its chuckle became a sick laughter.
“You thought you could just kick my head and it would cave in, didn’t you?” It was now almost doubling over from laughter. After a second or two that seemed like an eternity, it finally got up, the laughter ceased. “Well, let me show you what happens when you mess with a real, strong demon.” With a snarl it lunged for me, and just as I made to roll over to the side, I felt a light wind and heard a couple thumping noises followed by what sounded like a ball with many bumps on it rolling to a stop.
Wham!
I looked for the noise and saw a large muscular body without a head lying on the floor, starting to disintegrate into disappearing ash.

## Task

You are given a number `T` and `T` testcases follow, for each testcase, You are given one line of math expression.

Numbers will be separated by an operator (`+`, `-`, or `*`) with one space on each side. **Different from the last challenge, different operators may occur in one expression.**
You should follow basic rules of math: `*` has a higher precedence than `+` and `-`. `+` and `-` should have the same precedence and evaluated from left-to-right.
Numbers may be positive or negative. Zero will always be `0`, never `-0`.

Let the result of the expression be `r`. Output `r mod (10^9 + 7)` if r >= 0, or `-(|r| mod (10^9 + 7))` if r < 0.

### Examples

#### Input

```rs
8
1 + 3 + 2
3 + -2 - 9
3 * 5 + 4
3 + 5 * 4
-9 + 2 - 8 * 9 - 1
-7 * 3 - -3 * 7 + 0
0
23487 - -9283 + -3472 * 30190 * 376 - 90
```

#### Output

```rs
6
-8
19
23
-80
0
0
-412166727
```

- For test case 3, `3 * 5 + 4 = (3 * 5) + 4 = 15 + 4 = 19`.
- For test case 6, `-7 * 3 - -3 * 7 + 0 = -21 - -21 + 0 = 0`.
- For test case 8, although the actual result is `-39412167000`, we output `-(|-39412167000| mod (10^9 + 7)) = -412166727`.

#### Note

- Each operator will be either `+`, `-`, or `*`.
- `1 ≤ T`
- `-10`<sup>`8`</sup>` ≤ each number ≤ 10`<sup>`8`</sup>

### Submissions

Code can be written in any of these languages:

- `Python` 3.10
- `C/C++` (GCC 10.3)
- `Ruby` 3.1
- `Golang` 1.18
- `Java` 18 (Open JDK) - use **"class Main"!!!**
- `Rust` 1.61
- `C#` 10 (.Net 6.0)
- `JavaScript` ES2022 (Node.js 18.2)

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/PreviousChallenges/Challenge_108)
