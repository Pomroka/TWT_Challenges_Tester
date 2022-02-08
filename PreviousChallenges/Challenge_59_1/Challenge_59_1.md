# Challenge 59.1: The treasure

Avob was returning home after he went to visit his friend. On his way home he found a piece of map on the ground which leads to a treasure. a big one. avob decided to follow the map.

When he returned home, he started packing his bags to start on his journey. Avob needs to travel to the Algerian desert. He wants you to help him find the fastest way to travel there by plane.

## Task

You are given the flights available and your job is to help avob find the fastest way to get there

### Input

You are given a number `T`. `T` test cases follow.  
In each test case you are given a number `n`, the number of flights available. `n` lines follow. Each flight is given in the following way `from to time-taken`.

### Output

You have to print the index (or indices) of the flight(s) avob should take to reach his destination as fast as he can.

## Examples

### Input
```
2
5
UK DE 420
DE DZ 250
UK FR 60
FR DZ 50
UK DZ 130
3
UK FR 100
FR DZ 100
UK DZ 200 
```

### Output
```
3 4
3
```

### Notes

- avob starts from `UK`.
- Index starts from `1` here.
- The challenges uses ISO Country codes. https://www.ncbi.nlm.nih.gov/books/NBK7249/
- If there is a tie (like the second example), the lesser number of flights will have the priority.
- There will be at least one way ~~that will make avib visit HETHAT~~ that will make avib reach his destination.

## Submission and Grading 

- code must be written in python
- `eval` and `exec` functions are not allowed same goes for `import`

Test cases by @not everyone @here (Rick Dornodon#3962)

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/PreviousChallenges/Challenge_59_1)
