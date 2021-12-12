![TWT Logo](logo1.png "TWT Logo")

# Testers for TechWithTim Discord weekly challenges

You will find here my testers for weekly challenges.

----------

## <ins>How to use?</ins>

## New tester (Challenge 73 and newer)

Download tester file `test_challenge_XX.py` and file with test cases `test_cases.json` place them in same folder where is your file with solution.

Make sure Python has right to save to this folder.

This tester will create one file `temp_solution_file.py` make sure there's no such
file in same folder or there's nothing important in it cos it will be **overwritten!**

You can configure tester editing tester fila and changing `CONFIGURATION` section or using command line arguments.

Run with flag `-h` or `--help` for more information how to use command line arguments. 

```
$ python test_challenge_XX.py --help
```

Change `SOLUTION_SRC_FILE_NAME` to your file name in `CONFIGURATION` section or use `-s solution_file.py`.

### To test solution in languages other then Python
Use `-c command` or change `OTHER_LANG_COMMAND` to command to run your solution for not compiled languages or to already compiled executable for compiled languages. For multiword `command` command line argument surround it in quotes `"multi word command"`

### Examples:
```py
OTHER_LANG_COMMAND = "Cpp/c80_cpp.exe"  # relative to tester file path to compiled windows executable
OTHER_LANG_COMMAND = "/home/user/Dev/Challenge80/c80_c"  # absolute path to compiled linux executable
OTHER_LANG_COMMAND = "c80_rust.exe"  # name of compiled file in same folder as tester
OTHER_LANG_COMMAND = "java -cp Java/ c80_java.Main"  # command to run solution in non compiled language
OTHER_LANG_COMMAND = ""  # leave empty if you want to test python solution
```

```
> test_challenge_XX.py -c "java -cp Java/ c80_java.Main"

$ test_challenge_XX.py -c Rust/c80_rust/target/release/c80_rust
```

If you want to see your solution length in other languages then Python change `SOLUTION_FILE_NAME` to your solution source code file name.


If this tester wasn't prepared by me for the challenge you want to test,
you may need to adjust other configuration settings. Read the comments on each.

### Custom test cases

If you want use own test_cases, they must be in json format.
```py
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

## **Supported Python version**

- **Python 3.8+** works without modification
- **Python 3.7** you need to comment out line `otter="\N{otter}",`
- **Python 3.6** you need to comment out lines:
  * `from dataclasses import dataclass`
  * both lines that have `@dataclass`
  * comment out whole block starting with line `if Config.USE_EMOJI:` up to and including `else:` and unindent next line
- older Python version not supported

----------

## Old tester (Challenge 72 and older)

Download tester file `test_challenge_XX.py` and file with test cases `test_cases_ch_XX.py` place them in same folder where is your file with solution.

Import your solution in line `92`, and run tester file
```
> python test_challenge_XX.py
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

------

## To download individual file from GitHub
```sh
# Linux
> wget https://raw.githubusercontent.com/Pomroka/TWT_Challenges_Tester/master/Challenge_76/test_cases.json

# Windows 10
> curl -o test_cases.json https://raw.githubusercontent.com/Pomroka/TWT_Challenges_Tester/master/Challenge_76/test_cases.json
```

To download folder use https://downgit.github.io/#/home
