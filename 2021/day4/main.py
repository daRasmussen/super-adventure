import sys
import time
from typing import List, Set

test = True
debug = False
stdin = False
INFILENAME = "data.txt"
TESTFILENAME = "test.txt"

for arg in sys.argv:
    if arg == "--notest":
        test = False
    if arg == "--debug":
        debug = True
    if arg == "--stdin":
        stdin = True

class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

# Utils
def grid_columns(grid: List[List]) -> List[List]:
    columns = []
    for col_idx in range(len(grid[0])):
        columns.append([grid[i][col_idx] for i in range(len(grid))])
    return columns

print(f"\n{'=' * 30}\n")

# Read the input

if stdin:
    input_lines: List[str] = [l.strip() for l in sys.stdin.readlines()]
else:
    with open(INFILENAME) as f:
        input_lines: List[str] = [l.strip() for l in f.readlines()]

# Try and read in the test file
try:
    with open(TESTFILENAME) as f:
        test_lines: List[str] = [l.strip() for l in f.readlines()]
except Exception:
    test_lines = []

# Shared

def checkset(row_or_col: List[int], called: List[int]) -> bool:
    return set(row_or_col) - set(called) == set()

def check_board(board: List[List[int]], called: List[int]) -> int:
    return any(
        [checkset(r, called) for r in board]
        + [checkset(c, called) for c in grid_columns(board)]
    )


# Part 1
###############################################################################
print("Part 1:")

def part1(lines: List[str]) -> int:
    numbers = [int(x) for x in lines[0].split(",")]

    # Populate the boards array.
    boards = []
    curboard = []
    for l in lines[2:]:
        if l == "": # empty line delimiter
            boards.append(curboard)
            curboard = []
            continue
        curboard.append([int(x) for x in l.split()])
    boards.append(curboard)
    # Keep adding a new item until someone wins.
    i = 5
    while True:
        called = numbers[:i]
        i += 1
        for b in boards:
            if check_board(b, called):
                not_called = 0
                for r in b:
                    for c in r:
                        if c not in called:
                            not_called += c
                return not_called * called[-1]

# Run test on part 1
if test:
    print("Running test... ", end="")
    if not test_lines:
        print(f"{bcolors.FAIL}No test configured!{bcolors.ENDC}")
    else:
        test_ans_part1 = part1(test_lines)
        expected = 4512
        if expected is None:
            print(f"{bcolors.FAIL}No test configured!{bcolors.ENDC}")
        elif test_ans_part1 == expected:
            print(f"{bcolors.OKGREEN}PASS{bcolors.ENDC}")
        else:
            print(f"{bcolors.FAIL}FAIL{bcolors.ENDC}")
        print("Result: ", test_ans_part1)
        print()
part1_start = time.time()
print("Running input...")
ans_part1 = part1(input_lines)
part1_end = time.time()
print("Result: ", ans_part1)

tries = [
    # Store the attempts that failed here.
]

if tries:
    print("Tries Part 1:", tries)
    assert ans_part1 not in tries, "Same as an incorrect answer!"

# Regression Test
expected = None
if expected is not None:
    assert test or ans_part1 == expected
# Part 2
###############################################################################
print("\nPart 2:")

def part2(lines: List[str]) -> int:
    def checkrow(r: List[int], x: Set[int]) -> bool:
        return set(r) - x == set()
    def check_board(b: List[List[int]], ns: Set[int]):
        for r in b:
            if checkrow(r, ns):
                return r
        for c in range(5):
            col = [b[r][c] for r in range(5)]
            if checkrow(col, ns):
                return col
        return None
    boards = []
    curboard = []
    for l in lines[2:]:
        if l.strip() == "":
            boards.append(curboard)
            curboard = []
            continue
        curboard.append([int(x) for x in l.split()])
    boards.append(curboard)
    ns = list(map(int, lines[0].split(",")))
    called = ns[:5]
    i = 5
    while True:
        nb = []
        if len(boards) > 1:
            for b in boards:
                cb = check_board(b, set(called))
                if cb is None:
                    nb.append(b)
                boards = nb
        called = ns[: 5 + i]
        i += 1
        if len(boards) == 1 and check_board(b, set(called)):
            x = 0
            for r in boards[0]:
                for c in r:
                    if c not in called:
                        x += c
            l = []
            s = set()
            for r in boards[0]:
                for c in r:
                    l.append(c)
                    s.add(c)
            assert len(l) == len(s)
            return x * called[-1]

    # Run test on part 2
if test:
    print("Running test... ", end="")
    if not test_lines:
        print(f"{bcolors.FAIL}No test configured!{bcolors.ENDC}")
    else:
        test_ans_part1 = part1(test_lines)
        expected = 1924
        if expected is None:
            print(f"{bcolors.FAIL}No test configured!{bcolors.ENDC}")
        elif test_ans_part1 == expected:
            print(f"{bcolors.OKGREEN}PASS{bcolors.ENDC}")
        else:
            print(f"{bcolors.FAIL}FAIL{bcolors.ENDC}")
        print("Result: ", test_ans_part1)
        print()

part2_start = time.time()
print("Running input...")
ans_part2 = part2(input_lines)
part2_end = time.time()
print("Result: ", ans_part2)

tries2 = [
    40100
]

if tries2:
    print("Tries Part 2:", tries)
    assert ans_part2 not in tries, "Same as an incorrect answer!"

# Regression Test
expected = None
if expected is not None:
    assert test or ans_part1 == expected

if debug:
    part1_time = part1_end - part1_start
    part2_time = part2_end - part2_start
    print()
    print("DEBUG")
    print(f"Part 1: {part1_time * 1000}ms")
    print(f"Part 2: {part2_time * 1000}ms")
    print(f"TOTAL: {(part1_time + part2_time) * 1000}ms")
