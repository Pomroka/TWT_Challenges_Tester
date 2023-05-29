# Testers for TechWithTim Discord weekly challenges

[![latest](https://img.shields.io/badge/latest-Challenge--159-orange)](https://github.com/Pomroka/TWT_Challenges_Tester/releases/latest) [![Python version](https://img.shields.io/badge/python-3.6*%20%7C%203.7*%20%7C%203.8%20%7C%203.9%20%7C%203.10%20%7C%203.11-blue)](#supported-python-version) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

![TWT Logo](logo1.png "TWT Logo")

You will find here my testers for weekly challenges.

----------

- [**How to use?**](#how-to-use)
- [New tester (Challenge 73 and newer)](#new-tester-challenge-73-and-newer)
  - [To test solution in languages other than Python](#to-test-solution-in-languages-other-than-python)
  - [Examples](#examples)
  - [Custom test cases](#custom-test-cases)
- [**Supported Python version**](#supported-python-version)
- [Old tester (Challenge 72 and older)](#old-tester-challenge-72-and-older)
- [Some possible errors](#some-possible-errors)
- [How to download individual challenge tester/file from GitHub?](#how-to-download-individual-challenge-testerfile-from-github)

----------

## **How to use?**

## New tester (Challenge 73 and newer)

Download tester file `test_challenge_XX.py` and file with test cases `test_cases.json` place them in same folder where is your file with solution.

Make sure Python has right to save to this folder.

This tester will create one file `temp_solution_file.py` make sure there's no such
file in same folder or there's nothing important in it, cos it will be **overwritten!**

You can configure tester editing tester file and changing `CONFIGURATION` section or using command line arguments.

Run with flag `-h` or `--help` for more information how to use command line arguments.

```sh
python test_challenge_159.py --help
```

Change `SOLUTION_SRC_FILE_NAME` to your file name in `CONFIGURATION` section or use `-s solution_file.py`.

### To test solution in languages other than Python

Use `-c command` or change `OTHER_LANG_COMMAND` to command to run your solution for not compiled languages or to already compiled executable for compiled languages. For multi-word `command` command line argument surround it in quotes `"multi word command"`

### Examples

```py
OTHER_LANG_COMMAND = "Cpp/c159_cpp.exe"  # relative to tester file path to compiled windows executable
OTHER_LANG_COMMAND = "/home/user/Dev/Challenge159/c159_c"  # absolute path to compiled Linux executable
OTHER_LANG_COMMAND = "c159_rust.exe"  # name of compiled file in same folder as tester
OTHER_LANG_COMMAND = "java -cp Java/ c159_java.Main"  # command to run solution in non compiled language
OTHER_LANG_COMMAND = ""  # leave empty if you want to test python solution
```

```sh
> python test_challenge_159.py -c "java -cp Java/ c159_java.Main"

$ python test_challenge_159.py -c Rust/c159_rust/target/release/c159_rust
```

If you want to see your solution length in other languages than Python change `SOLUTION_FILE_NAME` to your solution source code file name.

If this tester wasn't prepared by me for the challenge you want to test,
you may need to adjust other configuration settings. Read the comments on each.

### Custom test cases

You can use test cases from official TWT challenge tester published after testing or in same format. Tester will convert them to format described below.

If you want to use own test_cases, they must be in JSON format.

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

All values must be strings! Cast all ints, floats, etc. to string before dumping JSON!

## **Supported Python version**

- **Python 3.8+** works without modification
- **Python 3.7** you need to comment out line `otter="\N{otter}",`
- **Python 3.6** you need to comment out lines:
  - `from dataclasses import dataclass`
  - both lines that have `@dataclass`
  - comment out whole block starting with line `if Config.USE_EMOJI:` up to and including `else:` and unindent next line
- older Python version not supported

----------

## Old tester (Challenge 72 and older)

Download tester file `test_challenge_XX.py` and file with test cases `test_cases_ch_XX.py` place them in same folder where is your file with solution.

Import your solution in line `92`, and run tester file

```sh
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

## Some possible errors

- `None` in `"Your output"`: Your solution didn't print for all cases.

- `None` in `"Input"`: Your solution print more times than there are cases.

  - If you see `None` in `"Input"` or `"Your output"` don't check failed cases until you fix problem with printing, cos "Input" and "Your output" are misaligned after first missing/extra print

- `"Your Output"` looks like `"Expected"` but tester show it's wrong. Check if you print trailing spaces.

- `StopIteration`: Your solution try to get more input than there is test cases

  - If you use `open(0)` instead of `input` you get `StopIteration` error in my tester or tester will hang waiting for EOF char not presented in input data
  - to avoid this use one of:
    - set `OTHER_LANG_COMMAND = "python to_submit_ch_159.py"`
    - run `python test_challenge_159.py -c "python to_submit_ch_159.py"`
- If you call your functions inside `if __name__ == '__main__':` your functions won't be called by default cos your solution is imported
  - to avoid this use one of:
    - set `OTHER_LANG_COMMAND = "python to_submit_ch_159.py"`
    - run `python test_challenge_159.py -c "python to_submit_ch_159.py"`
    - or don't use `if __name__ == '__main__':`

----------

## How to download individual challenge tester/file from GitHub?

You can switch branch to branch with that challenge, then click `Code` and `Download ZIP`

Or in **Releases** section click `Challenge XX` and download `source_code (...)`.

Or from command line:

```sh
# Linux
$ wget https://raw.githubusercontent.com/Pomroka/TWT_Challenges_Tester/master/Challenge_159/test_cases.json

# Windows 10
> curl -o test_cases.json https://raw.githubusercontent.com/Pomroka/TWT_Challenges_Tester/master/Challenge_159/test_cases.json
```

Or use [https://downgit.github.io/#/home](https://downgit.github.io/#/home) (ready to use link in Challenge_XX.md)
