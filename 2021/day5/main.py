#! /usr/bin/env python3

# SETUP
###############################################################################

import re
import sys
import time
from collections import defaultdict
from fractions import Fraction
from typing import Generator, Iterable, List, Match, Optional, Tuple

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
    UNDERLINE = "\0 3[4m"

if stdin:
    input_lines: List[str] = [l.strip() for l in sys.stdin.readlines()]
else:
    with open(INFILENAME) as f:
        input_lines: List[str] = [l.strip() for l in f.readlines()]
try:
    with open(TESTFILENAME) as f:
        test_lines: List[str] = [l.strip() for l in f.readlines()]
except Exception:
    test_lines = []

# Utils
##############################################################################
def irange(start, end=None, step=1) -> Generator[int, None, None]:
    """Inclusive range function."""
    if end is None:
        start, end = 0, start
    yield from range(start, end + 1, step=step)

def dirange(start, end=None, step=1) -> Generator[int, None, None]:
    """
    Directional, inclusive range. This range function is an inclusive version
    of :class `range` that figures out the correct step direction to make sure 
    that it goes from `start` to `end`, even if `end` is before `start`.

    >>> dirange(2, -2)
    >>> [2, 1, 0, -1, 2]
    >>> dirange(-2)
    >>> [0, -1, -2]
    >>> dirange(2)
    >>> [0, 1, 2]

    """
    assert step > 0
    if end is None:
        start, end = 0, start
    if end >= start:
        yield from irange(start, end, step)
    else:
        yield from range(start, end - 1, step=-step)

def int_points_between(
        start: Tuple[int, int], end: Tuple[int, int]
        ) -> Generator[Tuple[int, int], None, None]:
    """
    Return a generator of all of the integer points between two given points.
    Nots that you are *not* guaranteed that the points will be given from 
    `start` to `end`, but all points will be included.
    """
    x1, y1 = start
    x2, y2 = end
    if x1 == x2:
        yield from ((x1, y) for y in dirange(y1, y2))
    elif y1 == y2:
        yield from ((x, y1) for x in dirange(x1, x2))
    else:
        """
        If `x1 > x2`, that means that `start` is to the right of the `end`,
        so we need to switch the points around so teration always goes in the 
        positive `x` direction.
        """
        if x1 > x2:
            x1, x2, y1, y2 = x2, x1, y2, y1
        dy = y2 - y1
        dx = x2 - x1
        slope = Fraction(dy, dx)
        for i in irange(dy // slope.numerator):
            yield(x1 + (i * slope.denominator), y1 + (i * slope.numerator))

# Shared
###############################################################################
def rematch(pattern: str, s: str) -> Optional[Match]:
    return re.fullmatch(pattern, s)

def parselines(
        lines: List[str]) -> Iterable[Tuple[Tuple[int, int], Tuple[int, int]]]:
    for line in lines:
        x1, y1, x2, y2 = map(int, 
                rematch(r"(\d+),(\d+) -> (\d+),(\d+)", line).groups())
        yield (x1, y1), (x2, y2)


# Part 1
###############################################################################
print("Part 1:")


def part1(lines: List[str]) -> int:
    G = defaultdict(int)
    for (x1, y1), (x2, y2) in parselines(lines):
        for x, y in int_points_between((x1, x2), (x2, y2)):
            G[(x, y)] += 1
    return sum([1 for x in G.values() if x > 1])

# Run test on part 1
if test:
    print("Running test... ", end="")
    if not test_lines:
        print(f"{bcolors.FAIL}No test configured!{bcolors.ENDC}")
    else:
        test_ans_part1 = part1(test_lines)
        expected = 5
        if expected is None:
            print(f"{bcolors.FAIL}No test configured!{bcolors.ENDC}")
        elif test_ans_part1 == expected:
            print(f"{bcolors.OKGREEN}PASS{bcolors.ENDC}")
        else:
            print(f"{bcolors.FAIL}FAIL{bcolors.ENDC}")
            assert False

        print("Result:", test_ans_part1)
        print()

part1_start = time.time()
print("Running input...")
ans_part1 = part1(input_lines)
part1_end = time.time()
print("Result:", ans_part1)

tries = [
    # Store the attempts that failed here.
]
if tries:
    print("Tries Part 1:", tries)
    assert ans_part1 not in tries, "Same as an incorrect answer!"


# Regression Test
expected = 4826
if expected is not None:
    assert test or ans_part1 == expected
