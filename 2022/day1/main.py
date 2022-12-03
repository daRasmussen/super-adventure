X = [l.strip() for l in open("data.txt")]

Q = []
for e in ("\n".join(X)).split("\n\n"):
    q = 0
    for x in e.split("\n"):
        q += int(x)
    Q.append(q)
Q = sorted(Q)
print(Q[-1])
print(Q[-1]+Q[-2]+Q[-3])
