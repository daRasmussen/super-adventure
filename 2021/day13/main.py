from aocd import submit, get_data
import itertools
from collections import defaultdict, Counter, deque

data = get_data(day=13, year=2021)
ans = 0

G = {}
for line in data.splitlines():
    line = line.strip()
    if line and line.startswith("fold"):
        G2 = {}
        for (x, y) in G:
            if x < 655:
                G2[(x, y)] = True
            else:
                G2[(655-(x-655), y)] = True
        print(len(G2))
        ans = len(G2)
    elif line:
       x, y = [int(v) for v in line.strip().split(",")]
       G[(x, y)] = True

print(ans)
submit(ans, part='a', day=13, year=2021)
# submit(ans, part='b', day=13, year=2021)
