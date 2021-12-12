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

for k in E:
    E[k] = sorted(E[k])

t = 0
EV = []
Q = []

def add_task(x):
    Q.append(x)
def start_work():
    global Q
    while len(EV) < 5 and Q:
        x = min(Q)
        Q = [y for y in Q if y != x]
        EV.append((t + 61 + ord(x) - ord("A"), x))

for k in E:
    if D[k] == 0:
        add_task(k)
start_work()

while EV or Q:
    t, x = min(EV)
    EV = [y for y in EV if y!=(t,x)]
    for y in E[x]:
        D[y] -= 1
        if D[y] == 0:
            add_task(y)
    start_work()
ans = t
print(ans)
submit(ans, part='b', day=7, year=2018)
