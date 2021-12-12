from aocd import submit, get_data
from collections import defaultdict

data = get_data(day=3, year=2018)
print("\n")
C = defaultdict(int)
for line in data.splitlines():
    words = line.split()
    x, y = words[2].split(",")
    x, y = int(x), int(y[:-1])
    w, h = words[3].split("x")
    w, h = int(w), int(h)
    for dx in range(w):
        for dy in range(h):
            C[(x+dx, y+dy)] += 1
ans = 0
for (r, c),v in C.items():
    if v >= 2:
        ans += 1
print(ans)
submit(ans, part='a', day=3, year=2018)
# submit(ans, part='b', day=3, year=2018)
