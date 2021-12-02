import re
with open('data.txt') as f:
    d = f.readlines()
    d = [x.strip() for x in d]
    pattern = re.compile(r"(\w)(\d+)")
    cabels = []
    for cabel in d:
        nodes = cabel.split(",")
        tmp = []
        for node in nodes:
            res = pattern.match(node).groups()
            tmp.append({
                "direction": res[0],
                "value": int(res[1])
            })
        cabels.append(tmp)
coords = []
for c in cabels:
    pos = [0, 0]
    tmp = [pos]
    for n in c:
        direction, value = n.values()
        t = [tmp[-1][0], tmp[-1][1]]
        if direction == 'L':
            t[0] -= value
        if direction == 'R':
            t[0] += value
        if direction == 'U':
            t[1] += value
        if direction == 'D':
            t[1] -= value
        tmp.append(t)
    coords.append(tmp)

for path in coords:
    for index, coord in enumerate(path):
        k1, k2 = path[index], path[index+1 if index + 1 < len(path) else index]
        x1, y1 = k1[0], k1[1]
        x2, y2 = k2[0], k2[1]
        if x1 != x2 or y1 != y2:
            print(x1, x2, y1, y2)
        #print(x1, y1, x2, y2)
