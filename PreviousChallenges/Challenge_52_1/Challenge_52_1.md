# Challenge 52.1: Syllables

## Task:

Find the syllables of a given word:

- If one consonant follows a vowel then divide the word between the vowel and the consonant. Only if there is something after the consonant that follows a vowel
- If two consonants follow a vowel then divide the word between the two consonants.
- When the last letter is `"e"` and the letter before it is a consonant then it would become a silent letter and would therefore be added to the syllable before instead of being its own syllable.

Return a list of syllables of the given word.

## Example:

First input `n` is the number of cases.  
Next `n` lines are words

### Input
```
3
pokemon
pancake
hotel
```

### Output: 
```
po ke mon
pan cake
ho tel
```

### Notes:

- Vowels are `a`, `e`, `i`, `o`, `u`, `y`, yes `y` is included.  
- There will only be a maximum of `2` consonants in a row and `one` vowel in a row

## Submissions and Grading 

- code must be written in python
- `eval` and `exec` functions are not allowed same goes for `import`

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/PreviousChallenges/Challenge_52_1)
