# Testers for TechWithTim Discord weekly challenges

You will find here my testers for weekly challenges.

----------


## How to use? 

Download tester file `test_challenge_XX.py` and file with test cases `test_cases_ch_XX.py` place them in same folder where is your file with solution.

Import your solution in line `92`, and run tester file
```
>python test_challenge_XX.py
```
If you see some weird chars instead of colors in output or don't want colors
switch `COLOR_OUT` to `False` in line `30`

If there is more than one `test_cases_ch_XXx.py` file you can change import in line `28` or rename test case file removing letter after challenge number to use it.

----------

**WARNING:** My tester ignores printing in `input()` but official tester **FAILS** if you print something in `input()`

**Don't do that:**
```py
input("What is the test number?")
```
Use empty input: `input()`

----------

## Some possible errors:

`None` in `"Your output"`: Your solution didn't print for all cases.

`None` in `"Input"`: Your solution print more times then there is cases.

If you see `None` in `"Input"` or `"Your output"` don't check failed cases until you fix problem with printing, cos "Input" and "Your output" are misaligned after first missing/extra print

`StopIteration`: Your solution try to get more input then there is test cases
