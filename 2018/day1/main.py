from aocd import submit, get_data

import pytest

from collections import namedtuple

data = get_data(day=1, year=2018)
def part1(data: str) -> int:
    return sum([int(x) for x in data.splitlines()])

TestData = namedtuple("TestData", ["data", "result"])
TestData.__test__ = False # type: ignore

@pytest.mark.parametrize(
    ("data", "result"),
    (
      TestData("+1\n+1\n+1\n", 3),
      TestData("+1\n+1\n-2\n", 0),
      TestData("-1\n-2\n-3\n", -6),
    )
)
def test_part1(data, result):
    assert part1(data) == result

ans = part1(data)
print(ans)
#submit(ans, part='a', day=1, year=2018)

def part2(data:str) -> int:
    val = 0
    seen = {val}
    while True:
        for line in data.splitlines():
            val += int(line)
            if val in seen:
                return val
            else:
                seen.add(val)

@pytest.mark.parametrize(
    ("data", "result"),
    (
      TestData("+1\n-1\n", 0),
      TestData("+3\n+3\n+4\n-2\n-4\n", 10),
      TestData("-6\n+3\n+8\n+5\n-6\n",5),
      TestData("+7\n+7\n-2\n-7\n-4\n",14),
    )
)
def test_part2(data, result):
    assert part2(data) == result

ans = part2(data)
print(ans)
submit(ans, part='b', day=1, year=2018)

