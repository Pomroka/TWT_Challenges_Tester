"""
How to use?
Put this file, with test cases file and file with your solution in same folder.
Make sure Python has right to save to this folder.

This tester will create one file "temp_solution_file.py" make sure there's no such
file in same folder or there's nothing important in it cos it will be overwritten!

Change SOLUTION_SRC_FILE_NAME to your file name in CONFIGURATION section.

If this tester wasn't prepared by me for the challenge you want to test,
you may need to adjust other configuration settings. Read the comments on each.

If you want use own test_cases, they must be in json format.
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
All values must be strings! Cast all ints, floats, etc. to str before dumping json!

WARNING: My tester ignores printing in input() but official tester FAILS if you
        print something in input()
        Don't do that: input("What is the test number?")
        Use empty input: input()

Some possible errors:
    - None in "Your output": Your solution didn't print for all cases.
    - None in "Input": Your solution print more times then there is cases.
    - If you see None in "Input" or "Your output" don't check failed cases until
        you fix problem with printing, cos "Input" and "Your output" are misaligned
        after first missing/extra print
    - StopIteration: Your solution try to get more input then there is test cases
    - If you use `open` instead of `input` you get `StopIteration` error in my tester
        to avoid that use OTHER_LANG_COMMAND = "python to_submit_ch_83.py"
    - If you call your function inside `if __name__ == '__main__':` by default
        your functions wont be called cos your solution is imported.
        to avoid that use OTHER_LANG_COMMAND = "python to_submit_ch_83.py"
        or don't use `if __name__ == '__main__':`
"""
from __future__ import annotations

from dataclasses import dataclass


########## CONFIGURATION ################
@dataclass
class Config:

    # Name of your file with solution. If its not in same folder as this script
    # add absolute path or relative to this script file.
    # For other languages then python fill this with source code file name if
    # you want solution length to be displayed.
    # Examples:
    #   Absolute path
    # SOLUTION_SRC_FILE_NAME = "/home/user/Dev/Cpp/c83_c/c83_c/src/Main.cpp"
    #   Relative path to this script file
    # SOLUTION_SRC_FILE_NAME = "Rust/C83_rust/src/main.rs"
    #   File in same folder as this script
    SOLUTION_SRC_FILE_NAME = "to_submit_ch_129.py"

    # Command to run your solution written in other language then Python
    # For compiled languages compile yourself and use compiled executable file name
    # For interpreter languages give full command to run your solution
    # Examples:
    # OTHER_LANG_COMMAND = "c83_cpp.exe"
    # OTHER_LANG_COMMAND = "Cpp/c83_c/bin/x64/Debug/c83_c.exe"
    # OTHER_LANG_COMMAND = "Cpp/c83_c/bin/x64/Release/c83_c"
    # OTHER_LANG_COMMAND = "/home/user/Dev/Rust/c83_rust/target/release/c83_rust"
    # OTHER_LANG_COMMAND = "d:/Dev/C_Sharp/c83_cs/bin/Debug/net6.0/c83_cs.exe"
    # OTHER_LANG_COMMAND = "java -cp Java/ c83_java.Main"
    OTHER_LANG_COMMAND = ""

    # Name of file with inputs test cases (and output if SEP_INP_OUT_TESTCASE_FILE is False)
    # If test cases file is compressed, you don't need to extract it, just give name of
    # compressed file (with .gz extension)
    TEST_CASE_FILE = "test_cases.json.gz"

    # If test cases input and expected output are in separate files, name of file
    # with expected outputs for test cases. Empty string - if they in one file.
    TEST_CASE_FILE_EXP = ""

    # True - if you want colors in terminal output, False - otherwise or if your terminal
    # don't support colors and script didn't detect this
    COLOR_OUT: bool = True

    # -1 - use all test cases from test case file, you can limit here with how many
    # tests cases you want to test your solution. If you enter number bigger than
    # number of tests all tests will be used
    NUMBER_OF_TEST_CASES = -1

    # True - if you want to print some debug information, you need set:
    #   DEBUG_TEST_NUMBER to the test number you want to debug
    DEBUG_TEST: bool = False

    # Provide test number for which you want to see your debug prints. If you enter number
    # out of range, first test case will be used. (This number is 1 - indexed it is same number
    # you find when failed test case is printed in normal test). Ignored when DEBUG_TEST is False
    DEBUG_TEST_NUMBER = 1

    # True - if official challenge tester give one test case inputs and run your solution
    # again for next test case, False - if official challenge tester gives all test cases
    # once and your solution need to take care of it.
    TEST_ONE_BY_ONE: bool = False

    # True - if you want test your solution one test case by one test case, and solution
    # is written to take all test cases at once, this will add "1" as the first line input
    # Ignored if TEST_ONE_BY_ONE is False
    ADD_1_IN_OBO: bool = False

    # True - if you want to measure performance of your solution, running it multiple times
    SPEED_TEST: bool = False

    # How many test case to use per loop, same rules apply as for NUMBER_OF_TEST_CASES
    NUMBER_SPEED_TEST_CASES = -1

    # How many times run tests
    NUMER_OF_LOOPS = 2

    # Timeout in seconds. Will not timeout in middle of test case (if TEST_ONE_BY_ONE is False
    # will not timeout in middle of loop). Will timeout only between test cases / loops
    # If you don't want timeout set it to some big number or `float("inf")`
    TIMEOUT = 300

    # Set to False if this tester wasn't prepared for the challenge you testing
    # or adjust prints in `print_extra_stat` function yourself
    PRINT_EXTRA_STATS: bool = True

    # How often to update progress: must be > 0 and < 1
    # 0.1 - means update every 10% completed tests
    # 0.05 - means update every 5% completed tests
    PROGRESS_PERCENT = 0.1

    # How many failed cases to print
    # Set to -1 to print all failed cases
    NUM_FAILED = 5

    # Set to False if you want to share result but don't want to share solution length
    PRINT_SOLUTION_LENGTH: bool = True

    # If your terminal support unicode and your font has glyphs for emoji you can
    # switch to True
    USE_EMOJI: bool = False


# region #######################################################################

import argparse
import functools
import gzip
import json
import operator
import os
import platform
import subprocess
import sys
from enum import Enum, auto
from io import StringIO
from itertools import zip_longest
from pprint import pprint
from time import perf_counter
from typing import Callable, List, Tuple
from unittest import mock

TestInp = List[List[str]]
TestOut = List[str]
TestCases = Tuple[TestInp, TestOut]


def enable_win_term_mode() -> bool:
    win = platform.system().lower() == "windows"
    if win is False:
        return True

    from ctypes import byref, c_int, c_void_p, windll

    ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004
    INVALID_HANDLE_VALUE = c_void_p(-1).value
    STD_OUTPUT_HANDLE = c_int(-11)

    hStdout = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    if hStdout == INVALID_HANDLE_VALUE:
        return False

    mode = c_int(0)
    ok = windll.kernel32.GetConsoleMode(c_int(hStdout), byref(mode))
    if not ok:
        return False

    mode = c_int(mode.value | ENABLE_VIRTUAL_TERMINAL_PROCESSING)
    ok = windll.kernel32.SetConsoleMode(c_int(hStdout), mode)
    if not ok:
        return False

    return True


class Capturing(list):
    def __enter__(self) -> "Capturing":
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args: str) -> None:
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio  # free up some memory
        sys.stdout = self._stdout


def create_solution_function(path: str, file_name: str) -> int:
    if not file_name:
        return 0

    if file_name.find("/") == -1 or file_name.find("\\") == -1:
        file_name = os.path.join(path, file_name)

    if not os.path.exists(file_name):
        print(f"Can't find file {red}{file_name}{reset}!\n")
        print("Make sure:\n - your file is in same directory as this script.")
        print(" - or give absolute path to your file")
        print(" - or give relative path from this script.\n")
        print(f"Current Working Directory is: {yellow}{os.getcwd()}{reset}")

        return 0

    solution = []
    with open(file_name, newline="") as f:
        solution = f.readlines()

    sol_len = sum(map(len, solution))

    if not file_name.endswith(".py"):
        return sol_len

    tmp_name = os.path.join(path, "temp_solution_file.py")
    with open(tmp_name, "w") as f:
        f.write("def solution():\n")
        for line in solution:
            f.write("    " + line)

    return sol_len


def read_test_cases() -> TestCases:
    if test_cases_file.endswith(".gz"):
        with gzip.open(test_cases_file, "rb") as g:
            data = g.read()
        try:
            test_cases = json.loads(data)
        except json.decoder.JSONDecodeError:
            print(
                f"Test case file {yellow}{test_cases_file}{reset} is not valid JSON file!"
            )
            raise SystemExit(1)
    else:
        with open(test_cases_file) as f:
            try:
                test_cases = json.load(f)
            except json.decoder.JSONDecodeError:
                print(
                    f"Test case file {yellow}{test_cases_file}{reset} is not valid JSON file!"
                )
                raise SystemExit(1)

    if Config.TEST_CASE_FILE_EXP:
        with open(test_out_file) as f:
            try:
                test_out = json.load(f)
            except json.decoder.JSONDecodeError:
                print(
                    f"Test case file {yellow}{test_out_file}{reset} is not valid JSON file!"
                )
                raise SystemExit(1)
        test_inp = test_cases
    else:
        test_inp = test_cases[0]
        test_out = test_cases[1]

    if isinstance(test_cases[0], dict):
        return convert_official_test_cases(test_cases)

    return test_inp, test_out


def convert_official_test_cases(test_cases: List[dict[str, str]]) -> TestCases:
    test_inp, test_out = [], []
    for case in test_cases:
        try:
            test_inp.append(case["Input"].split("\n"))
            test_out.append(case["Output"])
        except KeyError:
            print(f"Test case {yellow}{case}{reset} is not valid format!")
            raise SystemExit(1)

    return test_inp, test_out


@dataclass
class Emoji:
    stopwatch: str = ""
    hundred: str = ""
    poo: str = ""
    snake: str = ""
    otter: str = ""
    scroll: str = ""
    filebox: str = ""
    chart: str = ""
    rocket: str = ""
    warning: str = ""
    bang: str = ""
    stop: str = ""
    snail: str = ""
    leopard: str = ""


class Lang(Enum):
    PYTHON = auto()
    OTHER = auto()


# endregion ####################################################################


def print_extra_stats(test_inp: TestInp, test_out: TestOut, num_cases: int) -> None:
    print(f" - Max len S: {yellow}" f"{max(len(x[0]) for x in test_inp):_}{reset}")
    print(
        f" - Average len S: {yellow}"
        f"{sum(len(x[0]) for x in test_inp) // num_cases:_}{reset}"
    )


def print_begin(
    format: str,
    num_cases: int,
    test_inp: TestInp,
    test_out: TestOut,
    *,
    timeout: bool = False,
) -> None:
    command = Config.OTHER_LANG_COMMAND

    if lang is Lang.PYTHON:
        running = f"{emojis.snake} {yellow}Python solution{reset}"
    else:
        running = f"{emojis.otter} {yellow}{command[command.rfind('/') + 1:]}{reset}"

    print(f"{emojis.rocket}Started testing, format {format}:")
    print(f"Running:{running}")
    print(f" - Number of cases{emojis.filebox}: {cyan}{num_cases:_}{reset}")
    if timeout:
        print(f" - Timeout: {red}{Config.TIMEOUT}{reset} seconds{emojis.stop}")
    if Config.PRINT_EXTRA_STATS:
        print_extra_stats(test_inp[:num_cases], test_out[:num_cases], num_cases)
    if (
        solution_len
        and Config.PRINT_SOLUTION_LENGTH
        and (
            lang is Lang.OTHER
            and not Config.SOLUTION_SRC_FILE_NAME.endswith(".py")
            or Config.OTHER_LANG_COMMAND.endswith(".py")
            or lang is Lang.PYTHON
        )
    ):
        print(f" - Solution length{emojis.scroll}: {green}{solution_len}{reset} chars.")
    print()


def print_summary(i: int, passed: int, time_taken: float) -> None:
    if Config.NUM_FAILED >= 0 and i - passed > Config.NUM_FAILED:
        print(
            f"{emojis.warning}Printed only first {yellow}{Config.NUM_FAILED}{reset} "
            f"failed cases!{emojis.warning}"
        )
        print(
            f"\rTo change how many failed cases to print change {cyan}NUM_FAILED{reset}"
            " in configuration section.\n"
        )
    e = f"{emojis.hundred}" if passed == i else f"{emojis.poo}"
    print(
        f"\rPassed: {green if passed == i else red}{passed:_}/{i:_}{reset} tests{e}{emojis.bang}"
    )
    print(f"{emojis.stopwatch}Finished in: {yellow}{time_taken:.4f}{reset} seconds")


def print_speed_summary(speed_num_cases: int, loops: int, times: List[float]) -> None:
    times.sort()
    print(
        f"\rTest for speed passed{emojis.hundred}{emojis.bang if emojis.bang else '!'}\n"
        f" - Total time: {yellow}{sum(times):.4f}"
        f"{reset} seconds to complete {cyan}{loops:_}{reset} times {cyan}"
        f"{speed_num_cases:_}{reset} cases!"
    )
    print(
        f" -{emojis.leopard} Average loop time from top {min(5, loops)} fastest: "
        f"{yellow}{sum(times[:5])/min(5, loops):.4f}{reset} seconds /"
        f" {cyan}{speed_num_cases:_}{reset} cases."
    )
    print(
        f" -{emojis.leopard} Fastest loop time: {yellow}{times[0]:.4f}{reset} seconds /"
        f" {cyan}{speed_num_cases:_}{reset} cases."
    )
    print(
        f" - {emojis.snail}Slowest loop time: {yellow}{times[-1]:.4f}{reset} seconds /"
        f" {cyan}{speed_num_cases:_}{reset} cases."
    )
    print(
        f" - {emojis.stopwatch}Average loop time: {yellow}{sum(times)/loops:.4f}{reset} seconds"
        f" / {cyan}{speed_num_cases:_}{reset} cases."
    )


def find_diff(out: str, exp: str) -> str:
    result = []
    for o, e in zip_longest(out, exp):
        if o == e:
            result.append(o)
        elif o is None:
            result.append(f"{red_bg}~{reset}")
        else:
            result.append(f"{red_bg}{o}{reset}")

    return "".join(result)


def check_result(
    test_inp: TestInp, test_out: TestOut, num_cases: int, output: List[str]
) -> Tuple[int, int]:
    passed = i = oi = 0
    for i, (inp, exp) in enumerate(
        zip_longest(test_inp[:num_cases], test_out[:num_cases]), 1
    ):
        out_len = len(exp.split("\n"))
        out = "\n".join(output[oi : oi + out_len])
        oi += out_len
        if out != exp:
            if i - passed <= Config.NUM_FAILED or Config.NUM_FAILED == -1:
                print(f"Test nr:{i}\n      Input: {cyan}")
                pprint(inp)
                print(f"{reset}Your output: {find_diff(out, exp) if out else f'{red_bg}None{reset}'}")
                print(f"   Expected: {green}{exp}{reset}\n")
        else:
            passed += 1

    if num_cases + sum(x.count("\n") for x in test_out[:num_cases]) < len(output) - 1:
        print(
            f"{red}{emojis.warning}Your output has more lines than expected!{emojis.warning}\n"
            f"Check if you don't print empty line at the end.{reset}\n"
        )
    return passed, i


########################################################################


def test_solution_aio(test_inp: TestInp, test_out: TestOut, num_cases: int) -> None:
    test_inp_: List[str] = functools.reduce(operator.iconcat, test_inp[:num_cases], [])

    @mock.patch("builtins.input", side_effect=[str(num_cases)] + test_inp_)
    def test_aio(input: Callable) -> List[str]:
        with Capturing() as output:
            solution()

        return output

    print_begin("All in one", num_cases, test_inp, test_out)

    start = perf_counter()
    output = test_aio()  # type: ignore
    end = perf_counter()

    passed, i = check_result(test_inp, test_out, num_cases, output)

    print_summary(i, passed, end - start)


def speed_test_solution_aio(
    test_inp: TestInp, test_out: TestOut, speed_num_cases: int
) -> None:
    test_inp_: List[str] = functools.reduce(
        operator.iconcat, test_inp[:speed_num_cases], []
    )

    @mock.patch("builtins.input", side_effect=[str(speed_num_cases)] + test_inp_)
    def test_for_speed_aio(input: Callable) -> bool:

        with Capturing() as output:
            solution()

        return "\n".join(output) == "\n".join(test_out[:speed_num_cases])

    loops = max(1, Config.NUMER_OF_LOOPS)
    print("\nSpeed test started.")
    print(f"Running: {yellow}Python solution{reset}")
    print(f'Testing {cyan}{speed_num_cases}{reset} cases, format "All in one":')
    print(f" - Number of loops: {cyan}{loops:_}{reset}")
    print(f" - Timeout: {red}{Config.TIMEOUT}{reset} seconds")
    if Config.PRINT_EXTRA_STATS:
        print_extra_stats(
            test_inp[:speed_num_cases], test_out[:speed_num_cases], speed_num_cases
        )
    print()

    times = []
    for i in range(loops):
        start = perf_counter()
        passed = test_for_speed_aio()  # type: ignore
        times.append(perf_counter() - start)
        if not passed:
            print(f"{red}Failed at iteration {i + 1}!{reset}")
            break
        if sum(times) >= Config.TIMEOUT:
            print(f"{red}Timeout at {i + 1} iteration!{reset}")
            break
        if 1 < loops <= 10 or not i % (loops * Config.PROGRESS_PERCENT):
            print(f"\rProgress: {yellow}{i:>{len(str(loops))}}/{loops}{reset}", end="")
    else:
        print_speed_summary(speed_num_cases, loops, times)


def test_solution_obo(test_inp: TestInp, test_out: TestOut, num_cases: int) -> None:
    def test_obo(test: List[str]) -> Tuple[float, str]:
        @mock.patch("builtins.input", side_effect=test)
        def test_obo_(input: Callable) -> List[str]:
            with Capturing() as output:
                solution()

            return output

        start = perf_counter()
        output = test_obo_()  # type: ignore
        end = perf_counter()

        return end - start, "\n".join(output)

    print_begin("One by one", num_cases, test_inp, test_out, timeout=True)

    times = []
    passed = i = 0
    for i in range(num_cases):
        test = ["1"] + test_inp[i] if Config.ADD_1_IN_OBO else test_inp[i]
        t, output = test_obo(test)
        times.append(t)
        if test_out[i] != output:
            if i - passed <= Config.NUM_FAILED or Config.NUM_FAILED == -1:
                print(f"\rTest nr:{i + 1}             \n      Input: {cyan}")
                pprint(test)
                print(f"{reset}Your output: {red}{output[0]}{reset}")
                print(f"   Expected: {green}{test_out[i]}{reset}\n")
        else:
            passed += 1
        if sum(times) >= Config.TIMEOUT:
            print(f"{red}Timeout after {i + 1} cases!{reset}")
            break
        if 1 < num_cases <= 10 or not i % (num_cases * Config.PROGRESS_PERCENT):
            print(
                f"\rProgress: {yellow}{i + 1:>{len(str(num_cases))}}/{num_cases}{reset}",
                end="",
            )

    print_summary(i + 1, passed, sum(times))


def speed_test_solution_obo(
    test_inp: TestInp, test_out: TestOut, speed_num_cases: int
) -> None:
    def test_for_speed_obo(test: List[str], out: str) -> Tuple[float, bool]:
        @mock.patch("builtins.input", side_effect=test)
        def test_obo_(input: Callable) -> List[str]:
            with Capturing() as output:
                solution()

            return output

        start = perf_counter()
        output = test_obo_()  # type: ignore
        end = perf_counter()

        return end - start, "\n".join(output) == out

    loops = Config.NUMER_OF_LOOPS
    print("\nSpeed test started.")
    print(f"Running: {yellow}Python solution{reset}")
    print(f'Testing {cyan}{speed_num_cases}{reset} cases, format "One by one":')
    print(f" - Number of loops: {cyan}{loops:_}{reset}")
    print(f" - Timeout: {red}{Config.TIMEOUT}{reset} seconds")
    if Config.PRINT_EXTRA_STATS:
        print_extra_stats(
            test_inp[:speed_num_cases], test_out[:speed_num_cases], speed_num_cases
        )
    print()

    timedout = False
    times: List[float] = []
    for i in range(loops):
        loop_times = []
        for j in range(speed_num_cases):
            test = ["1"] + test_inp[j] if Config.ADD_1_IN_OBO else test_inp[j]

            t, passed = test_for_speed_obo(test, test_out[j])
            loop_times.append(t)

            if not passed:
                print(f"\r{red}Failed at iteration {i + 1}!{reset}")
                break
            if sum(times) >= Config.TIMEOUT:
                print(f"\r{red}Timeout at {i + 1} iteration!{reset}")
                timedout = True
                break
        if timedout:
            break
        times.append(sum(loop_times))
        if 1 < loops <= 10 or not i % (loops * Config.PROGRESS_PERCENT):
            print(f"\rProgress: {yellow}{i:>{len(str(loops))}}/{loops}{reset}", end="")
    else:
        print_speed_summary(speed_num_cases, loops, times)


def debug_solution(test_inp: TestInp, test_out: TestOut, case_number: int) -> None:
    test = (
        ["1"] + test_inp[case_number - 1]
        if not Config.TEST_ONE_BY_ONE
        else test_inp[case_number - 1]
    )

    @mock.patch("builtins.input", side_effect=test)
    def test_debug(input: Callable) -> None:
        solution()

    command = Config.OTHER_LANG_COMMAND

    if lang is Lang.PYTHON:
        running = f"{emojis.snake} {yellow}Python solution{reset}"
    else:
        running = f"{emojis.otter} {yellow}{command[command.rfind('/') + 1:]}{reset}"

    print('Started testing, format "Debug":')
    print(f"Running: {running}")
    print(f" Test nr: {cyan}{case_number}{reset}")

    print(f"      Input: {cyan}")
    pprint(test_inp[case_number - 1])
    print(f"{reset}   Expected: {green}{test_out[case_number - 1]}{reset}")
    print("Your output:")
    if command:
        test_ = "1\n" + "\n".join(test_inp[case_number - 1])
        start = perf_counter()
        proc = subprocess.run(
            command.split(),
            input=test_,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
        )
        end = perf_counter()
        print(proc.stderr)
        print(proc.stdout)
        print(f"\nTime: {yellow}{end - start}{reset} seconds")

    else:
        test_debug()  # type: ignore


def test_other_lang(
    command: str, test_inp: TestInp, test_out: TestOut, num_cases: int
) -> None:
    test_inp_ = (
        f"{num_cases}\n"
        + "\n".join(functools.reduce(operator.iconcat, test_inp[:num_cases], []))
        + "\n"
    )
    print_begin("All in one", num_cases, test_inp, test_out)

    start = perf_counter()
    proc = subprocess.run(
        command.split(),
        input=test_inp_,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True,
    )
    end = perf_counter()

    err = proc.stderr
    output = proc.stdout.split("\n")
    output = [x.strip("\r") for x in output]

    if err:
        print(err)
        raise SystemExit(1)

    passed, i = check_result(test_inp, test_out, num_cases, output)

    print_summary(i, passed, end - start)


def speed_test_other_aio(
    command: str, test_inp: TestInp, test_out: TestOut, speed_num_cases: int
) -> None:
    test_inp_ = (
        f"{speed_num_cases}\n"
        + "\n".join(functools.reduce(operator.iconcat, test_inp[:speed_num_cases], []))
        + "\n"
    )

    def run() -> Tuple[bool, float]:
        start = perf_counter()
        proc = subprocess.run(
            command.split(),
            input=test_inp_,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
        )
        end = perf_counter()

        err = proc.stderr
        output = proc.stdout.split("\n")
        output = [x.strip("\r") for x in output]
        if err:
            print(err)
            raise SystemExit(1)

        return (
            "\n".join(output).strip() == "\n".join(test_out[:speed_num_cases]),
            end - start,
        )

    loops = max(1, Config.NUMER_OF_LOOPS)
    print("\nSpeed test started.")
    print(f"Running: {emojis.otter} {yellow}{command[command.rfind('/') + 1:]}{reset}")
    print(f'Testing {cyan}{speed_num_cases}{reset} cases, format "All in one":')
    print(f" - Number of loops: {cyan}{loops:_}{reset}")
    print(f" - Timeout: {red}{Config.TIMEOUT}{reset} seconds")
    if Config.PRINT_EXTRA_STATS:
        print_extra_stats(
            test_inp[:speed_num_cases], test_out[:speed_num_cases], speed_num_cases
        )
    print()

    times = []
    for i in range(loops):
        passed, time = run()
        times.append(time)
        if not passed:
            print(f"{red}Failed at iteration {i + 1}!{reset}")
            break
        if sum(times) >= Config.TIMEOUT:
            print(f"{red}Timeout at {i + 1} iteration!{reset}")
            break
        if 1 < loops <= 10 or not i % (loops * Config.PROGRESS_PERCENT):
            print(f"\rProgress: {yellow}{i:>{len(str(loops))}}/{loops}{reset}", end="")
    else:
        print_speed_summary(speed_num_cases, loops, times)


########################################################################


def parse_args() -> None:
    parser = argparse.ArgumentParser(
        usage="%(prog)s [options]",
        description="Yan Tovis unofficial tester for Tech With Tim discord Weekly Challenges. "
        "You can configure it editing CONFIGURATION section of this tester file "
        "or using command line arguments.",
        epilog="All file paths must be absolute or relative to this tester!",
    )

    parser.add_argument(
        "-s",
        "--source",
        metavar="path_src_file",
        help="Path to solution source file for Python solution, or for other languages if you "
        "want solution length to be printed.",
    )
    parser.add_argument(
        "-c",
        "--command",
        metavar="CMD",
        help="Command to execute solution written in other languages then Python.",
    )
    parser.add_argument(
        "-i",
        "--input",
        metavar="test_cases",
        help="Path to test cases input (input/expected output) JSON file.",
    )
    parser.add_argument(
        "-e",
        "--expected",
        metavar="test_output",
        help="Path to test cases expected values if they in separate "
        "file then input test cases.",
    )
    parser.add_argument(
        "--nocolor",
        action="store_true",
        help="If you don't want color output in terminal, or if your terminal"
        "don't support colors and script didn't detect this.",
    )
    parser.add_argument(
        "-n",
        "--number-cases",
        metavar="<int>",
        type=int,
        help="Number of test cases to use to test.",
    )
    parser.add_argument(
        "-d",
        "--debug",
        metavar="<int>",
        type=int,
        help="Test case number if you want to print something extra for debugging. "
        "Your solution will be run with only that one test case and whole output "
        "will be printed.",
    )
    parser.add_argument(
        "--onebyone",
        action="store_true",
        help="Use if official challenge tester gives one test case inputs and "
        "run your solution again for next test case.",
    )
    parser.add_argument(
        "--add1",
        action="store_true",
        help="If you want test your solution one test case by one test case, "
        "and solution is written to take all test cases at once, this will add '1' "
        "as the first line input.",
    )
    parser.add_argument(
        "-S",
        "--speedtest",
        metavar="<int>",
        type=int,
        help="Number of times to run tests to get more accurate times. Works "
        "only for Python solution.",
    )
    parser.add_argument(
        "--number-speed-cases",
        metavar="<int>",
        type=int,
        help="How many test case to use per loop when speed test.",
    )
    parser.add_argument(
        "--timeout",
        metavar="<int>",
        type=int,
        help="Timeout in seconds. Will not timeout in middle of test case. "
        'Not working in "All in One" mode. Will timeout only between test cases / loops.',
    )
    parser.add_argument(
        "-x",
        "--noextra",
        action="store_true",
        help="Use if this tester wasn't prepared for the challenge you testing.",
    )
    parser.add_argument(
        "-p",
        "--progress",
        metavar="<float>",
        type=float,
        help="How often to update progress: must be > 0 and < 1. 0.1 - means "
        "update every 10%% completed tests, 0.05 - means update every 5%% completed tests.",
    )
    parser.add_argument(
        "-f",
        "--failed",
        metavar="<int>",
        type=int,
        help="Number of failed tests to print (-1 to print all failed).",
    )
    parser.add_argument(
        "-l",
        "--nolength",
        action="store_true",
        help="Use if you want to share result but don't want to share solution length.",
    )
    parser.add_argument(
        "-E",
        "--emoji",
        action="store_true",
        help="Use unicode emoji. Your terminal must support unicode and your "
        "terminal font must have glyphs for emoji.",
    )

    args = parser.parse_args()

    if args.source:
        Config.SOLUTION_SRC_FILE_NAME = args.source
    if args.command:
        Config.OTHER_LANG_COMMAND = args.command
    if args.input:
        Config.TEST_CASE_FILE = args.input
    if args.expected:
        Config.TEST_CASE_FILE_EXP = args.expected
    if args.nocolor:
        Config.COLOR_OUT = False
    if args.number_cases:
        Config.NUMBER_OF_TEST_CASES = args.number_cases
    if args.debug:
        Config.DEBUG_TEST = True
        Config.DEBUG_TEST_NUMBER = args.debug
    if args.onebyone:
        Config.TEST_ONE_BY_ONE = True
    if args.add1:
        Config.ADD_1_IN_OBO = True
    if args.speedtest:
        Config.SPEED_TEST = True
        Config.NUMER_OF_LOOPS = args.speedtest
    if args.number_speed_cases:
        Config.NUMBER_SPEED_TEST_CASES = args.number_speed_cases
    if args.timeout:
        Config.TIMEOUT = args.timeout
    if args.noextra:
        Config.PRINT_EXTRA_STATS = False
    if args.progress:
        Config.PROGRESS_PERCENT = args.progress
    if args.failed:
        Config.NUM_FAILED = args.failed
    if args.nolength:
        Config.PRINT_SOLUTION_LENGTH = False
    if args.emoji:
        Config.USE_EMOJI = True


def main(path: str) -> None:
    test_inp, test_out = read_test_cases()

    if Config.DEBUG_TEST:
        case_number = (
            Config.DEBUG_TEST_NUMBER
            if 0 <= Config.DEBUG_TEST_NUMBER - 1 < len(test_out)
            else 1
        )
        debug_solution(test_inp, test_out, case_number)
        raise SystemExit(0)

    if 0 < Config.NUMBER_OF_TEST_CASES < len(test_out):
        num_cases = Config.NUMBER_OF_TEST_CASES
    else:
        num_cases = len(test_out)

    if 0 < Config.NUMBER_SPEED_TEST_CASES < len(test_out):
        speed_num_cases = Config.NUMBER_SPEED_TEST_CASES
    else:
        speed_num_cases = len(test_out)

    if Config.OTHER_LANG_COMMAND:
        os.chdir(path)
        test_other_lang(Config.OTHER_LANG_COMMAND, test_inp, test_out, num_cases)
        if Config.SPEED_TEST:
            speed_test_other_aio(
                Config.OTHER_LANG_COMMAND, test_inp, test_out, speed_num_cases
            )
        raise SystemExit(0)

    if Config.TEST_ONE_BY_ONE:
        test_solution_obo(test_inp, test_out, num_cases)
    else:
        test_solution_aio(test_inp, test_out, num_cases)
        if Config.SPEED_TEST:
            speed_test_solution_aio(test_inp, test_out, speed_num_cases)


if __name__ == "__main__":
    path = os.path.dirname(os.path.abspath(__file__))
    os.chdir(path)

    parse_args()

    color_out = Config.COLOR_OUT and enable_win_term_mode()
    red, green, yellow, cyan, reset, red_bg = (
        (
            "\x1b[31m",
            "\x1b[32m",
            "\x1b[33m",
            "\x1b[36m",
            "\x1b[0m",
            "\x1b[41m",
        )
        if color_out
        else [""] * 6
    )

    if Config.USE_EMOJI:
        emojis = Emoji(
            stopwatch="\N{stopwatch}  ",
            hundred="\N{Hundred Points Symbol}",
            poo=" \N{Pile of Poo}",
            snake="\N{snake}",
            otter="\N{otter}",
            scroll=" \N{scroll}",
            filebox=" \N{Card File Box} ",
            chart=" \N{Chart with Upwards Trend} ",
            rocket="\N{rocket} ",
            warning=" \N{warning sign} ",
            bang="\N{Heavy Exclamation Mark Symbol}",
            stop="\N{Octagonal sign}",
            snail="\N{snail} ",
            leopard=" \N{leopard}",
        )
    else:
        emojis = Emoji()

    solution_len = create_solution_function(path, Config.SOLUTION_SRC_FILE_NAME)

    lang = Lang.OTHER if Config.OTHER_LANG_COMMAND else Lang.PYTHON

    if lang is Lang.PYTHON:
        if not solution_len:
            print("Could not import solution!")
            raise SystemExit(1)

        from temp_solution_file import solution  # type: ignore

    test_cases_file = os.path.join(path, Config.TEST_CASE_FILE)
    if not os.path.exists(test_cases_file):
        print(
            f"Can't find file with test cases {red}{os.path.join(path, Config.TEST_CASE_FILE)}{reset}!"
        )
        print("Make sure it is in the same directory as this script!")
        raise SystemExit(1)

    test_out_file = (
        os.path.join(path, Config.TEST_CASE_FILE_EXP)
        if Config.TEST_CASE_FILE_EXP
        else test_cases_file
    )
    if Config.TEST_CASE_FILE_EXP and not os.path.exists(test_out_file):
        print(
            f"Can't find file with output for test cases {red}{test_out_file}{reset}!"
        )
        print("Make sure it is in the same directory as this script!\n")
        print(
            f"If output is in same file as input set {cyan}SEP_INP_OUT_TESTCASE_FILE{reset} "
            f"to {yellow}False{reset} in configure section."
        )
        raise SystemExit(1)

    main(path)
