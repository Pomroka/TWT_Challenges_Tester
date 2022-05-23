# Challenge 104: Giant Slayer

**Difficulty: 6/10**  
***Demon Slayer Story Part 4***

I look behind my back. A guy about six feet tall, just a bit taller than me, is standing about ten feet away. A relaxed yet trained to action stance that commands respect. “What you’ve just fought is a demon. But I trust you know that by now.”  
“A demon? No, it’s just some monster, demons don’t exist.” I said somewhat uncertainly.  
“Well, what you have just fought was in fact, a demon. If it were just some monster it would not have disappeared into thin air like it did.”  
“Why did it disappear? Things don’t just disappear into thin air do they?”  
“Well, if you want to know more you should join the demon slayer corps.”  
“The what?”  
“The demon slayer corps. Our mission is to rid the earth of demons while keeping the general public unaware of it.”  
“Why?”  
“Well, the public either wouldn’t believe us or there would be mass panic, wouldn’t there?”  
“I… I guess so.”  
“So seeing as how you handled that demon, would you be interested to join the corps?”  
“What? No, I have parents, I have siblings, I can’t just leave them... Joining this uhhh, corps of yours requires to leave all that behind doesn’t it?”  
“Not exactly, sure you will be away most of the time but you could still visit them maybe once a year or so.”  
“Once a year?” I let out a laugh, again louder than it should’ve been, “I can’t do that.”  
“I know this isn’t an easy decision, but… let me know if you change your mind.”  
“Change my mind? Let you know? How?” But he was already gone.

As an experienced member of the Demon Slayer Corp., you like to challenge the most powerful demons. Beating strong demons will give you power, however, messing around with weak demons will just cost your time, so you don't want to deal with them.
Each demon along a perfectly straight road is assigned with a **"desire value"**, which represents your willingness to deal with that demon. However, due to some magical reason, you can only fight one continuous sequence of demons.
Find the **maximum** total desire value you can get by fighting a subsequence of demons (or none) on the road.

## Task

You are given a number `T` and `T` testcases follow, for each testcase:

- The first line contains integer `N`, the number of demons on the road.
- The second line contains array `A` containing `N` integers, separated by space. `A[i]` represents the "desire value" of the `i`th demon on the road.

Output the **maximum desire value** of the sum of each possible subarrays of `A`.

### Examples

#### Input

```rs
3
4
-2 4 9 -1
8
-1 3 -2 5 3 -5 2 2
5
-4 -1 -10 -6 -2
```

#### Output

```rs
13
9
0
```

- For the first testcase, `A` = `[-2, 4, 9, -1]`. The maximum subarray sum of `A` is the sum of `[4, 9]` = 13. Including either -2 or -1 will make the value smaller.
- For the second testcase, the subarray with the maximum sum is `[3, -2, 5, 3]`.
- For the third test case, it is best to not fight any demon.

#### Note

- `1 ≤ T`
- `1 ≤ N ≤ 10`<sup>`5`</sup>
- `-10`<sup>`9`</sup>` ≤ A[i] ≤ 10`<sup>`9`</sup>
- You might want to use 64-bit integer types (i.e. `long long` in C++), as the sums can be very large if you try to compute them.

### Submissions

Code can be written in any of these languages:

- `Python` 3.10
- `C/C++` (GCC 10.3)
- `Ruby` 3.1
- `Golang` 1.18
- `Java` 18 (Open JDK) - use **"class Main"**!!!
- `Rust` 1.60
- `C#` 10 (.Net 6.0)

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/PreviousChallenge/Challenge_104)
