# Challenge 56.1: Contour shifting

Tim got a rectangular array matrix for his birthday, and now he's thinking about all the fun things he can do with it. He likes shifting a lot, so he decides to shift all of its i-contours in a clockwise direction if i is even, and counterclockwise if i is odd.

Here is how Tim defines `i-contours`:

- the `0-contour` of a rectangular array is the union of left and right columns as well as top and bottom rows.
- consider the initial matrix without the `0-contour`: its `0-contour` is the first contour.
- all subsequent contours are a union of left and right columns and top and bottom rows if the previous contour is removed.

## Example

### Input
```
1
5 4
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
17 18 19 20
```

### Output
```
5 1 2 3
9 7 11 4
13 6 15 8
17 10 14 12
18 19 20 16
```

## Submissions and Grading

- code must be written in python
- `eval` and `exec` functions are not allowed same goes for `import`


### Note

- each number is separated from a number to its side by a single space in both input and output
- the first line of the input specifies the number of cases
- the second line of the input specifies the number of rows then columns of the matrix


To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/PreviousChallenges/Challenge_56_1)
