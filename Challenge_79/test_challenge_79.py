"""
How to use?
Put this file, with test cases file and file with your solution in same folder.
Make sure Python has right to save to this folder.

This tester will create one file "temp_solution_file.py" make sure there's no such
file in same folder or there's nothing important in it cos it will be overwritten!

Change SOLUTION_FILE_NAME to your file name in CONFIGURATION section.

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
"""

########## CONFIGURATION ################

# Name of your file with solution. If its not in same folder as this script
# add absolute path or relative to CWD (Current Working Directory - directory from
# which you run this script)
SOLUTION_FILE_NAME = "to_submit_ch_79.py"

# Command to run your solution written in other language then Python
# For compiled languages compile yourself and use compiled executable file name
# For interpreter languages give full command to run your solution
# example: 
# OTHER_LANG_COMMAND = "S:/Dev/C++/Tests/c79_cpp_solution.exe"
# OTHER_LANG_COMMAND = "/home/user/c79_rust_solution/target/release/c79_rust_solution"
# OTHER_LANG_COMMAND = "c79_cs_solution.exe"
# OTHER_LANG_COMMAND = "java -cp S:/Dev/Java/ c79_java_solution.Main"
OTHER_LANG_COMMAND = ""                                                                                        

# True - If test cases input and output are in separate files
# False - if they in one file
SEP_INP_OUT_TESTCASE_FILE = False

# Name of file with inputs test cases (and output if SEP_INP_OUT_TESTCASE_FILE is False)
# If test cases file is compressed, you don't need to extract it, just give name of 
# compressed file (with .gz extension)
TEST_CASE_FILE = "test_cases.json"

# Name of file with outputs for test cases (ignored if SEP_INP_OUT_TESTCASE_FILE is False)
TEST_CASE_FILE_OUT = ""

# True - if you want colors in terminal output, False - otherwise or if your terminal
# don't support colors and script didn't detect this
COLOR_OUT = True

# -1 - use all test cases from test case file, you can limit here with how many
# tests cases you want to test your solution. If you enter number bigger than
# number of tests all tests will be used
NUMBER_OF_TEST_CASES = -1

# True - if official challenge tester give one test case inputs and run your solution
# again for next test case, False - if official challenge tester gives all test cases
# once and your solution need to take care of it.
TEST_ONE_BY_ONE = False

# True - if you want to print some debug information, you need set:
#   DEBUG_TEST_NUMBER to the test number you want to debug and 
#   ADD_1_IN_OBO to True if solution is written to take all test cases at once else to False
DEBUG_TEST = False

# Provide test number for which you want to see your debug prints. If you enter number
# out of range, first test case will be used. (This number is 1 - indexed it is same number
# you find when failed test case is printed in normal test). Ignored when DEBUG_TEST is False
DEBUG_TEST_NUMBER = 20

# True - if you want test your solution one test case by one test case, and solution
# is written to take all test cases at once, this will add "1" as the first line input
# Ignored if TEST_ONE_BY_ONE is False
ADD_1_IN_OBO = True

# True - if you want to measure performance of your solution, running it multiple times
SPEED_TEST = False

# How many test case to use per loop, same rules apply as for NUMBER_OF_TEST_CASES
NUMBER_SPEED_TEST_CASES = -1

# How many times run tests
NUMER_OF_LOOPS = -1

# Timeout in seconds. Will not timeout in middle of test case (if TEST_ONE_BY_ONE is False
# will not timeout in middle of loop). Will timeout only between test cases / loops
# If you don't want timeout set it to some big number or `float("inf")`
TIMEOUT = 300

# Set to False if this tester wasn't prepared for the challenge you testing
# or adjust prints in `print_extra_stat` function yourself
PRINT_EXTRA_STATS = False

# How often to update progress: must be > 0 and < 1
# 0.1 - means update every 10% completed tests
# 0.05 - means update every 5% completed tests
PROGRESS_PERCENT = 0.1

# How many failed cases to print
# Set to -1 to print all failed cases
NUM_FAILED = 5

# Set to False if you want to share result but don't want to share solution length
PRINT_SOLUTION_LENGTH = True

########################################

from itertools import zip_longest
import subprocess
import sys, os, platform, json, functools, operator, gzip
from time import perf_counter
from typing import Callable, List, Tuple
from unittest import mock
from io import StringIO
from pprint import pprint


def enable_win_term_mode() -> bool:
    win = platform.system().lower() == "windows"
    if win == False:
        return True

    from ctypes import windll, c_int, byref, c_void_p

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
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args) -> None:
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio  # free up some memory
        sys.stdout = self._stdout


def create_solution_function(path: str, file_name: str) -> int:
    if file_name.find("/") == -1 or file_name.find("\\") == -1:
        file_name = os.path.join(path, file_name)

    if not os.path.exists(file_name):
        print(f"Can't find file {red}{file_name}{reset}!\n")
        print("Make sure:\n - your file is in same directory as this script.")
        print(" - or give absolute path to your file")
        print(" - or give relative path from Current Working Directory.\n")
        print(f"Current Working Directory is: {yellow}{os.getcwd()}{reset}")

        return 0

    solution = []
    with open(file_name, newline="") as f:
        solution = f.readlines()
    
    sol_len = sum(map(len, solution))

    tmp_name = os.path.join(path, "temp_solution_file.py")
    with open(tmp_name, "w") as f:
        f.write("def solution():\n")
        for line in solution:
            f.write("    " + line)

    return sol_len


def read_test_cases() -> Tuple[List[List[str]], List[str]]:
    if test_cases_file.endswith(".gz"):
        with gzip.open(test_cases_file, "rb") as g:
            data = g.read()
        try:
            test_inp = json.loads(data)
        except json.decoder.JSONDecodeError:
            print(f"Test case file {yellow}{test_cases_file}{reset} is not valid JSON file!")
            exit(1)
    else:
        with open(test_cases_file) as f:
            try:
                test_inp = json.load(f)
            except json.decoder.JSONDecodeError:
                print(f"Test case file {yellow}{test_cases_file}{reset} is not valid JSON file!")
                exit(1)

    if SEP_INP_OUT_TESTCASE_FILE:
        with open(test_out_file) as f:
            try:
                test_out = json.load(f)
            except json.decoder.JSONDecodeError:
                print(f"Test case file {yellow}{test_out_file}{reset} is not valid JSON file!")
                exit(1)
    else:
        test_out = test_inp[1]
        test_inp = test_inp[0]

    return test_inp, test_out


def print_extra_stats(test_inp: List[List[str]], test_out: List[str], num_cases: int) -> None:
    print(
        f" - Average string length: {yellow}{sum(len(x[0]) for x in test_inp) // num_cases:_}"
        f"{reset}"
    )
    print(f" - Max string length: {yellow}{max(len(x[0]) for x in test_inp)}{reset}")



def test_solution_aio(test_inp: List[List[str]], test_out: List[str], num_cases: int) -> None:
    test_inp_: List[str] = functools.reduce(operator.iconcat, test_inp[:num_cases], [])

    @mock.patch("builtins.input", side_effect=[str(num_cases)] + test_inp_)
    def test_aio(input: Callable) -> List[str]:
        with Capturing() as output:
            solution()

        return output

    print('Started testing, format "All in one":')
    print(f"Running: {yellow}Python solution{reset}")
    print(f" - Number of cases: {cyan}{num_cases}{reset}")
    if PRINT_EXTRA_STATS:
        print_extra_stats(test_inp[:num_cases], test_out[:num_cases], num_cases)
    if PRINT_SOLUTION_LENGTH:
        print(f" - Solution length: {green}{solution_len}{reset} chars.")
    print()

    start = perf_counter()
    output = test_aio()  # type: ignore
    end = perf_counter()

    passed = i = oi = 0
    for i, (inp, exp) in enumerate(
        zip_longest(test_inp[:num_cases], test_out[:num_cases]), 1
    ):
        out_len = len(exp.split("\n"))
        out = "\n".join(output[oi:oi+out_len])
        oi += out_len
        if out != exp:
            if i - passed <= NUM_FAILED or NUM_FAILED == -1:
                print(f"Test nr:{i}\n      Input: {cyan}")
                pprint(inp)
                print(f"{reset}Your output: {red}{out}{reset}")
                print(f"   Expected: {green}{exp}{reset}\n")
        else:
            passed += 1

    if i - passed > NUM_FAILED:
        print(f"Printed only first {yellow}{NUM_FAILED}{reset} failed cases!")
        print(f"To change how many failed cases to print change {cyan}NUM_FAILED{reset} in configuration section.\n")
    print(f"Passed: {green if passed == i else red}{passed}/{i}{reset} tests")
    print(f"Finished in: {yellow}{end - start:.4f}{reset} seconds")


def speed_test_solution_aio(
    test_inp: List[List[str]], test_out: List[str], speed_num_cases: int
) -> None:
    test_inp_: List[str] = functools.reduce(operator.iconcat, test_inp[:speed_num_cases], [])

    @mock.patch("builtins.input", side_effect=[str(speed_num_cases)] + test_inp_)
    def test_for_speed_aio(input: Callable) -> bool:

        with Capturing() as output:
            solution()

        return "\n".join(output) == "\n".join(test_out[:speed_num_cases])

    loops = NUMER_OF_LOOPS
    print("\nSpeed test started.")
    print(f"Running: {yellow}Python solution{reset}")
    print(f'Testing {cyan}{speed_num_cases}{reset} cases, format "All in one":')
    print(f" - Number of loops: {cyan}{loops:_}{reset}")
    print(f" - Timeout: {red}{TIMEOUT}{reset} seconds")
    if PRINT_EXTRA_STATS:
        print_extra_stats(test_inp[:speed_num_cases], test_out[:speed_num_cases], speed_num_cases)
    print()
    
    times = []
    for i in range(loops):
        start = perf_counter()
        passed = test_for_speed_aio()  # type: ignore
        times.append(perf_counter() - start)
        if not passed:
            print(f"{red}Failed at iteration {i + 1}!{reset}")
            break
        if sum(times) >= TIMEOUT:
            print(f"{red}Timeout at {i + 1} iteration!{reset}")
            break
        if 1 < loops <= 10 or not i % (loops * PROGRESS_PERCENT):
            print(
                f"\rProgress: {yellow}{i:>{len(str(loops))}}/{loops}{reset}", end=""
            )
    else:
        print(
            f"\rTest for speed passed!\n - Total time: {yellow}{sum(times):.4f}"
            f"{reset} seconds to complete {cyan}{loops:_}{reset} times {cyan}"
            f"{speed_num_cases}{reset} cases!"
        )
        print(
            f" - Fastest loop time: {yellow}{min(times):.4f}{reset} seconds /"
            f" {cyan}{speed_num_cases}{reset} cases."
        )
        print(
            f" - Average loop time: {yellow}{sum(times)/loops:.4f}{reset} seconds"
            f" / {cyan}{speed_num_cases}{reset} cases."
        )


def test_solution_obo(test_inp: List[List[str]], test_out: List[str], num_cases: int) -> None:
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

    print('Started testing, format "One by one":')
    print(f"Running: {yellow}Python solution{reset}")
    print(f" - Number of cases: {cyan}{num_cases}{reset}")
    print(f' - Timeout: {red}{TIMEOUT}{reset} seconds')
    if PRINT_EXTRA_STATS:
        print_extra_stats(test_inp[:num_cases], test_out[:num_cases], num_cases)
    if PRINT_SOLUTION_LENGTH:
        print(f" - Solution length: {green}{solution_len}{reset} chars.")
    print()
    
    times = []
    passed = i = 0
    for i in range(num_cases):
        test = ["1"] + test_inp[i] if ADD_1_IN_OBO else test_inp[i]
        t, output = test_obo(test)
        times.append(t)
        if test_out[i] != output:
            if i - passed <= NUM_FAILED or NUM_FAILED == -1:
                print(f"\rTest nr:{i + 1}             \n      Input: {cyan}")
                pprint(test)
                print(f"{reset}Your output: {red}{output[0]}{reset}")
                print(f"   Expected: {green}{test_out[i]}{reset}\n")
        else:
            passed += 1
        if sum(times) >= TIMEOUT:
            print(f"{red}Timeout after {i + 1} cases!{reset}")
            break
        if 1 < num_cases <= 10 or not i % (num_cases * PROGRESS_PERCENT):
            print(
                f"\rProgress: {yellow}{i + 1:>{len(str(num_cases))}}/{num_cases}{reset}",
                end="",
            )

    if i - passed > NUM_FAILED:
        print(f"Printed only first {yellow}{NUM_FAILED}{reset} failed cases!")
        print(f"To change how many failed cases to print change {cyan}NUM_FAILED{reset} in configuration section.\n")
    print(f"\rPassed: {green if passed == i + 1 else red}{passed}/{i + 1}{reset} tests")
    print(f"Finished in: {yellow}{sum(times):.4f}{reset} seconds")


def speed_test_solution_obo(
    test_inp: List[List[str]], test_out: List[str], speed_num_cases: int
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

    loops = NUMER_OF_LOOPS
    print("\nSpeed test started.")
    print(f"Running: {yellow}Python solution{reset}")
    print(f'Testing {cyan}{speed_num_cases}{reset} cases, format "One by one":')
    print(f" - Number of loops: {cyan}{loops:_}{reset}")
    print(f" - Timeout: {red}{TIMEOUT}{reset} seconds")
    if PRINT_EXTRA_STATS:
        print_extra_stats(test_inp[:speed_num_cases], test_out[:speed_num_cases], speed_num_cases)
    print()

    times, timedout = [], False
    for i in range(loops):
        for j in range(speed_num_cases):
            test = ["1"] + test_inp[j] if ADD_1_IN_OBO else test_inp[j]

            t, passed = test_for_speed_obo(test, test_out[j])
            times.append(t)

            if not passed:
                print(f"\r{red}Failed at iteration {i + 1}!{reset}")
                break
            if sum(times) >= TIMEOUT:
                print(f"\r{red}Timeout at {i + 1} iteration!{reset}")
                timedout = True
                break
        if timedout:
            break
        if 1 < loops <= 10 or not i % (loops * PROGRESS_PERCENT):
            print(
                f"\rProgress: {yellow}{i:>{len(str(loops))}}/{loops}{reset}", end=""
            )
    else:
        print(
            f"\rTest for speed passed! It took your solution {yellow}{sum(times):.4f}{reset} "
            f"seconds to complete {cyan}{loops:_}{reset} times!"
        )
        print(f"Average time: {yellow}{sum(times)/loops:.4f}{reset} seconds")


def debug_solution(test_inp: List[List[str]], test_out: List[str], case_number: int) -> None:
    test = ["1"] + test_inp[case_number - 1] if ADD_1_IN_OBO else test_inp[case_number - 1]

    @mock.patch("builtins.input", side_effect=test)
    def test_debug(input: Callable) -> None:
        solution()
    
    command = OTHER_LANG_COMMAND if OTHER_LANG_COMMAND else "Python solution"

    
    print('Started testing, format "Debug":')
    print(f'Running: {yellow}{command}{reset}')
    print(f" Test nr: {cyan}{case_number}{reset}")

    print(f"      Input: {cyan}")
    pprint(test_inp[case_number-1])
    print(f"{reset}   Expected: {green}{test_out[case_number - 1]}{reset}")
    print("Your output:")
    if OTHER_LANG_COMMAND:
        test_ = "1\n" + "\n".join(test_inp[case_number - 1])
        proc = subprocess.run(
            command,
            input=test_,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )
        print(proc.stderr)
        print(proc.stdout)
        
    else:
        test_debug()  # type: ignore


def test_other_lang(
    command: str,
    test_inp: List[List[str]],
    test_out: List[str],
    num_cases: int
) -> None:
    test_inp_ = (
        f"{num_cases}\n" + "\n".join(functools.reduce(operator.iconcat, test_inp[:num_cases], [])) + "\n"
    )
    
    print('Started testing, format "All in one":')
    print(f"Running: {yellow}{command}{reset}")
    print(f" - Number of cases: {cyan}{num_cases}{reset}")
    if PRINT_EXTRA_STATS:
        print_extra_stats(test_inp[:num_cases], test_out[:num_cases], num_cases)
    print()
    
    start = perf_counter()
    proc = subprocess.run(
        command,
        input=test_inp_,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True
    )
    end = perf_counter()
    
    err = proc.stderr
    output = proc.stdout.split("\n")
    output = [x.strip('\r') for x in output]
    
    if err:
        print(err)
        exit(1)

    passed = i = oi = 0
    for i, (inp, exp) in enumerate(
        zip_longest(test_inp[:num_cases], test_out[:num_cases]), 1
    ):
        out_len = len(exp.split("\n"))
        out = "\n".join(output[oi:oi+out_len])
        oi += out_len
        if out != exp:
            if i - passed <= NUM_FAILED or NUM_FAILED == -1:
                print(f"Test nr:{i}\n      Input: {cyan}")
                pprint(inp)
                print(f"{reset}Your output: |{red}{out}{reset}|")
                print(f"   Expected: |{green}{exp}{reset}|\n")
        else:
            passed += 1
            
    if i - passed > NUM_FAILED:
        print(f"Printed only first {yellow}{NUM_FAILED}{reset} failed cases!")
        print(f"To change how many failed cases to print change {cyan}NUM_FAILED{reset} in configuration section.\n")

    print(f"Passed: {green if passed == i else red}{passed}/{i}{reset} tests")
    print(f"Finished in: {yellow}{end - start:.4f}{reset} seconds")


def main(path: str) -> None:
    test_inp, test_out = read_test_cases()
    

    if DEBUG_TEST:
        os.chdir(path)
        case_number = DEBUG_TEST_NUMBER if 0 <= DEBUG_TEST_NUMBER - 1 < len(test_out) else 1
        debug_solution(test_inp, test_out, case_number)
        exit(0)

    if 0 < NUMBER_OF_TEST_CASES < len(test_out):
        num_cases = NUMBER_OF_TEST_CASES
    else:
        num_cases = len(test_out)

    if 0 < NUMBER_SPEED_TEST_CASES < len(test_out):
        speed_num_cases = NUMBER_SPEED_TEST_CASES
    else:
        speed_num_cases = len(test_out)
        
    if OTHER_LANG_COMMAND:
        os.chdir(path)
        test_other_lang(OTHER_LANG_COMMAND, test_inp, test_out, num_cases)
        exit(0)

    if TEST_ONE_BY_ONE:
        test_solution_obo(test_inp, test_out, num_cases)
        if SPEED_TEST:
            speed_test_solution_obo(test_inp, test_out, speed_num_cases)
    else:
        test_solution_aio(test_inp, test_out, num_cases)
        if SPEED_TEST:
            speed_test_solution_aio(test_inp, test_out, speed_num_cases)


if __name__ == "__main__":
    color_out = COLOR_OUT and enable_win_term_mode()
    red, green, yellow, cyan, reset = (
        (
            "\x1b[31m",
            "\x1b[32m",
            "\x1b[33m",
            "\x1b[36m",
            "\x1b[0m",
        )
        if color_out
        else [""] * 5
    )

    path = os.path.dirname(os.path.abspath(__file__))
    solution_len = 0
    if not OTHER_LANG_COMMAND:
        solution_len = create_solution_function(path, SOLUTION_FILE_NAME)
    
        if not solution_len:
            print("Could not import solution!")
            exit(1)
            
        from temp_solution_file import solution

    test_cases_file = os.path.join(path, TEST_CASE_FILE)
    if not os.path.exists(test_cases_file):
        print(
            f"Can't find file with test cases {red}{os.path.join(path, TEST_CASE_FILE)}{reset}!"
        )
        print("Make sure it is in the same directory as this script!")
        exit(1)

    if SEP_INP_OUT_TESTCASE_FILE and not TEST_CASE_FILE_OUT:
        print("Wrong configuration!\n")
        print(
            f"{cyan}SEP_INP_OUT_TESTCASE_FILE{reset} is set to {yellow}True{reset} "
            f"but {cyan}TEST_CASE_FILE_OUT{reset} is empty!\n"
        )
        print(
            "If outputs for test cases are in the same file as inputs "
            f"set {cyan}SEP_INP_OUT_TESTCASE_FILE{reset} to {yellow}False{reset}."
        )
        print(
            "If input and output are in separated files enter file name in "
            f"{cyan}TEST_CASE_FILE_OUT{reset} in configure section"
        )
        exit(1)
        
    test_out_file = (
        os.path.join(path, TEST_CASE_FILE_OUT)
        if SEP_INP_OUT_TESTCASE_FILE
        else test_cases_file
    )
    if SEP_INP_OUT_TESTCASE_FILE and not os.path.exists(test_out_file):
        print(
            f"Can't find file with output for test cases {red}{test_out_file}{reset}!"
        )
        print("Make sure it is in the same directory as this script!\n")
        print(
            f"If output is in same file as input set {cyan}SEP_INP_OUT_TESTCASE_FILE{reset} "
            f"to {yellow}False{reset} in configure section."
        )
        exit(1)

    main(path)
