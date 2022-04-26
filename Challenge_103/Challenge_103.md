# Challenge 103: Pattern Recognizing

**Difficulty: 2/10**  
***Demon Slayer Story Part 3*** by Alex

After staring at the Tic-tac-toe board for a few seconds, the monster destroyed the board and launched itself at me, I threw myself to the side. The speed of that monster is incredible. I… Can I stay alive? I’ve never had to fight for my life before. He attempts to swing me off my legs, I jump up and use his head as a trampoline to do a backflip and land about four or five feet away from him. He is thrown slightly off balance but recovers very quickly. Very tough, a normal person would be lying on the ground, knocked out from such a trick. I wonder what it would take to knock this monster out, or… I guess it’s a demon… but… demon’s aren’t real though it’s just mythology isn’t it? I barely avoid an arrow shot from this monster’s belly- hold on, he can shoot arrows out of his belly? Another arrow narrowly avoided, I need to concentrate on the fight. A zig zag movement pattern to advance on him while keeping him confused, climb on him like on a wall in parkour, and a spinning kick in the side of the head. The head caved in like… Like it was made of clay. I land back on the ground and see the huge mass of disgusting flesh that was alive just moments ago crumble on the spot into ash that seems to disappear into thin air. I stare at the spot where the monster was for a few seconds when I hear a voice behind me. “Good job, I was thinking of helping but it looked like you had it under control.”

## Task

You are given a number `T` and `T` testcases follow, for each testcase,
The first line contains a string, call it `A`; and the second line contains another string, call it `B`.
Both of them contain **only** lowercase English alphabets (`a-z`).
Output an integer representing the number of occurrences of `B` in string `A`. That is, the number of times that `B` (second line) appears in `A` (first line).

### Examples

#### Input

```rs
4
mississippi
iss
abcdcdba
dc
aaaaa
aa
helloworld
appleandorange
```

#### Output

```rs
2
1
4
0
```

#### Explanation

For the first test case, there are `2` `iss` in `mississippi`: m **iss** **iss** ippi
For the third test case, there are `4` `aa` in `aaaaa`: **aa**aaa, a**aa**aa, aa**aa**a, aaa**aa**
For the fourth test case, you cannot find `appleandorange` in `helloworld`, so the answer is `0`.

#### Note

`1 ≤ T`
`1 ≤ |A|, |B| ≤ 10^6`

### Submissions

Code can be written in any of these languages:

- `Python` 3.10
- `C/C++` (GCC 10.3)
- `Ruby` 3.1
- `Golang` 1.18
- `Java` 18 (Open JDK) - use **"class Main"**!!!
- `Rust` 1.60
- `C#` 10 (.Net 6.0)

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_103)
