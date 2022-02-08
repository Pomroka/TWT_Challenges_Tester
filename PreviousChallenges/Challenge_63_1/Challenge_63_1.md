# Challenge 63.1: Do Your Job And Match

They've found the treasure, Avib is heading home now. On his way he noticed he was missing some of the treasure he got. When he looked back he saw footsteps in the sand. Stopid thief, stealing in the desert.

Avib realized there was no way he could figure out who the thief is without some help. So he called up his friends, they told him that apparently the nearest city holds a database matching foot shape and size to each individual that lives there. So Avib got on a phone call with the city forensics department, and told them his story.

You work in that department, your job is to match Avib's description to anything that will fit it in the database.

## Task

Find all possible suspects.

### Examples

You are given a number `T` the number of tests cases. `T` lines follow each line is a test case which has an integer `k` and a string `s` separated by a `" || "`, `k` lines follow being what's in the database. Output all possible suspects separated by `", "`.

### Input
```
3
3 || square, 10in
square, 10in: Leslie
oval, 15in: Isabella
circle, 9in: Derek
4 || red, big, ?
yellow, big, f: Isabella
red, big, m: Jhon
black, small, m: Jamal
red, big, f: Sara
2 || ?
square: Tomas
circle: Smith
```

### Output
```
Leslie
Jhon, Sara
Tomas, Smith
```

## Submissions and Grading

- code must be written in python
- `eval`, `exec` and `open` functions are not allowed same goes for `import`

**Note:** `?` means it can be anything

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/PreviousChallenges/Challenge_63_1)