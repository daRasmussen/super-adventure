from aocd import submit, get_data

data = get_data(day=5, year=2018)

M = {}
for c in "abcdefghijklmnopqrstuvwxyz":
    M[c.lower()] = c.upper()
    M[c.upper()] = c.lower()

stack = []
for c in data:
    if stack and c == M[stack[-1]]:
        stack.pop()
    else:
        stack.append(c)

ans = len(stack)
print(ans)
submit(ans, part='a', day=5, year=2018)
# submit(ans, part='b', day=5, year=2018)
