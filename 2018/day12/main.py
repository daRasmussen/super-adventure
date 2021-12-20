import numpy as np
from aocd import submit, get_data

data = get_data(day=12, year=2018)

def string_to_list(s):
    return [int(c == "#") for c in s]


def list_to_string(l):
    return "".join(["#" if x else "." for x in l])

lines = data.splitlines()
garden1 = lines[0].split()[2]
garden1 = string_to_list(garden1)
garden2 = list(garden1)
previous, current = garden1, garden2
patterns = {}
offset = 0
for i in range(2, len(lines)):
    before, after = lines[i].split(" => ")
    patterns[before] = int(after == "#")

for gen in range(20):
    previous = [0] * 5 + previous + [0] * 5
    current = [0] * 5 + current + [0] * 5
    offset += 5

    for i in range(2, len(previous) - 3):
        pattern = list_to_string(previous[i - 2 : i + 3])
        current[i] = patterns[pattern] if pattern in patterns else 0

    current = np.trim_zeros(current, "f")
    offset -= len(previous) - len(current)
    current = np.trim_zeros(current, "b")
    previous = list(current)
res = 0
for i in range(len(current)):
    if current[i]:
        res += i - offset
ans = res
print(ans)
submit(ans, part='a', day=12, year=2018)
# submit(ans, part='b', day=12, year=2018)
