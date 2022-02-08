# Challenge 87: One

All integer `K` satisfying `2 < K` can be written as `1111.....11` (only consisting of `1` or more `1s`) in one or more specific base. For example, you can write `3` (base `10`) as `11` in base `2`.

## Task

Given an integer `K` greater than `2`, find base `B` such as `K` can be written in the form of only one or more `1s` in base `B`.

**Input:**

First line: Integer `N` describing number of test cases
Next `N` lines:
An integer `K`

**Output:**

For each test case:
Output positive integer `B` in which `K` can be written as one or more `1s` in base `B`.
**If multiple `Bs` satisfy, output `B` with the most `1s` after writing `K` in base `B`.**

## Example

**Input:**

```rs
3
3
13
341
```

**Output:**

```rs
2
3
4
```

### Explanation

- `3 = 11` in base `2` so choose **<ins>2</ins>**.
- `13 = 111` in base `3`, `11` in base `12`. Choose **<ins>3</ins>**.
- `341 = 11111` in base **<ins>4</ins>**.

## Constraints

**2 < `K` < 10<sup>14</sup>**

Challenge suggested by @SnowballSH

## Submissions

Code can be written in either of these languages:

- `Python` 3.9
- `C++` (G++ 10.3)
- `Ruby` 3.0
- `Golang` 1.16
- `Java` 18
- `Rust` 1.52

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/PreviousChallenges/Challenge_87)
