from aocd import submit, get_data
from collections import Counter

data = get_data(day=14, year=2021)

S, rules = data.split("\n\n")

R = {}
for rule in rules.split("\n"):
    start, end = rule.split(" -> ")
    R[start] = end
for t in range(10):
    T = ""
    for i in range(len(S)):
        T += S[i]
        if i+1 < len(S):
            T += R[S[i]+S[i+1]]
    S = T
C = Counter(S)
ans = max(C.values())-min(C.values())
print(ans)
submit(ans, part='a', day=14, year=2021)
# submit(ans, part='b', day=14, year=2021)
