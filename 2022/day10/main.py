from aocd import submit, get_data
from collections import deque

data = get_data(day=10, year=2021)

SCORES = []
ans = 0
for line in data.split("\n"):
    bad = False
    S = deque()
    for c in line.strip():
        if c in ["(", "[", "{", "<"]:
            S.append(c)
        elif c == ")":
            if S[-1] != "(":
                ans += 3
                bad = True
                break
            else:
                S.pop()
        elif c == "]":
            if S[-1] != "[":
                ans += 57
                bad = True
                break
            else:
                S.pop()
        elif c == "}":
            if S[-1] != "{":
                ans += 1197
                bad = True
                break
            else:
                S.pop()
        elif c == ">":
            if S[-1] != "<":
                ans += 25137
                bad = True
                break
            else:
                S.pop()
    if not bad:
        score = 0
        P = {"(": 1, "[": 2, "{": 3, "<": 4}
        for c in reversed(S):
            score = score * 5 + P[c]
        SCORES.append(score)
SCORES.sort()
ans = SCORES[len(SCORES)//2]
print(ans)
submit(ans, part='b', day=10, year=2021)
