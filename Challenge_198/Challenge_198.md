# Challenge 198: Security Guard

**Difficulty: 3/10  
Labels: Greedy**

SnowballSH is a security guard at the main entrance of the Tim Institute of Technology. His only job is to keep track of the number of people entering and exiting the campus.

To perform this task, SnowballSH writes down a `+` whenever a person enters and a `-` whenever a person leaves. The campus **starts with zero people** in the beginning of a day. At some point during that day, he has written down a sequence `s` of `+`s and/or `-`s.

One day SnowballSH got lazy and decided to make up some fake data, so he didn't have to focus on his work. Suddenly, Tim, SnowballSH's boss, decided to check his work in the middle of a day! SnowballSH suddenly realized that his sequence `s` might be impossible and not plausible (say `+--+`, since there could not have been two people exiting while only one has entered)!

SnowballSH realized that he only has time to **swap at most one pair of characters** in his sequence `s`. Since SnowballSH does not wish to lose his job, help him find out whether he can use this opportunity to make his sequence plausible. Note that if the sequence is already plausible, SnowballSH doesn't have to swap characters and can hand it to Tim confidently.

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The only line contains a string `s`, the original, potentially impossible, sequence SnowballSH wrote down so far.

Output `YES` if SnowballSH can make his sequence plausible by swapping at most one pair of characters, otherwise output `NO`.

### Examples

#### Input

```rustrust
8
-+
+-
+++-
---++
+
-
+--++-++--+
+--+----+++---+++++-+-++
```

#### Output

```rust
YES
YES
YES
NO
YES
NO
YES
NO
```

For test case 1, we swap the two characters, `+-` is plausible.

### Note

- `1 <= T`
- `1 <= s <= 20,000`
- Inspiration: Codeforces/Kotlin Heroes

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

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_198)
