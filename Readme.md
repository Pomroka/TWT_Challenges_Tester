# Testers for TechWithTim Discord weekly challenges

You will find here my testers for weekly challenges.

----------

## <ins>How to use?</ins>

## New tester (Challenge 73 and newer)

Download tester file `test_challenge_XX.py` and file with test cases `test_cases.json` place them in same folder where is your file with solution.

Make sure Python has right to save to this folder.

This tester will create one file `temp_solution_file.py` make sure there's no such
file in same folder or there's nothing important in it cos it will be **overwritten!**

Change `SOLUTION_FILE_NAME` to your file name in `CONFIGURATION` section.

If this tester wasn't prepared by me for the challenge you want to test,
you may need to adjust other configuration settings. Read the comments on each.

### Custom test cases

If you want use own test_cases, they must be in json format.
```json
[
  [ # this list can be in separated file for inputs only
    ["test case 1"], # multiline case ["line_1", "line_2", ... ,"line_n"]
    ["test case 2"],
    ...
    ["test case n"]
  ],
  [ # and this for output only
    "output 1",
    "output 2",
    ...
    "output n"
  ]
]
```
All values must be strings! Cast all ints, floats, etc. to str before dumping json!

----------

## Old tester (Challenge 72 and older)

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
