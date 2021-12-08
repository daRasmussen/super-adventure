from aocd import get_data, submit
from collections import defaultdict

data = get_data(day=8, year=2021).split("\n")
ans = 0
for line in data:
    before, after = line.split("|")
    before = before.split()
    after = after.split()
    by_len = defaultdict(list)
    for w in before:
        by_len[len(w)].append(w)
    for w in after:
        if len(by_len[len(w)]) == 1:
            ans += 1
submit(ans, part="a", day=8, year=2021)
