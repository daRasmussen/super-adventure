infile = "data.txt"
G = {}
for line in open(infile):
    start, end = line.split("->")
    x1, y1 = start.split(",")
    x2, y2 = end.split(",")
    x1 = int(x1.strip())
    x2 = int(x2.strip())
    y1 = int(y1.strip())
    y2 = int(y2.strip())
    dx = x2-x1
    dy = y2-y1
    for i in range(1 + max(abs(dx), abs(dy))):
        x = x1 + (1 if dx>0 else (-1 if dx<0 else 0)) * i
        y = y1 + (1 if dy>0 else (-1 if dy<0 else 0)) * i
        if (x,y) not in G:
            G[(x,y)] = 0
        G[(x,y)] += 1

ans = 0
for k in G:
    if G[k] > 1:
        ans += 1
print('\n')
print(ans)

