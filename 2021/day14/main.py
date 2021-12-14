from aocd import submit, get_data
from collections import Counter

data = get_data(day=14, year=2021)

S, rules = data.split("\n\n")

R = {}
for rule in rules.split("\n"):
    start, end = rule.split(" -> ")
    R[start] = end
C1 = Counter()
for i in range(len(S)-1):
    C1[S[i]+S[i+1]] += 1
ans = 0
for t in range(41):
    if t in [10,40]:
        CF = Counter()
        for k in C1:
            CF[k[0]] += C1[k]
        CF[S[-1]] += 1
        ans = max(CF.values())-min(CF.values())
        print(ans)
    C2 = Counter()
    for k in C1:
        C2[k[0]+R[k]] += C1[k]
        C2[R[k]+k[1]] += C1[k]
    C1 = C2
print(ans)
submit(ans, part='b', day=14, year=2021)
