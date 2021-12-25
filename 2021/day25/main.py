from aocd import submit, get_data

data = get_data(day=25, year=2021)
ans = ''
import numpy as np

def step(a: np.ndarray) -> bool:
    moved = 0
    for (aVal, ax) in [(1, 1), (2, 0)]:
        coords = np.where((np.roll(a, -1, ax) == 0) & (a == aVal))
        moved += coords[0].size
        a[coords] = 0
        a[tuple((c + 1) % (a.shape[axis]) if axis == ax else c
                for (axis, c) in  enumerate(coords))] = aVal
    return moved > 0

a = np.array([[1 if c == '>' else (2 if c == 'v' else 0) 
    for c in l.strip()]
    for l in data.splitlines()])

i = 1
while step(a): i += 1
ans = i
print(ans)
submit(ans, part='a', day=25, year=2021)
# submit(ans, part='b', day=25, year=2021)
