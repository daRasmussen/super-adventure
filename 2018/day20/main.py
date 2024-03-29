from collections import defaultdict
from aocd import submit, get_data

data = get_data(day=20, year=2018)
ans = ''

f=data
dd={"N":(0,-1),"E":(1,0),"S":(0,1),"W":(-1,0)}
p=[]
px,py=x,y=0,0
d=defaultdict(int)
for c in f[1:-2]:
 if c=="(":
  p.append((x, y))
 elif c==")":
  x,y=p.pop()
 elif c=="|":
  x,y=p[-1]
 else:
  dx,dy=dd[c]
  x+=dx
  y+=dy
  d[x,y]=min(d[x,y],d[px,py]+1) if d[x,y] else d[px,py]+1
 px,py=x,y
dv=d.values()
ans = len([x for x in dv if x>=1000])
print(ans)
submit(ans, part='b', day=20, year=2018)
