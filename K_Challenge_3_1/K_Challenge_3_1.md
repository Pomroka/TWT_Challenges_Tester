
# K-Challenge 3: 1st One

You're looking to move into a new apartment, and you're given a list of blocks where each block contains an apartment that you could move into. In order to pick your apartment, you want to optimize its location. You also have a list of requirements: a list of buildings that are important to you (last line of input). 

For instance, you might value having a school and a gym near your apartment. The list of blocks
that you have contains information at every block about all of the buildings
that are present and absent at the block in question. 

For example, for every block, you have information whether a school, a pool, an office, and a gym are present or not.

In order to optimize your life, you want to minimize the farthest distance you'd have to walk from your apartment to reach all of your required buildings. 

Write a function that takes in a list of blocks and a list of your required buildings and that returns the location (the index) of the block that is most optimal for you.

## Format:

First input `N` number of blocks, then follows `N` input with list of facilities availability, and last input with list of requirements.

### Input:
```
5
office:0 gym:0 school:1 store:0 pool:1
office:1 gym:1 school:0 store:0 pool:0
office:0 gym:1 school:1 store:0 pool:0
office:1 gym:0 school:1 store:0 pool:1
office:0 gym:0 school:1 store:1 pool:0
office:0 gym school store
```

### Output:
```
3
```

### Explanation:

- From the first block (index `0`), you have to go `1` block further for gym, `4` blocks further for store
- From the second block, you have to go `1` block further for school, `3` blocks further for store
- From the third block, you have to go `2` block further for store
- From the fourth block, you have to go `1` block further for gym and `1` blocks further for store
- From the fifth block, you have to go `2` block further for gym

From the block fourth (index `3`) biggest distance is `1` to any facilities that are important to you.

## Note:
- `1` stands for `True` and `0` stands for `False`
- There can be any amenities not just gym, school, store
- There won't be two answers

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/K_Challenge_3_1)
