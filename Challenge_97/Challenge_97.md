# Challenge 97: Banik's House

**Difficulty: 5/10**  
It's Banik's birthday! Staff members of TWT are invited to Banik's house.
However, the road Banik's house is in is quite crowded, and many staff members struggled to find Banik's house.

Luckily, every house along the road has a color (The entire house is in that color), labelled from color `A` to color `Z`, inclusively. Two houses may have the same color. Banik thought if he could give everyone a unique pattern of colors, they should find his house easier.

Banik wants to know the smallest value of `K` such that if a staff looks at any sequence of `K` consecutive houses, he can uniquely determine the location of that sequence along the road.

Say the houses are colored `ABCDABC`. If Banik gives a sequence of `3` colors, even though `CDA` is unique, it might be `ABC`, which occurs twice along the road. However, every `4-color` sequence is unique along the road. Therefore, the answer is `4`.

## Task

You are given a number `T` and `T` testcases follow, for each testcase:  
You are given a positive integer `N`. The next line contains `N` characters, each in the range `[A, Z]`, which is the colors of houses along the road.  
Output the smallest possible value of `K`, as described above.

### Examples

#### Input

```rs
3
7
ABCDABC
18
HAPPYBIRTHDAYBANIK
14
BANIKBANSBANIK
```

#### Output

```rs
4
3
6
```

#### Note

`1 ≤ T`
`1 ≤ N ≤ 100`

### Submissions

Code can be written in any of these languages:

- `Python` 3.10
- `C/C++` (GCC 10.3)
- `Ruby` 3.1
- `Golang` 1.16
- `Java` 18 (Open JDK)
- `Rust` 1.59
- `C#` 10 (.Net 6.0)

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_97)
