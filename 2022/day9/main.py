from aocd import submit, get_data
from collections import deque

data = get_data(day=9, year=2021)
G = [[int(x) for x in line.strip()] for line in data.split("\n")]

R = len(G)
C = len(G[0])
DR = [-1, 0, 1, 0]
DC = [0, 1, 0, -1]
ans = 0
for r in range(R):
    for c in range(C):
        ok = True
        for d in range(4):
            rr = r+DR[d]
            cc = c+DC[d]
            if 0<=rr<R and 0<=cc<C and G[rr][cc]<=G[r][c]:
                ok = False
        if ok:
            ans += G[r][c] + 1
             
# submit(ans, part='a', day=9, year=2021)
S = []
SEEN = set()
for r in range(R):
    for c in range(C):
        if (r,c) not in SEEN and G[r][c]!=9:
            size = 0
            Q = deque()
            Q.append((r,c))
            while Q:
                (r,c) = Q.popleft()
                if (r,c) in SEEN:
                    continue
                SEEN.add((r,c))
                size += 1
                for d in range(4):
                    rr = r+DR[d]
                    cc = c+DC[d]
                    if 0<=rr<R and 0<=cc<C and G[rr][cc]!=9:
                        Q.append((rr,cc))
            S.append(size)
S.sort()
ans = S[-1]*S[-2]*S[-3]
# submit(ans, part='b', day=9, year=2021)
