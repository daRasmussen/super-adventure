from aocd import submit, get_data
from collections import deque

data = get_data(day=10, year=2021)

ans = 0
for line in data.split("\n"):
    S = deque()
    for c in line.strip():
        if c in ["(", "[", "{", "<"]:
            S.append(c)
        elif c == ")":
            if S[-1] != "(":
                ans += 3
                break
            else:
                S.pop()
        elif c == "]":
            if S[-1] != "[":
                ans += 57
                break
            else:
                S.pop()
        elif c == "}":
            if S[-1] != "{":
                ans += 1197
                break
            else:
                S.pop()
        elif c == ">":
            if S[-1] != "<":
                ans += 25137
                break
            else:
                S.pop()

print(ans)
submit(ans, part='a', day=10, year=2021)

# submit(ans, part='b', day=10, year=2021)
