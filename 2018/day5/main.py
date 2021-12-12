from aocd import submit, get_data

data = get_data(day=5, year=2018)

alpha = "abcdefghijklmnopqrstuvwxyz"
ans = 1e5
M = {}
for c in alpha:
    M[c.lower()] = c.upper()
    M[c.upper()] = c.lower()

for rem in alpha:
    s2 = [c for c in data if c!=rem.lower() and c!=rem.upper()]
    stack = []
    for c in s2:
        if stack and c == M[stack[-1]]:
            stack.pop()
        else:
            stack.append(c)
    ans = min(ans, len(stack))
print(ans)
submit(ans, part='b', day=5, year=2018)
