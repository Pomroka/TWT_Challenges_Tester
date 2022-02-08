# Challenge 60.1: The cards

After you helped avob travel the whole world just to go to Algeria (he thanks you for helping him btw), he was very tired of the journey, so he decided to visit his friend that he haven't seen since a very long time (never seen him before), HETHAT.

Avob and HETHAT sat together drank some tea and played some card games. One of the games they played has a square grid pattern, avob picks a column from there, then when HETHAT picks the cards up and lays them out he essentially rotates the grid 90 degrees in one direction (clockwise), given that he knows which column avob picked the first time, that column now becomes a row, so now when avob picks a column HETHAT knows exactly which column and row the card is in.

## Task

Find out which card avob chose.

### Input

You are given a number `T`. `T` test cases follow.  
In each test case you are given a number `x` where `x` is the dimension of the square. In the next line, you are given another two numbers, `a` and `b` where `a` is the first number avob said and `b` is the second number avob said. `x` lines follow, each line will have `x` numbers space-separated which makes the first grid hethat made. `x` more lines follow, each line will have `x` numbers space-separated which makes the second grid hethat made. 

### Output

You have to print the card avob chose.

## Examples

### Input
```
2
3
3 1
2 3 5
6 8 9
1 4 7
1 6 2
4 8 3
7 9 5
1
1 1
1
1
```

### Output
```
7
1
```

### Notes

- HETHAT will not cheat.
- The grid will not have similar numbers.

## Submission and Grading 

- you have to submit in a file
- code must be written in python
- `eval` and `exec` functions are not allowed same goes for `import` and `open`

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/PreviousChallenges/Challenge_60_1)
