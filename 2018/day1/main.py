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
def test(data, result):
    assert part1(data) == result

ans = part1(data)
print(ans)
#submit(ans, part='a', day=1, year=2018)


#submit(ans, part='b', day=1, year=2018)

