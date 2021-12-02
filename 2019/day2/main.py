with open('data.txt') as f:
    d = f.readlines()
    d = [x.strip() for x in d]
    li = d[0].split(",")
    li = [int(x) for x in li]
    #li = [1,9,10,3,2,3,11,0,99,30,40,50]
    li[1] = 12
    li[2] = 2
t = []
for l in li:
    if len(t) != 4:
        t.append(l)
        if len(t) == 4:
            i, a, b, o = t[0], t[1], t[2], t[3]
            if i == 1:
                li[o] = li[a] + li[b]
            if i == 2:
                li[o] = li[a] * li[b]
            if i == 99:
                break
    else:
        t = [l]
print(li)
