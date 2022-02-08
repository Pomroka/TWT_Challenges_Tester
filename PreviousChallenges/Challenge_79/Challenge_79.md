# Challenge 79: Spontaneous interview | A programming journey #1

You're walking down a street with what seems as a grass plain to your right. Someone is walking towards you in the distance. As they approach, you recognize Tim. "Omg Tim, it's so nice to finally meet you in real life, I've watched hundreds of your videos. You have the best YouTube channel of them all!"  
"Haha thx. Hey, you mind solving a little problem for me?"  
"Not at all, what's up?"  
"Okay, here it goes. By the way, if you can solve it, there's a seat in the office for you."

## Task

You are given a number `T` the number of tests cases. `T` cases follow. For each case you are given a `string` and a `character` on the next line. Encode the string using the single character `XOR` cipher with the given character as your cipher key.

## Example

### Input
```
2
aaa
5
bye
7
```

### Output
```
TTT
UNR
```

### Explanation

Let's say you have a random string of any length, and a single character we'll call a key. Split the string into individual characters then take each character separately and perform a XOR operation on it with the key you have, then add the resulting character into another string. That resulting string is what you need to print, and the whole process is called single character XOR encoding.

### NOTE:
- `string` - upper and lower english letters `[a-zA-Z]`
- `character` - digit `[0-9]`

## Submissions and grading

Code can be written in either of these languages:

- `Python 3.9`     - fully supported by my tester
- `C++ - G++ 10.3` - should work with my tester 
- `Ruby 3.0`       - wasn't tested, try yourself
- `Golang 1.16`    - should work with my tester

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/PreviousChallenges/Challenge_79)