from aocd import submit, get_data
from collections import defaultdict, deque

data = get_data(day=7, year=2018)

E = defaultdict(list)
D = defaultdict(int)
for line in data.splitlines():
    words = line.split()
    x = words[1]
    y = words[7]
    E[x].append(y)
    D[y] += 1

Q = []
for k in E:
    if D[k] == 0:
        Q.append(k)
ans = ""
while Q:
    x = sorted(Q)[0]
    Q = [y for y in Q if y != x]
    ans += x
    for y in E[x]:
        D[y] -= 1
        if D[y] == 0:
            Q.append(y)
print(ans)
submit(ans, part='a', day=7, year=2018)
# submit(ans, part='b', day=7, year=2018)
