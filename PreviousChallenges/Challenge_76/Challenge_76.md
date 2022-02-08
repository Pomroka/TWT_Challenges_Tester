# Challenge 76: Who's the murderer? | Amogus #6

M7MD: “Biz, Tekgar, I got an idea.”  
Biz: “What’s that?”  
M7MD: “Let’s go to each crime scene, get a DNA sample off of the murder weapons, and compare it to everyone on board.”  
Biz: “Let’s do it”  
Tekgar: “:smilecat:”  
Another meeting is called.  
Biz: “Hey everyone sorry for the repeated disturbance, but we may have the answer to who the murderer is.”  
Avib: “How?”  
Biz: “M7MD?”  
M7MD: “So we went to each crime scene, got a DNA sample from the murder weapons, then ran both of them against the DNA   of each of us on board.”  
Murderer: “Oh shit.”

## Task

Given `T` number of testcases, you need to accept:

1. A `half-DNA` strand found at the crime scene (say this is murder_DNA)
2. `n`, an integer denoting how many members are onboard
3. For `n` lines - the full DNA strand of every staff member on board, and their names (say this is DNA_list)

You need to construct the full DNA strand of the murderer (will explain more about this), and then compare the full DNA strand of murder_DNA with the full DNA strand of every staff member. The member who shares the most full DNA with the murderer is the prime suspect. Print the name of the prime suspect.

`DNA` is a double helix (essentially, two ropes held together with bonds) is made up of four subunits - Adenine, Thymine, Guanine, Cytosine. `A` and `T` always bond together, and `C` and `G` always bond together, thus holding DNA together. You will be given the subunits on one of the "ropes", and you need to construct the other half, by inserting each character's bonding pair into the DNA given (`A` -> `T` will be inserted, `G` -> `C` will be inserted, `C` -> `G` will be inserted, and `T` -> `A` will be inserted).

## Example

If you are given `ACGAT` as a half strand, then:

1. `A` -> Insert a `T` next to it
2. `C` -> insert a `G` next to it
3. `G` -> Insert an `C` next to it
4. `A` -> Insert a `T` next to it
5. `T` -> Insert a `A` next to it

And you get `ATCGGCATTA`

### Sample Input:
```
1                         -> There is 1 test case
ACGA                      -> This is the half strand of DNA found at the murder scene
3                         -> 3 people onboard
AGGTAAAT Avib             -> Full strand of avib's DNA
AGAGAGTC Tekgar           -> Full strand of tekgar's DNA
CCCTAAAG Espiobest        -> Full strand of Espiobest's DNA
```

### Output
```
Avib
```

### Explanation

Murderer's full DNA strand     - `ATCGGCAT`  
`Avib'` full DNA strand        - `AGGTAAAT`  
`Tekgar's` full DNA strand     - `AGAGAGTC`  
`Espiobest's` full DNA strand  - `CCCTAAAG`  

`Avib` shares `3` characters in the same position with the murderer (`A`, `A`, `T`)  
`Tekgar` shares `2` characters in the same position with the murderer (`A`, `G`)  
`Espiobest` shares `2` characters in the same position with the murderer (`C`, `A`)  

So `Avib` is the murderer :sadguncat:

In case two members share the same number of characters with the murderer's DNA, return both of them, arranged alphabetically (Why can't we have more than one murderer)

The length of the full DNA strand of each member will always be the same, and will be equal to 2 * length of murderer's half DNA strand

Challenge suggested by `@class DockerAddoct`

## Submissions and grading

- code must be written in python 3.9
- `eval`, `exec` and `open` functions are not allowed same goes for `import`

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/PreviousChallenges/Challenge_76)