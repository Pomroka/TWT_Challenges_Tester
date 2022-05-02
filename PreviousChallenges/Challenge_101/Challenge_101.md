# Challenge 101: Help Me

**Difficulty: 5/10**  
***Demon Slayer: Encountering a Demon, Part 1***

I’m soaring through the skies as I hear the sound of an alarm clock. I wake up. I have a taekwondo lesson this morning, and if it weren’t for the blasted family reunion right after I’d be looking forward to it. “Ben, breakfast’s ready!”

“I’ll be right there!” I yelled back as I lazily changed while heading downstairs after a trip to the bathroom. Breakfast doesn’t seem as good as usual, not sure if it’s my mom’s or my mood.

The sky on my way to taekwondo is clouded. The forecast said it would be sunny. I suppose even meteorologists have their day off every now and then.

Taekwondo turned out alright, had to do some sparring and some kicks. But now I have to… What’s that smell? If human nostrils could contract mine would right now. If you could combine the smell of rotten flesh, eggs, some feces, and sweat that might just sum it up. I turn around, and my legs get momentarily stuck to the ground.

It seems like I have remembered the locations of every human on my way here. But how many humans near me can come and help?

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The first line contains two integers `N` and `Q`, separated by spaces.
- The next line contains `N` integers, separated by spaces, which are the locations of human on your way here. Locations are conveniently labelled as natural numbers.
- The next `Q` lines are queries, each contain two numbers `A` and `B`. For each of the `Q` queries, output the number of humans between location `A` and `B`, **inclusive**, separated by spaces.

### Examples

#### Input

```rs
2
4 6
3 2 7 5
2 3
2 4
2 5
2 7
4 6
8 10
1 2
101
99 102
99 100
```

#### Output

```rs
2 2 3 4 1 0
1 0
```

For the first test case, there are `4` humans and `6` queries.
The street will look like this: `#HH#H#H#...`

#### Note

`1 ≤ T`
`1 ≤ N, Q ≤ 101,101`
`1 ≤ A ≤ B ≤ 1,101,101`

### Submissions

Code can be written in any of these languages:

- `Python` 3.10
- `C/C++` (GCC 10.3)
- `Ruby` 3.1
- `Golang` 1.18
- `Java` 18 (Open JDK) - use **"class Main"!!!**
- `Rust` 1.60
- `C#` 10 (.Net 6.0)

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/PreviousChallenges/Challenge_101)
