from aocd import submit, get_data
from collections import defaultdict, namedtuple, deque

import pytest

data = get_data(day=12, year=2021)
print("\n")
TestData = namedtuple("TestData", ["data", "result"])
TestData.__test__ = False # type: ignore

def get_data(filename):
    with open(filename) as f:
        return f.read()

test1 = get_data("test1.txt")
test2 = get_data("test2.txt")
test3 = get_data("test3.txt")

@pytest.mark.parametrize(
    ("data", "result"),
    (
        TestData(test1, 10),
        TestData(test2, 19),
        TestData(test3, 226)
    )
)

def test_part1(data, result):
    assert part1(data) == result

def part1(data):
    print(data)
    E = defaultdict(list)
    for line in data.splitlines():
        a, b = line.strip().split("-")
        E[a].append(b)
        E[b].append(a)
    start = ("start", set(["start"]))
    Q = deque([start])
    ans = 0
    while Q:
        pos, small = Q.popleft()
        if pos == "end":
            ans += 1
        for y in E[pos]:
            if y not in small:
                new_small = set(small)
                if y.lower() == y:
                    new_small.add(y)
                Q.append((y, new_small))
    return ans

ans = part1(data)
print(ans)
submit(ans, part='a', day=12, year=2021)

ans = ""
# submit(ans, part='b', day=12, year=2021)
