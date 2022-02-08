# Challenge 62.1: The door is locked

After some time in the desert alone, avib was going to give up until his friend HETHAT showed up and helped him. HETHAT had known that someone else knows about the treasure but he didn't know who it was. He wanted to help his friend avob get to it first. They found the door to the treasure and Alex was there too, he was the one who knew about the treasure other than avob. The door was locked and the key was in encrypted message. The three of them will work together now to open the door.

The encoded message is read one character at a time and the following steps are taken:

- If the character read is a `letter`, that `letter` is written onto the tape.
- If the character read is a `digit`, the entire current tape is repeatedly written `digit-1` more times in total.

## Task

Given `s` a string represents the encrypted message and `k` and integer find and output the `k-th` letter (1 indexed) in the decoded string.

## Examples

You are given a number `T` the number of tests cases. `T` lines follow, each line is a test case which has a string and an integer separated by a space `s k`

### Input
```
5
a3b 4
ha22 5
a99999 7500
ab2c3 10
a2b3c4d56789999e999999999 100000000
```

### Output
```
b
h
a
c
b
```

### Explanation 

- The decoded string is `"aaab"`. The `4th` letter in the string is `"b"`.
- The decoded string is `"hahahaha"`.  The `5th` letter is `"h"`.
- The decoded string is `"a"` repeated `9 ** 5` times.  The `7500th` letter is `"a"`.
- The decoded string is `"ababcababcababc"`.  The `10th` letter is `"c"`.
- The decoded string is ... Well you get it


## Submissions and Grading

- code must be written in python
- `eval`, `exec` and `open` functions are not allowed same goes for `import`


### NOTE:

- `s` will only contain lowercase letters and digits `2` through `9` and it will always start with a letter.
- It's guaranteed that `k` is less than or equal to the length of the decoded string.

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/PreviousChallenges/Challenge_62_1)