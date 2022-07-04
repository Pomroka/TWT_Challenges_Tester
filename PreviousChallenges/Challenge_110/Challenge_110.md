# Challenge 110: Missing Odd Number

**Difficulty: 2/10**  
_**Demon Slayer Story Part 7**_

The next taekwondo class I was more tense than usual. Both appearances of the demon slayer were so far quite sudden. I didn’t know what exactly to expect this time. Would he just appear out of thin air? The class had just finished, and I was just walking out when I saw him waiting outside. “Rather decent of you to show up without it being a surprise for once.” I said rather pleased.
“The first time I was already there, you simply hadn’t noticed me during your fight. The second time you were about to die, I didn’t think it was a good time for pleasantries.”
“Right… well. I’ll join the corps.”
“Oh? Well, that was easy.”
“I don’t want to come back to another demon trying to kill my family, if joining the corps will solve that problem I’ll do it.”
“Alright well, let’s wait until the end of the week so you can say your goodbyes to everyone at school, taekwondo, etc. Then I’ll come pick you up next Monday.”

You are given all **odd** numbers between `1` and the `N`<sup>`th`</sup> odd number (inclusively) but one. Output the missing odd number.

## Task

You are given a number `T` and `T` testcases follow, for each testcase,
You are given an integer `N`.
The next line contains `N-1` **odd** integers, separated by a single space.
Output the missing odd number between `1` and the `N`<sup>`th`</sup> natural odd number.

### Examples

#### Input

```rs
4
3
1 5
4
7 1 3
6
11 5 9 3 7
10
1 3 5 7 9 11 13 15 17
```

#### Output

```rs
3
5
1
19
```

For test case 1, the first three odd numbers are `1`, `3`, `5`. `3` is missing from the list.
For test case 3, the first six odd numbers are `1`, `3`, `5`, `7`, `9`, `11`. `1` is missing from the list.

#### Note

`1 ≤ T`
`2 ≤ N ≤ 10`<sup>`5`</sup>
All integers in the second line are **odd** and within `[1, 2N-1]`

### Submissions

Code can be written in any of these languages:

- `Python` 3.10
- `C/C++` (GCC 10.3)
- `Ruby` 3.1
- `Golang` 1.18
- `Java` 18 (Open JDK) - use "class Main"!!!
- `Rust` 1.61
- `C#` 10 (.Net 6.0)
- `JavaScript` ES2022 (Node.js 18.2)

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/PreviousChallenges/Challenge_110)
