file = 'data.txt'
X =[int(x) for x in open(file).read().strip().split(",")]
for _ in range(80):
    Y = []
    for x in X:
        if x == 0:
            Y.append(6)
            Y.append(8)
        else:
            Y.append(x-1)
    X = Y
print(len(X))
