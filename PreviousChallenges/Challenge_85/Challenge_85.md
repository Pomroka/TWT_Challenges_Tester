# Challenge 85: Christmas 🎄

There are only a few days left for Christmas, and you've already set up your Christmas tree, and bought baubles to hang on the tree. However, the city corporation has released a schedule of days (list of day numbers relative to today) on which power outs will occur, which means you need to buy a battery, with enough energy to light up the baubles, on the days of the power out.

Given that there are `n` number of days to Christmas, and each bauble consumes `e` energy per day. Every day, you place one more bauble on the tree (starting from `0`) till Christmas, when the tree becomes full.

You need to figure out the energy contained in the battery that you buy. Since batteries don't ship with decimal energy levels, you'll have to round up to the nearest multiple of `5`.

## Task

You are given a number `T` and `T` testcases follow, for each testcase you need to figure out how big of a battery is needed and print it out.

## Example

### Input

```sh
1                       # 1 test case
5                       # 5 days to Christmas
0.8                     # Each bauble consumes 0.8 units of energy per day
2 3 5                   # Power outs will take place on days 2, 3 and 5
```

### Output

```sh
10
```

## Explanation

- On the first day, the tree will have `1` bauble, and since there is no power out, you don't need to use your battery.
- On the second day, the tree will have `2` baubles, and since there is a power out, you'll need to supply `2 * 0.8 = 1.6` unit of energy from your battery.
- On the third day, the tree will have `3` baubles, and since there is a power out, you'll need to supply `3 * 0.8 = 2.4` units of energy from your battery.
- On the fourth day, there is no power out scheduled.
- On the fifth day (Christmas eve), the tree will have `5` baubles, and you'll need to supply `4.0` units of energy.

So you'll need to supply a total of `8` units of energy, which means you'll need a battery that has `10` units of energy in it.

Challenge suggested by @class YoQuackAddict

## Submissions

Code can be written in either of these languages:

- `Python` 3.9
- `C++` (G++ 10.3)
- `Ruby` 3.0
- `Golang` 1.16
- `Java` 18
- `Rust` 1.52

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/PreviousChallenges/Challenge_85)
