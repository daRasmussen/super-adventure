from collections import defaultdict

file = 'data.txt'
N =[int(x) for x in open(file).read().strip().split(",")]

X = defaultdict(int)
for n in N:
    if n not in X:
        X[n] = 0
    X[n] += 1

for day in range(256):
    Y = defaultdict(int)
    for x,cnt in X.items():
        if x == 0:
            Y[6] += cnt
            Y[8] += cnt
        else:
            Y[x-1] += cnt
    X = Y
print(sum(X.values()))
