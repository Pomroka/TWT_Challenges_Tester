# Challenge 61.1: The cards

avob had fun with his friend but now he has to go to the desert to continue his journey to find the treasure. avob followed the map which lead him into a dark cave (there was a dragon inside and avob found it jk or not).

In the cave he found a part of the treasure and another map which leads him to the next part of the treasure. avob decided to sleep that night in the cave but he forgot that he doesn't have enough water.

The next day when he wakes up he finds a lion eating him jk again and discovers that he doesn't have enough water. Going to the desert without water? He has a `x` liters of water, each liter gives him the strength to walk `n` km. He decides to call you with your special phone that works anywhere (we don't sell that phone here anymore). Help avob find the nearest place he can reach with other people.

## Task

You have a map which has the exact location of avob, help him find the nearest place with people in it.

### Input

You are given a number `T`. `T` test cases follow.  
On the first line you are given `x` and `n` space separated, where `x` is the amount of liters of water avob has and `n` is the distance avob can walk after drinking `1` liter of water. On the second line you are given two numbers `a` and `b` where `a` and `b` are the dimensions of the map. `a + 2` lines follow, each line as `b + 2` chars, each char is either:

-  `"#"` : a wall
-  `"*"` : a place with people in it
-  `" "` : desert
-  `"A"` : avob

### Output

Knowing that each block in the map is `100` meter help avob. Output `true` if avob can reach a place which has people otherwise, print `false`.

## Examples

### Input
```
1
1 1
6 10
############
#*      *  #
#       *  #
#         *#
#          #
#          #
# A        #
############
```

### Output
```
true
```

### Notes:

- avob can't move diagonally
- there won't be any walls inside the map

## Submission and Grading 

- you have to submit in a file
- code must be written in python
- `eval` and `exec` functions are not allowed same goes for `import` and `open`

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/PreviousChallenges/Challenge_61_1)