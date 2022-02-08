# Challenge 58.1: Push Box Game

Given the game board, your task is to find the new board after applying the movements.

You are given number `T`. `T` test cases follow. For each test case you are given `n s` where `n` is a number (the height of the board) and `s` is a string of the movements to do. `r`, `l`, `u`, `d` for right, left, up, down in order. `n` lines follow defining the board describing the board.

The elements in the board are:

- `#` representing a wall. Can't be pushed. (`║` in `test_cases_58_1_2.py`)
- `B` representing a box. Can be pushed.
- `U` representing the player. The one you control. 

You can guarantee that:

- There will be always 1 Player.
- Board will be always surrounded by walls.

### Notes: 

- When you hit a wall, your position doesn't change

## Example

### Input
```
1
5 lululddr
#######
#     #
#   B #
#   #U#
#######
```

### Output
```
#######
#     #
#   U #
#  B# #
#######
```

## Submission and Grading 

- code must be written in python
- `eval` and `exec` functions are not allowed same goes for `import`

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/PreviousChallenges/Challenge_58_1)
