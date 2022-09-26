# Challenge 122: Calm Down!

**Difficulty: 1/10**  
**Labels: Control Flow**

You are developing a chat application. During the beta testing phase, you are noticing a lot of people spamming in ALL CAPITAL LETTERS LIKE THIS, which may be negative for the community. You would like to convert those to lower cases.

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The first line contains an integer `N`.
- The second line contains `N` words, each consisting of only English alphabets (`a-zA-Z`), separated with a single space.

Output the words, separated by a single space, after the following filtration:

- If a word is the **first** word in the list, leave it as it is.
- If a word is **not the first** word and all of its letters are capital letters (`A-Z`), then make the entire word lowercase.

### Examples

#### Input

```rust
5
8
I dont care APPLE IS THE BEST FRUIT
5
But BAnANA is SIMPLY better
4
ok fine u win
1
KTHXBYE
6
PLZ SOLVE this challenge ITs EaSY
```

#### Output

```rust
I dont care apple is the best fruit
But BAnANA is simply better
ok fine u win
KTHXBYE
PLZ solve this challenge ITs EaSY
```

### Note

`1 <= T`
`1 <= N <= 10,000`
`1 <= length of each word <= 100,000`
Each word is guaranteed to only contain `a-z` and `A-Z`.

### Submissions

Code can be written in any of these languages:

- `Python` 3.10
- `C/C++` (GCC 10.3)
- `Ruby` 3.1
- `Golang` 1.18
- `Java` 18 (Open JDK) - use "class Main"!!!
- `Rust` 1.62
- `C#` 10 (.Net 6.0)
- `JavaScript` ES2022 (Node.js 18.2)

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/PreviousChallenges/Challenge_122)
