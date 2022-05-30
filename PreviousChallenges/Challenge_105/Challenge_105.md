# Challenge 105: Wrapping Exponents

**Difficulty:** ~~3~~**5/10**  
_**Demon Slayer Story Part 4**_

How did he manage to disappear so quickly and without a sound? What kind of martial arts does he know? Stunned, I pondered on it for a minute, then headed back home.

“Mom?”  
“Hi Ben! How was taekwondo?”  
“Alright. Listen mom, I came across some really cool warrior who can move without making a sound!”  
“Is that right? Did he tell you what martial arts he practices?”  
“No, but he told me about some demon slayer corps. Do you know what that could be?”  
“Demon slayers? Your grandma used to talk about demon slayers… Yeah”  
“So it’s real then? The demon slayer corps, demons, it’s all real?”  
“Well, I don’t know, she certainly talked about it a lot, and now you   say this man mentioned it? I suppose some of it might be true. I always thought of it as a fairy tale.  
For now, stop thinking about the demon stuff -- you have a math competition coming up tomorrow, remember? Go do some math's!”

I opened up a practice math exam. The first problem says, "calculate the value of (123<sup>123</sup>) mod (10<sup>9</sup> + 7)". Can you help me?

## Task

You are given a number `T` and `T` testcases follow, for each testcase:  
The first and only line contains two integers `a` and `b`, separated by _space_.
Efficiently output `a` to the power of `b`, `modulo (10`<sup>`9`</sup>` + 7)`.
(a.k.a., output `(a`<sup>`b`</sup>`) % 1000000007`)

### Examples

#### Input

```rs
3
3 4
2 8
123 123
```

#### Output

```rs
81
256
921450052
```

#### Note

`1 ≤ T`
`0 ≤ a, b ≤ 10`<sup>`9`</sup>
As the actual result of the exponentiation can be very big and the process may be very slow, we do not recommend actually computing the result of `a`<sup>`b`</sup>.

### Submissions

Code can be written in any of these languages:

- `Python` 3.10
- `C/C++` (GCC 10.3)
- `Ruby` 3.1
- `Golang` 1.18
- `Java` 18 (Open JDK) - use **"class Main"**!!!
- `Rust` 1.60
- `C#` 10 (.Net 6.0)

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/PreviousChallenges/Challenge_105)
