import random
import string
import json
import gzip
from tqdm import tqdm
from pathlib import Path

from challenge_86 import solution, is_winner

path = Path(__file__).parent

def generate_tests(number_of_cases: int, max_len: int, compress: bool) -> None:
    test_inputs = []
    test_expected = []
    players = {1: 'X', -1: 'O'}
    moves_to_pick = [*range(9)]
    for _ in tqdm(range(number_of_cases)):
        random.shuffle(moves_to_pick)
        staring_player = random.choice((1, -1))
        curr_player = staring_player
        grid = [0] * 9
        moves = []
        for m in moves_to_pick:
            grid[m] = curr_player
            curr_player *= -1
            moves.append(m + 1)
            if is_winner(grid):
                break
        test = [f"{players[staring_player]} {len(moves)}", " ".join(str(x) for x in moves)]
        test_inputs.append(test)
        test_expected.append(solution(test))
        

    print(len(test_inputs), len(test_expected))

    cases = [test_inputs, test_expected]

    if compress:
        content = bytes(json.dumps(cases), "utf-8")
        with gzip.open(path / "test_cases_s.json.gz", "wb", compresslevel=9) as g:
            g.write(content)
    else:

        with open(path / "test_cases.json", "w") as f:
            json.dump(cases, f, indent=2)


if __name__ == "__main__":
    generate_tests(number_of_cases=10000, max_len=60, compress=False)
