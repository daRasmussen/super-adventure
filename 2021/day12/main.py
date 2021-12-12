from aocd import submit, get_data
from collections import defaultdict, namedtuple, deque

import pytest

data = get_data(day=12, year=2021)
print("\n")

def part2(data):
    print(data)
    E = defaultdict(list)
    for line in data.splitlines():
        a, b = line.strip().split("-")
        E[a].append(b)
        E[b].append(a)
    start = ("start", set(["start"]), None)
    Q = deque([start])
    ans = 0
    while Q:
        pos, small, twice = Q.popleft()
        if pos == "end":
            ans += 1
        for y in E[pos]:
            if y not in small:
                new_small = set(small)
                if y.lower() == y:
                    new_small.add(y)
                Q.append((y, new_small, twice))
            elif y in small and twice is None and y not in ["start", "end"]:
                Q.append((y, small, y))
    return ans

ans = part2(data)
submit(ans, part='b', day=12, year=2021)
