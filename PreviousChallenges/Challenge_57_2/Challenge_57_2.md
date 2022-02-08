# Challenge 57.2: Jobs

After spending too much time learning programming, you decide that you want to work and get some money. After some searching you find some jobs on the internet but they have a dead line. You want to get as much money as you can from those jobs.

You are given a number `T`, the number of test cases. `T` cases follow.  
For each case you are given a number `n` which is the amount of jobs you found. `n` lines follow, for each job you are given the job name, the job dead line, the money you will get from that job in the following format `name deadline money`. 

Knowing that each job takes from you exactly one time unit. Output the jobs that you would choose, space separated and in the same order that you will do them, to get the most amount of money without breaking the time limit.

## Example

### Input
```
4
3
JOB 1 50
SomeJob 2 50
AnotherJob 1 100
2
SomeValue 3 50
OtherValue 2 50
2
SomeValue 2 60
OtherValue 2 50
2
SomeValue 2 50
OtherValue 2 50
```

### Output
```
AnotherJob SomeJob
OtherValue SomeValue
SomeValue OtherValue 
SomeValue OtherValue
```

Thanks to @Sips for suggesting the challenge.

## Submission and Grading 

- code must be written in python
- `eval` and `exec` functions are not allowed same goes for `import`

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/PreviousChallenges/Challenge_57_2)
