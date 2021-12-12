from aocd import submit, get_data
from collections import defaultdict

data = get_data(day=6, year=2018)

P = []

for line in data.splitlines():
    x, y = [int(s.strip()) for s in line.split(",")]
    P.append((x, y))

x_lo = min([x for x,_ in P])
x_hi = max([x for x,_ in P])
y_lo = min([y for _,y in P])
y_hi = max([y for _,y in P])

def d(p1, p2):
    x, y = p1
    r, c = p2
    return abs(x-r) + abs(y-c)

def closest(r, c):
    best = P[0]
    xx, yy = best
    tie = False
    for p in P[1:]:
        x, y = p
        if d((x,y), (r,c)) < d((xx,yy), (r,c)):
            best = p
            tie = False
        elif d((x,y), (r,c)) == d((xx,yy), (r,c)):
            tie = True
    if tie:
        return (-1, 1)
    else:
        return best


score = defaultdict(int)
for x in range(x_lo, x_hi+1):
    for y in range(y_lo, y_hi + 1):
        score[closest(x, y)] += 1


is_inf = set()
for r in range(500):
    for c in [-5000, 5000]:
        is_inf.add(closest(r, c))

for c in range(500):
    for r in [-5000, 5000]:
        is_inf.add(closest(r, c))

best = None
for k in score:
    if k not in is_inf and (best is None or score[k] > score[best]):
        x, y = k
        best = (x, y)

ans = score[best]
print(ans)
submit(ans, part='a', day=6, year=2018)
# submit(ans, part='b', day=6, year=2018)
