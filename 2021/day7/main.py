from aocd import get_data, submit

data = get_data(day=7, year=2021)

X = [int(x) for x in data.split(",")]
X.sort()
def C2(d):
    return d*(d+1)/2
best = 1e9
for med in range(2000):
    score = 0
    for x in X:
        d = abs(x-med)
        score += C2(d)
    if score < best:
        best = score
submit(int(best), part="b", day=7, year=2021)
