# Challenge 109: Days Between, Part I

**Difficulty: 3/10**  
_**Demon Slayer Story Part 6**_

“Thanks for holding on, I got held up” I looked up to the man talking to me. It was the same demon slayer I met that day.
“H-how, what?” I babbled.
“Are you still against joining the corps?”
“Huh? I uhh…”
“How about this, I’ll meet you after your next taekwondo class and you can tell me then?”
“Sure…” After my next taekwondo class? “How do you know when-” He’d already gone.
“You should join them!”
I looked up, surprised to hear my little brother.
“Then you could teach me all the cool stuff they can do!”
I let out a chuckle, and looked up at my parents. They were both looking at me silently.
“I’ll… think about it” My parents seemed to relax a bit.

Given two dates (month and date, no year), calculate the number of months and the number of days between them.

## Task

You are given a number `T` and `T` testcases follow, for each testcase:  
You are given two dates, `A` and `B`, in ISO-like format of `mm-dd`, separated by a single space.
If `B` is `M` months and `D` days after `A`, output `M D`.
Assume February has `28` days, and other months follow normal international rules.

### Examples

#### Input

```rs
7
02-02 02-03
11-11 12-11
09-11 12-03
02-27 03-31
04-11 06-10
07-07 07-07
01-01 12-31
```

#### Output

```rs
0 1
1 0
2 22
1 4
1 30
0 0
11 30
```

For test case 1, **Feb. 3rd** is `0` months, `1` day after **Feb. 2nd**.
For test case 2, **Dec. 11th** is `1` month, `0` days after **Nov. 11th**.
For test case 7, Almost a full year, but one day short, so `11` months `30` days.

You can use this tool to find solution of any data for testing purposes (just leave the year field blank): [www.timeanddate.com](https://www.timeanddate.com/date/durationresult.html)

#### Note

- `1 <= T`
- Date `A` will always come before date `B`, or is the same as date `B`.
- All date will be in `mm-dd` format.
- Zero padding will be added for single-digit numbers.
- `01 <= mm <= 12` and `01 <= dd <= 31`.
- All dates will be valid (nothing like `02-30`).

Challenge suggested by @not everyone @here

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

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/PreviousChallenges/Challenge_109)
