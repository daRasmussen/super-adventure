from aocd import get_data, submit

data = get_data(day=7, year=2021)

X = [int(x) for x in data.split(",")]
X.sort()
ans = 0
med = X[len(X)//2]
for x in X:
    ans += abs(x-med)
submit(ans, part="a", day=7, year=2021)
