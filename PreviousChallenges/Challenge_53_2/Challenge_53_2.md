# Challenge 53.2: Simon says

**Only what Simon said counts!**

On each test, you will be given a string of any length. This string can be anything. Your job is to output what Simon said!

## Rules:

- Anyone other than Simon doesn't count
- If Simon didn't says (must be `Simon says ...`, not Simon shouts or Simon say), it doesn't count
- If Simon's speech is empty after removing white spaces, it doesn't count
- Simon can only say at the beginning of the string
- If the string is not Simon saying something, output `...`. Otherwise, output what Simon said.

Line 1: an integer `n`
Next `n` lines: each lines contains a string. After applying the rules print the result in a single line.

## Examples

### Input 
```
10
Simon says Hello World!
Tim says Simon says I didn't say that...
Simon jumps high
Simon says
Simon saysok
I like apples
Simon says Tim says hello to me
simon says ello
 simon says ello
          SimOn said did i say this?
```

### Output 
```
Hello World!
...
...
...
...
...
Tim says hello to me
ello
...
...
```

## Submissions and Grading 

- code must be written in python
- `eval` and `exec` functions are not allowed same goes for `import`

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/PreviousChallenges/Challenge_53_2)
